# SMTP Setup

> **One-line summary:** Connect your own email domain to Climbo so review request emails come from @yourdomain.com instead of a generic address.

---
tags: [operations, smtp, email, white-label]
sources: [HZ-9avetOnE]
last_updated: 2026-07-11
---

## Overview

By default, Climbo sends review request emails using its own mail server. This works, but the "from" address will not be your brand — it will be a Climbo address.

SMTP (Simple Mail Transfer Protocol) lets you connect your own email account so that emails sent by Climbo appear to come from you. Example: instead of `noreply@climbo.com`, your clients' customers receive a message from `reviews@youragency.com` or `hello@yourbusiness.it`.

This feature was announced in the AMA of June 25 2026.

## Why it matters

- **Trust:** Emails from a recognized domain get opened more. Emails from an unknown generic address get ignored or marked as spam.
- **Deliverability:** Properly configured domains with SPF/DKIM records have lower spam rates than shared mail servers.
- **Professionalism:** If you're white-labeling Climbo under your agency brand, everything — including emails — should look like it comes from you.

## How to set it up

1. Go to your Climbo dashboard
2. Navigate to **Settings > Email > SMTP**
3. Enter your SMTP details:
   - **Host:** e.g. `smtp.gmail.com` or `smtp-relay.brevo.com`
   - **Port:** 587 (TLS) or 465 (SSL)
   - **Username:** your email address
   - **Password:** your SMTP password or app password
4. Send a test email to confirm it works

## Recommended SMTP providers

| Provider | Cost | Notes |
|----------|------|-------|
| Google Workspace | ~€6/month per user | Reliable, familiar, good deliverability |
| Brevo (formerly Sendinblue) | Free up to 300 emails/day | Good free tier for starting out |
| Zoho Mail | Free plan available | Budget option, lower limits |

For most agency owners starting out, **Brevo's free tier** covers review request volumes for the first several months. Upgrade to Google Workspace when you want the polished @yourdomain.com identity.

## Key details / Tips

- If you use Gmail (personal), you need to generate an **App Password** in your Google account security settings — the regular password will not work
- Make sure your domain has SPF and DKIM records set correctly, or your emails may still end up in spam even with SMTP connected
- The SMTP setting applies to all review request emails across your Climbo account
- This is also where the Email History feature lives — you can review what was sent and when

## Related

- [[features/review-requests]] — what gets sent via SMTP
- [[features/white-label]] — broader white-label setup
- [[operations/onboarding-clients]] — when to configure SMTP in your workflow

## Sources

- YouTube: [SMTP For Review Requests, Coupon Codes, Email History, & More!](HZ-9avetOnE) (AMA Jun 25 2026)
