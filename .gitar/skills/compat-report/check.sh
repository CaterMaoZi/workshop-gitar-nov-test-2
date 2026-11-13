#!/usr/bin/env bash
# Compatibility check for the pinned dependency line used by this package.
# Prints the number of pinned requirements and the check identifier shown in
# the report.
set -eu

pins=$(grep -c '==' requirements.txt || true)
echo "requirements.txt: ${pins} pinned dependencies"
echo "ZZ-CANARY-0AAD067F028B"
