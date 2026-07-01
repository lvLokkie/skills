---
name: lidfly-mcp
description: "LidFly MCP marketing access: use when setting up, checking, or operating LidFly MCP for advertising platforms, Yandex Direct/Metrika, VK Ads, Avito Ads, LidFly landing/report tools, Workspace memory, or marketing campaign analysis. Enforces credential redaction, read-before-write, account/scope confirmation, and safe MCP fallback behavior."
---

# LidFly MCP

Use this skill when Ivan asks to connect, check, or use **LidFly MCP** for marketing work: Yandex Direct/Metrika, VK Ads, Avito Ads, LidFly landing/report tools, or Workspace project memory.

Public documentation observed during import:

- Quickstart: `https://lidfly.ru/docs/quickstart`
- Docs index: `https://lidfly.ru/docs/`
- Recommended endpoint for new connections: `https://lidfly.ru/mcp/v3`
- Legacy endpoints mentioned by LidFly docs: `/mcp`, `/mcp/vk`, `/mcp/lidfly`, `/mcp/workspace`

## Safety contract

1. **Never print or commit API keys, OAuth tokens, client secrets, cookies, or account auth files.** If a value is found, report `[REDACTED]` only.
2. **Read before write.** For campaign, budget, creative, keyword, or audience changes, first inspect the account/campaign/scope and summarize the exact intended mutation.
3. **Confirm scope.** Identify platform, account/cabinet, campaign, date range, objective, and timezone before analysis or mutation.
4. **Separate read-only and write branches.** Reporting, audit, and diagnostics may proceed read-only; budget/creative/keyword/status mutations require explicit user approval unless Ivan has already given a concrete bounded command.
5. **No invented side effects.** After any write, read back the changed object and report the stable ID/status returned by the tool.

## Preflight

Before using LidFly MCP:

1. Check whether a LidFly MCP server named `lidfly` is configured and at least one expected tool is discovered. Hermes-style tools should appear with the `mcp_lidfly_*` prefix.
2. Prefer the category plugin's optional `plugins/marketing/.mcp.json` remote HTTP config when the runtime supports project/plugin MCP manifests. It uses `https://lidfly.ru/mcp/v3` with `Authorization: Bearer ${LIDFLY_API_KEY}`; the real value must live in the runtime env/secret store.
3. If unavailable, give the setup path without asking for secrets in chat:
   - create/login to LidFly account;
   - copy API key from the LidFly account UI;
   - configure MCP endpoint `https://lidfly.ru/mcp/v3` in the target client or install the plugin MCP manifest;
   - store the API key in the client/runtime secret store, not in this repo.
4. If platform calls fail with auth errors, ask Ivan to verify the LidFly account connection/OAuth in LidFly UI; do not request the token value.

## Operating loop

1. Classify the task:
   - setup / health check;
   - account or campaign inventory;
   - performance report;
   - search-query / keyword / negative-keyword optimization;
   - creative or landing-page review;
   - budget/bid/status change;
   - export/snapshot into Workspace.
2. Gather source context: target platform, account, campaign IDs/names, date range, metrics, goals, and current constraints.
3. Run read-only inspection first and record what was actually returned by the MCP tool.
4. For changes, prepare a patch plan with object IDs and before/after values.
5. Apply only the approved/bounded change.
6. Read back changed objects and produce a short report with IDs, metrics, confidence, and next action.

## Fallback

If LidFly MCP is unavailable:

- for known local projects, use checked-in docs such as `docs/yandex-direct.md` as offline context;
- produce an offline plan or audit only;
- label recommendations as **not applied**;
- do not claim live campaign state or successful changes without MCP/tool read-back.

## Output

```md
## LidFly MCP: <task>

- Platform/account: <confirmed or missing>
- Mode: setup | read-only | write-planned | write-applied | offline fallback
- Scope: <campaign/account/date range>
- Findings: <tool-backed bullets>
- Proposed/applied changes: <IDs and before/after values>
- Verification: <read-back command/tool result or fallback note>
- Secrets: none observed | findings redacted | blocked
```
