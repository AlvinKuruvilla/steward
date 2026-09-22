import type { BlockedOn, Derivation, WorkflowState } from "@/api";

/**
 * A state, and where the answer came from.
 *
 * The derivation class is never hidden and never inferred, which is what makes
 * the queue auditable rather than something to trust. UNKNOWN is the quietest
 * mark on the row: it is an absence of evidence, and it should not read as an
 * alert.
 */
const tone: Record<WorkflowState, string> = {
  DRAFT: "var(--color-draft)",
  UNTRIAGED: "var(--color-draft)",
  REVIEW_WAIT: "var(--color-attention)",
  RE_REVIEW_WAIT: "var(--color-attention)",
  CHANGES_REQUESTED: "var(--color-closed)",
  APPROVED: "var(--color-open)",
  MERGED: "var(--color-merged)",
  CLOSED: "var(--color-closed)",
};

const spoken: Record<WorkflowState, string> = {
  DRAFT: "draft",
  UNTRIAGED: "untriaged",
  REVIEW_WAIT: "review",
  RE_REVIEW_WAIT: "re-review",
  CHANGES_REQUESTED: "changes",
  APPROVED: "approved",
  MERGED: "merged",
  CLOSED: "closed",
};

export function StateMark({
  state,
  blockedOn,
  derivation,
}: {
  state: WorkflowState;
  blockedOn: BlockedOn;
  derivation: Derivation;
}) {
  return (
    <span
      className="flex items-baseline gap-2"
      title={`${state} · blocked on ${blockedOn} · ${derivation}`}
    >
      <span
        aria-hidden
        className="size-1.5 translate-y-[-1px] rounded-full"
        style={{ background: tone[state] }}
      />
      <span className="derived text-[12px]" style={{ color: tone[state] }}>
        {spoken[state]}
      </span>
      {derivation === "UNKNOWN" ? (
        <span className="text-[11px] text-[var(--color-muted)] opacity-70">
          no evidence
        </span>
      ) : derivation === "POLICY" ? (
        <span className="text-[11px] text-[var(--color-muted)]">by rule</span>
      ) : null}
    </span>
  );
}
