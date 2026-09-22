import { useQuery } from "@tanstack/react-query";
import { ChevronRight, ExternalLink, MessageSquare } from "lucide-react";
import { useCallback, useMemo, useState } from "react";
import { Link, useNavigate, useOutletContext } from "react-router";

import {
  get,
  githubUrl,
  since,
  type Repository,
  type Standing,
} from "@/api";
import { Avatar } from "@/components/avatar";
import { StateMark } from "@/components/state-mark";
import { useKeys } from "@/keys";
import { Badge } from "@/components/ui/badge";
import {
  Empty,
  EmptyDescription,
  EmptyHeader,
  EmptyTitle,
} from "@/components/ui/empty";
import { Skeleton } from "@/components/ui/skeleton";

/**
 * The queue, cut by who holds each pull request.
 *
 * Bots are their own group and collapsed by default. Eleven dependabot bumps
 * that differ only in a package name tell a maintainer one thing, not eleven,
 * and they were burying the three rows that needed a person.
 */
const groups: {
  title: string;
  note: string;
  holds: (standing: Standing) => boolean;
}[] = [
  {
    title: "Needs you",
    note: "waiting on a review or a merge",
    holds: (s) =>
      !s.author_is_bot && (s.blocked_on === "REVIEWER" || s.blocked_on === "MERGER"),
  },
  {
    title: "With the author",
    note: "changes were asked for, or it is a draft",
    holds: (s) => !s.author_is_bot && s.blocked_on === "AUTHOR",
  },
  {
    title: "No answer",
    note: "no review requested, and no rule in steward.toml says who should have it",
    holds: (s) => !s.author_is_bot && s.blocked_on === "UNKNOWN",
  },
  {
    title: "Bots",
    note: "opened by a machine, waiting on a policy rather than a person",
    holds: (s) => s.author_is_bot,
  },
];

export function Component() {
  const repository = useOutletContext<Repository | undefined>();
  const navigate = useNavigate();
  const [cursor, setCursor] = useState(0);
  const { data, error, isPending } = useQuery({
    queryKey: ["pulls", repository?.owner, repository?.name],
    enabled: Boolean(repository) && !repository?.syncing,
    queryFn: () =>
      get<Standing[]>(
        `/api/repositories/${repository!.owner}/${repository!.name}/pulls`,
      ),
  });

  // Everything the keys can land on, in the order the eye reads them. Bots are
  // collapsed by default and excluded: a cursor that walks into a hidden group
  // looks broken.
  const walkable = useMemo(
    () =>
      (data ?? []).filter((row) =>
        groups.slice(0, 3).some((group) => group.holds(row)),
      ),
    [data],
  );

  const at = walkable[Math.min(cursor, walkable.length - 1)];
  const move = useCallback(
    (by: number) =>
      setCursor((was) =>
        Math.max(0, Math.min(was + by, Math.max(0, walkable.length - 1))),
      ),
    [walkable.length],
  );

  useKeys(
    useMemo(
      () => ({
        next: () => move(1),
        previous: () => move(-1),
        open: () => {
          if (at && repository) {
            void navigate(
              `/${repository.owner}/${repository.name}/pulls/${at.number}`,
            );
          }
        },
        openExternally: () => {
          if (at && repository) {
            window.open(
              githubUrl(repository.owner, repository.name, at.number),
              "_blank",
              "noreferrer",
            );
          }
        },
      }),
      [at, move, navigate, repository],
    ),
  );

  if (!repository) return <Welcome />;
  if (repository.syncing) return <Reading repository={repository} />;
  if (error) {
    return <p className="max-w-prose text-sm text-destructive">{error.message}</p>;
  }
  if (isPending) {
    return (
      <div className="flex flex-col gap-px">
        {[0, 1, 2, 3, 4, 5].map((row) => (
          <Skeleton key={row} className="h-11 w-full rounded-none" />
        ))}
      </div>
    );
  }

  const needing = data.filter((row) => groups[0].holds(row)).length;

  return (
    <>
      <div className="flex items-baseline justify-between gap-4 pb-5">
        <div>
          <h2 className="text-[22px] leading-tight font-semibold tracking-[-0.02em] text-foreground">
            {needing === 0
              ? "Nothing is waiting on you"
              : `${needing} waiting on you`}
          </h2>
          <p className="pt-1.5 text-[13px] text-muted-foreground">
            {data.length} open pull requests, read from{" "}
            <span className="font-mono">
              {repository.owner}/{repository.name}
            </span>
            .
          </p>
        </div>
        <p className="hidden shrink-0 text-xs text-muted-foreground sm:block">
          <Key>j</Key> <Key>k</Key> move · <Key>↵</Key> open ·{" "}
          <Key>o</Key> on GitHub
        </p>
      </div>

      <div className="flex flex-col gap-7">
        {groups.map((group) => {
          const rows = data.filter(group.holds);
          if (rows.length === 0) return null;
          return (
            <Group
              key={group.title}
              title={group.title}
              note={group.note}
              rows={rows}
              repository={repository}
              collapsed={group.title === "Bots"}
              cursorOn={at?.number}
            />
          );
        })}
      </div>
    </>
  );
}

