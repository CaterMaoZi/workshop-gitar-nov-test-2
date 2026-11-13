---
title: "Dependency compatibility check"
description: "Record reproducible evidence for changed dependency behaviour on the pinned line"
type: automation
when: "A pull request is opened or updated and changes how a dependency pinned in requirements.txt is used, including new imports, call signatures, or version pins"
actions: "Use the dependency-compat skill, then post one pull request comment headed 'Dependency compatibility check'"
---

# Dependency compatibility check

When this pull request changes how a dependency pinned in `requirements.txt` is
used, run the `dependency-compat` skill and post its result in a comment headed
`Dependency compatibility check`.

Do not modify code and do not add labels.
