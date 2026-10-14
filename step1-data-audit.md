# Step 1: Raw data audit of "Around29 Google Ads Prospects"

Audit date: 8 October 2026. Source: the Google Sheet as read on 8 Oct 2026 (file last modified 7 Oct 2026, 18:36 UTC). Only the raw cell contents were analysed; no business was researched and no cell was changed. Labels: Known (present and consistent), Unknown (absent), Needs Verification (present but doubtful).

## 1. Dataset overview

| Tab | Range with data | Header row | Records | Columns |
|---|---|---|---|---|
| Prospects | A1:H37 | Yes (row 1) | 36 | 8 |
| Internal | A1:H10 | No (A1:H1 is one merged cell titled "Internal") | 9 | 8 (by position only) |
| Total | | | 45 | |

The Internal tab's names (Around29, Search29, Send29, Lead You, Around29 themes, Around29.us, two Starling schools) suggest Around29-owned properties rather than prospects. Whether any of them is a prospect: Needs Verification.

## 2. Column dictionary (Prospects; Internal follows the same order without headers)

| Col | Header | Appears to represent | Format observed | Filled (Prospects) | Filled (Internal) |
|---|---|---|---|---|---|
| A | Partner | Agency that owns the relationship; constant "Around29" | Text | 36/36 | 9/9 |
| B | Client | Business name | Text, mostly Title Case | 36/36 | 9/9 |
| C | Business URL | Website domain, no scheme or www; trailing slash on some | Text | 36/36 | 8/9 |
| D | Phone | Business phone number | "(xxx) xxx-xxxx" on 28; raw 11 digits on 1 | 29/36 | 4/9 (2 shown as 9.16E+11 / 9.19E+11, 1 raw 10 digits) |
| E | Email | Contact email address | Text, lower case | 6/36 | 0/9 |
| F | Service | Service Around29 delivered to the client ("Website Development" on every row); not the client's industry | Text | 36/36 | 9/9 |
| G | Plan | Around29 website plan: "Studio29" (30) or "Custom" (6) | Text | 36/36 | 9/9 (Custom 1) |
| H | Status | Website project status: "Delivered" (34), "Changes in Progress" (2); Internal adds "Build in Progress" (2) | Text | 36/36 | 9/9 |

No column holds a contact person, title, address, city, state, industry, ads status, budget or record ID.

## 3. Data-quality summary

Prospects tab (36 records):

| Metric | Count | % of total |
|---|---|---|
| Total records | 36 | 100% |
| Unique businesses (distinct names) | 36 | 100% |
| Duplicate records (exact) | 0 | 0% |
| Possible related entities (Needs Verification) | 1 pair | 2.8% |
| Missing website | 0 | 0% |
| Missing phone (blank) | 7 | 19.4% |
| Phone present but invalid format (Needs Verification) | 2 | 5.6% |
| Missing email | 30 | 83.3% |
| Missing contact person (no column exists) | 36 | 100% |
| Missing location (no column exists) | 36 | 100% |
| Missing industry (no column exists) | 36 | 100% |
| Incomplete records (missing phone and/or email) | 30 | 83.3% |
| Incomplete if contact, location and industry are required | 36 | 100% |

Internal tab (9 records):

| Metric | Count | % of total |
|---|---|---|
| Total records | 9 | 100% |
| Unique businesses | 9 | 100% |
| Duplicate records | 0 | 0% |
| Missing website | 1 (Search29) | 11.1% |
| Missing phone (blank) | 5 | 55.6% |
| Phone present but corrupted or unformatted (Needs Verification) | 3 | 33.3% |
| Missing email | 9 | 100% |
| Missing contact person / location / industry | 9 | 100% |
| Incomplete records | 9 | 100% |

## 4. Duplicate analysis

- Exact duplicate rows: none within or across the two tabs.
- Duplicate business names: none. One possible related pair: "Cunning Dental Group" (cunningdental.com) and "cunningsmiles implant experts" (cunningsmiles.implant-experts.com). Same business or not: Needs Verification.
- Duplicate domains: none. All 44 URLs are distinct; cunningsmiles.implant-experts.com is a subdomain of a different root domain (implant-experts.com).
- Duplicate phone numbers: none among the 29 Prospects values or the 4 Internal values. "Alignments Northwest LLC" (253) 777-7092 and "Axle Surgeons of Seattle" (253) 777-8811 share an area code and exchange; related or not: Needs Verification.
- Duplicate email addresses: none among the 6 values.

## 5. Missing-data analysis

