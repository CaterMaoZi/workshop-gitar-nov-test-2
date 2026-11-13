# Gitar workshop: Boxoffice

Boxoffice is the ticketing API behind a small venue's website. Customers buy tickets, each ticket carries a QR code, and gate staff scan it at the door. In this workshop you open three pull requests in your own fork and watch [Gitar](https://gitar.ai), Sonar's AI code verification agent, review all three, apply fixes, and automate a merge. Findings and fixes can differ a little between runs.

| Stage | What you'll see | Branch |
|---|---|---|
| 1 | An out-of-the-box review, then a fix from one comment | `stage-1` |
| 2 | How a short `.gitar/` instruction and rule change a review | `stage-2` |
| 3 | A failing CI run, diagnosed, fixed, and merged from one comment | `stage-3` |

Gitar talks to you in two places on each pull request. Its dashboard comment is one summary comment on the **Conversation** tab, and Gitar keeps editing it as the review goes. An inline finding is a comment Gitar leaves on a specific line of code, and it can show up above the dashboard comment, so scroll the whole tab.

Joining late? Do everything up to and including "Open the three pull requests", then pick up at whichever stage the presenter is on. The stages don't depend on each other.

## Before you start

Fork into your personal GitHub account rather than a company organization. An organization owner has to approve the Gitar install there, and organizations can turn off Actions on forks. Pick an account you've had for a while, because Gitar may not let a GitHub account that's under a week old, with no repos or followers, sign up.

