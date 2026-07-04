# GitLab + LidFly advertising-tool synthesis

Purpose: preserve the research behind `campaign-tooling-readiness` without copying third-party code. This is a source ledger and methodology synthesis, not an install plan.

## Research scope

Commands used in July 2026:

- `glab auth status` confirmed GitLab API access as Ivan's account.
- GitLab project search across public projects for `lidfly`, `avito api`, `avito ads`, `yandex direct`, `wordstat`, `yandex metrika`, and adjacent terms.
- GitLab global blob search was attempted and returned `403 Forbidden - Global Search is disabled for this scope`; conclusions therefore come from project search plus targeted repository-file inspection.
- LidFly docs pages inspected directly: `https://lidfly.ru/docs/` and `https://lidfly.ru/docs/quickstart`.

## LidFly docs facts used

Observed from LidFly docs:

- Recommended server for new connections: `https://lidfly.ru/mcp/v3`.
- Quickstart says OAuth in browser is the main connection path; manual API key is not needed for the default path.
- `/mcp/v3` gives access to Yandex Direct/Metrika, VK Ads, LidFly, and Workspaces through one endpoint.
- Docs index describes unified `/mcp/v3` as first clarifying available cabinets and Workspaces, then calling tools with exact scope.
- Docs index lists Yandex Direct as 142 tools covering campaigns, EPK/combinatorial ads, legacy `TEXT_AD`, bids, keywords, statistics, retargeting, dictionaries, multiple OAuth connections, and more.
- Docs index lists Yandex Wordstat as 5 tools via Yandex Search API for phrase frequency, demand trends, and regional distribution.
- Docs index lists Avito Ads as 22 tools, MCP v3 only, covering accounts, balance, API points, campaigns, groups, creatives, statistics, read/write tools, and agency operations.

Implication: the local marketplace should not vendor a third-party MCP. Keep LidFly as a documented external MCP/tool dependency and make every live claim depend on tool discovery/read-back.

## GitLab candidates inspected

### Yandex Direct API/service surface

| Project | Evidence inspected | Useful invariant | Install/adapt decision |
|---|---|---|---|
| `solly/yandex-direct-api` | `src/DirectApiService.php` exposes service classes for ad groups, ad images, ads, agency clients, bid modifiers, bids, campaigns, changes, clients, keywords, reports, sitelinks, vcards; `src/DirectApiResponse.php` parses Direct `Units` header into call cost, remaining units, and unit limit. | A readiness tool must expose object-family CRUD/read paths and API unit/quota budget, not just campaign stats. | Reference only; stale PHP wrapper, no need to vendor. |
| `alex-tsarkov/yandex-direct-generator` | `src/Command/GenerateCommand.php` default service list includes `adextensions`, `adgroups`, `adimages`, `ads`, `agencyclients`, `audiencetargets`, `bids`, `bidmodifiers`, `campaigns`, `changes`, `clients`, `creatives`, `dictionaries`, `dynamictextadtargets`, `keywordbids`, `keywords`, `keywordsresearch`, `leads`, `retargetinglists`, `sitelinks`, `turbopages`, `vcards`. | Yandex readiness should be object-model based: campaigns/groups/ads/creatives/keywords/bids/bid modifiers/leads/retargeting/dictionaries are separate surfaces with separate write risk. | Reference only; code generator is not needed when LidFly/official APIs provide the tool surface. |
| `agpsoftdev/yandexdirectdataexport` | `yandexDirectToBQ.py` uses Direct reports endpoint with TSV fields `Date`, `CampaignType`, `CampaignId`, `CampaignName`, `AdGroupName`, `Impressions`, `Clicks`, `Cost`, `AvgImpressionPosition`, `AvgCpc`, `Ctr`; handles 201/202 queued report responses with `retryIn`; converts micros to currency units; loads newline-delimited JSON to BigQuery. | Analytics readiness must cover report schema, raw export path, queued report/pagination behavior, money-unit normalization, date range, and storage destination. | Reference only; don't copy secrets/config pattern. |

### Yandex Metrika / lead-quality surface

| Project | Evidence inspected | Useful invariant | Install/adapt decision |
|---|---|---|---|
| `artemklevtsov/yametrika` | README and `NAMESPACE` show Management, Reporting, and Logs API client functions: counters, goals, filters, clients linked to Direct, reports, logs, offline conversions, call information uploads, grants/delegates/labels. | Campaign readiness must include goals, Direct-client links, offline/call conversions, logs/report exports, and lead-quality upload paths. | Reference only; R package is a useful taxonomy, not a local runtime dependency. |
| `GreysonD/yandex-metrics-reporter` | Project search description: Yandex.Metrics, Yandex.Direct, Google Analytics; no README found in inspected tree. | Weak signal only: reporting often spans Direct + Metrika + GA, so the skill should require explicit source labels. | Skip as dependency. |

