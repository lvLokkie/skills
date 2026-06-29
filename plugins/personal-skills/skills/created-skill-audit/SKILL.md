---
description: Audit agent-authored skills for no-op instructions, token waste, and unclear behavioral effect before keeping or publishing them.
---

# Created Skill Audit

Use this when reviewing a skill written or revised by an agent.

## Goal

Remove instructions that do not change agent behavior. Keep only lines that change what the agent will do, inspect, produce, avoid, or verify.

## Audit steps

1. Read the skill once and list its concrete triggers, inputs, outputs, tools, checks, and stop conditions.
2. Mark every sentence as one of:
   - **Behavioral** — changes a decision, action, artifact, command, check, or output shape.
   - **Context** — explains domain facts the agent cannot infer from the task.
   - **No-op** — only asks for generic quality or intent.
3. Delete no-op text unless it is converted into a measurable rule.
4. Merge duplicate rules and move bulky references out of `SKILL.md` into sibling files when needed.
5. Re-read the shortened skill and verify each remaining line answers: “What would the agent do differently because this line exists?”

## No-op patterns

Delete or rewrite lines like:

- “Be thorough.”
- “Make the commit message detailed.”
- “Write clean/easy-to-read code.”
- “Follow best practices.”
- “Think carefully.”
- “Make sure the result is high quality.”

These are no-ops because agents already attempt them and the line does not specify a different observable behavior.

## Rewrite patterns

| No-op | Behavioral replacement |
|---|---|
| “Be thorough.” | “Check `git status`, changed files, tests, docs, and generated artifacts before finalizing.” |
| “Write clean code.” | “Delete the old branch of logic after replacing it; do not leave compatibility shims unless callers still use them.” |
| “Detailed commit message.” | “Commit subject: `<type>: <change>`; body must include validation commands actually run.” |
| “Follow best practices.” | “Run the repo’s documented validator; if missing, add the exact validation gap to the final report.” |

## Output

Return a compact audit report:

```md
## Skill audit: <skill name>

- Kept: <count> behavioral/context lines
- Removed: <count> no-op lines
- Rewritten: <count> vague lines into measurable rules

### Findings
| Line/section | Classification | Action | Reason |
|---|---|---|---|

### Patch summary
- <files changed or proposed changes>

### Validation
- <commands/checks run>
```

## Decision rule

If removing a sentence would not change the agent’s next action, output, verification step, or refusal boundary, remove it.
