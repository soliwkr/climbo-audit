# Social Agent

> **One-line summary:** The Social Agent turns your client's best reviews into social media posts and publishes them automatically to Google Business Profile, Facebook, and Instagram.

---
tags: [ai-agents, social-media, gbp]
sources: [BRocA7husPU, LIn64wsy8wA]
last_updated: 2026-07-11
---

## Overview

The Social Agent does three things automatically when a new five-star review arrives:
1. Generates a branded image featuring the review text
2. Writes a caption for the post
3. Publishes to Google Business Profile (GBP), Facebook, and/or Instagram

No scheduling. No manual posting. No copywriter needed.

This matters for two reasons:
- **GBP ranking:** Google favors active profiles. A business that posts weekly ranks above one that posted once in 2022. The Social Agent keeps the profile alive continuously.
- **Social proof:** Potential customers browsing Instagram or Facebook see real five-star reviews from real customers. This is social proof that converts.

## How it works

### Setup (one time per client)

1. In the client's account, go to **AI Agents → Social Agent**
2. Enable the agent
3. Connect social platforms:
   - **Google Business Profile** — already connected from GBP setup
   - **Facebook** — client logs in via Facebook OAuth
   - **Instagram** — connected via Facebook Business Manager
4. Configure:
   - Which platforms to publish to
   - Post frequency (publish every review? or cap at X posts per week?)
   - Caption style (promotional, friendly, question-based, etc.)
   - Custom prompt for captions if you want a specific voice

### Ongoing operation

When a four or five-star review arrives, the agent:
1. Selects it as eligible for a post (lower-rated reviews are skipped)
2. Creates an image with the review text, star rating, and business branding
3. Writes a caption using the configured style
4. Publishes to all connected platforms simultaneously

The client can see all social posts in their platform under the **Social** or **Content** section. Posts go live without any approval step unless you configure otherwise.

## Key details / Tips

- **GBP posts are the most important output.** Even if the client doesn't care about Facebook, GBP posts directly influence local Maps ranking. Always enable GBP at minimum.
- **Image quality is automatic.** Climbo generates images that look like branded marketing materials. Clients who see the first auto-generated post are usually surprised how good it looks.
- **You can customize the visual style.** The image template follows your brand settings, so if you've set brand colors in Climbo, those colors appear in the generated images.
- **Frequency cap.** If a client gets 20 reviews in a week, you probably don't want 20 posts published in that same week. Configure a reasonable cap (e.g., 3 posts/week maximum) to keep posting natural.
- **Caption approval mode.** If a client is particular about messaging, enable an approval step so they (or you) can review captions before they publish.

## What clients see

From their dashboard, clients can see:
- A gallery of all auto-published social posts
- Which platform each post was sent to
- Engagement stats if connected via Facebook/Instagram API
- The SEO Agent activity alongside social activity in the Home Charts view

When a client sees that their Instagram profile now has 30 posts they never wrote, using real five-star reviews from real customers, the value of the platform is obvious.

## Related

- [[ai-agents/overview]] — how all three agents work together
- [[ai-agents/seo-agent]] — the reply agent that works in parallel
- [[features/gbp-integration]] — GBP must be connected for GBP posts
- [[features/client-portal]] — what clients see in their dashboard

## Sources

- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — Social Agent demo
- YouTube: [GEO Agent is Live! AMA](LIn64wsy8wA) — overview of all agents
