---
name: financial-model-spec
description: "Prepare a financial-model specification and assumptions ledger for a new business, business plan, investor memo, bank proposal, or operating plan. Use when the user needs revenue logic, unit economics, startup costs, burn, break-even, scenarios, or spreadsheet inputs before or alongside a business document."
---

# Financial model specification

This skill produces the document that tells a spreadsheet what to calculate. It is not a substitute for accounting, but it prevents vague business plans from inventing disconnected numbers.

Use UNIDO's financial-analysis / investment-appraisal frame as the default: cost estimates, basic accounting statements, financing plan, appraisal metrics, ratios, and uncertainty/sensitivity analysis.

## When to use

Use when the user asks for:

- financial model assumptions, unit economics, revenue model, startup costs, burn rate, runway, break-even, or scenario planning;
- spreadsheet structure for a business plan, investor plan, bank plan, grant budget, or internal operating plan;
- a sanity check on business-plan numbers before writing the final narrative.

Run `core-business-brief` first if the customer, offer, pricing logic, or operating model is not yet defined.

## Workflow

1. **Extract money rules.** From the core brief or notes, identify revenue streams, pricing units, payment timing, COGS, fixed costs, working capital, and one-off startup costs.
2. **Classify every input.** Mark each as `provided`, `source-backed`, `benchmark`, `ASSUMPTION:`, or `missing`.
3. **Build the UNIDO-style model map.** Define tabs/sections: assumptions, investment/capex, revenue/marketing, key inputs/COGS, overhead, human resources, implementation budget, working capital, financing, cash flow/P&L/balance sheet, appraisal metrics, ratios, scenarios, dashboard.
4. **Write formulas in words and symbols.** Every derived metric must have a formula, period, and units.
5. **Create scenarios and sensitivity checks.** At minimum: bear, base, bull; for investment-grade plans also test price, volume/capacity utilization, input costs, CAC, capex, and payment timing.
6. **Run sanity calculations.** Use tools for arithmetic and show the exact checks for totals, margins, runway, break-even, payback/NPV/IRR when applicable, ratios, and funding use.
7. **Surface validation tasks.** List which assumptions need customer interviews, quote requests, supplier checks, ad tests, or internal confirmation.

## Required model blocks

| Block | Must contain |
|---|---|
| Revenue / marketing | customer count or production volume, acquisition funnel, conversion, price, frequency, churn/retention, capacity utilization, expansion if relevant |
| Key inputs / COGS | raw materials or digital inputs, supplier/API/data costs, delivery/labor, payment fees, refunds/bad debt if relevant |
| Overhead and human resources | salaries, contractors, training, rent, software, infra, marketing, legal, admin, governance overhead |
| Startup investment / capex | incorporation, equipment, inventory, setup, deposits, licenses, launch spend, technology build, implementation budget |
| Working capital and financing | cash-in timing, payment terms, inventory/receivables/payables, equity/debt/grants/member contributions, funding use |
| Unit economics and ratios | gross margin, contribution margin, CAC, payback, LTV or repeat-purchase proxy, debt service coverage if relevant |
| Investment appraisal | break-even, runway, funding need, sensitivity/uncertainty, plus payback/NPV/IRR when upfront investment or financing choice is material |
| Dashboard | 5-10 decision metrics that show whether the business is working |

## Formula defaults

Use or adapt these formulas; never hide math in prose:

```text
Revenue = active_customers × average_order_value × purchase_frequency
Subscription revenue = paying_accounts × ARPA
Marketplace revenue = GMV × take_rate
Gross profit = revenue - variable_costs
Gross margin = gross_profit / revenue
Contribution margin = revenue - variable_costs - direct_sales_or_delivery_costs
CAC = acquisition_spend / new_customers
Payback_months = CAC / monthly_gross_profit_per_customer
Runway_months = cash_balance / net_monthly_burn
Break_even_month = first month where revenue >= total_costs and cumulative cash remains non-negative
Funding_need = cumulative_cash_deficit + safety_buffer
```

## Quality gates

| Gate | Pass condition |
|---|---|
| Single source of money truth | Pricing, take rate, cost drivers, and funding use are defined once and referenced downstream. |
| Bottom-up revenue | Revenue is driven by customers/volume/conversion/pricing, not only by market-share aspiration. |
| Scenario integrity | Bear/base/bull change named drivers; no hard-coded desired outcomes. |
| Cash timing | Revenue recognition and cash-in/cash-out timing are not silently treated as identical when payment terms matter. |
| Arithmetic verified | Derived totals and ratios were recalculated with a tool. |
| Assumptions visible | Every uncertain input has validation owner/task and confidence. |

## Output contract

```md
# Financial Model Specification: <business>

## Model purpose and decision
...

## Workbook / sheet map
| Sheet | Purpose | Key outputs |
|---|---|---|

## Assumptions ledger
| Driver | Unit | Bear | Base | Bull | Source/type | Confidence | Validation task |
|---|---:|---:|---:|---:|---|---|---|

## Formula library
| Metric | Formula | Notes |
|---|---|---|

## Scenario / investment appraisal summary
| Scenario | Revenue | Gross margin | Net burn/cash flow | Break-even | Payback/NPV/IRR if applicable | Runway | Funding need |
|---|---:|---:|---:|---|---|---:|---:|

## Sanity checks run
- <calculation/check/output>

## Open decisions before spreadsheet build
...
```

## Completion criterion

The spec is complete when another agent or human can build the spreadsheet without inventing hidden assumptions, and when the business plan can reference the model's variables, scenarios, and checks without redefining them.
