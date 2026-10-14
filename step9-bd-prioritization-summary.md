# Step 9: Business development prioritization

Date: 8 October 2026. Scope: all 45 records (36 prospects, 9 internal Around29 records). Outputs in the sheet: BD_PRIORITIZATION (45 ranked rows, method block at rows 48-63) and BD_LISTS (Top 10, Top 25, Immediate Outreach, Enrichment Required, Research Required, Deprioritized). Local copies: bd_prioritization.csv, bd_lists.csv, step9-bd-prioritization.py.

## Model

The BD score is not a sort by Google Ads score. It blends five dimensions, each 0-100, each with a visible basis column in the sheet:

| Dimension | Weight | Source |
|---|---|---|
| A. Google Ads Opportunity | 40% | Step 5 total score |
| B. Contactability | 20% | Step 6: phone verified on site 40 / valid but unverified 25 / conflicting 15; email verified 25 / directory 12; named contact on official source 35 / directory 20 / first name only 12 |
| C. Commercial Attractiveness | 15% | Step 5 customer value + scalability + industry fit, scaled to 100 |
| D. Research Confidence | 10% | Step 5 confidence (High 70 / Medium 45 / Low 20) plus Step 6 verification (+30 / +15 / +5) |
| E. Personalization Potential | 15% | Step 8 readiness (Ready 100 / After Research 75 / Missing 10); if no hook, Step 4 fit (60 / 45 / 25 / 15 / 10) |

Final priority is rule-based, then rank orders by priority and BD score:

- Priority 1 Contact Now: Step 5 Tier 1 or 2 and Step 8 Ready to Contact.
- Priority 2 Contact After Enrichment: Tier 1 or 2 with Step 8 Contact After Research.
- Priority 3 Research / Nurture: Tier 3 with Step 4 fit Moderate, Strong or Unknown.
- Priority 4 Deprioritize: Tier 4, or Tier 3 with Weak or Poor fit, or an internal Around29 record.

## Results

| Priority | Prospects | Internal | Total |
|---|---|---|---|
| 1 Contact Now | 13 | 0 | 13 |
| 2 Contact After Enrichment | 6 | 0 | 6 |
| 3 Research / Nurture | 6 | 0 | 6 |
| 4 Deprioritize | 11 | 9 | 20 |

### Top 10 (external prospects)

| Rank | Business | Industry | Ads score | Contactability | Commercial | BD score | Priority |
|---|---|---|---|---|---|---|---|
| 1 | VIP Pest Solutions | Home Services (pest) | 88.0 | 95 | 91 | 92.9 | 1 |
| 2 | Prime Care Dental Indy | Dental | 92.5 | 75 | 100 | 92.0 | 1 |
| 3 | AA Roofing and Decking | Home Services | 90.5 | 85 | 94 | 90.8 | 1 |
| 4 | Zellers Group (Zellersins) | Insurance | 77.0 | 100 | 91 | 89.5 | 1 |
| 5 | Affordable Junk Removal | Home Services | 87.0 | 100 | 80 | 89.3 | 1 |
| 6 | Superior Coatings NW | Home Services (painting) | 85.0 | 85 | 89 | 87.8 | 1 |
| 7 | La Jolla Grooming Co | Pet services | 75.0 | 100 | 60 | 84.0 | 1 |
| 8 | Wheeler-Sonoma Printers | B2B Services | 70.0 | 100 | 71 | 83.7 | 1 |
| 9 | Alignments Northwest | Automotive (B2B) | 78.5 | 77 | 77 | 83.3 | 1 |
| 10 | American Tree Excavation | Home Services (tree) | 80.0 | 72 | 86 | 81.8 | 1 |

Ranks 11-13 (also Priority 1): Northwest Eco Clean, Workhub Tulsa, Clean & Clear by Cliff.

### How the blend changed the order

- Cunning Dental Group has the second-highest Google Ads score (91.5) but drops to rank 14 and Priority 2: no email, current owner unknown, possible new management.
- Orion Optical (85.5) drops to rank 15 and Priority 2: no owner named and the on-file email is a third-party agency.
- Zellers Group rises from a 77 Ads score to rank 4: president, phone, email and address all verified on the official site, and Medicare enrollment is underway.
- Wheeler-Sonoma Printers and La Jolla Grooming rise on full contactability and verified owners despite mid-70s Ads scores.
- Axle Surgeons of Seattle (84) falls to rank 17: no person, no email, unconfirmed brand relationship.

### Enrichment required (Priority 2)

Cunning Dental Group, Orion Optical, Trans Landscaping, Axle Surgeons of Seattle, Calvary Cemetery, Ocean View Lodging. In every case the gap is a decision-maker name or a conflicting phone/email, closable with one call to the verified main line.

### Research required (Priority 3)

Top Dollar Pawn (policy review needed), Pinpoint Resource, Occasions Paper, ASL Camguard (no contact data at all), Cunningsmiles Implant Experts (site dead; likely duplicate of Cunning Dental), Will Rogers Stage Foundation.

### Deprioritized (Priority 4)

Eleven prospects: The Bartan Company and Around Cricket (outside the US market), Ornamental Grasses, Next Level Prospect, DBSA OK, Chili On The Green, Kiwanis Club of Tulsa, Lab Rescue, Tag OK, Brothers Micro Market (site down), Rosewood Parke (not a business). Five of these are nonprofits better served by the Google Ad Grants programme than by paid search. Plus the nine internal Around29 records, which are not sales prospects.

## Caveats

Contactability and personalization scores depend on the Step 6 research, which could not reach state registries or several directories; those values carry Needs Verification flags in ENRICHED_PROSPECTS. Weights are a judgement and are exposed in the sheet so they can be changed. No outreach has been made.
