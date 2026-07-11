# Google Sheets Integration

> **One-line summary:** Connect a Google Sheet to Climbo so new rows automatically add contacts and trigger review requests — no CRM required.

---
tags: [features, integrations, automation]
sources: [BRocA7husPU, YOUTUBE-ANALYSIS, SKOOL-ANALYSIS]
last_updated: 2026-07-11
---

## Overview

Google Sheets integration lets you use a simple spreadsheet as a CRM that feeds Climbo automatically. When a business owner adds a customer to their Google Sheet (name, phone, service date), Climbo picks it up via Zapier and automatically sends that customer a review request at the right time.

Released: May 2026. 24 comments in the Skool community on release.

## How it works

### The flow

```
Business owner adds new row to Google Sheet
  → Zapier detects new row
  → Zapier adds contact to Climbo
  → Climbo auto-send triggers: sends review request X hours after service date
```

### Setup

**What you need:**
- A Google Sheet with columns: Name, Phone Number (or Email), Service Date
- A Zapier account (free tier is sufficient)
- Climbo's Zapier integration enabled (Settings → Zapier)

**Step-by-step:**

1. In Climbo: go to **Settings → Zapier** → generate your Zapier API key
2. In Zapier: create a new Zap
   - Trigger: Google Sheets → New Row
   - Action: Climbo → Add Contact
3. Map columns: Sheet Name → Contact Name, Sheet Phone → Contact Phone, Sheet Date → Service Date
4. Enable auto-send in Climbo (set trigger: "send X hours after service date")
5. Test: add a row to the sheet, confirm the contact appears in Climbo within a few minutes

### The direct Google Sheets integration (May 2026)

Climbo also released a native Google Sheets integration (separate from Zapier) in May 2026. This allows client data — review counts, ratings, rankings — to sync out to a Google Sheet automatically. Use cases:

- **Client reporting:** Share a Google Sheet with your client instead of asking them to log into the portal — they see their data in a familiar format
- **Agency tracking:** One master sheet showing all clients' review counts, updated automatically
- **Custom dashboards:** Build Google Looker Studio dashboards from the Sheets data

## Key details / Tips

- **Perfect for technophobe clients.** If a client refuses to learn a dashboard but already uses Google Sheets daily, this integration gives them everything they need without changing their workflow.
- **The sheet is their CRM.** Train the client: "After every appointment, add the customer to row X. Everything else is automatic."
- **Column order matters in Zapier.** Map your columns carefully during Zap setup. A mismapped phone field sends review requests to the wrong number.
- **Date format matters.** Make sure the service date column uses a format Zapier recognizes (YYYY-MM-DD is safest). Wrong date format = auto-send fires at the wrong time or not at all.
- **You don't need Zapier if the client manually uploads CSVs.** Climbo accepts CSV contact uploads directly. For clients who prefer batch uploads over live sync, this is an easier path.

## Related

- [[features/review-requests]] — what happens after the contact is added
- [[operations/onboarding-clients]] — where Sheets integration fits in the onboarding flow
- [[features/client-portal]] — alternative to Sheets for clients comfortable with dashboards

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — Zapier/Sheets integration demo
- Skool: `new-feature-releases-updates-ama-recording-14052026` — 24 comments, May 2026 release
- YOUTUBE-ANALYSIS: feature timeline showing May 2026 Google Sheets release
