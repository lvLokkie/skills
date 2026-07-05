---
name: lv:report-writing
description: "Report writing: turn evidence, tool output, or research into a decision-ready report. Use when the user asks for a report/отчёт, brief, decision memo, status update, incident/debug report, audit/review, market or competitor analysis writeup, or a durable markdown deliverable with sources and next actions."
---

# Report writing

A report is a decision artifact, not a polished summary. It should answer what happened or what to do, show the evidence, label uncertainty, and end with next actions.

Use this skill to shape evidence into a report. It does not replace research, debugging, or execution skills: if evidence is missing, gather or verify it first.

## When to use

Use when the user asks for:

- a report, отчёт, brief, memo, writeup, review, audit, or status update;
- a durable markdown artifact with sources, command output, findings, and next actions;
- a research, market, competitor, incident, debug, experiment, or decision summary that must be traceable;
- a Telegram-ready executive summary backed by a fuller artifact.

Do not use for quick conversational answers, raw transcripts, handoffs, or prose polishing unless the user wants a report-shaped deliverable.

## Classification step

Before writing, classify the report:

- **Audience:** Ivan, work stakeholders, public readers, another agent, or a technical maintainer.
- **Decision:** what the report should help decide or do.
- **Type:** research/market, decision memo, status/update, incident/debug, audit/review, experiment/spike, or executive brief.
- **Freshness:** current facts required vs evergreen synthesis.
- **Evidence:** source-backed, tool-output-backed, self-report, or hypothesis.
- **Artifact:** chat summary, markdown file, spreadsheet, deck outline, ticket comment, or repo doc.

Completion criterion: the report type, audience, decision, evidence level, and artifact target are explicit. If one missing field changes the evidence path, ask one focused question; otherwise proceed with stated assumptions.

## Default structure

Use this order unless the report type needs a stricter template:

1. **Verdict.** 1–5 bullets with the answer and why it matters.
2. **Scope and method.** What was checked, what was not checked, time/date, sources/tools used.
3. **Key findings.** Group by decision-relevant themes. Each factual bullet has a source, file path, command output, or confidence label.
4. **Evidence ledger.** Use source IDs for research reports and command/file references for operational reports.
5. **Implications.** What the findings mean for the user's goal.
6. **Options or recommendation.** Compare realistic paths; do not invent perfect options.
7. **Risks, contradictions, and unknowns.** Keep blockers visible; do not average conflicting evidence away.
8. **Next actions.** Ordered, concrete, owner-aware steps.
9. **Appendix.** Raw data, long tables, commands, calculations, and links that would clutter the main brief.

Completion criterion: the verdict answers the decision, every finding is traceable or labeled, and next actions are concrete.

## Evidence rules

- Inspect sources or files before citing them; do not cite search snippets or memory as evidence.
- Use source IDs like `[S1]` for research reports and path/command handles for repo or ops reports.
- Label confidence per material finding: High, Medium, Low, or Unverified.
- High-impact claims need a primary source or independent corroboration.
- Numbers, percentages, dates, sizes, and financial calculations must be tool-checked.
- If a claim is plausible but unsupported, write `hypothesis` or `source not found`.
- Preserve source dates, access dates, jurisdiction, version, and scope when they affect the conclusion.

## Report adapters

| Type | Must include | Stop condition |
|---|---|---|
| Research / market | Source ledger, confidence labels, contradictions, recommendation. | Do not present vendor marketing as neutral fact without labeling it. |
| Decision memo | Options, tradeoffs, decision rule, recommendation, reversible vs irreversible choices. | Do not recommend if the decisive unknown is still untested and testable. |
| Status report | Done, in progress, blocked, evidence, next owner/action. | Do not report completion without verification or artifact handles. |
| Incident/debug | Impact, timeline, root-cause status, evidence, fix, prevention, open risks. | Do not claim root cause when only symptoms were observed. |
| Audit/review | Scope, checks run, findings by severity, remediation, validation. | Do not expand scope silently; list excluded areas. |
| Experiment/spike | Hypothesis, setup, commands/data, result, verdict, next experiment. | Do not declare feasibility when the key path was not exercised. |

## Style rules

- Default to Russian for Ivan/personal contexts; use English for work artifacts, public English docs, PR/MR text, and code-adjacent deliverables unless asked otherwise.
- Put the most important point first in the document and each section.
- Use plain language, short paragraphs, skimmable headings, tables for comparisons/ledgers, and bullets for decisions/next actions.
- Keep raw dumps out of the main report. Link or append them.

## Final verification

Before finalizing:

- [ ] The verdict answers the user's decision.
- [ ] Every material factual claim has a source, path, command output, or confidence label.
- [ ] Calculations were tool-checked.
- [ ] Unknowns and contradictions are visible.
- [ ] Artifact paths/URLs exist or are labeled as proposed.
- [ ] Secret-like values are absent or redacted.
- [ ] The final response tells the user where the report is and what to do next.

## Output contract

For chat-only reports, return a compact executive summary plus key evidence and next actions.

For durable reports, write a markdown artifact, verify it exists, and return:

```md
## Вывод
- <verdict>

## Артефакт
- `<absolute-or-repo-relative-path>`

## Проверка
- <commands/sources checked>

## Дальше
- <next action>
```

## Completion criterion

The report is complete only when the conclusion is first, evidence is traceable, uncertainty is labeled, calculations are verified, secret leakage is checked, and the next action is explicit.
