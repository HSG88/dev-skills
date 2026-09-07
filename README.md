# dev-skills

Six focused skills for coding agents: clear requirements, meaningful tests, independent review, simple design, and evidence-based judgment.

Use the skills that fit the task. A small fix does not need a full development ceremony. These instructions do not guarantee correctness, replace executable checks, or override your agent's permissions and instruction hierarchy.

## Skills

| Skill | Use it for |
|---|---|
| [clarify-intent](skills/clarify-intent/SKILL.md) | Resolve consequential ambiguity without an endless interview. |
| [acceptance-spec](skills/acceptance-spec/SKILL.md) | Preserve agreed requirements and reconcile delivery against evidence. |
| [behavior-tests](skills/behavior-tests/SKILL.md) | Test observable behavior with independent expected results and appropriate coverage. |
| [review-and-resolve](skills/review-and-resolve/SKILL.md) | Review the actual candidate, evaluate findings, and resolve supported defects. |
| [simple-design](skills/simple-design/SKILL.md) | Choose the least complex complete implementation, without reducing agreed scope. |
| [critical-thinking-peer](skills/critical-thinking-peer/SKILL.md) | Challenge unsupported claims, consider counterevidence, and agree when justified. |

The usual flow is clarify → define acceptance → implement and test → review and resolve → reconcile delivery. Skip stages that do not add value to the task. Keep project-specific commands and constraints in the project's existing instructions.

## Install

Clone this repository and inspect the skills before installing:

```sh
git clone https://github.com/HSG88/dev-skills.git
cd dev-skills
python3 scripts/validate.py
```

For Codex, copy each selected skill directory into your user skill directory. Current official documentation uses `~/.agents/skills`; some installations also discover `~/.codex/skills`. Use one supported location, not both. For a repository-scoped installation, use `.agents/skills` in that repository. Check the [official discovery documentation](https://learn.chatgpt.com/docs/build-skills) for your client.

For example, to install one skill without overwriting an existing one:

```sh
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/critical-thinking-peer && \
  cp -R skills/critical-thinking-peer ~/.agents/skills/
```

Invoke it in Codex with `$critical-thinking-peer`, or let the agent select it when relevant. Other hosts that support `SKILL.md` may use different installation locations, invocation syntax, or delegation tools; compatibility has not been tested across hosts.

The optional [global defaults](rules/global-defaults.md) are an editable instruction fragment. Merge the parts you want into your existing global agent instructions; do not replace the whole file. Avoid overlapping methodology packages that impose contradictory approval, testing, or scope rules. Preserve specialist skills.

The optional [CodeGraph bootstrap profile](rules/codegraph-bootstrap.md) adds automatic initial indexing for new code projects and CodeGraph-first code exploration when the tool is installed.

Copies do not update automatically. Review repository changes before copying an updated skill. Restart your client if changes are not discovered; use a fresh task when old instructions were already loaded.

## Validation and evidence

```sh
python3 scripts/validate.py
python3 scripts/test_validate.py
```

CI checks the repository's deliberately simple metadata format and local Markdown file links. It does not evaluate model behavior. See the [scenarios](evaluations/scenarios.md) and [evaluation record](evaluations/results.md) for the initial qualitative assessment and its limitations.

No API key, daemon, embedding model, or third-party search tool is required. [Tooling guidance](docs/tooling.md) describes optional additions.

## Contributing

Describe the concrete failure a change addresses. Keep triggers narrow, preserve user intent and authorization, and add a representative evaluation case when instructions materially change. Run both validation commands. Prefer removing contradictory or redundant rules over accumulating universal rules from isolated examples.

## Acknowledgments and license

The instructions were developed with AI assistance and informed by [Matt Pocock's skills](https://github.com/mattpocock/skills), [Superpowers](https://github.com/obra/superpowers), [Ground Truth](https://github.com/glichtenthal/ground-truth), and [Ponytail](https://github.com/DietrichGebert/ponytail). This repository provides newly written, selective workflow instructions, not those upstream plugins or their scripts. It is not affiliated with those projects.

[MIT license](LICENSE).
