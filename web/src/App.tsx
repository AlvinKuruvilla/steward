/**
 * The shell. One column of repositories, one of work, and a header thin enough
 * that the queue starts near the top of the window.
 *
 * Density is GitHub's: 1px rules between rows rather than gaps, no card around
 * anything that belongs in a list. Calm is OpenWork's: a soft outer shell, a
 * near-flat interior, and colour reserved for state.
 */
import { useQuery } from "@tanstack/react-query";
import { NavLink, Outlet, useParams } from "react-router";

import { get, type Repository } from "@/api";
import { AddRepository } from "@/components/add-repository";
import { Avatar } from "@/components/avatar";
import { Mark } from "@/components/mark";
import { Shortcuts } from "@/components/shortcuts";
import { ThemeToggle } from "@/components/theme-toggle";

// The window is the shell. A centred card would leave a third of a wide
// monitor empty and make the queue narrower the bigger the screen gets.
export default function App() {
  const { owner, name } = useParams();
  const { data: repositories } = useQuery({
    queryKey: ["repositories"],
    queryFn: () => get<Repository[]>("/api/repositories"),
    refetchInterval: (query) =>
      query.state.data?.some((r) => r.syncing) ? 1000 : false,
  });

  const selected =
    repositories?.find((r) => r.owner === owner && r.name === name) ??
    repositories?.[0];

  return (
    <div className="h-screen bg-background">
      <div className="grid h-full grid-cols-[14rem_minmax(0,1fr)]">
        <Sidebar repositories={repositories} selected={selected} />

        <div className="flex min-w-0 flex-col overflow-hidden bg-background">
          <header className="flex h-13 shrink-0 items-center justify-between gap-6 border-b border-border px-6 py-3">
            <div className="flex min-w-0 items-center gap-3">
              <h1 className="flex min-w-0 items-center gap-2 font-mono text-[13px] text-foreground">
                {selected ? (
                  <>
                    <Avatar login={selected.owner} size={18} />
                    <span className="truncate">
                      {selected.owner}/{selected.name}
                    </span>
                  </>
                ) : (
                  "Steward"
                )}
              </h1>
              <SyncState repository={selected} />
            </div>
            <div className="flex shrink-0 items-center gap-1">
              <Shortcuts />
              <AddRepository />
            </div>
          </header>

          <main className="min-w-0 flex-1 overflow-y-auto px-8 py-6">
            {/* The chrome fills the window; the reading column does not, so a
                title never runs the width of a 32-inch monitor. */}
            <div className="mx-auto max-w-[68rem]">
              <Outlet context={selected} />
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

function Sidebar({
  repositories,
  selected,
}: {
  repositories: Repository[] | undefined;
  selected: Repository | undefined;
}) {
  return (
    <aside className="flex flex-col gap-1 bg-sidebar px-3 py-4">
      <div className="flex items-center gap-2 px-2 pt-1 pb-4">
        <Mark />
        <span className="text-[13px] font-semibold tracking-[-0.01em] text-foreground">
          Steward
        </span>
        <span className="ml-auto">
          <ThemeToggle />
        </span>
      </div>

      <span className="px-2 pb-1.5 text-[11px] font-medium tracking-[0.08em] text-muted-foreground uppercase">
        Repositories
      </span>

      <nav className="flex flex-col gap-px">
        {repositories?.map((repository) => (
          <NavLink
            key={`${repository.owner}/${repository.name}`}
            to={`/${repository.owner}/${repository.name}`}
            className={() =>
              [
                "group flex h-8 items-center gap-2 rounded-md px-2",
                "text-[13px] transition-colors duration-100",
                repository === selected
                  ? "bg-background font-medium text-foreground shadow-[0_1px_2px_rgb(0_0_0/0.06)] ring-1 ring-border"
                  : "text-muted-foreground hover:bg-muted",
              ].join(" ")
            }
          >
            <span className="truncate">{repository.name}</span>
            {repository.syncing ? (
              <span className="ml-auto font-mono text-[11px] tabular-nums text-[var(--color-attention)]">
                {repository.pull_requests_read}
              </span>
            ) : null}
          </NavLink>
        ))}
      </nav>

      {repositories?.length === 0 ? (
        <p className="px-2 text-[13px] leading-relaxed text-muted-foreground">
          Nothing synced. Give Steward a repository and it reads the pull request
          history into an event log.
        </p>
      ) : null}

    </aside>
  );
}

function SyncState({ repository }: { repository: Repository | undefined }) {
  if (!repository) return null;

  if (repository.sync_error) {
    return (
      <span className="text-xs text-destructive">
        {repository.sync_error}
      </span>
    );
  }

  if (repository.syncing) {
    return (
      <span className="flex items-baseline gap-1.5 text-xs text-muted-foreground">
        <span className="size-1.5 translate-y-[-1px] animate-pulse rounded-full bg-[var(--color-attention)]" />
        reading
        <span className="font-mono tabular-nums text-foreground">
          {repository.pull_requests_read}
        </span>
        pull requests
      </span>
    );
  }

  if (!repository.last_sync) return null;

  return (
    <span className="text-xs text-muted-foreground">
      synced{" "}
      <time dateTime={repository.last_sync}>
        {new Date(repository.last_sync).toLocaleString(undefined, {
          month: "short",
          day: "numeric",
          hour: "2-digit",
          minute: "2-digit",
        })}
      </time>
    </span>
  );
}
