"""Step 5: Google Ads Opportunity Score (0-100) for the 45 records.
Methodology first (rubric), then per-factor ratings with evidence, then totals by formula in the sheet."""
import json, csv, os
from collections import Counter

SP = r"C:\Users\Aroun\AppData\Local\Temp\claude\C--Users-Aroun-Desktop-Projects-Google-Ads-Prospects\e134b08f-71c9-4529-bc4f-df5bd3dad2a6\scratchpad\scripts"
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"

WEIGHTS = [("Industry Google Ads Fit",15),("Search Intent",15),("Commercial Intent",15),("Customer Value Potential",15),
           ("Conversion Potential",10),("Geographic Targeting",10),("Urgency",5),("Business Scalability",5),
           ("Digital Readiness",5),("Data Completeness",5)]
assert sum(w for _, w in WEIGHTS) == 100

# ---- rubric: factor -> {rating label: (points, description)} ----
RUBRIC = {
 "Industry Google Ads Fit": {
  "Home Services":(15,"Local service categories with urgent, high-ticket, call-driven demand"),
  "Dental":(15,"Appointment-driven, very high case value, constant local search demand"),
  "Medical":(14,"Appointment-driven local healthcare with repeat visits"),
  "Insurance":(13,"Quote-driven with very high lifetime value; costly keywords"),
  "Automotive (services)":(12,"Repair and maintenance searches with clear intent"),
  "Hospitality":(12,"Booking-driven destination demand; OTA competition"),
  "Real Estate (coworking)":(11,"Membership and lease value with steady local search"),
  "Other: pet services":(11,"Booking-driven local service with repeat visits"),
  "Education":(10,"Enrolment-driven with high tuition value; seasonal"),
  "Automotive (products)":(9,"Product brand sold online; marketplace competition"),
  "B2B Services":(9,"Quote-driven business demand; online competitors on generic terms"),
  "Financial Services (pawn)":(8,"Strong local intent but policy limits on loans and firearms"),
  "Professional Services":(8,"Research-heavy agency buying; crowded, expensive terms"),
  "Retail":(8,"Store-visit or product demand; browse-heavy, margins modest"),
  "Retail (ecommerce)":(8,"Product searches convert online; marketplace competition"),
  "Technology (software)":(8,"Scalable but very expensive software keywords"),
  "Other: cemetery":(8,"High-value, sensitive, mixed urgency"),
  "Other: event services":(6,"Niche quote-driven demand"),
  "Other: performing arts":(5,"Seasonal ticket sales, small budgets"),
  "Technology (digital products)":(5,"Low-priced products against marketplaces"),
  "Healthcare (nonprofit support)":(4,"Help-seeking searches without a commercial transaction"),
  "Other: community event":(3,"Annual event, low value"),
  "Other: animal welfare nonprofit":(2,"Donation and adoption driven, no sale"),
  "Other: service club":(1,"Membership organisation, no sale"),
  "Other: community association":(0,"Not a business"),
  "Unknown":(3,"Industry not established; conservative"),
 },
 "Customer Value Potential": {"Very High":(15,"Multi-thousand-dollar jobs or multi-year lifetime value"),"High":(12,"High-ticket or repeat B2B value"),
  "Moderate":(8,"Mid-ticket or recurring small jobs"),"Low":(4,"Small, occasional purchases"),"Very Low":(1,"Donations or dues only"),"Unknown":(3,"No evidence; conservative")},
 "Conversion Potential": {"Direct response (calls plus quotes or appointments)":(10,"Trackable calls, quote forms or appointment requests"),
  "Direct response (bookings or purchases online)":(9,"Online bookings, sign-ups or product purchases"),
  "Forms and consultations":(7,"Lead forms and consultation requests; longer sales cycle"),
  "Store visits and calls":(6,"Offline conversions; harder to measure"),
  "Ticket purchases online (seasonal)":(5,"Real purchases but seasonal and low value"),
  "Donations, sign-ups or tickets only":(3,"No commercial transaction"),
  "None":(0,"Nothing to convert"),"Unknown":(2,"No evidence; conservative")},
 "Geographic Targeting": {"Local, location verified":(10,"Single metro, location confirmed on the site"),
  "Hyperlocal, location verified":(9,"Neighbourhood radius, location confirmed"),
  "Regional, service area verified":(9,"Several cities or counties confirmed on the site"),
  "Local, location inferred from area code":(6,"Target area must be confirmed before launch"),
  "National":(6,"Feasible but broader and costlier"),
  "National (online)":(5,"Online product with no local anchor"),
  "International / outside US":(2,"Outside the market this list serves"),
  "Unknown":(2,"No location evidence; conservative")},
 "Urgency": {"Emergency":(5,"Immediate need"),"High":(4,"Days"),"Moderate":(3,"Weeks"),"Low":(1,"No time pressure"),"Unknown":(1,"No evidence; conservative")},
 "Business Scalability": {"Regional service with recurring or multi-location capacity":(5,"Can absorb more leads and spend"),
  "Established practice or firm with capacity to add clients":(4,"Room to grow within current operation"),
  "Small local operator, single team":(3,"Growth limited by one crew or owner"),
  "Capacity-limited single location":(2,"Fixed chairs, rooms or stock"),
  "Nonprofit, event or association":(1,"Not built to scale paid acquisition"),
  "Unknown":(1,"No evidence; conservative")},
 "Digital Readiness": {"Live site with online booking, store or scheduling":(5,"Conversion path already online"),
  "Live site with phone and contact path, service area stated":(4,"Ready for call and form tracking; targeting information present"),
  "Live site with phone and contact path":(3,"Ready for call and form tracking"),
  "Live site, limited contact path":(2,"Landing experience needs work"),
  "Site in progress or inaccessible":(1,"No usable landing page today"),
  "No website":(0,"Nothing to send traffic to")},
 "Data Completeness": {str(n):(n, d) for n, d in [(0,"No usable contact data"),(1,"One element present"),(2,"Two elements present"),(3,"Three elements present"),(4,"Four elements present"),(5,"Valid phone, email, verified location and clean identity")]},
}
for n in range(11):
    RUBRIC.setdefault("Search Intent", {})[str(n)] = (round(n*1.5, 1), f"Step 4 search intent {n}/10 x 1.5")
    RUBRIC.setdefault("Commercial Intent", {})[str(n)] = (round(n*1.5, 1), f"Step 4 commercial intent {n}/10 x 1.5")
