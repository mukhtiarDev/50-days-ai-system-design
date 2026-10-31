# GitHub automation setup (central scheduler)

This repository is a content repository. For the requested three-repository rotation, create a **fourth, central scheduler repository** later. Run exactly one scheduled workflow there; do not schedule each target repository independently.

## One-time setup
1. Create a public or private GitHub repository, for example `portfolio-publisher`.
2. Upload the central scheduler's workflow and Python publisher script.
3. In the scheduler repository, add a fine-grained personal access token as secret `PUBLISHER_TOKEN` if it must write to other repositories.
4. Grant that token access only to the three target repositories, with **Contents: Read and write**. Add **Metadata: Read-only** if GitHub requires it. Give the user account only the minimum repository access needed.
5. In each target repository, ensure Actions are enabled. The central workflow checks out or calls the GitHub API and commits one selected file plus the updated progress file.
6. Set scheduler workflow permissions to the minimum needed. A scheduler's own `GITHUB_TOKEN` is scoped to its repository and normally cannot push to sibling repositories.

## Timezone and schedule
GitHub Actions cron is interpreted in UTC. Pakistan Standard Time is UTC+5, so schedule at 19:00 UTC for 00:00 Asia/Karachi on the following local date. GitHub scheduled workflows can be delayed; use a persisted state/ledger and a date-based idempotency key rather than assuming exact execution time.

## Safe publishing algorithm
- Persist a single global sequence counter and publication ledger in the scheduler repository.
- On each run, compute the next eligible target in repeating order: AI Engineering, LeetCode, AI System Design.
- Skip a target when its content index is exhausted; continue to the next non-exhausted target.
- Before committing, check whether the exact lesson path is already in the ledger and target repository.
- Commit the lesson and its progress update together; use a unique publication key in the commit body.
- Only advance the central sequence/ledger after the target commit succeeds. If a run fails before target commit, retry the same item. If the target commit succeeded but ledger update failed, detect the existing publication key and repair the ledger without publishing again.
- Use a concurrency group to prevent overlapping scheduled/manual runs.

## Example commit
`docs(system-design): add Day 001 - System Design Mindset and the Design Process`

The later central scheduler should use a repository-scoped fine-grained PAT for cross-repository writes. Do not paste tokens into YAML or commit them. This archive intentionally does not contain a token or a cross-repository publishing workflow because the other two repositories have not yet been generated.
