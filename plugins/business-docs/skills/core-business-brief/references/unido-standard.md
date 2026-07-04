# UNIDO baseline for business documents

Use this as the default baseline for `business-docs` outputs unless the user asks for another standard.

## Sources inspected

| ID | Source | Use |
|---|---|---|
| U1 | UNIDO, `Annex 7 Guide to the Business Plan`, official PDF: <https://www.unido.org/sites/default/files/2008-07/Annex_7_Guide_to_the_Business_Plan_0.pdf> | Lightweight business-plan sequence. |
| U2 | UNIDO, `Manual for the Preparation of Industrial Feasibility Studies`, official PDF: <https://www.unido.org/sites/default/files/files/2021-02/manual_for_the_preparation_of_industrial_feasibility_studies.pdf> | Investment-grade feasibility-study sequence. |
| U3 | UNIDO, `GSBPC Business Plan Template (simplified)`, official DOCX: <https://www.unido.org/sites/default/files/2016-08/GSBPC_Business_Plan_Template__simplified__0.docx> | Early-startup practical prompts. |

## What UNIDO contributes

UNIDO's simplified business-plan guide treats a business plan as a road map that sets strategic vision, joint/priority activities, and expenses; it should be revisited periodically. Its sections are:

1. Introduction / purpose / goals / timeframe.
2. Strategic vision based on feasibility-study SWOT, target markets, product range, price policy, distribution, promotion, and competitiveness.
3. Priority activities and provisional plan with expected results.
4. Funding and provisional budget, including operating and promotional costs.
5. Organizational structure, key personnel, responsibilities, and organization chart where useful.
6. Major risks and assumptions.
7. Appendices with support and proof.

UNIDO's industrial feasibility-study manual uses a fuller pre-investment structure:

1. Executive summary.
2. Project background and basic idea.
3. Market analysis and marketing concept.
4. Raw materials and supplies.
5. Location, site, and environment.
6. Engineering and technology.
7. Organization and overhead costs.
8. Human resources.
9. Implementation planning and budgeting.
10. Financial analysis and investment appraisal.

UNIDO's simplified startup template adds short practical sections for business-idea summary, product/service summary, competitor analysis, target market, marketing plan, and startup costs/financials.

## Local adaptation rules

1. **Default to UNIDO order.** Use the feasibility-study sequence for serious business plans and the simplified business-plan sequence for lightweight early drafts.
2. **Translate industrial terms for digital/service businesses.**
   - Raw materials and supplies → key inputs, suppliers, data, infrastructure, licenses, inventory, cloud/API dependencies.
   - Plant capacity → service capacity, throughput, onboarding capacity, support capacity, or delivery capacity.
   - Location/site/environment → operating geography, legal/tax/regulatory location, channel/platform dependence, environmental/social constraints when relevant.
   - Engineering and technology → product architecture, delivery process, tooling, make/buy/partner decisions, implementation constraints.
3. **Separate market from marketing.** Market demand, segmentation, and competition come before the marketing/sales concept.
4. **Keep implementation and budget joined.** Every priority activity should have timing, owner, expected result, cost, and funding source.
5. **Keep financing and investment appraisal explicit.** Record startup investment, operating costs, working capital, financing sources, cash flow, break-even, uncertainty scenarios, and payback/NPV/IRR when upfront investment or financing choice is material.
6. **Appendices are proof, not decoration.** Put source extracts, quote requests, calculations, resumes, legal docs, and detailed schedules there.

## UNIDO-adapted default structure

```text
0. One-page kernel / executive summary
1. Project background and basic idea
2. Strategic vision and objectives
3. Market analysis: demand, segments, competition, barriers
4. Marketing concept: product range, pricing, distribution, promotion, sales process
5. Product/service, capacity, key inputs and suppliers
6. Location / operating geography / environmental and regulatory constraints
7. Engineering, technology and operating model
8. Organization, overhead, team and human resources
9. Implementation plan and provisional budget
10. Financial analysis and investment appraisal
11. Major risks, assumptions, sensitivity checks and kill criteria
12. Appendices / evidence ledger
```
