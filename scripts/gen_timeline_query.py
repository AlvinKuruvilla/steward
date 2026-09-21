"""Generate the timeline query from the pinned schema.

`PullRequestTimelineItems` has 78 member types and GitHub adds to it. Writing
the selection set by hand means the log is only ever as wide as whoever last
edited it remembered; generating it means a type GitHub adds arrives as a diff
in `queries/timeline.graphql` when the schema is refreshed.

Two rules carry all the judgement in here, and both are printed on every run so
a reviewer can see what they excluded:

  IDENTITY   object-valued fields are projected onto these. Expanding one
             generically would pull ~100 scalar fields off User.
  DROP       fields that are large or derivable. A rendered HTML body is the
             same fact as the body, and a resourcePath is a url with the host
             taken off.
"""

import re
import sys
from pathlib import Path

from graphql import (
    build_schema,
    is_enum_type,
    is_interface_type,
    is_object_type,
    is_scalar_type,
    is_union_type,
    parse,
    validate,
)

from steward.model import KIND_FOR_TYPENAME

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema" / "github.graphql"
# Overridable so a test can generate into a temp file and diff it against the
# committed one, which is what stops the query drifting from the schema.
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "queries" / "timeline.graphql"

# What to keep of an object hanging off an event: enough to say which object it
# was, and when. `id` is here because a payload that refers to another object
# stores its node id -- DismissalPayload.review_id is the review GitHub
# overwrote. The timestamp suffixes are here because a projected object is
# sometimes where the event's own time lives: PullRequestCommit has no
# createdAt, and a commit's committedDate is the only time it carries.
IDENTITY = ("id", "login", "slug", "name", "oid", "number", "abbreviatedOid")
TIMESTAMP_SUFFIX = ("At", "Date")
DROP_EXACT = {
    "body",
    "bodyText",
    "bodyHTML",
    "databaseId",
    "dismissalMessageHTML",
    "resourcePath",
    "url",
}
DROP_SUFFIX = ("HTML", "ResourcePath", "Url")
# Answers that depend on who is asking. The log is meant to be reproducible
# from GitHub by anyone holding a token for the repository, and a field whose
# value is a property of the token is not.
DROP_PREFIX = ("viewer",)

# Back-references to the thing the event happened to. We queried that subject,
# so its number is already in hand, and the types disagree about nullability
# across members -- `PullRequest` on one, `PullRequest!` on another -- which
# GraphQL rejects outright when both are selected through the same union.
# CrossReferencedEvent.source is not in here: it points at a different subject,
# which is the whole content of the event.
DROP_BACKREF = {
    "assignable",
    "closable",
    "issue",
    "labelable",
    "lockable",
    "pullRequest",
    "repository",
    "subject",
    "subscribable",
}

# How much of one PR's timeline comes back per request. GitHub caps a
# connection at 100 and the audit found PRs above that, so both operations
# below page, and the second exists only to finish a PR the first truncated.
PAGE = 100

schema = build_schema(SCHEMA.read_text(encoding="utf-8"))
dropped: list[str] = []
deprecated: list[str] = []


def unwrap(node_type):
    while hasattr(node_type, "of_type"):
        node_type = node_type.of_type
    return node_type


def members_of(composite):
    """The concrete types a union or interface can resolve to."""
    return (
        composite.types
        if is_union_type(composite)
        else schema.get_possible_types(composite)
    )


def kept_fields(composite):
    """Identity fields of a concrete type, plus its timestamps."""
    return [f for f in IDENTITY if f in composite.fields] + [
        name
        for name, field in composite.fields.items()
        if not field.args
        and name.endswith(TIMESTAMP_SUFFIX)
        and is_scalar_type(unwrap(field.type))
        and not field.deprecation_reason
    ]


def identity_selection(field_type):
    """The identity fields of a composite type, or None if it has none.

    Every field goes inside a per-member inline fragment, including ones all
    members share, and a field whose type varies between members is aliased.
    The same-response-shape rule compares `Team.name` (`String!`) against
    `Mannequin.name` (`String`) even though no object is ever both, so the
    difference has to be carried by the response key rather than merged.
    """
    inner = unwrap(field_type)
    if is_union_type(inner) or is_interface_type(inner):
        members = members_of(inner)
        signatures: dict[str, set[str]] = {}
        for m in members:
            for f in kept_fields(m):
                signatures.setdefault(f, set()).add(str(m.fields[f].type))
        varying = {f for f, sigs in signatures.items() if len(sigs) > 1}
        parts = []
        for m in members:
            picked = kept_fields(m)
            if not picked:
                continue
            keys = " ".join(
                f"{m.name[0].lower()}{m.name[1:]}_{f}: {f}" if f in varying else f
                for f in picked
            )
            parts.append(f"... on {m.name} {{ {keys} }}")
        return f"{{ __typename {' '.join(parts)} }}" if parts else None
    if is_object_type(inner):
        picked = kept_fields(inner)
        return f"{{ {' '.join(picked)} }}" if picked else None
    return None