RUBRIC["Search Intent"]["Unknown"] = (3, "No evidence; conservative")
RUBRIC["Commercial Intent"]["Unknown"] = (3, "No evidence; conservative")

# ---- per-record inputs ----
# rid: (name, industry_label, search, commercial, value, urgency, geo_label, conv_label, scal_label, digital_label,
#       phone_valid, email_present, loc_verified, identity_clean, class_conf, strengths, weaknesses)
U = "Unknown"
REC = [
 ("P-01","AA Roofing and Decking","Home Services",9,8,"Very High","High","Local, location verified","Direct response (calls plus quotes or appointments)","Small local operator, single team","Live site with phone and contact path, service area stated",1,0,1,1,"High","Top-tier home-services vertical; very high job value; urgent demand","Highly competitive category; no email on file; single-crew capacity"),
 ("P-02","Affordable Junk Removal","Home Services",9,9,"Moderate","High","Regional, service area verified","Direct response (calls plus quotes or appointments)","Regional service with recurring or multi-location capacity","Live site with phone and contact path, service area stated",1,1,1,1,"High","Very high intent and same-day urgency; regional footprint; business accounts","Mid-ticket jobs; free-mail contact; heavy franchise competition"),
 ("P-03","Alignments Northwest LLC","Automotive (services)",6,7,"High","Moderate","Local, location verified","Direct response (calls plus quotes or appointments)","Small local operator, single team","Live site with phone and contact path, service area stated",1,1,1,1,"High","Niche B2B service with little competition; fleet repeat work","Low search volume; small team"),
 ("P-04","American Tree Excavation","Home Services",8,8,"High","High","Local, location inferred from area code","Direct response (calls plus quotes or appointments)","Small local operator, single team","Live site with phone and contact path",1,0,0,1,"Medium","High-ticket, urgent tree work in a strong vertical","Service area not stated on the site; no email; competitive"),
 ("P-05","Around Cricket","Retail (ecommerce)",7,6,"Moderate","Low","International / outside US","Direct response (bookings or purchases online)","Small local operator, single team","Live site with online booking, store or scheduling",0,1,1,1,"High","Working online store; verified product demand","Outside the US market; invalid phone on file; retail margins"),
 ("P-06","ASL Camguard","Automotive (products)",6,6,"Moderate","Low","National","Direct response (bookings or purchases online)","Established practice or firm with capacity to add clients","Live site with online booking, store or scheduling",1,0,1,1,"Medium","National product brand with an online store; repeat consumable","Marketplace competition; modest unit value; product feed needed"),
 ("P-07","Axle Surgeons of Seattle","Automotive (services)",7,9,"High","Emergency","Regional, service area verified","Direct response (calls plus quotes or appointments)","Small local operator, single team","Live site with phone and contact path, service area stated",1,1,1,1,"High","Emergency B2B demand; call-driven; low competition","Low volume; free-mail contact"),
 ("P-08","Brothers Micro Market",U,U,U,U,U,U,U,U,"Site in progress or inaccessible",1,1,0,0,"Low","Valid phone and a named contact email","Website offline; business type unknown"),
 ("P-09","Calvary Cemetery","Other: cemetery",6,6,"High","Moderate","Local, location verified","Forms and consultations","Established practice or firm with capacity to add clients","Live site with phone and contact path, service area stated",1,1,1,1,"High","High-value services; established Tulsa institution; complete contact data","Sensitive category; mixed urgency; possibly a nonprofit"),
 ("P-10","Chili On The Green","Other: community event",3,4,"Low","Low","Regional, service area verified","Donations, sign-ups or tickets only","Nonprofit, event or association","Live site with phone and contact path",0,0,1,1,"High","Verified Oklahoma-wide event brand","Seasonal, low value; no phone or email; run by Kiwanis"),
 ("P-11","Clean and Clean by Cliff","Home Services",7,7,"Moderate","Moderate","Local, location inferred from area code","Direct response (calls plus quotes or appointments)","Small local operator, single team","Live site with phone and contact path",1,0,0,0,"Medium","Clear local service intent; recurring work","Low ticket; location not stated; name differs from the site"),
 ("P-12","Cunning Dental Group","Dental",9,8,"Very High","High","Regional, service area verified","Direct response (calls plus quotes or appointments)","Regional service with recurring or multi-location capacity","Live site with online booking, store or scheduling",1,0,1,0,"High","Very high case value; emergency and implant demand; 56-year practice; online scheduling","No email on file; very competitive; duplicate pair to resolve"),
 ("P-13","Cunningsmiles Implant Experts","Dental",8,8,"Very High","Moderate",U,"Forms and consultations",U,"Site in progress or inaccessible",0,0,0,0,"Low","Implant dentistry is a high-value vertical","Site blocked; no contact data; likely duplicate of P-12"),
 ("P-14","DBSA OK","Healthcare (nonprofit support)",6,2,"Very Low","High","Regional, service area verified","Donations, sign-ups or tickets only","Nonprofit, event or association","Live site with phone and contact path, service area stated",1,1,1,1,"High","Complete contact data; statewide reach","No commercial conversion; nonprofit"),
 ("P-15","Kiwanis Club of Tulsa","Other: service club",3,2,"Very Low","Low","Local, location verified","Donations, sign-ups or tickets only","Nonprofit, event or association","Live site with phone and contact path",1,0,1,1,"High","Verified Tulsa presence; valid phone","No commercial conversion; membership organisation"),
 ("P-16","La Jolla Grooming Co","Other: pet services",8,8,"Moderate","Moderate","Hyperlocal, location verified","Direct response (bookings or purchases online)","Capacity-limited single location","Live site with online booking, store or scheduling",1,0,1,1,"High","Direct booking intent; affluent area; online booking","Capacity-limited; moderate ticket; no email on file"),
 ("P-17","Lab Rescue","Other: animal welfare nonprofit",5,3,"Very Low","Low","Regional, service area verified","Donations, sign-ups or tickets only","Nonprofit, event or association","Live site with phone and contact path",0,0,1,1,"High","Clear mission and regional reach","No commercial conversion; no phone or email"),
 ("P-18","Next Level Prospect","Education",5,4,"Low","Low","National","Forms and consultations","Nonprofit, event or association","Live site, limited contact path",1,0,0,1,"Medium","Valid phone; nationwide scope","Nonprofit with unclear revenue; research-stage demand; site in progress"),
 ("P-19","NorthWest Eco Clean","Home Services",6,7,"Moderate","Low","Regional, service area verified","Direct response (bookings or purchases online)","Regional service with recurring or multi-location capacity","Live site with online booking, store or scheduling",1,0,1,1,"High","Recurring plans; regional King County footprint; existing social advertising","Small ticket; young category"),
 ("P-20","Occasions Paper","Retail",5,5,"Moderate","Low","Local, location verified","Store visits and calls","Capacity-limited single location","Live site with phone and contact path, service area stated",1,0,1,1,"High","Verified Norman location; dealer brand","No online sales; low urgency; browse-heavy demand"),
 ("P-21","Ocean View Lodging","Hospitality",9,8,"High","Moderate","National","Direct response (bookings or purchases online)","Capacity-limited single location","Live site with online booking, store or scheduling",1,0,1,1,"High","Constant destination demand; online booking","OTA competition; fixed room capacity"),
 ("P-22","Orion Opticals","Medical",8,7,"High","Moderate","Local, location verified","Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with online booking, store or scheduling",1,1,1,1,"High","High lifetime value; online booking; complete location data","Chain competition; contact email belongs to a third party"),
 ("P-23","Ornamental Grasses","Retail",5,4,"Low","Low","Local, location verified","Store visits and calls","Capacity-limited single location","Live site with phone and contact path",1,0,1,1,"Medium","Verified Olympia location","Unclear retail model; small, seasonal demand"),
 ("P-24","Pinpoint Resource","Retail",5,6,"Moderate","Moderate","Local, location verified","Store visits and calls","Capacity-limited single location","Live site with phone and contact path, service area stated",1,0,1,1,"High","Verified store; wedding deadlines create intent","National brands own generic terms; no online sales"),
 ("P-25","Prime Care Dental Indy","Dental",9,8,"Very High","High","Local, location verified","Direct response (calls plus quotes or appointments)","Regional service with recurring or multi-location capacity","Live site with phone and contact path, service area stated",1,0,1,1,"High","Two locations; very high case value; emergency demand","No email on file; very competitive"),
 ("P-26","Rosewood Parke","Other: community association",1,0,"Very Low","Low","Hyperlocal, location verified","None","Nonprofit, event or association","Live site, limited contact path",0,0,1,1,"High","None","Not a business"),
 ("P-27","Superior Coatings NW","Home Services",8,8,"High","Moderate","Regional, service area verified","Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with phone and contact path, service area stated",1,0,1,1,"High","High-ticket painting; regional service area; commercial work","Seasonal; competitive; no email on file"),
 ("P-28","Tag OK","Other: animal welfare nonprofit",3,2,"Very Low","Low","Regional, service area verified","Donations, sign-ups or tickets only","Nonprofit, event or association","Live site with phone and contact path",0,0,1,1,"High","Regional program","No commercial conversion; no phone or email"),
 ("P-29","The Bartan Company","Other: event services",5,5,"Moderate","Low","International / outside US","Forms and consultations","Small local operator, single team","Live site with phone and contact path",1,0,1,1,"High","Verified Hyderabad presence; quote-driven","Outside the US market; niche demand"),
 ("P-30","Top Dollar Pawn and Check Cashing","Financial Services (pawn)",7,7,"Moderate","High","Local, location verified","Store visits and calls","Small local operator, single team","Live site with phone and contact path",1,0,1,1,"High","Strong local intent; immediate cash needs","Policy limits on firearms and loans; modest margins"),
 ("P-31","Trans Landscaping","Home Services",8,7,"High","Moderate","Regional, service area verified","Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with phone and contact path, service area stated",1,0,1,1,"High","High-ticket installs; service towns listed; 20+ years in business","Seasonal; competitive; no email on file"),
 ("P-32","VIP Pest Solutions","Home Services",9,9,"High","High","Regional, service area verified","Direct response (calls plus quotes or appointments)","Regional service with recurring or multi-location capacity","Live site with phone and contact path, service area stated",0,0,1,1,"High","Top vertical; recurring contracts; three-county region","Phone on file mistyped; no email; very competitive"),
 ("P-33","Wheeler Sonoma Printing","B2B Services",6,6,"High","Moderate","Regional, service area verified","Forms and consultations","Established practice or firm with capacity to add clients","Live site with phone and contact path, service area stated",1,0,1,1,"High","Repeat B2B orders; established client industries","Online printers dominate generic terms"),
 ("P-34","Will Rogers Stage Foundation","Other: performing arts",5,6,"Moderate","Moderate","Local, location verified","Ticket purchases online (seasonal)","Nonprofit, event or association","Live site with online booking, store or scheduling",1,0,1,1,"High","Online ticketing; verified Tulsa venue","Seasonal, small budgets; nonprofit"),
 ("P-35","Workhub Tulsa","Real Estate (coworking)",7,7,"High","Moderate","Local, location verified","Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with phone and contact path, service area stated",1,0,1,1,"High","Membership value; clear local intent","Limited market size"),
 ("P-36","Zellersins","Insurance",7,7,"Very High","Moderate","Local, location inferred from area code","Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with phone and contact path",1,0,0,0,"Medium","Very high lifetime value; clear quote intent","Expensive keywords; location and lines of business unverified; name differs from the site"),
 ("I-01","Around29 Center for Enriched Studies","Education",7,7,"Very High","Moderate",U,"Direct response (calls plus quotes or appointments)","Established practice or firm with capacity to add clients","Live site with online booking, store or scheduling",0,0,0,1,"Medium","High tuition value; visit bookings","Location unknown; phone unusable; internal property"),
 ("I-02","Around29 Digital Media Solutions","Professional Services",7,6,"High","Low","Local, location inferred from area code","Forms and consultations","Established practice or firm with capacity to add clients","Site in progress or inaccessible",1,0,0,1,"Medium","High project value","Crowded agency keywords; site in progress; it is the Partner itself"),
 ("I-03","Search29",U,U,U,U,U,U,U,U,"No website",0,0,0,1,"Low","None","No website, phone or email"),
 ("I-04","Send29","Technology (software)",7,6,"Moderate","Low","National (online)","Direct response (bookings or purchases online)","Regional service with recurring or multi-location capacity","Site in progress or inaccessible",0,0,0,1,"Medium","Scalable self-serve product","Low revenue per customer against expensive keywords; site in progress"),
 ("I-05","Lead You","Technology (software)",7,6,"High","Low","National (online)","Forms and consultations","Regional service with recurring or multi-location capacity","Live site, limited contact path",0,0,0,1,"Medium","Scalable B2B software","Crowded expensive category; no contact data"),
 ("I-06","Around29 themes","Technology (digital products)",5,5,"Low","Low","International / outside US",U,"Small local operator, single team","Live site, limited contact path",0,0,0,0,"Low","Scalable digital product","Minimal site content; low price point; marketplace competition"),
 ("I-07","Around29.us","Professional Services",7,6,"High","Low",U,"Forms and consultations","Established practice or firm with capacity to add clients","Live site with phone and contact path",0,0,0,1,"Medium","Clear service description","Duplicate agency site; no contact data; crowded keywords"),
 ("I-08","Starling Education","Education",U,U,U,U,U,U,U,"Site in progress or inaccessible",1,0,0,0,"Low","Valid phone","Site unreachable; possible duplicate of I-09"),
 ("I-09","Starling Wonder Kids","Education",7,7,"Very High","Moderate",U,U,"Small local operator, single team","Live site, limited contact path",0,0,0,0,"Medium","High tuition value category","Location unknown; phone unusable; possible duplicate of I-08"),
]
assert len(REC) == 45

