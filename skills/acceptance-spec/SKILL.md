---
name: acceptance-spec
description: Capture and maintain agreed software requirements as observable acceptance criteria, and reconcile delivery against them. Use for substantial features, changes with several constraints, or an explicit specification request; reuse existing specs.
---

# Acceptance specification

Preserve intended outcomes through implementation and review. Maintain one authoritative requirement record using the project's existing format; a small change may need only a short checklist in the task. Requirements, decisions, review dispositions, and delivery status can share that record; do not create separate documents just because several skills are used.

## Establish the contract

Use the original request, explicit subsequent decisions, and relevant project constraints. Identify their source. Label agent proposals and unresolved assumptions; do not imply they were accepted. Surface conflicts with earlier requirements rather than silently choosing the convenient version. Explicit user changes supersede old requirements; record the material change so reviewers use the right version.

Capture only applicable items:
- Outcome and intended user workflow.
- Required observable behavior, including material failure behavior.
- Data, permission, compatibility, accessibility, performance, and operational constraints that matter to this change. Use measurable thresholds only when provided or agreed; never invent precision.
- Explicit exclusions, dependencies, and unresolved decisions.
- Concrete examples and the evidence needed to establish acceptance.

For multiple requirements, give stable short IDs and use a compact table: requirement; source/status; acceptance example; evidence/status. For example, restart-safe notification deduplication needs a restart scenario, not just repeated checks in one process. This is an illustrative requirement, not a default for all applications.

Separate what must be true from a proposed implementation. Let implementation choices evolve when they preserve the contract. Do not shrink a requirement because it is difficult, redefine success around existing tests, or silently replace a requested feature with a prototype.

## Use during delivery

For work that benefits from sequencing, identify usable end-to-end slices with dependencies and acceptance checks. Skip separate slice planning for a single-step change. Address a costly uncertainty early. A plan sequences work; it must reference rather than duplicate the requirement record.

Reuse project status records for multi-session work. Record the current candidate/location, spec version, decisions, completed evidence, remaining work, and next action. On resumption, verify current files/state before trusting the handoff. Keep durable status concise and exclude credentials or sensitive runtime data.

At delivery, reconcile every in-scope requirement: met with appropriate evidence; not met/partial; or unverified with a concrete limitation. Include where and on what candidate checks ran. Passing narrow tests cannot establish broader integration, visual approval, production behavior, or human acceptance.

When release is in scope, include applicable configuration, migration/recovery, operator documentation, and post-release checks in the original contract. Keep implemented, reviewed, tested, deployed, and user-accepted states distinct. Release authorization is governed by the user's request and project rules, not by a completed checklist.

Do not mandate publishing issues, opening PRs, committing, or deploying. Record gaps honestly and continue authorized work that can resolve them.
