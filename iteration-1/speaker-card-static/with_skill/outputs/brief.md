# Pixel Chai Vol. 4: speaker announcement (single static)

Final: `out/slide-01.png` (1080×1350, 4:5) · source: `slides.html` · QA: clean (3 families, 4 sizes, nothing outside safe zone)
Review sheets: `out/phone-preview.png`, `out/grid-preview.png`, `out/contact-sheet.png`

## Assumptions (made without the client, change if wrong)
- Platform: Instagram feed, 4:5. No logo file, so "Pixel Chai" is set in type (Fraunces Soft), not drawn as a mark.
- CTA: RSVP through the link in bio. Entry price and capacity are not stated, so the post doesn't mention them.
- "Fintech startup" stays unnamed, as given. "Principal Product Designer" is shown exactly as supplied.

## Open items (check before posting)
1. **Date/day mismatch.** 7 Dec is a **Monday** in 2026 (Sunday in 2025, Tuesday in 2027). It isn't a Saturday in any nearby year. The post shows "Sat 7 Dec" as briefed. Confirm whether it should be **Sat 5 Dec** or **Mon 7 Dec**, then edit one line in `slides.html` (`<dt>When</dt>`).
2. Get Ananya's OK on her title and the "fintech startup" wording. Ask whether she wants the company named.
3. Real Pixel Chai logo (SVG/PNG), if one exists. It would replace the wordmark top-left at about 30 px cap height.
4. RSVP link (Luma/Google Form, etc.) for the bio. Also check the venue name spelling: "The Courtyard, Indiranagar".

## Strategy
```
Objective:      get Bangalore designers to RSVP for Vol. 4, and make the speaker feel worth showing up for
Audience:       product/UX/visual designers in Bangalore, junior to lead; many have shipped or used UPI/fintech flows
Single message: Ananya Rao is confirmed. She's talking about designing trust in money apps, Sat 7 Dec, 5 PM, Indiranagar.
Insight:        in a money app, trust gets won or lost on one small screen: the confirmation receipt. Every designer
                in the room has designed that "it went through" moment or nervously waited for it.
Big idea:       "Speaker confirmed": the announcement IS a transaction receipt. The talk's subject becomes the
                post's format, and the chai-stall bill ("Thank you · Visit again") makes it Pixel Chai's own.
Format:         single static, 4:5. One focal object (the receipt), three text levels (name > talk > details).
```

## Concept routes
1. **Recommended: "Speaker confirmed" receipt (format-led, type only).** A milky-chai receipt on a decoction-brown table. It has a ginger success tick, the name set as the "amount", the talk below a perforation, and the event details as transaction rows. "Your seat: Pending · RSVP →" is the CTA. It ends with the classic Indian bill sign-off "Thank you · Visit again" and has a chai-glass ring stain in the corner.
   Why: the joke is one designers get immediately. It's specific to this talk and this meetup, and it does the job without a photo. A competitor couldn't post it unchanged.
2. **Type statement.** A huge serif headline "Designing *trust* in money apps." fills the frame, and the speaker sits in the four corners (name, role, date, venue). It's calm and editorial, but it could announce any talk at any meetup.
3. **Loading state.** A chai glass drawn as a progress ring, "Confirming your speaker… ✓ Ananya Rao". It's playful, but the metaphor needs a second look and edges toward cute.

## Art direction (system)
- **Canvas** 1080×1350, margin 88 px, 8 px unit. Receipt is inset 88 px left and right, top 152 px, height 1010 px, rotated −1.2° with a soft ambient drop shadow. Furniture rows sit at 72 px from the top and bottom.
- **Palette** (60-30-10):
  - field: decoction brown `#3A2418`, with a warm lamp glow at top-left
  - paper: milky chai `#F3E4CC`
  - ink: `#2A1A10` (13.4:1)
  - muted: `#6B5040` (5.9:1)
  - accent: ginger `#A84718` (4.7:1 on paper), used only for the tick, "Speaker confirmed" and the seat/RSVP line
  - on-field: `#F3E4CC` (11.6:1) and `#C9AE90` (6.9:1)
- **Type** (3 families total):
  - Fraunces (Soft axis) for the name (120/0.95, −3%) and talk (72/1.02)
  - Inter Tight for the role and footer lines (30)
  - JetBrains Mono for labels and receipt rows (26, caps +14%)
  - Emphasis device: italic switch, used once, on *trust*.
- **Layout**: a borrowed-format "receipt" object centred on the field. Reading order runs Z: wordmark → tick + name → talk → details → CTA.
- **Motif**: the receipt itself (perforations with punched notches, zig-zag torn edge) plus a faint chai-glass ring. Future speaker cards reuse the receipt, and other formats can carry the ring.
- **Finish**: fine grain on the field, paper fibre on the receipt. No gradients on type, no stickers.
- **Imagery**: none. Type-led as briefed. If her photo arrives later, add a small circular B&W portrait "stamp" (≈160 px) beside the name. Don't redo the layout around a big portrait.
- **Furniture**: "Pixel Chai" wordmark top-left, "Vol. 04 · Bangalore" mono top-right, tagline bottom-left, "Link in bio" CTA bottom-right.

## Copy on the post
- Pixel Chai · Vol. 04 · Bangalore
- ✓ SPEAKER CONFIRMED
- **Ananya Rao**
- Principal Product Designer, fintech startup
- TALK: Designing *trust* in money apps
- WHEN: Sat 7 Dec · 5:00 PM
- WHERE: The Courtyard, Indiranagar
- YOUR SEAT: Pending · RSVP →
- THANK YOU · VISIT AGAIN
- A design meetup, over chai. · Link in bio

## Caption
```
Speaker confirmed. ✓

For Pixel Chai Vol. 4, Ananya Rao (Principal Product Designer at a fintech startup) is talking about designing trust in money apps. That covers the screens where people decide whether to believe your app with their money, from the first "Pay" tap to the second they see it went through.

Bring your questions. We'll bring the chai.

🗓 Sat, 7 Dec · 5 PM
📍 The Courtyard, Indiranagar

Your seat is still pending. RSVP through the link in bio.

#PixelChai #DesignMeetup #BangaloreDesign #ProductDesign #UXDesign #FintechDesign #DesignCommunity
```
(Change the day in the caption as well once open item 1 is settled.)

## Alt text
Speaker announcement for Pixel Chai Vol. 4, designed as a cream paper receipt on a dark chai-brown background. It reads: "Speaker confirmed: Ananya Rao, Principal Product Designer, fintech startup. Talk: Designing trust in money apps. When: Saturday 7 December, 5 PM. Where: The Courtyard, Indiranagar. Your seat: pending, RSVP." The receipt ends with "Thank you, visit again" and has a faint tea-glass ring in one corner.

## Image prompts
None needed (type-led).
