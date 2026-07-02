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

In the plugin browser, switch to `lvlokkie-skills-marketplace`, then install `general`, `skill-management`, and `marketing`.

**Activate.** Start a new Codex session after installing or upgrading the plugins. The available skill names are:

```text
general:report-writing
general:make-me-rich
skill-management:skill-audit
skill-management:skill-authoring
skill-management:skill-category-management
marketing:lidfly-mcp
marketing:ad-campaign-operations
marketing:avito-ads-feed
marketing:lead-routing-tracking
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
```

Equivalent commands inside Claude Code:

```text
/plugin marketplace add https://github.com/lvLokkie/skills.git
/plugin install general@lvlokkie-skills-marketplace
/plugin install skill-management@lvlokkie-skills-marketplace
/plugin install marketing@lvlokkie-skills-marketplace
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
/marketing:ad-campaign-operations
/marketing:avito-ads-feed
/marketing:lead-routing-tracking
```

**Keep it updated.** Refresh the marketplace and installed plugins explicitly:

```text
claude plugin marketplace update lvlokkie-skills-marketplace
claude plugin update general@lvlokkie-skills-marketplace
claude plugin update skill-management@lvlokkie-skills-marketplace
claude plugin update marketing@lvlokkie-skills-marketplace
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

Draft skills that are not ready for users live in the lifecycle category described in [docs/lifecycle.md](./docs/lifecycle.md); `in-progress` is intentionally not installed from the marketplace.

## Promoted categories and skills

### `general`

#### Model-invoked

| Skill | Purpose |
|---|---|
| [report-writing](./plugins/general/skills/report-writing/SKILL.md) | Write evidence-backed reports, briefs, and decision memos with sources, confidence labels, conclusions, and next actions. |

#### User-invoked

| Skill | Purpose |
|---|---|
| [make-me-rich](./plugins/general/skills/make-me-rich/SKILL.md) | Plan a task on the expensive model while cheaper sub-agents do bounded read-only analysis, then write an executable plan for cheaper executors. |

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
| [ad-campaign-operations](./plugins/marketing/skills/ad-campaign-operations/SKILL.md) | Operate and optimize advertising campaigns using source docs, campaign structure, metrics, experiments, and weekly action reports. |
| [avito-ads-feed](./plugins/marketing/skills/avito-ads-feed/SKILL.md) | Generate, audit, and smoke-test Avito service ad feeds, branded cards, listing copy, category mappings, and feed coverage. |
| [lead-routing-tracking](./plugins/marketing/skills/lead-routing-tracking/SKILL.md) | Audit and smoke-test lead forms, UTM/referrer attribution, n8n routing, Telegram/MAX delivery, and analytics goals. |

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
| `plugins/in-progress/skills/<name>/SKILL.md` | Draft lifecycle area for skills that are not published or installed. |
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
- Do not ship personal, in-progress, or deprecated upstream skills unless there is a fresh local audit.