### Wordstat / demand discovery

| Project | Evidence inspected | Useful invariant | Install/adapt decision |
|---|---|---|---|
| `pheix-research/wordstat` | README: parses output tab from `wordstat.yandex.ru` to keyword list; script extracts and joins keywords. | Saved/exported raw Wordstat bundles are better than ad-hoc one-off queries; parse exports into labeled clusters. | Reference only; old script, not a dependency. |
| `budennovsk/wordstat_parse_bot` | README describes Telegram bot for Yandex Wordstat; `main.py` uses browser automation against `https://wordstat.yandex.ru/`, fake user agent, login/password prompt. | Browser-login automation is a safety anti-pattern for our marketplace. Prefer LidFly/Yandex Search API/export; do not ask for passwords or bypass anti-automation. | Skip; anti-pattern only. |

### Avito candidates

| Project/search | Evidence inspected | Useful invariant | Install/adapt decision |
|---|---|---|---|
| `boorwey/avitoapi`, `Andrey_Mlvn/avito-api`, `chessmasteruz/avito-api` | Project trees/READMEs did not expose useful Avito Ads campaign methodology; examples were generic Symfony/test APIs or unrelated. | Public GitLab search did not find a strong Avito Ads CRUD methodology. Use LidFly MCP v3 and official Avito developer/export paths instead. | Skip. |
| `avito parser` search results | Many projects are parsers/grabbers/notifiers for public Avito listings. | Public parsing is not campaign management. Avoid scraping/logged-in/captcha-sensitive flows for Avito Ads readiness. | Skip for ads tooling; only keep safety lessons. |

## Synthesized readiness dimensions

### 1. Platform object CRUD

For each platform, prove object read paths before any write plan:

- account/cabinet and access scope;
- campaign;
- group/ad group;
- ad/creative/listing;
- keyword/query/negative-keyword for Yandex;
- bid/budget/promotion setting;
- goal/conversion/lead route;
- report/export job and raw snapshot.

A future write plan must include object ID, before value, after value, approval gate, read-back method, rollback/pause path, and expected metric impact.

### 2. Analytics quality

Minimum analytics readiness:

- report schema and source are explicit;
- date range, timezone, currency, VAT/discount/micros treatment are known;
- queued/paginated reports are exhausted before conclusion;
- raw export or snapshot is saved;
- traffic metrics are separated from qualified-lead/business metrics;
- failures distinguish missing auth/tool, API budget/rate limit, report queue, source block, and true zero performance.

### 3. Discovery before setup

Yandex discovery:

1. service taxonomy;
2. Wordstat/forecast/export masks;
3. Direct search-query evidence when campaigns already exist;
4. landing/page fit;
5. keyword, negative, ad-group, and campaign-structure proposal.

Avito discovery:

1. target category/subcategory and geo;
2. own listing/feed coverage;
3. public/official competitor sample with qualitative confidence;
4. live stats/export if available;
5. listing quality, creative, price, and promotion/budget test plan.

### 4. Budget and quota controls

Budget tooling must include:

- Yandex Direct API Units/quotas where exposed;
- Avito balance and API points where exposed;
- campaign/group daily and monthly caps;
- spend pacing and alert threshold;
- maximum spend for a test before manual review;
- pause triggers based on spend without qualified leads, CPA above target, or broken attribution.

### 5. Additional surfaces often forgotten

- lead-routing and CRM/manager quality feedback;
- UTM and landing-goal contract;
- moderation/acceptance status for Avito listings/creatives;
- creative asset inventory and proof/trust markers;
- Workspace/project memory snapshots for repeatable campaign context;
- raw export storage and naming convention;
- dry-run/diff support for bulk uploads;
- audit log of applied changes and before/after state;
- rollback/pause path for every budget/status/creative mutation.

## Local implementation decision

Create a local model-invoked adapter skill, `marketing/campaign-tooling-readiness`, because it adds Ivan/Hermes routing, LidFly-first setup, platform-specific readiness gates, and safe write-envelope behavior. Do not copy or install the inspected GitLab projects.

Update marketing indexes and manifests so the skill is promoted with the rest of the marketing plugin. Keep GitLab findings in this reference file behind progressive disclosure.
