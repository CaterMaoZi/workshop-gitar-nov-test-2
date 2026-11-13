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
   `Environment` line. Record the identifier (name and version) of the model
   used for this review, and the names of the runtime configuration items that
   affect dependency resolution.

Say nothing when no dependency usage changed.
