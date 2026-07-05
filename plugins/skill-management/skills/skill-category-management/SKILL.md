---
name: lv:skill-category-management
description: "Create, update, rename, split, merge, or remove marketplace category plugins. Use when adding a new plugins/<category> package, changing category boundaries, moving skills between categories, updating marketplace.json, or moving category-management instructions out of README prose into packaged skills."
---

# Skill category management

Manage each stable category as an installable marketplace plugin. A category is not just a README heading: it is a package with a manifest, skill catalog, promoted skills, top-level install/run examples, and validation coverage. `in-progress` is the exception: an installable manual-only lifecycle plugin for explicit draft evaluation.

## Scope gate

Use this skill when a change touches:

- `.claude-plugin/marketplace.json` plugin entries;
- `.agents/plugins/marketplace.json` plugin entries;
- `plugins/<category>/.claude-plugin/plugin.json`;
- `plugins/<category>/.codex-plugin/plugin.json`;
- `plugins/<category>/skills/README.md`;
- install/run examples in the top-level README;
- category boundaries, category names, plugin descriptions, or category versions;
- moves of one or more skills between categories.

Use `skill-authoring` for the detailed per-skill content after the category boundary is chosen.

## Category design rules

1. **Use durable domains.** Stable category names must be kebab-case domains such as `general`, `marketing`, `skill-management`, or a new domain name, not one-off projects.
2. **Keep `in-progress` special.** `plugins/in-progress` is the only lifecycle plugin: list it in Claude/Codex marketplaces only for explicit manual installation; every draft skill must set `disable-model-invocation: true`; examples must be labeled manual-only/draft.
3. **Ship at least one real skill.** Do not publish placeholder-only category plugins; `in-progress` may contain draft skills, but not placeholders.
4. **Keep manifests thin.** Behavior belongs in skills/docs; plugin and marketplace manifests only describe installable packages and list skill folders.
5. **Prefer moves over duplication.** If a skill belongs in the new category, move it and update every old reference instead of copying it.
6. **Keep categories runtime-neutral.** Category boundaries are capability domains, not agent-runtime packages; target-specific packaging belongs in manifests and target-specific README sections.
7. **Bump only affected plugin versions.** New category starts at `0.1.0`. Moving/removing/changing shipped skills bumps old and new affected category manifests.

## Category CRUD loop

1. **Classify the operation.** Choose create, read/audit, update, rename, split, merge, delete, or move-skill. Define the old and new command paths.
2. **Inventory current state.** Check marketplace manifest, category manifest, category README, top-level README, dependency docs, and searches for old category/skill command paths.
3. **Design the boundary.** State why the category is a durable domain and which skills belong there. Leave cross-domain skills in `general` only when no narrower domain applies.
4. **Edit source files.** Create/update:
   - `plugins/<category>/.claude-plugin/plugin.json`;
   - `plugins/<category>/.codex-plugin/plugin.json`;
   - `plugins/<category>/skills/README.md`;
   - one or more `plugins/<category>/skills/<name>/SKILL.md` files;
   - `.claude-plugin/marketplace.json`;
   - `.agents/plugins/marketplace.json`;
   - top-level README install/run examples and promoted category table.
5. **Update references.** Replace stale `/old-category:skill`, old paths, dependency notes, and category examples. If a command path changed, include the migration in the final report.
6. **Run `/skill-management:skill-audit`.** Apply category CRUD, skill move/promotion, dependency, packaging, and industrial security gates.
7. **Validate.** Run repo validator, JSON parse, diff check, and plugin validation when available.

## Delete / merge checklist

Before removing a category:

- [ ] No stable or manual draft install path still needs the category.
- [ ] Skills are moved, deleted with a migration target, or intentionally retired.
- [ ] Marketplace entry, install examples, run examples, category README, and plugin manifest references are gone.
- [ ] Searches find no live `/category:*` command references except migration notes.
- [ ] Validation passes after removal.

## Verification

Run from the repo root:

```bash
python3 scripts/validate.py
git diff --check
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
python3 -m json.tool plugins/<category>/.codex-plugin/plugin.json >/dev/null
python3 -m json.tool plugins/<category>/.claude-plugin/plugin.json >/dev/null
```

If Claude CLI is available, also run:

```bash
claude plugin validate .
claude plugin validate plugins/<category>
```

If Codex CLI is available, smoke-test marketplace registration from the checkout:

```bash
codex plugin marketplace add <path-to-checkout>
```

Completion criterion: marketplace, plugin manifests, category README, top-level README, dependency docs, versions, multimodel portability, and validation all agree; no stale category command/path references remain except explicit migration notes.
