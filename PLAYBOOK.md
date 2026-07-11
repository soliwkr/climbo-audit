# TROVATEMI.IT × CLIMBO — Playbook Operativo
**v1 · luglio 2026 · uso interno Chris Fioravanti**

> Questo documento risponde a una domanda sola: **come uso Climbo per costruire e far girare trovatemi.it?**
> Non è una review del software. È la mappa che collega ogni feature di Climbo a ogni livello dell'offerta.

---

## INDICE

1. [Cos'è Climbo davvero](#1-cosè-climbo-davvero)
2. [Mappa completa delle funzionalità](#2-mappa-completa-delle-funzionalità)
3. [Come Climbo alimenta i 3 livelli dell'offerta](#3-come-climbo-alimenta-i-3-livelli-dellofferta)
4. [Workflow operativo — dal cliente firmato al flywheel attivo](#4-workflow-operativo)
5. [Funzionalità avanzate e opportunità non ovvie](#5-funzionalità-avanzate-e-opportunità-non-ovvie)
6. [Gap, limitazioni e workaround](#6-gap-limitazioni-e-workaround)
7. [Climbo vs QuickSuite — cosa impariamo dal competitor](#7-climbo-vs-quicksuite)
8. [Il setup minimo per partire con Ivan](#8-il-setup-minimo-per-partire-con-ivan)

---

## 1. Cos'è Climbo davvero

Climbo non è un tool per recensioni. È una **piattaforma SaaS white-label** che tu rivendi come tuo software ai tuoi clienti. Il punto chiave: il cliente finale non sa che esiste Climbo — vede TROVATEMI.IT.

**Il modello economico:**
- Tu paghi Climbo: **€99/mese fisso** (clienti illimitati, tutte le funzionalità)
- Tu incassi dai clienti: €100 / €300 / €500 al mese
- Margine dal primo cliente: **break-even a 1 cliente ★, profitto netto da 2 in poi**

**Il motore centrale — Review Marketing Flywheel™:**
```
Recensione entra
  → AI risponde (parole chiave locali → Maps sale)
  → AI pubblica post social (GBP + Instagram + Facebook)
  → GEO Agent aggiorna sito/blog (citazione su ChatGPT/Perplexity)
  → profilo più forte → più visibilità → più clienti → più recensioni
```
Questo gira in automatico. Il cliente non tocca niente.

---

## 2. Mappa completa delle funzionalità

### Navigazione principale app (my.climbo.com)
| Sezione | Cosa fa | Usato in trovatemi.it |
|---------|---------|----------------------|
| **Clients** | Lista tutti i clienti, stato piano, location, billing | Ogni cliente = un'attività locale |
| **Plans** | Crei i piani abbonamento con prezzi, features, Stripe | I tuoi 3 livelli ★ ★★ ★★★ |
| **Brand** | White-label: nome, logo, dominio, colori, font | TROVATEMI.IT già configurato |
| **Sales** | Dashboard pagamenti, grafici MRR (7/30/90/365 giorni) | Monitoraggio ricavi mensili |
| **Settings** | Tutta la configurazione avanzata | Vedi dettaglio sotto |
| **Support** | Link al supporto Climbo | Non visibile al cliente finale |

### Settings — Finance
| Sotto-sezione | Cosa fa |
|--------------|---------|
| **Coupons** | Crea sconti (usa qui il coupon FONDATORE 100% forever) |
| **Payouts** | Configura come ricevi i pagamenti |
| **Methods** | Metodi di pagamento accettati (carta + SEPA) |
| **Accounting** | Documenti, balance report, riconciliazione, tasse |
| **Affiliate** | Programma affiliati per chi porta clienti |
| **Profile** | Profilo agenzia |

### Settings — General
| Sotto-sezione | Cosa fa |
|--------------|---------|
| **Account** | Nome, email, password — accesso Stripe integrato |
| **Team** | Aggiungi collaboratori (tu sei Owner) |
| **Emails / Templates** | Email automatiche ai clienti (Welcome, onboarding, ecc.) |
| **API** | Chiave API per integrazioni custom (Agency ID: `6a489ecc0d62c86c88b2d3e1`) |
| **Zapier** | Automazioni no-code (Climbo → Notion, Google Sheets, ecc.) |
| **Webhooks** | Notifiche real-time su pagamenti, aggiornamenti clienti |
| **Balance** | Credito pre-pagato per SMS/WhatsApp/Email/AI tokens |

### Brand (già configurato)
```
Brand Name:  TROVATEMI.IT ★
Domain:      os.trovatemi.it   ← sottodominio già attivo
Powered By:  https://os.trovatemi.it
```
**Azioni disponibili nel Brand:**
- AI Brand (nome AI assistant personalizzato)
- AI Logo
- SEO Agent (attiva/configura risposte recensioni con keyword)
- Social Agent (post automatici da recensioni)
- GEO Agent (sito/blog per AI search)
- Prompt sentence (istruzioni base per gli agenti AI)
- Powered By Logo + URL
- Colori, Font, Radius
- Free Trial Banner
- AI Chatbot per clienti
- Custom Code (JS/CSS aggiuntivo)
- Log In page preview + Embed Code

### Balance — costi operativi
| Canale | Costo |
|--------|-------|
| SMS (IT/EU) | ~€0.05–0.10 per messaggio |
| WhatsApp | $0.03 per messaggio |
| Email | $0.00 (gratuito) |
| AI Tokens | $6.60 per 1M token |

**Saldo attuale: $5.00** — ricarica prima di attivare il primo cliente con SMS/WhatsApp.

---

## 3. Come Climbo alimenta i 3 livelli dell'offerta

### ★ TROVATO — €100/mese
**Cosa prometti al cliente:** contatore recensioni che sale, profilo Google sistemato.

**Cosa gira su Climbo:**
1. **Onboarding cliente** → crei il profilo in Clients, assegni il piano ★ TROVATO
2. **Setup review collection:**
   - QR code generato da Climbo → stampi/incolla in loco
   - Link diretto alla pagina recensione Google
   - SMS/WhatsApp automatici post-visita (configurati una volta)
3. **SEO Agent attivo** → ogni recensione riceve risposta AI con nome attività + città + servizio
4. **Il cliente accede al suo pannello** su `os.trovatemi.it` → vede solo il contatore
5. **Tu non tocchi più niente** fino al giorno 7 (screenshot WhatsApp) e giorno 14 (call)

**Effort tuo dopo setup:** quasi zero. Il flywheel gira da solo.

---

### ★★ VISIBILE — €300/mese
**Cosa aggiungi:** GBP vivo (post, foto, video settimanali).

**Cosa gira su Climbo (in più rispetto a ★):**
1. **Social Agent attivo** → ogni recensione diventa post su GBP + Instagram + Facebook automaticamente
2. **Calendario 40 hook** (li produci tu con il cliente) → caricati su Climbo → distribuiti prima su GBP, poi social
3. **Templates email personalizzate** → comunicazioni col cliente branded TROVATEMI.IT
4. **Dashboard Sales** → mostri al cliente l'andamento del profilo

**Differenza operativa:** hai bisogno che il cliente (o la sua videomaker) produca contenuti. Tu dai il calendario e il flusso. Climbo distribuisce.

---

### ★★★ INEVITABILE — €500/mese + esclusiva
**Cosa aggiungi:** sito rank-and-rent, GEO Agent, presidio AI search.

**Cosa gira su Climbo (in più rispetto a ★★):**
1. **GEO Agent attivo** → costruisce e aggiorna automaticamente il sito/blog del cliente con recensioni + dati locali → citazione su ChatGPT/Perplexity/Google AI Overview
2. **Tre posizioni SERP pulite:**
   - Map Pack → GBP reale del cliente (gestito da Climbo)
   - Organico → portale rank-and-rent (tuo, esterno a Climbo)
   - Sito cliente → alimentato dal GEO Agent
3. **Reporting completo** → contatore recensioni + lead del portale + citazioni AI → tutto verificabile dal cliente

**Il flywheel completo:**
```
Portale ranka → lead → cliente chiude → Climbo chiede recensione
→ recensione entra → SEO Agent risponde (Maps sale)
→ Social Agent posta (GBP attivo)
→ GEO Agent aggiorna sito (AI search citazione)
→ portale converte di più → più lead → valore difendibile
```

---

## 4. Workflow operativo

### Nuovo cliente firmato → flywheel attivo in 24h

**Giorno 0 — Firma patto**
- [ ] Patto Fondatore firmato
- [ ] Stripe: attiva abbonamento con coupon FONDATORE
- [ ] Climbo: crea cliente in `#/clients`
- [ ] Assegna piano corretto
- [ ] Invia Welcome Email (template già pronto in Climbo)
- [ ] Fissa Call 1 con data e ora — **senza questa il cliente è un lead, non un cliente**

**Giorno 1-2 — Call 1 onboarding (REGISTRATA)**
- [ ] Accesso GBP del cliente → collegamento a Climbo
- [ ] Setup review collection: QR code + SMS/WhatsApp automatici
- [ ] Consegna targhetta NFC
- [ ] Attiva SEO Agent (+ Social Agent se livello ★★+)
- [ ] Mostra al cliente il suo pannello su `os.trovatemi.it`
- [ ] Stabilisci il "contatore zero" — screenshot del numero attuale di recensioni

**Giorno 7 — Tocco proattivo**
- [ ] Screenshot prime recensioni entrate → WhatsApp al cliente senza che lo chieda
- [ ] Richiede 2 minuti. Vale oro in fiducia.

**Giorno 14 — Call 2**
- [ ] Contatore prima/dopo (già visibile)
- [ ] Aggiustamento flusso se necessario
- [ ] Le domande del cliente = materiale per il Playbook futuro

**Giorno 90 — Raccolto**
- [ ] Contatore salito → chiedi le 3 cose del patto
- [ ] "Chi conosci che è messo come eri messo tu?" → primo nome caldo

---

## 5. Funzionalità avanzate e opportunità non ovvie

### Affiliate Program
Climbo ha un sistema affiliati nativo (`#/settings/affiliate`). Puoi creare affiliati che portano clienti e ricevono commissione. **Opportunità:** i fondatori stessi diventano affiliati dopo il giorno 90 — il referral è già previsto nel patto, ma puoi tracciarlo in Climbo automaticamente invece che a mano.

### API + Zapier + Webhooks
- **API Key** già disponibile (Agency ID: `6a489ecc0d62c86c88b2d3e1`)
- **Documentazione:** `climbo.readme.io/reference/add-client`
- **Zapier:** già configurabile — connetti Climbo a Google Sheets per tracciare i contatori, o a Notion per il tuo CRM interno
- **Webhooks:** notifiche real-time su pagamenti e aggiornamenti → utile per automatizzare il WhatsApp del giorno 7

**Automazione concreta suggerita:**
```
Webhook "nuovo cliente aggiunto" 
  → Google Sheet (log)
  → reminder automatico a 7 giorni
  → WhatsApp API (screenshot contatore)
```

### Templates email
In `#/settings/templates` ci sono già template attivi:
- Welcome Email Business Owners
- Welcome Email Agency Members

**Personalizza subito:** cambia il tono con il linguaggio TROVATEMI.IT (niente tecnico, niente gergo). La welcome email è il primo touchpoint dopo la firma.

### Coupons
Usa i coupon Climbo per il meccanismo fondatore:
- Crea coupon `FONDATORE` → 100% sconto → durata: forever
- Il cliente entra a listino pieno → applichi il coupon → fattura mostra €100 barrato → €0
- Quando diventa pagante: rimuovi il coupon, non toccare altro

### Balance pre-pagato
Il sistema balance copre i costi di SMS, WhatsApp e AI tokens. **Attenzione:** con $5 attuali puoi gestire forse 50-100 messaggi SMS. Ricarica prima di attivare il primo cliente su SMS/WhatsApp. Per i fondatori che vuoi tenere in costo zero, considera di usare solo Email (gratuita) + QR/NFC fisico per la raccolta.

### 21 piattaforme recensioni
Climbo supporta Google, Tripadvisor, Yelp, Booking.com e altre 17. Per i clienti locali italiani (Ivan = agenzia immobiliare):
- **Google** → priorità assoluta
- **Immobiliare.it / Casa.it** → verifica se supportati (non nel dato corrente)
- **Trustpilot** → alternativa per professioni

### Employee Reward System
Feature citata nel sito pubblico ma non esplorata nell'app (richiede cliente attivo). Permette di incentivare i dipendenti dell'attività a raccogliere recensioni. Per Ivan (agenzia con agenti): ogni agente può avere il proprio QR → si traccia chi porta più recensioni → gamification interna.

### AI Chatbot per i clienti
Attivabile nel Brand settings. Il cliente finale accede via chat e può:
- Mandare campagne di richiesta recensione
- Aggiornare il GBP
- Aggiungere contatti
- Gestire template di risposta

**Implicazione:** il cliente non deve imparare una dashboard. Parla con una chat. Riduce il churn da "non capisco il tool".

---

## 6. Gap, limitazioni e workaround

### Cosa non funziona ancora nel tuo account
Le seguenti sezioni restituiscono 404 — sono probabilmente legate a funzionalità che si attivano con clienti attivi o con upgrade di piano:

| Sezione | Status | Workaround |
|---------|--------|------------|
| `#/reviews` | 404 | Visibile nel pannello del singolo cliente |
| `#/ai-agents` | 404 | Si configura in Brand settings |
| `#/content` | 404 | Probabilmente attivo con clienti connessi |
| `#/analytics` | 404 | Dashboard Sales attiva (grafici MRR) |
| `#/tools` | 404 | Probabilmente funzionalità extra |
| `#/upgrade` | 404 | Non applicabile al tuo piano |
| `#/settings/white-label` | 404 | Il white-label si gestisce in Brand |

### Fatturazione elettronica (SDI)
**PROBLEMA CRITICO:** Stripe non emette fatture elettroniche italiane via SDI. Climbo gestisce i pagamenti via Stripe ma **non risolve l'obbligo di fatturazione elettronica** verso i clienti italiani.

**Soluzione:** Prima del primo cliente pagante, integra Stripe con Fatture in Cloud (o equivalente). Non è urgente per i fondatori (a €0), ma non puoi aspettare il giorno prima del primo incasso reale.

### SEPA Addebito Diretto
Citato nel tuo brandsheet come priorità per ridurre il churn da carta scaduta. Verifica se Climbo supporta SEPA nel checkout clienti o se devi gestirlo via Stripe direttamente.

### Rank-and-rent (portale) — fuori da Climbo
Il portale rank-and-rent (`agenziaimmobiliareformia.it` e simili) è **esterno a Climbo** — è il tuo asset, non suo. Climbo gestisce la parte GBP/recensioni del cliente; il portale è WordPress/HTML tuo. I due si integrano nel flywheel ma sono sistemi separati.

### "os.trovatemi.it" vs "trovatemi.it"
Il dominio white-label dell'app è già configurato su `os.trovatemi.it`. Il cliente accede lì. Il sito pubblico sarà `trovatemi.it`. Assicurati che i due non si sovrappongano nelle comunicazioni: `os.trovatemi.it` è il **pannello operativo** del cliente, `trovatemi.it` è la **landing di vendita**.

---

## 7. Climbo vs QuickSuite — cosa impariamo dal competitor

QuickSuite (Australia) ha un modello simile: software white-label per agenzie locali. L'analisi serve a capire cosa funziona nel mercato anglofono per replicarlo nel posizionamento italiano.

**Differenze chiave:**

| Dimensione | Climbo (motore) | QuickSuite (competitor) | Implicazione per trovatemi.it |
|------------|-----------------|------------------------|-------------------------------|
| Posizionamento | "Start Your AI Business" — vende l'opportunità all'agenzia | Più orientato al risultato finale per il cliente locale | trovatemi.it è già corretto: vende il risultato (il telefono che squilla), non il software |
| Pricing | €99/mese fisso, clienti illimitati | Struttura a tier non chiara dall'analisi | Vantaggio: margini crescono linearmente con ogni cliente |
| AI focus | 3 agenti (SEO, Social, GEO) + chatbot | Non esplicitato nell'analisi | Climbo è più avanzato tecnologicamente |
| Target vendita | Agenzie/marketer globali | Apparentemente simile | trovatemi.it si differenzia per il focus locale italiano e il rapporto diretto "Chris risponde" |

**La lezione principale da QuickSuite:** hanno una sezione "How It Works" molto chiara e step-by-step. Nel tuo one-pager e nella landing, mostrare i passaggi concreti (setup → prima recensione → contatore sale) è più efficace di descrivere il sistema.

---

## 8. Il setup minimo per partire con Ivan

Questo è l'unico checklist che conta adesso. Tutto il resto è distrazione.

### Climbo — da fare prima della call con Ivan
- [ ] **Crea piano "★ TROVATO"** in `#/plans` → €100/mese, clienti illimitati
- [ ] **Crea coupon "FONDATORE"** in `#/settings` → 100% per sempre
- [ ] **Personalizza Welcome Email** in `#/settings/templates` → tono TROVATEMI.IT
- [ ] **Ricarica balance** → almeno $20 per gestire SMS/WhatsApp dei primi clienti
- [ ] **Configura SMTP** in Brand → email da `@trovatemi.it` invece che default Climbo
- [ ] **Testa il flusso completo** con il Demo Client già presente → simula l'esperienza del cliente

### Il momento WOW (demo con Ivan)
Il double-tap NFC apre la pagina recensione Google di Ivan direttamente. Climbo non tocca questo momento — è NFC fisico. Climbo entra dopo: una volta che Ivan vuole procedere, gli mostri il pannello `os.trovatemi.it` e come funziona il flusso automatico.

### Cosa NON configurare adesso
- Webhook custom
- Zapier integrations
- API
- Affiliate program
- Fatturazione elettronica SDI (urgente solo prima del primo pagante)
- Piani ★★ e ★★★ (costruiscili quando hai il primo cliente ★)

---

## APPENDICE — La frase che spiega Climbo a Ivan (senza dirgli che esiste Climbo)

> «Quando qualcuno ti lascia una recensione, il sistema risponde automaticamente con le parole giuste per Google — nome del tuo studio, città, tipo di servizio. Poi quella stessa recensione diventa un post sul tuo profilo Google. Tutto questo gira da solo. Tu non tocchi niente. Io guardo che funzioni. Il contatore lo vedi tu, in tempo reale, dal tuo telefono.»

Niente tecnico. Niente Climbo. Niente flywheel. Il cliente compra il contatore che sale.

---

*Playbook v1 — si aggiorna dopo la Call 1 con Ivan.*
*★ TROVATEMI.IT — Ti facciamo trovare dove conta.*
