"""Signed gate codes for the boxoffice gate console.

The gate console verifies scanned ticket codes without a datastore lookup. A
code carries a signed payload produced with the service secret on the pinned
``itsdangerous`` line.
"""

from itsdangerous import BadSignature, URLSafeTimedSerializer

GATE_CODE_SALT = "boxoffice-gate-code-v1"


class GateCodeError(ValueError):
    """Raised when a scanned gate code is not valid."""


def _serializer(secret: str) -> URLSafeTimedSerializer:
    return URLSafeTimedSerializer(secret, salt=GATE_CODE_SALT)


def sign_gate_code(secret: str, ticket_id: str, event_id: str) -> str:
    """Return a signed gate code for one ticket."""
    return _serializer(secret).dumps({"ticket_id": ticket_id, "event_id": event_id})


def verify_gate_code(secret: str, code: str, max_seconds: int | None = None) -> dict:
    """Verify a signed gate code and return its payload.

    ``max_seconds=None`` keeps codes valid without an age limit; pass a positive
    number of seconds for codes that should expire.
    """
    max_age = None if max_seconds is None else int(max_seconds)
    try:
        payload = _serializer(secret).loads(code, max_age=max_age)
    except BadSignature as exc:
        raise GateCodeError("invalid gate code") from exc
    if not isinstance(payload, dict) or {"ticket_id", "event_id"} - payload.keys():
        raise GateCodeError("invalid gate payload")
    return payload
