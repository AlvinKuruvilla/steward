/**
 * Steward's mark: an event log read left to right, with the one row that is
 * still open drawn open. Geometric, monochrome, and the same shape at 16px as
 * at 64px.
 */
export function Mark({ size = 18 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden
      className="shrink-0"
    >
      <rect x="2" y="4" width="20" height="4" rx="1.25" className="fill-foreground" />
      <rect x="2" y="10" width="14" height="4" rx="1.25" className="fill-foreground/55" />
      <rect
        x="2.75"
        y="16.75"
        width="12.5"
        height="4.5"
        rx="1.5"
        className="stroke-foreground/45"
        strokeWidth="1.5"
      />
    </svg>
  );
}
