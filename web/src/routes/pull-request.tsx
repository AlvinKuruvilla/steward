import { useQuery } from "@tanstack/react-query";
import { Link, useParams } from "react-router";

import {
  get,
  githubUrl,
  since,
  type Derivation,
  type PullRequest,
  type WorkflowState,
} from "@/api";
import { StateMark } from "@/components/state-mark";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table";

/**
 * Why a pull request is where it is.
 *
 * Two columns: what Steward concluded, and what it concluded it from. The
 * episodes are the argument; the events are the evidence, and every episode
 * boundary is an event sitting at the same timestamp further down.
 */
export function Component() {
  const { owner, name, number } = useParams();
  const { data, error, isPending } = useQuery({
    queryKey: ["pull", owner, name, number],
    queryFn: () =>
      get<PullRequest>(
        `/api/repositories/${owner}/${name}/pulls/${number}`,
      ),
  });

  if (error) {
    return <p className="text-sm text-destructive">{error.message}</p>;
  }
  if (isPending) {
    return <Skeleton className="h-64 w-full" />;
  }

  return (
    <div className="flex flex-col gap-8">
      <header className="flex items-baseline gap-4">
        <Button
          size="xs"
          variant="ghost"
          className="-ml-2 text-muted-foreground"
          render={<Link to={`/${owner}/${name}`} />}
        >
          ← inbox
        </Button>
        <h2 className="font-mono text-[15px] tabular-nums text-foreground">
          #{data.standing.number}
        </h2>
        <StateMark
          state={data.standing.state}
          blockedOn={data.standing.blocked_on}
          derivation={data.standing.derivation}
        />
        <span className="truncate text-[13px] text-muted-foreground">
          {data.standing.title}
        </span>
        <a
          href={githubUrl(owner!, name!, data.standing.number)}
          target="_blank"
          rel="noreferrer"
          className="ml-auto shrink-0 text-xs text-muted-foreground hover:text-foreground"
        >
          open on GitHub ↗
        </a>
      </header>

      <div className="grid gap-10 lg:grid-cols-[minmax(0,22rem)_minmax(0,1fr)]">
        <section>
          <h3 className="pb-1.5 text-[13px] font-medium text-foreground">
            How it got here
          </h3>
          <Table>
            <TableBody>
              {data.episodes.map((episode, index) => (
                <TableRow key={`${episode.start}-${index}`}>
                  <TableCell>
                    <StateMark
                      state={episode.state}
                      blockedOn={episode.blocked_on}
                      derivation={episode.derivation}
                    />
                  </TableCell>
                  <TableCell className="w-24 text-right font-mono text-[11px] tabular-nums whitespace-nowrap text-muted-foreground">
                    {since(episode.start, episode.end)}{episode.end ? "" : " so far"}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          <p className="pt-3 text-xs leading-relaxed text-muted-foreground">
            {sentence(data.standing.state, data.standing.derivation)}
          </p>
        </section>

        <section>
          <h3 className="pb-1.5 text-[13px] font-medium text-foreground">
            What it was read from
          </h3>
          <Table>
            <TableBody>
              {data.events.map((moment, index) => (
                <TableRow key={`${moment.occurred_at}-${index}`}>
                  <TableCell className="w-32 align-top font-mono text-[11px] tabular-nums text-muted-foreground">
                    <time dateTime={moment.occurred_at}>
                      {stamp(moment.occurred_at)}
                    </time>
                  </TableCell>
                  <TableCell className="w-36 align-top font-mono text-xs text-foreground">
                    {moment.kind}
                  </TableCell>
                  <TableCell className="max-w-0">
                    <span className="block truncate text-xs text-foreground">
                      {moment.actor ?? "—"}
                    </span>
                    {Object.entries(moment.payload).length > 0 ? (
                      <span className="block pt-0.5 font-mono text-[11px] break-all text-muted-foreground">
                        {Object.entries(moment.payload)
                          .map(([key, value]) => `${key}=${String(value)}`)
                          .join("  ")}
                      </span>
                    ) : null}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </section>
      </div>
    </div>
  );
}

function stamp(when: string): string {
  return new Date(when).toLocaleString(undefined, {
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function sentence(state: WorkflowState, derivation: Derivation): string {
  if (derivation === "UNKNOWN") {
    return "No review was ever requested and no rule in steward.toml says who should hold this, so Steward does not guess.";
  }
  if (derivation === "POLICY") {
    return "A rule in steward.toml supplied what the events alone could not.";
  }
  return `Every step above came from a GitHub event, ending in ${state}.`;
}
