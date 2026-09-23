# 0002 — What Steward looks like

Status: accepted, 2026-09-21. Amended 2026-09-22: diagrams render,
and the stack is named.

Steward should look like OpenWork's surface wrapped around GitHub's density. Both
halves are real products with published tokens, so this document names values
rather than adjectives. The OpenWork values were read from
`apps/app/src/styles/colors.css` and `apps/app/src/app/index.css` at
`different-ai/openwork`; the GitHub values from `@primer/primitives` 11.10.0.

## What earns space

A maintainer opens Steward to answer "what is waiting on me, and why". Every
pixel either carries evidence or gets out of the way. There is no chart that
could have been a number, no card that could have been a row, and no color that
does not mean something.

This is why the product borrows from two places instead of one. OpenWork's
surface is calm and modern and would go soft if it had to hold three hundred
rows. GitHub's density holds three hundred rows and looks like 2012. Take the
shell from one and the contents from the other.

## Neutrals and accent, from OpenWork

Radix's 12-step scales on **slate**, because they give light and dark parity and
alpha variants without hand-mixing, and because they are what OpenWork uses.

| role | token | light | dark |
|---|---|---|---|
| app background | `--slate-1` | | |
| panel, sidebar | `--slate-2` | | |
| hover | `--slate-3` | | |
| active | `--slate-5` | | |
| secondary text | `--slate-11` | | |
| primary text | `--slate-12` | | |
| accent | | `#011627` | `#011627` |
| accent hover | | `#000000` | `#0a2540` |
| border | | `#f3f4f6` | `#262626` |

The accent is a near-black deep navy in both themes. That is deliberate and worth
keeping: with a monochrome accent, **color is reserved entirely for state**.
GitHub spends blue on every link and then needs green, purple, red and gray on
top of it. Steward spends nothing on chrome, so when something is green it means
one thing.

## State colors, from GitHub

Maintainers have years of muscle memory: green is open, purple is merged, red is
closed, gray is draft. Inventing a new mapping costs recognition and buys
nothing. These are Primer's functional values, unmodified.

| state | light fg | dark fg | emphasis |
|---|---|---|---|
| open | `#1a7f37` | `#3fb950` | `#1f883d` / `#238636` |
| merged | `#8250df` | `#ab7df8` | `#8250df` / `#8957e5` |
| closed | `#d1242f` | `#f85149` | `#cf222e` / `#da3633` |
| draft | `#59636e` | `#9198a1` | `#59636e` / `#656c76` |
| attention | `#9a6700` | `#d29922` | — |
| muted text | `#59636e` | `#9198a1` | — |

Steward's own states map onto these rather than adding a palette: `REVIEW_WAIT`
and `RE_REVIEW_WAIT` take attention, `APPROVED` takes open, `CHANGES_REQUESTED`
takes closed, `DRAFT` and `BOT_PR` take draft, and `UNKNOWN` takes muted. An
`UNKNOWN` is deliberately the quietest thing on the screen — it is an absence of
evidence and should not look like an alert.

## Typography carries the trust boundary

Two faces, one family: **Geist Variable** for chrome and prose, **Geist Mono**
for everything derived.

Inside a content area the rule is strict, and it is the visual form of
[`0001-llm-boundary.md`](0001-llm-boundary.md):

    monospace       a fact the engine derived, with an event behind it
    proportional    prose, chrome, and anything a model generated

So an enrichment block does not need a warning icon or a colored border to be
recognisable. It reads differently, because it is a different kind of claim.
Everything computed lines up in a monospace grid; the one generated paragraph on
the page does not. A maintainer learns this in about ten seconds and then never
has to think about it again.

Sizes: 13px mono for data rows, 14px proportional for prose, 12px for secondary
metadata. Tabular numerals everywhere a column of numbers appears.

## Radius and density

| element | radius | source |
|---|---|---|
| app shell, panel, modal | 16px | OpenWork `--dls-radius` |
| large surfaces | 24px | OpenWork `--dls-radius-lg` |
| data rows, badges, inline chips, buttons | 6px | GitHub |

Soft outside, tight inside. The window feels like a modern application; the list
inside it feels like a tool. Applying 16px to a row makes eight rows look like
eight cards, so a queue stops reading as a queue.

Density follows GitHub: 40px rows, an 8px spacing rhythm, borders between rows
rather than gaps, no card wrapper around anything that belongs in a list.