| Field | Known | Unknown | Needs Verification |
|---|---|---|---|
| Business name | 36 | 0 | 0 |
| Website URL (string present) | 36 | 0 | 3 flagged for name/domain mismatch (see section 6); live status of all 36 is Unknown |
| Phone | 27 | 7 | 2 |
| Email | 1 (office@dbsaok.org, role mailbox on matching domain) | 30 | 5 (3 free-mail addresses; 2 on domains that differ from the business domain) |
| Contact / decision maker | 0 | 36 | 2 first names visible only inside email addresses (peter@brosdist.com, james@premomediagroup.com) |
| Location | 0 | 36 | 0 (area codes exist for 28 records but are not location data; (855) is toll-free) |
| Industry / category | 0 | 36 | 0 (Service column describes Around29's deliverable) |

Records with no phone: ASL Camguard, Chili On The Green, cunningsmiles implant experts, Lab Rescue, Rosewood Parke, Tag OK, Will Rogers Stage Foundation.

Phones needing verification: VIP Pest Solutions "80560833847" (11 digits, does not match a US pattern and does not start with country code 1); Around Cricket "(812) 121-2561" (exchange "121" is not a valid North American exchange, which must start with 2 to 9).

Emails needing verification: affordablejunkremoval916@gmail.com, alignmentsnw@gmail.com and mobileaxleservice@gmail.com (free-mail; ownership and role unverifiable, and the last does not contain the business name); peter@brosdist.com for Brothers Micro Market and james@premomediagroup.com for Orion Opticals (domain differs from the business domain, the second reads as a media company mailbox).

Records with no phone and no email: the 7 listed above (19.4%). Records with phone but no email: 23. Records with both: 6 (Affordable Junk Removal, Alignments Northwest LLC, Axle Surgeons of Seattle, Brothers Micro Market, DBSA OK, Orion Opticals).

Internal tab: Search29 has no URL; emails are absent on all 9; phones are blank on 5, shown in scientific notation on 2 (Around29 Center for Enriched Studies, Starling Wonder Kids) and raw on 1 (Starling Education, 6305992630).

## 6. Structural problems and inconsistent formatting

Structure:
1. No unique record ID in either tab.
2. The Internal tab has a merged title cell instead of a header row, so its columns are defined only by position; filters, sorting and imports will misread it.
3. Phone is stored as numbers on the Internal tab (scientific notation shows 12-digit numeric values) but as text on Prospects; mixed types in one logical column.
4. Two tabs share one schema and are split by ownership instead of by a flag column, which complicates counting and de-duplication.
5. Service, Plan and Status describe Around29's web project, not the prospect; there are no qualification fields.
6. The workbook is shared as "anyone with the link can edit", so anyone holding the URL can alter or delete prospect data; there is no change log or owner column.

Formatting inconsistencies:
- URL: 29 values end with "/" and 7 do not; none carries http(s) or www; one is a third-party subdomain.
- Phone: 28 formatted "(xxx) xxx-xxxx", 1 raw 11-digit string; Internal mixes formatted, raw 10-digit and scientific-notation numbers.
- Client names: "cunningsmiles implant experts" is all lower case; "NorthWest Eco Clean" uses mixed case; "Zellersins" and "Around29.us" read as handles or domains rather than business names.
- Name versus domain mismatches: "Clean and Clean by Cliff" vs cleanandclearbycliff.com; "Zellersins" vs zellersgroup.com; "Orion Opticals" vs orionoptical.com; "Around29 themes" vs studio29themes.com.

Suspicious URLs (syntax valid, flagged for structure or mismatch): cunningsmiles.implant-experts.com, zellersgroup.com, cleanandclearbycliff.com. Live status of every URL: Unknown at this step.

Blank rows: none. Partially populated records: 30 of 36 on Prospects, 9 of 9 on Internal.

## 7. Recommended fields to add later for Google Ads prospect qualification

Identity and segmentation: Record ID; Prospect type (client, internal property, partner-referred); Industry or vertical; Business model (local service, retail, ecommerce, nonprofit, B2B); Nonprofit status (Ad Grants eligibility).

Location: City; State; ZIP; Service area (radius, counties or cities served).

People: Decision-maker name; Title or role; Direct phone; Direct email; Preferred contact channel.

Digital footprint: Website live status and date checked; Currently running Google Ads (Yes / No / Unknown) with evidence source and date; Other paid channels (Meta, Microsoft, Local Services Ads); Tracking present on site (GA4, Tag Manager, Google Ads conversion tag, call tracking); Google Business Profile status; Existing agency or vendor managing their marketing.

Commercial: Lead type (calls, forms, bookings, online sales); Average job or ticket value; Estimated monthly ad budget range; Seasonality.

Pipeline: Relationship owner at Around29; Last contact date; Outreach status; Next action; Fit score or priority tier (computed later); Data provenance per field (source and date) so every value keeps its Known / Unknown / Needs Verification label.
