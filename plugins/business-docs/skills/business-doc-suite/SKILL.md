---
name: lv:business-doc-suite
description: "Choose, sequence, and assemble the right business documents for a new venture, pivot, investment, grant, partner, or internal planning request. Use when the user asks for a business-document package, business blueprint/docs, startup docs, venture docs, business-plan set, or asks which business document to create first."
---

# Business docs suite

Use this skill to prevent document theater: choose the smallest coherent set of business documents that helps a real decision, then route each document to its owning skill.

Use UNIDO as the default baseline: lightweight early drafts follow UNIDO's business-plan guide; investment-grade plans follow UNIDO's industrial feasibility-study sequence adapted to the business type.

## When to use

Use when the user asks to:

- create a business-doc package for a new company, product line, or pivot;
- turn raw notes into venture documents, startup documents, a business blueprint, or a business plan set;
- decide whether they need a core brief, business plan, financial model, GTM memo, investor memo, or partner proposal;
- reconcile several business docs that disagree with each other.

Do not use for generic reports, product PRDs, marketing campaign operations, or pure financial calculations outside a business-doc context.

## Routing map

| Need | Primary document | Owning skill | Completion test |
|---|---|---|---|
| Define what the business is and why it can work | Core business brief / venture foundation memo | `core-business-brief` | 1-page kernel, 5-10 page memo, and assumptions ledger exist and agree. |
| Turn validated materials into an external-facing plan | Business plan / investor or partner plan | `business-plan-writing` | Audience-specific plan has sources, financial consistency, risks, and next actions. |
| Prepare assumptions for a spreadsheet model | Financial model specification | `financial-model-spec` | Assumptions, formulas, scenario inputs, and validation checks are single-sourced. |
| Review a finished business doc | Decision-ready critique | `business-plan-writing` plus `report-writing` if the output is a review report | Findings have severity, evidence, and concrete fixes. |

## Workflow

1. **Classify the decision.** Identify audience, decision, stage, geography, deadline, and required artifact format.
2. **Inventory inputs.** Read provided notes, links, spreadsheets, decks, or repo docs. Mark each key field as `provided`, `source-backed`, `assumption`, or `missing`.
3. **Choose the minimal UNIDO-based package.** Default sequence:
   - concept or early idea: `core-business-brief` first;
   - fundraising / bank / partner / grant: `core-business-brief` → `business-plan-writing`;
   - any revenue/cost/scenario question: `financial-model-spec` before the final plan;
   - existing conflicting docs: reconcile the core brief before writing downstream docs.
4. **Keep one source of truth.** Business identity, market/marketing concept, implementation budget, and money rules live in the core brief or financial model spec; downstream docs reference them instead of redefining them.
5. **Gate research and numbers.** Market, competitor, pricing, growth, CAC, LTV, runway, and break-even claims need inspected sources or explicit `ASSUMPTION:` labels. Use tools for arithmetic.
6. **Deliver in layers.** For large packages, return a short Telegram summary plus artifact paths. Keep raw notes, assumptions, and source ledger separate from polished narrative.

## Stop conditions

- If the user needs a legal, tax, regulated-finance, or licensing conclusion, label it as non-legal research and require primary-source verification before acting.
- Do not produce investor-ready claims from unverified numbers. Mark them as assumptions and surface the validation task.
- Do not ask for every missing detail up front. Ask only for decision-critical gaps that cannot be researched or safely assumed.

## Output contract

Return:

```md
## Документы
| Artifact | Status | Owner skill | Path/next action |
|---|---|---|---|

## Основные допущения
- `ASSUMPTION:` ...

## Проверки
- Sources inspected / calculations run / unresolved gaps.

## Следующий шаг
- One concrete action.
```

## Completion criterion

The suite is complete when the document set is minimal, ordered, internally consistent, and every downstream artifact traces its business identity, money rules, assumptions, and sources back to the owning document.