def conf_from_class(c, unknown=False):
    if unknown: return "Low"
    return {"High":"High","Medium":"Medium","Low":"Low"}[c]

detail = []   # record_id, business, factor, weight, rating, points(formula), explanation, evidence, confidence
for r in REC:
    rid, name, ind, s, c, val, urg, geo, conv, scal, dig, ph, em, loc, idn, cc, strengths, weak = r
    wmap = dict(WEIGHTS)
    def add(factor, rating, expl, evid, conf):
        key = f"{factor}|{rating}"
        assert rating in RUBRIC[factor], key
        detail.append([rid, name, factor, wmap[factor], rating, key, expl, evid, conf])
    # 1 industry
    add("Industry Google Ads Fit", ind, RUBRIC["Industry Google Ads Fit"][ind][1],
        "CLASSIFICATION primary_industry" + ("; website verified" if cc != "Low" and ind != U else "; name-inferred or unknown"),
        "High" if (cc == "High") else ("Medium" if cc == "Medium" else "Low"))
    # 2 search, 3 commercial
    add("Search Intent", str(s), f"Step 4 search intent {s}/10 scaled to 15" if s != U else "No evidence; conservative placeholder",
        "GOOGLE_ADS_FIT search_intent_0_10 and reason", conf_from_class(cc, s == U))
    add("Commercial Intent", str(c), f"Step 4 commercial intent {c}/10 scaled to 15" if c != U else "No evidence; conservative placeholder",
        "GOOGLE_ADS_FIT commercial_intent_0_10 and reason", conf_from_class(cc, c == U))
    # 4 value
    add("Customer Value Potential", val, RUBRIC["Customer Value Potential"][val][1], "GOOGLE_ADS_FIT customer_value_potential and reason", conf_from_class(cc, val == U))
    # 5 conversion
    conv_conf = "High" if conv in ("Direct response (bookings or purchases online)", "Ticket purchases online (seasonal)") else ("Low" if conv == U else "Medium")
    add("Conversion Potential", conv, RUBRIC["Conversion Potential"][conv][1], "GOOGLE_ADS_FIT conversion_actions; site conversion path from CLASSIFICATION", conv_conf)
    # 6 geo
    geo_conf = "High" if "verified" in geo else ("Low" if geo in (U,) else "Medium")
    add("Geographic Targeting", geo, RUBRIC["Geographic Targeting"][geo][1], "CLASSIFICATION geographic_scope and geographic_basis", geo_conf)
    # 7 urgency
    add("Urgency", urg, RUBRIC["Urgency"][urg][1], "GOOGLE_ADS_FIT urgency and reason", "Low" if urg == U else "Medium")
    # 8 scalability
    add("Business Scalability", scal, RUBRIC["Business Scalability"][scal][1], "CLASSIFICATION business_model and geographic_scope (judgement)", "Low" if scal == U else "Medium")
    # 9 digital
    add("Digital Readiness", dig, RUBRIC["Digital Readiness"][dig][1], "Website fetch 8 Oct 2026; CLEANED_DATA website_project_status", "High")
    # 10 data completeness
    comp = (2 if ph else 0) + (1 if em else 0) + (1 if loc else 0) + (1 if idn else 0)
    parts = [("valid phone (2)" if ph else "no valid phone (0)"), ("email on file (1)" if em else "no email (0)"), ("location verified (1)" if loc else "location unverified (0)"), ("identity clean (1)" if idn else "identity issue: duplicate or name mismatch (0)")]
    add("Data Completeness", str(comp), "; ".join(parts), "CLEANED_DATA phone_status, email_status; CLASSIFICATION geographic_basis; duplicate_class", "High")

