# TROVATEMI.IT × CLIMBO — Lean delivery playbook

**Current overlay: 2026-09-03**

> Questo documento risponde a una domanda sola: **come usiamo Climbo dentro il prodotto Trovatemi Lean senza trasformare il delivery layer nel prodotto?**

Governance owner: `soliwkr/trovatemi-os`.

Prima di usare qualsiasi materiale storico in questo repo leggere `TROVATEMI-DELIVERY-OVERLAY.md`.

---

## 1. Climbo nel modello Trovatemi

Climbo è il **delivery layer downstream**.

Non è:

- il CRM pre-sale;
- la fonte di verità di attribution;
- il motivo per creare più piani;
- il posizionamento pubblico;
- un nuovo prodotto.

Flow:

```text
acquisition
→ D1 / Audit Engine
→ report
→ activation / binding
→ Climbo provisioning
→ onboarding
→ first value
→ recurring delivery
```

Prospect pre-sale != Climbo contact.

---

## 2. Offerta commerciale corrente

Un solo prodotto:

- **TROVATEMI — €149/mese**;
- **21 giorni di trial**;
- **€0 durante il trial**;
- payment method required;
- rinnovo a €149/mese salvo cancellazione;
- per location.

Legacy da non usare:

- ★ TROVATO €100;
- ★★ VISIBILE €300;
- ★★★ INEVITABILE €500;
- coupon FONDATORE 100% forever;
- vecchi listini €199/€399.

---

## 3. Piano Climbo Lean

Baseline approvata/da verificare runtime:

### Reputation

- Reviews ON;
- Requests ON;
- Reminders ON;
- AI Sentiment ON;
- Review Filter OFF;
- AI Suggestions OFF initially unless needed;
- Video Testimonials OFF;
- Google review site ON;
- email/SMS/WhatsApp only where operational and cost-controlled;
- neutral/universal solicitation.

### Visibility

- Performance ON;
- SEO Agent ON where verified;
- Profile OFF;
- Website OFF;
- Widgets OFF;
- AI Ranking OFF;
- GEO OFF for Lean MVP unless explicitly reopened.

### Engagement

- Social sharing ON;
- Social Agent ON where tested;
- Facebook / Instagram / TikTok where actually supported;
- LinkedIn OFF by default.

### Other

- AI Chat OFF;
- client-facing API/Zapier surfaces OFF;
- hide Powered by ON where configured;
- billing ON.

Portal: `app.trovatemi.it`.

Legacy `os.trovatemi.it` naming is historical.

---

## 4. Review compliance

Trovatemi asks **universally and neutrally**.

No:

- review gating;
- incentives;
- selective solicitation only to happy customers;
- flows designed to suppress negative public reviews.

If vendor documentation/training shows:

```text
happy → public review
unhappy → private feedback
```

that pattern is evidence of vendor behavior, **not Trovatemi policy**.

---

## 5. Onboarding direction

Evidence from Climbo coaching supports:

> **Onboarding is not optional.**

Current operating direction:

1. preconfigure what can be preconfigured;
2. client handles Google/social OAuth and explicit consent where required;
3. human-assisted activation is acceptable;
4. recurring delivery should be automated where possible;
5. recurring manual service is not the core offer.

Do not build a new customer portal just to hide onboarding friction before the real dry-run shows what must be hidden.

Do not add GHL.

---

## 6. C0.1B deep gate

For each onboarding/provisioning step classify:

```text
PRESET
API
UI-AUTO
CLIENTE
UMANO
ELIMINARE
```

Questions for every step:

- Can it be preset in plan defaults?
- Is there an official/readable API?
- Does it require OAuth/consent from client?
- Is UI automation the only gap?
- Is the step actually necessary for first value?
- What is the cost to complete?

Rule:

> **API where possible; browser automation only as last mile.**

No production browser bot before this matrix is complete.

---

## 7. Suggested assisted trial sequence

The exact cadence is runtime-gated, but the current direction is:

### Activation

- trial starts;
- payment method captured;
- business identity confirmed;
- provisioning/binding authorized.

### Initial onboarding

- client account/access;
- business name/details;
- Google Business Profile OAuth;
- review flow / QR/link;
- baseline captured;
- social connections only if needed for current first-value path.

### First value

A concrete output must happen quickly, e.g.:

- first review request ready/sent;
- Google reviews syncing;
- first reply configured/produced;
- first reusable review content produced where applicable.

The product should not depend on the founder manually doing recurring work forever.

---

## 8. API / automation policy

Climbo public documentation confirms some API surfaces, but runtime capability must be verified before architecture depends on them.

Do not assume:

- every UI setting has a write API;
- API access is free/unlimited;
- idempotency is safe;
- exact lookup/uniqueness semantics exist;
- webhooks solve identity/reconciliation automatically.

D1/ADR fail-closed rules remain authoritative.

Browser automation is maintenance debt and a last mile, not the default architecture.

---

## 9. Cost-to-complete

Before enabling SMS, WhatsApp, API plans, AI services or automation infrastructure, record:

- upfront cost;
- recurring cost;
- per-message/token/usage cost;
- required paid tier;
- free-tier limitation;
- maintenance cost;
- whether the first-value goal can be achieved without it.

No spend just because a feature exists.

---

## 10. Vendor claims

Do not convert vendor copy into Trovatemi claims without evidence.

Examples to avoid unless verified:

- `reply within 2 hours boosts SEO`;
- guaranteed Maps ranking;
- guaranteed AI citation/visibility;
- guaranteed customer acquisition.

---

## 11. What is outside the Lean delivery now

- multi-tier plans;
- GEO/website build as default;
- AI chatbot;
- custom customer portal;
- GHL;
- Reportly;
- review gating;
- 30 NFC deployment;
- seller/affiliate automation;
- recurring content service;
- browser automation production;
- RankEmpire bundling.

---

## 12. Current sequencing

```text
H0 master home
→ L2 real audit + lead
→ M0 measurement/privacy/compliance
→ C0.1B delivery/onboarding matrix
→ L3 report → trial → first value
→ L4 first real batch
```

Climbo work must serve this sequence, not reopen it.
