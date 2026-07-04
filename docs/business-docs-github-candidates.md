# Business docs GitHub candidate analysis

Purpose: decide whether to import, depend on, or adapt public GitHub skills for Ivan's `business-docs` category. Result: use public repos as design evidence only; keep local skills small, portable, and focused on Ivan's business-document workflow.

## Snapshot

| Source | Commit inspected | Relevant pattern | Decision |
|---|---:|---|---|
| `bwerneckm/startup-skills` | `5645be0` | 13 startup-operation skills; strong decomposition into business model, GTM, finance, strategy; useful single-primary-home rule for frameworks. | Reference pattern. Do not copy: broad startup-ops framework and company placeholders are heavier than the local document-formation need. |
| `zonghaoyuan/business-plan-skill` | `232a51c` | Business-plan workflow: material audit, active research, interview, narrative construction, arithmetic verification, HTML/PDF output. | Reference pattern. Do not import: optional Puppeteer/HTML dependency and full BP generator are too output-format-specific for the marketplace core. |
| `greeun/business-plan-harness` | `2440752` | Planner→Generator→Evaluator harness; explicit gates for market, customer, financial coherence, assumptions, and no placeholders. | Reference pattern. Do not import: large multi-agent harness and Korean defaults are too heavy; borrow the ideas of research/financial gates and assumption labeling. |
| `ancoop/anskills` / `business-plan-research` | `142b3bd` | Citation-backed business plan, counterevidence, source tiers, parallel research roles, Google Doc output. | Reference pattern. Do not import: Google Drive MCP and quickchart-specific output are runtime-specific. Keep source tiers/counterevidence/neutrality. |
| `tianmind-studio/expert-review-panel` | `25bd988` | Pre-submission expert review with severity, evidence, concrete fix direction; includes business plans and PRDs among review targets. | Reference pattern for audit mode; do not import because scope is broader than business docs. |


## UNIDO baseline adopted after follow-up

Ivan asked to take the UNIDO standard as the base. Official UNIDO sources inspected:

| Source | Role |
|---|---|
| `Annex 7 Guide to the Business Plan` | Lightweight business-plan sequence: introduction, strategic vision, priority activities, funding/budget, organizational structure, risks/assumptions, appendices. |
| `Manual for the Preparation of Industrial Feasibility Studies` | Investment-grade feasibility sequence: executive summary; project background/basic idea; market analysis and marketing concept; raw materials/supplies; location/site/environment; engineering/technology; organization/overhead; human resources; implementation planning/budgeting; financial analysis/investment appraisal. |
| `GSBPC Business Plan Template (simplified)` | Early-startup practical prompts: business idea, product/services, competitors, target market, marketing plan, startup costs/financials. |

Local decision: make UNIDO the default structure and translate industrial terms for service/digital projects rather than importing a third-party business-plan generator.

## Local gaps found

- Existing `general:report-writing` covers reports/briefs, but not a durable business source-of-truth document that feeds a financial model and first 3-6 month plan.
- Marketing skills cover campaign/channel operations, but not foundational business-document formation.
- Existing repo policy already favors small skills, progressive disclosure, source-led research, and not vendoring external skills.

## Adopted patterns

1. **UNIDO baseline, document family, not monolith.** Use UNIDO order as the default and create `business-doc-suite`, `core-business-brief`, `business-plan-writing`, and `financial-model-spec` rather than a single giant business-plan harness.
2. **Core brief first.** The local source of truth is the core business brief: customer, value, market, product, revenue, GTM, operations, financial frame, risks, assumptions, first actions.
3. **Financial coherence gate.** Business plans and financial specs must reconcile price, volume, costs, burn, break-even, runway, and funding use.
4. **Evidence or assumption.** Numbers and market claims are source-backed or explicitly labeled `ASSUMPTION:` with a validation task.
5. **Neutrality and counterevidence.** Plans should surface risks and skeptical data rather than only confirm the idea.
6. **Runtime-neutral output.** Default to markdown artifacts and optional downstream rendering; do not add Google Drive, quickchart, Puppeteer, or multi-agent harness dependencies to the category.

## Import strategy

- Import strategy: **local skills from invariant patterns, no copied upstream prose**.
- Dependency mode: **reference only** for candidate repos.
- Security posture: candidate repos were cloned only for inspection into `/tmp/hermes-business-docs-scan`; no scripts were run and no external skill files were imported.
