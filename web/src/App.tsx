/**
 * The shell: a repository switcher that can add one, a sidebar, and whatever
 * the route renders. Layout follows docs/design/0002-visual-language.md.
 */
import { useQuery } from "@tanstack/react-query";
import { NavLink, Outlet, useParams } from "react-router";

import { get, type Repository } from "@/api";
import { AddRepository } from "@/components/add-repository";

const sections = [
  { to: "", label: "Inbox" },
  { to: "pulls", label: "PRs" },
  { to: "bots", label: "Bots" },
];

export default function App() {
  const { owner, name } = useParams();
  const { data: repositories } = useQuery({
    queryKey: ["repositories"],
    queryFn: () => get<Repository[]>("/api/repositories"),
    // While a sync is running the counts move, so this keeps up with it.
    refetchInterval: (query) =>
      query.state.data?.some((r) => r.syncing) ? 1000 : false,
  });

  const selected =
    repositories?.find((r) => r.owner === owner && r.name === name) ??
    repositories?.[0];

  return (
    <div className="min-h-screen p-4">
      <div className="mx-auto flex max-w-6xl flex-col overflow-hidden rounded-[var(--radius-shell)] border border-[var(--color-line)] bg-[var(--color-panel)] shadow-[var(--shadow-shell)]">
        <header className="flex items-center justify-between gap-4 border-b border-[var(--color-line)] px-4 py-3">
          <div className="flex items-baseline gap-3">
            <span className="derived">
              {selected ? `${selected.owner}/${selected.name}` : "no repository"}
            </span>
            <SyncState repository={selected} />
          </div>
          <AddRepository />
        </header>

        <div className="flex min-h-[32rem]">
          <nav className="w-40 shrink-0 border-r border-[var(--color-line)] p-2">
            {repositories?.length ? (
              sections.map((section) => (
                <NavLink
                  key={section.label}
                  to={
                    selected
                      ? `/${selected.owner}/${selected.name}/${section.to}`
                      : "/"
                  }
                  end
                  className={({ isActive }) =>
                    `block rounded-[var(--radius-row)] px-3 py-2 text-sm ${
                      isActive
                        ? "bg-[var(--color-active)] text-[var(--color-primary)]"
                        : "text-[var(--color-secondary)] hover:bg-[var(--color-hover)]"
                    }`
                  }
                >
                  {section.label}
                </NavLink>
              ))
            ) : (
              <p className="px-3 py-2 text-xs text-[var(--color-secondary)]">
                Add a repository to begin.
              </p>
            )}
          </nav>

          <main className="flex-1 p-4">
            <Outlet context={selected} />
          </main>
        </div>
      </div>
    </div>
  );
}

function SyncState({ repository }: { repository: Repository | undefined }) {
  if (!repository) return null;
  if (repository.sync_error) {
    return (
      <span className="text-xs text-[var(--color-state-closed)]">
        {repository.sync_error}
      </span>
    );
  }
  if (repository.syncing) {
    return (
      <span className="derived text-xs text-[var(--color-state-attention)]">
        reading… {repository.pull_requests_read} pull requests
      </span>
    );
  }
  return (
    <span className="text-xs text-[var(--color-secondary)]">
      {repository.last_sync
        ? `synced ${new Date(repository.last_sync).toLocaleString()}`
        : "never synced"}
    </span>
  );
}
