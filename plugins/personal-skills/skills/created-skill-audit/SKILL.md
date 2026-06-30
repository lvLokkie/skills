---
name: created-skill-audit
description: Audit agent-authored or revised skills for behavioral effect, context load, no-op prose, duplicated meaning, stale sediment, and publish readiness. Use when reviewing a skill, preparing a skill for the marketplace, or adapting workflow ideas from another skill repo.
---

# Created Skill Audit

Audit a skill before keeping, publishing, or adapting it. The standard is **observable behavior**: keep only text that changes what the agent will do, inspect, produce, avoid, or verify.

This skill is model-invoked because agents should reach for it autonomously when asked to create, revise, import, or publish skills.

## Audit loop

1. **Inventory the contract.** List the skill's triggers, inputs, outputs, tools, checks, references, and stop conditions.
2. **Classify every sentence.** Mark each as:
   - **Behavioral** — changes a decision, action, artifact, command, check, output shape, or refusal boundary.
   - **Context** — explains domain facts the agent cannot infer from the task.
   - **No-op** — asks for generic quality or intent without a measurable behavior.
3. **Prune no-ops sentence by sentence.** If a sentence fails the no-op test, delete it unless it can be converted into a checkable rule.
4. **Collapse duplication.** Keep each meaning in one source of truth. Replace repeated explanations with one leading word or one canonical rule.
5. **Move reference down the ladder.** Keep only branch-common steps in `SKILL.md`; move bulky examples, glossaries, and edge cases into sibling reference files with explicit context pointers.
6. **Check invocation shape.** Decide whether the skill is:
   - **model-invoked** — rich trigger phrasing in `description`, no `disable-model-invocation` flag;
   - **user-invoked** — `disable-model-invocation: true`, human-facing one-line description, no trigger list.
7. **Verify publish readiness.** Frontmatter parses, linked files exist, marketplace manifest includes only promoted skills, no secrets or local-only paths are embedded.

Completion criterion: every sentence is classified, every no-op is removed or rewritten, and the remaining skill has a clear invocation class plus a checkable stop condition.

## No-op test

Ask: **If this sentence disappeared, would the agent's next action, output, verification step, or refusal boundary change?**

Delete or rewrite lines like:

- “Be thorough.”
- “Make the commit message detailed.”
- “Write clean/easy-to-read code.”
- “Follow best practices.”
- “Think carefully.”
- “Make sure the result is high quality.”

## Rewrite patterns

| No-op | Behavioral replacement |
|---|---|
| “Be thorough.” | “Check `git status`, changed files, tests, docs, and generated artifacts before finalizing.” |
| “Write clean code.” | “Delete the old branch of logic after replacing it; do not leave compatibility shims unless callers still use them.” |
| “Detailed commit message.” | “Commit subject: `<type>: <change>`; body must include validation commands actually run.” |
| “Follow best practices.” | “Run the repo’s documented validator; if missing, add the exact validation gap to the final report.” |
| “Use this whenever relevant.” | “Use when the user asks to create, revise, import, publish, or audit a skill.” |

## External-skill adaptation gate

When importing ideas from another skill repo:

1. Map the upstream skill to an existing local umbrella skill first.
2. Prefer direct dependency/reference plus a thin local adapter over vendoring whole directories or copying skill bodies.
3. Add only local routing, configuration, deltas, and compatibility notes unless this marketplace explicitly owns the fork.
4. Record the candidate in `docs/mattpocock-dependency-candidates.md` or the relevant dependency note before promoting it.

## Output

Return a compact audit report:

```md
## Skill audit: <skill name>

- Invocation: model-invoked | user-invoked
- Kept: <count> behavioral/context sentences
- Removed: <count> no-op sentences
- Rewritten: <count> vague sentences into measurable rules
- Moved to references: <files or none>

### Findings
| Section | Classification | Action | Reason |
|---|---|---|---|

### Patch summary
- <files changed or proposed changes>

### Validation
- <commands/checks run>
```
