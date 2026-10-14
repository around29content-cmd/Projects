# Step 4: Google Ads suitability analysis

Date: 8 October 2026. Input: the 45 CLEANED_DATA records and the CLASSIFICATION evidence (website text fetched 8 Oct 2026). No new external research was used. Output: the GOOGLE_ADS_FIT tab (rows 1 to 46, 19 columns; industry summary A48:J65 and fit distribution A67:D73 as formulas), google_ads_fit.csv and step4-adsfit.py in the project folder.

Method: search intent and commercial intent are 0 to 10 judgements of how people search for each business type; customer value, urgency, geographic targeting, competition and fit are qualitative; every rating has a one-line reason in the sheet. No revenue or customer-value figures are asserted, and competition describes how contested the category is in search without naming any advertiser.

## Fit distribution

| Fit | All 45 | Prospects (36) | Internal (9) |
|---|---|---|---|
| Excellent | 6 | 6 | 0 |
| Strong | 10 | 10 | 0 |
| Moderate | 13 | 8 | 5 |
| Weak | 8 | 6 | 2 |
| Poor | 4 | 4 | 0 |
| Unknown | 4 | 2 | 2 |

Excellent: AA Roofing and Decking, Affordable Junk Removal, American Tree Excavation, Cunning Dental Group, Prime Care Dental Indy, VIP Pest Solutions.
Strong: Alignments Northwest, Axle Surgeons of Seattle, Clean and Clean by Cliff, La Jolla Grooming Co, Ocean View Lodging, Orion Opticals, Superior Coatings NW, Trans Landscaping, Workhub Tulsa, Zellersins.
Moderate (prospects): ASL Camguard, Calvary Cemetery, NorthWest Eco Clean, Occasions Paper, Pinpoint Resource, Top Dollar Pawn, Wheeler Sonoma Printing, Will Rogers Stage Foundation.
Weak (prospects): Around Cricket, Chili On The Green, DBSA OK, Next Level Prospect, Ornamental Grasses, The Bartan Company.
Poor: Kiwanis Club of Tulsa, Lab Rescue, Rosewood Parke, Tag OK.
Unknown: Brothers Micro Market, Cunningsmiles Implant Experts, Search29, Starling Education.

## Industry-level summary (all 45)

| Industry | Records | Avg search intent | Avg commercial intent | Excellent | Strong | Moderate | Weak | Poor | Unknown |
|---|---|---|---|---|---|---|---|---|---|
| Home Services | 8 | 8.0 | 7.9 | 4 | 3 | 1 | 0 | 0 | 0 |
| Dental | 3 | 8.7 | 8.0 | 2 | 0 | 0 | 0 | 0 | 1 |
| Medical | 1 | 8.0 | 7.0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Healthcare (nonprofit support) | 1 | 6.0 | 2.0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Automotive | 3 | 6.3 | 7.3 | 0 | 2 | 1 | 0 | 0 | 0 |
| Retail | 4 | 5.5 | 5.3 | 0 | 0 | 2 | 2 | 0 | 0 |
| Financial Services | 1 | 7.0 | 7.0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Insurance | 1 | 7.0 | 7.0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Hospitality | 1 | 9.0 | 8.0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Real Estate (coworking) | 1 | 7.0 | 7.0 | 0 | 1 | 0 | 0 | 0 | 0 |
| B2B Services | 1 | 6.0 | 6.0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Education | 4 | 6.3 | 6.0 | 0 | 0 | 2 | 1 | 0 | 1 |
| Professional Services | 2 | 7.0 | 6.0 | 0 | 0 | 2 | 0 | 0 | 0 |
| Technology | 3 | 6.3 | 5.7 | 0 | 0 | 1 | 2 | 0 | 0 |
| Other | 9 | 4.3 | 4.0 | 0 | 1 | 2 | 2 | 4 | 0 |
| Unknown | 2 | - | - | 0 | 0 | 0 | 0 | 0 | 2 |
| Total | 45 | 6.5 | 6.1 | 6 | 10 | 13 | 8 | 4 | 4 |

## Reading the summary

- Home Services and Dental are the natural core: 11 records, average search intent 8 or above, 6 Excellent and 3 Strong, phone-call and quote conversions, high or emergency urgency. Competition is high in every one of these categories, so budgets must be real.
- Automotive splits into two niche B2B operators with low competition and emergency or scheduled demand (Strong) and one national product brand (Moderate).
- Hospitality, Medical, Insurance and coworking each contribute one Strong prospect with clear booking, appointment or quote conversions; insurance and hotel terms are expensive.
- Retail is Moderate at best: store-visit campaigns on carried brands or local formalwear terms, with no online sales evident for most.
- The nine "Other" records average 4.3 search intent and 4.0 commercial intent; four are Poor and two Weak because they are nonprofits or associations with no commercial conversion. Five records are marked as candidates for a nonprofit grant-based advertising program rather than paid search (DBSA OK, Kiwanis Club of Tulsa, Lab Rescue, Tag OK, Will Rogers Stage Foundation).
- Internal records: the two education sites would be Strong fits if their market location were known; the agency and software products face expensive, crowded keywords and are rated Moderate or Weak.

## Caveats

- Two prospects are outside the US market (Around Cricket, The Bartan Company) and are rated Weak for that reason, not for lack of search demand.
- Top Dollar Pawn is rated Moderate because firearms and loan products face Google Ads policy limits; a policy review is needed before any campaign.
- Four ratings are Unknown because the website is offline, blocked, missing or unreachable.
- Three Excellent or Strong prospects still need a verified location before geo-targeting (American Tree Excavation, Clean and Clean by Cliff, Zellersins), and VIP Pest Solutions' source phone number is mistyped.
- Whether any prospect already advertises on Google was not assessed in this step; it is a verification task for a later stage.
