# Runtime configuration

Boxoffice keeps no external configuration files. `boxoffice.create_app()` builds the
in-memory store and the payment stand-in itself, and tests inject a deterministic
clock. This page lists the settings that exist today and notes where the automated
review pipeline keeps its own configuration.

## Application settings

| Setting | Where it is set | Purpose |
| - | - | - |
| `app.config["CLOCK"]` | `boxoffice.create_app(clock=...)` | Supplies the current time; tests pass a fixed clock |
| `app.extensions["boxoffice.store"]` | `boxoffice.create_app()` | In-memory event, order and ticket store |
| `app.extensions["boxoffice.payments"]` | `boxoffice.create_app()` | Stand-in card processor that records charges |
| `DEV_TOKENS` | `boxoffice/auth.py` | Bearer tokens accepted in local development |

## Pricing and limits

| Constant | Value | Purpose |
| - | - | - |
| `MAX_TICKETS_PER_ORDER` | 8 | Upper bound on tickets in a single order |
| `Event.price_cents` | per event | Base ticket price, in cents |

## Review pipeline configuration

The automated review pipeline keeps its own runtime configuration in the Gitar
organization settings, outside this repository. The relevant items are the gateway
configuration that routes model calls, the model alias requested for each task, and
an optional model version pin. Repository-side configuration is limited to the
`.gitar/` directory described in the repository customization documentation. This
repository does not declare a model or a gateway of its own.
