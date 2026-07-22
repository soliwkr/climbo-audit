# Climbo AMA Sessions -- Sales-Relevant Content Summary

Combined analysis of 5 AMA recordings (Jan 22 -- Apr 17, 2025) from the Climbo Accelerator Skool community. Focus: sales training, pricing, feature positioning, onboarding, and selling tips shared by Giacomo and guest Wayne Connell.

---

## 1. Sales Training Program -- Wayne Connell Partnership

**Source: Y-JnPapla-8 (Jan 22) + VibWfDfMwVA (Jan 29)**

Giacomo announced monthly free sales training sessions led by Wayne Connell, an Australian sales veteran (direct sales since 1992, 10,000+ in-home presentations). Wayne migrated his own clients to Climbo 2.0 and is described as "the review guy" in his market. The sessions ran previously in Climbo 1.0's Skool community in 2024 and were paused for a year while the team focused on 2.0 development.

### Wayne's Core Sales Philosophy

- **Local-first selling is the biggest lesson.** Small local business owners are not tech-savvy buyers. They want a local partner they can meet physically and trust. Trying to sell globally from day one is the wrong strategy. Wayne's own global clients all came from referrals that started locally.
- **"Your biggest success is always in your backyard."** Wayne became known in his area (Sunshine Coast, AU) as "the review guy" and expanded from there to the Gold Coast, then clients in NZ and the US -- all via referral.
- **The B2B local market hasn't changed fundamentally.** The way you communicate to local businesses and the techniques for door-to-door / in-person pitching remain effective.
- **Monthly Zoom format:** structured topic + open forum Q&A. Wayne grabs good ideas from the community, tests them himself, then refines them for the group.
- **Free for all community members.** Those wanting deeper 1-on-1 support can book paid sessions with Wayne. Wayne also runs a separate private mentoring group called "Climbo Pros."

### Giacomo's Reinforcement

> "A lot of people come to Climbo thinking they can sell to businesses in other continents, but small local business owners want a real local partnership."

He positions the Sales Accelerator as the counterpart to the product development: the platform gives you the tool, Wayne teaches you how to sell it.

---

## 2. Pricing Models & Strategy

### Coupon Codes (Y-JnPapla-8, Jan 22)

Released as V1. Agencies can create percentage or fixed-amount coupons with "once" or "forever" duration.

- **Selling tip:** Use scarcity -- e.g., "only 5 redemptions" or "expires in a week" (V2 will add expiration dates and redemption limits).
- **Sales team use case:** Each sales rep gets a unique coupon code. When a client subscribes using that code, a fixed percentage of MRR is automatically attributed to the rep. This is the foundation of the planned affiliate/sales-team system.
- Coupons are enabled per plan via the "allow coupons" toggle, which adds a "promotion code" field on the Stripe checkout.

### Package Pricing (Y-JnPapla-8, Jan 22)

New pricing model alongside the existing "price per location" model.

- **How it works:** Set a maximum number of locations per plan tier. Clients must upgrade to unlock more locations.
- **Example tiers:** Bronze (3 locations, $49/mo), Silver (5 locations, $99/mo), Gold (10 locations, $199/mo), Enterprise (100 locations, $999/mo -- hidden from billing portal, for enterprise deals only).
- **Key advice from Giacomo: Pick one pricing strategy.** Don't mix per-location and package plans in the same billing portal. Both models work; there are successful climbers using each.
- Coupons transition across plan upgrades (a "forever" coupon stays applied when a client switches from Bronze to Silver).
- Annual pricing is supported (e.g., $499/year vs $49/month).

### Free Trial Configuration (FtEM-FRfOgo, Feb 5)

- Free trial limit extended from 30 days to 90 days to accommodate agencies needing longer onboarding or more time to prove platform value.
- Free trial banner feature: show a customizable top-bar banner to trialing clients with a CTA (upgrade link, or Calendly booking link for an end-of-trial call).

### Freemium Model Discussion (FXjbN3T1BU8, Feb 12)

Giacomo opened community discussion about enabling smooth free-to-paid transitions. Current limitation: switching a client from a free plan to a paid plan requires deleting and recreating the account. Planned: seamless free-to-paid and paid-to-free switching without losing integrations, review links, or data.

