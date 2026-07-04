# Skill dependency policy

This repo treats dependencies as **capability contracts**, not as code to vendor. A dependency can be another skill, a plugin, an MCP server, a CLI, an API credential, or a local project convention.

Default rule: keep runtime packages self-contained, document upstream dependencies explicitly, and copy only local adapter behavior that this marketplace owns. MCP servers are distributed capabilities, not skill bodies: ship only safe metadata/config placeholders unless the target runtime has a verified MCP manifest/install path.

## Dependency classes

| Class | Meaning | Where to declare | Required behavior |
|---|---|---|---|
| **Hard skill dependency** | Without it, the local skill produces wrong output or cannot complete its core job. | `docs/dependencies.md` plus the local skill preflight/setup section. | Fail early with the missing dependency and setup path. |
| **Soft skill dependency** | It improves quality but the local skill can still produce useful output. | `docs/dependencies.md` or a short prose pointer in the local skill. | Degrade gracefully and label the fallback. |
| **Reference dependency** | Upstream is evidence, vocabulary, or inspiration; it is not invoked at runtime. | Case-study docs, source ledger, or skill references. | Cite the upstream; do not copy its procedure. |
| **Tool dependency** | A CLI, MCP server, runtime, API, or credential is needed for a branch. | The owning skill's `Prerequisites`, `Portability`, or setup section. | Preflight before use; provide fallback or stop condition. |
| **MCP dependency** | A Model Context Protocol server supplies runtime tools for live reads/writes. | Owning skill plus `docs/dependencies.md`; optional thin `.mcp.json`/runtime manifest only when supported. | Verify live discovery before use; keep secrets out of repo; label fallback output as offline. |
| **Plugin dependency** | Another installable plugin must be installed with this plugin. | `plugin.json dependencies` only after runtime support is verified. | Pin/version explicitly and validate install behavior. |

## Patterns observed in larger skill repos

| Pattern | Why it works | Local policy |
|---|---|---|
| Prose invocation (`Run /other-skill`) | Keeps skills composable without cross-folder coupling. | Prefer `/skill`-style references over deep relative links into another skill. |
| Setup skill for hard deps | Captures issue trackers, labels, doc layouts, credentials, or workspace choices once. | Add setup/preflight only when missing config would make output wrong. |
| Soft-dependency fallback | Avoids blocking useful work when MCP/API/tracker access is missing. | Every optional tool/API branch must say what fallback is allowed. |
| Self-contained plugin bundle | Installed plugin has the files it needs; maintainer-only shared sources are not runtime deps. | Runtime skill folders own their references/templates/scripts. Shared repo docs are policy, not runtime imports. |
| Stdlib/zero-config scripts | Reduces supply-chain and install failures. | Prefer stdlib scripts with sample mode; document unavoidable package/tool deps in the skill. |
| Generated catalogs + validators | Prevents README/manifest drift. | Update README, bucket README, Claude/Codex plugin manifests, and run `python3 scripts/validate.py`. |

## Declaring upstream skill dependencies

Use this table shape for any non-trivial dependency decision:

