# Skill dependency policy

This repo treats dependencies as **capability contracts**, not as code to vendor. A dependency can be another skill, a plugin, an MCP server, a CLI, an API credential, or a local project convention.

Default rule: keep runtime packages self-contained, document upstream dependencies explicitly, and copy only local adapter behavior that this marketplace owns.

## Dependency classes

| Class | Meaning | Where to declare | Required behavior |
|---|---|---|---|
| **Hard skill dependency** | Without it, the local skill produces wrong output or cannot complete its core job. | `docs/dependencies.md` plus the local skill preflight/setup section. | Fail early with the missing dependency and setup path. |
| **Soft skill dependency** | It improves quality but the local skill can still produce useful output. | `docs/dependencies.md` or a short prose pointer in the local skill. | Degrade gracefully and label the fallback. |
| **Reference dependency** | Upstream is evidence, vocabulary, or inspiration; it is not invoked at runtime. | Case-study docs, source ledger, or skill references. | Cite the upstream; do not copy its procedure. |
| **Tool dependency** | A CLI, MCP server, runtime, API, or credential is needed for a branch. | The owning skill's `Prerequisites`, `Portability`, or setup section. | Preflight before use; provide fallback or stop condition. |
| **Plugin dependency** | Another installable plugin must be installed with this plugin. | `plugin.json dependencies` only after runtime support is verified. | Pin/version explicitly and validate install behavior. |

## Patterns observed in larger skill repos

| Pattern | Why it works | Local policy |
|---|---|---|
| Prose invocation (`Run /other-skill`) | Keeps skills composable without cross-folder coupling. | Prefer `/skill`-style references over deep relative links into another skill. |
| Setup skill for hard deps | Captures issue trackers, labels, doc layouts, credentials, or workspace choices once. | Add setup/preflight only when missing config would make output wrong. |
| Soft-dependency fallback | Avoids blocking useful work when MCP/API/tracker access is missing. | Every optional tool/API branch must say what fallback is allowed. |
| Self-contained plugin bundle | Installed plugin has the files it needs; maintainer-only shared sources are not runtime deps. | Runtime skill folders own their references/templates/scripts. Shared repo docs are policy, not runtime imports. |
| Stdlib/zero-config scripts | Reduces supply-chain and install failures. | Prefer stdlib scripts with sample mode; document unavoidable package/tool deps in the skill. |
| Generated catalogs + validators | Prevents README/manifest drift. | Update README, bucket README, plugin manifest, and run `python scripts/validate.py`. |

## Declaring upstream skill dependencies

Use this table shape for any non-trivial dependency decision:

| Local adapter | Upstream repo | Upstream skill/plugin | Type | Why | Fallback | Status |
|---|---|---|---|---|---|---|
| `skill-audit` | `mattpocock/skills` | `writing-great-skills` | reference / soft | Mirrors upstream skill-quality vocabulary, then adds skill/category/dependency CRUD, local packaging, dependency, import-strategy, industrial-security, and Ivan/Hermes publish gates. | Use local audit gate for local skill/category changes and external skill candidates; inspect only the candidate/dependency context needed to decide install vs adapter vs local build. | active |
| `report-writing` | Hermes local skill library | `evidence-first-research-spikes`, `clear-ru-en-writing` | reference / soft | Evidence, confidence, source-ledger, and plain-language report conventions. | Use local report contract when those runtime skills are unavailable. | active |

Rules:

1. **Do not vendor by default.** Do not copy another repo's skill body, reference tree, plugin, or generated catalog into this repo just because it overlaps with local needs.
2. **Prefer upstream reference plus a thin adapter.** Local text may add routing, Ivan/Hermes paths, GitHub/GitLab/Kanban/Telegram conventions, setup deltas, and compatibility notes.
3. **Fork/adapt only with an owner decision.** If the target runtime cannot consume upstream directly and the workflow is important enough to maintain, record the compatibility gap and the maintenance owner before copying/reworking content.
4. **Keep reference docs inside the owning skill.** Cross-skill dependencies should invoke the skill or point to its public entrypoint, not reach into `../other-skill/references/private-file.md`.
5. **Preserve attribution.** If upstream ideas shape local behavior, keep a source note in this file, a case-study doc, or the skill's references.

## Tool and API dependencies

A skill that depends on a tool/API must include a preflight section with:

- command/API name;
- how to detect availability;
- minimum version or scope when relevant;
- safe setup hint;
- fallback behavior;
- stop condition when no fallback is safe;
- secret-handling rule if credentials are involved.

Example:

```md
## Prerequisites

- `gh` authenticated for GitHub issue writes. Check with `gh auth status`.
- Fallback: if `gh` is unavailable, write local markdown issues under `.scratch/issues/` and label the output as local-only.
- Stop: do not invent issue numbers or claim GitHub side effects without `gh issue view` read-back.
```

## Direct plugin dependency gate

Do not add `plugin.json dependencies` until all are true:

1. The target runtime supports installing and updating that dependency reliably.
2. The dependency is versioned or pinnable.
3. The dependency is needed by a promoted skill, not just a docs preference.
4. The install path was tested from a clean checkout/account.
5. The README states the install/update behavior and fallback if dependency install fails.
6. `python scripts/validate.py` or a follow-up validator checks the dependency declaration shape.

Until then, use documented upstream references and local adapters.

## Versioning impact

- Bump `plugins/personal-skills/.claude-plugin/plugin.json` when a shipped skill, shipped support file, or plugin manifest behavior changes.
- Do not bump the plugin version for repo-only docs that do not change installed skill behavior.
- If dependency policy changes alter how a promoted skill should execute, update the skill and bump the plugin version in the same commit.

## Review checklist

Before adding or changing a dependency:

- [ ] Is this hard, soft, reference, tool, or plugin dependency?
- [ ] Is the dependency declared in the narrowest useful place?
- [ ] Does the skill have preflight/fallback/stop behavior?
- [ ] Are secrets excluded from docs and examples?
- [ ] Are we copying upstream text? If yes, is the compatibility gap and ownership recorded?
- [ ] Are README, bucket README, plugin manifest, and validators still in sync?
