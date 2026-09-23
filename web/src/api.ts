/** The shapes /api returns. Mirrors src/steward/api.py. */

import { invoke } from "@tauri-apps/api/core";

export type WorkflowState =
  | "DRAFT"
  | "UNTRIAGED"
  | "REVIEW_WAIT"
  | "CHANGES_REQUESTED"
  | "RE_REVIEW_WAIT"
  | "APPROVED"
  | "MERGED"
  | "CLOSED";

export type BlockedOn =
  | "AUTHOR"
  | "REVIEWER"
  | "MERGER"
  | "NOBODY"
  | "UNKNOWN";

export type Derivation = "EVENT" | "POLICY" | "UNKNOWN";

export interface Standing {
  number: number;
  title: string | null;
  state: WorkflowState;
  blocked_on: BlockedOn;
  derivation: Derivation;
  since: string;
  author: string | null;
  author_is_bot: boolean;
  labels: string[];
  comments: number;
  last_kind: string | null;
  last_actor: string | null;
  last_at: string | null;
}

export interface Repository {
  owner: string;
  name: string;
  last_sync: string | null;
  syncing: boolean;
  pull_requests_read: number;
  sync_error: string | null;
}

export interface Episode {
  start: string;
  end: string | null;
  state: WorkflowState;
  blocked_on: BlockedOn;
  derivation: Derivation;
}

export interface Moment {
  kind: string;
  occurred_at: string;
  actor: string | null;
  payload: Record<string, string | number | boolean>;
}

export interface PullRequest {
  standing: Standing;
  episodes: Episode[];
  events: Moment[];
}

/**
 * Where the backend is, and the token it wants. The desktop shell starts the
 * backend on a port the kernel picks and makes a token for this launch, so both
 * are asked for once and then reused.
 */
interface Backend {
  url: string;
  token: string;
}

let backend: Promise<Backend> | undefined;

function connection(): Promise<Backend> {
  // A failure is not kept: the shell may still be starting the backend, and
  // the next request should ask again rather than inherit this one's error.
  backend ??= invoke<Backend>("backend").catch((error: unknown) => {
    backend = undefined;
    throw error;
  });
  return backend;
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const { url, token } = await connection();
  const response = await fetch(url + path, {
    ...init,
    headers: { ...init.headers, authorization: `Bearer ${token}` },
  });
  if (!response.ok) {
    const problem = (await response.json().catch(() => null)) as {
      detail?: string;
    } | null;
    throw new Error(problem?.detail ?? `${response.status} from ${path}`);
  }
  return (await response.json()) as T;
}

export function get<T>(path: string): Promise<T> {
  return request<T>(path);
}

export function post<T>(path: string, body: unknown): Promise<T> {
  return request<T>(path, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
}

/**
 * How long ago, at whatever scale reads right.
 *
 * A queue is scanned, so every value is two characters and a unit: minutes
 * under an hour, hours under two days, then days. "0h" for a seven-minute
 * episode reads like a bug.
 */
export function since(when: string, until?: string | null): string {
  const end = until ? new Date(until).getTime() : Date.now();
  const minutes = Math.max(0, (end - new Date(when).getTime()) / 60_000);
  if (minutes < 60) return `${Math.round(minutes)}m`;
  if (minutes < 60 * 48) return `${Math.round(minutes / 60)}h`;
  return `${Math.round(minutes / 1440)}d`;
}

/** Where a pull request lives on GitHub. */
export function githubUrl(
  owner: string,
  name: string,
  number: number,
): string {
  return `https://github.com/${owner}/${name}/pull/${number}`;
}
