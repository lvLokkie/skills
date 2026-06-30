# Matt Pocock skills reference and dependency candidates

Reference repo: <https://github.com/mattpocock/skills> (inspected at `448d0ade`).

This is a source-specific case study. The general dependency rules live in [`dependencies.md`](./dependencies.md).

## What to reuse without copying

This document is a dependency/adaptation map, not a copying backlog. The default follows [`dependencies.md`](./dependencies.md): **upstream as dependency/reference, local repo as thin integration layer**.

Local text is allowed only for:

- routing: which upstream skill to call for a local workflow;
- configuration: Ivan/Hermes paths, issue tracker, Telegram/Kanban/GitLab/GitHub conventions;
- deltas: explicit ways our workflow intentionally differs from upstream;
- compatibility notes: what cannot be consumed directly by the target agent.

Do not port full upstream procedures into this repo just because they overlap with our skills.

## Reusable upstream principles

- **Small composable skills, not giant process frameworks.** User-invoked skills orchestrate; model-invoked skills hold reusable discipline.
- **Invocation taxonomy.** Every promoted skill is explicitly model-invoked or user-invoked, and READMEs group them that way.
- **Progressive disclosure.** `SKILL.md` keeps the execution path; heavier examples, glossaries, and branch-specific detail move to sibling reference files.
- **Context-load budgeting.** A model-invoked description costs tokens every run; promote only skills that need autonomous reach.
- **Domain language and ADRs.** Code-work skills read/update `CONTEXT.md` and `docs/adr/` when terminology or irreversible decisions matter.
- **Setup pointers only for hard dependencies.** Mention setup explicitly only when a skill cannot produce correct output without config; soft dependencies degrade gracefully.
- **Catalog integrity.** Top-level README, bucket README, and plugin manifest agree on the promoted skill set.

## Our inherited/adapted surface

| Local surface | Upstream source | Status | Action |
|---|---|---|---|
| `~/.hermes/skills/software-development/improve-codebase-architecture` | `skills/engineering/improve-codebase-architecture` | Directly inherited/adapted in active Hermes skills | Keep as a local Hermes skill; do not duplicate into this marketplace unless packaging Hermes skills here becomes a goal. |
| `~/.hermes/skills/software-development/domain-grill-with-docs` | `skills/engineering/grill-with-docs` + domain modeling ideas | Adapted for Ivan/Hermes repo conventions | Keep local adaptation; dependency would be conceptual, not a direct install. |
| `plugins/personal-skills/skills/created-skill-audit` | Overlaps with `writing-great-skills` pruning/no-op discipline | Local derivative idea, not a copied upstream skill | Keep as our own marketplace skill; use upstream as reference for vocabulary and invocation model. |

## Potential dependencies from `mattpocock/skills`

| Priority | Upstream skill(s) | Dependency mode | Why we want it | Local handling |
|---|---|---|---|---|
| P0 | `writing-great-skills` | Dependency/reference first; local thin audit wrapper only | Best framework for skill quality: predictability, context load, progressive disclosure, no-op pruning, leading words. | Keep `created-skill-audit` as a local wrapper for Ivan publish gates; do not copy upstream reference content. |
| P0 | `grilling`, `grill-me`, `grill-with-docs` | Dependency/reference plus local router/delta notes | One-question-at-a-time alignment loop; recommended answer with each question; docs/code lookup before asking. | Local skills should point to the upstream flow and add only Ivan docs taxonomy/delivery deltas. |
| P0 | `tdd` | Dependency/reference; local project-specific test commands only | Red-green-refactor, public-interface tests, vertical slices, don't mock internals by default. | Do not reimplement the full TDD skill; add local setup/validation deltas where needed. |
| P0 | `diagnosing-bugs` | Dependency/reference; local deterministic loop hooks only | Deterministic reproduce → minimise → hypothesise → instrument → fix → regression-test loop. | Do not copy the loop; add local Hermes debugging entry points and cleanup conventions. |
| P1 | `codebase-design`, `domain-modeling`, `improve-codebase-architecture` | Prefer direct upstream dependency for Claude; keep Hermes inherited skill only where Hermes cannot consume dependency | Strong shared language: deep modules, seams, adapters, locality, leverage, deletion test, CONTEXT/ADR discipline. | Avoid maintaining a forked text copy in this marketplace. |
| P1 | `prototype` | Dependency/reference; local run/delete policy only | One-question prototype; split logic/state prototypes from UI prototypes; delete-or-absorb after verdict. | Local skill should only specify Ivan repo hygiene and validation. |
| P1 | `handoff` | Depend where available; local Hermes handoff remains platform adapter | Compact artifact for another agent/session, useful for Telegram/cron/kanban handoffs. | Do not duplicate in marketplace unless a platform cannot use the dependency. |
| P2 | `to-prd`, `to-issues`, `triage`, `implement` | Adapt selectively | Issue/PRD state machine and vertical issue slicing are useful, but upstream assumes its setup skill and tracker mappings. | Only import after local issue-tracker convention is stable. |
| P3 | `setup-pre-commit`, `git-guardrails-claude-code`, `scaffold-exercises`, `migrate-to-shoehorn` | Usually skip/direct install only when needed | Tool/course-specific or Claude-specific. | Do not add as default dependencies. |

## Not recommended as dependencies

- `personal/*` — tied to Matt's own setup.
- `in-progress/*` — drafts, not promoted upstream.
- `deprecated/*` — upstream has replaced or retired them.

## Proposed dependency policy

1. Keep this repo as a **universal personal marketplace**, not a mirror of Matt's repo.
2. For overlaps, prefer **direct upstream dependency/reference + local adapter**, not a forked local copy.
3. Local wrappers may add routing, config, and deltas, but must not restate the full upstream procedure.
4. Only fork/adapt text when the target agent cannot consume the upstream skill and the workflow is important enough to own maintenance.
5. If direct marketplace dependencies are added later, first pass the direct-plugin-dependency gate in [`dependencies.md`](./dependencies.md), pin them semantically in `plugin.json dependencies`, and keep this file as the Matt-specific rationale.
