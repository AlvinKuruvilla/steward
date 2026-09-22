import type { BlockedOn, Derivation, WorkflowState } from "@/api";

/**
 * A state, who holds it, and where the answer came from. 0002: the derivation
 * class is always shown, never inferred and never hidden, and UNKNOWN is the
 * quietest thing on the screen because it is an absence of evidence.
 */
const colors: Record<WorkflowState, string> = {
  DRAFT: "var(--color-state-draft)",
  UNTRIAGED: "var(--color-state-draft)",
  REVIEW_WAIT: "var(--color-state-attention)",
  RE_REVIEW_WAIT: "var(--color-state-attention)",
  CHANGES_REQUESTED: "var(--color-state-closed)",
  APPROVED: "var(--color-state-open)",
  MERGED: "var(--color-state-merged)",
  CLOSED: "var(--color-state-closed)",
};

export function StateChip({
  state,
  blockedOn,
  derivation,
}: {
  state: WorkflowState;
  blockedOn: BlockedOn;
  derivation: Derivation;
}) {
  return (
    <span className="derived flex items-center gap-2">
      <span style={{ color: colors[state] }}>{state}</span>
      <span className="text-[var(--color-secondary)]">·</span>
      <span className="text-[var(--color-secondary)]">{blockedOn}</span>
      <span className="text-[var(--color-secondary)]">·</span>
      <span
        className={
          derivation === "UNKNOWN"
            ? "text-[var(--color-state-draft)] opacity-60"
            : "text-[var(--color-secondary)]"
        }
      >
        {derivation}
      </span>
    </span>
  );
}
