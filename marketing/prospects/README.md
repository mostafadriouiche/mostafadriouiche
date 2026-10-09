# Prospect list: accounting firms in Casablanca

Built 2026-10-09. Every email address comes from the firm's **own website**: no guessed addresses, no bought lists, no scraped directories. The `source_url` column shows where each one was found.

| File | Contents |
|---|---|
| `cabinets-casablanca.csv` | 39 firms with a published email, ready to import into lemlist / Brevo (UTF-8) |
| `cabinets-casablanca-sans-email.csv` | 5 firms with a website but no published email: use phone or contact form |

## Columns
- `prenom`, `accroche`: **empty on purpose.** Fill them before sending (partner's first name from the firm's "équipe" page or LinkedIn, plus one real detail for the first line of email 1). Without them, open with "Bonjour," and drop the accroche line.
- `priority`
  - **A** (23): small/medium fiduciaires and cabinets doing bookkeeping and VAT returns for TPE/PME. Best fit for Owl: start here.
  - **B** (10): established expert-comptable firms, more audit/advisory work.
  - **C** (6): large audit firms, or domiciliation/multi-service businesses. Lower fit.
- `confidence`
  - **High**: firm-domain address shown consistently on its site.
  - **Medium**: Gmail address, older page, or a second address also shown.
  - **Low**: conflicting spellings or unclear Casablanca presence (see `notes`).

## Before you send
1. **Verify every address** with a verification tool (ZeroBounce, NeverBounce or Bouncer). Some pages are 1–3 years old. Remove anything marked invalid, and keep bounces under 2%.
2. Send AMDE Anfa **or** Création Entreprise Casablanca, not both (same group).
3. Start with priority A, 10–20 per day per mailbox, from your secondary domain (see `../email-strategy.md`).
4. Keep this file as your record of where each address came from, and remove anyone who replies "non" or "stop".

## Growing the list
Same rule: only addresses on the firm's own site. Next sources: OEC Maroc and OPCA member lists, Telecontact.ma (find names, then visit each site), and other cities (Rabat, Tanger, Marrakech, Agadir).
