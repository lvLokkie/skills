# Plan format

The artifact `make-me-rich` writes. The executor follows the plan **verbatim**: execute literally, never re-analyze, and stop on any mismatch. Tier names are defined in [SKILL.md](SKILL.md).

## Header

- Goal — one paragraph.
- Target design — the "how it will be" picture the steps converge on.
- Execution rules for the executor, stated in the plan itself: follow the plan verbatim; on any mismatch, stop and report instead of improvising.

## Steps

Each step carries all five fields:

- Action with exact paths and commands.
- Expected result.
- Checkable completion criterion — the executor can tell done from not-done without judgment calls.
- Executor tier: `economy`, `standard`, or `planner`.
- Escalation rule: criterion fails or ambiguity is found → stop and return the step to the planner tier.

## Location

Default `docs/plans/YYYY-MM-DD-<slug>-plan.md` in the target project; overridable at the manifest checkpoint.
