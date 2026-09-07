---
name: review-and-resolve
description: Review software changes against requirements and correctness, then evaluate and resolve findings with evidence. Use for meaningful feature changes, risky fixes, or requested reviews, including uncommitted work.
---

# Review and resolve

Keep finding defects and resolving findings as distinct phases. Do not silently turn a read-only review request into an edit request.

## Establish the candidate

Identify the requested repository/worktree, comparison baseline, original requirements and accepted changes, relevant project rules, and actual files under review. Include committed, staged, unstaged, and relevant untracked work when those belong to the requested candidate; a comparison ending at HEAD excludes working changes. Preserve unrelated user work. Resolve ambiguous ownership before altering it.

Record the candidate commit and, for working changes, a snapshot or content digests sufficient to detect changes during review. Use an existing diff/review mechanism rather than building a tracking system. Read surrounding code and relevant callers where needed; a diff alone may omit the defect's cause or effect.

## Independent review

If you are the delegated reviewer, perform only the assigned read-only review and return findings; do not delegate again or enter the resolution phase. When the host provides a built-in defect-review skill, reuse its defect discipline and add the accepted-requirement and evidence checks needed here. Do not mistake a defect-only verdict for full specification coverage.

For consequential changes such as authorization, persistent state, external side effects, or broad shared behavior, use a fresh reviewer when delegation is available and authorized. Low-risk localized work can use labeled self-review unless project rules require independence. Supply the candidate, original requirements, accepted amendments, and raw evidence—not a verdict to endorse. One fresh reviewer is the default; split specialized reviews only when the scope warrants it. If independence is unavailable, label the review as self-review and follow any project requirement that prohibits self-approval.

Assess:
- Missing, partial, or unrequested behavior against the current accepted contract.
- Correctness, regressions, failure behavior, and relevant security/data risks.
- For retries of external side effects, whether an uncertain operation may already have taken effect; require evidence of safe repeatability or reconciliation before accepting replay.
- Test adequacy and whether evidence covers the claimed behavior.
- Maintainability and project conventions, distinguishing preferences from defects.

For each actionable finding, provide location, trigger, consequence, supporting evidence, and severity. State confidence or missing evidence when material. Do not invent findings to satisfy a quota or demand abstractions merely because a pattern has a name. Rank actual impact first; optional improvements must not block unrelated delivery.

## Resolve and close

The implementing agent independently checks each finding. Mark it accepted, rejected with counterevidence, or unresolved with the specific missing fact/decision. User insistence and reviewer confidence are not technical evidence; explicit scope changes remain valid user decisions.

Fix accepted findings within authorization, run affected checks, and retain the disposition in the existing review/task record. Re-review material fixes and newly affected behavior against the resulting candidate. Preserve still-valid evidence for unchanged areas. If files changed during review, reconcile the changes before applying its verdict to the new candidate.

Stop when substantive findings are resolved or clearly reported as remaining, and the requested review scope is covered. Do not spin until reviewers agree or declare acceptance merely because no findings were produced. Report the candidate, coverage, unresolved risks, and whether the review was independent. Human approval and release status are separate claims.
