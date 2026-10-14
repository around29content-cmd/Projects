# Step 5: Google Ads opportunity scoring model

Date: 8 October 2026. Inputs: CLEANED_DATA, CLASSIFICATION and GOOGLE_ADS_FIT (45 records). No new external research. Outputs in the sheet: SCORING_METHOD (weights and rubric), SCORE_FACTOR_DETAIL (450 factor rows with rating, points, explanation, evidence, confidence) and GOOGLE_ADS_OPPORTUNITY_SCORE (45 scored records, tier distribution at rows 48-53). Local copies: scoring_method.csv, score_factor_detail.csv, google_ads_opportunity_score.csv, step5-score.py.

## Methodology (fixed before ranking)

| Factor | Weight | Rating source | Points |
|---|---|---|---|
| Industry Google Ads Fit | 15 | CLASSIFICATION primary industry | Rubric label 0-15 (Home Services and Dental 15; nonprofits, clubs and associations 0-4; Unknown 3) |
| Search Intent | 15 | GOOGLE_ADS_FIT search intent 0-10 | Step 4 score x 1.5; Unknown 3 |
| Commercial Intent | 15 | GOOGLE_ADS_FIT commercial intent 0-10 | Step 4 score x 1.5; Unknown 3 |
| Customer Value Potential | 15 | GOOGLE_ADS_FIT customer value | Very High 15, High 12, Moderate 8, Low 4, Very Low 1, Unknown 3 |
| Conversion Potential | 10 | GOOGLE_ADS_FIT conversion actions plus verified site path | Direct response 10 or 9, forms 7, store visits 6, tickets 5, donations 3, none 0, Unknown 2 |
| Geographic Targeting | 10 | CLASSIFICATION scope and basis | Local verified 10, hyperlocal 9, regional verified 9, local inferred 6, national 6, national online 5, outside US 2, Unknown 2 |
| Urgency | 5 | GOOGLE_ADS_FIT urgency | Emergency 5, High 4, Moderate 3, Low 1, Unknown 1 |
| Business Scalability | 5 | Business model, scope and locations on the site | 5 to 1 by capacity to absorb leads; nonprofit 1; Unknown 1 |
| Digital Readiness | 5 | Website status observed 8 Oct 2026 | Online booking 5, contact path plus service area 4, contact path 3, limited 2, site in progress 1, no site 0 |
| Data Completeness | 5 | CLEANED_DATA contactability | Valid phone 2, email 1, verified location 1, clean identity 1 |

Design rules: the score measures attractiveness as a Google Ads client, so data completeness is capped at 5 points and website quality only enters through Digital Readiness (5 points). Unknown ratings receive the lowest or near-lowest points and are marked Low confidence; nothing is inferred to earn points. Each factor row in SCORE_FACTOR_DETAIL carries its rating, points (looked up from the rubric), a one-line explanation, the upstream evidence field and a confidence level. The total is a SUMIFS over those rows, so a rubric change in SCORING_METHOD re-scores every record.

Tiers: 85-100 Tier 1 Immediate Opportunity; 70-84 Tier 2 Strong Prospect; 50-69 Tier 3 Research/Nurture; 0-49 Tier 4 Low Priority.

## Ranking

