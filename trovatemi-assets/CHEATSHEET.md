# TROVATEMI.IT — CHEATSHEET OPERATIVA

> Una pagina che riassume tutto quello di cui abbiamo parlato: modello, cosa comprare, come personalizzare, come produrre, come vendere. Il resto sono i file di dettaglio in `trovatemi-assets/` e `wiki/`.

---

## 1. Il modello (in 4 righe)

- Paghi **Climbo €99/mese** (clienti illimitati) → incassi **€100/300/500** per cliente.
- Break-even al **1° cliente**, profitto dal 2°.
- Il cliente vede **TROVATEMI.IT**, non sa che esiste Climbo.
- Vendi **il contatore recensioni che sale**, non un software.

## 2. La regola n°1 + il funnel

> **≥1 contatto al giorno.** Sempre. Se procrastini con tool/dashboard, ti manca un contatto, non uno strumento.

```
30 contatti → 10 trial gratis → 3 clienti/mese → dopo 12 mesi ≈ €3.600 MRR
```

## 3. Cosa comprare — primo ordine (~€90-130)

| Articolo | Q.tà | Note |
|----------|------|------|
| Card NFC custom/nere (card-eroe da demo) | 5-10 | Ordinata stampata / doming |
| Card PVC bianche NTAG215 (funzionali) | 10 | Le encodi tu |
| Sticker NFC NTAG215 (rotolo) | 50 | Consumabile nascosto |
| Espositori acrilici A6 | 3-5 | Per stand fai-da-te |
| Cartoncino 250-300g A4 | 100 | Per l'EcoTank |
| Ricarica Balance Climbo | — | ~$20 |

→ Dettaglio + query di ricerca: `checklist-acquisti.md`

## 4. I 3 tipi di NFC + i chip

| Tipo | Ruolo | Lo mostri? |
|------|-------|-----------|
| Sticker a rotolo | Consumabile nascosto (dietro card/stand) | ❌ |
| Card PVC bianca | Funzionale (staff/scorta) | ⚠️ dietro le quinte |
| Card custom/nera + stand | Card-eroe / prop premium | ✅ è il WOW |

**Chip:** NTAG **213** (URL, economico) · **215** (URL+vCard, standard) · **216** (solo più memoria). **424 DNA** = crittografia/anti-clone → **non ti serve**. Per un link recensione, il 213/215 basta.

## 5. Personalizzare le card NERE (regole d'oro)

- ⚠️ **PVC + laser = NO** → rilascia cloro tossico, rovina la macchina.
- ⚠️ **Mai forare/incidere in profondità** → dentro c'è la bobina NFC.

| Metodo | Resa | Note |
|--------|------|------|
| **Doming** (adesivo resina 3D oro) | ⭐⭐⭐ **La migliore** | Su PVC/stand nero: premium, sicuro, economico, no attrezzatura |
| Incisione laser | ⭐⭐⭐ | **Solo su METALLO** (no PVC). Mono argento |
| Stampa UV | ⭐⭐ | Bianco/colore coprente su nero |
| Vinile ritagliato | ⭐ | DIY, piatto |

→ File design: `nfc-card-black-edition.html` (card) · `nfc-stand-black-76mm.html` (stand) · versione solo-logo per doming da fare al bisogno.

## 6. Chi produce cosa

| Cosa | Produzione |
|------|-----------|
| Inserti stand, flyer, QR, cartoncino staff | 🖨️ **EcoTank** (carta, no PVC rigido) |
| Card-eroe, card nere, doming | 🏭 **Fornitore** (stampa/UV/doming) |
| Card bianche funzionali | ⚪ **Vuote + NFC Tools** (encoding) |

> La tua EcoTank NON stampa card PVC rigide. Stampante per tessere (€800+) solo a volume.

## 7. Il kit di benvenuto = scatola + settimana

**Fisico:** 1-2 stand da banco (nome cliente + QR) · 2-3 NFC card encodate · sticker di scorta · QR kiosk laminato · cartoncino istruzioni staff.
**Digitale:** Welcome Email · pannello os.trovatemi.it · prima campagna riattivazione · screenshot "contatore zero" · call giorno 14 fissata.

→ Template d'ordine ripetibile (logo + QR = uniche variabili): `kit-cliente-spec.md`

## 8. Prospecting (come trovo clienti)

- **Walk-in** (mar-gio): «Ho un regalo» → tap NFC → gap col concorrente → 5 recensioni gratis.
- **Flyer leaflet-drop** (brandizzato trovatemi.it): `flyer-a5-leaflet-drop.html`
- **Gruppi Facebook**: post + DM pronti in `facebook-groups-copy.md`

## 9. Compliance Google (aprile 2026) — usala come selling point

- Chiedi a **tutti**, non solo ai contenti (no gating).
- **Mai** incentivi (sconti/premi per recensioni).
- Niente copioni imposti, niente richiesta nomi dipendenti.
- QR/NFC stand = OK (il cliente sceglie di scansionare).

## 10. Non distrarti (adesso)

NON servono: dashboard CF Workers, webhook, Zapier, API, stampante tessere, mini-laser, piani ★★/★★★. Si costruiscono **quando hai i clienti**. La leva è uscire e parlare.

## 11. Fornitori

- **Locali** (Formia/Fondi/Terracina): `fornitori-locali.md` → chiedi doming + card + adesivi.
- **Brief da consegnare**: `brief-fornitore.md`
- **Doming online** (brand one-time): Centroresina, Sticker.it, StickerPrinting, FlyerAlarm.

---

## 📁 Indice di tutti gli asset

| File | Cos'è |
|------|-------|
| `PLAYBOOK.md` | Mappa Climbo ↔ offerta trovatemi.it |
| `playbook-personale.md` | Il tuo manuale operativo (regola n°1, funnel, script, obiezioni) |
| `wiki/operations/materiali-vendita.md` | Guida completa acquisti + kit |
| `checklist-acquisti.md` | Primo ordine con query di ricerca |
| `nfc-card-template.html` | Card-eroe fronte/retro (fornitore NFC) |
| `nfc-card-black-edition.html` + `.svg` | Card nera mono (laser/UV/vinile/doming) |
| `nfc-stand-black-76mm.html` + `.svg` | Stand nero verticale mono |
| `stand-insert-a6-template.html` | Inserto stand (EcoTank) |
| `flyer-a5-leaflet-drop.html` | Flyer prospecting (EcoTank) |
| `staff-instructions-a6-template.html` | Cartoncino staff (kit, conforme Google) |
| `facebook-groups-copy.md` | Post + script DM |
| `scoreboard-attivita-a4.html` | Scoreboard funnel €3k (muro) |
| `tracker-attivita.xlsx` | Tracker con formule (Google Sheets) |
| `brief-fornitore.md` | Scheda preventivo fornitore |
| `kit-cliente-spec.md` | Template d'ordine kit cliente |
| `fornitori-locali.md` | Lead fornitori zona Formia/Fondi/Terracina |

---

*Se dubiti su cosa fare: guarda lo scoreboard. Una casella vuota = un titolare che non hai ancora incontrato. Esci. ★*
