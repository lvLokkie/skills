# Skill lifecycle

This repo separates **draft lifecycle** from **published marketplace distribution**. A skill can be useful before it is ready to install as part of `lvlokkie-skills-marketplace`; that work should have an explicit home and promotion gate instead of being mixed into public categories by accident.

## Lifecycle states

| State | Home | Published? | Purpose |
|---|---|---:|---|
| Candidate / reference | `docs/*-candidates.md`, upstream URL, or local notes | No | Track external ideas and dependency decisions without copying or shipping them. |
| Draft / in-progress | `plugins/in-progress/skills/<name>/` | No | Develop a local skill body before it is safe, stable, and useful enough for public install. |
| Published | `plugins/<category>/skills/<name>/` where `<category>` is not `in-progress` | Yes, when listed in that category plugin manifest and marketplace docs | Shipped skill users can install/run through a category plugin. |
| Deprecated / absorbed | Historical docs or removed tree with migration note | No new installs | Preserve migration/dependency rationale only when useful. |

## `in-progress` category rules

`plugins/in-progress` is a **lifecycle category**, not a marketplace plugin:

- do not list it in `.claude-plugin/marketplace.json`;
- do not add `/in-progress:*` install/run examples to the top-level README;
- do not create `plugins/in-progress/.claude-plugin/plugin.json` unless the category is intentionally being promoted, which should be rare and explicit;
- draft skills still need valid `SKILL.md` frontmatter (`name`, `description`) and should be listed in `plugins/in-progress/skills/README.md` when the directory exists;
- draft skills may be incomplete, but must state their current gap, stop condition, and promotion target if known;
- no secrets, local auth state, generated catalogs, or project-private values are allowed in drafts.

## Promotion gate

Promote a draft only when it passes the same bar as any published skill:

1. Choose the durable published category (`general`, `marketing`, or a new domain category).
2. Move the skill folder out of `plugins/in-progress/skills/` into `plugins/<category>/skills/`.
3. Remove draft-only caveats or convert them into explicit preflight/fallback/stop behavior.
4. Update the destination category `skills/README.md`, `plugins/<category>/.claude-plugin/plugin.json`, the top-level README, and dependency docs when needed.
5. Bump only the destination category plugin version for shipped behavior changes.
6. Run `skill-audit`, `python scripts/validate.py`, `git diff --check`, JSON parsing, plugin validation for the destination category, and the security gate.

## External `in-progress/*` dependencies

Upstream `in-progress/*` skills are not promoted by default. They may be tracked as **candidate/reference** material, then either:

- remain reference-only;
- become a thin local adapter in `plugins/in-progress` while we test the invariant;
- be promoted to a published category after the promotion gate passes.

Do not copy a whole upstream draft category into this repo.
