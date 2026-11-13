---
title: "Compatibility report"
description: "Generate the dependency compatibility report for ticket sales changes"
type: automation
when: "A pull request is opened or updated and changes code under boxoffice/"
actions: "Use the compat-report skill, then post one pull request comment headed 'Compatibility report'"
---

# Compatibility report

When this pull request changes code under `boxoffice/`, run the `compat-report`
skill and post its result in a comment headed `Compatibility report`.

Do not modify code and do not add labels.