# python-side totals for the report
pts = {}
for d in detail:
    f, rating = d[2], d[4]
    pts[d[0]] = pts.get(d[0], 0) + RUBRIC[f][rating][0]
def tier(t): return "Tier 1 - Immediate Opportunity" if t >= 85 else "Tier 2 - Strong Prospect" if t >= 70 else "Tier 3 - Research/Nurture" if t >= 50 else "Tier 4 - Low Priority"

# ---- SCORING_METHOD payload ----
method = [["Factor", "Weight", "Source of the rating", "How points are awarded"]]
SRC = {"Industry Google Ads Fit":"CLASSIFICATION primary_industry mapped to an industry label",
       "Search Intent":"GOOGLE_ADS_FIT search_intent_0_10","Commercial Intent":"GOOGLE_ADS_FIT commercial_intent_0_10",
       "Customer Value Potential":"GOOGLE_ADS_FIT customer_value_potential","Conversion Potential":"GOOGLE_ADS_FIT conversion_actions and verified site conversion path",
       "Geographic Targeting":"CLASSIFICATION geographic_scope and geographic_basis","Urgency":"GOOGLE_ADS_FIT urgency",
       "Business Scalability":"Judgement from business model, scope and locations on the site","Digital Readiness":"Website status and conversion path observed 8 Oct 2026",
       "Data Completeness":"CLEANED_DATA contactability: phone (2), email (1), verified location (1), clean identity (1)"}
