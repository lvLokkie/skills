---
name: skill-authoring
description: "Create, revise, promote, move, or retire skills in this marketplace. Use when adding a SKILL.md, changing a skill's invocation class, moving drafts from in-progress, updating skill references/dependencies, or replacing README-only skill-management instructions with real packaged skills."
---

# Skill authoring

Manage one skill at a time as a shipped artifact, not as loose README prose. The skill folder is the source of truth; README tables and plugin manifests are package indexes.

## Scope gate

Use this skill when a change touches:

- `plugins/<category>/skills/<name>/SKILL.md` or sibling reference/template/script files;
- `plugins/<category>/skills/README.md` entries for a promoted skill;
- `plugins/<category>/.codex-plugin/plugin.json` skill directory and presentation metadata;
- `plugins/<category>/.claude-plugin/plugin.json` skill lists;
- `plugins/in-progress/skills/<name>/` draft lifecycle state;
- top-level README install/run examples or promoted-skill tables;
- dependency notes that explain why a skill is local, upstream, soft, hard, MCP, or reference-backed.

If the change primarily creates/renames/removes a whole category plugin, use `skill-category-management` first and this skill for the per-skill moves.

## Authoring loop

1. **Classify the operation.** Choose create, update, move, promote, retire, or import/adapt. Name the owning category and the expected command path, for example `/skill-management:skill-authoring`.
2. **Check local value.** Keep a local skill only when it adds Ivan/runtime routing, package indexes, dependency handling, verification, guardrails, or workflow behavior that an upstream dependency/reference does not already provide.
3. **Choose lifecycle state.** Use `plugins/in-progress/skills/<name>/` for drafts that are not user-ready. Publish only by moving into a durable marketplace category under `plugins/<category>/skills/<name>/`.
4. **Set invocation class.**
   - Model-invoked: no `disable-model-invocation`; the `description` starts with concrete trigger verbs and names distinct branches.
   - User-invoked: add `disable-model-invocation: true`; the `description` is a short human-facing command summary.
5. **Write the behavior in `SKILL.md`.** Include trigger conditions, inputs, ordered actions, dependency/preflight checks, stop/fallback conditions, output contract, and verification. Move bulky examples or references into sibling files with explicit links.
6. **Preserve multimodel portability.** Keep shared behavior agent-neutral. Put target-specific invocation syntax, install steps, manifest fields, and runtime caveats in target-specific docs/manifests, or document the prerequisite, fallback, and stop condition.
7. **Update package indexes.** Keep the destination `skills/README.md`, destination Claude/Codex plugin manifests, top-level README run examples/promoted table, and dependency docs aligned. When moving a skill, remove stale entries from the old category too.
8. **Bump versions.** Bump only the owning category plugin manifest versions when shipped behavior or command paths change. If moving between categories changes both old and new plugin surfaces, bump both affected plugin manifests.
9. **Run the publish gate.** Run `/skill-management:skill-audit` for the exact CRUD operation, then validation commands.

## Move / promotion checklist

For moving a skill between categories or promoting it from `in-progress`:

- [ ] `name` stays stable unless the skill is intentionally renamed.
- [ ] Old category manifests and README no longer list it.
- [ ] New category manifests and README list it.
- [ ] Top-level README command examples and promoted table point to the new path.
- [ ] Dependency docs and candidate notes use the new path.
- [ ] Migration impact is noted if the user-invoked command path changed.
- [ ] `plugins/in-progress` remains absent from marketplace install examples.

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

Completion criterion: source files, README catalogs, manifests, dependency notes, versions, multimodel portability, and validation agree; `/skill-management:skill-audit` has no unresolved packaging or security findings.
