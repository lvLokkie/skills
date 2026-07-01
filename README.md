# Ivan's Universal Skills Marketplace

A personal, vendor-neutral marketplace for shipping Ivan's agent skills across Claude Code, Hermes, Codex, and future agents.

The repo is intentionally small: **skills are the product**, per-agent manifests are thin packaging, and third-party skill repos are treated as dependencies or reference material rather than copied wholesale.

## Install

Claude Code marketplace install:

```text
/plugin marketplace add lvLokkie/skills
/plugin install general@ivan-skills-marketplace
/plugin install marketing@ivan-skills-marketplace
```

Run promoted skills:

```text
/general:skill-audit
/general:report-writing
/marketing:lidfly-mcp
/marketing:ad-campaign-operations
/marketing:avito-ads-feed
/marketing:lead-routing-tracking
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

## Promoted categories and skills

### `general`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [skill-audit](./plugins/general/skills/skill-audit/SKILL.md) | Audit local skill/package changes and external skill candidates against `writing-great-skills`, Ivan packaging gates, and industrial security checks before publishing or importing. |
| [report-writing](./plugins/general/skills/report-writing/SKILL.md) | Write evidence-backed reports, briefs, and decision memos with sources, confidence labels, conclusions, and next actions. |

### `marketing`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [lidfly-mcp](./plugins/marketing/skills/lidfly-mcp/SKILL.md) | Use LidFly MCP safely for advertising-platform access, setup checks, tool-scope selection, and read/write guardrails. |
| [ad-campaign-operations](./plugins/marketing/skills/ad-campaign-operations/SKILL.md) | Operate and optimize advertising campaigns using source docs, campaign structure, metrics, experiments, and weekly action reports. |
| [avito-ads-feed](./plugins/marketing/skills/avito-ads-feed/SKILL.md) | Generate, audit, and smoke-test Avito service ad feeds, branded cards, listing copy, category mappings, and feed coverage. |
| [lead-routing-tracking](./plugins/marketing/skills/lead-routing-tracking/SKILL.md) | Audit and smoke-test lead forms, UTM/referrer attribution, n8n routing, Telegram/MAX delivery, and analytics goals. |

### User-invoked

None yet. Prefer direct upstream dependencies for generic command skills like `handoff` unless this marketplace needs a local platform adapter.

## Repository layout

| Path | Role |
|---|---|
| `.claude-plugin/marketplace.json` | Claude marketplace entry pointing at category plugin packages. |
| `plugins/<category>/.claude-plugin/plugin.json` | Thin category plugin manifest; must list promoted skill folders. |
| `plugins/<category>/skills/<name>/SKILL.md` | Source of truth for shipped Claude skills. |
| `plugins/<category>/skills/README.md` | Category catalog grouped by invocation class. |
| `docs/invocation.md` | Invocation taxonomy and dependency style. |
| `docs/dependencies.md` | General dependency policy: hard/soft/reference/tool/MCP/plugin deps, fallbacks, and no-vendoring rules. |
| `docs/mattpocock-dependency-candidates.md` | Reference analysis and shortlist of upstream skills to depend on or adapt. |
| `AGENTS.md` | Working rules for agents editing this repo. |

## Add or revise a skill

1. Create or edit `plugins/<category>/skills/<name>/SKILL.md`.
2. Decide invocation class:
   - model-invoked: rich trigger phrasing in `description`;
   - user-invoked: add `disable-model-invocation: true` and use a human-facing one-line description.
3. Add heavy references as sibling `.md` files, not into the top of `SKILL.md`.
4. Update:
   - `plugins/<category>/skills/README.md`
   - `plugins/<category>/.claude-plugin/plugin.json`
   - `.claude-plugin/marketplace.json` when adding/removing a category
   - this README's promoted-skill table
5. Run validation:

```bash
python scripts/validate.py
```

6. Bump the owning `plugins/<category>/.claude-plugin/plugin.json` version on behavior changes.

## Add or revise a skill category

A category is a marketplace plugin under `plugins/<category>/`. Use categories for durable domains, not one-off projects.

1. Create or edit:
   - `plugins/<category>/.claude-plugin/plugin.json`
   - `plugins/<category>/skills/README.md`
   - one or more real `plugins/<category>/skills/<name>/SKILL.md` files
2. Register or update the category in `.claude-plugin/marketplace.json`.
3. Update this README with install/run examples and promoted skills.
4. Run `skill-audit` category CRUD gates: create/read/update/delete/move, packaging, dependency policy, and security scan.
5. Run `python scripts/validate.py`, `git diff --check`, JSON parse, and plugin validation when available.

## Dependency policy

- Do not vendor third-party skill repos by default.
- Classify dependencies as hard, soft, reference, tool, or plugin dependencies in [docs/dependencies.md](./docs/dependencies.md).
- For overlaps, prefer upstream dependency/reference plus a thin local adapter; do not restate the full upstream skill locally.
- If the target agent cannot consume the upstream skill directly, document the compatibility gap and maintenance owner before forking/adapting text.
- Do not ship personal, in-progress, or deprecated upstream skills unless there is a fresh local audit.
