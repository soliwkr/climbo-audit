# Skool — Climbo Accelerator AI Agency
**Audit · luglio 2026**

> **Nota accesso:** Il token Skool configurato appartiene a un account non iscritto alla community. I dati di post, classroom e leaderboard richiedono il cookie `auth_token` dell'account Google iscritto. Per completare l'audit dei post: apri skool.com loggato con Google → DevTools → Application → Cookies → copia `auth_token` → `skool-pp-cli auth set-token`.

---

## Dati community (estratti via API pubblica)

| Campo | Valore |
|-------|--------|
| **Nome** | Climbo Accelerator – AI Agency |
| **Slug** | `climbo` |
| **Membri** | 901 |
| **Creata** | 26 novembre 2025 |
| **Prezzo** | "Soon €27/month" (attualmente libera con abbonamento Climbo?) |
| **Owner** | Giacomo Chinellato — Co-founder di Climbo.com |
| **Colore brand** | #009E5D |
| **Tab attive** | Community · Classroom · Calendar · Map |

**Descrizione pubblica:**
> "Launch a white-label AI Agency in days, powered by the Review Marketing Flywheel for local businesses."

**Landing page description (per i nuovi iscritti):**
> "Soon €27/month. For new and established agency owners who want to sell a white-label AI system to local businesses and create predictable monthly recurring revenue. Practical strategies, real operator stories..."

---

## Link ufficiali dalla community

| Label | URL |
|-------|-----|
| New? Apply Here 🚀 | https://climbo.com/apply |
| Features Roadmap 🗺️ | https://roadmap.climbo.com |
| Community Rules 🤝 | https://www.skool.com/climbo/community-rules-please-read-before-posting |

---

## Survey nuovi iscritti (domande di accesso)
1. Email address
2. WhatsApp number (con prefisso internazionale)
3. *(ulteriori domande non estratte)*

La community richiede un'application — non è accesso libero. Questo segnala un posizionamento curato e un'audience di qualità.

---

## Video pinned (dalla LP della community)
`https://youtu.be/sIGOLZ1kFAQ` — da analizzare nel modulo YouTube.

---

## Opportunità per trovatemi.it

1. **La community è il prodotto di supporto** — 901 agenzie che usano Climbo si scambiano tattiche, case study, win. Per Christian: leggere i post = capire i pain point reali degli utenti → adattare il pitch per Ivan.

2. **€27/mese in arrivo** — La community diventerà a pagamento. Opportunità: partecipare attivamente adesso (gratis) per costruire autorità prima che si chiuda o diventi costosa.

3. **Il Classroom di Skool** — Contiene probabilmente il corso "come vendere Climbo" che Giacomo ha costruito. Da esplorare con login corretto: ogni modulo = playbook pronto da adattare per il mercato italiano.

4. **Pattern replicabile** — Se Climbo ha 901 agenzie che usano il suo software + una community che le supporta, il modello è validato. trovatemi.it non sta inventando niente — sta localizzando in Italia qualcosa che funziona globalmente.

---

## Prossimo step Skool
Per completare l'audit:
1. Vai su [skool.com/climbo](https://www.skool.com/climbo) dal browser con il tuo Google account
2. DevTools (F12) → Application → Cookies → `www.skool.com` → copia `auth_token`
3. Aggiorna `~/.config/skool-pp-cli/config.toml` con il nuovo `access_token`
4. Riesegui: `skool-pp-cli sync climbo && skool-pp-cli posts top --community climbo --json`
