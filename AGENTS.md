# AGENTS.md — Working Rules

Personal, vendor-neutral skills marketplace. Single source of truth for skills,
MCP servers, and agent instructions — synced across devices via git, installed
through the Claude Code plugin marketplace (and portable to other agents).

## 1. Layout — where things live

| Path | Role | Edit? |
|---|---|---|
| skills/<name>/SKILL.md | Single source for every skill | ✅ source |
| .mcp.json | MCP servers (open standard) | ✅ source |
| bin/ | Bundled executables (added to PATH while enabled) | ✅ source |
| hooks/hooks.json | Lifecycle hooks | ✅ source |
| AGENTS.md | Canonical agent instructions (this file) | ✅ source |
| dotfiles/.claude/settings.json | Synced harness settings | ✅ source |
| .claude-plugin/, plugins/ | Claude packaging (thin manifests) | ✅ thin |
| .codex-plugin/ | Codex packaging (thin, optional) | ✅ thin |
| CLAUDE.md, GEMINI.md, .cursor/* | Generated from AGENTS.md | ❌ never by hand |

## 2. Vendor-neutrality (golden rules)

1. skills/ is the ONLY source. Per-tool manifests are thin/generated, never authored content.
2. Write skill bodies in terms of actions ("search the repo", "run the tests"), not Claude-specific tool names.
3. Canonical instructions live in AGENTS.md. CLAUDE.md / GEMINI.md / cursor rules are regenerated, not edited.
4. External capability only via open standards: MCP in .mcp.json; document CLI prerequisites, never assume a proprietary connector.

## 3. Secrets & sync policy

- NEVER commit: ~/.claude.json, .credentials.json, *.local.json, any token / API key.
- Secrets are referenced, not embedded — via env, apiKeyHelper, or ${user_config.*}.
- Committed: settings.json (declarative), AGENTS.md, skills/, .mcp.json (no secrets), bin/, hooks/.
- New device = git clone + fresh claude login. Credentials are per-device, never copied.

## 4. Skill authoring

- One skill = one folder skills/<kebab-name>/SKILL.md.
- Frontmatter description is required, action-oriented, and states when to use the skill.
- Keep SKILL.md focused; put heavy reference material in sibling files (progressive disclosure).
- If a skill needs a CLI or MCP tool, add a preflight check + setup hint inside the skill — no silent assumption.

## 5. External tools and dependencies (MCP / CLI / plugins)

- Prefer bundling: MCP in .mcp.json, scripts/binaries in bin/, all paths via ${CLAUDE_PLUGIN_ROOT}.
- A system CLI you can't bundle (`glab`, `pup`, `jq`) → document the prerequisite in `SKILL.md` with a runtime/preflight check and setup hint. This includes Claude CLIs.
- Plugin-to-plugin dependencies go through `plugin.json dependencies` (semver). This field is for plugins, not CLIs.
- Do not vendor or nest third-party plugins inside this plugin. Keep external plugins as declared dependencies so ownership, updates, and licenses stay clear.
- MCP capabilities are declared through `.mcp.json`, not hidden inside skill prose or proprietary connector assumptions.
- Third-party skills, snippets, or workflow ideas may be adapted into `skills/<name>/SKILL.md` only when the license permits; keep attribution where required.
- Per-tool manifests stay thin/generated and must not become the source of dependency logic.

## 6. Versioning & releases

- Bump plugin.json version on any behavior change — users only receive updates when it changes.
- Keep the marketplace.json plugin entry in sync with the plugin manifest.

## 7. Git workflow

- Never commit or push without an explicit ask. Branch per change: feat/, fix/, docs/, ref/.
- Gate outward actions: confirm before gh repo create, push, or making the repo public.
- After editing skills/ or AGENTS.md, regenerate derived files (`CLAUDE.md`, cursor rules) in the same commit.
- Conventional commit messages.

## 8. Definition of done (any repo change)

- [ ] Edited the single source (`skills/` or `AGENTS.md`), not a generated file
- [ ] Derived files regenerated, or confirmed not present/applicable
- [ ] No secrets introduced
- [ ] version bumped if behavior changed
- [ ] Validated locally: claude --plugin-dir . and/or claude plugin validate
