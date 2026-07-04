---
name: core-business-brief
description: "Create or revise the core business document for a new venture: business concept note, venture brief, startup foundation memo, business blueprint, or founding business brief. Use when the user wants to define what sells, to whom, why they buy, how value is delivered, how money is made, what assumptions/risks exist, and what should feed the financial model and first 3-6 month plan."
---

# Core business brief

A core business brief is the source document for a new business. It is not a questionnaire and not a pitch: it fixes the business logic, evidence, assumptions, operating model, and financial-model inputs that later docs must not contradict.

Default to the UNIDO business-plan / industrial-feasibility-study sequence in `references/unido-standard.md`, adapted for the business type. For digital or service businesses, translate industrial terms such as raw materials, plant capacity, location, and engineering into key inputs, service capacity, operating geography, technology, and delivery process.

## When to use

Use when the user asks for a:

- business concept note, venture brief, startup foundation memo, business blueprint, founding memo, or core business document;
- structured definition of a new company, product line, market entry, or pivot;
- base document for a financial model, business plan, investor deck, grant proposal, or operating plan;
- critique/rewrite of a business idea where assumptions and first actions matter more than polish.

## Inputs to establish

Proceed with explicit assumptions when details are missing, but first classify:

| Field | Examples |
|---|---|
| Stage | raw idea, validation, MVP, revenue, pivot, expansion |
| Geography | city/country/online/global and any regulated jurisdictions |
| Customer | buyer, user, decision maker, budget holder |
| Offering | product/service, delivery mode, pricing hypothesis |
| Evidence | sources, interviews, competitor pages, internal numbers, unknowns |
| Intended next artifact | financial model, business plan, deck, operating plan |

## Workflow

1. **Inventory materials.** Read provided notes/docs/links. Build an information map: `provided`, `source-backed`, `assumption`, `missing`, `contradiction`.
2. **Research only decision-critical gaps.** For market, competitor, pricing, regulatory, or benchmark claims, inspect sources before citing. Do not cite search snippets.
3. **Write the 1-page kernel first.** Include: business essence, customer, pain, offer, revenue model, wedge, first milestone, biggest assumption, and kill criterion.
4. **Write the 5-10 page core document** using the UNIDO-adapted structure below.
5. **Create a financial-model input ledger.** Extract price, volume, capacity, conversion, CAC, variable inputs, fixed costs, staffing, working capital, financing sources, break-even, scenarios, and validation owner into a table.
6. **Create the first 3-6 month implementation plan and provisional budget.** Tie each activity to timing, owner, expected result, cost, funding source, assumption tested, metric, and refusal/kill criterion.
7. **Run consistency checks.** Money rules, target customer, product scope, marketing concept, operating model, implementation budget, and financial model must agree across sections.

## Required UNIDO-adapted structure

0. **One-page kernel / executive summary** — business essence, customer, offer, economics, first milestone, biggest assumption, and kill criterion.
1. **Project background and basic idea** — origin, purpose, goals, timeframe, problem, solution, and why now.
2. **Strategic vision and objectives** — SWOT-informed direction, target market focus, product range, price posture, distribution, promotion, and competitiveness.
3. **Market analysis** — demand, segments, customer/buyer/decision maker, competitors, substitutes, barriers, and source-backed market assumptions.
4. **Marketing concept / go-to-market** — positioning, pricing, channels, promotion, sales cycle, first experiments, and expected results.
5. **Product/service, capacity, key inputs and suppliers** — MVP, packages, service levels, capacity/throughput, raw materials or digital inputs, supplier/API/data dependencies.
6. **Location / operating geography / environmental and regulatory constraints** — site or service geography, infrastructure, platform/channel constraints, legal/regulatory and environmental/social issues.
7. **Engineering, technology and operating model** — delivery process, technology choices, make/buy/partner decisions, quality controls, support and maintenance.
8. **Organization, overhead, team and human resources** — responsibilities, key roles, hiring/training needs, overhead categories, contractors and governance.
9. **Implementation plan and provisional budget** — priority activities, timing, owner, cost, funding source, expected result.
10. **Financial analysis and investment appraisal frame** — startup investment, opex, working capital, revenue drivers, break-even, cash-flow needs, financing options, scenario/sensitivity inputs.
11. **Major risks, assumptions and kill criteria** — what must be true, how to test it, metric, owner, mitigation, and stop condition.
12. **Appendices / evidence ledger** — proof for claims: sources, quotes, calculations, resumes, legal docs, detailed schedules.

## Quality gates

| Gate | Pass condition |
|---|---|
| Customer specificity | Buyer, user, decision maker, and budget source are explicit or marked unknown. |
| Value trace | Every offer maps to a named customer pain and alternative. |
| Market evidence | Market/competitor/pricing numbers have inspected sources or `ASSUMPTION:` labels. |
| Money coherence | Revenue model can be expressed as price × volume × frequency or another explicit formula. |
| Operating feasibility | Delivery process, required team, suppliers, and technology are named for the first phase. |
| Actionability | First 3-6 months include testable assumptions, metrics, and kill criteria. |

## Output contract

For a durable artifact, write markdown with:

```md
# Core Business Brief: <business>

## 1-page kernel
...

## Core document
### 0. One-page kernel / executive summary
...
### 12. Appendices / evidence ledger
...

## Financial-model input ledger
| Variable | Base | Bear | Bull | Source/assumption | Validation task |
|---|---:|---:|---:|---|---|

## First 3-6 months
| Month | Action | Assumption tested | Metric | Pass/kill criterion |
|---|---|---|---|---|

## Source and assumption ledger
...
```

## Completion criterion

The core brief is complete only when it can seed a financial model and a business plan without reinterpreting the business: the customer, offer, money logic, operations, assumptions, metrics, first actions, and kill criteria are explicit and internally consistent.
