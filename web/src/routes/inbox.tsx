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
import {
  Empty,
  EmptyDescription,
  EmptyHeader,
  EmptyTitle,
} from "@/components/ui/empty";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table";

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
    return <p className="max-w-prose text-sm text-destructive">{error.message}</p>;
  }
  if (isPending) {
    return (
      <div className="flex flex-col gap-2">
        {[0, 1, 2, 3, 4].map((row) => (
          <Skeleton key={row} className="h-10 w-full" />
        ))}
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-9">
      {groups.map((group) => {
        const rows = data.filter((row) => group.holds(row.blocked_on));
        if (rows.length === 0) return null;
        return (
          <section key={group.title}>
            <div className="flex items-baseline gap-3 pb-1.5">
              <h2 className="text-[13px] font-medium text-foreground">
                {group.title}
              </h2>
              <span className="font-mono text-[11px] tabular-nums text-muted-foreground">
                {rows.length}
              </span>
              <span className="truncate text-xs text-muted-foreground">
                {group.note}
              </span>
            </div>

            <Table>
              <TableBody>
                {rows.map((standing) => (
                  <Row
                    key={standing.number}
                    repository={repository}
                    standing={standing}
                  />
                ))}
              </TableBody>
            </Table>
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
  const to = `/${repository.owner}/${repository.name}/pulls/${standing.number}`;
  return (
    <TableRow className="group relative">
      {/* Two lines, as GitHub does it: the title is the row, everything else
          is metadata under it. A number and an author alone cannot be told
          apart at a glance. */}
      <TableCell className="max-w-0 py-2 align-top">
        <Link
          to={to}
          className="block truncate text-[13px] font-medium text-foreground after:absolute after:inset-0 group-hover:underline"
        >
          {standing.title ?? `#${standing.number}`}
        </Link>
        <div className="flex min-w-0 items-center gap-1.5 pt-0.5 text-xs text-muted-foreground">
          <span className="font-mono tabular-nums">#{standing.number}</span>
          <span>·</span>
          <span className="truncate">
            {standing.author ?? "author since deleted"}
          </span>
          {standing.author_is_bot ? (
            <Badge variant="secondary" className="h-4 px-1 text-[10px]">
              bot
            </Badge>
          ) : null}
          {standing.labels.slice(0, 2).map((label) => (
            <Badge key={label} variant="outline" className="h-4 px-1 text-[10px]">
              {label}
            </Badge>
          ))}
        </div>
      </TableCell>
      <TableCell className="w-px py-2 align-top whitespace-nowrap">
        <StateMark
          state={standing.state}
          blockedOn={standing.blocked_on}
          derivation={standing.derivation}
        />
      </TableCell>
      <TableCell className="w-10 py-2 text-right align-top font-mono text-xs tabular-nums text-muted-foreground">
        {standing.comments > 0 ? standing.comments : ""}
      </TableCell>
      <TableCell className="w-12 py-2 text-right align-top font-mono text-xs tabular-nums text-muted-foreground">
        {daysSince(standing.since)}d
      </TableCell>
    </TableRow>
  );
}

function Welcome() {
  return (
    <Empty className="pt-16">
      <EmptyHeader>
        <EmptyTitle>Nothing read yet</EmptyTitle>
        <EmptyDescription>
          Steward reads a repository's pull request history into an append-only
          log, then works out what is waiting on whom. It never writes to
          GitHub.
        </EmptyDescription>
        <EmptyDescription>
          Put an <span className="font-mono">owner/repo</span> in the box above.
          A few hundred pull requests take about half a minute.
        </EmptyDescription>
      </EmptyHeader>
    </Empty>
  );
}

function Reading({ repository }: { repository: Repository }) {
  return (
    <Empty className="pt-16">
      <EmptyHeader>
        <EmptyTitle>
          Reading {repository.owner}/{repository.name}
        </EmptyTitle>
        <EmptyDescription>
          <span className="font-mono tabular-nums text-foreground">
            {repository.pull_requests_read}
          </span>{" "}
          pull requests so far. Every timeline event is stored as it arrives, so
          this happens once per repository.
        </EmptyDescription>
      </EmptyHeader>
    </Empty>
  );
}
