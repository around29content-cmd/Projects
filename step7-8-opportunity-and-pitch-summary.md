# Steps 7 and 8: Google Ads market opportunity research and sales pitch intelligence

Date: 8 October 2026. Scope: the 19 Tier 1 and Tier 2 prospects plus Cunningsmiles Implant Experts (P-13). Inputs: Step 6 enrichment (verified contact and service facts), website text and HTML saved 8 Oct 2026, and a landing-page fact extraction over that HTML. Outputs in the sheet: GOOGLE_ADS_OPPORTUNITY (Step 7, 20 rows x 14 columns) and SALES_PITCH_INTELLIGENCE (Step 8, 20 rows x 13 columns, readiness summary at rows 23-28). Local copies: google_ads_market_opportunity.csv, sales_pitch_intelligence.csv, step7-8-opportunity-pitch.py.

## Rules applied

- Keyword themes are intent patterns (service + city, near me, emergency, cost, quote, appointment, product). No search volumes are asserted anywhere.
- Landing-page issues are split into a verified-facts column (page weight, viewport tag, tel links, form elements, booking widgets, CTA wording, pages returning 404) and an analyst-reading column. Mobile rendering was not tested; only the presence of a viewport tag is reported.
- Campaign recommendations are reasoned from the business model; no competitor advertising data was used.
- Every business problem is prefixed "Potential problem" because none has been confirmed with the business.
- Sales hooks name only what the business actually publishes (services, offers, booking tools, service area, pricing).

## Outreach readiness

| Status | Records | Tier 1 |
|---|---|---|
| Ready to Contact | 13 | 5 |
| Contact After Research | 6 | 2 |
| Missing Critical Information | 1 | 0 |
| Do Not Contact Yet | 0 | 0 |

Ready to Contact: Prime Care Dental Indy, AA Roofing and Decking, VIP Pest Solutions, Affordable Junk Removal, Superior Coatings NW, American Tree Excavation, Workhub Tulsa, Alignments Northwest, Zellers Group, Northwest Eco Clean, La Jolla Grooming, Clean & Clear by Cliff, Wheeler-Sonoma Printers.

Contact After Research (reason): Cunning Dental Group (current owner unknown, possible new management), Orion Optical (no owner named; on-file email is a third-party agency), Axle Surgeons of Seattle (no person named; national-brand relationship unconfirmed), Trans Landscaping (no person named), Ocean View Lodging (phone conflict; operator unknown), Calvary Cemetery (executive director role in transition).

Missing Critical Information: Cunningsmiles Implant Experts (site not live, nothing verifiable).

## Time-sensitive hooks

- Zellers Group: Medicare Annual Enrollment runs 15 Oct to 7 Dec; the agency has four Medicare-specialist agents.
- Workhub Tulsa: six private suites pre-leasing for 1 November 2026 with published pricing and a tour form.
- Clean & Clear by Cliff: Christmas-light hanging season (October to December) with Housecall Pro booking already live.
- American Tree Excavation: storm season; site advertises 24-hour emergency service but names no service area.

## Common landing-page findings (verifiable)

- 7 of 19 sites return 404 on /about and /about-us; Workhub Tulsa also returns 404 on /contact and /contact-us.
- Only 3 of 19 home pages contain a native form element; most rely on buttons that open forms, external schedulers or a separate contact page.
- 6 sites embed a booking or scheduling tool (Orion Optical, Workhub Tulsa, Ocean View Lodging, Northwest Eco Clean, Clean & Clear by Cliff via Housecall Pro, Affordable Junk Removal via its own form); the rest are call-or-form only.
- Cunning Dental Group's home page HTML is about 950 KB, Affordable Junk Removal's about 505 KB, Orion Optical's about 380 KB: page-weight risks for paid traffic.
- 5 sites publish no service-area cities (AA Roofing, American Tree, Alignments Northwest, La Jolla Grooming, Axle Surgeons has a map only), which blocks confident geo-targeting until confirmed on the call.
- Wheeler-Sonoma has no contact form or quote path despite an About page that mentions online ordering.

## What was not done

No outreach was sent. No search volumes, cost-per-click or competitor ad data were used. Mobile rendering, page speed and Google Business Profile status were not tested. Internal record I-01 was excluded.
