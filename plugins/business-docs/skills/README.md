# Business Docs Skills

Promoted skills shipped by the `business-docs` plugin. Keep this list in sync with `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, the top-level README, and the business-docs GitHub candidate analysis.

## Category contract

Use this category for UNIDO-based document formation around new ventures, business models, financial assumptions, business plans, investor/partner/bank/grant plans, and internal founding memos. Keep live company credentials, private financial data, and non-public customer lists in the project workspace or runtime inputs, not in marketplace skill bodies.

## Skill routing

| Task | Use | Default mode |
|---|---|---|
| Decide which business documents are needed and in what order | [business-doc-suite](./business-doc-suite/SKILL.md) | Minimal coherent package; avoid document theater. |
| Define the business logic that feeds plans, decks, and financial models | [core-business-brief](./core-business-brief/SKILL.md) | UNIDO-adapted 1-page kernel + 5-10 page core memo + assumptions ledger. |
| Write or audit a business plan, investor/bank/partner plan, grant plan, or investment memo | [business-plan-writing](./business-plan-writing/SKILL.md) | Audience-specific plan with sources, financial checks, risks, and next action. |
| Prepare financial model assumptions, formulas, scenarios, and sanity checks | [financial-model-spec](./financial-model-spec/SKILL.md) | Spreadsheet-ready spec; all uncertain inputs labeled and validated. |

## Model-invoked

- **[business-doc-suite](./business-doc-suite/SKILL.md)** — Choose, sequence, and assemble the right business-document package for a venture, pivot, investment, grant, partner, or internal planning request.
- **[core-business-brief](./core-business-brief/SKILL.md)** — Create the core business document: essence, customer, value, market, product, revenue model, GTM, operations, financial frame, risks, assumptions, and first 3-6 months.
- **[business-plan-writing](./business-plan-writing/SKILL.md)** — Write, rewrite, or audit audience-specific business plans and investment/partner/bank/grant memos from source materials and assumptions.
- **[financial-model-spec](./financial-model-spec/SKILL.md)** — Produce a spreadsheet-ready financial model specification with assumptions, formulas, scenarios, validation tasks, and arithmetic checks.

## User-invoked

None yet.

## Category verification

Before shipping changes to this category:

1. Check that each promoted skill is listed in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, this README, and the top-level README.
2. Confirm no real private financial data, customer names, credentials, or company-private figures were added to the skill bodies.
3. Run `python3 scripts/validate.py`, `git diff --check`, parse changed JSON, run `claude plugin validate plugins/business-docs` when Claude CLI is available, smoke-test Codex marketplace registration when Codex CLI is available, and apply the `/skill-management:skill-audit` security gate.
