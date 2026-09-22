/**
 * The shell. One column of repositories, one of work, and a header thin enough
 * that the queue starts near the top of the window.
 *
 * Density is GitHub's: 1px rules between rows rather than gaps, no card around
 * anything that belongs in a list. Calm is OpenWork's: a soft outer shell, a
 * near-flat interior, and colour reserved for state.
 */
import { useQuery } from "@tanstack/react-query";
import { NavLink, Outlet, useParams } from "react-router";

import { get, type Repository } from "@/api";
import { AddRepository } from "@/components/add-repository";

export default function App() {
  const { owner, name } = useParams();
  const { data: repositories } = useQuery({
    queryKey: ["repositories"],
    queryFn: () => get<Repository[]>("/api/repositories"),
    refetchInterval: (query) =>
      query.state.data?.some((r) => r.syncing) ? 1000 : false,
  });

  const selected =
    repositories?.find((r) => r.owner === owner && r.name === name) ??
    repositories?.[0];

  return (
    <div className="min-h-screen bg-[var(--slate-2)]">
      <div className="mx-auto grid min-h-screen max-w-[1180px] grid-cols-[13rem_1fr] gap-px bg-[var(--color-line-soft)] px-6">
        <Sidebar repositories={repositories} selected={selected} />

        <div className="flex min-w-0 flex-col bg-[var(--color-app)]">
          <header className="flex h-14 shrink-0 items-center justify-between gap-6 border-b border-[var(--color-line-soft)] px-6">
            <div className="flex min-w-0 items-baseline gap-3">
              <h1 className="derived truncate text-[13px] text-[var(--color-ink)]">
                {selected ? `${selected.owner}/${selected.name}` : "Steward"}
              </h1>
              <SyncState repository={selected} />
            </div>
            <AddRepository />
          </header>

          <main className="min-w-0 flex-1 px-6 py-5">
            <Outlet context={selected} />
          </main>
        </div>
      </div>
    </div>
  );
}

function Sidebar({
  repositories,
  selected,
}: {
  repositories: Repository[] | undefined;
  selected: Repository | undefined;
}) {
  return (
    <aside className="flex flex-col bg-[var(--color-raised)] px-3 py-5">
      <span className="px-2 pb-3 text-[11px] font-medium tracking-[0.08em] text-[var(--color-muted)] uppercase">
        Repositories
      </span>

      <nav className="flex flex-col gap-px">
        {repositories?.map((repository) => (
          <NavLink
            key={`${repository.owner}/${repository.name}`}
            to={`/${repository.owner}/${repository.name}`}
            className={() =>
              [
                "group flex items-baseline gap-2 rounded-[var(--radius-row)] px-2 py-1.5",
                "text-[13px] transition-colors duration-100",
                repository === selected
                  ? "bg-[var(--color-selected)] text-[var(--color-ink)]"
                  : "text-[var(--color-muted)] hover:bg-[var(--color-hover)]",
              ].join(" ")
            }
          >
            <span className="truncate">{repository.name}</span>
            {repository.syncing ? (
              <span className="derived ml-auto text-[11px] text-[var(--color-attention)]">
                {repository.pull_requests_read}
              </span>
            ) : null}
          </NavLink>
        ))}
      </nav>

      {repositories?.length === 0 ? (
        <p className="px-2 text-[13px] leading-relaxed text-[var(--color-muted)]">
          Nothing synced. Give Steward a repository and it reads the pull request
          history into an event log.
        </p>
      ) : null}

      <footer className="mt-auto px-2 pt-6 text-[11px] leading-relaxed text-[var(--color-muted)]">
        <span className="derived">mono</span> is derived from an event.
        <br />
        Prose is not.
      </footer>
    </aside>
  );
}

function SyncState({ repository }: { repository: Repository | undefined }) {
  if (!repository) return null;

  if (repository.sync_error) {
    return (
      <span className="text-[12px] text-[var(--color-closed)]">
        {repository.sync_error}
      </span>
    );
  }

  if (repository.syncing) {
    return (
      <span className="flex items-baseline gap-1.5 text-[12px] text-[var(--color-muted)]">
        <span className="size-1.5 translate-y-[-1px] animate-pulse rounded-full bg-[var(--color-attention)]" />
        reading
        <span className="derived text-[var(--color-ink)]">
          {repository.pull_requests_read}
        </span>
        pull requests
      </span>
    );
  }

  if (!repository.last_sync) return null;

  return (
    <span className="text-[12px] text-[var(--color-muted)]">
      synced{" "}
      <time dateTime={repository.last_sync}>
        {new Date(repository.last_sync).toLocaleString(undefined, {
          month: "short",
          day: "numeric",
          hour: "2-digit",
          minute: "2-digit",
        })}
      </time>
    </span>
  );
}
