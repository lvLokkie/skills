---
name: lv:avito-market-intelligence
description: "Avito market intelligence and ads analytics: use when researching Avito demand, competitor listings, category/geo/pricing, promotion mechanics, Avito Ads/LidFly MCP stats, campaign groups/creatives, or market research for alpha-service/service projects."
---

# Avito market intelligence

Use this skill for **Avito-side market and campaign intelligence**: category/geo demand, competitor listing review, price bands, offer gaps, promotion hypotheses, Avito Ads stats, and listing/campaign analytics for alpha-service or similar service projects.

Observed reference sources:

- LidFly docs: `https://lidfly.ru/docs/` — Avito Ads is exposed through MCP v3 only; docs describe tools for accounts, balance, API points, campaigns, groups, creatives, statistics, read/write operations, and agency operations.
- Avito developer portal: `https://developers.avito.ru/api-catalog` — API descriptions are published in Swagger 3.0; API use requires authorization; personal and application authorization types are documented.
- Avito auction docs found at `https://developers.avito.ru/api-catalog/auction/documentation` — auction mechanics regulate promotion levels with bids.
- GitHub candidates inspected in July 2026:
  - `elchin92/avito-mcp` (package declares MIT) — broad Avito MCP with read-only/guarded/full modes, allowlists, confirmation meta-tools, local-first credentials, and useful tool families for stats/promotion.
  - `MissiaL/avito-api` — agent-skill pattern around the official Avito OpenAPI spec; useful invariant: do not load the whole spec, search/show endpoint slices and inspect security/scope per operation.
  - `b1zya/n8n-nodes-avito-api` (MIT) — n8n community node with OAuth2 credential handling and Avito resources including items, promotion, messenger, ratings, autoload, CPA/call tracking.

Treat these as capability references. Current listing status, spend, balance, and performance require LidFly/Avito/API/export read-back.

## Safety contract

1. **Official paths only.** Prefer LidFly MCP, Avito API, Avito Pro/API exports, or manually provided exports/screenshots. Do not bypass login, CAPTCHA, robots, or protected Avito pages.
2. **Read-before-write.** Listing, campaign, group, creative, bid, promotion, or budget changes need current object read-back and an approved before/after plan.
3. **Separate market sample from live stats.** Public listing samples show positioning/pricing, not actual demand or contacts. Live Avito stats/exports show performance.
4. **No fake competitor metrics.** If views, contacts, spend, or bid data is not returned by an official tool/export, mark it unknown.
5. **Redact private account context.** Do not expose tokens, client IDs tied to credentials, chat data, phone numbers, exact account balances, or manager names unless Ivan asked for a project-specific report.

## Preflight

Identify:

- project/service and target Avito category/subcategory;
- target geos and service radius;
- decision target: launch, category selection, price positioning, creative/listing refresh, promotion budget, or competitor audit;
- access path: LidFly MCP (`mcp_lidfly_*`), Avito MCP/API/export, n8n Avito node, feed files, manual screenshots, or public sample only;
- target objects: account/cabinet, campaigns, groups, creatives, listings, feed IDs, date range;
- mode: `market research`, `read-only live`, `write-planned`, or `write-applied`.

If live access goes through LidFly, use `lidfly-mcp` first and confirm Avito account/campaign scope.

## Research loop

1. **Map the category.** Confirm category/subcategory, required listing fields, promotion surfaces, competitor query set, geos, and service intent.
2. **Pick the safest tool mode.** Prefer read-only/live inventory first. If an Avito MCP exposes modes, use `read_only` for discovery, `guarded` for proposed writes, and avoid `full_access` unless Ivan gave a bounded mutation and the tool has confirmation/read-back.
3. **Discover endpoints/tools narrowly.** If using an OpenAPI/spec helper, search by tag/path/summary and show only the target endpoint/schema/security fields. Do not load multi-megabyte specs into context.
4. **Inventory own supply.** Read current listings/feed/campaigns/groups/creatives where available. Check service × city coverage, title/description fit, price, image, contact path, and UTM/lead routing.
5. **Sample the market safely.** Use official exports/API when available. If only public Avito pages are reviewed manually, keep sample size small, record query/geo/date, and label it `manual public sample`.
6. **Build competitor matrix.** Compare title promise, price band, proof/trust markers, photos/cards, delivery/response terms, review signals, freshness, and promotion visible placement where observable.
7. **Pull live stats when available.** Read impressions/views/contacts/conversion/spend/balance/campaign/group/creative stats from LidFly/Avito/API/export. Record date range and timezone.
8. **Diagnose gaps.** Classify findings as category mismatch, weak title, price mismatch, missing proof, poor creative, thin geo/service coverage, low promotion, lead-routing gap, or measurement gap.
9. **Plan tests.** Propose small bounded tests: listing copy variant, price/offer band, card image, category/geography split, promotion bid/budget, or feed coverage change.
10. **Gate changes.** Publishing listings, editing creatives, changing promotion/bids/budget, sending messages, or pausing campaigns requires approval and read-back by object ID/status.

## Analysis rubric

| Area | Evidence to collect | Decision |
|---|---|---|
| Category fit | Avito category/API/feed/listing source | keep / move / split |
| Geo fit | target city/region sample or stats | launch / expand / hold |
| Price band | competitor sample + own economics | lower / justify premium / add entry offer |
| Offer strength | title, proof, service terms, reviews | rewrite / add proof / keep |
| Creative | image/card/listing visual check | regenerate / A-B test / keep |
| Promotion | auction/bid/stats evidence | increase / decrease / test / unknown |
| Lead quality | contacts → CRM/n8n/Metrika/manager feedback | scale / filter / fix routing |

## Stop conditions

Stop before claiming success when:

- requested live stats require Avito/LidFly access that is not configured;
- public sample is too small or unrepresentative for a demand conclusion;
- the action would publish/edit/pause/promote live listings without approval;
- official data lacks date range, object IDs, or account scope;
- the requested tactic would violate Avito terms or automation controls.

## Output

```md
## Avito market intelligence: <project>

- Mode: market research | read-only live | write-planned | write-applied | offline fallback
- Scope: <category/geos/listings/campaigns/date range>
- Sources: <LidFly/Avito/API/export/feed/public sample/files>
- Verdict: <launch/expand/fix-listings/test-promotion/hold>

### Market and competitor map
| Segment | Evidence | Gap | Action | Confidence |
|---|---|---|---|---|

### Campaign/listing actions
- Applied: <none or IDs with before/after>
- Proposed: <bounded tests or fixes>

### Verification
- Read-back: <tool/export/file/public sample note>
- Live Avito status: verified | not verified | blocked
- Secrets/account-private data: none observed | redacted | blocked
```
