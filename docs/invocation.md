# Skill invocation model

This marketplace follows the same core split as `mattpocock/skills`: every promoted skill is either **model-invoked** or **user-invoked**.

## Model-invoked

Use for reusable behavior an agent should reach for autonomously, or behavior another skill must be able to call.

Frontmatter:

```yaml
---
name: example-skill
description: Do X. Use when the user asks for A, mentions B, or another skill needs C.
---
```

Rules:

- Keep the `description` model-facing: state the behavior plus distinct trigger branches.
- Avoid synonym stuffing; one real branch gets one trigger phrase.
- Accept the context-load cost only when autonomous invocation is valuable.

## User-invoked

Use for orchestration flows the human intentionally starts, or rarely used commands that would waste context if auto-loaded.

Frontmatter:

```yaml
---
name: example-command
description: Human-facing one-line summary.
disable-model-invocation: true
---
```

Rules:

- The description is human-facing, not a trigger list.
- A user-invoked skill may call model-invoked skills in prose.
- Do not make a user-invoked skill depend on another user-invoked skill; the model cannot reliably reach it.

## Dependency style

- Express skill-to-skill dependencies as `/skill-name` prose, not deep relative links into another skill's private files.
- Shared reference belongs inside the skill that owns it.
- If a third-party skill is useful as-is, prefer declaring it as a marketplace dependency or tap instead of vendoring it into this repo.
- If only the idea is useful, adapt the invariant into the local umbrella skill and keep attribution in a docs note when required.
