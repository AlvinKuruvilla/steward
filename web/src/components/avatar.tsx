/**
 * An author's face, from GitHub's own avatar endpoint.
 *
 * No backend work: `github.com/<login>.png` redirects to the avatar, and a
 * login is what the log already stores.
 *
 * A GitHub App's login carries a `[bot]` suffix that is not part of any
 * account name, so it is stripped: `dependabot[bot]` and `cla-assistant[bot]`
 * both resolve once it is gone. `github-actions` has no user account behind it
 * at all and falls back to initials -- the only fix for that is storing the
 * avatar_url GitHub reports, which is mutable presentation data and does not
 * belong in an append-only log.
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
  const account = login?.replace(/\[bot\]$/, "");

  if (!account || broken) {
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
      src={`https://github.com/${encodeURIComponent(account)}.png?size=${size * 2}`}
      alt=""
      width={size}
      height={size}
      loading="lazy"
      onError={() => setBroken(true)}
      className="shrink-0 rounded-full bg-muted ring-1 ring-black/5"
    />
  );
}
