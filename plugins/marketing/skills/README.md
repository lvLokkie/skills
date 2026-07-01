# Marketing Skills

Promoted skills shipped by the `marketing` plugin. Keep this list in sync with `.claude-plugin/plugin.json`, optional `.mcp.json`, the top-level README, and `docs/dependencies.md`.

## Category contract

Use this category for paid-acquisition and funnel operations where source docs, live marketing tools, MCP/API reads, and production safety boundaries matter. Keep project-specific IDs, offers, phone numbers, webhook suffixes, and account details in the project repo or runtime tool output — not in marketplace skill bodies.

## Skill routing

| Task | Use | Default mode |
|---|---|---|
| Connect/check/use LidFly MCP, advertising account inventory, live campaign reads/writes | [lidfly-mcp](./lidfly-mcp/SKILL.md) | Read-only MCP discovery first; bounded writes only after approval and read-back. |
| Audit/optimize/report paid campaigns across Yandex Direct/Metrika, VK Ads, Avito, LidFly | [ad-campaign-operations](./ad-campaign-operations/SKILL.md) | Source docs first, live/tool metrics second, bounded actions last. |
| Generate or audit Avito XML feeds, service × city coverage, branded cards, listing copy | [avito-ads-feed](./avito-ads-feed/SKILL.md) | Local build/feed checks; live acceptance only with Avito/API/export evidence. |
| Check lead forms, UTM/referrer payloads, n8n routing, Telegram/MAX delivery, analytics goals | [lead-routing-tracking](./lead-routing-tracking/SKILL.md) | Docs/local smoke first; production delivery only with workflow/log/read-back evidence. |

## MCP distribution

The plugin ships an optional `plugins/marketing/.mcp.json` for LidFly remote HTTP MCP:

- server name: `lidfly`;
- endpoint: `https://lidfly.ru/mcp/v3`;
- auth placeholder: `${LIDFLY_API_KEY}`;
- expected Hermes-style tool prefix when discovered: `mcp_lidfly_*`.

Default auth order: OAuth/credential store if the runtime and server support it; otherwise local env/secret-store value for `LIDFLY_API_KEY`; otherwise leave MCP unavailable and use offline fallback. Never commit tokens, cookies, browser sessions, generated tool catalogs, account-private config, or local profile paths.

## Model-invoked

- **[lidfly-mcp](./lidfly-mcp/SKILL.md)** — Use LidFly MCP safely for advertising-platform access, setup checks, tool-scope selection, and read/write guardrails.
- **[ad-campaign-operations](./ad-campaign-operations/SKILL.md)** — Operate and optimize advertising campaigns using source docs, campaign structure, metrics, experiments, and weekly action reports.
- **[avito-ads-feed](./avito-ads-feed/SKILL.md)** — Generate, audit, and smoke-test Avito service ad feeds, branded cards, listing copy, category mappings, and feed coverage.
- **[lead-routing-tracking](./lead-routing-tracking/SKILL.md)** — Audit and smoke-test lead forms, UTM/referrer attribution, n8n routing, Telegram/MAX delivery, and analytics goals.

## User-invoked

None yet.

## Category verification

Before shipping changes to this category:

1. Check that each promoted skill is listed in `.claude-plugin/plugin.json`, this README, and the top-level README.
2. Parse `.mcp.json` and confirm it contains only placeholders, not secrets.
3. Run `python scripts/validate.py`, `git diff --check`, `claude plugin validate plugins/marketing`, and the `/skill-management:skill-audit` security gate.
