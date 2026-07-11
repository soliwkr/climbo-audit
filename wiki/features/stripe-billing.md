# Stripe Billing

> **One-line summary:** Climbo connects to your Stripe account so client subscriptions are billed automatically — no invoices to chase, no manual renewals.

---
tags: [features, billing, stripe]
sources: [PLAYBOOK, YOUTUBE-ANALYSIS, skool-first-client-stripe]
last_updated: 2026-07-11
---

## Overview

Climbo integrates with Stripe for client billing. Once connected, your clients enter their payment details once during signup and are billed automatically on a recurring schedule. You receive the money in your Stripe account. You do not handle any payment manually.

This is what makes the agency model truly passive: clients pay forever without you lifting a finger.

## How it works

### Connecting Stripe

1. Go to **Settings → Finance → Account** in your Climbo agency dashboard
2. Click "Connect Stripe" — you'll be redirected to Stripe's OAuth flow
3. Log in to your Stripe account (or create one at stripe.com if you don't have one)
4. Authorize Climbo to create subscriptions on your behalf
5. Done — Stripe is now connected

### Creating plans with Stripe

When you create a Plan in Climbo (`Plans → New Plan`), you set:
- Plan name
- Monthly or annual price
- Features included
- Trial period (optional — e.g., 14 days free before first charge)

Climbo automatically creates the corresponding Stripe product and price object. When a client subscribes to your plan, a Stripe subscription is created. Billing is automatic.

### The client checkout experience

When a new client signs up or upgrades, they see a Stripe-hosted checkout page with:
- Your agency's branding (colors, logo — configured in your Stripe account under Branding)
- The plan details and price
- Credit card or SEPA debit input fields
- Optional: coupon code field (if you've created coupons in Climbo)

After payment, their account is automatically activated or upgraded.

### Coupons and free trials

Create coupons in `Settings → Finance → Coupons`:
- **100% discount forever** — for founding clients or special offers
- **% off for X months** — for introductory promotions
- **Fixed amount off** — for one-time discounts

Clients enter the coupon code at checkout. Stripe applies the discount automatically.

For a free trial without a coupon: set a trial period on the plan itself (e.g., 14-day free trial — card required at signup but not charged until the trial ends).

### The Sales dashboard (Home Charts)

In your agency dashboard under **Sales**, you see:
- MRR (Monthly Recurring Revenue) for the last 7, 30, 90, and 365 days
- Individual subscription activity
- Revenue trends

After the July 9, 2026 update (Home Charts), this view became significantly more detailed.

### Payouts

Configure how you receive money in `Settings → Finance → Payouts`. Stripe pays out to your bank account on your configured schedule (daily, weekly, or monthly). Make sure your bank details are accurate before your first client is charged.

## Key details / Tips

- **Stripe is not available everywhere.** If you operate in a country where Stripe is not supported, you'll need to handle billing manually or use a Stripe alternative connected via Zapier/Pabbly. Multiple community members in non-Stripe countries have found workarounds.
- **VAT for EU operators.** Stripe may require a VAT number during integration for businesses in the EU. If you don't have one, check the Climbo community for workarounds specific to your country.
- **Stripe branding.** The Stripe checkout page can show your brand colors and logo. Configure this in your Stripe account under Settings → Branding — it does not sync automatically from Climbo's brand settings.
- **Moving clients from free to paid.** If you add a client manually (without Stripe), you can later transition them to a paid Stripe plan. The community has discussed the smoothest way to do this — generally create a private, non-public plan and share the checkout link directly.
- **The "First client with Stripe" moment** is a community milestone. When the first automatic payment hits your Stripe dashboard, the business model becomes real. (This post got 39 comments in the Skool community.)

## Related

- [[getting-started/pricing-and-plans]] — how to structure your pricing
- [[features/balance-explained]] — separate from Stripe (covers SMS/WhatsApp/AI costs)
- [[getting-started/account-setup]] — where Stripe setup fits in initial configuration

## Sources

- Operational reference: PLAYBOOK
- Skool: `first-client-with-stripe-yeyyyy` — 39-comment community celebration
- YouTube analysis: YOUTUBE-ANALYSIS (Stripe Accounting feature, July 2026)
