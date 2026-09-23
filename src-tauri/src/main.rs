//! The desktop shell: a window around the interface, and the Python backend it
//! talks to.
//!
//! At launch the shell makes a token, starts `steward serve` with it, and waits
//! for the backend's handshake on stdout:
//!
//! ```text
//! shell                                   steward serve --watch-stdin
//!   |  spawn, STEWARD_API_TOKEN=<token>  ->  |
//!   |                                        |  binds 127.0.0.1:0
//!   |  <- {"steward":"listening","port":N}   |  (first and only stdout line)
//!   |                                        |
//! window                                     |
//!   |  invoke("backend") -> {url, token}     |
//!   |  fetch(url + /api/..., Bearer token) ------------------------------>  |
//!   |                                        |
//!   |  quit: kill child; crash: stdin EOF -> |  exits
//! ```
//!
//! The token is what keeps other local processes out: the backend listens on
//! loopback, which every process on the machine shares. It lives only in this
//! process, the backend's environment, and the page's memory, and is never
//! logged.
//!
//! In a debug build the backend is the repository's own, run through `uv`, with
//! its database in the repository's `tmp/data` so development never touches an
//! installed copy's data.

#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::sync::Mutex;
use std::time::Duration;

use serde::{Deserialize, Serialize};
use tauri::{AppHandle, Manager, RunEvent, State};
use tauri_plugin_shell::ShellExt;
use tauri_plugin_shell::process::{CommandChild, CommandEvent};
use tokio::sync::watch;

/// Where the page sends requests, and what it must send with them.
#[derive(Clone, Serialize)]
struct Backend {
    url: String,
    token: String,
}

#[derive(Clone)]
enum Status {
    Starting,
    Ready(Backend),
    Failed(String),
}

/// The backend's status, which the `backend` command waits on, and its process,
/// which the shell kills on quit.
struct Sidecar {
    status: watch::Receiver<Status>,
    child: Mutex<Option<CommandChild>>,
}

#[derive(Deserialize)]
struct Handshake {
    steward: String,
    port: u16,
}

/// Long enough for `uv run` to resolve the environment and the backend to
/// migrate on a cold start; short enough that a backend that will never answer
/// is reported rather than waited on. Arbitrary.
const STARTUP_TIMEOUT: Duration = Duration::from_secs(30);

/// Where the page finds the backend. Waits while it is starting.
#[tauri::command]
async fn backend(sidecar: State<'_, Sidecar>) -> Result<Backend, String> {
    let mut status = sidecar.status.clone();
    let settled = tokio::time::timeout(
        STARTUP_TIMEOUT,
        status.wait_for(|s| !matches!(s, Status::Starting)),
    )
    .await
    .map_err(|_| "the backend did not start within 30 seconds".to_string())?
    .map_err(|_| "the backend's supervisor has gone".to_string())?
    .clone();
    match settled {
        Status::Ready(backend) => Ok(backend),
        Status::Failed(why) => Err(why),
        Status::Starting => unreachable!("wait_for returned on a settled status"),
    }
}

/// 32 bytes from the OS, as hex.
fn token() -> String {
    let mut bytes = [0u8; 32];
    getrandom::fill(&mut bytes).expect("the OS random source is available");
    bytes.iter().map(|b| format!("{b:02x}")).collect()
}

fn start_backend(app: &AppHandle) -> Result<Sidecar, Box<dyn std::error::Error>> {
    let token = token();

    #[cfg(debug_assertions)]
    let (command, data_dir) = {
        let repository = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .parent()
            .expect("src-tauri sits inside the repository")
            .to_path_buf();
        let command = app
            .shell()
            .command("uv")
            .args(["run", "steward", "serve"])
            .current_dir(&repository);
        (command, repository.join("tmp").join("data"))
    };

    // TODO(alvin): bundle the frozen backend through `externalBin` in
    // tauri.conf.json. Until then a release build starts, finds no sidecar, and
    // the interface reports the failure.
    #[cfg(not(debug_assertions))]
    let (command, data_dir) = (
        app.shell().sidecar("steward")?.args(["serve"]),
        app.path().app_data_dir()?,
    );

    let (mut events, child) = command
        .args(["--watch-stdin", "--data-dir"])
        .arg(&data_dir)
        .env("STEWARD_API_TOKEN", &token)
        .spawn()?;

    let (report, status) = watch::channel(Status::Starting);
    tauri::async_runtime::spawn(async move {
        while let Some(event) = events.recv().await {
            match event {
                CommandEvent::Stdout(line) => {
                    let handshake = serde_json::from_slice::<Handshake>(&line)
                        .ok()
                        .filter(|h| h.steward == "listening");
                    match handshake {
                        Some(h) if matches!(*report.borrow(), Status::Starting) => {
                            let _ = report.send(Status::Ready(Backend {
                                url: format!("http://127.0.0.1:{}", h.port),
                                token: token.clone(),
                            }));
                        }
                        // The backend writes nothing else to stdout, so anything
                        // here is a bug in it; show it rather than drop it.
                        _ => eprintln!("backend stdout: {}", String::from_utf8_lossy(&line)),
                    }
                }
                CommandEvent::Stderr(line) => {
                    eprintln!("{}", String::from_utf8_lossy(&line).trim_end());
                }
                CommandEvent::Error(error) => eprintln!("backend: {error}"),
                CommandEvent::Terminated(exit) => {
                    let _ = report.send(Status::Failed(format!(
                        "the backend exited (code {:?}, signal {:?}); its stderr is in the terminal",
                        exit.code, exit.signal
                    )));
                }
                _ => {}
            }
        }
    });

    Ok(Sidecar {
        status,
        child: Mutex::new(Some(child)),
    })
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            let sidecar = start_backend(app.handle())?;
            app.manage(sidecar);
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![backend])
        .build(tauri::generate_context!())
        .expect("tauri.conf.json and the bundled interface are valid")
        .run(|app, event| {
            // The shell plugin kills only the children it spawned for the page,
            // not ones started from Rust. Dropping the child also closes the
            // backend's stdin, which is what stops a `uv run` grandchild.
            if let RunEvent::Exit = event {
                let sidecar = app.state::<Sidecar>();
                let child = sidecar.child.lock().expect("no panic while held").take();
                if let Some(child) = child {
                    let _ = child.kill();
                }
            }
        });
}
