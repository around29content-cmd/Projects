# Around29 Google Ads Prospecting Project

Complete record of the Google Ads business-development pipeline built for Around29 Digital Media Solutions on the workbook "Around29 Google Ads Prospects". Work completed 8 October 2026. No outreach has been sent.

Workbook: https://docs.google.com/spreadsheets/d/11akD17izkmI2n7YuSvnyIvx3MrjRhC_JWtIml9WN5xg/edit

---

## 1. Purpose

Turn a raw list of 45 records (36 external prospects plus 9 internal Around29 properties) into a prioritised, evidence-backed Google Ads sales pipeline that management can act on: who to call, what to say, what is still missing, and what the opportunity is worth in search terms.

Around29 sells web, SEO and marketing services (Studio29, Search29 dashboard, Send29). The goal is a Google Ads upsell to businesses that fit paid search.

---

## 2. Standing rules

These applied to every step and every deliverable.

- **Raw tabs are never modified.** Prospects and Internal stay exactly as received. Every output lives in its own tab.
- **Nothing is invented.** No search volumes, traffic estimates, budgets, revenue figures or performance claims. Where a fact could not be established the value is `Not Found`, `Needs Verification` or `Not Available`.
- **Verified versus Inferred.** Verified = confirmed against the sheet, a live website, a directory or Search29. Inferred = Around29's reading of verified facts, and labelled as such.
- **First-party only for traffic.** No Similarweb, Semrush or similar estimates. Google Ads clicks, Search Console clicks and Business Profile views are not traffic.
- **Approval-gated.** Each step was delivered, reviewed and approved before the next began.
- **Every value traces to a source.** Evidence, source URLs and confidence ratings sit beside every researched value.

---

## 3. The pipeline, step by step

| Step | What was done | Output tab(s) | Key result |
|---|---|---|---|
| 1 Audit | Inventory of the raw workbook: columns, blanks, corrupt values, duplicates | (report only) | Prospects tab had 8 columns and no contact person, address, industry or budget; Internal tab had no header and two phone numbers stored as floats |
| 2 Cleaning | Standardised names, phones, emails, URLs; flagged quality issues; duplicate check | CLEANED_DATA, DATA_QUALITY_FLAGS | 29 valid phones, 6 emails, 0 contact names; two possible duplicate pairs flagged, none confirmed |
| 3 Classification | Industry and business-model classification per record | CLASSIFICATION | 15 consolidated industries; models such as emergency, high-ticket, recurring, subscription, B2B, nonprofit |
| 4 Google Ads fit | Industry fit, search intent, commercial intent, conversion path, geography, urgency per record | GOOGLE_ADS_FIT | Strongest intent: dental, pest, lodging, junk removal, roofing, tree, landscaping, painting, optometry, pet grooming |
| 5 Scoring | 100-point Google Ads Opportunity Score with tiers | SCORING_METHOD, SCORE_FACTOR_DETAIL, GOOGLE_ADS_OPPORTUNITY_SCORE | Tier 1: 7 prospects (85 to 100); Tier 2: 13 records (70 to 84) |
| 6 Enrichment | Decision-maker, role, address, service area, locations, services, phone and email verified from official sites and directories for Tier 1 and 2 | ENRICHED_PROSPECTS, MISSING_DATA_QUEUE | 20 records enriched; 130 field-level gaps queued with next actions; six source-data corrections found (recorded, not applied) |
| 7 Opportunity research | Keyword themes, geo targets, conversion goals, campaign types, verified landing-page facts per prospect | GOOGLE_ADS_OPPORTUNITY | Seven of 19 sites return 404 on About pages; only three home pages have a native form; five sites publish no service-area cities |
| 8 Pitch intelligence | Potential problem, sales hook, pitch angle, outreach readiness, contact to use | SALES_PITCH_INTELLIGENCE | 13 Ready to Contact, 6 Contact After Research, others Missing Critical Information or not enriched |
| 9 BD prioritisation | Blended BD score (opportunity, contactability, commercial potential, research confidence, personalisation) and four priorities | BD_PRIORITIZATION, BD_LISTS | Priority 1: 13; Priority 2: 6; Priority 3: 6; Priority 4: 20 (11 external, 9 internal) |
| 10 Final report | Executive report with sections 1 to 10 and final outputs A to E | step10-final-bd-report.md, web page | Home Services and Dental first; local, urgent, high-ticket models; 13 immediate calls |
| Master view | One-page management view, 12 columns per business, live summary blocks | MASTER MANAGEMENT VIEW | P1 10, P2 6, P3 8, P4 21; HIGH 15, MEDIUM 18, LOW 12 |
| Ads research | Google Ads and other-platform advertising status for all 36 prospects | ADS RESEARCH (plus master columns I, J, K) | 7 running Google Ads (2 through Around29), 4 on Meta, 9 untapped HIGH opportunities |
| Traffic research | First-party website traffic | WEBSITE TRAFFIC RESEARCH (plus master column L) | 4 sites verified via Search29 GA4; 41 Not Available |
| QA and explainer | Full QA of the master view; meeting explainer; deck | MASTER-MANAGEMENT-VIEW-Meeting-Explainer.docx, Around29-Google-Ads-BD-Report.pptx | All 45 scores, bands, priorities and research values reconcile; one blank cell fixed |

