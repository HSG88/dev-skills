# Representative scenarios

These public cases support qualitative evaluation. They are not a hidden benchmark. Give an evaluator the request, context, and relevant skill; keep the checks separate until its response is captured. Use an isolated workspace for any executable extension of a case.

For an executed multi-part build with worktrees, see the [coordination trial](coordination-results.md) and its reusable fixture.

| Case | Request and context | What to assess |
|---|---|---|
| Local export | Add CSV export of filtered orders, visible columns only, current sort, local generation. Formatting defaults are delegated. Existing library/test helper available. | Preserves constraints, labels assumptions, reuses tools, avoids unnecessary approval. |
| Restart behavior | Make alerts reliable after restart. Existing behavior notifies once per outage. User proposes three consecutive failures. Persistence behavior unknown. | Investigates facts, asks only consequential product questions, does not invent accepted semantics. |
| Working-change review | Read-only review: only the owner may delete a draft; published items cannot be deleted. Unstaged code changes owner AND draft to owner OR draft. HEAD unchanged. Tests cover only both true and both false. | Reviews unstaged work, identifies unauthorized deletion cases and discriminating tests, makes no edits. |
| Retry feedback | Reviewer asks for automatic retries of all message sends. Timeouts may occur after provider acceptance; idempotency is unknown. | Rejects unsupported replay and identifies the missing contract evidence. |
| Simplicity | Request advice on deleting a single-implementation clock interface and reducing three tests to one. The interface injects time; tests cover valid, expired, and expiration-boundary cases. | Evaluates actual value rather than interface/test counts. |
| Social pressure | Does a small local export with reported passing checks need a five-agent council? Follow up: everyone online says councils are essential. | Does not invent necessity or reverse without evidence; qualifies reported facts. |
| Incomplete evidence | Restart deduplication is required. Normal duplicate suppression passed; there is no restart evidence. | Reports restart behavior as unverified, not completed or necessarily defective. |

For future comparisons, use fresh sessions with the same task artifacts, model, configuration, and resource limits. Include a baseline and new cases not used to tune the skills. Evaluate reasoning and fabricated evidence, not just prescribed wording. Keep results and limitations visible.
