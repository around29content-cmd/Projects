"""Step 6: compile agent research JSON into ENRICHED_PROSPECTS and MISSING_DATA_QUEUE rows.

Reads scratchpad/enrich/group*.json, writes:
  enrich_rows.json   (ENRICHED_PROSPECTS rows, formulas for tier/score)
  queue_rows.json    (MISSING_DATA_QUEUE rows)
  project CSVs enriched_prospects.csv and missing_data_queue.csv
Never fills a value the agents did not source; unverified values carry a [Needs Verification] suffix.
"""
import csv, glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ENRICH = os.path.join(HERE, "..", "enrich")
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"
RESEARCHED_ON = "2026-10-08"

# Python-side tier/score (sheet uses VLOOKUP formulas; these feed the CSV and priority logic)
SCORES = {}
with open(os.path.join(PROJ, "google_ads_opportunity_score.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        SCORES[r["record_id"]] = (r["tier"], float(r["total_score"]))

FILE = {}
with open(os.path.join(PROJ, "cleaned_data.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        FILE[r["record_id"]] = {
            "phone": r["phone_original"] if r["phone_original"] not in ("", "(blank)") else "",
            "email": r["email_std"] if r["email_std"] not in ("", "Unknown") else "",
            "name": r["business_name_std"],
            "url": r["url_std"],
        }

ORDER = ["P-25", "P-12", "P-01", "P-32", "P-02", "P-22", "P-27",
         "P-07", "P-31", "P-04", "P-35", "P-03", "P-21", "P-36", "P-19", "P-16", "P-09", "P-11", "P-33",
         "P-13"]

FIELDS = ["contact_name", "contact_role", "owner", "founder", "marketing_contact", "phone", "email", "website",
          "address", "service_area", "number_of_locations", "locations", "business_type", "primary_services",
          "high_value_services", "booking_contact_method"]
CORE = {"contact_name", "contact_role", "phone", "email", "website", "address", "service_area"}

PHONE_RE = re.compile(r"\(?\b(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})\b")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

NEXT_ACTION = {
    "contact_name": "Call the main line and ask for the owner or decision-maker by name and role; check the LinkedIn company page.",
    "contact_role": "Confirm the contact's role on the first call.",
    "owner": "Ask on the call who owns the business; confirm against the state business registry (manual lookup).",
    "founder": "Ask on the call; low priority unless it is the same person as the decision-maker.",
    "marketing_contact": "Ask on the first call who handles marketing and the website; many small firms have none (record 'owner handles marketing').",
    "phone": "Call the number shown on the official site to confirm it rings through, then correct the Prospects tab.",
    "email": "Request a direct email on the first call; use the website contact form until then.",
    "website": "Open the site manually and confirm it is live and belongs to this business.",
    "address": "Confirm the street address on the call and against the Google Business Profile.",
    "service_area": "Ask which cities or counties they serve; required before any geo-targeting is set up.",
    "number_of_locations": "Confirm on the call.",
    "locations": "Confirm on the call.",
    "business_type": "Confirm the legal entity with a manual registry lookup (WA SOS CCFS, CA bizfile, OK SOS or IN INBiz) or ask on the call.",
    "primary_services": "Review the site manually and confirm on the call.",
    "high_value_services": "Ask on the call which services they most want to grow.",
    "booking_contact_method": "Review the site manually.",
}


def clean(v):
    if isinstance(v, (list, tuple)):
        v = "; ".join(clean(x) for x in v)
    return re.sub(r"\s+", " ", str(v or "")).strip()


def status_of(fo):
    return clean(fo.get("status", "")) if isinstance(fo, dict) else ""


def display(field, fo):
    """Cell text for a field object."""
    if not isinstance(fo, dict):
        return "Not Found"
    st = status_of(fo)
    val = clean(fo.get("value", ""))
    if st == "Not Found" or val.lower().startswith("not found") or val == "":
        return "Not Found"
    if field == "phone":
        m = PHONE_RE.search(val)
        if m:
            val = "(%s) %s-%s" % m.groups()
    if field == "email":
        m = EMAIL_RE.search(val)
        if m:
            val = m.group(0)
    if "Needs Verification" in st:
        return val + " [Needs Verification]"
    if st == "Official registry":
        return val + " [registry]"
    return val


def is_found(fo):
    return display("x", fo) != "Not Found"


def is_verified(fo):
    return status_of(fo).startswith("Verified") or status_of(fo) == "Official registry"


def compile_record(rec):
    rid = rec["record_id"]
    tier, score = SCORES[rid]
    tier_num = int(tier.split()[1])
    f = {k: rec.get(k, {}) for k in FIELDS}

    found_core = sum(1 for k in CORE if is_found(f[k]))
    verified_core = sum(1 for k in CORE if is_verified(f[k]))
    if found_core == len(CORE):
        enrichment = "Enriched - all core fields found"
    elif found_core >= 4:
        enrichment = "Enriched - partial (%d of %d core fields found)" % (found_core, len(CORE))
    else:
        enrichment = "Minimal (%d of %d core fields found)" % (found_core, len(CORE))

    conflicts = [k for k in ("phone", "email", "address", "website") if "Conflicting" in status_of(f[k])]
    if conflicts:
        verification = "Needs Verification - conflicting " + ", ".join(conflicts)
    elif all(is_verified(f[k]) for k in ("phone", "website", "address")):
        verification = "Verified - phone, website and address on official sources"
    elif verified_core >= 3:
        verification = "Partially Verified (%d of %d core fields on official sources)" % (verified_core, len(CORE))
    else:
        verification = "Needs Verification"

    src_parts = []
    for k in ("phone", "email", "address", "contact_name", "owner", "service_area"):
        s = clean(f[k].get("source", "")) if isinstance(f[k], dict) else ""
        if s and is_found(f[k]):
            src_parts.append("%s: %s" % (k, s))
    source = " | ".join(src_parts) if src_parts else "; ".join(rec.get("sources_consulted", [])[:3])

    phone_status = status_of(f["phone"]) or "Not Found"
    mf = f["phone"].get("matches_file") if isinstance(f["phone"], dict) else None
    if not FILE[rid]["phone"]:
        mf = None
    if mf is True:
        phone_status += "; matches number on file"
    elif mf is False:
        phone_status += "; DIFFERS from number on file"
    email_status = status_of(f["email"]) or "Not Found"
    mfe = f["email"].get("matches_file") if isinstance(f["email"], dict) else None
    if not FILE[rid]["email"]:
        mfe = None
        if is_found(f["email"]):
            email_status += "; no email was on file - new"
    if mfe is True:
        email_status += "; matches email on file"
    elif mfe is False:
        email_status += "; DIFFERS from email on file"

    std_name = FILE[rid]["name"]
    agent_name = clean(rec.get("business_name", ""))
    notes = clean(rec.get("notes", ""))
    if agent_name and agent_name != std_name:
        notes = "Name as found: " + agent_name + ". " + notes
    web_cell = display("website", f["website"])
    if web_cell == "Not Found" and FILE[rid]["url"]:
        web_cell = FILE[rid]["url"] + " [Needs Verification - not live on 2026-10-08]"
    row = [rid, std_name, tier, score, enrichment,
           display("contact_name", f["contact_name"]), display("contact_role", f["contact_role"]),
           display("owner", f["owner"]), display("founder", f["founder"]), display("marketing_contact", f["marketing_contact"]),
           display("phone", f["phone"]), phone_status, display("email", f["email"]), email_status,
           web_cell, status_of(f["website"]) or "Not Found",
           display("address", f["address"]), display("service_area", f["service_area"]),
           display("number_of_locations", f["number_of_locations"]), display("locations", f["locations"]),
           display("business_type", f["business_type"]), display("primary_services", f["primary_services"]),
           display("high_value_services", f["high_value_services"]), display("booking_contact_method", f["booking_contact_method"]),
           source, verification, notes, RESEARCHED_ON]

    # queue rows
    checked = "; ".join(rec.get("sources_consulted", []))
    q = []
    for k in FIELDS:
        fo = f[k]
        st = status_of(fo) or "Not Found"
        if is_found(fo) and ("Needs Verification" not in st):
            continue
        cur = display(k, fo)
        if k in ("phone", "email", "address", "contact_name") and tier_num == 1:
            pri = "High"
        elif (k in CORE and tier_num <= 2) or tier_num == 1:
            pri = "Medium"
        else:
            pri = "Low"
        why = st if cur == "Not Found" else st + ": " + clean(fo.get("value", ""))[:300]
        q.append([rid, std_name, tier, score, k, cur, checked[:700], why, NEXT_ACTION[k], pri])
    if mf is False:
        q.append([rid, std_name, tier, score, "phone (on file)", "Prospects tab value differs from official site",
                  checked[:700], "Official site shows " + display("phone", f["phone"]), "Correct the Prospects phone after confirming by call.", "High" if tier_num == 1 else "Medium"])
    if mfe is False:
        q.append([rid, std_name, tier, score, "email (on file)", "Prospects tab value differs from official site",
                  checked[:700], "Official site shows " + display("email", f["email"]), "Confirm which address the business wants used.", "High" if tier_num == 1 else "Medium"])
    return row, q


def main():
    recs = {}
    for fp in sorted(glob.glob(os.path.join(ENRICH, "group*.json"))):
        for r in json.load(open(fp, encoding="utf-8")):
            recs[r["record_id"]] = r
    rows, queue = [], []
    for rid in ORDER:
        if rid not in recs:
            print("MISSING", rid)
            continue
        row, q = compile_record(recs[rid])
        rows.append(row)
        queue.extend(q)
    prio = {"High": 0, "Medium": 1, "Low": 2}
    queue.sort(key=lambda r: (prio[r[9]], ORDER.index(r[0]), FIELDS.index(r[4]) if r[4] in FIELDS else -1))

    header = ["record_id", "business_name_std", "tier", "total_score", "enrichment_status", "contact_name", "contact_role", "owner", "founder",
              "marketing_contact", "phone", "phone_status", "email", "email_status", "website", "website_status", "address", "service_area",
              "number_of_locations", "locations", "business_type", "primary_service", "high_value_services", "booking_contact_method",
              "source", "verification_status", "notes", "researched_on"]
    qheader = ["record_id", "business_name_std", "tier", "total_score", "missing_field", "current_value", "sources_checked", "why_missing",
               "suggested_next_action", "priority"]
    with open(os.path.join(PROJ, "enriched_prospects.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(header); w.writerows(rows)
    with open(os.path.join(PROJ, "missing_data_queue.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(qheader); w.writerows(queue)

    # sheet payloads: tier and score as formulas against GOOGLE_ADS_OPPORTUNITY_SCORE
    def cap(v, n):
        v = str(v)
        return v if len(v) <= n else v[: n - 20].rstrip() + " ... [full text in CSV]"
    sheet_rows = []
    for i, r in enumerate(rows, start=2):
        rr = [cap(c, 600) for c in r]
        rr[24] = cap(r[24], 400)
        rr[26] = cap(r[26], 800)
        rr[2] = '=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$O$46,15,FALSE),"Unknown")' % i
        rr[3] = '=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$N$46,14,FALSE),"Unknown")' % i
        sheet_rows.append(rr)
    sheet_q = []
    for i, r in enumerate(queue, start=2):
        rr = list(r)
        srcs = [x.strip() for x in str(r[6]).split(";") if x.strip()]
        rr[6] = "%d sources checked: %s" % (len(srcs), "; ".join(srcs[:3])) if srcs else r[6]
        rr[6] = cap(rr[6], 260)
        rr[7] = cap(r[7], 260)
        rr[2] = '=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$O$46,15,FALSE),"Unknown")' % i
        rr[3] = '=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$N$46,14,FALSE),"Unknown")' % i
        sheet_q.append(rr)
    json.dump(sheet_rows, open(os.path.join(HERE, "enrich_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(sheet_q, open(os.path.join(HERE, "queue_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("records", len(rows), "queue rows", len(queue))
    from collections import Counter
    print(Counter(r[9] for r in queue))
    print(Counter(r[4] for r in queue).most_common())
    for r in rows:
        print(r[0], "|", r[4], "|", r[25], "| phone:", r[10], "| email:", r[12], "| contact:", r[5])


if __name__ == "__main__":
    main()