---

## 4. Scoring frameworks

### Step 5 Google Ads Opportunity Score (per record, 0 to 100)

Industry Google Ads Fit 15, Search Intent 15, Commercial Intent 15, Customer Value Potential 15, Conversion Potential 10, Geographic Targeting 10, Urgency 5, Business Scalability 5, Digital Readiness 5, Data Completeness 5. Tiers: Tier 1 85+, Tier 2 70 to 84, Tier 3 50 to 69, Tier 4 under 50.

### Management Opportunity Score (MASTER MANAGEMENT VIEW, 0 to 100)

Reuses the Step 5 factor ratings with management weights: Google Ads Fit 20 (Step 5 fit rescaled from 15), Commercial Intent 15, Customer Value 15, Search Demand 15, Conversion 10, Geographic 10, Urgency 5, Scalability 5, Digital Readiness 5. Data Completeness is deliberately dropped so a business does not look like a better opportunity because more is known about it. Bands: HIGH 75+, MEDIUM 50 to 74.9, LOW under 50.

### Contactability (master view)

- READY: phone verified on the official site plus a named person (Step 8 "Ready to Contact").
- ENRICH FIRST: attractive but a decision-maker, email or identity gap (Step 8 "Contact After Research", or not enriched but commercially plausible).
- NOT READY: internal record, LOW opportunity, dead site, or missing critical information.

### Priority rules (master view, first match wins)

1. Internal record = P4
2. HIGH and READY = P1
3. ENRICH FIRST and score 65+ = P2
4. MEDIUM and not NOT READY = P3
5. Everything else = P4

Overrides from the brief: Around Cricket and Ornamental Grasses forced to P4 (outside US market, weak fit); Cunningsmiles Implant Experts P4 (dead site, possible duplicate); Top Dollar Pawn held at P3 pending a Google Ads policy review.

### Why the master view shows 10 Contact Now and the BD report shows 13

BD_PRIORITIZATION ranks on a blended BD score, so three fully contactable businesses qualify as Priority 1 there. The master view requires a HIGH band (75+) for P1, so La Jolla Grooming Co (74.7), Clean & Clear by Cliff (74.0) and Wheeler-Sonoma Printers (69.0) sit at P3 in the master view. Both views are correct for their purpose. The explanation is a hover note on cell N3 of the master view, in Section 6 of the report, and in the Word explainer.

---

## 5. Headline findings

### Volume and priority

| Measure | Value |
|---|---|
| Records analysed | 45 (36 external, 9 internal) |
| Tier 1 / Tier 2 | 7 / 13 |
| Priority 1 (BD report) | 13 |
| Priority 2 / 3 / 4 | 6 / 6 / 20 |
| Master view P1 / P2 / P3 / P4 | 10 / 6 / 8 / 21 |
| HIGH / MEDIUM / LOW | 15 / 18 / 12 |

### Industry

Home Services (8 prospects, 7 in Contact Now, average Step 5 score 82.6) is the volume play. Dental (3, average 84.0) is the value play. Healthcare (optometry), Insurance, Real Estate (coworking) and Hospitality score HIGH but are one business each. Retail, Education and Other are dominated by store-visit models and nonprofits.

### Business models

Multi-location (92.0), emergency service (89.3), high-ticket service (82.8), lead generation (82.2) and subscription (80.8) score best. Nonprofits, events and associations (41.7) should be routed to Google Ad Grants, not paid search.

### Geography (Priority 1 and 2 only)

- Puget Sound, WA: 8, seven of them within Pierce and south King County. One market to learn once.
- California: 8, spread from the Central Coast to the Inland Empire. Eight separate local pitches.
- Tulsa, OK: 2. Indianapolis, IN: 1.

### Advertising activity (36 prospects)

| Finding | Count |
|---|---|
| Running Google Ads now (last 30 days) | 7 |
| No Google Ads evidence | 28 |
| Unknown (India-based, US-only lookup) | 1 |
| Paid Meta (Facebook) advertising | 4 |
| Google Ads tag on site, no ads found | 2 |
| TikTok or LinkedIn tags | 0 |

