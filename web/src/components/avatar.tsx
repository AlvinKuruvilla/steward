/**
 * An author's face, from GitHub's own avatar endpoint.
 *
 * No backend work: `github.com/<login>.png` redirects to the avatar, and a
 * login is what the log already stores. Falls back to initials when the
 * account is gone or the image fails.
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
      src={`https://github.com/${encodeURIComponent(login)}.png?size=${size * 2}`}
      alt=""
      width={size}
      height={size}
      loading="lazy"
      onError={() => setBroken(true)}
      className="shrink-0 rounded-full bg-muted ring-1 ring-black/5"
    />
  );
}