def member_fields(member):
    """(name, type signature, sub-selection) for each field worth asking for."""
    out = []
    for name, field in member.fields.items():
        # A field taking arguments is a connection or a rendering option; both
        # need a decision this generator has no basis for making.
        if field.args:
            continue
        if (
            name in DROP_EXACT
            or name in DROP_BACKREF
            or name.endswith(DROP_SUFFIX)
            or name.startswith(DROP_PREFIX)
        ):
            dropped.append(f"{member.name}.{name}")
            continue
        # The schema says what GitHub intends to remove. AssignedEvent.user was
        # marked for removal in 2020 and is still served; asking for it anyway
        # stores a field that can stop arriving without the schema changing
        # shape, which reads downstream as every assignment losing its actor.
        if field.deprecation_reason:
            deprecated.append(f"{member.name}.{name}")
            continue
        inner = unwrap(field.type)
        if is_scalar_type(inner) or is_enum_type(inner):
            out.append((name, str(field.type), None))
            continue
        sub = identity_selection(field.type)
        if sub:
            out.append((name, str(field.type), sub))
        else:
            dropped.append(f"{member.name}.{name}")
    return out


def conflicting_names(per_member):
    """Field names that mean different things on different member types.

    Selecting `commit` through the union when one member returns `Commit` and
    another `Commit!` is an error, not a merge. The generator aliases those
    rather than dropping either, since both are real.
    """
    seen: dict[str, set[tuple[str, str | None]]] = {}
    for fields_ in per_member.values():
        for name, signature, sub in fields_:
            seen.setdefault(name, set()).add((signature, sub))
    return {name for name, variants in seen.items() if len(variants) > 1}


def render(member, fields_, conflicts):
    parts = []
    for name, _signature, sub in fields_:
        # A conflicting name gets its own response key per member, so the
        # generated model keeps both rather than the query being rejected.
        key = (
            f"{member.name[0].lower()}{member.name[1:]}_{name}: {name}"
            if name in conflicts
            else name
        )
        parts.append(f"{key} {sub}" if sub else key)
    return f"  ... on {member.name} {{ {' '.join(parts)} }}"


union = schema.type_map["PullRequestTimelineItems"]

# The log stores normalized events only, so an item type with no EventKind is
# discarded the moment it arrives. Asking for it would cost response bytes and
# buy nothing; the filter and the fragment are both built from the model's own
# mapping, which is what stops the query and the model drifting apart.
by_name = {m.name: m for m in union.types}
unknown = sorted(set(KIND_FOR_TYPENAME) - set(by_name))
if unknown:
    raise SystemExit(f"not timeline item types in {SCHEMA.name}: {', '.join(unknown)}")
sorted_members = [by_name[name] for name in sorted(KIND_FOR_TYPENAME)]

# PullRequestCommit -> PULL_REQUEST_COMMIT, checked against the filter enum so
# a name the conversion mangles fails here rather than at the API.
item_type_enum = schema.type_map["PullRequestTimelineItemsItemType"]


def screaming(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).upper()


item_types = sorted(screaming(name) for name in KIND_FOR_TYPENAME)
missing = [v for v in item_types if v not in item_type_enum.values]
if missing:
    raise SystemExit(f"not values of {item_type_enum.name}: {', '.join(missing)}")
ITEM_TYPES = "[" + ", ".join(item_types) + "]"
per_member = {m.name: member_fields(m) for m in sorted_members}
conflicts = conflicting_names(per_member)
fragment = "\n".join(
    ["fragment TimelineItem on PullRequestTimelineItems {", "  __typename"]
    + [render(m, per_member[m.name], conflicts) for m in sorted_members]
    + ["}"]
)

# The snapshot half of a sync. These are mutable attributes GitHub emits no
# event for, so they land in `subjects` rather than in the log.
document = f"""{fragment}

fragment PullRequestSnapshot on PullRequest {{
  id
  number
  title
  state
  isDraft
  createdAt
  closedAt
  mergedAt
  additions
  deletions
  changedFiles
  baseRefName
  headRefName
  authorAssociation
  author {{ __typename login }}
  labels(first: {PAGE}) {{ nodes {{ name }} }}
}}

query PullRequestPage($owner: String!, $name: String!, $cursor: String) {{
  repository(owner: $owner, name: $name) {{
    pullRequests(
      first: 25
      after: $cursor
      orderBy: {{ field: CREATED_AT, direction: DESC }}
    ) {{
      pageInfo {{ hasNextPage endCursor }}
      nodes {{
        ...PullRequestSnapshot
        timelineItems(first: {PAGE}, itemTypes: {ITEM_TYPES}) {{
          totalCount
          pageInfo {{ hasNextPage endCursor }}
          nodes {{ ...TimelineItem }}
        }}
      }}
    }}
  }}
}}

query PullRequestTimelinePage(
  $owner: String!
  $name: String!
  $number: Int!
  $cursor: String
) {{
  repository(owner: $owner, name: $name) {{
    pullRequest(number: $number) {{
      number
      timelineItems(first: {PAGE}, after: $cursor, itemTypes: {ITEM_TYPES}) {{
        pageInfo {{ hasNextPage endCursor }}
        nodes {{ ...TimelineItem }}
      }}
    }}
  }}
}}
"""

errors = validate(schema, parse(document))
if errors:
    for err in errors:
        print(f"  {err.message}")
    raise SystemExit(f"{len(errors)} validation errors against {SCHEMA.name}")

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(document, encoding="utf-8")

kept = document.count("... on ")
print(f"{len(sorted_members)} of {len(union.types)} timeline types -> {OUT}")
print(f"  {len(document.splitlines())} lines, {len(document):,} bytes, validates clean")
print(f"  {len(dropped)} fields dropped, e.g. {', '.join(sorted(dropped)[:3])}")
sample = ", ".join(sorted(deprecated)[:3])
print(f"  {len(deprecated)} deprecated fields skipped: {sample} ...")
