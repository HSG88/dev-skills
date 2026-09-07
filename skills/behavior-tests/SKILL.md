---
name: behavior-tests
description: Design and run meaningful tests for changed software behavior, using a test-first loop where practical. Use for feature logic, bug regressions, and risk-sensitive changes; follow the project's existing test tools.
---

# Behavior tests

Choose tests from the requirements and the consequences of failure, not the number of lines changed.

Inspect the existing test setup and affected flow. Reuse its runner, fixtures, and conventions. Select public boundaries that expose the required behavior; use focused unit tests for algorithms or invariants when these provide clearer, faster evidence than a large end-to-end setup. Do not ask the user to approve routine test boundaries already supported by the task.

For new logic, write a meaningful failing test, implement the smallest complete slice that passes, and refactor locally if it improves clarity while tests remain green. For a bug, establish the original symptom and a failing regression before the fix when feasible. A failed import, missing credential, or broken harness does not establish the intended red state.

If a test cannot reproduce an intermittent or environment-specific failure, gather evidence and explain the limitation. Do not manufacture a passing proxy or claim the bug is proven fixed. For an exploratory spike or a change with no sensible automated assertion, use an appropriate bounded check and state exactly what it establishes.

Expected results must come from a requirement, independently worked example, trusted reference, or invariant. Do not derive the expected answer using the same algorithm under test. Check meaningful negative cases: invalid input, denied operations, failure handling, boundaries, state transitions, or concurrency when relevant. No arbitrary one-test ceiling or mandatory exhaustive matrix.

Control time, randomness, and external dependencies at suitable boundaries. Use realistic fakes or test services when useful. Call counts and persistent-state inspection are valid when they directly establish requirements such as no duplicate side effects or durability. Do not call every internal observation a bad test; explain why it is needed. A mock passing does not establish compatibility with the real provider.

Run checks that cover changed behavior plus applicable project-required checks. Distinguish newly introduced failures from a verified baseline failure; neither is a pass. Reuse a result only when the relevant candidate, inputs, configuration, and dependencies remain unchanged. After a fix, rerun affected checks and broaden only as impact or project requirements warrant.

Keep tests in the project's normal suite so regressions stay detectable. Do not weaken assertions, delete meaningful checks, or change requirements just to obtain green results. Report check results and material coverage limits; do not claim the entire feature is accepted from the test suite alone.
