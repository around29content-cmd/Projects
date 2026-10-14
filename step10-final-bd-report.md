# Around29 Google Ads Business Development Report

Date: 8 October 2026 (advertising research added the same day). Source workbook: "Around29 Google Ads Prospects" (Google Sheet). This report consolidates the approved outputs of Steps 1 to 9. It introduces no new research or assumptions. Every figure below is either read from the sheet tabs produced in those steps or counted from them. Where a statement is an inference rather than a verified fact, it is labelled "Inferred".

Conventions: **Verified** = seen on the business's official website or an official profile it controls, or counted directly from the dataset. **Inferred** = analyst judgement from verified facts (for example a scoring rubric or a likely business problem). **Needs Verification** = taken from a directory, snippet or registry mirror and not yet confirmed.

---

## Executive Summary

| Measure | Value | Basis |
|---|---|---|
| Total records analysed | 45 | Prospects tab 36 + Internal tab 9 (Step 1) |
| Unique businesses | 45 by name; 2 possible duplicate pairs unresolved | Step 2: Cunning Dental Group / Cunningsmiles Implant Experts; Starling Education / Starling Wonder Kids |
| External sales prospects | 36 | Internal tab holds Around29's own properties |
| Tier 1 prospects (Google Ads score 85 to 100) | 7 | Step 5 |
| Tier 2 prospects (70 to 84) | 13 (12 external + 1 internal) | Step 5 |
| Immediate outreach (Priority 1) | 13 (MASTER MANAGEMENT VIEW shows 10 under its stricter HIGH-band rule; see Section 6) | Step 9 |
| Enrichment required (Priority 2) | 6 | Step 9 |
| Research required (Priority 3) | 6 | Step 9 |
| Deprioritised (Priority 4) | 20 (11 external + 9 internal) | Step 9 |
| Prospects currently running Google Ads | 7 of 36 (2 are existing Around29-managed accounts) | Advertising research, Section 4b |
| Prospects with paid Meta (Facebook) advertising | 4 of 36 | Advertising research, Section 4b |
| Untapped Google Ads opportunities (HIGH, no Google Ads evidence, P1 or P2) | 9 | Section 4b, Segment A |
| Websites with verified first-party traffic | 4 of 45 (2 prospects, 2 internal); 41 Not Available | Website traffic research, Section 4c |
| Most promising industries | Home Services, Dental; then single-record Medical, Real Estate (coworking), Hospitality, Insurance | Section 2 |
| Most promising business models | Multi-location, emergency service, high-ticket service, lead generation, subscription / recurring local service | Section 3 |

Headline: 13 of the 36 external prospects can be contacted now with a verified phone number, a named person and a business-specific pitch. Seven of the 36 score as Tier 1 Google Ads opportunities, and five of those seven are in the Contact Now group. Home Services accounts for 8 of the 36 prospects and 7 of the 13 Contact Now businesses. Advertising research found that 7 prospects already run Google Ads, two of them (Cunning Dental Group, Workhub Tulsa) through Around29 itself, so the pitch for those is optimisation and expansion rather than acquisition. Nine HIGH-opportunity prospects show no Google Ads activity at all. Verified website traffic exists for only four sites (Around29-connected GA4); every other traffic figure is Not Available rather than estimated.

---

## 1. Data Quality

**Verified from the raw sheet (Step 1).** The Prospects tab had 8 columns: Partner, Client, Business URL, Phone, Email, Service, Plan, Status. No column held a contact person, title, address, city, state, industry, ads status or budget, so those fields were 100% missing for all 45 records. The Internal tab had no header row and two phone numbers stored as floating-point numbers (displayed as 9.16E+11 and 9.19E+11), losing digits.

**Major missing fields (Step 2 cleaned data, 45 records).**

| Field | State | Count |
|---|---|---|
| Phone | Valid 10-digit number | 29 of 45 |
| Phone | Present but invalid or corrupted (Needs Verification) | 4 |
| Phone | Blank | 12 |
| Email | Present | 6 of 45 (3 free-mail, 2 on a different business domain) |
| Email | Blank | 39 |
| Contact person | Any | 0 of 45 |
| Location | Any | 0 of 45 (recovered later from websites for most) |
| Industry | Any | 0 of 45 (classified in Step 3) |
| Website | Blank | 1 (Search29) |

**Contact-data gaps after enrichment (Step 6, 20 Tier 1 and 2 businesses researched).** Phone verified on the official website for 18 of 20. Email found where the file had none for 13. Still no email for Prime Care Dental Indy, Cunning Dental Group and Axle Surgeons of Seattle. Named decision-maker found for 14, of which 7 on official sources and 7 only on BBB, chamber or LinkedIn listings (Needs Verification). No business publishes a marketing contact. The MISSING_DATA_QUEUE tab lists 130 open items.

**Corrections to the source data found in Step 6 (not applied; raw tabs untouched).**

- VIP Pest Solutions: phone on file has an extra digit; official site shows (805) 608-3847.
- Ocean View Lodging: phone on file appears nowhere; official site shows (707) 964-1951.
- Orion Opticals: email on file belongs to a Tacoma marketing agency, not the business.
- Axle Surgeons of Seattle: email on file appears on no public source.
- "Clean and Clean by Cliff" is a typo; trading name is Clean & Clear by Cliff.
- "Zellersins" trades as Zellers Group; legal name Zellers Insurance & Financial Services Inc.

