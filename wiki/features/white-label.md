# White-Label

> **One-line summary:** White-label means your clients see your brand entirely — your name, your domain, your AI assistant's name, your colors. Climbo is invisible.

---
tags: [features, white-label, branding]
sources: [BRocA7husPU, PQiNrTKVLOU, YOUTUBE-ANALYSIS]
last_updated: 2026-07-11
---

## Overview

White-label is the business model that makes Climbo worth €99/month. You are not reselling "Climbo." You are selling your own AI reputation management platform. Your clients see your brand everywhere: the login page, the dashboard, the email notifications, the AI assistant name, the review link they share with customers.

From Climbo's 2026 video "Your AI, Fully Branded":

> "Give your AI its own name, logo, and identity. You can even personalize every single agent — SEO, Social, and GEO."

## How it works

All white-label settings live in **Brand** in your agency dashboard at `my.climbo.com`.

### What you can customize

| Element | What to set | Where clients see it |
|---------|------------|---------------------|
| Brand Name | Your agency name | Login page, emails, dashboard header |
| Custom Domain | e.g., `app.youragency.com` | Browser URL bar, every link |
| Logo | Your logo file | Login page, dashboard, emails |
| Colors | Primary/secondary colors | Buttons, highlights, accents |
| Font | Custom web font | All text in the platform |
| AI Name | e.g., "Aria", "MaxAI" | Chatbot, agent activity, email subject lines |
| AI Logo | Custom avatar for your AI | Chatbot interface |
| "Powered By" URL | Your domain | Footer of the platform |
| Free Trial Banner | Custom upgrade message | Clients on trial plan |
| Custom Code | JS/CSS injections | Platform-wide customization |

### Custom Domain Setup

1. Purchase a subdomain for your agency (e.g., `app.youragency.com`)
2. In Climbo Brand settings, enter this domain
3. Add a CNAME DNS record pointing to Climbo's servers (Climbo provides the target address)
4. Wait 5–30 minutes for DNS propagation
5. Your clients now access the platform at your domain — no reference to Climbo in the URL

### AI Agent Personalization

Each of the three AI agents can be individually branded. In Brand settings:
- Set a prompt sentence that defines the AI's personality and approach
- Customize the agent names (what clients see when they look at agent activity)
- Add a custom AI logo that appears in the chat interface

### AI Chatbot

Enable the AI Chatbot in Brand settings. When active, your clients interact with your named AI assistant via chat instead of navigating the dashboard manually. The chatbot can:
- Send review request campaigns
- Update GBP info
- Add contacts
- Manage templates

This is especially useful for tech-averse clients. They don't learn a dashboard; they talk to an AI assistant that has your name and branding.

### Email branding

Every automated email your clients receive (welcome email, review notifications, billing reminders) comes from your agency's SMTP if configured. See [[operations/smtp-setup]] for setup details.

Without custom SMTP, emails still show your agency name but may come from a Climbo sending domain.

## Key details / Tips

- **Test your branded platform before the first client call.** Open a private/incognito browser window and visit your custom domain. See exactly what your client will see. Fix anything that looks off.
- **The login page is a sales asset.** It is the first thing a prospect sees when you show them "the platform." Make sure it looks professional.
- **White-label extends to the review link.** The link you share with your client's customers shows your client's branding — their logo, their business name. Climbo's name never appears.
- **Support access.** Clients cannot see the Support link that leads to Climbo. They see only your agency's contact methods, which you configure.

## Related

- [[getting-started/account-setup]] — where to configure Brand settings
- [[operations/smtp-setup]] — branded email setup
- [[features/client-portal]] — what the branded dashboard looks like for clients
- [[features/stripe-billing]] — Stripe can also be branded with your colors

## Sources

- YouTube: [Climbo Restart](PQiNrTKVLOU) — white-label as core business model
- YouTube: [Your AI Fully Branded](rJhFyiE_Yvk) — agent personalization (May 2026)
- YouTube: [Start a $3k/mo Reputation Management Business](BRocA7husPU) — platform walkthrough with white-label in context