- **Segment A, untapped (9):** AA Roofing and Decking, VIP Pest Solutions, Superior Coatings NW, American Tree Excavation, Zellers Group, Alignments Northwest, Northwest Eco Clean, Trans Landscaping, Axle Surgeons of Seattle. Cleanest acquisition pitches.
- **Segment B, already on Google Ads (7):** Prime Care Dental Indy, Cunning Dental Group*, Affordable Junk Removal, Workhub Tulsa*, Orion Optical, Ocean View Lodging, Calvary Cemetery. Pitch optimisation and expansion. *Existing Around29-managed accounts.
- **Segment C, paid elsewhere (2):** Northwest Eco Clean, Around Cricket. Google Ads as an additional channel.

"No" means no evidence was found after reasonable research, not that the business never advertised.

### Website traffic (first-party only)

| Business | September 2026 | Confidence |
|---|---|---|
| Affordable Junk Removal | 838 sessions (62% paid search) | High |
| Cunning Dental Group | 480 sessions (down from several thousand a month in late 2025) | High |
| Around29 Digital Media Solutions (internal) | 695 sessions | Medium |
| Send29 (internal) | 72 sessions, partial month | Medium |
| All other 41 | Not Available | n/a |

Metric is Sessions because Search29 stores daily, not monthly deduplicated, users. Cunning Dental shows 124 paid-search sessions against several hundred Google Ads clicks; check tagging before any performance claim.

### Timing windows

Now: American Tree Excavation (storm season). 15 Oct to 7 Dec: Zellers Group (Medicare enrollment). Oct to Dec: Clean & Clear by Cliff (Christmas lights). 1 Nov: Workhub Tulsa (pre-leasing). From March: AA Roofing (decks), Superior Coatings NW (exterior painting). Spring: Trans Landscaping (hardscape).

---

## 6. Immediate outreach list (13)

In BD-score order: VIP Pest Solutions, Prime Care Dental Indy, AA Roofing and Decking, Zellers Group, Affordable Junk Removal, Superior Coatings NW, La Jolla Grooming Co, Wheeler-Sonoma Printers, Alignments Northwest, American Tree Excavation, Northwest Eco Clean, Workhub Tulsa, Clean & Clear by Cliff. Contacts, phones and hooks are on SALES_PITCH_INTELLIGENCE. Names marked NV came from directories and must be confirmed on the call.

**Enrichment queue (Priority 2):** Cunning Dental Group, Orion Optical, Trans Landscaping, Axle Surgeons of Seattle, Calvary Cemetery, Ocean View Lodging.

**Research queue (Priority 3):** Top Dollar Pawn, Pinpoint Resource, Occasions Paper, ASL Camguard, Cunningsmiles Implant Experts, Will Rogers Stage Foundation.

---

## 7. Recommendations and next actions

1. This week: call the four time-bound Priority 1 prospects (Zellers Group, Workhub Tulsa, Clean & Clear by Cliff, American Tree Excavation).
2. This week: call the remaining nine Priority 1 prospects in BD-score order; confirm directory-sourced names.
3. Next two weeks: close the six Priority 2 gaps by phone; run registry lookups; record the six source-data corrections in a new column.
4. Before launch: confirm service-area cities for AA Roofing, American Tree, Alignments Northwest and La Jolla Grooming; fix flagged landing pages.
5. Within a month: resolve the two possible duplicate pairs and Cunningsmiles; decide the Ad Grants route for the five nonprofits.
6. Each wave: re-run the Transparency Center and Meta Ad Library checks.
7. First call: request GA4 or Search Console read access from Priority 1 prospects; never substitute estimates.
8. Housekeeping: reconcile the list with Search29; confirm whether Premo Media Group manages Orion Optical's ads.

Pitch guidance: Search campaigns first, Shopping and Performance Max later. For Segment B, pitch optimisation, conversion tracking and expansion, not acquisition. Handle Cunning Dental Group and Workhub Tulsa as existing Around29 accounts.

---

## 8. Research methods