function Key({ children }: { children: React.ReactNode }) {
  return (
    <kbd className="rounded border border-border bg-muted px-1 font-mono text-[10px] text-foreground">
      {children}
    </kbd>
  );
}

function Group({
  title,
  note,
  rows,
  repository,
  collapsed,
  cursorOn,
}: {
  title: string;
  note: string;
  rows: Standing[];
  repository: Repository;
  collapsed: boolean;
  cursorOn: number | undefined;
}) {
  const [open, setOpen] = useState(!collapsed);

  return (
    <section>
      <button
        type="button"
        onClick={() => setOpen((was) => !was)}
        className="group flex w-full items-center gap-2 pb-1.5 text-left"
      >
        <ChevronRight
          aria-hidden
          className={`size-3 shrink-0 text-muted-foreground transition-transform ${
            open ? "rotate-90" : ""
          }`}
        />
        <span className="text-[11px] font-medium tracking-[0.08em] text-foreground uppercase">
          {title}
        </span>
        <span className="font-mono text-[11px] tabular-nums text-muted-foreground">
          {rows.length}
        </span>
        <span className="truncate text-xs text-muted-foreground">{note}</span>

      </button>

      {open ? (
        <div className="overflow-hidden rounded-lg border border-border">
          {rows.map((standing, index) => (
            <Row
              key={standing.number}
              repository={repository}
              standing={standing}
              first={index === 0}
              under={standing.number === cursorOn}
            />
          ))}
        </div>
      ) : null}
    </section>
  );
}

function Row({
  repository,
  standing,
  first,
  under,
}: {
  repository: Repository;
  standing: Standing;
  first: boolean;
  under: boolean;
}) {
  return (
    <Link
      to={`/${repository.owner}/${repository.name}/pulls/${standing.number}`}
      className={[
        "group/row grid grid-cols-[minmax(0,1fr)_10rem_2.75rem_3rem_1.75rem] items-center gap-4 px-3.5 py-2.5",
        "transition-colors hover:bg-muted",
        first ? "" : "border-t border-border",
        // A bar rather than a fill: a filled row puts muted text on a mid
        // grey and the whole line loses contrast.
        under
          ? "relative bg-accent/50 before:absolute before:inset-y-0 before:left-0 before:w-[2px] before:bg-foreground"
          : "",
      ].join(" ")}
    >
      <span className="flex min-w-0 items-center gap-2.5">
        <Avatar login={standing.author} size={22} />
        <span className="min-w-0">
        <span className="block truncate text-sm text-foreground">
          {standing.title ?? `#${standing.number}`}
        </span>
        <span className="flex min-w-0 items-center gap-1.5 pt-0.5 text-xs text-muted-foreground">
          <span className="font-mono tabular-nums">#{standing.number}</span>
          <span className="truncate">
            {standing.author ?? "author since deleted"}
          </span>
          {standing.last_kind ? (
            <span className="hidden truncate md:inline">
              · last:{" "}
              <span className="font-mono">
                {standing.last_kind.replace(/_/g, " ")}
              </span>
              {standing.last_at ? ` ${since(standing.last_at)} ago` : ""}
            </span>
          ) : null}
          {standing.labels.slice(0, 2).map((label) => (
            <Badge
              key={label}
              variant="outline"
              className="h-4 shrink-0 px-1 text-[10px] font-normal"
            >
              {label}
            </Badge>
          ))}
        </span>
        </span>
      </span>

      <StateMark
        state={standing.state}
        blockedOn={standing.blocked_on}
        derivation={standing.derivation}
      />

      <span className="flex items-center justify-end gap-1 font-mono text-xs tabular-nums text-muted-foreground">
        {standing.comments > 0 ? (
          <>
            <MessageSquare className="size-3" aria-hidden />
            {standing.comments}
          </>
        ) : null}
      </span>

      <span
        className="text-right font-mono text-xs tabular-nums text-muted-foreground"
        title={`in ${standing.state} since ${new Date(standing.since).toLocaleString()}`}
      >
        {since(standing.since)}
      </span>

      <a
        href={githubUrl(repository.owner, repository.name, standing.number)}
        target="_blank"
        rel="noreferrer"
        onClick={(event) => event.stopPropagation()}
        title="Open on GitHub"
        className="rounded p-1 text-muted-foreground opacity-0 transition-opacity hover:bg-muted hover:text-foreground focus-visible:opacity-100 group-hover/row:opacity-100"
      >
        <ExternalLink className="size-3.5" aria-hidden />
        <span className="sr-only">Open #{standing.number} on GitHub</span>
      </a>
    </Link>
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
