import { useQuery } from "@tanstack/react-query";
import { useOutletContext } from "react-router";

import { daysSince, get, type BlockedOn, type Repository, type Standing } from "@/api";
import { StateChip } from "@/components/state-chip";

/**
 * The queue, grouped by who it is waiting on. 0002's screen: NEEDS YOU first,
 * then everything waiting on someone else, then what nothing can be said about.
 */
const groups: { title: string; holds: (blocked: BlockedOn) => boolean }[] = [
  { title: "Needs you", holds: (b) => b === "REVIEWER" || b === "MERGER" },
  { title: "Waiting on others", holds: (b) => b === "AUTHOR" },
  { title: "No answer", holds: (b) => b === "UNKNOWN" },
];

export function Component() {
  const repository = useOutletContext<Repository | undefined>();
  const { data, error, isPending } = useQuery({
    queryKey: ["pulls", repository?.owner, repository?.name],
    enabled: Boolean(repository) && !repository?.syncing,
    queryFn: () =>
      get<Standing[]>(
        `/api/repositories/${repository!.owner}/${repository!.name}/pulls`,
      ),
  });

  if (!repository) {
    return (
      <p className="text-sm text-[var(--color-secondary)]">
        Nothing synced yet. Add a repository above.
      </p>
    );
  }
  if (repository.syncing) {
    return (
      <p className="text-sm text-[var(--color-secondary)]">
        Reading {repository.owner}/{repository.name}…{" "}
        <span className="derived">{repository.pull_requests_read}</span> pull
        requests so far.
      </p>
    );
  }
  if (isPending) {
    return <p className="text-sm text-[var(--color-secondary)]">Reading…</p>;
  }
  if (error) {
    return <p className="text-sm text-[var(--color-state-closed)]">{error.message}</p>;
  }

  return (
    <div className="flex flex-col gap-6">
      {groups.map((group) => {
        const rows = data.filter((row) => group.holds(row.blocked_on));
        if (rows.length === 0) return null;
        return (
          <section key={group.title}>
            <h2 className="mb-1 text-xs tracking-wide text-[var(--color-secondary)] uppercase">
              {group.title}
              <span className="derived ml-2 normal-case">{rows.length}</span>
            </h2>
            <ul className="border-t border-[var(--color-line)]">
              {rows.map((row) => (
                <Row key={row.number} standing={row} />
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}

function Row({ standing }: { standing: Standing }) {
  return (
    <li className="flex h-[var(--spacing-row)] items-center gap-3 border-b border-[var(--color-line)] px-2 hover:bg-[var(--color-hover)]">
      <span className="derived w-16 text-[var(--color-secondary)]">
        #{standing.number}
      </span>
      <span className="flex-1 truncate text-sm">
        {standing.author ?? "unknown author"}
      </span>
      <StateChip
        state={standing.state}
        blockedOn={standing.blocked_on}
        derivation={standing.derivation}
      />
      <span className="derived w-12 text-right text-[var(--color-secondary)]">
        {daysSince(standing.since)}d
      </span>
    </li>
  );
}
