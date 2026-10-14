# Step 2: Data cleaning and standardization

Date: 8 October 2026. Source: Prospects!A2:H37 (36 records) and Internal!A2:H10 (9 records) of the "Around29 Google Ads Prospects" workbook, read through the Sheets API. The raw tabs were not modified. Outputs: two new tabs in the same workbook, CLEANED_DATA (45 records, 35 columns) and DATA_QUALITY_FLAGS (98 flag rows), plus local copies cleaned_data.csv, data_quality_flags.csv and the rule script step2-clean.py.

Labels: Unknown = no source data; Needs Verification = source data present but doubtful; Known = present and consistent. Nothing was inferred or looked up.

## 1. Cleaning rules

| Rule | What it does | Records affected |
|---|---|---|
| R1 Business name | Trim and collapse whitespace; convert all-lowercase names to Title Case; keep the original in business_name_original | 1 changed (P-13); 45 originals kept |
| R2 Website URL | Lower-case; strip scheme and www (none present); strip trailing slash; derive domain_std and root_domain; url_std = https://domain/ as a convention | 44 standardized (35 had a trailing slash); 1 Unknown (I-03) |
| R3 Phone | Extract digits; valid 10-digit North American numbers become phone_e164 (+1...), phone_display, phone_area_code and an area-code region hint; anything else is Needs Verification with the reason; blank is Unknown | 29 valid; 4 Needs Verification (P-05, P-32, I-01, I-09); 12 Unknown |
| R4 Email | Lower-case and trim; syntax check; extract domain; classify against the website root domain (matches / different business domain / free-mail) | 6 validated: 1 Known, 5 Needs Verification; 39 Unknown |
| R5 Contact name | No source column: Unknown; first names found inside email addresses are recorded as hints only | 45 Unknown; 2 hints (P-08 Peter, P-22 James) |
| R6 Location | No source column: city, state and country are Unknown; area_code_region_hint holds the public area-code assignment, not a verified location | 45 Unknown; 29 hints |
| R7 Industry | No source column: Unknown; the Service value is kept as service_delivered | 45 Unknown |
| R8 Record reference | record_id (P-01..P-36, I-01..I-09), source_tab and source_row | 45 |
| R9 Duplicates | Classify every record Exact / Likely / Possible / Unique on name, domain, phone and email (see section 3) | 45 evaluated |
| R10 Flags | One DATA_QUALITY_FLAGS row per issue per record, plus dataset-level rows (record_id = ALL); flag_count and high_severity_flags are formulas | 98 rows: 59 High, 27 Medium, 12 Low |

## 2. Number of records affected

| Measure | Count | % of 45 |
|---|---|---|
| Records in CLEANED_DATA | 45 | 100% |
| Name standardized (case) | 1 | 2.2% |
| URL standardized | 44 | 97.8% |
| Phone normalized to E.164 | 29 | 64.4% |
| Phone Needs Verification | 4 | 8.9% |
| Phone Unknown | 12 | 26.7% |
| Email Known | 1 | 2.2% |
| Email Needs Verification | 5 | 11.1% |
| Email Unknown | 39 | 86.7% |
| Contact name Unknown | 45 | 100% |
| City / state / country Unknown | 45 | 100% |
| Industry Unknown | 45 | 100% |
| Records with at least one High flag | 39 | 86.7% |
| Records with no High flag | 6 | 13.3% |

## 3. Duplicate handling

Classes: Exact duplicate = identical name, domain, phone and email. Likely duplicate = same domain, phone or email with a different name. Possible duplicate = shared distinctive leading name token (6 or more characters) with different domains. Unique = none of these. The partner's own brand token (around29) is excluded, otherwise the Internal records and Around Cricket would have matched on "around".

| Class | Records | Which |
|---|---|---|
| Exact duplicate | 0 | |
| Likely duplicate | 0 | |
| Possible duplicate | 4 | P-12 Cunning Dental Group and P-13 cunningsmiles implant experts (token "cunning"; cunningdental.com vs cunningsmiles.implant-experts.com); I-08 Starling Education and I-09 Starling Wonder Kids (token "starling"; starling.education vs starlingwonderkids.com) |
| Unique | 41 | all others |

