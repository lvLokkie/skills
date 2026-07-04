---
name: campaign-tooling-readiness
description: "Marketing campaign tooling readiness: use before setting up or changing Avito Ads, Yandex Direct/Metrika, VK Ads, or LidFly-managed campaigns when the work is to inventory tools, prove CRUD/read/write coverage, analytics quality, discovery inputs, budget controls, and lead-quality feedback loops before live campaign setup."
---

# Campaign tooling readiness

Use this skill when Ivan wants to **prepare the tool stack before campaign setup**. The goal is not to launch campaigns yet; it is to prove that agents can safely discover accounts, read live state, export analytics, plan writes, control budgets, and verify lead quality through LidFly or official platform paths.

Reference synthesis:

```text
plugins/marketing/skills/campaign-tooling-readiness/references/gitlab-lidfly-ad-tools-synthesis.md
plugins/marketing/skills/lidfly-mcp/SKILL.md
plugins/marketing/skills/yandex-wordstat-research/SKILL.md
plugins/marketing/skills/avito-market-intelligence/SKILL.md
plugins/marketing/skills/lead-routing-tracking/SKILL.md
```

Treat public GitLab projects as capability evidence and anti-pattern signals, not as installable dependencies. Prefer LidFly MCP v3 and official exports/APIs for live work.

## When to use

Use for:

- deciding whether the agent/tool surface is ready for a future Avito or Yandex campaign setup phase;
- building a CRUD/readiness matrix for campaigns, groups, ads/creatives, keywords, bids, budgets, audiences, feeds, and goals;
- checking analytics quality before optimization: stats export, date ranges, UTM/goal joins, lead-quality feedback, and spend pacing;
- planning discovery inputs: Wordstat/Direct reports, Avito category/geo/competitor research, service taxonomy, feed coverage, and landing fit;
- preparing bounded write plans without applying them;
- deciding what tooling is still missing from LidFly, local scripts, project docs, or n8n/CRM before live changes.

Do not use to publish listings, create campaigns, change budgets, alter bids, or edit creatives directly. Route approved live mutations through `lidfly-mcp` plus the platform-specific skill after the readiness gate passes.

## Preflight

1. Identify project and platform branch: `Yandex Direct/Metrika`, `Avito Ads`, `VK Ads`, `cross-platform`, or `offline docs only`.
2. Identify access path:
   - preferred: LidFly MCP v3 server `lidfly`, expected Hermes tool prefix `mcp_lidfly_*`;
   - fallback: official platform API/export/UI screenshot;
   - offline: project docs only.
3. Identify target scope: account/cabinet, campaigns, groups, listings/creatives, feed, geos, service lines, date range, timezone, goals, target CPA/lead-quality threshold, and budget ceiling if known.
4. Set mode:
   - `tool inventory` — discover available tools and scopes;
   - `readiness audit` — prove read/export/report coverage;
   - `write-plan only` — produce object-level mutations for approval later;
   - `blocked/offline` — record missing live access and produce offline next actions.
5. If LidFly tools are unavailable, do not claim live state. Produce a missing-tool checklist and use offline references only.

## Readiness loop

1. **Inventory tools before strategy.** List exact readable and writable object families. Separate read-only, guarded write, destructive/risky write, export/report, and workspace/memory tools.
2. **Build a platform object map.** Record the hierarchy and stable IDs that later writes will need.
3. **Prove read coverage.** For every critical object, specify how to read current state, get stable ID/status, and capture an audit snapshot.
4. **Prove analytics coverage.** Specify reports, metrics, date ranges, segmentation dimensions, pagination/queue behavior, currency/VAT handling, and how raw exports are saved.
5. **Prove discovery coverage.** Route Yandex demand work to `yandex-wordstat-research`; route Avito category/geo/pricing work to `avito-market-intelligence`; route feed/listing coverage to `avito-ads-feed`.
6. **Prove lead-quality coverage.** Route UTM, forms, n8n delivery, Metrika goals, and CRM/manager feedback to `lead-routing-tracking`. Do not optimize spend without a lead-quality signal.
7. **Define write envelopes.** For each future mutation class, define allowed fields, required before/after read-back, dry-run/approval need, rollback path, and stop condition.
8. **Define budget guardrails.** Require account balance/API-point visibility where relevant, daily/monthly budget ceilings, spend pacing alerts, per-test caps, and pause/rollback triggers.
9. **Decide readiness.** Mark each branch `ready`, `partial`, or `blocked`; every blocked item needs the smallest tool, export, doc, or manual step that unblocks it.

## Platform branches

### Yandex Direct / Metrika readiness

Required surfaces:

