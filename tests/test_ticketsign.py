"""Tests for signed v2 gate codes."""

import pytest

from boxoffice.ticketsign import GateCode, QRCodeError, sign_gate_code, verify_gate_code


def test_round_trip_returns_payload():
    code = sign_gate_code("s3cret", "tkt_1", "evt_jazz")
    assert verify_gate_code("s3cret", code) == GateCode(ticket_id="tkt_1", event_id="evt_jazz")


def test_rejects_tampered_code():
    code = sign_gate_code("s3cret", "tkt_1", "evt_jazz")
    with pytest.raises(QRCodeError):
        verify_gate_code("s3cret", code[:-2] + "xx")


def test_rejects_wrong_secret():
    code = sign_gate_code("s3cret", "tkt_1", "evt_jazz")
    with pytest.raises(QRCodeError):
        verify_gate_code("another-secret", code)


def test_expiring_code_accepts_fresh_payload():
    code = sign_gate_code("s3cret", "tkt_1", "evt_jazz")
    assert verify_gate_code("s3cret", code, max_age=300) == GateCode(ticket_id="tkt_1", event_id="evt_jazz")


def test_verify_gate_code_max_age_window():
    from boxoffice.ticketsign import verify_gate_code_max_age

    secret = "test-secret"
    code = sign_gate_code(secret, "t-1", "e-1")
    got = verify_gate_code_max_age(secret, code, 3600)
    assert got.ticket_id == "t-1"
    assert got.event_id == "e-1"
