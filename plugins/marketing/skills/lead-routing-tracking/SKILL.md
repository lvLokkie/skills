---
name: lv:lead-routing-tracking
description: "Lead routing and marketing attribution: use when auditing, designing, or smoke-testing landing-page lead forms, UTM/referrer payloads, n8n lead routing, Telegram/MAX delivery, webhook fallback, honeypot handling, Metrika/Clarity goals, or campaign-to-lead attribution for marketing funnels."
---

# Lead routing and tracking

Use this skill for the operational link between paid traffic and real leads: landing form payloads, attribution fields, webhook routing, messenger delivery, analytics goals, and smoke tests.

Reference sources imported from local projects:

```text
/Users/admin/repos/lvLokkie/territory-accounting-landing/docs/lead-payload.md
/Users/admin/repos/lvLokkie/territory-accounting-landing/docs/integrations/n8n-lead-routing.md
/Users/admin/repos/lvLokkie/territory-accounting-landing/src/components/CtaSection.astro
/Users/admin/repos/lvLokkie/territory-accounting-landing/src/layouts/BaseLayout.astro
/Users/admin/repos/lvLokkie/n8n-workflows/README.md
```

Treat these as project-specific references. Do not copy production webhook URLs, chat IDs, tokens, credential names with values, or account-private details into reports.

## Safety contract

1. **No secrets in chat or repo.** Redact API keys, bot tokens, webhook suffixes, chat/user IDs, cookies, auth files, and credential values as `[REDACTED]`.
2. **Webhook URLs are spam surface.** Even if a frontend webhook is public by design, report it as `https://<n8n-domain>/webhook/<project>/leads/<random-suffix>` unless Ivan explicitly asks to inspect the live value.
3. **Do not claim production delivery without read-back.** Verify n8n workflow active state, webhook registration, delivery logs, or actual smoke-test response before saying lead routing works.
4. **Respect consent and honeypot.** A valid lead requires consent and bot/spam filtering; invalid/spam paths should not notify managers.

## Preflight

1. Identify project, landing domain, form component, and environment variable that carries the webhook URL.
2. Identify routing target: Telegram bot, Telegram user bridge, MAX bot, CRM/table, or local-only test.
3. Identify attribution fields required by the campaign report: source, page, referrer, UTM source/medium/campaign/content/term, client time/timezone, and calculator/service context.
4. Identify mode:
   - **docs-only audit** — inspect repository files, no live calls;
   - **local smoke** — run local form/build tests only;
   - **live read-only** — inspect n8n/workflow/logs;
   - **live write/smoke** — send bounded test lead after approval.

## Payload contract

Minimum valid lead:

```text
name: non-empty string
contact: non-empty string
consentToPersonalData: true
source/page/submittedAt: preferred, fill server-side if missing
```

Attribution fields to preserve when present:

```text
referrer
utmSource
utmMedium
utmCampaign
utmContent
utmTerm
clientTimezone
clientTime
calculatorSummary
```

For static landing → n8n cross-origin flows, preserve the simple-request workaround from the source project: send `JSON.stringify(payload)` without `Content-Type: application/json` when avoiding browser CORS preflight is required. If strict JSON is needed, put a same-origin proxy or a backend that handles `OPTIONS` in front of n8n.

## Operating loop

1. **Inspect source files.** Read the form component, layout/analytics wrapper, payload docs, and routing runbook.
2. **Map the funnel.** Traffic source → landing page → form event → webhook → normalization → delivery/persistence → analytics goal.
3. **Check attribution integrity.** Verify UTM/referrer/source/page/client-time fields survive from browser to notification/persistence.
4. **Check spam and consent gates.** Honeypot, required fields, consent, invalid lead response, and no-notify behavior.
5. **Check delivery.** For n8n, verify workflow active state, webhook path, credentials/env names, retries/timeouts, and target delivery constraints.
6. **Check analytics.** Verify form start, submit, fallback-open, and lead-submit goals are named consistently with campaign reports.
7. **Smoke test only when bounded.** Use sanitized test lead data and mark it as test; read back response/logs.

## Stop conditions

Stop and report a blocker instead of pretending success when:

- production workflow is inactive or webhook is not registered;
- credentials/env vars are missing;
- target messenger cannot receive messages from the bot/user bridge;
- CORS/preflight blocks the browser request;
- smoke test would send real PII or spam a production recipient without approval.

## Output

```md
## Lead routing/tracking: <project>

- Mode: docs-only | local smoke | live read-only | live smoke
- Funnel: <traffic → landing → webhook → delivery/persistence → analytics>
- Attribution fields: pass | partial | missing
- Consent/spam gates: pass | partial | missing
- Delivery: pass | partial | blocked | not verified
- Analytics goals: pass | partial | missing | not verified

### Findings
| Area | Evidence | Action | Risk |
|---|---|---|---|

### Verification
- <files/tools/smoke tests inspected>
- Secrets: none observed | redacted | blocked
```
