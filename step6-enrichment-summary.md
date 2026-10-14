# Step 6: Prospect data enrichment

Date: 8 October 2026. Scope: the 19 Tier 1 and Tier 2 prospects from Step 5, plus Cunningsmiles Implant Experts (P-13, Tier 3 only because every field was unknown; a dental implant practice is high potential). Internal record I-01 (Tier 2) is the agency's own school site and was not researched. Outputs in the sheet: ENRICHED_PROSPECTS (20 rows x 28 columns) and MISSING_DATA_QUEUE (130 rows, summary at rows 133-152). Local copies: enriched_prospects.csv (full-length cells), missing_data_queue.csv, step6-enrich-compile.py, and the per-group research JSON with a source URL for every value in step6-research-json/.

## Method

Research ran in eight parallel passes over the public web only: official website first (home, about, contact, services, locations, footer and schema markup), then profiles the business controls (BBB accredited profile, own Facebook or LinkedIn), then directories and registry mirrors (BBB, OpenCorporates mirrors of the California and Washington registries, Chambers of Commerce, Nextdoor, Yelp search snippets), then professional profiles. Every value carries the URL where it was seen and one of six statuses: Verified - official website, Verified - official profile, Official registry, Directory - Needs Verification, Conflicting - Needs Verification, Not Found. Nothing was guessed: no email addresses were constructed from name patterns, no owner was inferred from a domain registration, and a field was marked Not Found after two reasonable attempts. In the sheet, any value not taken from the official site carries a [Needs Verification] suffix.

Limits: the Washington, California, Oklahoma and Indiana state registries and licence lookups are JavaScript applications that could not be fetched, so legal-entity details rest on registry mirrors or BBB. Yelp, Facebook, LinkedIn profile pages, KING 5, the Diocese of Tulsa and several directories blocked direct fetches (403), so values from them come from search snippets and are labelled accordingly.

## Results

| Measure | Count |
|---|---|
| Prospects researched | 20 |
| Phone verified on official site | 18 (plus 1 conflicting, 1 not live) |
| Phone on file wrong or conflicting | 2 (VIP Pest Solutions, Ocean View Lodging) |
| Email found where file had none | 13 |
| Email still Not Found | 3 (Prime Care Dental, Cunning Dental, Axle Surgeons) plus P-13 |
| Named decision-maker found | 14 (7 verified on official sources, 7 from BBB/Chamber/LinkedIn - Needs Verification) |
| Street address verified on official site | 12 |
| Service area confirmed on official site | 14 |
| Verification status Verified (phone, website, address all official) | 11 |
| Partially Verified | 4 |
| Needs Verification (a conflict in phone, email or address) | 5 |

### Corrections to the Prospects tab (not applied; raw data untouched)

- VIP Pest Solutions: file phone 80560833847 has an extra digit; official site shows (805) 608-3847. Legal name is Veritas Innovative Pest & Termite Solutions (Santa Maria, CA; serves San Luis Obispo, Santa Barbara and Ventura counties).
- Ocean View Lodging: file phone (707) 964-7366 appears nowhere; every page of the site shows (707) 964-1951.
- Orion Opticals: file email james@premomediagroup.com is a Tacoma marketing agency, not the business; the store publishes no email (Nextdoor lists info@orionoptical.com, unverified).
- Clean and Clean by Cliff: trading name is Clean & Clear by Cliff (window cleaning, Bonney Lake / Lake Tapps, WA).
- Zellersins: trading name Zellers Group, legal name Zellers Insurance & Financial Services Inc.; zellersins.com redirects to zellersgroup.com.
- Axle Surgeons of Seattle: file email mobileaxleservice@gmail.com appears on no public source.
- Cunningsmiles Implant Experts: the subdomain returns 403/404 and nothing on cunningdental.com or elsewhere links it to Cunning Dental Group. Recommend treating it as a dead microsite rather than a separate prospect until confirmed.

### Decision-makers found on official sources

Dr. Vijaya Palaparthi (Prime Care Dental, dentist; owner not stated), Dr. Ronald Cunning (Cunning Dental founder; current owner not stated), Jamie Parkins (VIP Pest, CEO per BBB accredited profile), Ashley Ramirez (Affordable Junk Removal, owner per BBB accredited profile), Dean Zellers (Zellers Group, President), Garrett Larson (La Jolla Grooming, founder), Baird Conner (Wheeler-Sonoma Printers, owner). Names resting only on directories: Ahmed R. Al-Jebori (AA Roofing), Donovan Peters (Superior Coatings), Kristian Guttu (American Tree), Martez Johnson (Northwest Eco Clean), Cliff McIntosh (Clean & Clear by Cliff), Katherine Pohjola (Cunning Dental GM, 2023 TV segment), Carla (Workhub Tulsa, first name only).

## Missing-data queue

130 open items: 11 High (Tier 1 core contact fields), 63 Medium, 56 Low. Most common gaps: marketing contact (20 of 20 - none of these businesses publishes one), owner (18), founder (17), contact role (13), contact name (12), address (8), email (7). Seven of the queue rows concern a Prospects-tab value that differs from the official site. The suggested next action for most items is a single discovery call; the queue gives the exact question to ask per prospect.

## What was not done

No outreach, pitch or campaign work. State registry and licence status were not confirmed. No Google Business Profile data was collected (not fetchable). No Search29 or other internal data was used.