| Rank | Record | Business | Score | Tier | Confidence |
|---|---|---|---|---|---|
| 1 | P-25 | Prime Care Dental Indy | 92.5 | 1 | High |
| 2 | P-12 | Cunning Dental Group | 91.5 | 1 | High |
| 3 | P-01 | AA Roofing and Decking | 90.5 | 1 | High |
| 4 | P-32 | VIP Pest Solutions | 88.0 | 1 | High |
| 5 | P-02 | Affordable Junk Removal | 87.0 | 1 | High |
| 6 | P-22 | Orion Opticals | 85.5 | 1 | High |
| 7 | P-27 | Superior Coatings NW | 85.0 | 1 | High |
| 8 | P-07 | Axle Surgeons of Seattle | 84.0 | 2 | High |
| 9 | P-31 | Trans Landscaping | 83.5 | 2 | High |
| 10 | P-04 | American Tree Excavation | 80.0 | 2 | High |
| 11 | P-35 | Workhub Tulsa | 79.0 | 2 | High |
| 12 | P-03 | Alignments Northwest LLC | 78.5 | 2 | High |
| 12 | P-21 | Ocean View Lodging | 78.5 | 2 | High |
| 14 | P-36 | Zellersins | 77.0 | 2 | High |
| 15 | P-19 | NorthWest Eco Clean | 75.5 | 2 | High |
| 16 | P-16 | La Jolla Grooming Co | 75.0 | 2 | High |
| 17 | P-09 | Calvary Cemetery | 71.0 | 2 | High |
| 17 | P-11 | Clean and Clean by Cliff | 71.0 | 2 | High |
| 17 | I-01 | Around29 Center for Enriched Studies | 71.0 | 2 | High (location unknown) |
| 20 | P-33 | Wheeler Sonoma Printing | 70.0 | 2 | High |
| 21 | P-13 | Cunningsmiles Implant Experts | 68.0 | 3 | Low |
| 22 | P-30 | Top Dollar Pawn and Check Cashing | 67.0 | 3 | High |
| 23 | P-06 | ASL Camguard | 64.0 | 3 | High |
| 24 | P-24 | Pinpoint Resource | 61.5 | 3 | High |
| 24 | I-02 | Around29 Digital Media Solutions | 61.5 | 3 | High |
| 26 | I-05 | Lead You | 60.5 | 3 | High |
| 27 | P-05 | Around Cricket | 58.5 | 3 | High |
| 28 | P-20 | Occasions Paper | 58.0 | 3 | High |
| 28 | I-09 | Starling Wonder Kids | 58.0 | 3 | Medium |
| 30 | P-34 | Will Rogers Stage Foundation | 57.5 | 3 | High |
| 30 | I-04 | Send29 | 57.5 | 3 | High |
| 30 | I-07 | Around29.us | 57.5 | 3 | High (location unknown) |
| 33 | P-23 | Ornamental Grasses | 51.5 | 3 | High |
| 34 | P-29 | The Bartan Company | 49.0 | 4 | High |
| 35 | P-18 | Next Level Prospect | 47.5 | 4 | High |
| 36 | P-14 | DBSA OK | 43.0 | 4 | High |
| 37 | P-10 | Chili On The Green | 36.5 | 4 | High |
| 38 | P-17 | Lab Rescue | 34.0 | 4 | High |
| 38 | I-06 | Around29 themes | 34.0 | 4 | Low |
| 40 | P-15 | Kiwanis Club of Tulsa | 31.5 | 4 | High |
| 41 | P-28 | Tag OK | 29.5 | 4 | High |
| 42 | I-08 | Starling Education | 28.0 | 4 | Low |
| 43 | P-08 | Brothers Micro Market | 22.0 | 4 | Low |
| 44 | I-03 | Search29 | 19.0 | 4 | Low |
| 45 | P-26 | Rosewood Parke | 17.5 | 4 | High |

## Tier distribution

| Tier | All 45 | Prospects (36) | Internal (9) |
|---|---|---|---|
| Tier 1 Immediate Opportunity | 7 | 7 | 0 |
| Tier 2 Strong Prospect | 13 | 12 | 1 |
| Tier 3 Research/Nurture | 13 | 8 | 5 |
| Tier 4 Low Priority | 12 | 9 | 3 |
| Average score | 61.9 | 65.0 | 49.7 |

## Confidence flags

- Low overall confidence (4 or more factors rated Unknown): Brothers Micro Market, Search29, Starling Education (8 unknown factors each), Cunningsmiles Implant Experts (6), Around29 themes (5). Their scores are floors, not estimates; Cunningsmiles in particular would likely reach Tier 1 if its site and location were verified, since it is a dental implant practice.
- Medium: Starling Wonder Kids (conversion path and location unknown).
- Two Tier 2 or 3 records are penalised only for an unverified location: Around29 Center for Enriched Studies and Around29.us.
- Three Tier 1 or 2 prospects still need a confirmed service area before any geo-targeting: American Tree Excavation, Clean and Clean by Cliff, Zellersins. VIP Pest Solutions scores 2/5 on data completeness because its source phone number is mistyped.
- Top Dollar Pawn sits in Tier 3 partly because of Google Ads policy limits on loans and firearms; a policy review is required before it could move up.

## What was not done

No sales pitch, outreach copy or external research. Whether any prospect already runs Google Ads was not checked. Rankings are relative to this list only.
