# Climbo LLM Wiki — Schema

This document is the operating manual for the LLM that maintains this wiki.
Read it fully before touching any wiki file.

---

## What this wiki is

A persistent, interlinked knowledge base about Climbo — the white-label AI review
and local SEO platform. Built from:
- 30 YouTube transcripts from @climboapp (Jan–Jul 2026)
- 933 Skool community posts (Nov 2025–Jul 2026)
- Public site and authenticated app documentation

**Audience:** New Climbo agency owners who just signed up and don't know where to start.
Tone: clear, direct, no fluff, no jargon unless explained. English.

**You (the LLM) own this layer entirely.** The human reads it; you write and maintain it.

---

## Directory structure

```
wiki/
├── SCHEMA.md              ← this file (never modify without user direction)
├── index.md               ← content catalog, update on every change
├── log.md                 ← append-only operations log
├── overview.md            ← what Climbo is, how it all fits together
├── getting-started/
│   ├── what-is-climbo.md
│   ├── account-setup.md
│   ├── first-client-checklist.md
│   └── pricing-and-plans.md
├── features/
│   ├── review-requests.md
│   ├── nfc-cards.md
│   ├── gbp-integration.md
│   ├── white-label.md
│   ├── client-portal.md
│   ├── stripe-billing.md
│   ├── google-sheets.md
│   ├── mobile-app.md
│   └── balance-explained.md
├── ai-agents/
│   ├── overview.md
│   ├── seo-agent.md
│   ├── social-agent.md
│   └── geo-agent.md
├── sales/
│   ├── finding-clients.md
│   ├── demo-script.md
│   ├── objections.md
│   └── pricing-conversations.md
├── compliance/
│   ├── google-review-policy-2026.md
│   └── gdpr-eu.md
├── operations/
│   ├── onboarding-clients.md
│   ├── retention.md
│   └── smtp-setup.md
├── case-studies/
│   └── community-wins.md
└── ama/
    └── README.md          ← index of AMA summaries
```

---

## Page format

Every wiki page follows this template:

```markdown
# Page Title

> **One-line summary** of what this page covers.

<!-- Optional: frontmatter block -->
---
tags: [feature, review-requests]
sources: [BRocA7husPU, skool-post-XXXX]
last_updated: 2026-07-11
---

## Overview
[2-3 paragraphs max. What is this, why does it matter, when do you use it]

## How it works
[Step by step if procedural, or structured explanation if conceptual]

## Key details / Tips
[Bullet points of gotchas, best practices, common mistakes]

## Related
- [[other-page]] — why it's related
- [[another-page]] — why it's related

## Sources
- YouTube: [Video Title](videoId) — timestamp if relevant
- Skool: post slug or topic
```

**Rules:**
- `[[wiki-link]]` syntax for internal links (Obsidian-compatible)
- Never exceed 500 words per page unless the topic requires it
- No walls of text — use headers, bullets, short paragraphs
- Every page must have at least one `## Related` entry
- Every page must list its `## Sources`

---

## Index format (index.md)

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD — N pages total_

## Getting Started
- [[getting-started/what-is-climbo]] — One-line description
- ...

## Features
- ...

## AI Agents
- ...

## Sales
- ...

## Compliance
- ...

## Operations
- ...

## Case Studies
- ...

## AMA Summaries
- ...
```

---

## Log format (log.md)

Each entry starts with `## [YYYY-MM-DD] operation | description`.
This makes it grep-parseable: `grep "^## \[" log.md | tail -10`

```markdown
## [2026-07-11] ingest | YouTube transcripts — 30 videos processed
## [2026-07-11] ingest | Skool posts — 933 posts processed  
## [2026-07-11] build | Initial wiki — 25 pages created
```

---

## Ingest workflow

When adding a new source:
1. Read the source fully
2. Identify which existing pages it updates, contradicts, or extends
3. Update those pages
4. Create new pages if needed
5. Update index.md
6. Append to log.md

When a source **contradicts** an existing page, add a `> ⚠️ Note:` callout
with the date and source, then flag the discrepancy clearly.

---

## Query workflow

When answering a question:
1. Read index.md to find relevant pages
2. Read those pages
3. Synthesize answer with `[[citations]]`
4. If the answer is broadly useful, file it as a new wiki page

---

## Lint checklist (run periodically)

- [ ] Orphan pages (no inbound links from other pages)
- [ ] Broken `[[links]]` (page doesn't exist)
- [ ] Pages with no `## Sources`
- [ ] Contradictions between pages
- [ ] Missing pages for concepts mentioned but not documented

---

## Content principles

**For beginners:**
- Define every term on first use
- Never assume they know what GBP, NFC, or white-label means
- Lead with "what you do" before "how it works"
- Use real examples from the community whenever possible

**What to leave out:**
- Internal Climbo dev details (API internals, database schema)
- Speculation about future features
- Content that hasn't been confirmed working

---

_Schema version: 1.0 — 2026-07-11_
