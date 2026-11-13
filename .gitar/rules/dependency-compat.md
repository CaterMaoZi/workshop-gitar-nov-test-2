---
title: "Dependency compatibility check"
description: "Verify changed dependency behaviour against the pinned line's compatibility matrix"
type: automation
when: "A pull request is opened or updated and changes how a dependency pinned in requirements.txt is used, including new imports, call signatures, or version pins"
actions: "Use the dependency-compat skill, then post one pull request comment headed 'Dependency compatibility check'"
---

# Dependency compatibility check

When this pull request changes how a dependency pinned in `requirements.txt` is
used, run the `dependency-compat` skill and post its result in a comment headed
`Dependency compatibility check`.

For every behaviour the change relies on, name the matrix row you checked and
the URL you read it from. Record the audit trail produced by the skill script.
Do not modify code and do not add labels.
