/**
 * An account's face: an author, or the owner standing in for a repository.
 *
 * Resolved by the API rather than by guessing a URL: `github.com/<login>.png`
 * covers people and not GitHub Apps, whose login carries a `[bot]` suffix that
 * belongs to no account -- and `github-actions` has no user page at all.
 * Initials when the account is gone or the lookup fails.
 */
import { useState } from "react";

export function Avatar({
  login,
  size = 20,
}: {
  login: string | null;
  size?: number;
}) {
  const [broken, setBroken] = useState(false);

  if (!login || broken) {
    return (
      <span
        aria-hidden
        className="inline-flex shrink-0 items-center justify-center rounded-full bg-muted text-[9px] font-medium text-muted-foreground"
        style={{ width: size, height: size }}
      >
        {(login ?? "?").slice(0, 1).toUpperCase()}
      </span>
    );
  }

  return (
    <img
      src={`/api/avatars/${encodeURIComponent(login)}`}
      alt=""
      width={size}
      height={size}
      loading="lazy"
      onError={() => setBroken(true)}
      className="shrink-0 rounded-full bg-muted ring-1 ring-black/5"
    />
  );
}
