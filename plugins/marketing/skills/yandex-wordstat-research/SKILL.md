---
name: lv:yandex-wordstat-research
description: "Yandex/Wordstat market and keyword research: use when estimating demand, building keyword clusters, mining search queries, planning Yandex Direct structure, negative keywords, geos, competitor hypotheses, or market research for alpha-service/service projects before or during paid acquisition."
---

# Yandex Wordstat and Direct research

Use this skill for **Yandex-side market intelligence**: demand estimation, keyword/negative-keyword discovery, Direct campaign structure, query mining, and market-research inputs for alpha-service or similar service projects.

Observed reference sources:

- LidFly docs: `https://lidfly.ru/docs/` and `https://lidfly.ru/docs/quickstart` — unified `https://lidfly.ru/mcp/v3`, OAuth-first setup, Yandex Direct/Metrika tool catalog.
- Yandex Direct API keyword object: `https://yandex.ru/dev/direct/doc/en/objects/keyword` — keywords are managed by the `Keywords` service; bids/priorities by `KeywordBids`; keywords may include negative keywords and refining operators.
- Yandex Direct API report types: `https://yandex.ru/dev/direct/doc/reports/type.html` — `SEARCH_QUERY_PERFORMANCE_REPORT` groups report data by ad group and search query; other report types cover account, campaign, ad group, ad, and criteria stats.
- GitHub candidates inspected in July 2026:
  - `nebelov/yandex-direct-for-all` (MIT) — broad Yandex performance plugin; useful methodology: product map → masks → saved Wordstat wave → analysis, and paginated-report exhaustion before conclusions.
  - `puzanov/wordstat-agent` (MIT) — practical Wordstat API notes via Yandex Cloud Search API v2 with `YANDEX_API_KEY` + `YANDEX_FOLDER_ID` and stdlib CLI patterns.
  - `OlegRadinuk/yandex-direct-mcp` and `demokrat90/yandex-direct-mcp` (MIT) — useful dry-run/confirm and sandbox/production safety patterns for write-capable Direct MCPs.
  - `JHamidun/claude-skill-seo-machine-ru` (MIT) mentions browser-cookie/internal Wordstat access; treat that as a fallback warning only, not a default, because official/API/export paths are safer.

Treat source snippets as API orientation, not proof of the current account state. Live state requires MCP/API/UI/export read-back.

## Safety contract

1. **Read-only first.** Keyword research, forecast pulls, reports, and exports are safe; adding keywords, negatives, bids, budgets, or campaign structure needs explicit bounded approval and read-back.
2. **No synthetic demand.** Do not invent frequency, CPC, CTR, CPA, or competitor numbers. If Wordstat/Direct/Metrika/LidFly data is unavailable, label demand as qualitative or hypothesis-only.
3. **Separate external demand from account performance.** Wordstat/forecast data is market demand; Direct/Metrika reports are performance evidence; do not mix them without labeling the source.
4. **Respect platform rules.** Use official UI/API/MCP/export paths. Do not bypass auth, CAPTCHA, rate limits, or scrape protected Yandex surfaces.
5. **Protect account context.** Redact tokens, account IDs tied to credentials, client names, and private campaign IDs unless Ivan asked for project-specific output.

## Preflight

Before research, identify:

- project/service: e.g. `alpha-service`, service lines, offer, landing pages, lead goal;
- geography and language: city/region, Russia-wide vs local, Russian/English query forms;
- decision target: market sizing, campaign launch, campaign expansion, negatives cleanup, budget allocation, or competitor positioning;
- data path: LidFly MCP (`mcp_lidfly_*`), Yandex Cloud Search API Wordstat, Yandex Direct API, Wordstat UI/export, Metrika, saved CSV/XLSX, or offline-only;
- date range/timezone for performance reports;
- acceptable action mode: `research-only`, `read-only live`, `write-planned`, or `write-applied`.

