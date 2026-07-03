# GitHub candidate synthesis for marketing skills

Inspected in July 2026 to improve the local `marketing` skill pack without vendoring third-party code or generated catalogs.

## Decision table

| Candidate | License signal | Useful invariant | Local strategy |
|---|---:|---|---|
| `nebelov/yandex-direct-for-all` | MIT | Yandex performance work should be file-first: product map → masks → saved Wordstat wave/raw bundle → analysis; exhaust pagination before conclusions. | Reference/synthesize methodology only; do not import large bundle or local client assumptions. |
| `puzanov/wordstat-agent` | MIT | 2026 Wordstat path via Yandex Cloud Search API v2 with `YANDEX_API_KEY`, `YANDEX_FOLDER_ID`, region, and stdlib CLI; Wordstat needs seed phrases, not blank trend discovery. | Reference/synthesize API preflight and CLI pattern. |
| `OlegRadinuk/yandex-direct-mcp` | MIT | Mutating Direct tools should default to dry-run/`confirm=false`; sandbox/production switch is explicit. | Synthesize safety guard into `yandex-wordstat-research`/`ad-campaign-operations`. |
| `demokrat90/yandex-direct-mcp` | MIT | Small Direct+Wordstat MCP and API reference docs; useful as an implementation reference. | Reference only; prefer LidFly MCP for Ivan's runtime. |
| `Yurich-ru/yandex-ads-mcp` | no license found | Broad Direct/Metrika/Wordstat MCP surface, but unlicensed. | Do not copy/import; at most use as a search lead after license clarification. |
| `elchin92/avito-mcp` | package/README MIT; GitHub API reported NOASSERTION | Avito MCP modes/read-only/guarded/full, allowlists, confirmation meta-tools, local-first tokens, stats/promotion tool families. | Reference/synthesize safety and capability taxonomy; do not vendor generated tools/swaggers. |
| `MissiaL/avito-api` | license unclear/NOASSERTION from GitHub API | Agent skill pattern: official OpenAPI is too large; search/show only endpoint slices, inspect operation security/scope before calls. | Reference pattern only unless license clarified. |
| `b1zya/n8n-nodes-avito-api` | MIT in package | n8n Avito OAuth2 credential and resource coverage: items, promotion, messenger, ratings, autoload, CPA, call tracking. | Reference for n8n branch; do not add plugin dependency until clean install/use is required. |
| `JHamidun/claude-skill-seo-machine-ru` | MIT | Warns that browser-cookie/internal Wordstat access may work when official paths fail. | Treat as unsafe fallback/caution, not default; avoid browser-cookie automation. |

## Local synthesis rules

1. Keep LidFly MCP v3 as the preferred live path for Ivan because it centralizes Yandex/Avito account scopes and read/write tools.
2. Use external GitHub repos as reference patterns, not runtime dependencies, unless Ivan explicitly asks to install or fork one.
3. For Yandex research: force product map + mask layers + saved raw wave before analysis; avoid one-off query fishing.
4. For Direct/Avito writes: require read-back, dry-run/guarded mode where available, and explicit approved scope.
5. For Avito OpenAPI work: search endpoint slices and inspect security/scopes; never dump full specs or generated catalogs into skill context.
6. Browser-cookie/internal APIs are not default paths; use official API/MCP/export first and label any manual/browser fallback.
