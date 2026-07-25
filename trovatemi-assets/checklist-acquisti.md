# Checklist d'Acquisto — Materiali Vendita trovatemi.it

> Lista operativa per il **primo ordine**. Sono **query di ricerca** (non link a prodotti singoli, che scadono): scegli il venditore col miglior rapporto prezzo/recensioni. Prezzi indicativi IT/EU, lug 2026. Specifiche da verificare **sempre**.

---

## ✅ Primo ordine consigliato (Fase 0)

| # | Articolo | Q.tà | Prezzo | Dove |
|---|----------|------|--------|------|
| 1 | Sticker NFC NTAG215 (rotolo/bulk) | 50 | €15-20 | Amazon / AliExpress |
| 2 | NFC card PVC bianche NTAG215 | 10 | €15-25 | Amazon |
| 3 | Card NFC premium (hero, stampata) | 5-10 | €30-50 | fornitore NFC custom / Vistaprint |
| 4 | Espositori acrilici A6 inclinati | 3-5 | €12-20 | Amazon |
| 5 | Cartoncino 250-300g A4 (stampa in casa) | 100 fogli | €8-12 | Amazon / cartoleria |
| 6 | Buste plastificazione A6 (opz.) | 100 | €8-10 | Amazon |
| **App** | NFC Tools (encoding) | — | **Gratis** | App Store / Play Store |

**Totale primo ordine: ~€90-130** (di cui €30-50 una tantum per la card hero). Balance Climbo a $20 a parte.

---

## Dettaglio + query di ricerca

### 1. Sticker NFC NTAG215 (il consumabile nascosto)
- **Cerca:** `NTAG215 stickers` · `NFC adesivi NTAG215 25mm`
- Amazon IT → `https://www.amazon.it/s?k=NTAG215+adesivi`
- AliExpress → `https://www.aliexpress.com/wholesale?SearchText=NTAG215+sticker`
- **Specifiche da verificare:** chip **NTAG215** (non NTAG213 se vuoi lo standard), **13.56 MHz**, ø **25mm**, adesivo sul retro. Confezione 50/100 pz.
- **Uso:** incollati **dietro** card e inserti stand. Ne bastano 50 per partire.

### 2. NFC card PVC bianche NTAG215 (funzionali / staff)
- **Cerca:** `NTAG215 PVC card blank` · `NFC card bianche NTAG215`
- Amazon IT → `https://www.amazon.it/s?k=NFC+card+NTAG215+bianche`
- **Specifiche:** formato tessera **CR80 (85.6×54mm)**, **NTAG215**, PVC rigido bianco. Confezione 10.
- **Uso:** le encodi tu col review link del cliente → per lo staff / da tavolo. **Non** sono la card da demo.

### 3. Card NFC premium — la HERO da demo (ordinata stampata)
- **Due strade:**
  - **A) Stampa custom** col tuo design (`nfc-card-template.html`): cerca `custom printed NFC card` / `NFC business card custom print` → invii il PDF, ricevi le card stampate full-color.
  - **B) Card nera/metallo** già premium anche senza stampa: cerca `NFC card black matte NTAG215` / `metal NFC card`.
- Amazon IT → `https://www.amazon.it/s?k=NFC+card+personalizzata+stampa`
- **Nota:** è l'unico pezzo che **NON** stampi con l'EcoTank (PVC rigido). Ordine piccolo 5-10 pz, ti dura per sempre.

### 4. Espositori acrilici A6 inclinati (base degli stand)
- **Cerca:** `espositore acrilico A6 da banco inclinato` · `acrylic sign holder A6 slanted`
- Amazon IT → `https://www.amazon.it/s?k=espositore+acrilico+A6+inclinato`
- **Specifiche:** formato **A6 (105×148mm)**, inclinato/a L da banco, trasparente. Prendine 3-5.
- **Uso:** ci infili l'inserto stampato (`stand-insert-a6-template.html`) + sticker NFC dietro = stand completo ~€3.

### 5. Cartoncino 250-300g A4 (per la tua EcoTank)
- **Cerca:** `cartoncino 250g A4 stampa inkjet` · `carta 300g A4 bianca`
- Amazon IT → `https://www.amazon.it/s?k=cartoncino+250g+A4`
- **Uso:** inserti stand, cartoncini staff, flyer A5. Rigidità giusta per stare in piedi nell'acrilico.

### 6. Buste plastificazione A6 (opzionale ma consigliato)
- **Cerca:** `buste plastificazione A6` (serve una **plastificatrice**; se non ce l'hai → `pouches autoadesivi A6` senza macchina)
- Amazon IT → `https://www.amazon.it/s?k=buste+plastificazione+A6`
- **Uso:** proteggi cartoncino staff e QR kiosk. La **lamination non blocca l'NFC** (community).

---

## ⚠️ Da NON comprare adesso (te lo ricorda anche il PLAYBOOK)
- Coaster NFC, braccialetti NFC → solo in fase scaling (10+ clienti)
- Plastificatrice costosa → parti con pouches autoadesivi
- Ordini bulk da 100+ card custom → aspetta di avere volume

---

## Dopo l'ordine: encoding in 4 passi
1. Prendi il **review link** del cliente da Climbo
2. Apri **NFC Tools** → Write → Add a record → URL/URI
3. Incolla il link → avvicina il telefono allo sticker/card (1 secondo)
4. **Testa**: avvicina un altro telefono e verifica che apra la pagina

## Correlati
- [[operations/materiali-vendita]] — la guida completa con quantità per fase
- `trovatemi-assets/` — i template stampabili (card, stand, flyer, staff)
