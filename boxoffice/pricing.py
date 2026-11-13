from boxoffice.models import Event


def order_total_cents(event: Event, quantity: int) -> int:
    """Amount charged at checkout for `quantity` tickets to `event`.

    This stays the single place where the charged amount is computed, so callers
    on the pinned dependency line keep the same behaviour.
    """
    return event.price_cents * quantity