If using LidFly, apply `lidfly-mcp` first: confirm server discovery, account/cabinet scope, and read/write tool boundaries.

## Research loop

1. **Build service taxonomy / product map.** List seed services, synonyms, pain/problem queries, commercial modifiers (`цена`, `заказать`, `под ключ`, `сервис`, `ремонт`, etc.), geo modifiers, exclusions, official names, conversational names, jargon, abbreviations, misspellings, Latin/Cyrillic variants, industry use cases, and competitor/category terms.
2. **Create mask layers before fetching.** Split seeds into `L1 root` broad masks, `L2 product` masks, `L3 commercial` masks, geo masks, and exclusion/negative masks. Do not one-off-query Wordstat while analyzing; first collect a complete labeled raw bundle for the wave.
3. **Cluster by intent.** Split into:
   - high-intent commercial queries;
   - problem/diagnostic queries;
   - competitor/brand queries;
   - informational queries for content/retargeting;
   - irrelevant/negative clusters.
4. **Collect demand evidence.** Prefer Wordstat/Direct forecast/export or LidFly/Yandex tools. Capture exact source, geo, date, query form, and raw artifact path. If only snippets or memory are available, mark as unverified.
5. **Analyze only saved raw bundles.** Read summaries/manifests/TSV/CSV first; avoid dumping long raw JSON into context. Exhaust all pages for paginated reports before conclusions.
6. **Collect account evidence when campaigns exist.** Pull Direct reports for the chosen range. Use `SEARCH_QUERY_PERFORMANCE_REPORT` for real user queries and keyword/negative decisions; use campaign/ad group/ad/criteria reports for structure and performance context.
7. **Triangulate with Metrika/leads.** Join queries/campaigns to goals, UTM, landing pages, and lead quality when available. If lead quality is missing, do not optimize solely for cheap clicks.
8. **Produce action candidates.** Classify each candidate as keyword expansion, negative keyword, ad-group split, geo split, landing/offer gap, budget/bid test, or measurement fix.
9. **Gate changes.** Bulk keyword/negative uploads, bid changes, budget changes, and campaign edits require a concise before/after patch plan and approval unless the user gave a concrete bounded command. Prefer dry-run/sandbox/confirm guards when the selected MCP/API supports them.

## Analysis rubric

For each cluster, record:

| Field | Meaning |
|---|---|
| Intent | commercial / problem / competitor / informational / irrelevant |
| Geo | target city/region or national |
| Evidence | Wordstat/forecast/export/report/MCP/file and date |
| Demand | exact metric if verified; otherwise qualitative label |
| Competition proxy | CPC/bid/auction/visible competitor signal if verified |
| Landing fit | existing page/offer that can satisfy the query |
| Campaign action | add, split, negative, test ad, build page, hold |
| Confidence | high / medium / low based on source quality |

## Stop conditions

Stop and report a blocker when:

- no official/UI/API/export path is available for requested demand numbers;
- the requested operation would edit live Direct campaigns without approved scope;
- data lacks geo/date/source labels;
- query data is too sparse for performance conclusions;
- the work depends on private lead-quality data that is unavailable.

## Output

```md
## Yandex/Wordstat research: <project>

- Mode: research-only | read-only live | write-planned | write-applied | offline fallback
- Scope: <service/geos/date range/account or file>
- Sources: <Wordstat/Direct/Metrika/LidFly/files inspected>
- Verdict: <launch/expand/fix-measurement/hold>

### Demand and keyword map
| Cluster | Intent | Evidence | Action | Confidence |
|---|---|---|---|---|

### Negative keywords / waste
- <query/cluster> → <reason/evidence>

### Campaign structure
- <campaign/ad group/landing mapping>

### Verification
- Tool/file read-back: <IDs, report names, exports, or fallback note>
- Changes applied: <none or IDs with before/after>
- Secrets/account-private data: none observed | redacted | blocked
```
