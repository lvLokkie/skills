# In-progress Skills

Draft skills that are useful enough to evaluate but not ready for stable marketplace promotion. This lifecycle category is installable only as a manual-invocation plugin: every draft skill must set `disable-model-invocation: true`, and agents must not load these skills autonomously.

## Manual install

Claude Code:

```text
/plugin install in-progress@lvlokkie-skills-marketplace
```

Codex: install `in-progress` from the `lvlokkie-skills-marketplace` plugin browser (`/plugins`).

## User-invoked draft skills

| Skill | Status | Promotion target |
|---|---|---|
| [wizard](./wizard/SKILL.md) | Imported draft from `mattpocock/skills` for evaluation; manual-only and not stable. | Promote only after `/skill-management:skill-audit` confirms local value, secret-handling guardrails, packaging, and validation. |

## Draft gate

Before promoting any draft:

1. Convert draft caveats into explicit preflight/fallback/stop behavior.
2. Move the skill into a durable published category under `plugins/<category>/skills/`.
3. Update both Claude and Codex manifests, bucket README, top-level README, dependency notes, and versions.
4. Run `python3 scripts/validate.py`, `git diff --check`, JSON parsing, Claude plugin validation when available, Codex marketplace registration smoke test when available, and the `/skill-management:skill-audit` security gate.
