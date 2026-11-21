# Terra Ledger · "5 things to check on the RERA website before you book a flat"

Instagram carousel, 7 slides, 1080×1350 (4:5). Built with static-post-studio. Files: `slides.html` (source), `out/slide-01…07.png`, `out/contact-sheet.png`, `out/phone-preview.png`, `out/grid-preview.png`, `out/qa.json` (QA clean), `caption.md`, `brand-kit-terra-ledger.md`.

## Assumptions made (test run, no client available)
- Platform: Instagram feed, 4:5 so it can also be boosted. English only.
- RERA = **MahaRERA** (Pune is in Maharashtra). Checks are written generically ("search it on MahaRERA") rather than naming exact menu paths, which change.
- No logo file supplied: the brand name is set in type ("TERRA LEDGER · PUNE"); no symbol invented.
- "Navy and sand" turned into exact hex values (below). A muted clay is added as the single accent, used only for red flags (ties to "Terra"; easy to swap to navy if the client wants strictly two colours).
- No handle or website supplied, so none appears on the slides.

## Strategy
```
Objective:      Get first-time buyers to save the post and DM "RERA" (lead for the free checklist).
Audience:       First-time home buyers in Pune, 28–38. They know "RERA" exists but think it is a
                registration stamp, not something they can read themselves before paying a token.
Single message: Ten minutes on the MahaRERA website, before the token amount, protects you.
Insight:        Buyers trust the brochure and the sales office; the builder's own declarations
                (approvals, title, progress, complaints) are public on MahaRERA and almost nobody reads them.
Big idea:       "The RERA Ledger": the carousel is a ruled ledger page. Five empty boxes on the cover,
                one box ticked per slide, all five ticked on the close. The brand name (Ledger) becomes
                the format, and the format is literally a checklist, which is why people save it.
Format:         Carousel, 7 slides, 4:5. Listicle with a payoff: hook, 5 checks, recap + CTA.
Story arc:      01 Cover: numbered promise + 5 empty boxes
                02 Check 1 Registration & validity  (works alone as a "second cover")
                03 Check 2 Approved plans
                04 Check 3 Land title & encumbrances
                05 Check 4 Construction progress & bookings
                06 Check 5 Complaints & track record
                07 Recap ledger (5 ticked) + "DM us RERA" for the free checklist
```

## Concept routes
1. **The RERA Ledger (chosen)**, format-led: ruled ledger paper, entry numerals, checkbox progress tracker, red-flag row. Cover: "5 things to check on RERA, *before* you book a flat." Chosen because it is ownable (only Terra *Ledger* can own the ledger), calm, and it makes the post a checklist, which is what gets saved.
2. **Type-led "Before the token"**: big serif statements on sand/navy alternating fields, one question per slide, no motif. Cover: "Before you pay the token, *open one website.*" Calm and premium but less saveable and less ownable.
3. **Browser-window explainer**: each slide a stylised generic browser window with the relevant field highlighted. Cover: "Your builder already told you everything. *It's on MahaRERA.*" Most literal and instructive, but risks looking like an imitation of a government site and dates quickly when the portal changes.

## Design system
- **Canvas**: 1080×1350, 88 px margin (64 px safe), 8 px spacing unit. Fixed furniture: wordmark top-left, mono counter top-right, hairline rule at y=160.
- **Grid**: single left axis at 88 px; entry numeral and tracker on one row (y=216), kicker + headline + body block from y=448, red-flag panel pinned to the bottom margin.
- **Palette** (contrast checked with palette.py):
  - field sand `#EEE6D8` (~60%) · field-2 `#E4D8C4` (red-flag panel)
  - ink navy `#13254A` (12.18:1 on sand) · muted `#4C5670` (5.90:1)
  - dark navy `#13254A` field for cover and close · on-dark `#EEE6D8` (12.18:1) · on-dark muted `#C9C0AE` (8.36:1)
  - accent clay `#9A4226` (5.33:1 on sand), red flags only
