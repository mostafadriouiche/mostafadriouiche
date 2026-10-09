# Owl email strategy for accounting firms

Goal: book demos with accounting firms (*cabinets comptables*) and turn them into paying Owl customers.

## The key decision: two email tracks

You want professional emails with animation and video. That works, but **only after the prospect has replied**. Sent cold, a designed HTML email with a GIF and a video link lands in spam or the "Promotions" tab, and it also burns your domain's reputation.

| | Track A: Cold outreach | Track B: Nurture / demo follow-up |
|---|---|---|
| **Who** | Firms that don't know you yet | Firms that replied "yes", asked for the video, booked a demo, or signed up |
| **Format** | Plain text, ~80 words, no images, no link in email 1 | Designed HTML: logo, animated GIF, video thumbnail, button |
| **Goal** | Get a reply | Get a demo booked, then a pilot started |
| **Sent from** | A **secondary domain** (see setup) | Your main domain `thinkactionn.com` via an email-marketing tool |
| **Copy** | `emails/cold-sequence-fr.md` | `emails/nurture-sequence-fr.md` + `emails/templates/owl-video-email.html` |

The bridge between the two is email 2 of the cold sequence: *"Je peux vous envoyer une vidéo de 2 minutes ?"*. Whoever says yes moves to Track B and gets the animated video email.

## About video in email

No major email client (Gmail, Outlook) plays a video inside the email. The standard professional approach:

1. Record the demo (2 minutes max): one real client file, from invoices to finished VAT return.
2. Host it on YouTube (unlisted), Vimeo or a page on thinkactionn.com.
3. In the email, put an **animated GIF** (3–5 seconds of the video, or the animation in `emails/assets/owl-flow.gif`) with a **▶ play button** on top. Clicking it opens the video page.
4. Outlook desktop shows only the **first frame** of a GIF, so the first frame must make sense on its own. The provided GIF does.

Keep each GIF under ~1 MB, and host images on your site or in the email tool. Never attach them.

## Sending setup (do this before the first cold email)

### 1. Protect `thinkactionn.com`
Your Namecheap mailbox on `thinkactionn.com` is for customers, invoices and replies. **Do not send cold emails from it.** Spam complaints on cold email would hit the domain your customers depend on. Namecheap Private Email also has hourly and daily sending caps, and it isn't built for campaigns.

### 2. Buy 1–2 secondary domains (Namecheap, ~10 $/year each)
Use names that are obviously yours, for example `getowl-compta.com`, `thinkaction-owl.com` or `owl-cabinet.com`. Redirect each one to thinkactionn.com.

Create **2 mailboxes per domain** for real people, e.g. `mostafa@` and `contact@` (each with a name, photo and signature). You can host them on Namecheap Private Email, Google Workspace or Microsoft 365. Many French accounting firms use Microsoft 365 or OVH, so Microsoft 365 mailboxes tend to land better with them.

### 3. DNS records (Namecheap → Domain List → Manage → Advanced DNS) on **every** domain, including thinkactionn.com
| Type | Host | Value |
|---|---|---|
| TXT (SPF) | `@` | `v=spf1 include:spf.privateemail.com ~all` (Namecheap Private Email; add `include:` for your sending tool too, e.g. Brevo) |
| TXT (DKIM) | provided by Private Email / your tool | copy from the Private Email dashboard → *DKIM*, and from your sending tool |
| TXT (DMARC) | `_dmarc` | `v=DMARC1; p=none; rua=mailto:dmarc@thinkactionn.com` |

Keep only one SPF record per domain; merge the `include:`s into it.

### 4. Warm up for 3–4 weeks
- Weeks 1–2: warm-up only (built into lemlist / Instantly), plus a few real emails to people who will answer.
- Weeks 3–4: 5–10 cold emails per mailbox per day, then rise slowly to 20–25 max.
- 2 domains × 2 mailboxes × 20/day ≈ **80 emails/day**, which is plenty for a niche like accounting firms.

### 5. Tools
| Job | Recommended | Why |
|---|---|---|
| Cold sequences (Track A) | **lemlist** (French company) or Instantly | Warm-up, mailbox rotation, auto-stop on reply |
| Rich HTML emails (Track B) | **Brevo** (French, GDPR-native) or Mailchimp | Drag-and-drop editor, GIFs, sends from thinkactionn.com |
| List verification | Dropcontact (French), ZeroBounce, NeverBounce | Keep bounces under 2% |
| Booking demos | Calendly or Cal.com | One link in Track B |

**Turn OFF open tracking and click tracking in the cold tool.** Measure replies, not opens.

## Building the list
Sources of accounting firms (*cabinets d'expertise comptable*):
- National professional directory (in France: the Ordre des experts-comptables annuaire; in Morocco: the OEC Maroc; adapt to your country)
- Google Maps: "expert-comptable [ville]", "cabinet comptable [ville]"
- LinkedIn Sales Navigator: title *Expert-comptable associé*, company size 2–50

Start with **200 firms in one city or region**. Write down per firm: partner name, email, city, size, and one personal detail (recent LinkedIn post, a specialty such as *BTP*, *restauration*, *e-commerce*, hiring a collaborator). That detail powers the first line of email 1.

## Legal (check for your country)
- **France (CNIL):** B2B email prospecting is allowed without prior consent **if the message relates to the recipient's profession** (Owl for an accountant qualifies), the sender is identified, and there's an easy opt-out. Every email in this kit includes an opt-out line and your company identity.
- **Other countries** (Morocco, Algeria, Tunisia, Belgium…): rules differ. Check your national data-protection authority before sending.
- Honor every "non" / "stop" immediately and keep a do-not-contact list.

## Calendar: align with VAT deadlines
Accounting firms are buried right before VAT deadlines and receptive right **after**. Send cold emails in the 1–2 weeks after a monthly/quarterly VAT deadline, with Tuesday–Thursday, 9–11 h, as the best slots. Avoid the last week before a deadline and the *saison fiscale* peak.

## Metrics and stop-loss
| Metric | Target | If below |
|---|---|---|
| Bounce rate | < 2% | Pause, re-verify the list |
| Reply rate (cold) | 5–10% | After 300 sends under 1%: change the targeting or the angle, not the volume |
| Positive replies → demo | 30–50% | Speed up replies (answer within the hour) |
| Demo → pilot | 30%+ | Improve the demo: use one of *their* files |
| Spam complaints | < 0.1% | Pause, cut volume, review copy |

## 30-day launch plan
| Week | Do |
|---|---|
| 1 | Fill the TODOs in `.agents/product-marketing.md`. Buy secondary domains, set DNS, start warm-up. Record the 2-minute demo video. |
| 2 | Build and verify the first list (200 firms, one region). Set up Brevo with the HTML template and the nurture sequence. |
| 3 | Start cold sequence at 5–10/day per mailbox. Reply to every answer within the hour. |
| 4 | Review replies, keep the best-performing first line, then scale to 20/day per mailbox and a second region. |

## Next skills to use
- `prospecting`: build and qualify the list
- `sales-enablement`: demo script and objection handling (security, price, "on a déjà un logiciel")
- `offers`: design the pilot offer (e.g. 30 days, 10 client files, free setup)
- `copywriting`: landing page that the video email links to
