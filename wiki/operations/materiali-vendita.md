# Materiali di Vendita — Lista Acquisti trovatemi.it

> **Riassunto in una riga:** cosa comprare per iniziare a vendere, con tipi di NFC spiegati, quantità per fase e costi indicativi. Il materiale fisico che chiude la vendita è la card NFC — non il software.

---
tags: [operations, sales, nfc, shopping-list, trovatemi]
sources: [PLAYBOOK, COACHING-SALES-DEEP-DIVE, features/nfc-cards]
last_updated: 2026-07-25
---

## La logica in 30 secondi

Nel modello trovatemi.it il momento che chiude la trattativa **non è il software** (Climbo, invisibile al cliente): è il **double-tap NFC** davanti al titolare — «Ho un regalo per te» → tap col telefono → si apre la pagina recensione Google in 2 secondi. Gli occhi si illuminano, e la vendita è di fatto chiusa.

Quindi gli acquisti si dividono in due famiglie:

1. **Il motore che gira** → software ricorrente (Climbo, dominio, balance).
2. **Il materiale fisico che vende** → NFC card, stand, sticker. **Qui va il 90% di quello che compri all'inizio.**

---

## Capire i 3 tipi di NFC (leggere prima di comprare)

Il chip da usare è sempre lo stesso — **NTAG215, 13.56 MHz** (compatibile con iPhone 7+ e tutti gli Android; per un semplice URL basterebbe anche NTAG213, ma NTAG215 è lo standard "senza pensieri"). Cambia il **formato fisico**:

| Tipo | Cos'è | A cosa serve | Lo mostri al cliente? |
|------|-------|--------------|----------------------|
| **Sticker a rotolo** (ø25mm) | Tag adesivi tondi, in rotoli da 50/100 | Il **consumabile nascosto**: lo incolli *dietro* una card o *dentro* uno stand. Economico ma brutto | ❌ Mai — sta nascosto |
| **NFC card PVC** (formato carta di credito) | Tessera rigida, stampabile fronte/retro col brand | La **targhetta demo / "regalo"** che tocchi col telefono davanti al titolare | ✅ Sì — è il WOW |
| **NFC stand da banco** | Espositore acrilico A6 inclinato + cartoncino "Recensiscici" + QR, con sticker NFC dietro | Quello che **lasci al cliente** sul bancone/reception | ✅ Sì — resta in loco |

> ⚠️ **Il dubbio più comune:** i **rotoli NON sono il prodotto di vendita.** Sono la scorta da nascondere dietro card e stand. Quello che porti in demo è la **card PVC**; quello che lasci è lo **stand**.

### Come è fatto uno "stand da banco" (fai-da-te, il più economico)

Non serve comprarlo pre-assemblato. Costruirlo costa meno e lo brandizzi:

```
Espositore acrilico A6 inclinato (porta-foto/porta-menu da bancone)  ~€2-4
  + cartoncino stampato "Lasciaci una recensione su Google" + QR      ~€0.20 (stampa)
  + 1 sticker NFC del rotolo incollato dietro                         ~€0.40
  = 1 stand completo brandizzato trovatemi.it                         ~€3-5
```

Lo sticker si scrive in 1 secondo con l'app **NFC Tools** (gratis, iOS/Android): Write → Add a Record → URL → incolli il review link del cliente da Climbo → avvicini il telefono. Fatto. La **lamination non interferisce** con l'NFC (confermato dalla community).

---

## 🎯 Fase 0 — Kit minimo per partire (comprare SUBITO)

Il necessario per fare le prime demo (Vittorio + walk-in nei bar/ristoranti della zona).

| Articolo | Quantità | Dove | Costo |
|----------|----------|------|-------|
| **NFC card PVC bianche NTAG215** (da scrivere tu) | 10 pz | Amazon | ~€15-25 |
| **Sticker NFC a rotolo NTAG215** (scorta consumabile) | 1 rotolo da 50 | Amazon/AliExpress | ~€15-20 |
| **Espositori acrilici A6 inclinati** (per stand fai-da-te) | 3 pz | Amazon | ~€10-15 |
| **App NFC Tools** | — | App Store / Play Store | **Gratis** |
| **Ricarica Balance Climbo** | fino a $20 | app Climbo | $20 |

**Totale materiale fisico Fase 0: ~€40-60.** Con questo fai demo illimitate e attivi i primi 2-3 clienti.

