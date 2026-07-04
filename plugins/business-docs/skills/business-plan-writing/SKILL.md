---
name: business-plan-writing
description: "Write, rewrite, or audit a business plan, investor plan, bank/partner proposal, grant/startup-program plan, or investment memorandum from a core business brief, notes, deck, research, or financial assumptions. Use when the user wants a polished decision document, not just the underlying business logic."
---

# Business plan writing

Use this skill to turn a defined business into a decision-ready plan for a specific audience. The plan must be persuasive because it is concrete and evidenced, not because it uses hype.

Default to the UNIDO baseline in `../core-business-brief/references/unido-standard.md`: simplified business-plan sequence for lightweight drafts, and industrial-feasibility-study sequence for investment-grade plans.

## When to use

Use for:

- business plans, investor plans, bank plans, partner proposals, grant/startup-program forms, investment memos;
- turning a pitch deck or core business brief into a narrative plan;
- rewriting a business plan for a different audience;
- auditing a business plan for gaps, contradictions, unsupported claims, or weak financial logic.

If the business itself is still undefined, run `core-business-brief` first. If spreadsheet assumptions are the main blocker, run `financial-model-spec` first.

## Audience modes

| Audience | Emphasize | Avoid |
|---|---|---|
| Founder/internal | sequencing, assumptions, metrics, operating decisions | decorative market theater |
| Investor | market wedge, growth logic, unit economics, team, milestones, funding use | unsupported TAM optimism |
| Bank/lender | cash-flow reliability, collateral/repayment, downside controls | venture-style hockey-stick claims |
| Partner | mutual value, operational fit, delivery responsibilities, risk sharing | over-broad company narrative |
| Grant/startup program | eligibility, social/economic impact, feasibility, budget, milestones | generic pitch language |

## Workflow

1. **Classify audience and decision.** Name the reader, what they must decide, and the required format/depth.
2. **Audit inputs.** Build an information map for each section: `sufficient`, `partial`, `missing`, `needs verification`, `contradiction`.
3. **Research public gaps before interviewing.** Market, competitors, regulation, benchmarks, and pricing should be researched when public data exists. Ask the user only for internal facts and strategic choices.
4. **Build the narrative plan.** State the core story in UNIDO order: background/basic idea → market/marketing concept → inputs/capacity/operations → organization/resources → implementation/budget → financial appraisal → risks/appendices.
5. **Draft the plan.** Use the UNIDO-adapted structure, compressing or expanding sections by audience mode.
6. **Verify numbers and consistency.** Recalculate derived metrics with tools. Cross-check repeated revenue, cost, market, team, timeline, and funding numbers.
7. **Neutrality pass.** Replace hype with evidence. Include counterevidence, risks, and conditions for success.
8. **Deliver with an evidence ledger.** Cite sources, file paths, and assumptions separately from the polished plan.

## Default UNIDO-adapted structure

0. Executive summary.
1. Project background and basic idea.
2. Strategic vision, objectives, and decision requested.
3. Market analysis: demand, segments, customer, competition, substitutes, barriers.
4. Marketing concept: offer, product range, pricing, distribution, promotion, sales process.
5. Product/service, capacity, key inputs, suppliers, data/API/infrastructure dependencies.
6. Location/site or operating geography, environmental/social/regulatory constraints.
7. Engineering, technology, delivery process, quality controls, and operating model.
8. Organization, overhead, team, human resources, training, governance.
9. Implementation plan and provisional budget: activities, timing, owners, costs, expected results.
10. Financial analysis and investment appraisal: startup investment, opex, working capital, financing, cash flow, break-even, scenarios, and payback/NPV/IRR when upfront investment or financing choice is material.
11. Major risks, assumptions, sensitivity/counterevidence, mitigations and kill criteria.
12. Appendices / evidence ledger / source schedules.

## Writing rules

- Start with the decision, not background.
- Every numeric or market claim has an inspected source, a file/sheet reference, or an `ASSUMPTION:` label.
- Use bottom-up revenue logic where possible; top-down market sizing alone is not a plan.
- Make competitors named and comparable on concrete axes.
- Keep one money logic: pricing, unit economics, revenue, burn, break-even, and funding use must reconcile.
- Separate MVP/first phase from later phases and wishlist features.
- Use tables for comparisons, assumptions, use-of-funds, milestones, and risks.

## Audit mode

When reviewing an existing plan, produce:

| Severity | Meaning |
|---|---|
| P0 | The document should not be used until fixed: false/unsupported core claim, financial contradiction, missing customer, or regulatory blocker. |
| P1 | Weakens the decision: unclear segment, shallow competition, missing channel economics, unrealistic timeline. |
| P2 | Improves quality: style, ordering, examples, visuals, formatting. |

Each finding must include location, evidence, why it matters, and a concrete fix.

## Output contract

```md
# Business Plan: <business>

## Executive summary
...

## Plan
<sections adapted to audience>

## Assumptions and evidence ledger
| Claim/number | Type | Source or assumption | Confidence | Validation task |
|---|---|---|---|---|

## Financial consistency checks
- <formula/check/result>

## Risks and counterevidence
...

## Next action
...
```

## Completion criterion

The business plan is complete when the target reader can make the intended decision, factual claims are traceable, financial logic reconciles, risks are visible, and the requested next action is explicit.