Nothing was deleted or merged. Each possible duplicate carries duplicate_of, duplicate_reason and a POSSIBLE_DUPLICATE flag. P-03 Alignments Northwest LLC and P-07 Axle Surgeons of Seattle share area code and exchange 253-777; they are kept Unique with a POSSIBLE_RELATED_ENTITY flag because names, domains and emails differ.

## 4. Standardization decisions

- Phones are stored as text in E.164 (+1XXXXXXXXXX) plus a (XXX) XXX-XXXX display form; a number is only standardized when the exchange and area code follow North American numbering rules.
- The two Internal phones displayed as 9.16E+11 and 9.19E+11 were read at full precision (916306000000 and 918640000000); both are 12 digits ending in six zeros, so the real numbers cannot be recovered and they are Needs Verification.
- url_std uses https:// as a convention; the source has no scheme and no URL was fetched. This is recorded as a dataset-level Low flag.
- Only one name was changed (lower case to Title Case). Spelling conflicts between a name and its domain (Clean and Clean / cleanandclear, Zellersins / zellersgroup) were flagged, not corrected.
- Email status is Known only when the email domain matches the website domain. Free-mail addresses and third-party domains are Needs Verification.
- Empty source cells are shown as "(blank)" in the *_original columns so a blank is distinguishable from a missing read.
- Internal records are kept in CLEANED_DATA with an INTERNAL_TAB_RECORD flag rather than dropped, because whether they are prospects is a business decision.
- Industry, location and contact fields exist in the structure but hold Unknown; they are not populated from name words or area codes.

## 5. Remaining data gaps

| Gap | Records | Status |
|---|---|---|
| Contact / decision maker | 45 | Unknown |
| City, state, country | 45 | Unknown |
| Industry / category | 45 | Unknown |
| Email | 39 Unknown, 5 Needs Verification | |
| Phone | 12 Unknown, 4 Needs Verification | |
| Website URL | 1 Unknown (I-03 Search29) | |
| Website not Delivered | 4 (P-13, P-18, I-02, I-04) | Needs Verification |
| Possible duplicates | 2 pairs | Needs Verification |
| Prospect status of Internal records | 9 | Needs Verification |
| Live URL check, ads activity, tracking, Business Profile, budget | 45 | Not in scope of this step |

## 6. Cleaned structure

CLEANED_DATA columns (35): record_id, source_tab, source_row, partner, business_name_original, business_name_std, website_url_original, domain_std, root_domain, url_std, phone_original, phone_e164, phone_display, phone_area_code, area_code_region_hint, phone_status, email_original, email_std, email_domain, email_domain_type, email_status, contact_name, contact_name_hint, city, state, country, industry_category, service_delivered, plan, website_project_status, duplicate_class, duplicate_of, duplicate_reason, flag_count, high_severity_flags.

DATA_QUALITY_FLAGS columns (10): record_id, business_name, source_tab, source_row, field, flag_code, severity, original_value, detail, recommended_action.

Flag codes used: CONTACT_FIELD_ABSENT, LOCATION_FIELD_ABSENT, INDUSTRY_FIELD_ABSENT, INTERNAL_TAB_NO_HEADER, SHARING_ANYONE_CAN_EDIT, URL_SCHEME_UNVERIFIED (dataset level); EMAIL_MISSING, EMAIL_FREEMAIL, EMAIL_DOMAIN_MISMATCH, EMAIL_ROLE_MAILBOX, PHONE_MISSING, PHONE_INVALID_FORMAT, PHONE_STORED_AS_NUMBER, PHONE_UNFORMATTED_IN_SOURCE, URL_MISSING, URL_THIRD_PARTY_SUBDOMAIN, NAME_DOMAIN_MISMATCH, NAME_CASE_STANDARDIZED, NAME_LOOKS_LIKE_HANDLE, CONTACT_NAME_HINT, WEBSITE_NOT_DELIVERED, INTERNAL_TAB_RECORD, POSSIBLE_DUPLICATE, POSSIBLE_RELATED_ENTITY (record level).
