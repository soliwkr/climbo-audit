# GDPR — EU Compliance for Review Requests

> **One-line summary:** Practical guidance for EU agency owners sending review requests — what you need to know, not legal advice.

---
tags: [compliance, gdpr, eu, email, sms]
sources: [skool-gdpr-compliant, skool-post-ama-promise]
last_updated: 2026-07-11
---

## Overview

If you're operating in the EU, GDPR applies when you collect and use customer data (names, phone numbers, email addresses) to send review requests. This page covers the basics you need to stay safe in practice.

This is not legal advice. If you have specific concerns, consult a lawyer in your country.

## What GDPR means for your Climbo setup

When your clients give you a list of their past customers to upload into Climbo, those customers' data (name, email, phone) is being processed. As the agency running Climbo:

- **Your client is the data controller** — they collected that data from their customers
- **You are the data processor** — you're processing it on their behalf
- You should have a **Data Processing Agreement (DPA)** in place with each client (a short contract addendum)

## Lawful basis for sending review requests

The most practical lawful basis for a review request is **legitimate interest** or an **existing customer relationship** (in some EU countries, this is called the "soft opt-in" rule under ePrivacy).

In practice, this means:

- Only send review requests to people who have **had a real transaction** with the business — not cold contacts, not scraped lists
- The request must be **related to the transaction** (asking about their experience as a customer)
- The business name must be **clearly visible** in the message so the recipient knows who is contacting them

## Practical checklist

- [ ] Only import customers who have made a purchase or appointment
- [ ] Review request templates include the business name (Climbo's default templates do)
- [ ] You have a DPA with your clients
- [ ] Clients understand they are responsible for having had a legitimate relationship with their customers
- [ ] Do not purchase contact lists or send to unrelated contacts

## What about SMS?

SMS (text messages) for marketing is more tightly regulated in some EU countries than email. In some jurisdictions you need explicit opt-in consent for promotional SMS. Review requests generally qualify as transactional, not promotional, but this varies by country. When in doubt, start with email.

## Key details / Tips

- GDPR came up as one of the highest-engagement threads in the Skool community (28 comments, Jan 2026) — it is a real concern for EU agency owners
- Climbo's data is stored in their infrastructure; ask Climbo support directly for their DPA if you need one for your clients
- The "legitimate interest" basis is generally sufficient for post-transaction review requests to existing customers — you do not need prior opt-in consent in most EU countries for this specific use case

## Related

- [[features/review-requests]] — how review requests are sent
- [[compliance/google-review-policy-2026]] — Google's own policy rules
- [[operations/onboarding-clients]] — where to get customer lists from clients

## Sources

- Skool: `gdpr-compliant` (Jan 14 2026, 28 comments)
- Skool: `post-ama-promise` — GDPR compliance update discussion (Jun 2026)
