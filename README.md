# Personal Claude Code Skills Marketplace

A minimal personal Claude Code plugin marketplace for installing Ivan's own skills on any machine.

The `hello-world` skill is only a placeholder smoke test; delete it when real skills exist.

## Install

```text
/plugin marketplace add lvLokkie/personal-claude-skills-marketplace
/plugin install personal-skills@personal-skills-marketplace
/personal-skills:hello-world
```

## Add a new skill

Create `plugins/personal-skills/skills/<name>/SKILL.md` with required frontmatter:

```md
---
description: What this skill does and when to use it.
---
Skill instructions go here.
```

Skills auto-discover from `skills/`; no path fields are needed in `plugin.json`.

For private repos, installation needs a git credential helper or a `GITHUB_TOKEN` environment variable.