- **Websites:** each prospect's site saved as HTML and read for contacts, services, locations, forms, tags and page errors.
- **Directories:** BBB, chambers of commerce, state registries for owner names and addresses; marked NV until confirmed.
- **Google Ads Transparency Center:** by domain, US region, "Any time" and "Last 30 days" (date filter validated by confirming "Today" returned zero).
- **Meta Ad Library:** exact-phrase search by business name; results counted only when the sponsoring page was the prospect; look-alike advertisers excluded.
- **Site tag scan:** Google Ads conversion tags, GA4, GTM, Meta pixel, TikTok and LinkedIn tags.
- **Search29 (Around29's dashboard, read-only SQL):** client list, Google Ads summaries, GA4 daily and channel-monthly sessions, Search Console clicks, connected integrations.
- **Not verifiable:** Yelp advertising, display networks, non-US Transparency Center regions, Facebook versus Instagram placement.

---

## 9. Workbook tabs

| Tab | Contents |
|---|---|
| Prospects, Internal | Raw source, untouched |
| CLEANED_DATA, DATA_QUALITY_FLAGS | Step 2 |
| CLASSIFICATION | Step 3 |
| GOOGLE_ADS_FIT | Step 4 |
| SCORING_METHOD, SCORE_FACTOR_DETAIL, GOOGLE_ADS_OPPORTUNITY_SCORE | Step 5 |
| ENRICHED_PROSPECTS, MISSING_DATA_QUEUE | Step 6 |
| GOOGLE_ADS_OPPORTUNITY | Step 7 |
| SALES_PITCH_INTELLIGENCE | Step 8 |
| BD_PRIORITIZATION, BD_LISTS | Step 9 |
| MASTER MANAGEMENT VIEW | One row per business (A:L), summary blocks (N:S), hover notes on A1, G1, I1, L1, N3 |
| ADS RESEARCH | Advertising evidence, sources, confidence per business |
| WEBSITE TRAFFIC RESEARCH | Traffic value, metric, period, source, GA4 property, confidence per business |

### MASTER MANAGEMENT VIEW columns

A Business, B Industry, C Business Model, D Google Ads Opportunity (HIGH/MEDIUM/LOW), E Opportunity Score, F Contactability, G Priority, H BD Action / Sales Angle, I Running Ads, J Ads Ever Run, K Platforms, L Website Traffic. Summary blocks: management counts N1:P9, Top 5 industries N11:P18, Top 10 opportunities N20:S31, management insight N33:Q38. All summary cells are live formulas.

---

## 10. Deliverables in the project folder

| File | What it is |
|---|---|
| step10-final-bd-report.md | Final BD report (Version 5): executive summary, sections 1 to 10, final outputs A to E |
| Web report | https://claude.ai/artifact/LRsPDLQqrdJ5JbqL8YWYiM (private until shared) |
| Around29-Google-Ads-BD-Report.pptx | 24-slide presentation: Overview; 01 Findings; 02 Advertising; 03 Traffic; 04 Action, with native charts, geography and timing slides |
| Online deck | https://claude.ai/artifact/SeS2QqaK7xnZ2nHWToQd87 (16-slide version, exports to .pptx or PDF) |
| MASTER-MANAGEMENT-VIEW-Meeting-Explainer.docx | 14-section Word explainer: layout, columns, score framework, contactability, priority rules, segments, traffic rule, Q&A, QA log, deck mapping |
| master_management_view.csv, ads_research.csv, bd_prioritization.csv, bd_lists.csv, sales_pitch_intelligence.csv, google_ads_market_opportunity.csv, enriched_prospects.csv, missing_data_queue.csv, google_ads_opportunity_score.csv, classification.csv, cleaned_data.csv, google_ads_fit.csv | CSV copies of each sheet tab |
| master-management-view.py, ads-research.py, step9-bd-prioritization.py, step7-8-opportunity-pitch.py and earlier step scripts | Scripts that produced each tab, kept for reproducibility |
| step6-research-json/ | Per-prospect enrichment evidence |

---

## 11. QA record (8 October 2026)

- All 45 management Opportunity Scores recomputed from Step 5 factors: 45 of 45 match.
- Bands, priorities and overrides: 45 of 45 correct. Sort order correct.
- Advertising columns against ADS RESEARCH: 45 of 45 match. Traffic column against WEBSITE TRAFFIC RESEARCH: match.
- Summary formulas reconcile to 45; Segment A formula returns the nine names listed.
- One defect fixed: the BD Action for Occasions Paper was blank and was restored.
- Known labelling differences: master view uses corrected display names (Clean & Clear by Cliff, Zellers Group, Wheeler-Sonoma Printers, Orion Optical) and consolidated industries; BD_PRIORITIZATION keeps the Step 2 names.

---

## 12. Open items

- Confirm directory-sourced owner names on first calls.
- Resolve the duplicate pairs (Cunning Dental Group / Cunningsmiles; Starling Education / Starling Wonder Kids).
- Apply the six source-data corrections in a new column.
- Clarify account control for Orion Optical, Calvary Cemetery, Ocean View Lodging and Affordable Junk Removal before pitching.
- Check Cunning Dental's Ads-to-GA4 attribution gap.
- Connect GA4 to the Workhub Tulsa account.
- Optional additions discussed but not built because they need new data or a decision: revenue potential per prospect, a Search29 case study of the two managed accounts, a competitor-advertiser check per market, a landing-page readiness scorecard, and a live outreach tracker.
