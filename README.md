# Ivan's Universal Skills Marketplace

A personal, vendor-neutral marketplace for shipping Ivan's agent skills across Codex, Claude Code, Hermes, and future agents.

The repo is intentionally small: **skills are the product**, per-agent manifests are thin packaging, and third-party skill repos are treated as dependencies or reference material rather than copied wholesale.

## Install & Activate

Skill bodies are vendor-neutral (see [docs/invocation.md](./docs/invocation.md) and [docs/dependencies.md](./docs/dependencies.md)); packaging is per-agent. Codex and Claude Code are packaged targets; Hermes and other agents consume the same source skills or thin target adapters.

### Codex

This follows the [official Codex plugin flow](https://developers.openai.com/codex/plugins): register a marketplace, then install plugin entries from the Plugin Directory (`/plugins` in Codex CLI).

**Add the marketplace from a local checkout.** Codex reads this repo through `.agents/plugins/marketplace.json`.

```bash
codex plugin marketplace add <path-to-checkout>
```

**Add the marketplace from GitHub.** Prerequisite: this is a private GitHub project, so the installing machine needs working git auth — a git credential helper, `gh auth login`, or `GITHUB_TOKEN`. Use the `.git` URL so Codex clones with local git credentials.

```bash
codex plugin marketplace add --sparse .agents/plugins --sparse plugins https://github.com/lvLokkie/skills.git
```

**Install plugins.** The current Codex CLI exposes marketplace plugin installation through the plugin browser, not through a separate `codex plugin install` command:

```text
codex
/plugins
```

In the plugin browser, switch to `lvlokkie-skills-marketplace`, then install `general`, `skill-management`, `marketing`, and `business-docs`; optionally install `in-progress` for manual-only draft skills.

**Activate.** Start a new Codex session after installing or upgrading the plugins. The available skill names are:

```text
general:report-writing
general:make-me-rich
business-docs:business-doc-suite
business-docs:core-business-brief
business-docs:business-plan-writing
business-docs:financial-model-spec
skill-management:skill-audit
skill-management:skill-authoring
skill-management:skill-category-management
marketing:lidfly-mcp
marketing:campaign-tooling-readiness
marketing:ad-campaign-operations
marketing:yandex-wordstat-research
marketing:avito-market-intelligence
marketing:avito-ads-feed
marketing:lead-routing-tracking
# Optional manual-only draft skill:
in-progress:wizard
```

Manual update for a Git-backed marketplace:

```bash
codex plugin marketplace upgrade lvlokkie-skills-marketplace
```

For a local checkout marketplace, update the checkout and start a new Codex session.

### Claude Code

**Install from a terminal.** Prerequisite: this is a private GitHub project, so the installing machine needs working git auth — a git credential helper, `gh auth login`, or `GITHUB_TOKEN`. Use the `.git` URL so the marketplace is cloned with git credentials.

```bash
claude plugin marketplace add https://github.com/lvLokkie/skills.git
claude plugin install general@lvlokkie-skills-marketplace
claude plugin install skill-management@lvlokkie-skills-marketplace
claude plugin install marketing@lvlokkie-skills-marketplace
claude plugin install business-docs@lvlokkie-skills-marketplace
# Optional manual-only draft skills:
claude plugin install in-progress@lvlokkie-skills-marketplace
```

Equivalent commands inside Claude Code:

```text
/plugin marketplace add https://github.com/lvLokkie/skills.git
/plugin install general@lvlokkie-skills-marketplace
/plugin install skill-management@lvlokkie-skills-marketplace
/plugin install marketing@lvlokkie-skills-marketplace
/plugin install business-docs@lvlokkie-skills-marketplace
# Optional manual-only draft skills:
/plugin install in-progress@lvlokkie-skills-marketplace
```

**Activate.** Installed plugins load on the next session. Restart Claude Code, or run `/reload-plugins` to apply without restarting. Confirm with `/plugin` (Installed tab) or `claude plugin list`.

Run promoted skills:

```text
/general:report-writing
/general:make-me-rich
/skill-management:skill-audit
/skill-management:skill-authoring
/skill-management:skill-category-management
/marketing:lidfly-mcp
/marketing:campaign-tooling-readiness
/marketing:ad-campaign-operations
/marketing:yandex-wordstat-research
/marketing:avito-market-intelligence
/marketing:avito-ads-feed
/marketing:lead-routing-tracking
/business-docs:business-doc-suite
/business-docs:core-business-brief
/business-docs:business-plan-writing
/business-docs:financial-model-spec
# Optional manual-only draft skill:
/in-progress:wizard
```

**Keep it updated.** Refresh the marketplace and installed plugins explicitly:

```text
claude plugin marketplace update lvlokkie-skills-marketplace
claude plugin update general@lvlokkie-skills-marketplace
claude plugin update skill-management@lvlokkie-skills-marketplace
claude plugin update marketing@lvlokkie-skills-marketplace
claude plugin update business-docs@lvlokkie-skills-marketplace
```

Updates rely on valid GitHub credentials; if they expire, re-authenticate.

### Other agents

Skill sources under `plugins/<category>/skills/<name>/SKILL.md` are kept portable, so a target agent can consume them directly or through a thin per-agent manifest; add new packaging alongside the Codex and Claude Code entries rather than forking the skill bodies.

## Principles adopted from `mattpocock/skills`

- **Small, composable skills.** Prefer one sharp workflow over a giant process framework.
- **User-invoked vs model-invoked.** User-invoked skills orchestrate by explicit command; model-invoked skills carry reusable behavior and trigger phrasing.
- **Progressive disclosure.** Put the main execution path in `SKILL.md`; move bulky reference into sibling files.
- **Context-load budget.** Every model-invoked description costs tokens. Promote only skills that need autonomous reach.
- **No-op pruning.** Keep only text that changes observable behavior.
- **Dependency over copying.** Use external skill repos as dependencies or reference; local skills should be thin adapters for routing, config, and deltas — not rewritten forks of upstream procedures.

See [docs/invocation.md](./docs/invocation.md), [docs/dependencies.md](./docs/dependencies.md), and [docs/mattpocock-dependency-candidates.md](./docs/mattpocock-dependency-candidates.md).

Draft skills that are not ready for stable users live in the lifecycle category described in [docs/lifecycle.md](./docs/lifecycle.md); `in-progress` is available as an optional manual-only plugin for explicit evaluation.

## Categories and skills

### `general`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [report-writing](./plugins/general/skills/report-writing/SKILL.md) | Write evidence-backed reports, briefs, and decision memos with sources, confidence labels, conclusions, and next actions. |

#### User-invoked

| Skill | Purpose |
|---|---|
| [make-me-rich](./plugins/general/skills/make-me-rich/SKILL.md) | Plan a task on the expensive model while cheaper sub-agents do bounded read-only analysis, then write an executable plan for cheaper executors. |

### `business-docs`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [business-doc-suite](./plugins/business-docs/skills/business-doc-suite/SKILL.md) | Choose, sequence, and assemble the right business-document package for a venture, pivot, investment, grant, partner, or internal planning request. |
| [core-business-brief](./plugins/business-docs/skills/core-business-brief/SKILL.md) | Create the core business document: essence, customer, value, market, product, revenue model, GTM, operations, financial frame, risks, assumptions, and first 3-6 months. |
| [business-plan-writing](./plugins/business-docs/skills/business-plan-writing/SKILL.md) | Write, rewrite, or audit audience-specific business plans and investment/partner/bank/grant memos from source materials and assumptions. |
| [financial-model-spec](./plugins/business-docs/skills/financial-model-spec/SKILL.md) | Produce a spreadsheet-ready financial model specification with assumptions, formulas, scenarios, validation tasks, and arithmetic checks. |

### `skill-management`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [skill-audit](./plugins/skill-management/skills/skill-audit/SKILL.md) | Audit local skill/package changes and external skill candidates against `writing-great-skills`, Ivan packaging gates, and industrial security checks before publishing or importing. |
| [skill-authoring](./plugins/skill-management/skills/skill-authoring/SKILL.md) | Create, update, promote, move, or retire marketplace skills while keeping source files, invocation class, manifests, README catalogs, dependencies, versions, and validation in sync. |
| [skill-category-management](./plugins/skill-management/skills/skill-category-management/SKILL.md) | Create, update, rename, split, merge, or remove marketplace category plugins with manifests, catalogs, install examples, versions, validation, and migration notes aligned. |

### `marketing`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [lidfly-mcp](./plugins/marketing/skills/lidfly-mcp/SKILL.md) | Use LidFly MCP safely for advertising-platform access, setup checks, tool-scope selection, and read/write guardrails. |
| [campaign-tooling-readiness](./plugins/marketing/skills/campaign-tooling-readiness/SKILL.md) | Prove Avito/Yandex/LidFly tooling readiness before setup: CRUD coverage, analytics quality, discovery backlog, budget controls, and lead-quality loops. |
| [ad-campaign-operations](./plugins/marketing/skills/ad-campaign-operations/SKILL.md) | Operate and optimize advertising campaigns using source docs, campaign structure, metrics, experiments, and weekly action reports. |
| [yandex-wordstat-research](./plugins/marketing/skills/yandex-wordstat-research/SKILL.md) | Estimate Yandex demand, build Wordstat/Direct keyword clusters, mine search queries, plan negatives and campaign structure. |
| [avito-market-intelligence](./plugins/marketing/skills/avito-market-intelligence/SKILL.md) | Research Avito category/geo/pricing/competitors, inspect Avito Ads stats, and plan listing or promotion tests. |
| [avito-ads-feed](./plugins/marketing/skills/avito-ads-feed/SKILL.md) | Generate, audit, and smoke-test Avito service ad feeds, branded cards, listing copy, category mappings, and feed coverage. |
| [lead-routing-tracking](./plugins/marketing/skills/lead-routing-tracking/SKILL.md) | Audit and smoke-test lead forms, UTM/referrer attribution, n8n routing, Telegram/MAX delivery, and analytics goals. |


### `in-progress`

Manual-only draft skills. Install this category only when you explicitly want to evaluate unfinished workflows; draft skills are not model-invoked and are not stable public workflows.

#### User-invoked

| Skill | Purpose |
|---|---|
| [wizard](./plugins/in-progress/skills/wizard/SKILL.md) | Generate an interactive bash wizard for a manual setup, migration, or state transition while preserving confirmation and secret-handling gates. |

### User-invoked

None yet. Prefer direct upstream dependencies for generic command skills like `handoff` unless this marketplace needs a local platform adapter.

## Repository layout

| Path | Role |
|---|---|
| `.agents/plugins/marketplace.json` | Codex marketplace entry pointing at category plugin packages. |
| `.claude-plugin/marketplace.json` | Claude marketplace entry pointing at category plugin packages. |
| `plugins/<category>/.codex-plugin/plugin.json` | Codex category plugin manifest and presentation metadata. |
| `plugins/<category>/.claude-plugin/plugin.json` | Thin category plugin manifest; must list promoted skill folders. |
| `plugins/<category>/skills/<name>/SKILL.md` | Source of truth for shipped skills. |
| `plugins/in-progress/skills/<name>/SKILL.md` | Manual-only draft lifecycle area for skills that are installable only for explicit evaluation. |
| `plugins/<category>/skills/README.md` | Category catalog grouped by invocation class. |
| `docs/invocation.md` | Invocation taxonomy and dependency style. |
| `docs/lifecycle.md` | Draft → published skill lifecycle, including the non-published `in-progress` category. |
| `docs/dependencies.md` | General dependency policy: hard/soft/reference/tool/MCP/plugin deps, fallbacks, and no-vendoring rules. |
| `docs/mattpocock-dependency-candidates.md` | Reference analysis and shortlist of upstream skills to depend on or adapt. |
| `THIRD_PARTY_NOTICES.md` | Required upstream license notices for adapted third-party skill content. |
| `AGENTS.md` | Working rules for agents editing this repo. |

## Manage skills and categories

Skill/category operations are packaged as skills, not kept as README-only procedure:

- Use [`skill-authoring`](./plugins/skill-management/skills/skill-authoring/SKILL.md) to create, update, promote, move, or retire a skill.
- Use [`skill-category-management`](./plugins/skill-management/skills/skill-category-management/SKILL.md) to create, update, rename, split, merge, or remove category plugins.
- Use [`skill-audit`](./plugins/skill-management/skills/skill-audit/SKILL.md) as the publish/import/security gate for every skill, category, dependency, README, manifest, MCP, or packaging change.

Minimum verification remains:

```bash
python3 scripts/validate.py
git diff --check
```

Also parse changed JSON manifests, run `claude plugin validate .` plus `claude plugin validate plugins/<changed-category>` when Claude CLI is available, and smoke-test Codex marketplace registration with `codex plugin marketplace add <path-to-checkout>` when Codex CLI is available. Codex plugin installation itself is interactive through `/plugins`.

## Dependency policy

- Do not vendor third-party skill repos by default.
- Classify dependencies as hard, soft, reference, tool, MCP, or plugin dependencies in [docs/dependencies.md](./docs/dependencies.md).
- For overlaps, prefer upstream dependency/reference plus a thin local adapter; do not restate the full upstream skill locally.
- If the target agent cannot consume the upstream skill directly, document the compatibility gap and maintenance owner before forking/adapting text.
- Do not ship personal, in-progress, or deprecated upstream skills as stable workflows unless there is a fresh local audit and promotion.
