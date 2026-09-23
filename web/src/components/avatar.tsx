/**
 * An account's face: an author, or the owner standing in for a repository.
 *
 * Resolved by the API rather than by guessing a URL: `github.com/<login>.png`
 * covers people and not GitHub Apps, whose login carries a `[bot]` suffix that
 * belongs to no account -- and `github-actions` has no user page at all.
 * Initials when the account is gone or the lookup fails.
 *
 * The API answers with the URL rather than redirecting to it: an <img> request
 * cannot carry the backend's token, so the lookup goes through `get` and the
 * <img> points at GitHub's CDN directly.
 */
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";

import { get } from "@/api";

export function Avatar({
  login,
  size = 20,
}: {
  login: string | null;
  size?: number;
}) {
  const [broken, setBroken] = useState(false);
  const avatar = useQuery({
    queryKey: ["avatar", login],
    queryFn: () =>
      get<{ url: string }>(`/api/avatars/${encodeURIComponent(login!)}`),
    enabled: login !== null,
    // An avatar moves rarely, and the API caches it for the life of the
    // process anyway.
    staleTime: Infinity,
    retry: false,
  });

  if (!login || broken || avatar.isError || !avatar.data) {
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
      src={avatar.data.url}
      alt=""
      width={size}
      height={size}
      loading="lazy"
      onError={() => setBroken(true)}
      className="shrink-0 rounded-full bg-muted ring-1 ring-black/5"
    />
  );
}
