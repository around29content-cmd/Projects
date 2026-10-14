"""Step 9: BD prioritization model. Blends Google Ads opportunity (Step 5) with contactability, commercial
attractiveness, research confidence and personalization potential (Steps 3-8). Writes bd_rows.json, lists.json, CSVs."""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"
rd = lambda f: {r["record_id"]: r for r in csv.DictReader(open(os.path.join(PROJ, f), encoding="utf-8"))}
CLEAN, CLASS, FIT, SCORE = rd("cleaned_data.csv"), rd("classification.csv"), rd("google_ads_fit.csv"), rd("google_ads_opportunity_score.csv")
ENR, PITCH, OPP = rd("enriched_prospects.csv"), rd("sales_pitch_intelligence.csv"), rd("google_ads_market_opportunity.csv")

W = {"A": 0.40, "B": 0.20, "C": 0.15, "D": 0.10, "E": 0.15}

# Short sales angles for records not enriched in Step 6 (Tier 3/4 and internal). Based on Steps 3-5 only.
ANGLE = {
 "P-05": "Online cricket-gear store: Shopping/brand campaigns possible, but the market is outside the US list focus; angle only if they want US buyers.",
 "P-06": "National dash-cam brand: Shopping and brand defence; needs a product feed and national budget, not a local pitch.",
 "P-08": "No angle until the website is restored and the business is identified.",
 "P-10": "Annual Kiwanis chili event: not a paid-search prospect; route any ad request through the club (P-15).",
 "P-14": "Mental-health nonprofit: Google Ad Grants programme, not paid search.",
 "P-15": "Service club: Google Ad Grants for membership/events; no commercial sale.",
 "P-17": "Animal rescue nonprofit: Google Ad Grants for adoptions/donations.",
 "P-18": "Nonprofit mentoring programme with site in progress: no paid-search angle yet.",
 "P-20": "Paper/gift retailer: small store-visit campaign on carried brands and local gift terms; modest budget.",
 "P-23": "Plant nursery by appointment: seasonal store-visit campaign at best; unclear retail model.",
 "P-24": "Formalwear/tuxedo retailer: local 'tuxedo rental [city]' and wedding terms for store visits.",
 "P-26": "Homeowners association: not a business; no angle.",
 "P-28": "Animal-welfare awareness programme: Google Ad Grants; no commercial conversion.",
 "P-29": "Event services outside the US: angle only if they target US clients.",
 "P-30": "Pawn shop: local 'pawn shop near me' and 'sell gold' intent is strong, but loan and firearm policies limit ads; needs a policy review before any pitch.",
 "P-34": "Performing-arts venue: seasonal ticket-sales campaigns plus Ad Grants for awareness; small budgets.",
 "I-01": "Internal (Around29 school site): not a sales prospect.",
 "I-02": "Internal (Around29 agency): not a sales prospect.",
 "I-03": "Internal (Search29): not a sales prospect.",
 "I-04": "Internal (Send29): not a sales prospect.",
 "I-05": "Internal (Lead You): not a sales prospect.",
 "I-06": "Internal (Around29 themes): not a sales prospect.",
 "I-07": "Internal (Around29.us): not a sales prospect.",
 "I-08": "Internal (Starling Education): not a sales prospect.",
 "I-09": "Internal (Starling Wonder Kids): not a sales prospect.",
}


def f(x):
    try: return float(x)
    except: return 0.0


