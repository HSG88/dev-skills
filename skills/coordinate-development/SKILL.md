---
name: coordinate-development
description: Coordinate substantial multi-part development with task dependencies, bounded subagents, isolated edits, integration, and recovery. Use when useful parallel work or multiple dependent implementation steps justify coordination; skip routine single-step changes.
---

# Coordinate development

Own the integrated outcome, not just worker dispatch. Use the existing task record and native agent/Git tools; do not build an orchestration framework for an ordinary feature.

## Choose the work shape

Read the accepted requirements, relevant project instructions, current checkout, and existing changes. Use acceptance-spec for the contract when useful. Identify tasks, prerequisites, shared interfaces, and the checks that establish completion. A short table of task, dependencies, owner, candidate, status, and evidence is sufficient; do not duplicate the spec.

Resolve shared contracts before concurrent consumers implement against them. Mark work ready only when its necessary decisions and dependencies are available. Split by independently testable behavior rather than arbitrary file counts. If the change is tightly coupled or delegation costs more than it saves, execute sequentially.

## Assign bounded work

When this skill applies, use native subagents for bounded assignments that benefit from delegation, within available capacity and applicable permissions. Start small: one coordinator and one worker is sufficient for many tasks. Do not queue work while waiting for a slot that only the waiting agent can release. If capacity or delegation is unavailable, work sequentially or report the specific unavailable independent check.

Give each worker: objective; accepted requirements and shared interfaces; minimal relevant source/instruction pointers; exact write ownership; baseline/candidate; checks; output expectations; and a finite stopping condition. Do not send an intended review verdict or require inheriting the coordinator's whole history. Workers may request a contract change but must not silently change shared assumptions. No recursive delegation by default.

## Isolate edits and resources

For concurrent writers, use separate worktrees when supported and appropriate. Reuse suitable host-provided isolation. Identify the repository and baseline before creation; include existing uncommitted input deliberately or keep it separate, never assume a new worktree contains it. Honor requests not to commit. A reviewed patch is an alternative to a worker commit.

Assign one owner per writable file or shared interface during a work period. Disjoint files can still share a runtime resource: allocate separate test databases, ports, temporary paths, and sessions, or serialize access. A worktree is not a security boundary and does not isolate an external account. Never fall back to the user's primary checkout if required isolation fails.

## Run a bounded feedback loop

Use behavior-tests and simple-design where relevant. Continue implement/check/fix cycles while evidence changes and progress is being made. A repeated failure with no new information calls for investigation or replanning, not another identical retry. Keep acceptance criteria fixed unless the user changes them. Reaching a time or resource bound means preserve progress and report remaining work, not declare completion.

While workers run, do useful independent work. Handle material questions promptly. Before reassigning ownership, stop or confirm completion of the previous writer so a late result cannot overwrite newer work. Do not repeat external side effects after ambiguous outcomes without safe-repeatability evidence.

## Integrate and review

Inspect actual worker changes and test evidence before integrating. Verify the returned candidate is based on the expected baseline and matches the reviewed files; detect changes made after review. Treat reports as claims, not proof.

Integrate accepted changes in dependency order. Resolve conflicts by the accepted behavior, not by choosing one side wholesale. Check the combined result, including interactions that isolated worker tests cannot establish. Use review-and-resolve for consequential changes and focused re-review after material fixes. A worker reviewing its own result is not independent review.

## Finish or resume safely

Record the integrated candidate, requirement status, evidence, unresolved findings, and next action. After interruption, inspect actual files, Git state, and worker status before trusting the record. Resume from established state; do not replay completed mutations blindly.

Remove temporary worktrees only after proving they were created for this work, are inactive and clean, and their work is integrated or deliberately preserved. Directory names alone do not establish ownership. Keep dirty, uncertain, active, or recovery-relevant worktrees. Publishing and deployment remain governed by the user's authorization; completing a task graph grants no new authority.
