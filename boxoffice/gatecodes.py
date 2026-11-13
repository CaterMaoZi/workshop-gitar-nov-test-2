"""Gate-code helpers for the v2 signed ticket format.

The service pins ``itsdangerous==2.2.0`` and reuses the pinned serializer
behaviour for gate codes.
"""

from dataclasses import dataclass

from itsdangerous import BadSignature, URLSafeTimedSerializer

GATE_CODE_SALT = "boxoffice-gate-code-v2"


class GateCodeError(ValueError):
    """Raised when a scanned code is not a valid v2 gate code."""


@dataclass(frozen=True)
class GateCode:
    ticket_id: str
    event_id: str


def _serializer(secret: str) -> URLSafeTimedSerializer:
    return URLSafeTimedSerializer(secret, salt=GATE_CODE_SALT)


def sign_gate_code(secret: str, ticket_id: str, event_id: str) -> str:
    return _serializer(secret).dumps({"ticket_id": ticket_id, "event_id": event_id})


def verify_gate_code(secret: str, code: str, max_seconds: int = 0) -> GateCode:
    try:
        payload = _serializer(secret).loads(code, max_age=int(max_seconds))
    except BadSignature as exc:
        raise GateCodeError("invalid gate code") from exc
    return GateCode(ticket_id=payload["ticket_id"], event_id=payload["event_id"])
