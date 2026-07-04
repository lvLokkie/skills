# Marketing Skills

Promoted skills shipped by the `marketing` plugin. Keep this list in sync with `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, optional `.mcp.json`, the top-level README, and `docs/dependencies.md`.

## Category contract

Use this category for paid-acquisition tooling readiness, campaign operations, and funnel operations where source docs, live marketing tools, MCP/API reads, and production safety boundaries matter. Keep project-specific IDs, offers, phone numbers, webhook suffixes, and account details in the project repo or runtime tool output — not in marketplace skill bodies.

## Skill routing

| Task | Use | Default mode |
|---|---|---|
| Connect/check/use LidFly MCP, advertising account inventory, live campaign reads/writes | [lidfly-mcp](./lidfly-mcp/SKILL.md) | Read-only MCP discovery first; bounded writes only after approval and read-back. |
| Prepare tooling before campaign setup: CRUD coverage, analytics quality, discovery backlog, budget controls | [campaign-tooling-readiness](./campaign-tooling-readiness/SKILL.md) | Readiness only; no live campaign mutations, produce unblockers and write envelopes. |
| Audit/optimize/report paid campaigns across Yandex Direct/Metrika, VK Ads, Avito, LidFly | [ad-campaign-operations](./ad-campaign-operations/SKILL.md) | Source docs first, live/tool metrics second, bounded actions last. |
| Estimate Yandex demand, build Wordstat/Direct keyword clusters, mine queries, plan negatives/structure | [yandex-wordstat-research](./yandex-wordstat-research/SKILL.md) | Research/read-only data first; keyword/bid/campaign writes only after approval. |
| Research Avito category/geo/pricing/competitors, pull Avito Ads stats, plan listing/promotion tests | [avito-market-intelligence](./avito-market-intelligence/SKILL.md) | Official/API/export/public-sample evidence; publish/promotion writes only after approval. |
| Generate or audit Avito XML feeds, service × city coverage, branded cards, listing copy | [avito-ads-feed](./avito-ads-feed/SKILL.md) | Local build/feed checks; live acceptance only with Avito/API/export evidence. |
| Check lead forms, UTM/referrer payloads, n8n routing, Telegram/MAX delivery, analytics goals | [lead-routing-tracking](./lead-routing-tracking/SKILL.md) | Docs/local smoke first; production delivery only with workflow/log/read-back evidence. |

## MCP distribution

The plugin ships an optional `plugins/marketing/.mcp.json` for LidFly remote HTTP MCP:

- server name: `lidfly`;
- endpoint: `https://lidfly.ru/mcp/v3`;
- preferred auth: runtime/client OAuth when supported by the MCP client;
- fallback auth placeholder for static-token clients: `${LIDFLY_API_KEY}`;
- expected Hermes-style tool prefix when discovered: `mcp_lidfly_*`.

Default auth order: OAuth/credential store if the runtime and server support it; otherwise local env/secret-store value for `LIDFLY_API_KEY` in static-token clients; otherwise leave MCP unavailable and use offline fallback. Never commit tokens, cookies, browser sessions, generated tool catalogs, account-private config, or local profile paths.

## Model-invoked

- **[lidfly-mcp](./lidfly-mcp/SKILL.md)** — Use LidFly MCP safely for advertising-platform access, setup checks, tool-scope selection, and read/write guardrails.
- **[campaign-tooling-readiness](./campaign-tooling-readiness/SKILL.md)** — Prove Avito/Yandex/LidFly tool readiness before setup: CRUD, analytics quality, discovery inputs, budgets, and lead-quality loops.
- **[ad-campaign-operations](./ad-campaign-operations/SKILL.md)** — Operate and optimize advertising campaigns using source docs, campaign structure, metrics, experiments, and weekly action reports.
- **[yandex-wordstat-research](./yandex-wordstat-research/SKILL.md)** — Estimate Yandex demand, build Wordstat/Direct keyword clusters, mine search queries, plan negatives and campaign structure.
- **[avito-market-intelligence](./avito-market-intelligence/SKILL.md)** — Research Avito category/geo/pricing/competitors, inspect Avito Ads stats, and plan listing or promotion tests.
- **[avito-ads-feed](./avito-ads-feed/SKILL.md)** — Generate, audit, and smoke-test Avito service ad feeds, branded cards, listing copy, category mappings, and feed coverage.
- **[lead-routing-tracking](./lead-routing-tracking/SKILL.md)** — Audit and smoke-test lead forms, UTM/referrer attribution, n8n routing, Telegram/MAX delivery, and analytics goals.

## User-invoked

None yet.

## Category verification

Before shipping changes to this category:

1. Check that each promoted skill is listed in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, this README, and the top-level README.
2. Parse `.mcp.json` and confirm it contains only placeholders, not secrets.
3. Run `python3 scripts/validate.py`, `git diff --check`, `claude plugin validate plugins/marketing` when Claude CLI is available, `codex plugin marketplace add <path-to-checkout>` when Codex CLI is available, and the `/skill-management:skill-audit` security gate.