Sign in at [app.gitar.ai](https://app.gitar.ai) first and connect GitHub from inside Gitar, so the install is linked to your Gitar account. Gitar shows your workspace name at the top left. If that's your company's workspace, ask the presenter before you connect anything. Eligible new Gitar organizations get a 14-day Pro trial that starts when you connect GitHub.

If GitHub asks which repositories Gitar can access, either choice works. With **All repositories**, your fork shows up in Gitar after you click **Refresh**. With **Only select repositories**, you'll add the fork in "Connect Gitar to your fork" below.

## Set up your fork

1. On this repo's page, click **Fork**. Keep the repository name, uncheck **Copy the `main` branch only** (it starts checked), and click **Create fork**. Your fork's page should show **4 branches**.
2. In your fork, open the **Actions** tab and click **I understand my workflows, go ahead and enable them**. You should see a workflow called **Test** in the list.

## Connect Gitar to your fork

1. In Gitar, click the gear icon to open **Settings**, then open **Configuration**.
2. Under **Repositories**, click **Refresh**, then type `workshop-gitar-nov` in **Search repositories...**. The list doesn't show every repository at once, so search instead of scrolling. You should see `<your-username>/workshop-gitar-nov` with its **Enabled** box checked. Leave the **Disable all** button next to **Refresh** alone.

If your fork isn't listed, open GitHub's **Settings > Applications > Installed GitHub Apps**, click **Configure** next to Gitar, add your fork to the repositories Gitar can access, save, and click **Refresh** in Gitar again.

## Open the three pull requests

GitHub's form often points at the upstream `sonar-samples` repo, so check where each pull request will land before you create it.

1. In your fork, open **Pull requests > New pull request**.
2. If you see a **base repository** dropdown, set it to your fork. The list also shows other people's forks, so pick the one under your username.
3. Set **base** to `main` and **compare** to `stage-1`. Before you click **Create pull request**, look at the top left of the page: it must read `<your-username> / workshop-gitar-nov`. If it reads `sonar-samples / workshop-gitar-nov`, go back to step 1.
4. Click **Create pull request**. GitHub fills in the title and description from the branch's commit. Keep both and click **Create pull request** again.
5. Under the new pull request's title, GitHub should say it merges into `main` from `stage-1`. If it says `sonar-samples:main` instead, close that pull request and start again from step 1.
6. Repeat steps 1 to 5 with **compare** set to `stage-2`, then `stage-3`.

You should now have three open pull requests in your fork. Their numbers may not match the stage numbers, so tell them apart by title, or by the `stage-N` branch shown under the title. Within a minute each one shows a `test` check: green on Stages 1 and 2, red on Stage 3. Gitar starts reviewing all three on its own.

## Stage 1: out-of-the-box review, then `gitar fix`

Read the diff while Gitar reviews it. Gitar's first review usually lands in two or three minutes, sometimes up to five, as a dashboard comment plus an inline finding.

On the **Conversation** tab, find Gitar's inline finding, type `gitar fix` in the **Reply** box under it, and click **Comment**. Within a couple of minutes you should see a new commit from Gitar on the pull request. Open that commit and check which files it changed and whether its `test` check is green. Leave this pull request open and unmerged.

## Stage 2: teach Gitar your team's rules

Before you read the review, open the pull request's **Files changed** tab and read the two files under `.gitar/`.

An instruction in `.gitar/review/` changes what the review looks for. A rule in `.gitar/rules/` makes Gitar take an action when a pull request event matches, and the action here is posting a comment.

Back on the **Conversation** tab, you should see Gitar's inline finding, which cites the instruction file, and a separate comment that the rule posted. The finding's label (Bug, for example) may not use the instruction file's wording. In the dashboard comment, expand **Verification**. The **Rules** row only counts what the rules did, for example "1 action taken", and the rule's separate comment is that action.

Stage 2 is review only, so don't fix or merge it.

## Optional: merge controls for Stage 3

To run Stage 3's automated merge yourself, configure these now. Otherwise, watch the presenter's screen.

1. In your fork, open **Settings > General**, scroll to **Pull Requests**, and check **Allow auto-merge**.
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

   Click **Create**. GitHub may ask you to confirm access with your password, passkey, or two-factor code before it saves the ruleset. You should then see `require-tests` in the rulesets list. If `test` doesn't show up in the search, run **Actions > Test > Run workflow** on `main` and search again.
3. In Gitar, open **Settings > Configuration** and search for your fork under **Repositories**. In the **Overrides** column at the right end of its row, click the small sliders icon to open **Configure repository overrides**.
4. Turn on **Auto-approve PRs based on code review**. More toggles appear under it, such as **Auto-merge PRs**. Leave those off. Changes save automatically. Click **Done** to close the dialog.

The **Behavior** section on the main Configuration page has the same auto-approve toggle, but it applies to every repository Gitar can see, so use your fork's overrides.

Gitar's auto-merge toggle stays off so Stages 1 and 2 stay open. In Stage 3, the `gitar auto-merge:on` command turns on merging for that pull request only. The command needs auto-approve on, and GitHub still waits for the required `test` check before it merges.

| Where | Setting | Value |
|---|---|---|
| GitHub, your fork | Allow auto-merge | On |
| Gitar, your fork's overrides | Auto-approve PRs based on code review | On |
| Gitar, your fork's overrides | Toggles that appear under auto-approve | Off |

## Stage 3: CI failure, then auto-apply and auto-merge

The pull request's `test` check is red. Open Gitar's dashboard comment and read its analysis of the failed CI run first, because applying the fix replaces it.

If you set up merge controls, post one new comment on the **Conversation** tab with both commands, one per line. Use the copy button on the block.

```text
gitar auto-apply:on
gitar auto-merge:on
```

Paste them exactly as shown. With a space after the colon (`auto-apply: on`), Gitar doesn't recognize the command.

Within a few minutes Gitar pushes a fix commit, its dashboard comment changes from **Blocked** to **Approved**, and the pull request's timeline shows Gitar enabling auto-merge. Once the `test` check on Gitar's commit turns green, GitHub marks the pull request **Merged**. Open Gitar's commit and check that it changed application code.

## Troubleshooting

| Problem | What to do |
|---|---|
| Your fork only has `main` | Delete the fork (its **Settings** page, at the bottom), then fork again with **Copy the `main` branch only** unchecked |
| Pull request opened on `sonar-samples` instead of your fork, or Gitar says it isn't allowed to push to a forked pull request | Close it. Open **New pull request** in your fork again, and check that the top left reads `<your-username> / workshop-gitar-nov` before you create it |
| No Gitar comment after five minutes | If the dashboard comment shows a review running, wait for it. If there's no Gitar comment at all, check that your fork is **Enabled** under **Repositories** in Gitar, then comment `gitar review` |
| No `test` check on a pull request | Enable Actions in your fork, then close and reopen the pull request. If your organization has disabled Actions, fork into your personal account instead |
| Stage 3 shows no CI analysis | Comment `gitar review` |
| Stage 3 command did nothing | Post the two lines again as a new comment, copied from this README, with no space after either colon |
| Stage 3 is approved but doesn't merge | Check GitHub's **Allow auto-merge**, that `require-tests` is **Active** and requires `test`, and auto-approve in your fork's Gitar overrides |

## Run the checks locally

You can run the same checks the **Test** workflow runs before you open a pull request:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The API lives in `boxoffice/` and the test suite in `tests/`, so both commands work from the repository root.

## Take it further

- Stage 3 merges into your fork's `main`, so a re-run starts from the changed `main`.
- To make the Stage 2 instruction and rule permanent, copy the `.gitar/` folder from the `stage-2` branch to `main` in your fork through a pull request. The instruction and rule then apply to every pull request. Add a rule of your own beside them.
- Gitar reads your coding agent's instruction files from the repo root: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and files one level deep in `.cursor/rules/` and `.claude/rules/`. Add an `AGENTS.md` with one team rule, open a pull request, and watch the review apply it.
- Add a skill at `.gitar/skills/<name>/SKILL.md` with `name` and `description` frontmatter, then trigger it: `gitar run the <name> skill on this`. Gitar also reads skills from `.claude/skills/`, `.agents/skills/`, and `.github/skills/`.
- Write approval criteria in `.gitar/config/approve.md` and merge criteria in `.gitar/config/merge.md`. Gitar reads `merge.md` from the default branch only, so a pull request can't grant itself auto-merge.
- Connect Slack or Jira under **Settings > Integrations**.
- Other useful commands are `gitar review`, `gitar display:verbose`, and `gitar auto-apply:off`.
- Enterprise adds knowledge with citations, cross-repo and cross-PR analysis, and functional validation against linked issues.
