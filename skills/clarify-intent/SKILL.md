---
name: clarify-intent
description: Resolve consequential ambiguity in a proposed feature, product, or design before committing to its behavior. Use when intent, constraints, or user experience remain unclear; skip routine changes with sufficient requirements.
---

# Clarify intent

Produce shared understanding sufficient for the next useful implementation slice, not an exhaustive interview.

Read the user's request and relevant existing decisions first. Follow the project's retrieval instructions to inspect facts that can be established locally. Distinguish current behavior from desired behavior: existing code is evidence of what happens, not authority over what the user wants.

Identify the intended user, outcome, concrete workflow, constraints, exclusions, and material unknowns. Ask only questions that change observable behavior, an expensive design commitment, or acceptance. Prioritize dependencies; keep each round small enough to answer. Include a recommendation with the reason when it helps. Do not delegate merely to locate facts.

An explicit requirement is already a decision. Do not repeatedly ask the user to approve settled requirements or routine implementation choices. An unresolved product decision cannot be answered by elapsed time or the agent's preferred design. Continue independent work while it is pending. For reversible implementation details, state a reasonable assumption and proceed within existing authorization.

For a consequential architectural choice, compare the viable alternatives against actual constraints and the cost of reversal. Run a bounded disposable experiment when uncertainty is empirical. A prototype answers its stated question; it is not production acceptance evidence.

For user interfaces, use a concrete interaction example or small prototype when prose leaves important ambiguity. Distinguish functional criteria from user preferences about appearance. Let the user judge subjective fit; do not substitute the agent's aesthetic preference.

Record resolved terminology and decisions in existing project documents. Avoid creating a second glossary or forcing an ADR for routine choices. Record a durable rationale when a decision is costly to reverse or otherwise likely to be misunderstood.

Finish when the next slice has a clear outcome and acceptance examples, and its remaining unknowns are either non-blocking implementation choices or explicitly pending decisions. Summarize only decisions, consequential assumptions, and unresolved questions. Preserve the user's authority over priorities and scope without making them choose every technical detail.
