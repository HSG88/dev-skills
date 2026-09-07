# Executed coordination trial

Date: 2026-09-07. This was a bounded synthetic software build, not a production feature or a controlled effectiveness benchmark.

## Setup and division

The [task contract](coordination-fixture/TASK.md) specified a local CSV renderer and CLI. The [seed files](coordination-fixture/exporter.py) intentionally lacked implementations. The coordinator established the shared function signature before creating two worktrees from the same baseline: one for a delegated renderer worker and one for the coordinator's CLI implementation. The worker owned exporter.py and its focused tests; the coordinator owned cli.py. An unrelated untracked note in the integration checkout was reserved for preservation.

The host refused another new agent thread, so an existing idle worker was reused with a new bounded assignment. Work did not wait indefinitely for an unavailable slot or start recursive delegation. The worker was not used as its own independent reviewer. Exact model/version and generation settings were not independently captured; this is not a model comparison.

## Observed evidence

- Acceptance checks failed on the seed because the required export behavior was unimplemented.
- The worker delivered a commit limited to its two owned files and four passing standard-library tests. The CLI change was committed separately in its own worktree against the same shared contract.
- The coordinator inspected the actual worker diff, integrated both commits, independently reran the worker's four tests, and ran [combined acceptance checks](check_coordination.py).
- The integrated checks passed filtering, numeric sorting, column selection/order, CSV escaping, LF termination, null/missing fields, empty results, unchanged input records, and CLI output/input-file preservation.
- The CLI exercised the actual renderer; two isolated success reports were not treated as proof of integration.
- Both worker worktrees were confirmed inactive and clean, their owned files matched the integrated result, and they were removed without force. Their branches and the integrated fixture remain preserved; the unrelated untracked note was unchanged.

The [retained result](coordination-result/exporter.py), CLI, and focused tests allow replay of the software checks in CI. They do not replay the agent interaction or establish that future agents will coordinate correctly. The check does not instrument network calls; absence of networking was assessed from the small implementation's source and dependencies.

## Additional improvement

A separate validator probe demonstrated that malformed YAML metadata was accepted. A regression test failed before the repair and passed after replacing the hand-written metadata parser with PyYAML. Invalid value types and duplicate keys are also rejected. PyYAML is a validation-only dependency, not a skill runtime requirement.

## Limits

An independent reviewer examined the skill, rule/documentation changes, validator repair, fixture contract, and retained implementation. It reported no actionable findings and independently passed metadata validation, validator regression checks, four renderer tests, and combined CLI acceptance checks. It did not independently observe the historical dispatch, worktree creation, initial failures, or cleanup; those are coordinator-recorded observations.

One coordinator and one delegated worker participated. The trial does not establish speedup, lower cost, multi-machine orchestration, conflict recovery under concurrent edits, external-service isolation, or automatic crash recovery. Those instructions remain design guidance and require targeted validation when those workflows are used. More agents were neither required nor tested.