| Local adapter | Upstream repo | Upstream skill/plugin | Type | Why | Fallback | Status |
|---|---|---|---|---|---|---|
| `skill-management/skill-audit` | `mattpocock/skills` | `writing-great-skills` | reference / soft | Mirrors upstream skill-quality vocabulary, then adds skill/category/dependency CRUD, local packaging, dependency, import-strategy, industrial-security, and Ivan/Hermes publish gates. | Use local audit gate for local skill/category changes and external skill candidates; inspect only the candidate/dependency context needed to decide install vs adapter vs local build. | active |
| planned `software-development/*` adapters | `mattpocock/skills` | `grilling`, `grill-me`, `grill-with-docs` | reference / soft | One-question-at-a-time alignment, recommended answer with each question, and docs/code lookup before asking are reusable across product, architecture, and implementation reviews. | If upstream is unavailable, use local adapter text only for routing, repo-doc taxonomy, and delivery deltas; do not copy the full upstream procedure. | candidate |
| planned `software-development/*` adapters | `mattpocock/skills` | `tdd`, `diagnosing-bugs`, `prototype` | reference / soft | Red-green-refactor, deterministic bug diagnosis, and one-question prototype loops are core software-delivery dependencies that should be referenced at root instead of hidden in a source-specific note. | Use local project test/run commands and cleanup policy as the adapter; fall back to local lifecycle checks when the upstream skill cannot be consumed directly. | candidate |
| planned `software-development/*` adapters | `mattpocock/skills` | `codebase-design`, `domain-modeling`, `improve-codebase-architecture` | reference / soft | Provides shared architecture language: deep modules, seams, adapters, locality, leverage, deletion tests, CONTEXT, and ADR discipline. | Keep local skills focused on repo conventions and packaging; avoid maintaining a forked text copy unless direct dependency consumption is impossible and ownership is explicit. | candidate |
| planned issue/product adapters | `mattpocock/skills` | `to-prd`, `to-issues`, `triage`, `implement` | reference / future adapter | Useful PRD/issue state machine and vertical slicing, but upstream assumes setup/tracker mappings that this marketplace has not standardized yet. | Do not promote until local issue-tracker conventions and fallback behavior are explicit. | candidate |
| `productivity/handoff` or direct upstream dependency | `mattpocock/skills` | `handoff` | reference / direct dependency where available | Generic handoff is useful but should normally remain an upstream command/dependency, not a rewritten local marketplace skill. | Keep local Hermes handoff only as a platform adapter when the target runtime cannot consume upstream directly. | active |
| `plugins/in-progress/skills/wizard` | `mattpocock/skills` | `skills/in-progress/wizard` (+ `template.sh`) | fork/adapt, MIT-licensed draft | Wizard generation is useful for manual setup/migrations, but upstream marks it in-progress and generated scripts can touch `.env` files and GitHub secrets. Keeping it under the manual-only `plugins/in-progress` plugin preserves the draft lifecycle while we evaluate local value and guardrails. | Do not publish or run generated wizards end-to-end without a fresh audit; promote only after secret-handling, attribution, validation, and Claude/Codex packaging gates pass. | active draft |
| `report-writing` | Hermes local skill library | `evidence-first-research-spikes`, `clear-ru-en-writing` | reference / soft | Evidence, confidence, source-ledger, and plain-language report conventions. | Use local report contract when those runtime skills are unavailable. | active |
| `marketing/lidfly-mcp` | `lidfly.ru` | LidFly MCP v3 (`https://lidfly.ru/mcp/v3`) | MCP / soft | Provides advertising-platform access for Yandex Direct/Metrika, VK Ads, Avito Ads, LidFly landing/report tools, and Workspace memory; prefer OAuth when the runtime supports it, with optional `plugins/marketing/.mcp.json` `${LIDFLY_API_KEY}` placeholder for static-token clients. | If MCP is unavailable, produce offline plans only and do not claim live campaign state or side effects. | active |
| `marketing/campaign-tooling-readiness` | GitLab public candidates + LidFly docs | `plugins/marketing/skills/campaign-tooling-readiness/references/gitlab-lidfly-ad-tools-synthesis.md` | reference / MCP / soft | Synthesizes GitLab-observed Yandex Direct service surfaces, report export patterns, Metrika goal/log/offline conversion surfaces, weak/unsafe Avito parser candidates, and current LidFly MCP v3 tool families into a local readiness gate for Ivan campaigns. | If LidFly/official exports are unavailable, produce a blocked/offline readiness checklist only; do not set up or mutate campaigns. | active |
| `marketing/ad-campaign-operations` | `territory-accounting-landing` | `docs/yandex-direct.md` | reference / soft | Project campaign structure, Yandex Direct/Metrika IDs, weekly optimization checklist, and campaign performance workflow. | Treat as offline source context only; require MCP/API read-back before claiming live state or applied changes. | active |
| `marketing/yandex-wordstat-research` | Yandex Direct docs + LidFly docs | Keyword object, report types, LidFly Yandex/Metrika MCP catalog | reference / tool / soft | Provides official orientation for keyword services, bid services, search-query reports, and OAuth/MCP access while keeping live demand/performance data behind tool/export read-back. | If Wordstat/Direct/Metrika/LidFly data is unavailable, produce qualitative/offline research only and do not invent demand, CPC, CTR, or CPA numbers. | active |
| `marketing/avito-market-intelligence` | Avito developer portal + LidFly docs | Avito Swagger API catalog, auction docs, LidFly Avito Ads MCP catalog | reference / tool / soft | Provides Avito API/MCP capability orientation for category, listings, promotion, campaign, creative, and stats research without scraping or unsafe publishing. | If Avito/LidFly/API/export access is unavailable, label public samples as qualitative and do not claim live stats or applied listing/promotion changes. | active |
| `marketing/avito-ads-feed` | `territory-accounting-landing` | `src/pages/avito-feed.xml.ts`, `scripts/generate-avito-cards.ts` | reference / soft | Avito XML feed shape, service × city coverage, branded card generation, and listing constraints. | Run local build/feed checks; require Avito/API/export read-back before claiming live acceptance or performance. | active |
| `marketing/lead-routing-tracking` | `territory-accounting-landing`, `n8n-workflows` | `docs/lead-payload.md`, `docs/integrations/n8n-lead-routing.md`, lead router workflow | reference / soft | Lead payload, UTM/referrer attribution, webhook/n8n routing, messenger delivery, analytics goal smoke checks. | Redact webhook suffixes and chat IDs; require n8n/workflow/read-back before claiming production routing works. | active |

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

