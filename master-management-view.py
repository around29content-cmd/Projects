"""MASTER MANAGEMENT VIEW: one row per business, 8 columns, from the approved Step 3-9 outputs.
Score framework (management brief): Fit 20, Commercial 15, Value 15, Search 15, Conversion 10, Geo 10, Urgency 5, Scalability 5, Digital 5.
Step 5 factor points are reused; Industry Fit (/15) is rescaled to /20; Data Completeness is dropped so data quality earns nothing."""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"
rd = lambda f: {r["record_id"]: r for r in csv.DictReader(open(os.path.join(PROJ, f), encoding="utf-8"))}
S, C, CL, P = rd("google_ads_opportunity_score.csv"), rd("classification.csv"), rd("cleaned_data.csv"), rd("sales_pitch_intelligence.csv")
F = rd("google_ads_fit.csv")
f = lambda x: float(x or 0)

IND = {"P-01": "Home Services", "P-02": "Home Services", "P-03": "Automotive", "P-04": "Home Services", "P-05": "Ecommerce", "P-06": "Automotive",
       "P-07": "Automotive", "P-08": "Unknown", "P-09": "Other", "P-10": "Other", "P-11": "Home Services", "P-12": "Dental", "P-13": "Dental",
       "P-14": "Other", "P-15": "Other", "P-16": "Other", "P-17": "Other", "P-18": "Education", "P-19": "Home Services", "P-20": "Retail",
       "P-21": "Hospitality", "P-22": "Healthcare", "P-23": "Retail", "P-24": "Retail", "P-25": "Dental", "P-26": "Other", "P-27": "Home Services",
       "P-28": "Other", "P-29": "Other", "P-30": "Financial Services", "P-31": "Home Services", "P-32": "Home Services", "P-33": "B2B",
       "P-34": "Other", "P-35": "Real Estate", "P-36": "Insurance", "I-01": "Education", "I-02": "Professional Services", "I-03": "Unknown",
       "I-04": "Technology", "I-05": "Technology", "I-06": "Technology", "I-07": "Professional Services", "I-08": "Education", "I-09": "Education"}
MODEL = {"P-01": "High-Ticket Service", "P-02": "Local Service", "P-03": "B2B", "P-04": "Emergency Service", "P-05": "Ecommerce", "P-06": "Manufacturer",
         "P-07": "Emergency Service", "P-08": "Unknown", "P-09": "Consultation", "P-10": "Other (charity event)", "P-11": "Recurring Service",
         "P-12": "High-Ticket Service", "P-13": "High-Ticket Service", "P-14": "Other (nonprofit)", "P-15": "Other (nonprofit)", "P-16": "Appointment-Based",
         "P-17": "Other (nonprofit)", "P-18": "Other (nonprofit)", "P-19": "Subscription", "P-20": "Retail", "P-21": "Appointment-Based", "P-22": "Appointment-Based",
         "P-23": "Retail", "P-24": "Retail", "P-25": "Multi-Location", "P-26": "Other (association)", "P-27": "Project-Based", "P-28": "Other (nonprofit)",
         "P-29": "Project-Based", "P-30": "Retail", "P-31": "Project-Based", "P-32": "Recurring Service", "P-33": "B2B", "P-34": "Other (nonprofit)",
         "P-35": "Subscription", "P-36": "Consultation", "I-01": "Appointment-Based", "I-02": "B2B", "I-03": "Unknown", "I-04": "Subscription",
         "I-05": "Subscription", "I-06": "Ecommerce", "I-07": "B2B", "I-08": "Unknown", "I-09": "Appointment-Based"}
