# AGENTS.md — Working Rules

Personal, vendor-neutral skills marketplace. Single source of truth for Ivan's promoted agent skills, packaged first for Claude Code and kept portable to Hermes, Codex, and future agents.

## 1. Layout — where things live

| Path | Role | Edit? |
|---|---|---|
| `plugins/<category>/skills/<name>/SKILL.md` | Source for shipped Claude skills | ✅ source |
| `plugins/<category>/skills/README.md` | Category skill catalog grouped by invocation class | ✅ source |
| `.claude-plugin/marketplace.json` | Marketplace entry pointing at plugin/category packages | ✅ thin |
| `plugins/<category>/.claude-plugin/plugin.json` | Category plugin manifest and promoted skill list | ✅ thin |
| `.mcp.json` or runtime MCP manifest, if added | MCP server distribution metadata only: endpoints/packages/placeholders, no secrets | ✅ thin |
| `docs/` | Invocation model, dependency policy, dependency rationale, ADRs/reference notes | ✅ source |
| `AGENTS.md` | Canonical agent instructions for this repo | ✅ source |
| `CLAUDE.md`, `GEMINI.md`, `.cursor/*` | Generated compatibility files if present | ❌ never by hand |

Generated compatibility files are downstream artifacts. If a generated file is stale, update the source rule in `AGENTS.md`, docs, manifests, or the owning `SKILL.md`, then regenerate through the repo's sync path instead of editing the generated file directly.

## 2. Vendor-neutrality

1. Skill bodies describe actions and checks, not proprietary tool names.
2. Per-agent manifests are packaging only; behavior belongs in `SKILL.md` or docs.
3. External capability is declared via open standards or documented prerequisites; never hide dependency logic in prose.
4. Third-party skill repos are dependencies/reference material, not folders to mirror wholesale or prose to rewrite locally.

## 3. Invocation taxonomy

Every promoted skill is either:

- **Model-invoked** — no `disable-model-invocation`; description is model-facing and includes distinct trigger branches.
- **User-invoked** — `disable-model-invocation: true`; description is a human-facing one-line summary.

Keep README, bucket README, and plugin manifest in sync. See `docs/invocation.md`.

## 4. Skill authoring

- One skill = one folder under `plugins/<category>/skills/<kebab-name>/`.
- Frontmatter must include `name` and `description`.
- Keep `SKILL.md` focused on the execution path; put heavy references in sibling files.
- Every step needs a checkable completion criterion.
- Delete no-op prose. If a sentence does not change behavior, output, verification, or refusal boundary, remove it.
- Use `skill-audit` on every local skill, skill category/plugin, skill README, plugin manifest, marketplace manifest, dependency policy, or skill-packaging change.
- Use `skill-audit` on `AGENTS.md` changes that alter editing rules, packaging rules, dependency policy, release/version policy, or the definition of done.
- Use `skill-audit` before installing, copying, forking, importing, or adapting third-party skills.
- Apply the skill/category/dependency CRUD gates in `skill-audit` for create, read/audit, update, delete, move, import/adapt, and plugin dependency promotion.

## 5. External tools and dependencies

- Follow `docs/dependencies.md` for dependency classification: hard, soft, reference, tool, MCP, or plugin.
- Prefer upstream dependency/reference plus a thin local adapter over vendoring another plugin or copying its skill bodies.
- For overlapping skills, keep only local routing, configuration, Ivan/Hermes deltas, and compatibility notes.
- Treat MCP servers as distributed capabilities, not hidden skill code: default to documented external setup or a thin runtime manifest; do not vendor MCP servers, generated tool catalogs, browser/session state, or credentials into skills.
- Use the MCP default ladder before inventing alternatives: hosted/SaaS → remote HTTP MCP with OAuth; no OAuth → HTTP with env placeholder; local/dev tool → stdio pinned `uvx`/`npx` with narrow scopes; team distribution → `.mcp.json` placeholders; personal Hermes runtime → `~/.hermes/config.yaml` plus local secrets; unknown/unverified → documented external MCP plus offline fallback.
- Every MCP-dependent skill must name the server/transport, required tool scopes, auth storage, preflight/test command, read/write guardrails, fallback, and stop condition before it can claim live state or side effects.
- Ship MCP manifests/config snippets only with env/OAuth/secret-store placeholders and disabled-by-default auth when credentials are absent; never commit bearer tokens, cookies, account sessions, or local profile paths.
- If a system CLI, MCP server, API, or credential cannot be bundled, document the prerequisite, preflight, fallback, and stop condition in the owning skill.
- Run the industrial security gate from `skill-audit` on changed or candidate files: prefer `gitleaks`/`trufflehog` when available, otherwise run a fallback secret scan and inspect executable payloads, prompt-injection bait, hidden network/install side effects, and local-only credentials.
- Do not commit secrets: credentials, tokens, local auth files, browser/session profiles, or `*.local.*`. Redact real values as `[REDACTED]` in reports.
- Keep general dependency policy in `docs/dependencies.md`; keep source-specific rationale in a case-study doc such as `docs/mattpocock-dependency-candidates.md` or an ADR.

## 6. Versioning and releases

- Bump the owning `plugins/<category>/.claude-plugin/plugin.json` version on behavior changes.
- Keep `.claude-plugin/marketplace.json` description aligned with the plugin manifest.
- Do not commit or push without explicit user instruction.

## 7. Definition of done

- [ ] Edited source files, not generated files
- [ ] README, bucket README, and plugin manifest agree on promoted skills
- [ ] No placeholder skills are shipped
- [ ] No secrets or local-only credentials introduced
- [ ] Version bumped for behavior changes
- [ ] No commit or push was performed unless Ivan explicitly asked for it
- [ ] `python scripts/validate.py` passes
- [ ] `git diff --check` passes
- [ ] Plugin JSON parses and `claude plugin validate .` / `claude plugin validate plugins/personal-skills` pass when Claude CLI is available
- [ ] `skill-audit` security gate was run on changed/candidate files
