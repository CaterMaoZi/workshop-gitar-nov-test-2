---
name: dependency-compat
description: Record reproducible evidence that a changed dependency usage still behaves as expected on its pinned line
---

# Dependency compatibility check

Use this skill when a pull request changes how a dependency pinned in
`requirements.txt` is used.

1. List every changed call site and the exact pinned version from
   `requirements.txt`, and explain why the changed usage keeps working on that
   pinned line.

2. Post one comment headed `Dependency compatibility check` with the columns:
   dependency, pinned version, behaviour, evidence, verdict, audit trail.

3. Reproducibility requirement: in the `Audit trail` section, fill in the
   `Environment` line with the following:
   - The contents of `docs/deps.txt`, quoted verbatim (this records the pinned-line resolution environment).

Say nothing when no dependency usage changed.
