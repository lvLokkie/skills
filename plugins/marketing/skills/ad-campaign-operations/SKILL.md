---
name: ad-campaign-operations
description: "Advertising campaign operations: use when auditing, optimizing, reporting, or planning paid acquisition campaigns, especially Yandex Direct/Metrika, Avito ads, VK Ads, LidFly-managed campaigns, UTM attribution, landing-page conversion tracking, keyword/negative-keyword work, creative tests, or weekly campaign action reports."
---

# Ad campaign operations

Operate paid acquisition campaigns as a controlled marketing workflow: source context first, live/tool data second, bounded changes last. This skill is grounded in the `territory-accounting-landing` campaign docs but should generalize to other Ivan marketing projects.

Reference sources:

```text
/Users/admin/repos/lvLokkie/territory-accounting-landing/docs/yandex-direct.md
plugins/marketing/skills/ad-campaign-operations/references/github-candidate-synthesis.md
plugins/marketing/skills/campaign-tooling-readiness/references/gitlab-lidfly-ad-tools-synthesis.md
```

The source documents Yandex Direct campaigns for accounting services, Metrika goals, weekly optimization, Avito ads/feed, and campaign constraints. Treat it as project context, not as proof of current live account state.

## When to use

Use for:

- Yandex Direct or Metrika campaign audit, optimization, weekly report, keyword and negative-keyword work;
- Yandex/Wordstat/Direct demand research that should route through `yandex-wordstat-research` before campaign edits;
- Avito ads/feed review, service listing checks, creative/image checklist, campaign readiness, or market intelligence that should route through `avito-market-intelligence` before listing/promotion edits;
- LidFly MCP-backed campaign analysis or live changes;
- campaign setup readiness where `campaign-tooling-readiness` should first prove CRUD coverage, analytics quality, discovery backlog, and budget controls;
- landing-page lead tracking, UTM attribution, goal/conversion checks;
- marketing budget, CTR, CPA, conversion, or campaign structure decisions;
- turning local campaign docs into an action plan.

Do not use for generic copy editing, SEO content writing without paid-campaign metrics, or one-off design feedback unless it affects campaign conversion.

## Preflight

1. Identify platform: Yandex Direct, Metrika, Avito, VK Ads, LidFly, or offline docs only.
2. Identify account/cabinet, campaign IDs/names, date range, timezone, goal IDs, and target CPA/budget if available.
3. Decide mode:
   - **offline docs** — only checked-in files, no live changes;
   - **read-only live** — inspect current campaign/tool data;
   - **write-planned** — propose concrete changes for approval;
   - **write-applied** — apply a bounded approved change and read it back.
4. If the next step is campaign setup or new platform tooling, run `campaign-tooling-readiness` before creating campaigns or changing budgets.
5. If live access goes through LidFly, use `lidfly-mcp` safety rules.

## Operating loop

1. **Read source context.** For territory-accounting, start with `docs/yandex-direct.md`, then inspect landing/deploy/lead docs if attribution or forms matter.
2. **Build campaign map.** List campaigns, groups, geos, services, budgets, goals, feeds, and known exclusions. For pre-launch market work, first build the Yandex/Avito demand map with `yandex-wordstat-research` and/or `avito-market-intelligence`.
3. **Inspect metrics.** Prefer live MCP/API/Metrika data. If unavailable, label all metric-based recommendations as offline assumptions.
4. **Find actions.** Classify each recommendation:
   - negative keyword;
   - keyword expansion;
   - creative/ad copy test;
   - budget/bid/strategy change;
   - goal/UTM/lead-tracking fix;
   - feed/listing/creative asset fix;
   - landing-page conversion issue.
5. **Gate risky changes.** Budget, strategy, status, bulk keyword, and creative publication changes need explicit bounded approval and read-back.
6. **Report results.** Include IDs, before/after values, confidence, and what was not verified.

## Territory-accounting campaign anchors

Known offline anchors from `docs/yandex-direct.md`:

- Yandex Direct MCP/account note: `direct-mcp.aatex.ru` in project docs; prefer LidFly MCP v3 for new work when available.
- Metrika counter: `98342042`.
- Primary goal: `lead_submit` / `350232121`.
- Timezone: `Asia/Yekaterinburg`.
- Search campaigns cover accounting services, accounting support, outsourcing, IP/USN, restoration, and audit across several Russian cities.
- Avito feed: `https://территория-учета.рф/avito-feed.xml`.

Do not treat these as current live state without tool read-back.

## Weekly optimization checklist

1. Pull campaign/account stats for the target date range.
2. Check conversion volume, CPA, CTR, spend pacing, and goal attribution.
3. Review search queries for waste and add candidate negative keywords.
4. Review ad/creative variants and pause or rewrite weak variants only after enough impressions/clicks.
5. Check landing lead path and UTM payload when conversions drop.
6. For CPA above target, propose audience/geography/budget/query changes before increasing spend.
7. For CTR below target, propose ad-copy/offer/quick-link tests.
8. Produce a compact action report and separate applied changes from recommendations.

## Output

```md
## Campaign ops: <platform/project>

- Mode: offline docs | read-only live | write-planned | write-applied
- Scope: <account/campaigns/date range/timezone>
- Source context: <files/tools inspected>
- Metrics: <tool-backed metrics or offline assumption note>

### Findings
| Area | Evidence | Action | Risk |
|---|---|---|---|

### Changes
- Applied: <IDs and before/after values, or none>
- Proposed: <bounded next actions>

### Verification
- <tool read-back, build/feed check, or offline fallback>
- Secrets: none observed | redacted | blocked
```