- **Type**: Fraunces (display, opsz 144, regular + italic), Manrope (text), IBM Plex Mono (utility labels). Cover 116 px, H2 80 px, body 36 px, red-flag line 30 px, labels 24 px mono caps +14% tracking.
- **Emphasis device**: italic switch in Fraunces, 1–2 words per headline (registered, approved plan, land, keeping pace, buyers, before).
- **Layouts**: dark type-statement (cover, close) ↔ light ledger-entry (checks). Rhythm: navy, sand ×5, navy.
- **Motif**: ledger paper (48 px horizontal ruling at ~7%, double margin rule at the left edge) + checkboxes (empty on cover, progress tracker filling 1→5 on check slides, all ticked on close).
- **Finish**: fine grain (13% multiply on sand, 7% screen on navy). No photos, no stock, no icons except the small red-flag glyph.
- **Imagery**: none, type-led and graphic, as briefed.
- **Furniture**: wordmark in type; mono counter "NN / 07"; swipe cue on cover; CTA as a sand panel on navy; micro disclaimer on the last slide.

## Slide copy
**01 · Cover** (navy)
Kicker: FOR FIRST-TIME HOME BUYERS
Headline: 5 things to check on RERA, *before* you book a flat.
Sub: Ten minutes on the MahaRERA website, before you pay any token amount.
Graphic: five empty boxes 01–05. Footer: SAVE IT FOR YOUR SITE VISIT · SWIPE →

**02 · Check 1 of 5 · Registration**
Is the project *registered*, and still valid?
Search it on MahaRERA. Note the registration number and the completion date the builder declared.
Red flag: No registration number on the ad or brochure, or a registration that has lapsed.

**03 · Check 2 of 5 · Approved plans**
Does your flat exist on the *approved plan*?
Open the sanctioned plan and commencement certificate. Match your wing, floor and carpet area.
Red flag: Your floor isn't in the sanctioned plan yet, and you're told "approval is coming".

**04 · Check 3 of 5 · Land title**
Who owns the *land*, and is it mortgaged?
Read the legal title report and the encumbrances the builder has declared: loans, liens, disputes.
Red flag: A court case or a loan on the land that the sales team never mentioned.

**05 · Check 4 of 5 · Progress**
Is construction *keeping pace* with the promise?
Read the latest quarterly progress update: work completed, and flats booked versus total.
Red flag: Updates that stopped coming, or progress stuck at the same stage for quarters.

**06 · Check 5 of 5 · Track record**
What do other *buyers* say on record?
Look up complaints and orders against this project, and the builder's other projects.
Red flag: Repeated complaints about delays, or older projects that are still unfinished.

**07 · Close** (navy)
Kicker: YOUR RERA LEDGER
Tick all five *before* you pay a token.
☑ Registration is valid · ☑ Flat is on the approved plan · ☑ Land title is clear · ☑ Progress is on track · ☑ Complaints are checked
CTA panel: DM us *"RERA"*. We'll send you our free one-page checklist to take on your next site visit.
Micro: General information, not legal advice. Always verify on the official MahaRERA website before you pay.

## Caption, hashtags, alt text
See `caption.md`.

## QA log
- Pass 1: cover headline broke the italic phrase across lines; check-slide headlines left orphans ("valid?"); body at 25ch ran to 4 lines; slide 7 had 5 content sizes (QA warning).
- Pass 2: headlines broken by meaning; body widened; single checkbox replaced with a 5-box progress tracker (stronger swipe logic, more graphic); CTA size unified with H2. QA clean.
- Pass 3: removed remaining body orphans on cover and slide 6. QA clean; phone preview legible at 390 px; grid crop keeps the headline and boxes.

## Open items for the client
1. **Logo**: supply the logo file if they want it instead of the typeset wordmark.
2. **MahaRERA agent registration number**: if Terra Ledger is registered as a MahaRERA real-estate agent, add the number to the slide 7 footer (MahaRERA expects it on agents' promotions). Not added because it was not supplied.
3. **Handle / website** for the close slide, if wanted.
4. **The free checklist itself** must exist before posting, plus an auto-reply or a person to answer "RERA" DMs.
5. **Legal review**: have their legal/RERA person confirm the five checks match the current MahaRERA portal (section names like quarterly progress updates and declared encumbrances).
6. **Accent**: confirm the clay red-flag colour, or swap `--accent` to navy in `slides.html` for a strict two-colour version.

## Image prompts
None. The post is type-led and graphic by brief.