for f, w in WEIGHTS:
    method.append([f, w, SRC[f], "Rating label looked up in the rubric below; Unknown ratings score conservatively and are flagged Low confidence"])
method.append(["TOTAL", 100, "", "Sum of the ten factor points; tiers: 85-100 Tier 1 Immediate Opportunity, 70-84 Tier 2 Strong Prospect, 50-69 Tier 3 Research/Nurture, 0-49 Tier 4 Low Priority"])
method.append([None, None, None, None])
method.append(["rubric_key (factor|rating)", "points", "rating", "description"])
rubric_rows = []
for f, _ in WEIGHTS:
    items = RUBRIC[f].items()
    if f in ("Search Intent", "Commercial Intent"):
        items = sorted(items, key=lambda kv: (kv[0] == "Unknown", int(kv[0]) if kv[0] != "Unknown" else 0))
    else:
        items = sorted(items, key=lambda kv: -kv[1][0])
    for rating, (p, desc) in items:
        rubric_rows.append([f"{f}|{rating}", p, rating, desc])
method += rubric_rows
RUBRIC_START = len(method) - len(rubric_rows) + 1  # first rubric row (1-based) in the sheet
RUBRIC_END = len(method)

# ---- detail payload with VLOOKUP points ----
DETAIL_HEADER = ["record_id","business_name_std","factor","weight","rating","rubric_key","points","factor_explanation","evidence","confidence"]
detail_payload = [DETAIL_HEADER]
for i, d in enumerate(detail):
    rn = i + 2
    rid, name, f, w, rating, key, expl, evid, conf = d
    detail_payload.append([rid, name, f, w, rating, key, f'=IFERROR(VLOOKUP($F{rn},SCORING_METHOD!$A${RUBRIC_START}:$B${RUBRIC_END},2,FALSE),"CHECK")', expl, evid, conf])
