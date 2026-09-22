import { useQuery } from "@tanstack/react-query";
import { Link, useParams } from "react-router";

import { get, type Derivation, type PullRequest, type WorkflowState } from "@/api";
import { StateMark } from "@/components/state-mark";

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
    return (
      <p className="text-[13px] text-[var(--color-closed)]">{error.message}</p>
    );
  }
  if (isPending) {
    return <p className="text-[13px] text-[var(--color-muted)]">Reading…</p>;
  }

  return (
    <div className="flex flex-col gap-8">
      <header className="flex items-baseline gap-4">
        <Link
          to={`/${owner}/${name}`}
          className="text-[12px] text-[var(--color-muted)] hover:text-[var(--color-ink)]"
        >
          ← inbox
        </Link>
        <h2 className="derived text-[15px] text-[var(--color-ink)]">
          #{data.standing.number}
        </h2>
        <StateMark
          state={data.standing.state}
          blockedOn={data.standing.blocked_on}
          derivation={data.standing.derivation}
        />
        <span className="text-[13px] text-[var(--color-muted)]">
          opened by {data.standing.author ?? "an account since deleted"}
        </span>
      </header>

      <div className="grid gap-10 lg:grid-cols-[minmax(0,22rem)_minmax(0,1fr)]">
        <section>
          <h3 className="pb-2 text-[13px] font-medium text-[var(--color-ink)]">
            How it got here
          </h3>
          <ol className="border-t border-[var(--color-line-soft)]">
            {data.episodes.map((episode, index) => (
              <li
                key={`${episode.start}-${index}`}
                className="grid grid-cols-[1fr_auto] items-baseline gap-3 border-b border-[var(--color-line-soft)] py-2"
              >
                <span className="flex items-baseline gap-2">
                  <StateMark
                    state={episode.state}
                    blockedOn={episode.blocked_on}
                    derivation={episode.derivation}
                  />
                </span>
                <span className="derived text-[11px] text-[var(--color-muted)]">
                  {span(episode.start, episode.end)}
                </span>
              </li>
            ))}
          </ol>
          <p className="pt-3 text-[12px] leading-relaxed text-[var(--color-muted)]">
            {sentence(data.standing.state, data.standing.derivation)}
          </p>
        </section>

        <section>
          <h3 className="pb-2 text-[13px] font-medium text-[var(--color-ink)]">
            What it was read from
          </h3>
          <ol className="border-t border-[var(--color-line-soft)]">
            {data.events.map((moment, index) => (
              <li
                key={`${moment.occurred_at}-${index}`}
                className="grid grid-cols-[8.5rem_9rem_1fr] items-baseline gap-3 border-b border-[var(--color-line-soft)] py-1.5"
              >
                <time
                  className="derived text-[11px] text-[var(--color-muted)]"
                  dateTime={moment.occurred_at}
                >
                  {stamp(moment.occurred_at)}
                </time>
                <span className="derived truncate text-[12px] text-[var(--color-ink)]">
                  {moment.kind}
                </span>
                <span className="flex min-w-0 items-baseline gap-2">
                  <span className="truncate text-[12px] text-[var(--color-muted)]">
                    {moment.actor ?? "—"}
                  </span>
                  {Object.entries(moment.payload).map(([key, value]) => (
                    <span
                      key={key}
                      className="derived truncate text-[11px] text-[var(--color-muted)]"
                    >
                      {key}={String(value)}
                    </span>
                  ))}
                </span>
              </li>
            ))}
          </ol>
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

/** How long an episode lasted, or that it is the one still running. */
function span(start: string, end: string | null): string {
  const finished = end ? new Date(end).getTime() : Date.now();
  const hours = (finished - new Date(start).getTime()) / 3_600_000;
  const measure = hours < 48 ? `${Math.round(hours)}h` : `${Math.round(hours / 24)}d`;
  return end ? measure : `${measure}, still`;
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
