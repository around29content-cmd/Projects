# Step 3: Business and industry classification

Date: 8 October 2026. Input: the 45 records in CLEANED_DATA. Output: the CLASSIFICATION tab of the workbook (rows 1 to 46, 16 columns; COUNTIF distribution blocks in A48:B116), classification.csv and the rule file step3-classify.py in the project folder. No record was scored.

Evidence tiers: Verified = the business's own website text (title, meta description, page text) fetched 8 Oct 2026; Inferred = business name, domain or phone area code only; Unknown = no usable evidence. Industry evidence: 41 Verified, 2 Inferred (P-13, I-08), 2 Unknown (P-08, I-03). Customer acquisition channels are Inferred from the business type for all records except 11 where the site itself shows the channel (online store, booking, ticketing or donation page).

Fields created: primary_industry, industry_evidence, secondary_industry, business_model (multi-tag), model_evidence, customer_type, customer_acquisition_model (multi-tag), acquisition_evidence, service_type, geographic_scope, geographic_basis, classification_confidence, evidence_source, classification_notes.

## 1. Industry distribution

| Primary industry | All 45 | Prospects (36) | Internal (9) |
|---|---|---|---|
| Home Services | 8 | 8 | 0 |
| Other (see note) | 9 | 9 | 0 |
| Retail | 4 | 4 | 0 |
| Education | 4 | 1 | 3 |
| Dental | 3 | 3 | 0 |
| Automotive | 3 | 3 | 0 |
| Technology | 3 | 0 | 3 |
| Professional Services | 2 | 0 | 2 |
| Medical | 1 | 1 | 0 |
| Healthcare | 1 | 1 | 0 |
| Financial Services | 1 | 1 | 0 |
| Insurance | 1 | 1 | 0 |
| Hospitality | 1 | 1 | 0 |
| Real Estate | 1 | 1 | 0 |
| B2B Services | 1 | 1 | 0 |
| Unknown | 2 | 1 | 1 |
| Legal, Construction, Restaurant/Food, Ecommerce, Beauty & Wellness, Fitness, Travel, Manufacturing, Logistics | 0 | 0 | 0 |

"Other" holds nine organisations the category list does not cover: a cemetery, a community event, a service club, a pet groomer, two animal-welfare nonprofits, a homeowners association, an event-rental company and a performing-arts foundation. Construction (4), B2B Services (6), Healthcare (3) and Ecommerce (3) appear as secondary industries.

## 2. Business-model distribution (records carrying the tag)

| Tag | All 45 | Prospects (36) |
|---|---|---|
| B2C | 32 | 29 |
| Local service | 18 | 18 |
| B2B | 17 | 12 |
| Recurring service | 10 | 9 |
| Appointment-based | 9 | 7 |
| Lead generation | 8 | 8 |
| High-ticket service | 8 | 8 |
| Project-based | 8 | 6 |
| Subscription | 7 | 3 |
| Ecommerce | 6 | 3 |
| Retail | 6 | 6 |
| Emergency service | 3 | 3 |
| Consultation-based | 3 | 3 |
| Multi-location | 2 | 2 |
| Manufacturer / Distributor | 1 / 1 | 1 / 1 |
| Other (nonprofit, event, association, lodging) | 9 | 9 |
| Unknown | 3 | 1 |
| Franchise, Marketplace | 0 | 0 |

Customer type (all 45): B2C 20, B2C and B2B 13, B2B 8, members and donors 2, Unknown 2.

## 3. Geographic distribution

| Scope | All 45 | Prospects (36) |
|---|---|---|
| Local | 18 | 18 |
| Local (India) | 2 | 2 |
| Regional | 12 | 12 |
| National | 2 | 2 |
| National/International (online) | 3 | 0 |
| Unknown | 8 | 2 |

Prospects by state (verified site text where available, otherwise area code): Oklahoma 12 (Tulsa, Broken Arrow, Norman, Oklahoma City), Washington 10 (Puget Sound), California 8, Indiana 1, India 2, not stated 3 (P-08, P-13, P-18). Three prospects rely on an area-code hint for location (P-04, P-11, P-36).

## 4. Major classification patterns

- Local and regional service businesses with lead-generation or appointment models are the largest group: 16 of 36 prospects (Home Services 8, Automotive 3, Dental 3, Medical 1, Insurance 1), 14 of them verified from site text.
- Nonprofits and community organisations are the second group: 9 of 36 prospects run on donations, membership or ticket sales rather than commercial lead generation.
- Retail and walk-in businesses: 5 of 36 (stationery, menswear, pawn shop, plant nursery, cricket store); only the cricket store has a verified online shop, and it is in India.
- Prospects cluster in three markets: Tulsa and Oklahoma City (12), the Tacoma and Seattle corridor (10), and California (8).
- The Internal tab is Around29's own portfolio: two agency sites, three online products (email marketing, lead-generation software, website themes) and three education entities.
- Site text revealed one new relationship: Chili On The Green is presented by the Kiwanis Club of Tulsa (P-10 and P-15). The Cunning and Starling pairs remain possible duplicates.

## 5. Classification problems

- The category list has no class for nonprofits, pet services, funeral services, event services, arts or community associations; 9 records sit in "Other" with a qualifier. Adding "Nonprofit / Community" and "Pet Services" would clear most of them.
- Several businesses span two categories (optometry with eyewear retail; pawn loans with resale retail; an oil-additive brand that manufactures and sells online). Secondary industry carries the second class.
- Acquisition channels cannot be verified from a website alone; they are Inferred for 34 of 45 records and only partly verified for 11.
- Two sites were inaccessible (P-08 returned 503, P-13 returned 403), one record has no URL (I-03) and one Internal site did not respond (I-08); these are Unknown or name-inferred with Low confidence.
- Four websites are not marked Delivered (P-13, P-18, I-02, I-04), so their current content may change.
- Two prospects operate in India (P-05, P-29), outside a US prospect pool.
- The Ecommerce tag counts ticketing and self-serve platforms as well as product stores; only P-05 and P-06 are product stores.
- Nine Internal records are classified for completeness but are Around29's own properties.

## 6. Examples of ambiguous businesses

- Ornamental Grasses (P-23): the page mentions a nursery and visits by appointment, but reads partly as a gardening information site; retail model not fully evident (Medium).
- Zellersins (P-36): the site title is "Zellers Group" with no description; insurance is verified only from body text, and the location is an area-code hint (Medium).
- ASL Camguard (P-06): a product brand with an online store and a toll-free number, based in Tulsa; national scope inferred (Medium).
- Calvary Cemetery (P-09): a service business by model, probably a religious nonprofit by structure; nonprofit status not verified.
- Chili On The Green (P-10): an annual event that is at once a food competition, a ticketed event and the fundraising arm of a service club.
- Next Level Prospect (P-18): education services delivered by a 501(c)(3); "nationwide" wording but no stated base.
- Brothers Micro Market (P-08): site offline; the name suggests vending or micro markets, which was not enough to classify.
- Around29 themes (I-06): the only evidence is the title "Themes"; classified Technology with Low confidence.