def contactability(rid):
    e = ENR.get(rid)
    if e:
        pts, why = 0, []
        ps, es = e["phone_status"], e["email_status"]
        if ps.startswith("Verified") and "DIFFERS" not in ps: pts += 40; why.append("phone verified on site (40)")
        elif ps.startswith("Verified"): pts += 35; why.append("phone verified on site, file value wrong (35)")
        elif "Conflicting" in ps: pts += 15; why.append("phone conflicts between file and site (15)")
        elif e["phone"] != "Not Found": pts += 20; why.append("phone unverified (20)")
        else: why.append("no phone (0)")
        if es.startswith("Verified"): pts += 25; why.append("email verified on site (25)")
        elif e["email"] != "Not Found": pts += 12; why.append("email from directory/conflicting (12)")
        else: why.append("no email (0)")
        c = e["contact_name"]
        if c == "Not Found": why.append("no named contact (0)")
        elif "[Needs Verification]" in c: pts += 20; why.append("named contact from directory (20)")
        elif "first name" in c.lower() or "surname not" in c.lower(): pts += 12; why.append("first name only (12)")
        else: pts += 35; why.append("named contact on official source (35)")
        return pts, "; ".join(why)
    r = CLEAN[rid]; pts, why = 0, []
    if r["phone_status"] == "Valid": pts += 25; why.append("valid phone on file, unverified (25)")
    else: why.append("no valid phone (0)")
    if r["email_std"] not in ("", "Unknown"): pts += 12; why.append("email on file, unverified (12)")
    else: why.append("no email (0)")
    if r["contact_name"] not in ("", "Unknown"): pts += 20; why.append("contact name on file (20)")
    else: why.append("no contact name (0)")
    why.append("not enriched in Step 6")
    return pts, "; ".join(why)


def commercial(rid):
    s = SCORE[rid]
    cv, sc, ind = f(s["Customer Value Potential"]), f(s["Business Scalability"]), f(s["Industry Google Ads Fit"])
    pts = round((cv + sc + ind) / 35 * 100)
    return pts, "Step 5 factors: customer value %g/15, scalability %g/5, industry fit %g/15" % (cv, sc, ind)


def confidence(rid):
    base = {"High": 70, "Medium": 45, "Low": 20}.get(SCORE[rid]["overall_confidence"], 20)
    why = "Step 5 confidence %s (%d)" % (SCORE[rid]["overall_confidence"], base)
    e = ENR.get(rid)
    if e:
        v = e["verification_status"]
        add = 30 if v.startswith("Verified") else 15 if v.startswith("Partially") else 5
        base += add; why += "; Step 6 %s (+%d)" % (v.split(" (")[0].split(" - ")[0], add)
    else:
        why += "; not enriched (+0)"
    return min(base, 100), why


def personalization(rid):
    p = PITCH.get(rid)
    if p:
        r = p["outreach_readiness"]
        pts = {"Ready to Contact": 100, "Contact After Research": 75, "Missing Critical Information": 10}.get(r, 50)
        return pts, "Step 8 hook written; readiness %s (%d)" % (r, pts)
    fit = FIT[rid]["google_ads_fit"]
    pts = {"Excellent": 60, "Strong": 60, "Moderate": 45, "Weak": 25, "Poor": 15, "Unknown": 10}.get(fit, 10)
    return pts, "no Step 8 hook; Step 4 fit %s (%d)" % (fit, pts)


def category(rid, tier, ready):
    if rid.startswith("I-"):
        return "Priority 4 - Deprioritize", "Internal Around29 record, not a sales prospect"
    t = int(tier.split()[1]); fit = FIT[rid]["google_ads_fit"]
    if t <= 2 and ready == "Ready to Contact":
        return "Priority 1 - Contact Now", "Tier %d opportunity; verified channel, named contact and Step 8 hook" % t
    if t <= 2:
        return "Priority 2 - Contact After Enrichment", "Tier %d opportunity; Step 8 readiness '%s'" % (t, ready)
    if t == 3 and fit in ("Excellent", "Strong", "Moderate", "Unknown"):
        return "Priority 3 - Research / Nurture", "Tier 3 score with Step 4 fit %s; evidence incomplete" % fit
    if t == 3:
        return "Priority 4 - Deprioritize", "Tier 3 score but Step 4 fit %s" % fit
    return "Priority 4 - Deprioritize", "Tier 4 score; Step 4 fit %s" % fit


