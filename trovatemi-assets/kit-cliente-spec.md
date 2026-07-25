# Kit Cliente — Spec Ripetibile (trovatemi.it)

> Il "template d'ordine" del kit di benvenuto. Ogni cliente ha lo **stesso identico kit**; cambiano solo **2 variabili**. Standardizzare = produrre un kit in mezza giornata invece che ogni volta da zero.

---

## Le uniche 2 (+1) variabili per cliente

1. **`{LOGO_CLIENTE}`** — PNG a sfondo trasparente (glielo chiedo in onboarding)
2. **`{QR_CLIENTE}`** — QR del suo review link, generato da Climbo
3. *(testo)* **`{NOME_ATTIVITÀ}`** — per l'inserto stand

Tutto il resto è fisso. Nessuna riprogettazione.

---

## Bill of Materials — cosa contiene ogni kit

| Articolo | Q.tà | Personalizzazione | Chi lo produce |
|----------|------|-------------------|----------------|
| Stand da banco (acrilico A6 + inserto + sticker NFC) | 1-2 | Inserto con `{NOME_ATTIVITÀ}` + `{QR_CLIENTE}` | 🖨️ EcoTank (inserto) + 🛒 acrilico |
| NFC card encodate col review link | 2-3 | Encoding col link cliente | ⚪ vuote + NFC Tools |
| Sticker NFC di scorta (pre-encodati) | 3-5 | Encoding col link cliente | ⚪ rotolo + NFC Tools |
| QR kiosk laminato | 1 | `{QR_CLIENTE}` | 🖨️ EcoTank + plastifica |
| Cartoncino istruzioni staff | 1 | **Nessuna** (neutro, riusabile) | 🖨️ EcoTank |

**Premium (piani ★★ / ★★★):** aggiungi card PVC stampate col `{LOGO_CLIENTE}` (dal fornitore locale) al posto delle bianche.

Costo vivo/kit: **~€10-15** (base) · ~€20-30 (premium con card stampate).

---

## Il flusso di produzione (checklist, ~mezza giornata)

**In onboarding (raccolgo le variabili):**
- [ ] Chiedo `{LOGO_CLIENTE}` (PNG trasparente)
- [ ] Prendo il review link da Climbo → genero `{QR_CLIENTE}`
- [ ] Annoto `{NOME_ATTIVITÀ}`

**Produzione:**
- [ ] Inserisco `{NOME_ATTIVITÀ}` + `{QR_CLIENTE}` nel template `stand-insert-a6-template.html`
- [ ] Stampo inserto + QR kiosk + cartoncino staff (EcoTank, cartoncino 250-300 g)
- [ ] Ritaglio (cutting mat) e plastifico QR kiosk + staff card
- [ ] Assemblo gli stand: acrilico + inserto + **sticker NFC dietro** (encodato)
- [ ] Encodo card + sticker col review link (NFC Tools) e **testo** ogni pezzo
- [ ] *(premium)* Ordino/ritiro le card stampate `{LOGO_CLIENTE}` dal fornitore

**Consegna:**
- [ ] Consegno il kit alla **call di onboarding** (giorno 1-2)
- [ ] Mostro allo staff il cartoncino "recensione in 5 secondi"

---

## Perché standardizzarlo

- **Velocità onboarding = retention** (il repo lo ripete): kit pronto in 24-48h dalla firma.
- **Scalabilità:** da 1 a 10 clienti senza reinventare nulla — cambio solo logo + QR.
- **Rapporto fornitore:** gli mando sempre lo **stesso ordine-tipo**, lui esegue veloce.

---

## Ordine-tipo da mandare al fornitore (premium)

```
Cliente: {NOME_ATTIVITÀ}
- 10 × card PVC CR80 opache, stampa fronte con {LOGO_CLIENTE} (file allegato, tracciati)
  → NFC lo inserisco/encodo io
- 50 × adesivi domed oro {LOGO_CLIENTE} 35mm  [opzionale, per card/stand nere]
Consegna richiesta: entro 48h
```

*Correlati: `brief-fornitore.md` · `stand-insert-a6-template.html` · `staff-instructions-a6-template.html`*