### GEO Agent Pricing (LIn64wsy8wA, Apr 17)

- Blog post generation costs 3-5 cents per article (AI generation + Nano Banana image).
- No markup on AI costs -- agencies pay what Climbo pays.
- Initially free for the first few weeks, then billing will appear in the balance section.
- No bring-your-own-key option initially (uses Climbo's OpenAI + Gemini keys). Planned as a future feature if requested.

---

## 3. Feature Positioning Advice

### How to Sell the SEO Agent

**Source: VibWfDfMwVA (Jan 29)**

- **Bulk review reply** is a powerful onboarding hook: clients with hundreds of unanswered Google reviews see immediate value. The agent replies to 5 past reviews/day (safe rate to avoid Google penalties). Show clients the progress tracker.
- **AI History dashboard** lets you showcase agent activity at end-of-trial meetings: "Look, without lifting a finger, the platform replied to X reviews and shared Y posts on social media."
- **Custom prompts** let you fine-tune the agent to match client voice, making the platform feel bespoke rather than generic.

### How to Sell the Website Feature

**Source: FtEM-FRfOgo (Feb 5) + FXjbN3T1BU8 (Feb 12)**

- Position it as solving a real problem: most small local businesses don't have a proper website because they don't know how to build one.
- The website is automatically populated from the Google Business Profile -- zero manual work for the client.
- **Lighthouse scores** (100 SEO, 100 accessibility, 100 best practices, 90+ performance) are a tangible selling point. Show the PageSpeed Insights results to prospects.
- **Rich snippets / schema markup** are automatically generated and updated. Agencies that do this manually charge thousands of dollars. Climbo does it with one click.
- The website is optimized for both Google and LLMs, which is a forward-looking differentiator.
- Can be enabled/disabled per plan tier, so you can use it as an upsell feature in higher-tier packages.
- Custom domain support via CNAME -- you or your client can set this up during onboarding.

### How to Sell the GEO Agent

**Source: LIn64wsy8wA (Apr 17)**

- Position as the "missing piece of the review marketing flywheel": SEO agent handles review replies, Social agent shares reviews on social media, GEO agent generates blog content from business data + reviews.
- **Automated blogging** that targets local keywords (e.g., "best karate studio in [city name]") -- exactly what ranks in Google and AI chat answers.
- Articles include review quotes as social proof and CTAs (visit website, Google Maps directions, leave a review).
- Social media cross-posting: each blog post can automatically generate a social media post with a caption and link.
- Blog analytics coming soon (views, CTA clicks) so agencies can prove ROI to clients.
- **FAQ-style articles** planned: "What is the best [business type] in [city]?" -- these rank extremely well in AI chat answers (ChatGPT, Perplexity, etc.).

### How to Sell Widgets (VibWfDfMwVA, Jan 29)

- New ability to filter widgets by review source (show only Google reviews, hide Trustpilot, etc.).
- Video support on review links increases conversion -- clients can add a selfie video saying "thanks for visiting, we'd love a review."

---

## 4. Onboarding Guidance

### Google Connection During Onboarding (VibWfDfMwVA, Jan 29)

- New first-login flow prompts clients to connect their Google Business Profile immediately (via login or public access).
- Clients who connect during onboarding arrive in the platform with reviews, profile info, and all Google features already populated.
- Skippable for clients who want to do it later, but "a big percentage will complete this integration" if prompted.

### Free Trial Email Sequences (FtEM-FRfOgo, Feb 5)

Five new automated email templates:
1. **Welcome email** (existing)
2. **3 days after signup** -- stimulate engagement or invite to book an end-of-trial meeting
3. **7 days after signup** -- same purpose, second touchpoint
4. **Trial ending soon** (3 days before trial ends, existing)
5. **Trial ended -- payment success/failure** (existing)

Plus new payment lifecycle emails:
- **Charge succeeded** -- monthly "thank you" / confirmation
- **Charge failed** -- critical for reducing involuntary churn; prompts clients to update their payment method before their platform is paused

All disabled by default; enable individually from Agency Settings > Templates.

### Free Trial Banner (VibWfDfMwVA, Jan 29)

- Customizable banner shown only to trialing clients.
- Suggested uses: "You are on a 7-day free trial" + "Upgrade here" button, or a Calendly link to book an end-of-trial review call.
- Increases conversion from trial to paid.

### Onboarding Setup Advice (Y-JnPapla-8, Jan 22)

- During setup, train the client's staff on what words to use when asking for reviews.
- Help clients fill in their Google Business Profile completely (logo, cover photo, description, social URLs, photos, attributes, services) -- this data feeds the website, widgets, and AI agents.
- If clients aren't tech-savvy, set up the custom domain CNAME for them during onboarding.

---

## 5. Selling Tips from Giacomo

### On Sustainability (Y-JnPapla-8, Jan 22)

> "Climbo is not a super easy business model, but if you commit to work especially locally, be a real local partner for your clients, there are a lot of people who started from zero and transformed it into a real business. Not easy -- nothing is easy, especially business -- but this is possible."

### On Proving Value During Free Trials

- Use the AI History dashboard to show clients that agents are working in the background.
- At end-of-trial meetings, demonstrate: reviews replied to, social posts created, ranking improvements.
- The free trial banner keeps the upgrade CTA always visible.

### On Reducing Churn

- Automated charge-failed emails catch involuntary churn before the platform pauses.
- The 3-day and 7-day post-signup emails keep clients engaged during the critical first week.
- The knowledge base chatbot (embeddable in the white-label platform) reduces support burden and helps clients self-serve.

### On Incentivized Reviews

- Offering incentives for Google reviews violates Google policies and FTC rules.
- Verbal/physical interaction is a gray area -- staff can mention a reward when asking for a review in person, but nothing should be written on the review link.
- Giacomo's stance: "We do not suggest it if in your country it's not 100% legal."

### On Sales Team / Affiliate System (Planned)

- Each sales rep gets a unique coupon code.
- Fixed commission percentage on MRR from clients they close.
- Reps add their PayPal for payouts; commissions are tracked automatically.
- Initially fixed percentage; advanced options (tiered, time-limited) in future versions.
- Planned for Q1 2025 (likely May based on April AMA update).

### On Upselling Multi-Location Clients

- Package pricing naturally creates an upsell path: clients hit their location limit and must upgrade.
- Enterprise tier can be hidden from the billing portal for custom/negotiated deals.
- Multi-location management improvements planned: aggregated widgets, aggregated stats across all locations.

---

## 6. Key Feature Timeline (Sales-Relevant)

| Feature | Status as of Apr 17 | Sales Impact |
|---|---|---|
| Monthly Sales Trainings (Wayne) | Live since Feb 2 | Direct sales coaching |
| Coupon Codes V1 | Live | Discounting, scarcity, sales rep tracking |
| Package Pricing | Live | Tiered upsell model |
| Free Trial Banner | Live | Trial-to-paid conversion |
| Google Connect at Onboarding | Live | Faster time-to-value |
| Agency Email Templates (5 new) | Live | Automated nurture sequence |
| Bulk Review Reply | Live | Onboarding wow factor |
| AI History Dashboard | Live | End-of-trial demo tool |
| Pre-Built Website | Live | New sellable feature, SEO proof points |
| GEO Agent | Live (Apr 17) | Blog + social automation, AI visibility |
| Employee Review Tracking | Next in roadmap | Staff gamification, accountability |
| Sales Team / Affiliate System | Planned (May+) | Scale via sales reps |
| Freemium Model (free-to-paid switch) | Planned | Premium conversion path |

---

## Summary

The 5 AMA sessions reveal a deliberate strategy: Climbo is building a flywheel where each new feature (SEO agent, social agent, website, GEO agent) creates an additional reason for local businesses to stay and pay, while simultaneously giving agencies more proof points to close deals. Wayne Connell's sales training reinforces that the winning approach is hyper-local, relationship-driven selling -- not mass outreach. Giacomo's pricing advice consistently emphasizes simplicity (pick one model, don't overcomplicate), and his onboarding guidance focuses on reducing time-to-value so clients experience the platform's automation within their first login. The planned sales team / affiliate system will let agencies scale beyond solo selling by recruiting reps with tracked coupon codes and automated commission attribution.
