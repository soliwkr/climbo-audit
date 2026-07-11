# Account Setup

> **One-line summary:** Everything you need to configure before signing your first client — brand, billing, email, and balance.

---
tags: [getting-started, setup]
sources: [BRocA7husPU, PLAYBOOK]
last_updated: 2026-07-11
---

## Overview

When you first log into `my.climbo.com`, you land on a mostly-blank agency dashboard. Before you touch the client section, complete your agency setup. This takes 1–2 hours and you only do it once.

The dashboard has six main sections: **Clients, Plans, Brand, Sales, Settings, Support.**

## How it works

### Step 1 — Configure your Brand

Go to **Brand** in the left sidebar. This is where Climbo becomes invisible and your brand takes over.

Set:
- **Brand Name** — your agency name (what clients see everywhere)
- **Custom Domain** — a subdomain like `app.youragency.com` (point it to Climbo's DNS)
- **Logo** — your agency logo, shown on the login page and inside the platform
- **Colors and Font** — match your existing brand
- **AI Brand Name** — the name your AI assistant shows to clients (e.g., "Aria" or "MaxAI")
- **Powered By** — set to your domain so emails and footers link back to you

Also in Brand, you can configure:
- **SEO Agent** settings (default tone, language, keywords)
- **Social Agent** settings
- **GEO Agent** settings
- **Free Trial Banner** — shown to trial clients to prompt upgrade
- **AI Chatbot** — enables a chat widget your clients use instead of the dashboard

### Step 2 — Set up Stripe billing

Go to **Settings → Finance** to connect Stripe. Stripe handles all subscription billing between you and your clients.

Once connected, you can create pricing plans, accept credit cards and SEPA direct debit, and view your MRR (Monthly Recurring Revenue) in the Sales dashboard.

> **Note for EU operators:** Stripe does not emit Italian-format electronic invoices (SDI). If you operate in Italy or another EU country with specific invoicing requirements, integrate a tool like Fatture in Cloud before your first paying client.

### Step 3 — Create your Plans

Go to **Plans** and create at least one subscription plan. Example:
- Name: "Starter Reputation"
- Price: $149/month
- Features: review collection, SEO Agent, GBP management

You can create multiple plans (basic, pro, premium) and control which features each plan includes.

### Step 4 — Configure SMTP

Go to **Brand → SMTP** or **Settings** to configure a custom email sender. Without this, review request emails go out from a default Climbo domain. With SMTP configured, they come from `hello@youragency.com` — fully branded.

### Step 5 — Set up Balance

Go to **Settings → Balance** and add credit. Balance is the pre-paid pool that covers SMS, WhatsApp, and AI token costs.

Cost reference:
| Channel | Approx. cost |
|---------|-------------|
| SMS (EU) | ~€0.05–0.10 per message |
| WhatsApp | ~$0.03 per message |
| Email | Free |
| AI Tokens | $6.60 per 1M tokens |

Add at least $20–50 before activating your first client on SMS or WhatsApp.

### Step 6 — Customize Email Templates

Go to **Settings → Emails / Templates** to edit the Welcome Email your clients receive when they join. Make the tone match your agency — warm, direct, and free of any technical jargon. This is the first thing they read after signing up.

### Step 7 — Test with the Demo Client

Climbo provides a demo client account. Walk through the full client experience before you bring in real clients:
- Connect a Google account
- Set up a review link
- Enable the SEO Agent
- Send a test review request

## Key details / Tips

- Your custom domain needs a DNS CNAME record pointing to Climbo's server. Contact support if you need help — it typically takes 5–10 minutes once the record propagates.
- The agency dashboard and the client dashboard are different. You see everything; clients see only their own data.
- Coupons (Settings → Finance → Coupons) let you give clients a discounted or free trial period — useful for your first wave of customers.

## Related

- [[features/white-label]] — deeper guide to brand customization
- [[features/stripe-billing]] — how Stripe billing works
- [[features/balance-explained]] — understanding the pre-paid credit system
- [[operations/smtp-setup]] — SMTP configuration step by step
- [[getting-started/first-client-checklist]] — what to do after setup

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — setup walkthrough starting ~20min mark
- Operational reference: PLAYBOOK (trovatemi.it internal doc)
