# Prospect lists: accounting firms in Morocco

Built 2026-10-09. Every email address comes from the firm's **own website**: no guessed addresses, no bought lists, no scraped directories. The `source_url` column shows where each one was found.

| File | Firms | Contents |
|---|---|---|
| `cabinets-maroc-tous.csv` | 66 | All cities in one file: **import this one** into lemlist / Brevo |
| `cabinets-casablanca.csv` | 40 | Casablanca |
| `cabinets-rabat.csv` | 12 | Rabat and Témara |
| `cabinets-marrakech.csv` | 14 | Marrakech |
| `cabinets-maroc-sans-email.csv` | 11 | Firms with a website but no published email: use phone or contact form |

All files are UTF-8 with the same columns. Use the `city` column to filter by city in your sending tool.

## Columns
- `prenom`, `accroche`: mostly **empty on purpose.** Fill them before sending (partner's first name from the firm's "équipe" page or LinkedIn, plus one real detail for the first line of email 1). Without them, open with "Bonjour," and drop the accroche line.
- `priority`
  - **A** (40): small/medium fiduciaires and cabinets doing bookkeeping and VAT returns for TPE/PME. Best fit for Owl: start here.
  - **B** (17): established expert-comptable firms, more audit/advisory work.
  - **C** (9): large audit firms, foreign-headquartered firms, or company-formation businesses. Lower fit.
- `confidence`
  - **High** (35): firm-domain address shown consistently on its site.
  - **Medium** (26): Gmail address, older page, partner's own address, or a second address also shown.
  - **Low** (5): conflicting details or unclear fit (see `notes`).

## Before you send
1. **Verify every address** with a verification tool (ZeroBounce, NeverBounce or Bouncer). Some pages are 1–3 years old. Remove anything marked invalid, and keep bounces under 2%.
2. Send AMDE Anfa **or** Création Entreprise Casablanca, not both (same group).
3. TS Partners (Rabat) has no generic inbox. The address is a partner's own, published on the firm's site, so write to him personally (`prenom` is filled).
4. 13 addresses are Gmail: the firm publishes them, but they are often the owner's personal inbox. Write to them with extra care.
5. Start with priority A, 10–20 per day per mailbox, from your secondary domain (see `../email-strategy.md`).
6. Keep these files as your record of where each address came from, and remove anyone who replies "non" or "stop".

## Growing the list
Same rule: only addresses on the firm's own site. Next sources: OEC Maroc and OPCA member lists, Telecontact.ma (find names, then visit each site), and other cities (Tanger, Agadir, Fès, Kénitra).
