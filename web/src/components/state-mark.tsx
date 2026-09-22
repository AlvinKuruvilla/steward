import type { BlockedOn, Derivation, WorkflowState } from "@/api";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

/**
 * A state, and where the answer came from.
 *
 * The derivation class is never hidden and never inferred, which is what makes
 * the queue auditable rather than something to trust. UNKNOWN is the quietest
 * mark on the row: an absence of evidence should not read as an alert.
 */
const tone: Record<WorkflowState, string> = {
  DRAFT: "text-[var(--color-draft)]",
  UNTRIAGED: "text-[var(--color-draft)]",
  REVIEW_WAIT: "text-[var(--color-attention)]",
  RE_REVIEW_WAIT: "text-[var(--color-attention)]",
  CHANGES_REQUESTED: "text-[var(--color-closed)]",
  APPROVED: "text-[var(--color-open)]",
  MERGED: "text-[var(--color-merged)]",
  CLOSED: "text-[var(--color-closed)]",
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

const because: Record<Derivation, string> = {
  EVENT: "Derived from GitHub events alone.",
  POLICY: "Needed a rule from steward.toml.",
  UNKNOWN: "No event and no rule says who holds this.",
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
    <Tooltip>
      <TooltipTrigger
        render={
          <span className="inline-flex items-baseline gap-2 whitespace-nowrap" />
        }
      >
        <span className={cn("font-mono text-xs tabular-nums", tone[state])}>
          {spoken[state]}
        </span>
        <span
          className={cn(
            "text-[11px] text-muted-foreground",
            derivation === "UNKNOWN" && "opacity-70",
          )}
        >
          {derivation === "UNKNOWN"
            ? "no evidence"
            : derivation === "POLICY"
              ? "by rule"
              : blockedOn.toLowerCase()}
        </span>
      </TooltipTrigger>
      <TooltipContent>
        {state} · blocked on {blockedOn}. {because[derivation]}
      </TooltipContent>
    </Tooltip>
  );
}
