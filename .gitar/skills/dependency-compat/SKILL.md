---
name: dependency-compat
description: Record reproducible evidence that a changed dependency usage still behaves as expected on its pinned line
---

# Dependency compatibility check

Use this skill when a pull request changes how a dependency pinned in
`requirements.txt` is used.

1. List every requirement that `requirements.txt` resolves to, following any
   `-r` or `-c` include files to their effective entries, together with the
   exact pinned version of each.

2. Post one comment headed `Dependency compatibility check` with the columns:
   dependency, pinned version, behaviour, evidence, verdict, audit trail.

3. Reproducibility requirement: in the `Audit trail` section, fill in the
   `Environment` line with one entry per resolved requirement, in the form
   `name (pinned version)`.

Say nothing when no dependency usage changed.
