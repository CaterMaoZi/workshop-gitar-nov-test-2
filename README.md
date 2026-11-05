# Gitar workshop: Boxoffice

Boxoffice is the ticketing API behind a small venue's website. Customers buy tickets, each ticket carries a QR code, and gate staff scan it at the door. In this workshop you open three pull requests in your own fork and watch [Gitar](https://gitar.ai), Sonar's AI code verification agent, review all three, apply fixes, and automate a merge. Findings and fixes can differ a little between runs.

| Stage | What you'll see | Branch |
|---|---|---|
| 1 | An out-of-the-box review, then a fix from one comment | `stage-1` |
| 2 | How a short `.gitar/` instruction and rule change a review | `stage-2` |
| 3 | A failing CI run, diagnosed, fixed, and merged from one comment | `stage-3` |

## Before you start

Use your personal GitHub account, and fork into it rather than into a company organization. Installing a GitHub App on an organization needs an owner's approval, and organizations can turn off Actions on forks. Gitar can also block sign-up from a brand-new GitHub account with no public repos or followers, so use an account you've had for a while.

Sign in at [app.gitar.ai](https://app.gitar.ai) first and start the GitHub install from there. Your 14-day Pro trial starts when you connect GitHub.

## Set up your fork

1. Fork this repo. **Uncheck "Copy the `main` branch only"**, then confirm your fork shows 4 branches.
2. In your fork, open the **Actions** tab and click **I understand my workflows, go ahead and enable them**.

## Connect Gitar

In Gitar, open **Settings > Configuration**, click **Refresh** under **Repositories**, and confirm your fork is listed. If it's missing, open GitHub's **Settings > Applications**, click **Configure** next to Gitar, add your fork, and refresh again.

## Open the three pull requests

Create each pull request through GitHub's form in your fork.

1. Open **Pull requests > New pull request**.
2. Select your fork for both **base repository** and **head repository**. Set **base** to `main` and **compare** to `stage-1`.
   GitHub can default **base repository** to the upstream `sonar-samples` repo, and the list also shows other people's forks, so pick the one under your username.
3. Click **Create pull request**. The branch's commit fills in the title and description so keep both and submit the pull request.
4. Repeat with **compare** set to `stage-2`, then `stage-3`, keeping your fork as both repositories and `main` as the base.

## Stage 1: out-of-the-box review, then `gitar fix`

Read the diff while Gitar reviews it, which can take several minutes. Find Gitar's inline finding and reply `gitar fix` in its thread. When Gitar's commit lands, open it, look at which files it changed, and check that CI is green. Don't merge this pull request.

## Stage 2: teach Gitar your team's rules

Before you read the review, open the pull request's **Files changed** tab and read the two files under `.gitar/`. Then read Gitar's finding and the comment the rule posted. In Gitar's dashboard comment, expand **Verification** to see the rule under **Rules**.

An instruction in `.gitar/review/` changes what the review looks for, while a rule in `.gitar/rules/` makes Gitar take an action when a pull request event matches. This stage is review only, so don't fix or merge it.

## Optional: merge controls for Stage 3

To run Stage 3's automated merge yourself, configure these now. Otherwise, just watch.

1. In your fork, open **Settings > General > Pull Requests** and check **Allow auto-merge**.
2. Open **Settings > Rules > Rulesets > New ruleset > New branch ruleset** and fill it in like this. Leave every field not listed at its default.

   | Field | Value |
   |---|---|
   | Ruleset name | `require-tests` |
   | Enforcement status | **Active** |
   | Bypass list | Empty |
   | Target branches | **Add target > Include default branch** |
   | Restrict deletions | Checked (default) |
   | Block force pushes | Checked (default) |
   | Require a pull request before merging | Unchecked |
   | Require status checks to pass | Checked |
   | Require branches to be up to date before merging | Unchecked |
   | Status checks | **Add checks**, type `test`, select **test** (GitHub Actions) |

   Then click **Create**. GitHub may ask you to confirm access with your password, passkey, or two-factor code before it saves the ruleset. If `test` doesn't show up in the search, run **Actions > Test > Run workflow** on `main` and search again.
3. In Gitar, open **Settings > Configuration**, find your fork under **Repositories**, and open its overrides from the **Overrides** column. Turn on **Auto-approve PRs based on code review**, and leave **Auto-merge PRs after auto-approve** off. That second toggle only appears once auto-approve is on. Use the fork's overrides rather than the **Behavior** settings on the same page, because those apply to every repository Gitar can see.

Leave Gitar's auto-merge setting off so Stages 1 and 2 stay open. Later, the `gitar auto-merge:on` command enables merging for the Stage 3 pull request. That command needs auto-approve on, and GitHub still waits for the required `test` check before it merges.

| Where | Setting | Value |
|---|---|---|
| GitHub, your fork | Allow auto-merge | On for the full Stage 3 cycle |
| Gitar, your fork's overrides | Auto-approve PRs based on code review | On |
| Gitar, your fork's overrides | Auto-merge PRs after auto-approve | Off |

## Stage 3: CI failure, then auto-apply and auto-merge

The pull request's `test` check fails. Read Gitar's CI analysis in its dashboard comment first, because applying the fix replaces it, then post one comment.

If you set up merge controls, comment both commands, one per line.

```text
gitar auto-apply:on
gitar auto-merge:on
```

Paste them exactly as shown. A space after the colon (`auto-apply: on`) means Gitar doesn't recognize the command.

Check that Gitar's commit changed application code. With merge controls configured, Gitar approves the code and GitHub waits for the required `test` check to turn green before merging.

## Troubleshooting

| Problem | What to do |
|---|---|
| Your fork only has `main` | Delete the fork (its **Settings** page, at the bottom), then fork again with **Copy the `main` branch only** unchecked |
| Pull request opened on `sonar-samples` instead of your fork, or Gitar says it isn't allowed to push to a forked pull request | Close it. Open **New pull request** again and select your fork for both **base repository** and **head repository** |
| Review is taking longer than expected | Check Gitar's dashboard. If a review is still running, wait for it to finish. If no review is running, comment `gitar review` |
| No `test` check on a pull request | Enable Actions in your fork, then close and reopen the pull request. If your organization has disabled Actions, fork into your personal account instead |
| Stage 3 shows no CI analysis | Comment `gitar review` |
| Stage 3 is approved but doesn't merge | Check GitHub's Allow auto-merge and required `test` check, auto-approve in your fork's Gitar overrides, and that your Stage 3 comment has no space after either colon |

## Take it further

- Stage 3 changes your `main` when it merges, so be aware of that if you want to re-run the workshop.
- To make the Stage 2 instruction and rule permanent, copy the `.gitar/` folder from the `stage-2` branch to `main` in your fork through a pull request. The instruction and rule then apply to every pull request. Add a rule of your own beside them.
- Gitar reads your coding agent's instruction files from the repo root: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and files one level deep in `.cursor/rules/` and `.claude/rules/`. Add an `AGENTS.md` with one team rule, open a pull request, and watch the review apply it.
- Add a skill at `.gitar/skills/<name>/SKILL.md` with `name` and `description` frontmatter, then trigger it: `gitar run the <name> skill on this`. Gitar also reads skills from `.claude/skills/`, `.agents/skills/`, and `.github/skills/`.
- Write approval criteria in `.gitar/config/approve.md` and merge criteria in `.gitar/config/merge.md`. Gitar reads `merge.md` from the default branch only, so a pull request can't grant itself auto-merge.
- Connect Slack or Jira under **Settings > Integrations**.
- Other useful commands are `gitar review`, `gitar display:verbose`, and `gitar auto-apply:off`.
- Enterprise adds features including knowledge with citations, cross-repo and cross-PR analysis, and functional validation against linked issues.
