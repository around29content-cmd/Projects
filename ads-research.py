"""Advertising platform research results (checked 8 Oct 2026) for the MASTER MANAGEMENT VIEW.
Sources: Google Ads Transparency Center (ATC, region US, by domain, 'Any time' and 'Last 30 days' filters), Meta Ad Library
(US, exact-phrase keyword search; a result counts only when the sponsoring page name is the prospect), site HTML tag scan
(saved 8 Oct 2026), and Around29's own Search29 dashboard for accounts it manages.
'No' = no evidence found after this research, NOT confirmed never ran."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"
D = "2026-10-08"
ATC = "https://adstransparency.google.com/?region=US&domain="
META = "https://www.facebook.com/ads/library/?country=US&search_type=keyword_exact_phrase&q="
NOEV = "No = no evidence found after reasonable research, not confirmed never ran."

R = {}
def add(name, run, ever, plat, ev, src, conf):
    R[name] = [name, run, ever, plat, ev, src, D, conf]

add("Prime Care Dental Indy", "Yes", "Yes", "None identified",
    "ATC: 5 ads by verified advertiser 'Primecare Dental LLC' pointing to primecaredentalindy.com; all 5 also shown under the Last 30 days filter. Meta Ad Library exact phrase 'Prime Care Dental' returned only a Las Vegas practice (primecare-dental.com), a different business; no ads by the Indianapolis page. No ad tags beyond GA4 on site.",
    ATC + "primecaredentalindy.com | " + META + "%22Prime%20Care%20Dental%22", "High")
add("Cunning Dental Group", "Yes", "Yes", "Facebook Ads",
    "ATC: 36 ads by verified advertiser 'Cunning Dental Group', 36 under Last 30 days. Search29 (Around29 dashboard): Google Ads connected, spend $8,238.61 / 585 clicks / 26 conversions 1 Sep-7 Oct 2026 across Sedation Dentistry, Brand, PMax and Implant Maintenance campaigns (data to 7 Oct 2026) - Around29 manages this account. Meta Ad Library: 4 active ads by page 'Cunning Dental Group' started 1 Oct 2026 (IV sedation 50% off); placement (Facebook vs Instagram) not shown, so recorded as Facebook Ads only. Search29 also shows a Facebook Ads integration connected. Meta pixel and CallRail present on site.",
    ATC + "cunningdental.com | " + META + "%22Cunning%20Dental%20Group%22 | Search29 client id 1 (ads_summary, client_snapshot)", "High")
add("AA Roofing and Decking", "No", "No", "None identified",
    "ATC: 0 ads for aaroofingdecking.com (Any time). Meta exact phrase 'AA Roofing': results are unrelated pages (Big Daily, The Daily Buzz). Site tags: GA4 only, no Google Ads or Meta tag. " + NOEV,
    ATC + "aaroofingdecking.com | " + META + "%22AA%20Roofing%22", "Medium")
add("VIP Pest Solutions", "No", "No", "None identified",
    "ATC: 0 ads for vippestsolutions.com. Meta exact phrase 'VIP Pest Solutions': no ads match. Site tags: GA4 only. " + NOEV,
    ATC + "vippestsolutions.com | " + META + "%22VIP%20Pest%20Solutions%22", "Medium")
add("Affordable Junk Removal", "Yes", "Yes", "None identified",
    "ATC: 1 ad pointing to affordablejunkremovalca.com by verified advertiser 'Choice Medias LLC' (a third party, not the business; relationship unverified), shown under Last 30 days. Search29 (Around29 client id 3): no Google Ads integration; GA4, GSC, GTM, Business Profile, Yext connected. Meta exact phrase 'Affordable Junk Removal' returns ~220 ads for other companies with the same generic words; no page matching the Sacramento business seen in the top results (inconclusive). Yelp link on site is a listing, not evidence of Yelp advertising.",
    ATC + "affordablejunkremovalca.com | " + META + "%22Affordable%20Junk%20Removal%22 | Search29 client_snapshot id 3", "Medium")
add("Superior Coatings NW", "No", "No", "None identified",
    "ATC: 0 ads for superiorcoatingsnw.com. Meta exact phrase 'Superior Coatings': 2 active ads by a page 'Superior Coatings' referencing the Eccles Theater, Salt Lake City - a different company. Site tags: GA4 only. " + NOEV,
    ATC + "superiorcoatingsnw.com | " + META + "%22Superior%20Coatings%22", "Medium")
add("American Tree Excavation", "No", "No", "None identified",
    "ATC: 0 ads for americantreeexcavation.com. Meta exact phrase 'American Tree': matches are American Tree Service (Modesto CA) and an insurance agency - different businesses. Site tags: GA4 only. " + NOEV,
    ATC + "americantreeexcavation.com | " + META + "%22American%20Tree%22", "Medium")
add("Zellers Group (Zellersins)", "No", "No", "None identified",
    "ATC: 0 ads for zellersgroup.com. Meta exact phrase 'Zellers Group': no ads match. Site tags: GA4 only. " + NOEV,
    ATC + "zellersgroup.com | " + META + "%22Zellers%20Group%22", "Medium")
add("Workhub Tulsa", "Yes", "Yes", "None identified",
    "ATC: 8 ads pointing to workhubtulsa.com by verified advertiser 'Around29 Digital Media Solutions'. Search29 (client 'Workhub', id 97): Google Ads connected ('Work Hub -Tulsa'), monthly budget $700 (Aug-Oct 2026), spend $982 / 98 clicks / 3 conversions 1 Sep-7 Oct 2026, campaign 'Co-working Spaces', data to 6 Oct 2026 - Around29 manages this account. Google Ads conversion tag AW-11546379903 on site. Meta exact phrase 'WorkHub Tulsa': no ads match.",
    ATC + "workhubtulsa.com | Search29 client id 97 (ads_summary, client_snapshot) | " + META + "%22WorkHub%20Tulsa%22", "High")
add("Alignments Northwest LLC", "No", "No", "None identified",
    "ATC: 0 ads for alignmentsnorthwest.com. Meta exact phrase: no ads match. Search29 (client id 98): only Business Profile and Yext (listings management, not advertising). Site tag: legacy Universal Analytics only. " + NOEV,
    ATC + "alignmentsnorthwest.com | " + META + "%22Alignments%20Northwest%22 | Search29 client_snapshot id 98", "Medium")
add("NorthWest Eco Clean", "No", "No", "Facebook Ads",
    "ATC: 0 ads for northwestecoclean.com. Meta Ad Library: active ads by page 'Northwest Eco Clean' started 11 May 2026 and 5 Aug 2026 (King County bin-cleaning video ads, 'Get quote' button); placement not shown, recorded as Facebook Ads. Meta pixel present on site. Google: " + NOEV,
    ATC + "northwestecoclean.com | " + META + "%22Northwest%20Eco%20Clean%22", "High")
add("Clean & Clear by Cliff", "No", "No", "None identified",
    "ATC: 0 ads for cleanandclearbycliff.com. Meta exact phrase 'Clear by Cliff': no ads match. Site tags: GA4 only. " + NOEV,
    ATC + "cleanandclearbycliff.com | " + META + "%22Clear%20by%20Cliff%22", "Medium")
add("Orion Optical", "Yes", "Yes", "None identified",
    "ATC: 9 ads by verified advertiser 'Orion Optical, LLC.' pointing to orionoptical.com; 9 under Last 30 days. Meta exact phrase 'Orion Optical': no ads match. Site tags: GA4 only. Email on file belongs to Premo Media Group, a marketing agency that is also a Search29 partner; whether it runs these ads is unverified (no Orion client accessible in Search29).",
    ATC + "orionoptical.com | " + META + "%22Orion%20Optical%22", "High")
add("Trans Landscaping", "No", "Unknown", "None identified",
    "ATC: 0 ads for trans-landscaping.com (Any time). Site carries a Google Ads conversion tag (AW-11140737511) plus GTM, which indicates a Google Ads account was set up at some point, but no ads appear in ATC - historical status Unknown. Meta exact phrases 'Tran's Landscaping' and 'Trans Landscaping': no ads match.",
    ATC + "trans-landscaping.com | site HTML tag scan 8 Oct 2026 | " + META + "%22Trans%20Landscaping%22", "Medium")
add("Axle Surgeons of Seattle", "No", "No", "None identified",
    "ATC: 0 ads for axlesurgeonseattle.com. Meta exact phrase 'Axle Surgeons': no ads match. Search29 (client id 94): Business Profile and Yext only. Site tags: GA4 only. " + NOEV,
    ATC + "axlesurgeonseattle.com | " + META + "%22Axle%20Surgeons%22 | Search29 client_snapshot id 94", "Medium")
add("Ocean View Lodging", "Yes", "Yes", "None identified",
    "ATC: 4 ads pointing to oceanviewlodging.com by verified advertiser 'Suhail Ahmad' (an individual; relationship to the lodge unverified), 4 under Last 30 days; 'Today' filter returned 0 (used to validate the filter). Meta exact phrase 'Ocean View Lodge': no ads match. Site tags: GA4 and GTM.",
    ATC + "oceanviewlodging.com | " + META + "%22Ocean%20View%20Lodge%22", "Medium")
add("Calvary Cemetery", "Yes", "Yes", "Facebook Ads",
    "ATC: 14 ads pointing to calvarycemetery.org by verified advertiser 'CoxNet', 14 under Last 30 days (CoxNet appears to be a media company advertising on the cemetery's behalf - inferred). Meta Ad Library: one inactive video ad by page 'Calvary Cemetery' ran 17 Jun-28 Sep 2026 linking to calvarycemetery.org ('A haven in the heart of Tulsa'). Site tags: GTM and legacy UA.",
    ATC + "calvarycemetery.org | https://www.facebook.com/ads/library/?country=US&q=%22Calvary%20Cemetery%22%20Tulsa", "Medium")
add("La Jolla Grooming Co", "No", "No", "None identified",
    "ATC: 0 ads for ljgrooming.com. Meta exact phrase 'La Jolla Grooming': no ads match. Yelp link on site is a listing only. Site tags: GA4. " + NOEV,
    ATC + "ljgrooming.com | " + META + "%22La%20Jolla%20Grooming%22", "Medium")
add("Wheeler-Sonoma Printers", "No", "No", "None identified",
    "ATC: 0 ads for wheeler-sonoma.com. Meta exact phrase 'Wheeler-Sonoma': no ads match. Site tags: GA4. " + NOEV,
    ATC + "wheeler-sonoma.com | " + META + "%22Wheeler-Sonoma%22", "Medium")
add("Top Dollar Pawn and Check Cashing", "No", "Unknown", "None identified",
    "ATC: 0 ads for topdollartulsa.com. Site carries a Google Ads conversion tag (AW-16769436125), indicating an account was set up, but no ads appear in ATC - historical status Unknown. Meta exact phrase 'Top Dollar Pawn': the only match is 'Top Dollar Pawn TCI' (Turks and Caicos), a different business.",
    ATC + "topdollartulsa.com | site HTML tag scan 8 Oct 2026 | " + META + "%22Top%20Dollar%20Pawn%22", "Medium")
add("ASL Camguard", "No", "No", "None identified", "ATC: 0 ads for aslcamguard.com (ATC also covers Shopping). Meta exact phrase: no ads match. Site tags: GA4 and legacy UA. " + NOEV, ATC + "aslcamguard.com | " + META + "%22ASL%20Camguard%22", "Medium")
add("Pinpoint Resource", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. Site tags: GA4. " + NOEV, ATC + "pinpointresource.com | " + META + "%22Pinpoint%20Resource%22", "Medium")
add("Occasions Paper", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. Yelp link on site is a listing only. " + NOEV, ATC + "occasionspaper.com | " + META + "%22Occasions%20Paper%22", "Medium")
add("Will Rogers Stage Foundation", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase 'Will Rogers Stage': no ads match. " + NOEV, ATC + "willrogersstage.com | " + META + "%22Will%20Rogers%20Stage%22", "Medium")
add("Cunningsmiles Implant Experts", "No", "Unknown", "None identified", "ATC: 0 ads for cunningsmiles.implant-experts.com. Site not live (403/404). Meta exact phrase 'Cunning Smiles': results are unrelated pages. Business identity unverified, so history Unknown.", ATC + "cunningsmiles.implant-experts.com | " + META + "%22Cunning%20Smiles%22", "Low")
add("Around Cricket", "No", "No", "Facebook Ads",
    "ATC: 0 ads for aroundcricket.com. Search29 (Around29 client id 122): Facebook Ads integration connected under the 'Around 29 Digital Media Solutions' ad account with Facebook data through 13 Aug 2026, i.e. Meta ads were run for this client via Around29 (dates of activity not retrieved). Meta Ad Library exact phrase 'Around Cricket' did not surface the page in top results. Instagram account connected as a page, not evidence of Instagram Ads.",
    "Search29 client_snapshot id 122 | " + ATC + "aroundcricket.com | " + META + "%22Around%20Cricket%22", "Medium")
add("Ornamental Grasses", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase returns ~3,000 ads using the generic phrase by other advertisers; none by this nursery seen. " + NOEV, ATC + "ornamental-grasses.com | " + META + "%22Ornamental%20Grasses%22", "Medium")
add("Next Level Prospect", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. " + NOEV, ATC + "nextlevelprospect.com | " + META + "%22Next%20Level%20Prospect%22", "Medium")
add("The Bartan Company", "Unknown", "Unknown", "None identified", "ATC (region US): 0 ads; the business is based in India and ATC was queried for the US region only, so this is not conclusive. Meta exact phrase 'Bartan Company' (US): no ads match. Site tag: legacy UA.", ATC + "thebartancompany.com | " + META + "%22Bartan%20Company%22", "Low")
add("DBSA OK", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase 'DBSA Oklahoma': no ads match. " + NOEV, ATC + "dbsaok.org | " + META + "%22DBSA%20Oklahoma%22", "Medium")
add("Chili On The Green", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. " + NOEV, ATC + "chilionthegreen.com | " + META + "%22Chili%20on%20the%20Green%22", "Medium")
add("Lab Rescue", "No", "No", "None identified", "ATC: 0 ads. Meta keyword 'Lab Rescue' Oklahoma: results are unrelated advertisers. " + NOEV, ATC + "labrescue.net | https://www.facebook.com/ads/library/?country=US&q=%22Lab%20Rescue%22%20Oklahoma", "Medium")
add("Tag OK", "No", "No", "None identified", "ATC: 0 ads. Meta keyword 'Tag OK' Oklahoma: results are tag agencies and other unrelated advertisers. " + NOEV, ATC + "tagok.org | https://www.facebook.com/ads/library/?country=US&q=%22Tag%20OK%22%20Oklahoma", "Medium")
add("Kiwanis Club of Tulsa", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. " + NOEV, ATC + "kiwaniscluboftulsa.org | " + META + "%22Kiwanis%20Club%20of%20Tulsa%22", "Medium")
add("Brothers Micro Market", "No", "Unknown", "None identified", "ATC: 0 ads. Site down; business unidentified. Meta exact phrase: no ads match.", ATC + "brothersmicromarket.com | " + META + "%22Brothers%20Micro%20Market%22", "Low")
add("Rosewood Parke", "No", "No", "None identified", "ATC: 0 ads. Meta exact phrase: no ads match. Homeowners association. " + NOEV, ATC + "rosewoodparke.com | " + META + "%22Rosewood%20Parke%22", "Medium")
for n in ["Around29 Center for Enriched Studies", "Lead You", "Starling Wonder Kids", "Around29 Digital Media Solutions", "Send29", "Around29.us", "Around29 themes", "Starling Education", "Search29"]:
    add(n, "Unknown", "Unknown", "Not researched (internal)", "Internal Around29 property; excluded from the advertising research by scope.", "n/a", "n/a")

order = [r[0] for r in json.load(open(os.path.join(HERE, "master_rows.json"), encoding="utf-8"))]
fix = {"Zellersins": "Zellers Group (Zellersins)", "Clean and Clean by Cliff": "Clean & Clear by Cliff", "Wheeler Sonoma Printing": "Wheeler-Sonoma Printers", "Orion Opticals": "Orion Optical"}
order = [fix.get(n, n) for n in order]
missing = [n for n in order if n not in R]; assert not missing, missing
rows = [R[n] for n in order]
json.dump([[r[1], r[2], r[3]] for r in rows], open(os.path.join(HERE, "master_ads_cols.json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump(rows, open(os.path.join(HERE, "ads_research_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
with open(os.path.join(PROJ, "ads_research.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["Business", "Running Ads", "Ads Ever Run", "Platforms", "Evidence", "Source", "Research Date", "Confidence"]); w.writerows(rows)
from collections import Counter
print(Counter(r[1] for r in rows), Counter(r[2] for r in rows), Counter(r[3] for r in rows))
