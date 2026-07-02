# Skill lifecycle

This repo separates **draft lifecycle** from **stable marketplace distribution**. A skill can be useful before it is ready as a stable workflow; that work has an explicit manual-only home and promotion gate instead of being mixed into stable public categories by accident.

## Lifecycle states

| State | Home | Published? | Purpose |
|---|---|---:|---|
| Candidate / reference | `docs/*-candidates.md`, upstream URL, or local notes | No | Track external ideas and dependency decisions without copying or shipping them. |
| Draft / in-progress | `plugins/in-progress/skills/<name>/` | Manual-only | Evaluate a local skill body before it is safe, stable, and useful enough for stable categories. |
| Published | `plugins/<category>/skills/<name>/` where `<category>` is not `in-progress` | Yes, when listed in that category plugin manifest and marketplace docs | Shipped skill users can install/run through a category plugin. |
| Deprecated / absorbed | Historical docs or removed tree with migration note | No new installs | Preserve migration/dependency rationale only when useful. |

## `in-progress` category rules

`plugins/in-progress` is a **manual-only lifecycle plugin**, not a stable marketplace category:

- list it in `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` only so drafts can be manually installed;
- every draft skill must be user-invoked with `disable-model-invocation: true`;
- public docs may show `/in-progress:*` only under an explicit manual-only draft section;
- draft skills still need valid `SKILL.md` frontmatter (`name`, `description`, `disable-model-invocation: true`) and must be listed in `plugins/in-progress/skills/README.md`;
- draft skills may be incomplete, but must state their current gap, stop condition, and promotion target if known;
- no secrets, local auth state, generated catalogs, or project-private values are allowed in drafts.

## Promotion gate

Promote a draft only when it passes the same bar as any published skill:

1. Choose the durable published category (`general`, `marketing`, or a new domain category).
2. Move the skill folder out of `plugins/in-progress/skills/` into `plugins/<category>/skills/`.
3. Remove draft-only caveats or convert them into explicit preflight/fallback/stop behavior.
4. Update the destination category `skills/README.md`, `plugins/<category>/.claude-plugin/plugin.json`, `plugins/<category>/.codex-plugin/plugin.json`, both marketplace manifests, the top-level README, and dependency docs when needed.
5. Bump only the destination category plugin version for shipped behavior changes.
6. Run `/skill-management:skill-audit`, `python3 scripts/validate.py`, `git diff --check`, JSON parsing, Claude plugin validation for the destination category when available, Codex marketplace registration smoke test when available, and the security gate.

## External `in-progress/*` dependencies

Upstream `in-progress/*` skills are not stable-promoted by default. They may be tracked as **candidate/reference** material, manually installed under `plugins/in-progress`, then either:

- remain reference-only;
- become a manual-only local adapter in `plugins/in-progress` while we test the invariant;
- be promoted to a published category after the promotion gate passes.

Do not copy a whole upstream draft category into this repo.
