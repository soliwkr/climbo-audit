# GBP Integration

> **One-line summary:** Connecting Google Business Profile (GBP) is the foundation of everything — reviews, replies, social posts, ranking, and the GEO Agent all depend on it.

---
tags: [features, gbp, google]
sources: [BRocA7husPU]
last_updated: 2026-07-11
---

## Overview

**GBP (Google Business Profile)** is the free Google listing that appears when someone searches for a local business. It shows the name, address, hours, photos, reviews, and contact info. It is the most important digital asset a local business has.

Climbo connects directly to GBP via the Google API. Once connected:
- New reviews appear in Climbo automatically
- The SEO Agent can publish replies directly to Google
- The Social Agent can create GBP posts
- Business info edited in Climbo syncs to Google instantly
- The GEO Agent can generate a website that matches GBP data exactly

## How it works

### Connecting GBP

During client onboarding:
1. Go to client account → **Settings → Integrations → Google**
2. Click "Connect Google Account"
3. The client logs in with the Google account that manages their GBP
4. Select the correct GBP location if they have multiple
5. Done — connection takes about 60 seconds

If the client cannot be present, you can request **Manager access** on their GBP instead:
- Go to Google Business Profile manager → add a new Manager using your Google account
- Once accepted, you can connect the GBP from your Climbo without needing the client's login credentials
- This also protects you: if the client churns, remove your access. If you own the Manager role, you maintain control.

### What Climbo manages via GBP

Once connected, from inside the client's Climbo dashboard:
- **Business info** — name, address, phone, website, hours, social links, services, attributes — any edit here syncs to Google automatically
- **Photos** — add or update photos; they appear on GBP
- **Special hours** — holiday hours, temporary closures
- **Google Posts** — publish updates, offers, events directly to GBP (Social Agent does this automatically; client or you can also post manually)
- **Reviews** — see and reply to all Google reviews in one place

### Why accurate GBP info matters

If the hours on GBP say "open until 8pm" but the business closes at 6pm, customers arrive at a locked door and leave a 1-star review. If the website says one phone number but GBP says another, Google sees inconsistency and penalizes rankings.

Climbo's GBP integration ensures the info stays accurate. Any change made in Climbo flows to Google and also updates the auto-generated website (if the GEO Agent is active), keeping everything consistent.

This consistency is a direct ranking factor: Google trusts businesses whose information matches across their listing and their website.

## Multiple locations

If a client has more than one location (e.g., a chain of gyms, a franchise), each location is a separate client profile in Climbo. You onboard each location individually. Some community members manage clients with 15+ locations this way.

## Key details / Tips

- **GBP must be claimed.** If the client's Google listing is unclaimed (no manager), help them claim it first at `business.google.com`. This is free and takes a few days for Google to verify.
- **Suspended or flagged GBPs.** If a client's GBP has been suspended, Climbo cannot fix that. You'll need to work with Google's reinstatement process separately.
- **One GBP per Climbo client profile.** Do not connect two different GBPs to the same client account — create separate profiles.
- **Instant sync.** The connection is live. Reviews appear in Climbo within minutes of being posted on Google.
- **Other review platforms.** Climbo supports 21 review platforms total. Connect Tripadvisor, Yelp, Booking.com, etc. from the same Integrations section. Google stays the priority.

## Related

- [[ai-agents/seo-agent]] — needs GBP to publish replies
- [[ai-agents/social-agent]] — needs GBP to publish posts
- [[ai-agents/geo-agent]] — pulls GBP data to build the website
- [[features/review-requests]] — where reviews come from
- [[getting-started/first-client-checklist]] — GBP connection as onboarding step

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — GBP connection demo and explanation of why consistency matters
