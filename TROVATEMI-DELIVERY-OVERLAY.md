# TROVATEMI — Lean delivery overlay

## Status

**Current Trovatemi overlay — 2026-09-03.**

Questo repository contiene evidence Climbo, coaching, materiali storici e vecchi asset Trovatemi. Questa pagina definisce **come interpretarli oggi**.

Governance owner: `soliwkr/trovatemi-os`.

Current operational context: `docs/00-governance/11-current-lean-context.md` nella governance Trovatemi.

Quando una fonte in questo repo entra in conflitto con il current Lean context, **la fonte resta evidence/history ma non diventa policy Trovatemi**.

---

## 1. Product freeze

Trovatemi Lean = un solo prodotto:

- **€149/mese**;
- **21-day trial**;
- €0 durante trial;
- payment method required;
- per location.

Da considerare storici/non operativi:

- €100/€300/€500;
- ★/★★/★★★ tiers;
- €199/€399;
- coupon founder 100% forever;
- 3-tier delivery playbook.

---

## 2. Architecture

```text
acquisition → D1/audit → report → activation/onboarding → Climbo
```

- D1 = pre-sale lead/lifecycle/consent/attribution/provenance;
- Climbo = downstream delivery after activation/binding;
- prospect pre-sale != Climbo contact;
- no GHL / parallel CRM / new customer portal.

---

## 3. Climbo role

Climbo is the delivery layer, not the customer-facing category.

Current plan baseline:

- Reviews ON;
- Requests ON;
- Reminders ON;
- AI Sentiment ON;
- Review Filter OFF;
- Google-first flow;
- SEO Agent ON where verified;
- Social Agent ON where operational/tested;
- Facebook / Instagram / TikTok where actually supported/tested;
- Performance ON;
- Website / Widgets / GEO / AI Chat out of Lean MVP unless explicitly reopened.

Current portal naming: `app.trovatemi.it`.

Legacy `os.trovatemi.it` references are historical.

---

## 4. Review policy

Trovatemi uses **neutral and universal solicitation**.

Do not implement review gating.

Specifically, do not adopt a vendor pattern that routes:

```text
satisfied → public review
unsatisfied → private feedback
```

for the purpose of suppressing negative public reviews.

No review incentives.

---

## 5. Vendor claims policy

Vendor/coaching claims are evidence, not automatically Trovatemi claims.

Do not publish unverified causal claims such as:

- `reply within 2 hours → SEO naturally improves`;
- guaranteed Maps ranking;
- guaranteed AI visibility;
- guaranteed customer growth.

Trovatemi only claims what is supported by runtime/evidence.

---

## 6. Onboarding direction

Evidence from Climbo training supports a strong onboarding principle:

> **Onboarding is not optional.**

Current Trovatemi direction:

- preconfigure what can be preconfigured;
- client performs OAuth/consent where necessary;
- assisted activation is acceptable;
- standardized human touchpoint is acceptable;
- recurring delivery should be automated where possible;
- recurring manual service is not the core product.

C0.1B classification:

`PRESET / API / UI-AUTO / CLIENTE / UMANO / ELIMINARE`

Implementation rule:

> **API where possible; browser automation only as last mile after a real dry-run proves the gap.**

---

## 7. Report / outbound

**Reportly is out.**

Do not use Reportly as current inbound/outbound/report architecture.

Trovatemi Audit Engine owns:

- evidence;
- cohort/benchmark;
- deterministic/versioned scoring;
- five private answers;
- report explanation;
- activation CTA.

LLM may explain. It must not invent score or Maps ranking.

---

## 8. Physical kit

Current Lean rule:

- Starter Review Kit digital during trial;
- physical Welcome Kit only after first successful payment;
- target €25 all-in;
- hard cap €40 all-in including shipping.

Legacy instructions to buy 30 NFC units or stock inventory before validation are historical and not current authorization.

NFC/QR remain valid mechanisms where compliant and useful, but not the current build gate.

---

## 9. Current delivery sequencing

```text
H0 master home
→ L2 real audit + lead
→ M0 measurement/privacy/compliance
→ C0.1B delivery/onboarding deep gate
→ L3 report → trial → first value
→ L4 first real batch
```

Do not use old playbooks to jump directly into seller scaling, NFC volume, automation or multi-tier fulfillment.

---

## 10. How to read this repo

### Evidence / keep

- provider UI observations;
- API documentation and endpoint evidence;
- coaching principles;
- onboarding sequence evidence;
- supported feature observations;
- cost observations;
- historical experiments.

### Do not import automatically

- pricing;
- tiers;
- coupon strategy;
- review gating;
- unverified SEO claims;
- old portal/domain naming;
- old prospect batch size;
- old physical-kit timing;
- old sales scripts that conflict with current messaging.

---

## 11. Cost-to-complete

Before adding API plans, browser automation, SMS/WhatsApp balance, paid AI services or new integrations, disclose:

1. upfront cost;
2. recurring cost;
3. mandatory downstream cost;
4. free/incomplete limitations;
5. whether the goal fails without paying.

No recurring tool spend just to make the architecture prettier.
