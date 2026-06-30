---
name: avito-ads-feed
description: "Avito ads feed operations: use when generating, auditing, or smoke-testing Avito service ads, XML feeds, listing copy, branded card images, category/service mappings, city expansion, feed build checks, or paid/listing performance follow-up for Ivan's marketing projects."
---

# Avito ads feed

Use this skill for Avito service-ad workflows: XML feed generation, listing coverage, service/city expansion, image-card generation, category mapping, and feed smoke tests.

Reference sources imported from local project:

```text
/Users/admin/repos/lvLokkie/territory-accounting-landing/src/pages/avito-feed.xml.ts
/Users/admin/repos/lvLokkie/territory-accounting-landing/scripts/generate-avito-cards.ts
/Users/admin/repos/lvLokkie/territory-accounting-landing/docs/yandex-direct.md
/Users/admin/repos/lvLokkie/territory-accounting-landing/src/data/site.ts
```

Treat these as project-specific examples. Do not copy real phone numbers, addresses, legal details, or brand-specific account values into a generic marketplace template.

## Safety contract

1. **Redact account/contact details in generic reports.** Use placeholders like `{{phone}}`, `{{brand_name}}`, `{{city}}`, `{{site_url}}`, and `{{legal_name}}` unless Ivan explicitly asks for project-specific output.
2. **No live publishing without approval.** Feed generation and local build checks are safe; uploading/publishing Avito listings or changing paid promotion settings requires explicit bounded approval and read-back.
3. **Do not bypass Avito controls.** No captcha/login bypass, scraping behind auth, or automation against protected Avito surfaces unless an official/API-permitted path is available.
4. **Separate feed validity from live performance.** A valid XML feed does not prove Avito accepted, indexed, or promoted the ads.

## Preflight

1. Identify project root, feed endpoint/file, service list, city list, source-of-truth data file, image output directory, and build command.
2. Identify target mode:
   - **local feed audit** — inspect source and generated XML shape;
   - **local asset generation** — generate/check branded cards;
   - **build smoke** — run project build/check;
   - **live Avito follow-up** — inspect official/API stats or manually exported data;
   - **write/publish** — apply approved changes and read back status.
3. Identify required listing dimensions: services, cities, prices, categories, contact method, manager name, images, and feed URL.

## Feed checklist

For each feed change, verify:

- expected ad count = `services × cities` after deliberate exclusions;
- each ad has stable ID, category, service type/subcategory, title, description, price, address/city, contact method, manager name, and image URL;
- title length and required Avito fields fit platform constraints;
- excluded services are documented with the reason, not silently dropped;
- prices are numeric where required and formatted separately for copy;
- image URLs match generated files and public site paths;
- XML is well-formed and uses the expected target/format version;
- build command regenerates endpoint/assets without secrets.

## Card image checklist

For generated branded images:

1. Confirm card slugs match feed image URLs.
2. Generate cards with the project command, for example `npx tsx scripts/generate-avito-cards.ts` when the repo supports it.
3. Verify expected files exist under the public image directory.
4. Inspect one image visually when layout/copy changed.
5. Keep project-specific copy in the project repo; marketplace skills should describe the process, not vendor the images.

## Operating loop

1. Read the feed endpoint and source-of-truth data file.
2. Build a service × city matrix and compare it to expected campaign scope.
3. Run or propose the local generation/build checks.
4. Validate generated XML and image references.
5. For live stats, use official Avito/API/exported data; label manual/exported data quality.
6. Produce a short action list: feed fixes, card fixes, copy/category fixes, live follow-up, or no-op.

## Stop conditions

Stop before claiming success when:

- local build/check is unavailable or failing;
- generated image files are missing;
- the feed endpoint cannot be built or parsed;
- live acceptance/performance is requested but no Avito/API/export evidence is available;
- a change would publish or alter live listings without approval.

## Output

```md
## Avito ads feed: <project>

- Mode: local audit | asset generation | build smoke | live read-only | write-planned | write-applied
- Scope: <services × cities, exclusions>
- Expected ads: <N>
- Feed status: pass | partial | fail | not generated
- Assets: pass | partial | fail | not checked
- Live Avito status: verified | not verified | blocked

### Findings
| Area | Evidence | Action | Risk |
|---|---|---|---|

### Verification
- <commands/files/API/export inspected>
- Secrets/contact details: none observed | redacted | blocked
```