ANGLE = {
 "P-32": "Verified three-county pest and termite operator with recurring plans and a $95 inspection offer; contact the CEO now.",
 "P-25": "Two-office dental practice with online booking; implant and Invisalign Search per office. Contact the named dentist (owner unverified).",
 "P-01": "Licensed roofer with financing and high-ticket replacements but no cities on site; contact the owner and confirm service area.",
 "P-36": "Independent agency with four Medicare specialists; Annual Enrollment runs to 7 Dec. Contact the president this week.",
 "P-02": "Owner-run junk removal with online booking and strong reviews; same-day and commercial Search plus brand defence. Contact the owner.",
 "P-27": "Licensed painter with commercial references; exterior and commercial Search for Pierce County. Contact the owner (name from BBB).",
 "P-16": "Family grooming salon in affluent La Jolla with repeat clients; tight-radius Search and Maps. Contact the founder.",
 "P-33": "Specialty printer (engraving, wine labels) with named owner; specialty Search after adding a quote form. Contact the owner.",
 "P-03": "Niche mobile truck-alignment service with little competition; fleet-focused Search on the I-5 corridor. Contact Jordan or Austin.",
 "P-04": "BBB-accredited 24-hour tree service with no service area on site; emergency Search for Pierce County. Contact the owner (name from BBB).",
 "P-19": "Subscription bin cleaning with online scheduling in King County; route-density Search plus HOA and commercial. Contact the owner (name from BBB).",
 "P-35": "32-suite office building pre-leasing six suites for 1 Nov with pricing and tour form live; launch Tulsa office Search now.",
 "P-11": "Window cleaner with Housecall Pro booking; Christmas-light season is live. Contact Cliff and launch the seasonal campaign.",
 "P-12": "Highest-value implant and full-arch practice, but current owner unknown and no email. Identify the decision-maker, then pitch.",
 "P-22": "Luxury optical boutique with online exam booking; owner unnamed and an outside agency may already run marketing. Clarify first.",
 "P-31": "Verified nine-city hardscape contractor with free estimates; no decision-maker named anywhere. Identify the owner, then pitch seasonally.",
 "P-07": "24/7 mobile axle repair with high-intent B2B demand; no person, email or confirmed brand relationship. Identify the operator first.",
 "P-09": "Diocesan cemetery expanding pre-need sales; executive director role in transition. Identify the new director before pitching.",
 "P-21": "Ocean-view lodge losing direct bookings to OTAs; phone on file conflicts and operator unknown. Confirm contact, then pitch brand defence.",
 "P-30": "Strong local pawn and gold-buying intent, but loan and firearm policies limit ads. Policy review before any outreach.",
 "P-24": "Formalwear retailer; local tuxedo and wedding terms could drive store visits. Verify contact and decision-maker first.",
 "P-20": "Paper and gift retailer; small store-visit campaign at best. Verify contact and whether budget exists before outreach.",
 "P-06": "National dash-cam brand suited to Shopping, not local Search; no phone, email or contact on file. Research before outreach.",
 "P-13": "Implant site is dead and may duplicate Cunning Dental Group; confirm the business exists before any action.",
 "P-34": "Performing-arts venue with seasonal ticket sales; small budgets, Ad Grants likely better. Research before outreach.",
 "P-29": "Event services based in India; outside the US market this list serves. Deprioritize.",
 "P-23": "Plant nursery by appointment with weak search fit and small tickets. Deprioritize.",
 "P-05": "Cricket-gear ecommerce serving a non-US market. Deprioritize unless they want US buyers.",
 "P-18": "Nonprofit mentoring programme with site in progress; no paid-search conversion. Deprioritize.",
 "P-14": "Mental-health nonprofit; no commercial conversion. Refer to Google Ad Grants, not paid search.",
 "P-10": "Annual Kiwanis charity event; not a paid-search prospect. Deprioritize.",
 "P-15": "Service club with no commercial conversion. Refer to Ad Grants; deprioritize for paid search.",
 "P-17": "Animal rescue nonprofit; Ad Grants route. Deprioritize for paid search.",
 "P-28": "Animal-welfare awareness programme; Ad Grants route. Deprioritize for paid search.",
 "P-08": "Website down and business unidentified. Deprioritize until the site is restored.",
 "P-26": "Homeowners association, not a business. Deprioritize.",
}
INTERNAL_ANGLE = "Around29 internal property, not a sales prospect; excluded from outreach."

def score(rid):
    s = S[rid]
    return round(f(s["Industry Google Ads Fit"]) * 20 / 15 + f(s["Commercial Intent"]) + f(s["Customer Value Potential"]) + f(s["Search Intent"])
                 + f(s["Conversion Potential"]) + f(s["Geographic Targeting"]) + f(s["Urgency"]) + f(s["Business Scalability"]) + f(s["Digital Readiness"]), 1)

rows = []
for rid in S:
    sc = score(rid)
    opp = "HIGH" if sc >= 75 else "MEDIUM" if sc >= 50 else "LOW"
    internal = rid.startswith("I-")
    ready = P[rid]["outreach_readiness"] if rid in P else None
    if internal: contact = "NOT READY"
    elif ready == "Ready to Contact": contact = "READY"
    elif ready == "Contact After Research": contact = "ENRICH FIRST"
    elif ready == "Missing Critical Information": contact = "NOT READY"
    elif opp == "LOW": contact = "NOT READY"
    else: contact = "ENRICH FIRST"  # not enriched, commercially plausible, contact data incomplete
    if internal: pri = "P4"
    elif opp == "HIGH" and contact == "READY": pri = "P1"
    elif contact == "ENRICH FIRST" and sc >= 65: pri = "P2"
    elif opp == "MEDIUM" and contact != "NOT READY": pri = "P3"
    elif contact == "READY" and opp == "MEDIUM": pri = "P3"
    else: pri = "P4"
    # rule overrides from the brief: outside target market / weak fit / insufficient evidence -> P4; policy obstacle -> P3
    if rid in ("P-05", "P-23"): contact, pri = "NOT READY", "P4"
    if rid == "P-13": pri = "P4"
    if rid == "P-30": pri = "P3"
    rows.append(dict(rid=rid, name=CL[rid]["business_name_std"], ind=IND[rid], model=MODEL[rid], opp=opp, sc=sc, contact=contact, pri=pri,
                     angle=INTERNAL_ANGLE if internal else ANGLE[rid], internal=internal))
# fix display names found in Step 6
fix = {"P-11": "Clean & Clear by Cliff", "P-36": "Zellers Group (Zellersins)", "P-33": "Wheeler-Sonoma Printers", "P-22": "Orion Optical"}
for r in rows:
    if r["rid"] in fix: r["name"] = fix[r["rid"]]
oppn = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}; cn = {"READY": 0, "ENRICH FIRST": 1, "NOT READY": 2}
rows.sort(key=lambda r: (r["internal"], r["pri"], -r["sc"], oppn[r["opp"]], cn[r["contact"]]))
H = ["Business", "Industry", "Business Model", "Google Ads Opportunity", "Opportunity Score", "Contactability", "Priority", "BD Action / Sales Angle"]
tbl = [[r["name"], r["ind"], r["model"], r["opp"], r["sc"], r["contact"], r["pri"], r["angle"]] for r in rows]
json.dump(tbl, open(os.path.join(HERE, "master_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
with open(os.path.join(PROJ, "master_management_view.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(H); w.writerows(tbl)
from collections import Counter, defaultdict
print(Counter(r["pri"] for r in rows), Counter(r["opp"] for r in rows), Counter(r["contact"] for r in rows))
g = defaultdict(list)
for r in rows:
    if not r["internal"]: g[r["ind"]].append(r["sc"])
for k, v in sorted(g.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])): print(k, len(v), round(sum(v) / len(v), 1))
for r in rows: print(r["pri"], r["sc"], r["opp"], r["contact"], r["name"], "|", len(r["angle"].split()))