rows = []
for rid, s in SCORE.items():
    name = CLEAN[rid]["business_name_std"]; tier = s["tier"]; ads = f(s["total_score"])
    b, bw = contactability(rid); c, cw = commercial(rid); d, dw = confidence(rid); e, ew = personalization(rid)
    bd = round(W["A"] * ads + W["B"] * b + W["C"] * c + W["D"] * d + W["E"] * e, 1)
    ready = PITCH[rid]["outreach_readiness"] if rid in PITCH else "Not enriched"
    cat, creason = category(rid, tier, ready)
    angle = OPP[rid]["primary_opportunity"] if rid in OPP and rid != "P-13" else ANGLE.get(rid, "Verify the business before any angle.")
    model = CLASS[rid]["business_model"]
    rows.append(dict(rid=rid, name=name, industry=CLASS[rid]["primary_industry"], model=model, ads=ads, tier=tier, b=b, bw=bw, c=c, cw=cw,
                     d=d, dw=dw, e=e, ew=ew, bd=bd, cat=cat, creason=creason, angle=angle, internal=rid.startswith("I-")))

pri = lambda r: int(r["cat"].split()[1])
rows.sort(key=lambda r: (r["internal"], pri(r), -r["bd"], -r["ads"]))
for i, r in enumerate(rows, 1): r["rank"] = i

H = ["rank", "record_id", "business_name_std", "industry", "business_model", "google_ads_score", "ads_tier", "contactability_0_100", "contactability_basis",
     "commercial_potential_0_100", "commercial_basis", "research_confidence_0_100", "confidence_basis", "personalization_0_100", "personalization_basis",
     "bd_score", "final_priority", "priority_reason", "sales_angle"]
sheet, csvrows = [], []
for i, r in enumerate(rows, start=2):
    base = [r["rank"], r["rid"], r["name"], r["industry"], r["model"]]
    tail = [r["b"], r["bw"], r["c"], r["cw"], r["d"], r["dw"], r["e"], r["ew"], r["bd"], r["cat"], r["creason"], r["angle"]]
    sheet.append(base + ['=IFERROR(VLOOKUP($B%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$N$46,14,FALSE),"Unknown")' % i,
                         '=IFERROR(VLOOKUP($B%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$O$46,15,FALSE),"Unknown")' % i] + tail)
    csvrows.append(base + [r["ads"], r["tier"]] + tail)
with open(os.path.join(PROJ, "bd_prioritization.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(H); w.writerows(csvrows)

prospects = [r for r in rows if not r["internal"]]
lab = lambda r: "%s %s (%s, BD %.1f)" % (r["rid"], r["name"], r["cat"].split(" - ")[0], r["bd"])
lists = {
    "Top 10": [lab(r) for r in prospects[:10]],
    "Top 25": [lab(r) for r in prospects[:25]],
    "Immediate Outreach (Priority 1)": [lab(r) for r in prospects if pri(r) == 1],
    "Enrichment Required (Priority 2)": [lab(r) for r in prospects if pri(r) == 2],
    "Research Required (Priority 3)": [lab(r) for r in prospects if pri(r) == 3],
    "Deprioritized (Priority 4)": [lab(r) for r in rows if pri(r) == 4],
}
json.dump(sheet, open(os.path.join(HERE, "bd_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump(lists, open(os.path.join(HERE, "bd_lists.json"), "w", encoding="utf-8"), ensure_ascii=False)
with open(os.path.join(PROJ, "bd_lists.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["list", "entry"])
    for k, v in lists.items():
        for x in v: w.writerow([k, x])
from collections import Counter
print(Counter(r["cat"] for r in rows))
for r in rows: print(r["rank"], r["rid"], r["name"][:28].ljust(28), "ads", r["ads"], "B", r["b"], "C", r["c"], "D", r["d"], "E", r["e"], "BD", r["bd"], "|", r["cat"])