## MCP distribution policy

Treat an MCP server as a capability contract with a transport, auth model, tool scope, and verification path. A skill may rely on MCP tools, but must not smuggle the MCP server implementation or credentials into the skill folder.

### Default decision ladder

Use this ladder in order. Do not present all modes as equal choices unless a concrete constraint breaks the default.

| Case | Default solution | Do not do |
|---|---|---|
| Hosted/SaaS service with OAuth MCP support | Remote HTTP MCP using OAuth; tokens live in the client/runtime credential store. | Do not ask for tokens in chat or commit static headers. |
| Hosted/SaaS service with only static token auth | Remote HTTP MCP config with `Authorization: Bearer ${SERVICE_API_KEY}` placeholder; disabled or setup-blocked until the env/secret exists. | Do not paste the real token into `.mcp.json`, docs, examples, or logs. |
| Local/dev tool or local data source | Stdio MCP using pinned `uvx`/`npx`/binary command, minimal args, and narrow filesystem/network scope. | Do not mount broad home directories, run `curl|bash`, or rely on implicit shell env secrets. |
| Team/project distribution | Project/plugin `.mcp.json` or runtime manifest with placeholders, scopes, and verification instructions. | Do not commit user/local MCP config, browser profiles, sessions, or generated tool catalogs. |
| Ivan's personal Hermes runtime | `~/.hermes/config.yaml` `mcp_servers` entry plus local secret source such as `~/.hermes/.env`; restart/new session for discovery. | Do not encode Ivan's machine-local secrets or profile paths in the skills repo. |
| Runtime cannot consume manifests yet | Documented external MCP plus local adapter skill that gives setup, guardrails, fallback, and stop condition. | Do not fork/bundle just to paper over missing marketplace/runtime support. |
| Unknown trust, unpinned package, or unverified setup | Mark as `reference`/`documented external MCP`; provide offline fallback only. | Do not install, import, or claim live access until security and discovery are verified. |

For auth, choose in this order: OAuth/credential store → env/secret-store placeholder → disabled setup instructions. Static literal secrets in repo files are always wrong.

