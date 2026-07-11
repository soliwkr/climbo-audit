# AI Agents Overview

> **One-line summary:** Three AI agents run automatically in the background, turning each new review into SEO value, social content, and AI search visibility.

---
tags: [ai-agents, core-feature]
sources: [BRocA7husPU, LIn64wsy8wA, sIGOLZ1kFAQ, 12NwL4G8vIE]
last_updated: 2026-07-11
---

## Overview

Climbo has three AI agents. You enable them during client onboarding and they run on autopilot forever after. Your client does not need to understand them — they just see the results.

The agents work together as a loop: every incoming review feeds all three agents, which together improve the client's visibility across Google, social media, and AI search engines.

```
New review arrives
  ↓
SEO Agent → AI reply with local keywords → Google Maps ranking improves
  ↓
Social Agent → review becomes a post on GBP, Facebook, Instagram
  ↓
GEO Agent → review content feeds blog article → ChatGPT/Perplexity citation
  ↓
More visibility → more customers → more reviews
```

This is the **Review Marketing Flywheel**. It compounds over time. A client with 10 reviews benefits less than one with 100, which benefits less than one with 500.

## The three agents

### SEO Agent
Automatically replies to every Google review using the client's business name, city, and main services as keywords. This is the most direct signal Google uses to rank local businesses.

Configurable settings:
- Reply tone (professional, friendly, formal)
- Reply length
- Language (supports multiple languages)
- Custom keywords to include
- Additional instructions

→ Full details: [[ai-agents/seo-agent]]

### Social Agent
Takes the best incoming reviews and turns them into social media posts. Generates an image and a caption, then publishes to Google Business Profile posts, Facebook, and Instagram — automatically.

The GBP post is especially important: Google favors active profiles. Regular posts signal to Google that the business is engaged, which helps Maps ranking.

→ Full details: [[ai-agents/social-agent]]

### GEO Agent
Builds and updates a website/blog for the client using their review content and business data. This content is structured with schema markup so AI systems like ChatGPT, Perplexity, and Google's AI Overviews can cite the business.

Released April 17, 2026. This is the newest and most differentiated of the three agents.

→ Full details: [[ai-agents/geo-agent]]

## Where to configure agents

Agents are configured in two places:
1. **Brand settings** (agency-level defaults) — set the baseline behavior for all clients
2. **Per-client settings** — override defaults for individual clients

Go to `Brand → SEO Agent / Social Agent / GEO Agent` to set defaults. Then when you onboard a client, go to their account and adjust if needed.

## What the client sees

From the July 9, 2026 AMA (Home Charts feature), the client's home screen shows:
- **Agent Activity panel** — a live log of what each agent has done (replies written, posts published, blog articles created)
- **Growth charts** — review count over time, rating trend, GBP impressions and clicks

Clients see proof that the system is working without needing to understand the mechanics.

## Key details / Tips

- You can run "reply to all past reviews" with one click — useful for clients who have 50+ unanswered reviews from years past
- The AI name that appears to clients is your branded AI name (configured in Brand), not "Climbo AI"
- If a client asks ChatGPT about their business type in their city and the business doesn't appear, the GEO Agent is the fix
- Agents use tokens from your Balance. At $6.60 per 1M tokens, the cost is minimal for most clients

## Related

- [[ai-agents/seo-agent]] — SEO Agent in detail
- [[ai-agents/social-agent]] — Social Agent in detail
- [[ai-agents/geo-agent]] — GEO Agent in detail
- [[features/gbp-integration]] — why GBP connection is required for agents
- [[features/balance-explained]] — token costs and balance management

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — agent setup walkthrough
- YouTube: [GEO Agent is Live!](LIn64wsy8wA) — AMA April 17, 2026
- YouTube: [Climbo in 1 minute](sIGOLZ1kFAQ) — three-agent summary
- YouTube: [Home Charts AMA](12NwL4G8vIE) — client dashboard update July 9, 2026
