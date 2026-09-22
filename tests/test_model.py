"""Contracts in `model.py` that nothing else checks."""

from __future__ import annotations

import json

import pytest
from hypothesis import given
from hypothesis import strategies as st

from steward.model import (
    PAYLOAD_FOR,
    ActorRef,
    ActorType,
    CommitPayload,
    CrossReferencePayload,
    DismissalPayload,
    EventKind,
    IssueStateReason,
    LabelPayload,
    Payload,
    PullRequestReviewState,
    ReviewPayload,
    StateReasonPayload,
    SubjectType,
    payload_from_dict,
    payload_to_dict,
    validate_payload,
)

# Four kinds declare ActorRef, so this keeps whichever comes last. Any kind that
# declares a shape decodes it the same way; the mapping only has to pick one.
KIND_FOR = {shape: kind for kind, shape in PAYLOAD_FOR.items() if shape is not None}

PAYLOADS = st.one_of(
    st.builds(ActorRef, name=st.text(), type=st.sampled_from(ActorType)),
    st.builds(ReviewPayload, state=st.sampled_from(PullRequestReviewState)),
    st.builds(
        DismissalPayload,
        previous_state=st.sampled_from(PullRequestReviewState),
        review_id=st.text(),
    ),
    st.builds(LabelPayload, name=st.text()),
    st.builds(CommitPayload, oid=st.text()),
    st.builds(
        CrossReferencePayload,
        source_type=st.sampled_from(SubjectType),
        source_number=st.integers(),
    ),
    st.builds(StateReasonPayload, reason=st.sampled_from(IssueStateReason)),
)


def test_payload_for_covers_every_kind() -> None:
    # PAYLOAD_FOR is a contract only if it is total. Adding a kind and forgetting
    # its payload type-checks and passes CI; it surfaces as a KeyError in the
    # normalizer, against a real repository, on a sync that is rate-limited.
    assert set(PAYLOAD_FOR) == set(EventKind)


def test_validate_payload_accepts_the_declared_shape() -> None:
    validate_payload(EventKind.LABELED, LabelPayload("lgtm"))


def test_validate_payload_rejects_another_kinds_shape() -> None:
    with pytest.raises(ValueError, match="LABELED carries LabelPayload"):
        validate_payload(EventKind.LABELED, CommitPayload("abc123"))


def test_validate_payload_rejects_a_payload_on_a_kind_that_carries_none() -> None:
    with pytest.raises(ValueError, match="MERGED carries no payload"):
        validate_payload(EventKind.MERGED, LabelPayload("lgtm"))


def test_validate_payload_accepts_none_for_every_kind() -> None:
    # Including the kinds that declare a shape: a pull request closes with no
    # reason, so None has to be legal wherever a payload is optional in practice.
    for kind in EventKind:
        validate_payload(kind, None)


@given(PAYLOADS)
def test_payload_round_trips(payload: Payload) -> None:
    # Through json, not just through the dict: the column is JSONB, so a value
    # that dict equality accepts but the serializer does not would pass a test
    # that stopped at payload_to_dict.
    assert payload is not None  # PAYLOADS builds shapes; None has its own test
    row = json.loads(json.dumps(payload_to_dict(payload)))
    assert payload_from_dict(KIND_FOR[type(payload)], row) == payload


def test_absent_payload_round_trips_as_empty() -> None:
    assert payload_to_dict(None) == {}
    for kind in EventKind:
        assert payload_from_dict(kind, {}) is None


def test_payload_from_dict_names_the_missing_field() -> None:
    with pytest.raises(ValueError, match="payload needs review_id"):
        payload_from_dict(EventKind.REVIEW_DISMISSED, {"previous_state": "APPROVED"})


def test_payload_from_dict_rejects_a_value_outside_the_enum() -> None:
    with pytest.raises(ValueError, match="APPROVEED"):
        payload_from_dict(EventKind.REVIEW, {"state": "APPROVEED"})
