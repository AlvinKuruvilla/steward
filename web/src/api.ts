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
  state: WorkflowState;
  blocked_on: BlockedOn;
  derivation: Derivation;
  since: string;
  author: string | null;
}

export interface Repository {
  owner: string;
  name: string;
  last_sync: string | null;
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

/** Whole days since `when`, which is the only precision a queue needs. */
export function daysSince(when: string): number {
  const elapsed = Date.now() - new Date(when).getTime();
  return Math.floor(elapsed / 86_400_000);
}
