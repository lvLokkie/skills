---
name: lv:make-me-rich
description: Plan a task on the expensive model while a bounded swarm of cheaper sub-agents does read-only analysis; outputs an executable plan for cheaper executors.
disable-model-invocation: true
argument-hint: "The task to plan"
---

# Make Me Rich

You are the **planner** tier. Produce a plan artifact for the given task and stop; never execute the plan. Bulk fact-gathering is delegated to a bounded **swarm** of cheaper analysts so expensive tokens are spent only on decomposition, synthesis, and plan writing.

## Tiers

- **planner** — the model running this session, assumed the most capable available. It does intake, decomposition, synthesis, and plan writing.
- **economy** — sub-agent models materially cheaper than the planner. They do read-only analysis against briefs; for each analyst, pick the cheapest model adequate for its question.
- **standard** — mid-capability models. Used only as a plan-step executor annotation; do not use this tier during analysis unless a question demands it.

## Preflight

1. Confirm the runtime can spawn parallel sub-agents with a per-agent model override.
2. If it cannot, go to **Fallback** before doing anything else.
3. If the session model is itself economy-class, tell the user the planner tier equals the session model and the economics collapse; continue only on explicit user approval.

## Phases

1. **Intake.** Restate the task: goal, boundaries, and what a done plan must answer. Ask at most one clarification round.
   - Done when: a one-paragraph task statement has been shown to the user.
2. **Manifest.** Decompose the task into questions about current state. For each analyst, state the question, economy model, and expected return. Default to 6 or fewer analysts; hard cap 10 per invocation, across all waves. State the plan destination, defaulting to `docs/plans/YYYY-MM-DD-<slug>-plan.md` in the target project.
   - Done when: the manifest has been shown and the user has explicitly approved it. Spawn nothing before approval.
3. **Swarm.** Spawn the approved analysts in parallel, each with a self-contained brief. Use one wave. A second wave is allowed once, only for gaps named after reading wave-one summaries and only within the remaining cap.
   - Done when: every manifest question has a summary or a named gap.
4. **Synthesis.** Build the target design and plan exclusively from analyst summaries. Read raw files yourself only point-wise to resolve contradictions between summaries.
   - Done when: every plan step traces to a summary or a point check.
5. **Plan artifact.** Write the plan following [plan-format.md](plan-format.md). Report the absolute plan path, analyst count per tier, and gaps left open.
   - Done when: the file exists at the reported path.

## Analyst brief

Every spawned analyst receives:

- Self-contained context: exact paths, one concrete question, and explicit boundaries for what not to explore.
- Read-only rule: no edits and no side-effecting calls.
- Response contract: facts plus evidence paths, 40 lines maximum, never raw file dumps.
- No recursion: the analyst must not spawn sub-agents.

## Runtime mapping

- Claude Code: use the Agent tool with the `model` parameter; use `haiku` for mechanical collection and `sonnet` for semantic analysis.
- Other runtimes: use their sub-agent facility with a per-agent model override; if none exists, **Fallback** applies.

## Fallback and stop

- No sub-agents or no model override: offer the user a choice between degraded mode (sequential analysis in this session, no savings) and stopping.
- Cap exhausted with gaps remaining: stop and return the gaps to the user.
- Summaries still contradict each other after a point-wise recheck: stop and return the contradiction to the user.