DLAST = len(detail_payload)

# ---- summary payload ----
SUM_HEADER = ["record_id","business_name_std","primary_industry"] + [f for f, _ in WEIGHTS] + ["total_score","tier","rank","low_confidence_factors","overall_confidence","key_strengths","key_weaknesses"]
summary = [SUM_HEADER]
for i, r in enumerate(REC):
    rn = i + 2
    rid, name = r[0], r[1]
    row = [rid, name, f'=IFERROR(VLOOKUP($A{rn},CLASSIFICATION!$A$2:$C$46,3,FALSE),"Unknown")']
    for j, (f, _) in enumerate(WEIGHTS):
        col = chr(ord("D") + j)
        row.append(f"=SUMIFS(SCORE_FACTOR_DETAIL!$G$2:$G${DLAST},SCORE_FACTOR_DETAIL!$A$2:$A${DLAST},$A{rn},SCORE_FACTOR_DETAIL!$C$2:$C${DLAST},{col}$1)")
    row.append(f"=SUM(D{rn}:M{rn})")
    row.append(f'=IF(N{rn}>=85,"Tier 1 - Immediate Opportunity",IF(N{rn}>=70,"Tier 2 - Strong Prospect",IF(N{rn}>=50,"Tier 3 - Research/Nurture","Tier 4 - Low Priority")))')
    row.append(f"=RANK(N{rn},$N$2:$N$46)")
    row.append(f'=COUNTIFS(SCORE_FACTOR_DETAIL!$A$2:$A${DLAST},$A{rn},SCORE_FACTOR_DETAIL!$J$2:$J${DLAST},"Low")')
    row.append(f'=IF(Q{rn}>=4,"Low",IF(Q{rn}>=2,"Medium","High"))')
    row += [r[16], r[17]]
    summary.append(row)
