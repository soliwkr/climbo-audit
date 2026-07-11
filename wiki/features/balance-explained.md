# Balance Explained

> **One-line summary:** Balance is your pre-paid credit pool that covers the cost of SMS messages, WhatsApp messages, and AI tokens used across all your clients.

---
tags: [features, billing, balance]
sources: [PLAYBOOK, YOUTUBE-ANALYSIS]
last_updated: 2026-07-11
---

## Overview

Your Climbo Balance is separate from your €99/month subscription. It is a pre-paid credit system — similar to a phone top-up. You add money to your balance, and Climbo deducts from it as you use SMS, WhatsApp, and AI agents.

Email is free and does not touch your balance.

## How it works

### What uses balance

| Channel / Feature | Approximate cost |
|-------------------|-----------------|
| SMS (EU/US) | €0.05–0.10 per message |
| WhatsApp | ~$0.03 per message |
| Email | Free |
| AI Tokens (SEO/Social/GEO agents) | $6.60 per 1 million tokens |

**Real-world context:**
- A client getting 50 review requests per month via SMS = approximately $2.50–5.00/month in balance
- A client with 30 incoming reviews/month (SEO Agent replies each) = roughly $0.10–0.20 in AI tokens
- AI token costs are minimal for most use cases

### Adding balance

Go to **Settings → Balance** in your agency dashboard and add credit via card. You can set a minimum threshold and enable auto-recharge if you want to avoid running out unexpectedly.

### How balance is shared

Your single balance pool covers all your clients. If you have 20 clients all sending SMS review requests, they all draw from the same pool. There is no per-client allocation by default.

> June 2026 update: **AI Token Allocation per client** was released, allowing you to assign a specific token budget to individual clients. This prevents one high-volume client from consuming disproportionate resources.

### Choosing the right channel per client

- **Email** → free, good for B2B clients or when phone numbers aren't collected
- **SMS** → high open rates (90%+), ideal for restaurants and high-traffic local businesses
- **WhatsApp** → highest engagement in many markets, requires WhatsApp Business number setup by client
- **QR/NFC** → no balance cost at all (review request is built into the physical display)

For clients on free trials or in early stages, QR/NFC + email-only setup has zero variable costs. Upgrade to SMS/WhatsApp once you're billing them.

### Monitoring balance

Your agency dashboard shows your current balance. You can also see usage logs — how many messages were sent, to whom, at what cost. This helps you understand the actual cost per client and whether your pricing covers it.

## Key details / Tips

- **Top up before activating your first SMS-heavy client.** With a starting balance of $5, you have maybe 50–100 SMS messages. If your client sends requests to 200 customers on day one, you'll run out mid-campaign.
- **For early-stage agencies (1–5 clients):** $20 balance is sufficient for months. Revisit as you scale.
- **Balance costs are your cost of goods sold.** Factor them into your per-client profitability: if you charge $100/month and spend $5/month on SMS for that client, your margin is $95 — still excellent.
- **WhatsApp Business number:** Before enabling WhatsApp requests for a client, they need to have a verified WhatsApp Business number. This is set up in their integrations, not in your balance settings.

## Related

- [[features/review-requests]] — which channels use balance
- [[getting-started/account-setup]] — where to set up balance in initial configuration
- [[features/stripe-billing]] — separate from balance (handles client subscriptions)

## Sources

- Operational reference: PLAYBOOK
- YOUTUBE-ANALYSIS: Balance Explained video (June 2026), AI Token Allocation (June 2026)
