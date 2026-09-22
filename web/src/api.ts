/** The shapes /api returns. Mirrors src/steward/api.py. */

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

export async function get<T>(path: string): Promise<T> {
  const response = await fetch(path);
  if (!response.ok) {
    const body = (await response.json().catch(() => null)) as {
      detail?: string;
    } | null;
    throw new Error(body?.detail ?? `${response.status} from ${path}`);
  }
  return (await response.json()) as T;
}

export async function post<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(path, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    const problem = (await response.json().catch(() => null)) as {
      detail?: string;
    } | null;
    throw new Error(problem?.detail ?? `${response.status} from ${path}`);
  }
  return (await response.json()) as T;
}

/** Whole days since `when`, which is the only precision a queue needs. */
export function daysSince(when: string): number {
  const elapsed = Date.now() - new Date(when).getTime();
  return Math.floor(elapsed / 86_400_000);
}