Shadows are OpenWork's, which is to say nearly invisible — `0 8px 24px
rgba(15,23,42,0.05)` in light, `0 14px 36px rgba(0,0,0,0.24)` in dark — and they
appear on shells and popovers only. Never on a row.

## Motion

OpenWork's curve, `260ms cubic-bezier(0.22, 1, 0.36, 1)`, for panels, popovers
and accordions, with `prefers-reduced-motion` honored.

**State never animates.** A PR that moved from `REVIEW_WAIT` to
`RE_REVIEW_WAIT` is different when you next look at it; it does not slide,
crossfade, or pulse. Animating state implies Steward is doing something, and
Steward is showing something. The distinction is the whole product.

## Diagrams

State diagrams and timelines render. The earlier decision here was ASCII, on the
grounds that it survives being copied into an issue comment and costs nothing to
maintain; that is a real loss and it is being paid for legibility.

A rendered diagram still belongs to the derived register: monospace labels,
tabular numerals, the same state colors as a row. Nothing is drawn that a
maintainer cannot trace to an event.

Charts follow the rule at the top of this document. A chart that could have been
a number is a number. The first one that cannot is V1.5's lifetime attribution,
and there is no chart before it.

## A screen

```text
┌──────────────────────────────────────────────────────────────────────┐
│  precogly/precogly                              synced 20 seconds ago│   <- 16px shell
├────────────┬─────────────────────────────────────────────────────────┤
│            │                                                         │
│ Inbox    2 │  NEEDS YOU                                              │
│ PRs     15 │  ──────────────────────────────────────────────────     │   <- 40px rows,
│ Bots    13 │  #491  re-review        author pushed after your review │      6px chips,
│ Flow       │        RE_REVIEW_WAIT · EVENT · 1d          CI 6/7      │      1px rules
│ People     │  ──────────────────────────────────────────────────     │
│            │  #4    review           no review submitted             │
│            │        REVIEW_WAIT · POLICY · 2d            CI ok       │
│            │                                                         │
│            │  WAITING ON OTHERS                                      │
│            │  ──────────────────────────────────────────────────     │
│            │  #551  contributor      changes requested Sep 19        │
│            │        CHANGES_REQUESTED · EVENT · 2d                   │
│            │                                                         │
│            │  BOTS                                        13 · 17d   │
│            │  dependabot · 11 grouped · npm, pip                     │
│            │                                                         │
└────────────┴─────────────────────────────────────────────────────────┘

 EVENT   derived from a GitHub event alone; the strongest claim available
 POLICY  an event plus a rule this repository wrote down in steward.toml
 UNKNOWN neither, rendered muted; never inferred and never hidden
```

Every row's state carries its derivation class inline. It costs six characters
and it is the difference between a tool a maintainer audits and a tool they
either trust or abandon.

## What renders it

Vite, React, React Router, Tailwind and shadcn, with Geist from Fontsource --
the stack `different-ai/openwork` runs in `apps/app`, which is where the tokens
above were read from. Not Next.js: openwork uses that for `apps/review` and its
marketing surfaces, and it would put a Node server inside the desktop app to
render a tool that is local and single-user.

Everything in openwork outside `/ee` is MIT, so components and tokens can be
lifted with the notice attached. `/ee` is a separate proprietary licence.

Python serves JSON; the built assets are static. One container, one server.

## Trade-offs

**It will look plainer than its competitors.** No charts, no scores, no
gradients, no sparkline next to every number. Products that have those demo
better. Steward's argument is that a maintainer opens it every morning rather
than once.

**Two type registers is a constraint that will chafe.** Somebody will want a
derived number inside a sentence, and the rule says the sentence is proportional
and the number is mono, which looks slightly wrong in the middle of prose. The
rule stays: the moment derived and generated content share a face, the boundary
is only a policy document again.

**Borrowing Primer's state colors ties us to GitHub's vocabulary.** If Steward
ever grows a state GitHub has no concept of, it has no color and will have to
earn one. That is a good problem — it means the state came from somewhere real.

**Slate plus a near-black accent is nearly monochrome.** In a screenshot Steward
looks austere next to a colorful dashboard. That is the point, and it is also a
genuine adoption cost, so it is written here as a decision rather than discovered
later as an accident.
