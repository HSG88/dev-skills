---
name: simple-design
description: Choose the least complex complete implementation and remove unnecessary complexity during coding or design. Use when selecting an approach, abstraction, dependency, or scoped refactor; preserve agreed behavior and project constraints.
---

# Simple design

Optimize for the total cost of understanding, changing, operating, and validating the solution—not its line count.

Before editing, understand the relevant behavior, constraints, and existing implementation. Follow project retrieval rules; inspect affected callers and boundaries sufficiently to understand impact. Expand investigation when uncertainty warrants it, without reading the entire repository by default.

Prefer reuse of a suitable existing pattern, native facility, standard library, or installed dependency. Suitability includes semantics, compatibility, failure handling, maintenance, and operating constraints. Do not build custom logic merely to avoid a dependency already used appropriately. Add a new dependency only for a concrete benefit that justifies its cost.

Implement the agreed outcome completely. Omit speculative extensions, redundant wrappers, premature generalization, and unused configuration. Propose a scope reduction explicitly when it would help; do not ship it as a substitute for the requested product. A requested capability is not speculative merely because its implementation is complex.

Use an abstraction when it protects a real boundary, clarifies a domain concept, isolates an external dependency, or removes consequential duplication. A single implementation can justify an interface. Configuration is justified when actual deployments, users, or hardware need variation. Avoid neither abstraction nor duplication dogmatically; choose the simpler maintained result.

Prefer readable code and cohesive modules over compressed expressions or the fewest files. Fix defects at the responsible boundary after checking shared callers; do not move a guard to a shared function if that changes valid behavior for other consumers. Keep unrelated cleanup out of the change.

Preserve required validation, security, accessibility, failure handling, durability, and compatibility. Test effort follows behavior and risk using existing project tools; there is no one-test limit. A one-line change can be high risk.

If a deliberate limitation matters, document its concrete ceiling and what observation would justify revisiting it, near the relevant code or in existing decision notes. Do not add ritual debt comments to ordinary simple code. Do not choose a known inadequate shortcut for an accepted requirement.

Scale process to the change. This skill governs engineering choices, not response length, persona, permission policy, or persistent session modes. Explain meaningful tradeoffs and evidence at the depth the task needs.
