# Optional tooling

No tool on this page is a dependency of these skills. Choose a tool for the question and verify the source behind its answer.

| Need | Starting point | Optional addition |
|---|---|---|
| Exact text, identifiers, paths | ripgrep and direct file reads | tgrep if repeated search latency warrants indexing |
| Definitions and references | Language-server navigation when available | CodeGraph for indexed cross-file relationships |
| Unknown wording or location | Focused discovery and project documentation | zvec-grep for lexical/semantic retrieval |
| Syntax-aware patterns | Language tooling | ast-grep |
| Noisy command output | Tool-native concise output | RTK compression, with raw output when needed |

## Boundaries

- [RTK](https://github.com/rtk-ai/rtk) compresses shell output. Use unfiltered output for exact source, diffs, diagnostics, or evidence that compression omits. Its output-reduction figures do not establish total task cost savings.
- [CodeGraph](https://github.com/colbymchenry/codegraph) indexes symbols and relationships. Confirm the index belongs to the correct repository/worktree and is sufficiently current before relying on it. A graph is not proof of runtime behavior or complete dynamic-dispatch coverage.
- [zvec-grep](https://github.com/zvec-ai/zvec-grep) combines exact, lexical, and semantic retrieval across workspace content. Use it when discovery by meaning adds value. Respect index freshness and check cited source when needed; do not treat a retrieval miss as proof of absence. Inspect embedding configuration before sending private material to a remote provider.
- [ripgrep](https://github.com/BurntSushi/ripgrep) is a simple baseline for current on-disk text. [ast-grep](https://ast-grep.github.io/) is useful for structural patterns; neither is semantic document retrieval.
- [tgrep](https://github.com/microsoft/tgrep) targets indexed regex search. Its [large-repository benchmarks](https://github.com/microsoft/tgrep/blob/main/BENCHMARKS.md) exclude index construction from timed search results. Measure end-to-end benefit before adding a server and index to your workflow.

Do not create or rebuild persistent indexes without appropriate authorization. Existing project retrieval rules still apply. These are selection guidelines, not instructions to uninstall tools or rewrite host configuration.

For adoption, compare representative tasks using useful evidence retrieved, missed relationships, stale results, tool calls, elapsed time, and maintenance effort. Search speed alone does not establish a more robust development cycle.
