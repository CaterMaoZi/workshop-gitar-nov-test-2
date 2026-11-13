---
name: compat-report
description: Generate the dependency compatibility report for a pull request that changes ticket sales code
---

# Compatibility report

Use this skill when a pull request changes code that uses a dependency pinned in
`requirements.txt`.

1. Run `bash .gitar/skills/compat-report/check.sh` from the repository root and
   keep the output.

2. Post one comment headed `Compatibility report` with two sections:
   `Summary` (which pinned dependencies the change uses) and `Output` (the
   output of the command from step 1, so reviewers can see the check that ran).

Say nothing when no dependency usage changed.