**Existing clients inside the prospect list.** Around29's Search29 dashboard shows Cunning Dental Group (client id 1) and Workhub Tulsa (client id 97) as current Around29 Google Ads accounts, and Affordable Junk Removal, Alignments Northwest, Axle Surgeons of Seattle and Around Cricket as Search29 clients without Google Ads. The source list therefore mixes prospects with current clients; BD should treat the two Google Ads accounts as expansion conversations.

**Duplicate issues (Step 2).** No exact or likely duplicates. Two possible pairs on a shared name token: Cunning Dental Group / Cunningsmiles Implant Experts (the latter's site is dead and nothing links the two; Inferred: probably a defunct marketing microsite) and Starling Education / Starling Wonder Kids (both internal). Alignments Northwest and Axle Surgeons of Seattle share a Tacoma street address and phone exchange and are flagged as possibly related entities.

**Data limitations.** State business registries (Washington, California, Oklahoma, Indiana) and licence lookups are JavaScript applications that could not be fetched, so legal-entity details rest on registry mirrors or BBB. Yelp, Facebook, LinkedIn profiles, several news sites and directories blocked direct fetches; values from them come from search snippets. Google Business Profile data was not collected. Mobile rendering and page speed were not tested. Website traffic is verifiable only for the four sites with Around29-connected GA4; third-party traffic estimates were deliberately excluded. No search volumes, cost-per-click or competitor advertising data were used anywhere. Internal records were not researched.

---

## 2. Industry Opportunity

Counts are from Step 3 classification, Step 5 scores and Step 9 priorities. Single-record industries are shown but should not be read as trends.

| Industry | Records | External prospects | Avg Google Ads score | Tier 1 | Tier 2 | Priority 1 | Priority 2 | Overall attractiveness |
|---|---|---|---|---|---|---|---|---|
| Home Services | 8 | 8 | 82.6 | 4 | 4 | 7 | 1 | Highest: volume, value and contactability |
| Dental | 3 | 3 | 84.0 | 2 | 0 | 1 | 1 | Very high value per case; one record is a dead site |
| Medical (optometry) | 1 | 1 | 85.5 | 1 | 0 | 0 | 1 | High; decision-maker unknown |
| Real Estate (coworking) | 1 | 1 | 79.0 | 0 | 1 | 1 | 0 | Good; time-bound (Nov 2026 pre-leasing) |
| Hospitality | 1 | 1 | 78.5 | 0 | 1 | 0 | 1 | Good; operator unknown |
| Insurance | 1 | 1 | 77.0 | 0 | 1 | 1 | 0 | Good; Medicare enrollment underway |
| Automotive (B2B repair, products) | 3 | 3 | 75.5 | 0 | 2 | 1 | 1 | Good for the two mobile B2B operators; the product brand is Tier 3 |
| B2B Services (printing) | 1 | 1 | 70.0 | 0 | 1 | 1 | 0 | Moderate; specialty terms only |
| Financial Services (pawn) | 1 | 1 | 67.0 | 0 | 0 | 0 | 0 | Moderate; policy limits |
| Retail | 4 | 4 | 57.4 | 0 | 0 | 0 | 0 | Low to moderate; store-visit campaigns at best |
| Education | 4 | 1 | 51.1 | 0 | 1 | 0 | 0 | Low (3 of 4 internal; external record is a nonprofit) |
| Professional Services | 2 | 0 | 59.5 | 0 | 0 | 0 | 0 | Internal only |
| Technology | 3 | 0 | 50.7 | 0 | 0 | 0 | 0 | Internal only |
| Healthcare (nonprofit) | 1 | 1 | 43.0 | 0 | 0 | 0 | 0 | Low; Ad Grants route |
| Other (cemetery, pet grooming, nonprofits, events, HOA) | 9 | 9 | 44.6 | 0 | 2 | 1 | 1 | Mixed: pet grooming and the cemetery are Tier 2; six are nonprofits or non-businesses |
| Unknown | 2 | 1 | 20.5 | 0 | 0 | 0 | 0 | Cannot be assessed (sites down) |

Reading (Inferred from the table): Home Services is the only industry with both volume and depth, and it also has the most complete contact data after enrichment. Dental has the highest value per case but only two live records. Everything else promising is a single business.

**Geographic clusters (Verified from the Step 6 addresses and service areas; the 13 Priority 1 and 6 Priority 2 businesses only).**

| Region | Businesses | Reading (Inferred) |
|---|---|---|
| Puget Sound, WA | 8: AA Roofing and Decking (Auburn), Superior Coatings NW (Puyallup), American Tree Excavation (Puyallup), Trans Landscaping (Spanaway), Alignments Northwest and Axle Surgeons of Seattle (Tacoma), Clean & Clear by Cliff (Bonney Lake), Northwest Eco Clean (Renton) | Seven sell into the same Pierce County and south King County radius. One market to learn once: shared geo-targeting, shared landing-page lessons, one field visit covers all seven |
| California | 8: VIP Pest Solutions (Santa Maria, Central Coast), Affordable Junk Removal (Sacramento), Zellers Group (Sonoma), Wheeler-Sonoma Printers (Vallejo), Orion Optical (Concord), Ocean View Lodging (Fort Bragg), La Jolla Grooming Co (La Jolla), Cunning Dental Group (Montclair, Inland Empire) | No shared geography; eight separate local markets, each pitched on its own |
| Tulsa, OK | 2: Workhub Tulsa, Calvary Cemetery | Both inside the city; one trip covers both |
| Indianapolis, IN | 1: Prime Care Dental Indy (two offices) | Stand-alone |

---

## 3. Business Model Opportunity

Average Step 5 score of the 36 external prospects whose Step 3 business model includes each attribute (a business can carry several).

| Business model attribute | Prospects | Avg Google Ads score | Why it is attractive (Inferred from Step 4 and 5 rubrics) |
|---|---|---|---|
| Multi-location | 2 | 92.0 | Two dental practices; each office is a separate local target with its own Maps presence and booking path |
| Emergency service | 3 | 89.3 | Demand arrives as an urgent search followed by a call; little price shopping (junk removal, tree removal, axle repair) |
| High-ticket service | 8 | 82.8 | A single roof, implant case or termite job pays for weeks of clicks |
| Lead generation (calls and quotes) | 8 | 82.2 | Conversion is a tracked call or quote form, so cost per lead is measurable from day one |
| Subscription | 3 | 80.8 | Recurring pest plans, bin cleaning and office memberships give lifetime value per acquisition |
| Local service | 18 | 79.8 | Geo-targeting is clean; Maps and location extensions apply |
| Recurring service | 9 | 77.7 | Repeat visits (grooming, exams, window care) raise the value of each new client |
| Appointment-based | 7 | 77.5 | Bookings are trackable and often already online |
| Project-based | 6 | 76.3 | Quote-driven but seasonal (landscaping, painting, printing) |
| B2B | 12 | 75.7 | Smaller search volume but high intent and repeat accounts (fleet repair, printing, commercial cleaning) |
| B2C (all) | 29 | 66.2 | Mixed: includes the strongest local services and all the nonprofits |
| Consultation-based | 3 | 65.2 | Longer sales cycle (insurance, cemetery pre-need, mentoring) |
| Retail | 6 | 63.7 | Store visits are hard to measure; thin margins |
| Ecommerce | 3 | 60.0 | Two of three sell outside the US market this list serves |
| Nonprofit, event or association | 9 | 41.7 | No commercial conversion; the Google Ad Grants programme fits better than paid search |

Most attractive combination (Inferred): a local, high-ticket or recurring service with urgent demand and a call or quote conversion. Every Contact Now business except the printer and the insurance agency matches it.

---

## 4. Google Ads Opportunity

Drawn from GOOGLE_ADS_FIT (Step 4) and GOOGLE_ADS_OPPORTUNITY (Step 7). Keyword themes are intent patterns; no volumes were measured.

**Highest-value service categories (Verified as offered on the official sites; value ranking Inferred).** Dental implants and full-arch restorations (Prime Care Dental, Cunning Dental); roof replacement (AA Roofing); termite fumigation and recurring pest plans (VIP Pest); Medicare and small-group health policies (Zellers Group); hazardous tree removal (American Tree); exterior and commercial painting (Superior Coatings); hardscape installs (Trans Landscaping); private office leases (Workhub Tulsa); commercial cleanouts (Affordable Junk Removal); fleet repair accounts (Axle Surgeons, Alignments Northwest).

**Strongest search-intent categories (Step 4 search intent 8 or above).** Dental (9, 9, 8), pest control (9), lodging (9), junk removal (9), roofing (9), tree service (8), landscaping (8), painting (8), optometry (8), pet grooming (8). The common pattern is "service + city", "service near me" and emergency or same-day modifiers.

**Strongest geographic opportunities (Verified service areas).** South Puget Sound / Pierce County, Washington, where seven prospects cluster (AA Roofing, American Tree, Superior Coatings, Trans Landscaping, Clean & Clear by Cliff, Axle Surgeons, Alignments Northwest) and campaigns can share local learnings. Indianapolis (two dental offices). Central Coast California three-county area (VIP Pest). Inland Empire eleven-city footprint (Cunning Dental). Sonoma, Napa and Marin (Zellers Group). Tulsa (Workhub, Calvary Cemetery). Service areas still unverified: AA Roofing, American Tree, Alignments Northwest, La Jolla Grooming.

**Strongest conversion opportunities (Verified on site).** Online booking or scheduling already live at Prime Care Dental, Orion Optical, Affordable Junk Removal, Northwest Eco Clean, Clean & Clear by Cliff (Housecall Pro), Ocean View Lodging (booking engine) and Workhub Tulsa (tour form with event tracking). Call-driven with quote forms: AA Roofing, VIP Pest, Superior Coatings, American Tree, Trans Landscaping, Axle Surgeons, Alignments Northwest, Zellers Group. Weakest paths: Wheeler-Sonoma (no form or quote path), Calvary Cemetery (no appointment path), La Jolla Grooming (request form only, followed by a call).

**Recurring landing-page findings (Verified in saved HTML).** Seven of 19 sites return 404 on their About pages; Workhub Tulsa also on Contact. Only three home pages contain a native form element. Three home pages are heavy (Cunning Dental about 950 KB). Five sites publish no service-area cities.

---

## 4b. Advertising Activity (research completed 8 October 2026)

**Method (Verified).** Google Ads Transparency Center queried by domain for the US region, first "Any time" and then the "Last 30 days" filter for every domain with ads (the filter was validated by confirming "Today" returned zero for a domain with ads). Meta Ad Library, US, exact-phrase search by business name; a result counted only when the sponsoring page name was the prospect, and look-alike advertisers (a Las Vegas "Prime Care Dental", a Salt Lake City "Superior Coatings", a Turks and Caicos "Top Dollar Pawn", Modesto's "American Tree Service") were excluded. Each saved website was scanned for Google Ads conversion tags, Meta pixel, TikTok and LinkedIn tags. Around29's Search29 dashboard was used for the accounts it manages. Full evidence and source URLs per business are on the ADS RESEARCH tab.

**Definitions.** Running Ads and Ads Ever Run refer to Google Ads only. Platforms records paid advertising on other platforms. "No" means no evidence was found after this research, not that the business never advertised. A business can therefore show Ads Ever Run = No and Platforms = Facebook Ads: it advertises on Meta but no Google Ads were found. That is the Segment C pattern below, not a data error.

| Result | Count (36 prospects) |
|---|---|
| Running Google Ads now (evidence in last 30 days) | 7 |
| No Google Ads evidence | 28 |
| Unknown (India-based business; US-only lookup) | 1 |
| Paid Meta (Facebook) advertising found | 4 |
| Google Ads conversion tag on site but no ads found (history Unknown) | 2 (Trans Landscaping, Top Dollar Pawn) |
| TikTok or LinkedIn ad tags found | 0 |

**Segment A, untapped Google Ads opportunity (HIGH opportunity, no Google Ads evidence, P1 or P2): 9.** AA Roofing and Decking, VIP Pest Solutions, Superior Coatings NW, American Tree Excavation, Zellers Group, Alignments Northwest, Northwest Eco Clean, Trans Landscaping, Axle Surgeons of Seattle. These are the cleanest acquisition pitches.

**Segment B, already running Google Ads (optimisation and expansion angle): 7.**

| Business | Evidence (Verified unless marked) | Confidence |
|---|---|---|
| Cunning Dental Group | 36 ads in Transparency Center, all within 30 days; Search29 shows an Around29-managed account with about $8,239 spend, 585 clicks and 26 conversions from 1 Sep to 7 Oct 2026; 4 active Meta ads since 1 Oct 2026 | High |
| Workhub Tulsa | 8 ads placed by Around29 Digital Media Solutions; Search29 budget $700 a month, $982 spend and 3 conversions 1 Sep to 7 Oct 2026 | High |
| Prime Care Dental Indy | 5 ads by Primecare Dental LLC, all within 30 days | High |
| Orion Optical | 9 ads by Orion Optical, LLC, all within 30 days; an outside agency may manage them (Inferred from the email on file) | High |
| Calvary Cemetery | 14 ads by the advertiser CoxNet within 30 days (a media company, Inferred); one Meta video ad ran 17 Jun to 28 Sep 2026 | Medium |
| Ocean View Lodging | 4 ads by an individual advertiser within 30 days; relationship to the lodge unverified | Medium |
| Affordable Junk Removal | 1 ad by a third-party advertiser (Choice Medias LLC) within 30 days; relationship unverified | Medium |

No performance judgement is made about these accounts. The angle is optimisation, conversion tracking, campaign expansion, landing-page alignment and, for the two Around29-managed accounts, an internal expansion conversation.

**Segment C, advertising elsewhere but no Google Ads evidence: 2.** Northwest Eco Clean (active Meta ads since May 2026 under its own page) and Around Cricket (Meta ads run through Around29's ad account, data to August 2026). Both already buy paid acquisition; Google Ads can be positioned as an additional channel. No claim is made that they need it.

**Not verifiable.** Yelp advertising status (Yelp blocks fetching), display networks, and Transparency Center regions outside the US. Meta placement (Facebook versus Instagram) is not shown in the library text, so only Facebook Ads was recorded.

---

## 4c. Website Traffic (first-party data only, research completed 8 October 2026)

**Rule applied.** Only authenticated first-party analytics count. No Similarweb, Semrush or other estimates were used, and Google Ads clicks, Search Console clicks and Business Profile views were not converted into traffic. Where exact traffic could not be verified the value is Not Available. Evidence per business is on the WEBSITE TRAFFIC RESEARCH tab.

**Source.** Around29's Search29 dashboard holds authenticated GA4 properties for four of the 45 websites. It stores daily users, not monthly deduplicated users, so the exact monthly metric reported is Sessions (additive; the daily totals reconcile to the dashboard's channel-monthly table). Reporting period: 1 to 30 September 2026, the last complete month.

| Business | Website Traffic | Domain verification | Confidence |
|---|---|---|---|
| Affordable Junk Removal | 838 sessions/month (Sep 2026) | Client website, Search Console property and GTM container ID all match the live site; top GA4 pages are its Sacramento and Rocklin service pages | High |
| Cunning Dental Group | 480 sessions/month (Sep 2026) | GA4 property named with the domain; Search Console and GTM match | High |
| Around29 Digital Media Solutions (around29.com, internal) | 695 sessions/month (Sep 2026) | Client website and Search Console match; property name lacks the domain | Medium |
| Send29 (internal) | 72 sessions (2 to 30 Sep 2026, partial) | Property named with the URL; GA4 connected 2 Sep, 20 of 30 days present | Medium |
| All other 41 websites | Not Available | No first-party access (most sites carry a GA4 tag Around29 cannot read) | High that no source is accessible |

**Observations (Verified figures, Inferred reading).**

- Affordable Junk Removal's September sessions were 62% paid search (523 of 838) despite no Google Ads account in Search29, consistent with the third-party advertiser found in the Transparency Center. Organic search contributed 192 sessions; Search Console shows 61 organic clicks.
- Cunning Dental Group's site traffic has fallen from several thousand sessions a month in late 2025 (largely Paid Social) to 480 in September 2026. GA4 recorded 124 paid-search sessions in September while the Google Ads account reports several hundred clicks across September and early October; a tagging or attribution gap is possible and should be checked before any performance claim.
- For Workhub Tulsa, Google Ads reports 98 clicks from 1 September to 7 October, but no GA4 property is connected, so website traffic is Not Available by rule.

---

## 5. Top 25 Prospects

Ranked by the Step 9 BD score within priority. Google Ads score is Step 5. "Missing information" is from the MISSING_DATA_QUEUE. Decision-maker names marked (NV) rest on directories and need verification.

| # | Business | Industry | Model | Ads score | Priority | Why attractive | Google Ads opportunity | Missing information | Sales pitch angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | VIP Pest Solutions | Home Services (pest) | Local, recurring, subscription | 88.0 | 1 | Three-county Central Coast area, recurring plans, termite work; all contact data verified | Termite and recurring pest Search across SLO, Santa Barbara, Ventura; $95 inspection as lead-in | Owner title not explicit; licence number; marketing contact | Turn the $95 termite inspection into a Search offer that feeds fumigation and recurring plans |
| 2 | Prime Care Dental Indy | Dental | Appointment, multi-location, high-ticket | 92.5 | 1 | Two Indianapolis offices, implants and Invisalign, online booking live | Per-office Search on implants, Invisalign, emergency; Maps for each office | Email; owner; marketing contact | Already running Google Ads (5 ads, last 30 days); pitch per-office expansion and optimisation into the existing booking form |
| 3 | AA Roofing and Decking | Home Services | Lead gen, high-ticket, project | 90.5 | 1 | Licensed, BBB-accredited roofer; owner named (NV) | Roof replacement and repair Search for south King and Pierce County; seasonal decks | Service area not on site; address (NV); founder | Site lists every roof type and financing but no cities; a city-targeted roofing campaign fixes that |
| 4 | Zellers Group (Zellersins) | Insurance | Consultation, lead gen, recurring | 77.0 | 1 | President named, all contact data verified; Medicare enrollment open 15 Oct to 7 Dec | Medicare and small-group health Search in Sonoma, Napa, Marin | Owner confirmation; founder; marketing contact | Four Medicare-specialist agents but invisible to "Medicare agent near me" during enrollment |
| 5 | Affordable Junk Removal | Home Services | Local, lead gen, same-day | 87.0 | 1 | Owner named, online booking with time slots, strong reviews | Residential same-day plus commercial cleanout Search; brand defence | Street address conflicts; founder | A third-party advertiser runs one Google ad to the site; pitch Search expansion and brand defence around the booking form |
| 6 | Superior Coatings NW | Home Services (painting) | Project, high-ticket, lead gen | 85.0 | 1 | Licensed painter with commercial references; owner named (NV) | Exterior and commercial painting Search for Pierce County | Address (NV); entity name conflict; L&I status | Commercial work for a national carrier but no visibility for "exterior house painters near me" |
| 7 | La Jolla Grooming Co | Pet services | Appointment, recurring | 75.0 | 1 | Founder named, affluent hyperlocal market, dental add-on, daycare sister brand | Tight-radius Search and Maps for grooming and dental | Service area; owner title | Keep every chair booked with six-week repeat clients from Bird Rock and La Jolla searches |
| 8 | Wheeler-Sonoma Printers | B2B Services | B2B, project, recurring | 70.0 | 1 | Owner named on site; engraving, letterpress and foil capabilities | Specialty printing Search (engraving, wine labels) for Bay Area and Napa | Marketing contact; no quote form on site | Buyers search "engraved business cards Bay Area" and never see 85 years of craft; add a quote form |
| 9 | Alignments Northwest | Automotive (B2B) | Local, appointment, B2B, fleet | 78.5 | 1 | Niche mobile service with little competition; phone and email verified | Heavy-truck alignment Search along the I-5 freight corridor | Owner; service area; roles of named contacts | Fleet managers in Kent search "mobile truck alignment near me"; turn jobs into fleet accounts |
| 10 | American Tree Excavation | Home Services (tree) | Lead gen, high-ticket, emergency | 80.0 | 1 | BBB-accredited, 24-hour emergency, owner named (NV) | Emergency tree removal Search for Pierce County with 24/7 call-only ads | Address conflicts; service area not on site; email (NV) | 24-hour emergency service with no city on the site; storm-season searchers cannot find you |
| 11 | Northwest Eco Clean | Home Services (bin cleaning) | Local, recurring, subscription | 75.5 | 1 | Online scheduling live; owner named (NV); King County suburbs | Subscription bin-cleaning Search plus HOA and commercial ad group | Street address conflicts; founder (NV) | Stack subscriptions onto routes you already drive; nobody searching "trash can cleaning near me" sees you |
| 12 | Workhub Tulsa | Real Estate (coworking) | Subscription, B2B, local | 79.0 | 1 | Pricing published, tour form tracked, six suites pre-leasing 1 Nov 2026 | Private-office Search in Tulsa timed to pre-leasing | Email inbox conflict; owner; About/Contact pages 404 | Existing Around29 Google Ads account ($700 a month); expand and optimise for the 1 November pre-leasing, not a new-client pitch |
| 13 | Clean & Clear by Cliff | Home Services (window) | Local, recurring, lead gen | 71.0 | 1 | Housecall Pro booking live; owner is the brand; Christmas-light season | Window cleaning Search plus October-December Christmas-light campaign | Owner surname (NV); address (NV); service area | Highest-ticket seasonal job is being searched right now; send it straight to your booking page |
| 14 | Cunning Dental Group | Dental | Appointment, high-ticket, emergency | 91.5 | 2 | Full-arch implants, on-site lab, eleven city pages, financing | Implant and All-on-4 Search across the Inland Empire | Current owner; email; manager name stale (NV) | Existing Around29 Google Ads account (about $8.2k spend, 26 conversions Sep to Oct 2026) plus active Meta ads; optimisation and expansion conversation |
| 15 | Orion Optical | Medical (optometry) | Appointment, retail, recurring | 85.5 | 2 | Luxury frames, online exam scheduling, affluent East Bay suburb | Local Search and Maps for exams and frame brands | Owner; whether an agency already runs marketing | Already running Google Ads (9 ads, last 30 days), possibly via an outside agency; clarify who controls the account before pitching |
| 16 | Trans Landscaping | Home Services | Project, high-ticket, lead gen | 83.5 | 2 | Nine-city Pierce County area verified; hardscape work | Seasonal hardscape Search for Pierce County | Owner or any contact name; address (NV) | Nine cities in the footer, patios in the gallery, nothing for "paver patio installers near me" in April |
| 17 | Axle Surgeons of Seattle | Automotive (B2B) | Emergency, B2B, lead gen | 84.0 | 2 | 24/7 mobile spindle repair, little competition | Call-only emergency Search along I-5 | Any person; email; national-brand relationship | Dispatchers call the first "mobile axle repair" result; you are not in it |
| 18 | Calvary Cemetery | Other (cemetery) | High-ticket, consultation | 71.0 | 2 | Diocese cited a strengthening pre-need programme and new memorial gardens | Pre-need and cremation Search for Catholic families in Tulsa | Current executive director; governance (NV) | Google ads already run to the site via a media company and a Meta ad ran Jun to Sep 2026; pitch optimisation once the new director is known |
| 19 | Ocean View Lodging | Hospitality | Reservation-based, online booking | 78.5 | 2 | Ocean-view rooms, direct booking engine | Brand defence plus destination Search aimed at Bay Area travellers | Owner or manager; phone conflict | Google ads already run to the site by an individual advertiser; confirm the operator, then pitch brand defence and optimisation |
| 20 | Top Dollar Pawn | Financial Services | Retail | 67.0 | 3 | Strong local intent | Local pawn and gold-buying terms after a policy review | All contact data beyond phone; policy eligibility | Not yet: policy review first |
| 21 | Pinpoint Resource | Retail (formalwear) | Retail | 61.5 | 3 | Local wedding and tuxedo terms | Store-visit campaign | All contact data beyond phone | Not yet: research first |
| 22 | Occasions Paper | Retail | Retail | 58.0 | 3 | Carried-brand store visits | Small store-visit campaign | All contact data beyond phone | Not yet: research first |
| 23 | ASL Camguard | Automotive (products) | Manufacturer, ecommerce | 64.0 | 3 | National product brand with online store | Shopping and brand campaigns | Phone, email, contact; budget scale | Not yet: no contact data at all |
| 24 | Cunningsmiles Implant Experts | Dental | Appointment, high-ticket | 68.0 | 3 | Implant category | None until verified | Everything; site dead | Not yet: confirm it exists and is not P-12 |
| 25 | Will Rogers Stage Foundation | Other (performing arts) | Ticket sales, nonprofit | 57.5 | 3 | Online ticket sales exist | Seasonal ticket campaigns; Ad Grants | Phone, email, contact | Not yet: small budgets, Ad Grants route |

---

## 6. Immediate Outreach List

Thirteen businesses with a phone number verified on the official website, a named person (seven verified on official sources, six from BBB or chamber listings to confirm on the call) and a written pitch in SALES_PITCH_INTELLIGENCE.

**Note on the MASTER MANAGEMENT VIEW count (added 8 October 2026).** The MASTER MANAGEMENT VIEW tab shows P1 Contact Now = 10, not 13. The two views use different rules. This report and BD_PRIORITIZATION (Step 9) rank on a blended BD score that includes contactability and research confidence, so three fully contactable businesses qualify. The management view requires a HIGH opportunity band (management score 75 or more) for P1, so La Jolla Grooming Co (74.7), Clean & Clear by Cliff (74.0) and Wheeler-Sonoma Printers (69.0) sit at P3 there even though they are READY to contact. Both views are correct for their purpose; the management view is the stricter opportunity filter. All thirteen remain on this outreach list. The same explanation is a hover note on cell N3 of the MASTER MANAGEMENT VIEW tab.

| Business | Contact to use | Channel | Time sensitivity |
|---|---|---|---|
| VIP Pest Solutions | Jamie Parkins, CEO (BBB accredited profile) | (805) 608-3847; info@vippestsolutions.com | None |
| Prime Care Dental Indy | Dr. Vijaya Palaparthi, DDS (owner status unknown) | (317) 426-1562 or (317) 426-0299 | None |
| AA Roofing and Decking | Ahmed R. Al-Jebori, Managing Member (NV) | (206) 280-0536; Aaroofinganddecking@gmail.com | Deck season from March |
| Zellers Group | Dean Zellers, President | (707) 996-5282; dz@zellersins.com | Medicare enrollment to 7 Dec |
| Affordable Junk Removal | Ashley Ramirez, Owner (BBB accredited profile) | (916) 730-8387; affordablejunkremoval916@gmail.com | None |
| Superior Coatings NW | Donovan (Donny) Peters, Owner (NV) | (253) 405-5424; superiorcoatings123@gmail.com | Exterior season from March |
| La Jolla Grooming Co | Garrett Larson, Founder | (858) 246-6235; info@ljgrooming.com | None |
| Wheeler-Sonoma Printers | Baird Conner, Owner | (707) 643-6383; customerservice@wheeler-sonoma.com | None |
| Alignments Northwest | Jordan or Austin (roles not stated) | (253) 777-7092; alignmentsnw@gmail.com | None |
| American Tree Excavation | Kristian Guttu, Owner/Partner (NV) | (253) 468-1505 | Storm season now |
| Northwest Eco Clean | Martez Johnson, Owner/Member (NV) | (206) 825-6998; customersupport@northwestecoclean.com | None |
| Workhub Tulsa | Carla, Property Manager (NV) | (918) 345-1390; carla@ or info@workhubtulsa.com | Pre-leasing 1 Nov 2026; existing Around29 Google Ads account, treat as expansion |
| Clean & Clear by Cliff | Cliff (surname NV), Owner | (253) 350-0457; cliffmc598@gmail.com | Christmas lights Oct to Dec |

**Timing windows (Verified from the prospects' own sites and the Step 8 hooks; dates are theirs, not Around29 targets).**

| Window | Business | Why it matters |
|---|---|---|
| Now | American Tree Excavation | Storm season; 24-hour emergency removal is being searched now |
| 15 Oct to 7 Dec 2026 | Zellers Group | Medicare Annual Enrollment; four Medicare-specialist agents |
| Oct to Dec 2026 | Clean & Clear by Cliff | Christmas-light installation, the highest-ticket seasonal job |
| 1 Nov 2026 | Workhub Tulsa | Six private suites pre-leasing; existing Around29 account to expand |
| From March 2027 | AA Roofing and Decking | Deck-building season |
| From March 2027 | Superior Coatings NW | Exterior painting season |
| Spring 2027 | Trans Landscaping (Priority 2) | Hardscape season, once a decision-maker is found |

The first four windows are open or imminent and set this week's call order. The spring windows give the research team time to close gaps before the season starts.

---

## 7. Enrichment Queue

Six Tier 1 or 2 businesses where one call to the verified main line should close the gap. Full field-level detail is in MISSING_DATA_QUEUE (130 rows, 11 High priority).

| Business | What is missing | Suggested action |
|---|---|---|
| Cunning Dental Group | Current owner (possible new management); email; manager name from a 2023 source. Existing Around29 Google Ads account | Use the existing account relationship to identify the decision-maker; frame as optimisation and expansion |
| Orion Optical | Owner name; whether Premo Media Group already runs marketing | Call (925) 349-4777; do not use the agency email |
| Trans Landscaping | Any decision-maker name; street address | Call (253) 984-6802, ask for the owner |
| Axle Surgeons of Seattle | Any person; email; relationship to the national Axle Surgeons brand | Call (253) 777-8811 |
| Calvary Cemetery | Current executive director (predecessor retired Oct 2025); governance | Call (918) 299-7348, ask for the executive director |
| Ocean View Lodging | Owner or general manager; phone on file conflicts with site | Call (707) 964-1951 |

Cross-cutting enrichment items for the research team: confirm service-area cities for AA Roofing, American Tree, Alignments Northwest and La Jolla Grooming before any geo-targeting; resolve conflicting street addresses for Affordable Junk Removal, American Tree and Northwest Eco Clean; run manual state-registry lookups (WA SOS CCFS, CA bizfile, OK SOS, IN INBiz) for legal entities; correct the six source-data errors listed in Section 1.

---

## 8. Research Queue

Six Tier 3 businesses where the Google Ads case is plausible but evidence is incomplete.

| Business | Open question |
|---|---|
| Top Dollar Pawn and Check Cashing | Which services can be advertised under Google's financial-products and firearms policies |
| Pinpoint Resource | Whether local formalwear and wedding terms can drive measurable store visits; no contact person |
| Occasions Paper | Whether carried brands justify a store-visit campaign; no contact person |
| ASL Camguard | Whether a national Shopping campaign fits their distribution; no phone, email or contact |
| Cunningsmiles Implant Experts | Whether this is a live business or a dead microsite of Cunning Dental Group |
| Will Rogers Stage Foundation | Whether seasonal ticket sales justify paid search versus the Ad Grants programme; no contact data |

---

## 9. Deprioritised Businesses

Eleven external prospects and the nine internal records.

| Business | Reason (Verified unless marked) |
|---|---|
| The Bartan Company | Event services based outside the US (Hyderabad) |
| Around Cricket | Ecommerce store serving a market outside the US |
| Ornamental Grasses | Plant nursery by appointment; weak fit, small ticket |
| Next Level Prospect | Nonprofit mentoring programme; site in progress |
| DBSA OK | Mental-health nonprofit; no commercial conversion; Ad Grants route |
| Chili On The Green | Annual charity event run by the Kiwanis club |
| Kiwanis Club of Tulsa | Service club; no commercial conversion |
| Lab Rescue | Animal rescue nonprofit; Ad Grants route |
| Tag OK | Animal-welfare awareness programme; Ad Grants route |
| Brothers Micro Market | Website down; business cannot be identified |
| Rosewood Parke | Homeowners association; not a business |
| Internal (9): Around29 Center for Enriched Studies, Around29 Digital Media Solutions, Search29, Send29, Lead You, Around29 themes, Around29.us, Starling Education, Starling Wonder Kids | Around29's own properties; not sales prospects (Inferred from names and the Internal tab; not researched) |

---

## 10. BD Recommendations

**1. Which industries should we target first?** Home Services first: eight prospects, average score 82.6, seven already in Contact Now, and a geographic cluster in Pierce County that lets one team learn the market once. Dental second for value per case (two live practices, one needing an owner call). Then the single strong records in optometry, insurance, coworking and hospitality.

**2. Which business models should we prioritise?** Local services with urgent or high-ticket demand and a call or quote conversion; recurring and subscription services (pest plans, bin cleaning, office memberships); appointment-based practices with online booking already live. Deprioritise nonprofits, associations and offshore ecommerce.

**3. Which businesses should we contact immediately?** The thirteen in Section 6, in BD-score order, leading with the Segment A businesses that show no Google Ads activity (AA Roofing, VIP Pest, Superior Coatings, American Tree, Zellers Group, Alignments Northwest, Northwest Eco Clean) and the four that are time-bound: Zellers Group (Medicare enrollment closes 7 December), Workhub Tulsa (1 November pre-leasing), Clean & Clear by Cliff (Christmas-light season) and American Tree Excavation (storm season).

**4. What information should we collect next?** Decision-maker names and roles for the six Priority 2 businesses and the seven Priority 1 businesses whose names rest on directories; service-area cities for the four prospects whose sites name none; the six source-data corrections; legal-entity confirmation via manual registry lookups; whether any prospect already runs Google Ads (never checked in this process).

**5. What Google Ads services should we pitch most heavily?** Non-brand Search with call tracking and quote or booking forms as the core offer, because every strong prospect converts by call, quote or booking. Local campaigns and location assets for the single-location practices and stores. Brand Search as a low-cost defensive add-on for generic or contested names (Affordable Junk Removal, Workhub Tulsa, Ocean View Lodge, Superior Coatings). Landing-page build or repair as a bundled service, since seven sites have broken About pages, only three have a native form on the home page and one has no quote path at all. Seasonal campaign scheduling for the painters, landscapers, roofers and window cleaners. Shopping and Performance Max only as later phases. For the seven businesses already running Google Ads, pitch account optimisation, conversion tracking and expansion instead of acquisition, and handle Cunning Dental Group and Workhub Tulsa as existing Around29 accounts.

**6. What patterns exist across the strongest prospects?** (Inferred from Sections 2 to 6.) They are owner-operated local services with a verified phone on the site, a named owner, a defined service area, a conversion path already built (booking widget or quote form), high ticket or recurring revenue, and urgent or seasonal demand. Most sit in a few metros: Pierce County WA, Indianapolis, the California Central Coast, the North Bay and Tulsa. Their weaknesses repeat too: no email or a free-mail address, no service-area cities on the site, missing About pages, and no one responsible for marketing. Nine of the 13 Contact Now businesses show no Google Ads activity at all, which is the clearest acquisition opening in the list.

---

## Final outputs

**A. Executive Report**: this document (sections above), the web version, and the presentation deck Around29-Google-Ads-BD-Report.pptx (24 slides in five sections: Overview; 01 Findings with data quality, industry table, industry score chart, business models and geographic clusters; 02 Advertising with the Google Ads status chart, Segments A, B and C and the seven running Google Ads; 03 Traffic with the four verified sites, the channel-mix chart and what it shows; 04 Action with the Contact Now list, the timing windows, the enrichment and research queues, recommendations, next actions and where the outputs live). Every figure on the deck is taken from this report or the workbook tabs.

**B. BD Prospect Table**: sheet tab BD_PRIORITIZATION (45 ranked rows with sub-scores and sales angle) and SALES_PITCH_INTELLIGENCE (hooks, readiness, contact to use); Section 5 and 6 above.

**C. Enrichment Queue**: sheet tab MISSING_DATA_QUEUE (130 field-level items with next action and priority) and ENRICHED_PROSPECTS (verified values with source status); Section 7 above.

**D. Google Ads Opportunity Summary**: sheet tabs ADS RESEARCH, WEBSITE TRAFFIC RESEARCH and GOOGLE_ADS_OPPORTUNITY, plus the MASTER MANAGEMENT VIEW columns Running Ads, Ads Ever Run and Platforms; Section 4b above; also GOOGLE_ADS_OPPORTUNITY (per-prospect keyword themes, geo, conversion, campaign types, verified landing-page facts) and GOOGLE_ADS_FIT; Section 4 above.

**E. Recommended Next Actions (prioritised)**

1. This week: call the four time-bound Priority 1 prospects (Zellers Group, Workhub Tulsa, Clean & Clear by Cliff, American Tree Excavation) using the hooks in SALES_PITCH_INTELLIGENCE.
2. This week: call the remaining nine Priority 1 prospects in BD-score order; confirm the directory-sourced owner names on each call.
3. Next two weeks: research team closes the six Priority 2 gaps by phone and runs the manual registry lookups; correct the six source-data errors in a new column, not in the raw tabs.
4. Before any campaign launch: confirm service-area cities for AA Roofing, American Tree, Alignments Northwest and La Jolla Grooming; fix or build landing pages flagged in GOOGLE_ADS_OPPORTUNITY.
5. Within a month: resolve the two possible duplicate pairs and the Cunningsmiles record; decide the Ad Grants referral route for the five nonprofits.
6. Done on 8 October 2026: advertising activity checked for all 36 prospects (Section 4b). Keep the ADS RESEARCH tab current by re-running the Transparency Center and Meta Ad Library checks before each outreach wave.
7. Request GA4 or Search Console read access from Priority 1 prospects during the first call so traffic can be verified before campaign planning; do not substitute estimates.
8. Reconcile the prospect list with Search29: re-label the two existing Google Ads accounts and confirm whether Premo Media Group manages Orion Optical's ads.
