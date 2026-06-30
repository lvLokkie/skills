# Ivan's Universal Skills Marketplace

A personal, vendor-neutral marketplace for shipping Ivan's agent skills across Claude Code, Hermes, Codex, and future agents.

The repo is intentionally small: **skills are the product**, per-agent manifests are thin packaging, and third-party skill repos are treated as dependencies or reference material rather than copied wholesale.

## Install

Claude Code marketplace install:

```text
/plugin marketplace add lvLokkie/skills
/plugin install personal-skills@personal-skills-marketplace
```

Run the promoted skill:

```text
/personal-skills:created-skill-audit
```

For private clones, installation needs a git credential helper or `GITHUB_TOKEN` available to the installing machine.

## Principles adopted from `mattpocock/skills`

- **Small, composable skills.** Prefer one sharp workflow over a giant process framework.
- **User-invoked vs model-invoked.** User-invoked skills orchestrate by explicit command; model-invoked skills carry reusable behavior and trigger phrasing.
- **Progressive disclosure.** Put the main execution path in `SKILL.md`; move bulky reference into sibling files.
- **Context-load budget.** Every model-invoked description costs tokens. Promote only skills that need autonomous reach.
- **No-op pruning.** Keep only text that changes observable behavior.
- **Dependency over copying.** Use external skill repos as dependencies or reference; local skills should be thin adapters for routing, config, and deltas — not rewritten forks of upstream procedures.

See [docs/invocation.md](./docs/invocation.md), [docs/dependencies.md](./docs/dependencies.md), and [docs/mattpocock-dependency-candidates.md](./docs/mattpocock-dependency-candidates.md).

## Promoted skills

### Model-invoked

| Skill | Purpose |
|---|---|
| [created-skill-audit](./plugins/personal-skills/skills/created-skill-audit/SKILL.md) | Audit agent-authored or revised skills for behavioral effect, context load, no-op prose, duplicated meaning, stale sediment, and publish readiness. |

### User-invoked

None yet. Add user-invoked skills only when the human should intentionally start the flow and the skill should not spend model context by default.

## Repository layout

| Path | Role |
|---|---|
| `.claude-plugin/marketplace.json` | Claude marketplace entry pointing at the plugin package. |
| `plugins/personal-skills/.claude-plugin/plugin.json` | Thin plugin manifest; must list promoted skill folders. |
| `plugins/personal-skills/skills/<name>/SKILL.md` | Source of truth for shipped Claude skills. |
| `plugins/personal-skills/skills/README.md` | Bucket catalog grouped by invocation class. |
| `docs/invocation.md` | Invocation taxonomy and dependency style. |
| `docs/dependencies.md` | General dependency policy: hard/soft/reference/tool/plugin deps, fallbacks, and no-vendoring rules. |
| `docs/mattpocock-dependency-candidates.md` | Reference analysis and shortlist of upstream skills to depend on or adapt. |
| `AGENTS.md` | Working rules for agents editing this repo. |

## Add or revise a skill

1. Create or edit `plugins/personal-skills/skills/<name>/SKILL.md`.
2. Decide invocation class:
   - model-invoked: rich trigger phrasing in `description`;
   - user-invoked: add `disable-model-invocation: true` and use a human-facing one-line description.
3. Add heavy references as sibling `.md` files, not into the top of `SKILL.md`.
4. Update:
   - `plugins/personal-skills/skills/README.md`
   - `plugins/personal-skills/.claude-plugin/plugin.json`
   - this README's promoted-skill table
5. Run validation:

```bash
python scripts/validate.py
```

6. Bump `plugins/personal-skills/.claude-plugin/plugin.json` version on behavior changes.

## Dependency policy

- Do not vendor third-party skill repos by default.
- Classify dependencies as hard, soft, reference, tool, or plugin dependencies in [docs/dependencies.md](./docs/dependencies.md).
- For overlaps, prefer upstream dependency/reference plus a thin local adapter; do not restate the full upstream skill locally.
- If the target agent cannot consume the upstream skill directly, document the compatibility gap and maintenance owner before forking/adapting text.
- Do not ship personal, in-progress, or deprecated upstream skills unless there is a fresh local audit.
