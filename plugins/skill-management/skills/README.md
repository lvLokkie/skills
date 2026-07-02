# Skill Management Skills

Promoted skills shipped by the `skill-management` plugin. Keep this list in sync with `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, and the top-level README.

Use this category for workflows that manage this repository's skill lifecycle, category plugins, marketplace indexes, dependency gates, and publish readiness. Domain execution skills belong in narrower categories such as `general` or `marketing`.

## Model-invoked

Model- or user-reachable. Descriptions use trigger phrasing so an agent can load the skill autonomously.

- **[skill-audit](./skill-audit/SKILL.md)** — Audit local skill/package changes and external skill candidates against `writing-great-skills`, Ivan packaging gates, and industrial security checks before publishing or importing.
- **[skill-authoring](./skill-authoring/SKILL.md)** — Create, update, promote, move, or retire marketplace skills while keeping source files, invocation class, manifests, README catalogs, dependencies, versions, and validation in sync.
- **[skill-category-management](./skill-category-management/SKILL.md)** — Create, update, rename, split, merge, or remove marketplace category plugins with manifests, catalogs, install examples, versions, validation, and migration notes aligned.

## User-invoked

Reachable only when a human explicitly invokes the skill. None yet.

## Category gate

Before publishing changes in this category:

1. Confirm each promoted skill is listed in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, this README, and the top-level README.
2. Run `/skill-management:skill-audit` for the relevant skill/category CRUD operation and security gate.
3. Run `python3 scripts/validate.py`, `git diff --check`, JSON parsing, `claude plugin validate plugins/skill-management` when Claude CLI is available, and `codex plugin marketplace add <path-to-checkout>` when Codex CLI is available.
