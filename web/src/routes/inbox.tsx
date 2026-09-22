import { useQuery } from "@tanstack/react-query";
import { Link, useOutletContext } from "react-router";

import {
  daysSince,
  get,
  type BlockedOn,
  type Repository,
  type Standing,
} from "@/api";
import { StateMark } from "@/components/state-mark";

/**
 * The queue, cut by who it is waiting on rather than by state. A maintainer
 * opens this to find their own work, so their own work is the first group and
 * the only one that gets a count in the corner of the eye.
 */
const groups: {
  title: string;
  note: string;
  holds: (blocked: BlockedOn) => boolean;
}[] = [
  {
    title: "Needs you",
    note: "waiting on a review or a merge",
    holds: (b) => b === "REVIEWER" || b === "MERGER",
  },
  {
    title: "With the author",
    note: "changes were asked for, or it is a draft",
    holds: (b) => b === "AUTHOR",
  },
  {
    title: "No answer",
    note: "no review was ever requested, and no rule says who should have it",
    holds: (b) => b === "UNKNOWN",
  },
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

  if (!repository) return <Welcome />;
  if (repository.syncing) return <Reading repository={repository} />;
  if (error) {
    return (
      <p className="max-w-prose text-[13px] text-[var(--color-closed)]">
        {error.message}
      </p>
    );
  }
  if (isPending) {
    return <p className="text-[13px] text-[var(--color-muted)]">Reading the log…</p>;
  }

  return (
    <div className="flex flex-col gap-9">
      {groups.map((group) => {
        const rows = data.filter((row) => group.holds(row.blocked_on));
        if (rows.length === 0) return null;
        return (
          <section key={group.title}>
            <div className="flex items-baseline gap-3 pb-2">
              <h2 className="text-[13px] font-medium text-[var(--color-ink)]">
                {group.title}
              </h2>
              <span className="derived text-[11px] text-[var(--color-muted)]">
                {rows.length}
              </span>
              <span className="truncate text-[12px] text-[var(--color-muted)]">
                {group.note}
              </span>
            </div>

            <ul className="border-t border-[var(--color-line-soft)]">
              {rows.map((standing) => (
                <Row
                  key={standing.number}
                  repository={repository}
                  standing={standing}
                />
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}

function Row({
  repository,
  standing,
}: {
  repository: Repository;
  standing: Standing;
}) {
  return (
    <li className="border-b border-[var(--color-line-soft)]">
      <Link
        to={`/${repository.owner}/${repository.name}/pulls/${standing.number}`}
        className="grid h-10 grid-cols-[4.5rem_1fr_auto_3.5rem] items-center gap-4 px-2 transition-colors duration-100 hover:bg-[var(--color-hover)]"
      >
        <span className="derived text-[12px] text-[var(--color-muted)]">
          #{standing.number}
        </span>
        <span className="truncate text-[13px] text-[var(--color-ink)]">
          {standing.author ?? "author since deleted"}
        </span>
        <StateMark
          state={standing.state}
          blockedOn={standing.blocked_on}
          derivation={standing.derivation}
        />
        <span className="derived text-right text-[12px] text-[var(--color-muted)]">
          {daysSince(standing.since)}d
        </span>
      </Link>
    </li>
  );
}

function Welcome() {
  return (
    <div className="max-w-[46ch] pt-10">
      <h2 className="text-[15px] text-[var(--color-ink)]">
        Nothing here yet
      </h2>
      <p className="pt-2 text-[13px] leading-relaxed text-[var(--color-muted)]">
        Steward reads a repository's pull request history into an append-only
        log, then works out what is waiting on whom. It never writes to GitHub.
      </p>
      <p className="pt-3 text-[13px] leading-relaxed text-[var(--color-muted)]">
        Put an <span className="derived">owner/repo</span> in the box above to
        start. A few hundred pull requests take about half a minute.
      </p>
    </div>
  );
}

function Reading({ repository }: { repository: Repository }) {
  return (
    <div className="max-w-[46ch] pt-10">
      <h2 className="text-[15px] text-[var(--color-ink)]">
        Reading {repository.owner}/{repository.name}
      </h2>
      <p className="pt-2 text-[13px] leading-relaxed text-[var(--color-muted)]">
        <span className="derived text-[var(--color-ink)]">
          {repository.pull_requests_read}
        </span>{" "}
        pull requests so far. Every timeline event is stored as it arrives, so
        this only happens once per repository.
      </p>
    </div>
  );
}