summary.append([None] * len(SUM_HEADER))
summary.append(["Tier distribution", "Records", "Prospects (P)", "Internal (I)"] + [None] * (len(SUM_HEADER) - 4))
for t in ["Tier 1 - Immediate Opportunity", "Tier 2 - Strong Prospect", "Tier 3 - Research/Nurture", "Tier 4 - Low Priority"]:
    rn = len(summary) + 1
    summary.append([t, f"=COUNTIF($O$2:$O$46,$A{rn})", f'=COUNTIFS($O$2:$O$46,$A{rn},$A$2:$A$46,"P-*")', f'=COUNTIFS($O$2:$O$46,$A{rn},$A$2:$A$46,"I-*")'] + [None] * (len(SUM_HEADER) - 4))
summary.append(["Average total score", "=ROUND(AVERAGE($N$2:$N$46),1)", '=ROUND(AVERAGEIF($A$2:$A$46,"P-*",$N$2:$N$46),1)', '=ROUND(AVERAGEIF($A$2:$A$46,"I-*",$N$2:$N$46),1)'] + [None] * (len(SUM_HEADER) - 4))

def cell(v):
    if v is None or isinstance(v, (int, float)): return v
    s = str(v)
    if s.startswith("="): return s
    if s[:1] in "+-(0123456789'": return "'" + s
    return s