For write-capable MCPs, the default operating mode is read-only discovery first; writes need explicit user-approved scope plus read-back verification.

| Distribution mode | Use when | Required rules |
|---|---|---|
| **Documented external MCP** | The server is hosted remotely or installed by `npx`/`uvx`/vendor docs. | Owning skill names endpoint/package, transport (`stdio` or HTTP), required scopes, auth storage, preflight/test command, fallback, and stop condition. |
| **Thin MCP manifest/config snippet** | The target agent/runtime supports MCP manifests or config import. | Commit only package names, URLs, env-var placeholders, disabled-by-default auth placeholders, timeouts, and scope comments; never commit tokens, cookies, local profile paths, or generated tool catalogs. |
| **Plugin dependency** | The runtime can install another plugin that supplies the MCP capability. | Pass the direct plugin dependency gate below, pin/version it, and verify a clean install discovers the expected MCP tools. |
| **Local adapter skill** | The server is useful but runtime distribution is not portable yet. | Keep only local routing, guardrails, and setup deltas in `SKILL.md`; leave the server as a documented tool dependency. |
| **Fork/bundle MCP server** | Only when no safe upstream install path exists and Ivan accepts maintenance ownership. | Record owner, license, pin, update path, security review, and clean install test before copying any server code. |

Every MCP-dependent skill must include:

- server name and transport, plus expected runtime tool-name prefix when relevant;
- read-only vs write-capable tool split, with writes requiring explicit user-approved scope and read-back verification;
- auth model: OAuth/env/secret store; remote HTTP Bearer/API tokens must be placeholders or disabled until the user sets the secret;
- preflight: how to detect the server and verify at least one expected tool before claiming live access;
- fallback: what offline/local output is allowed when MCP is missing;
- stop condition: what the agent must not claim or do without MCP read-back.

Security gates for MCP distribution:

- Prefer OAuth or runtime secret stores. Do not commit bearer tokens, cookies, browser session files, account IDs tied to secrets, or machine-local profile paths.
- For stdio servers, pin package versions where practical and review install/postinstall behavior; do not use `curl|bash`, `sudo`, destructive filesystem access, or broad filesystem mounts by default.
- For remote HTTP servers, use env placeholders in config snippets and keep unauthenticated placeholders disabled until the secret is present.
- Do not commit generated MCP tool catalogs. Tool names can drift; skills should state expected prefixes/classes and verify live discovery.

## Direct plugin dependency gate

Do not add `plugin.json dependencies` until all are true:

1. The target runtime supports installing and updating that dependency reliably.
2. The dependency is versioned or pinnable.
3. The dependency is needed by a promoted skill, not just a docs preference.
4. The install path was tested from a clean checkout/account.
5. The README states the install/update behavior and fallback if dependency install fails.
6. `python3 scripts/validate.py` or a follow-up validator checks the dependency declaration shape.

Until then, use documented upstream references and local adapters.

## Versioning impact

- Bump the owning `plugins/<category>/.claude-plugin/plugin.json` and `plugins/<category>/.codex-plugin/plugin.json` when a shipped skill, shipped support file, or plugin manifest behavior changes.
- Do not bump the plugin version for repo-only docs that do not change installed skill behavior.
- If dependency policy changes alter how a promoted skill should execute, update the skill and bump the plugin version in the same commit.

## Review checklist

Before adding or changing a dependency:

- [ ] Is this hard, soft, reference, tool, MCP, or plugin dependency?
- [ ] Is the dependency declared in the narrowest useful place?
- [ ] Does the skill have preflight/fallback/stop behavior?
- [ ] If MCP is involved, is distribution mode, transport, auth storage, tool scope, live-discovery test, fallback, and stop condition explicit?
- [ ] Are secrets excluded from docs and examples?
- [ ] Are we copying upstream text? If yes, is the compatibility gap and ownership recorded?
- [ ] Are README, bucket README, Claude/Codex plugin manifests, and validators still in sync?