| Surface | Must prove before setup |
|---|---|
| Account/client | Accessible clients, account/cabinet scope, currency, timezone, API unit/quota visibility. |
| Campaigns/ad groups/ads | List/get current state, stable IDs, status, strategy, geos, schedules, landing URLs, UTM patterns. |
| Keywords/negative keywords | Discovery source, existing keyword/query report, add/remove plan, bulk-upload guard, conflict checks. |
| Bids/budgets/strategies | Read current budgets, bids, bid modifiers, spend pacing, balance/quota; writes need explicit approval. |
| Metrika goals/leads | Counter, goals, offline conversions/call uploads if used, Direct client link, UTM-to-goal join. |
| Reports | Campaign/ad group/ad/criteria/search-query reports with Date, CampaignId, AdGroupName, Impressions, Clicks, Cost, AvgCpc, CTR, conversions/goal fields where available. |

Discovery order: service taxonomy → Wordstat masks/export → Direct forecast/search-query evidence → landing fit → campaign structure proposal. If Wordstat/Direct data is unavailable, label the output as hypothesis-only.

### Avito Ads readiness

Required surfaces:

| Surface | Must prove before setup |
|---|---|
| Account/cabinet | Account list, balance, API points/quota, agency/client scope, object ownership. |
| Listings/feed | Current listings/feed IDs, category/service mapping, city/service coverage, images, prices, moderation/acceptance state. |
| Campaigns/groups/creatives | List/get stable IDs, status, creative assets, group/listing bindings, promotion surfaces. |
| Budget/promotion | Balance, campaign/group budgets, bids/promotion levels if exposed, pacing, per-test caps, stop triggers. |
| Statistics | Views/impressions, contacts/leads, spend, conversion proxy, date range, geo/category/group/creative dimensions. |
| Market discovery | Category/geo/pricing competitor matrix and listing-quality gaps; public samples are qualitative only. |

Discovery order: category/geo hypothesis → own feed/listing coverage → competitor sample/export → live Avito stats if available → listing/promotion test plan. Do not scrape behind login or bypass Avito controls.

## Common CRUD matrix

Use this matrix in readiness reports. Fill `Tool/read path`, `Write path`, `Risk`, and `Blocker` for each platform-specific object.

| Object | Read | Create | Update | Pause/Delete | Analytics | Risk gate |
|---|---|---|---|---|---|---|
| Account/cabinet | Required | N/A | N/A | N/A | balance/quota | Never mutate auth/account settings through campaign ops. |
| Campaign | Required | planned only | approval | approval | spend/CPA/CTR | Budget/status/strategy changes need read-back. |
| Group/ad group | Required | planned only | approval | approval | segment stats | Split/merge affects attribution and budgets. |
| Ad/creative/listing | Required | planned only | approval | approval | CTR/views/contacts | Publishing/moderation risk; keep asset IDs. |
| Keyword/query/negative | Required for Yandex | planned only | approval for bulk | approval | search-query report | Need duplicate/conflict/negative checks. |
| Bid/budget/promotion | Required | approval | approval | approval | pacing/CPC/CPA | Always cap and read back before/after. |
| Goal/lead route | Required | separate approval | separate approval | separate approval | conversion/lead quality | Route through `lead-routing-tracking`. |

## Analytics quality checklist

- Source and mode are explicit: LidFly MCP, official export/API, project docs, or manual sample.
- Date range, timezone, account/campaign IDs, currency, VAT/discount treatment, and sampling/pagination behavior are recorded.
- Raw export/snapshot path or tool read-back is saved when available.
- Metrics separate traffic quality (`CTR`, `CPC`, `views`, `contacts`) from business quality (`valid lead`, `qualified lead`, `CPA`, manager feedback).
- Spend is joined to campaign/group/creative/keyword/listing dimensions before reallocating budget.
- Low-volume recommendations are labeled as hypotheses, not conclusions.
- Failures distinguish no data, auth/tool missing, rate/API budget exhausted, and real zero performance.

## Output

```md
## Campaign tooling readiness: <project/platform>

- Mode: tool inventory | readiness audit | write-plan only | blocked/offline
- Access path: LidFly MCP v3 | official API/export | project docs | missing
- Scope: <accounts/campaigns/geos/services/date range/timezone>
- Verdict: ready | partial | blocked

### Readiness matrix
| Area | Status | Evidence/read-back | Missing tool/data | Next unblocker |
|---|---|---|---|---|

### CRUD and write envelope
| Object | Read path | Planned write path | Approval/read-back gate | Risk |
|---|---|---|---|---|

### Analytics quality
| Metric/Report | Source | Quality | Gap | Action |
|---|---|---|---|---|

### Discovery backlog
- Yandex: <Wordstat/Direct/Metrika tasks or none>
- Avito: <category/feed/competitor/stats tasks or none>
- Lead quality: <routing/goals/CRM feedback tasks or none>
- Budget controls: <caps/pacing/balance/API-point tasks or none>

### Verification
- Tools/files inspected: <exact names/paths/URLs>
- Changes applied: none; readiness only
- Secrets/account-private data: none observed | redacted | blocked
```