> 💡 **Trucco costi-zero sui fondatori:** per la raccolta recensioni usa **solo Email (gratis) + QR/NFC fisico**, così non consumi balance sugli SMS. Il balance a $20 ti copre gli SMS solo dei clienti che li vogliono davvero.

---

## 📦 Kit di benvenuto per cliente (per ogni cliente firmato)

Il PLAYBOOK prevede la targhetta NFC **inclusa nel piano come "kit di benvenuto"**. Per ogni cliente:

| Articolo | Quantità/cliente |
|----------|------------------|
| Stand da banco brandizzato (acrilico + cartoncino + sticker) | 1-2 (reception + cassa) |
| NFC card PVC (da lasciare allo staff / da tavolo) | 2-3 |
| Sticker NFC di scorta | 3-5 |

Costo vivo per kit: **~€10-15/cliente** — trascurabile su un abbonamento da €100-500/mese.

---

## 🔧 Il motore (software ricorrente)

| Voce | Nota | Costo |
|------|------|-------|
| **Climbo** | Unico costo fisso vero. Break-even già col 1° cliente ★ TROVATO a €100/mese | €99/mese |
| **Dominio trovatemi.it** | `os.trovatemi.it` (app) già configurato. Serve `trovatemi.it` come landing di vendita | ~€10-15/anno |
| **SMTP proprio** (`@trovatemi.it`) | Da configurare in Brand → email brandizzate invece del default Climbo | incluso/minimo |
| **Balance top-up** | SMS ~€0.05-0.10, WhatsApp $0.03, Email gratis, AI token $6.60/1M | a consumo |

---

## ⚠️ Prima del primo cliente PAGANTE (non ora, ma bloccante)

- **Fatture in Cloud** (o equivalente) — Stripe **non emette fattura elettronica italiana via SDI**. Non urgente coi fondatori a €0, ma bloccante il giorno del primo incasso reale. **~€8-25/mese.**

---

## 📈 Fase Scaling (solo con ~10 clienti attivi — NON adesso)

Ordine bulk da AliExpress/Alibaba (costo/pezzo crolla a €3-5 su card custom stampate):

- **100 sticker NFC** + **50 card PVC stampate custom** trovatemi.it
- **10-15 stand da banco**
- **Coaster NFC** (sottobicchieri con NFC + QR) — tattica Wayne per bar/ristoranti
- **Braccialetti NFC** per dipendenti — tattica Gurby (un NFC per dipendente, gamification raccolta recensioni)
- **warmupinbox.com** (~$15/inbox) — solo se parti con cold email a volume
- **Report/audit stampati** — per fiere di settore (Host Milano, TuttoFood, Sigep Rimini) e walk-in

---

## Riepilogo: la lista della spesa di OGGI

1. **10 NFC card PVC bianche NTAG215** → ~€20
2. **1 rotolo da 50 sticker NFC NTAG215** → ~€15
3. **3 espositori acrilici A6** (per gli stand fai-da-te) → ~€12
4. **App NFC Tools** → gratis
5. **Ricarica Balance Climbo a $20**
6. *(verifica di avere)* dominio `trovatemi.it` + Climbo €99/mese

**Investimento iniziale reale per iniziare a vendere: ~€50-60 di materiale**, oltre ai €99/mese di Climbo. Tutto il resto (Fatture in Cloud, coaster, warmup email, ordine bulk) arriva dopo, in ordine di quando serve davvero.

**Non stai comprando tecnologia — stai comprando il momento WOW.** Le card NFC sono ciò che fa illuminare gli occhi al titolare e chiude la trattativa.

---

## Correlati

- [[features/nfc-cards]] — come funzionano, encoding, placement
- [[sales/demo-script]] — come usare l'NFC nella demo (il double-tap che chiude)
- [[getting-started/first-client-checklist]] — setup NFC in onboarding
- [[features/balance-explained]] — costi SMS/WhatsApp/AI token
- PLAYBOOK.md — struttura offerta trovatemi.it e "kit di benvenuto"

## Fonti

- PLAYBOOK.md — targhetta NFC come kit di benvenuto, setup minimo, balance
- skool/COACHING-SALES-DEEP-DIVE.md §9 — materiali fisici NFC (Wayne, Jason Leigh, Gurby, Donna Marie), costi bulk €3-5/pz
- Skool: `bulk-nfc-enabled-business-flyer-idea`, `amazon-items-to-build-a-reputation-kit-on-a-budget`, `fortune-favours-the-brave`