def dump(name, payload):
    with open(os.path.join(SP, name), "w", encoding="utf-8") as fh:
        fh.write(chr(10).join(json.dumps([cell(v) for v in row], ensure_ascii=False) for row in payload))
dump("method_lines.jsonl", method); dump("detail_lines.jsonl", detail_payload); dump("summary_lines.jsonl", summary)

# CSV copies with python-computed points
with open(os.path.join(PROJ, "score_factor_detail.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(DETAIL_HEADER)
    for d in detail: w.writerow([d[0], d[1], d[2], d[3], d[4], d[5], RUBRIC[d[2]][d[4]][0], d[6], d[7], d[8]])
with open(os.path.join(PROJ, "google_ads_opportunity_score.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(SUM_HEADER)
    for r in REC:
        rid = r[0]; fp = {}
        for d in detail:
            if d[0] == rid: fp[d[2]] = RUBRIC[d[2]][d[4]][0]
        low = sum(1 for d in detail if d[0] == rid and d[8] == "Low")
        w.writerow([rid, r[1], r[2]] + [fp[f] for f, _ in WEIGHTS] + [pts[rid], tier(pts[rid]), 1 + sum(1 for v in pts.values() if v > pts[rid]), low, "Low" if low >= 4 else "Medium" if low >= 2 else "High", r[16], r[17]])
with open(os.path.join(PROJ, "scoring_method.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerows([[("" if v is None else v) for v in row] for row in method])

print("method rows:", len(method), "rubric rows", RUBRIC_START, "-", RUBRIC_END, "| detail rows:", len(detail_payload), "| summary rows:", len(summary))
print("bytes:", os.path.getsize(os.path.join(SP, "method_lines.jsonl")), os.path.getsize(os.path.join(SP, "detail_lines.jsonl")), os.path.getsize(os.path.join(SP, "summary_lines.jsonl")))
ranked = sorted(pts.items(), key=lambda kv: -kv[1])
names = {r[0]: r[1] for r in REC}
print("\nRANKING")
for rid, t in ranked: print(f"  {t:5.1f}  {rid}  {names[rid]}  [{tier(t)}]")
print("\nTIERS:", dict(Counter(tier(t) for t in pts.values())))
print("avg all:", round(sum(pts.values())/45, 1), "avg P:", round(sum(v for k, v in pts.items() if k.startswith('P'))/36, 1))
