"""Step 2: build CLEANED_DATA and DATA_QUALITY_FLAGS from the raw Prospects and Internal tabs.

Raw values are embedded exactly as read from the sheet on 8 Oct 2026. Nothing is inferred:
fields with no source data are written as 'Unknown'; doubtful values are 'Needs Verification'.
"""
import re, json, csv, os
from collections import Counter

SP = r"C:\Users\Aroun\AppData\Local\Temp\claude\C--Users-Aroun-Desktop-Projects-Google-Ads-Prospects\e134b08f-71c9-4529-bc4f-df5bd3dad2a6\scratchpad\scripts"
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"

# (Partner, Client, Business URL, Phone, Email, Service, Plan, Status) — Prospects rows 2..37
PROSPECTS = [
 ("Around29","AA Roofing and Decking","aaroofingdecking.com/","(206) 280-0536","","Website Development","Studio29","Delivered"),
 ("Around29","Affordable Junk Removal","affordablejunkremovalca.com","(916) 730-8387","affordablejunkremoval916@gmail.com","Website Development","Studio29","Delivered"),
 ("Around29","Alignments Northwest LLC","alignmentsnorthwest.com","(253) 777-7092","alignmentsnw@gmail.com","Website Development","Studio29","Delivered"),
 ("Around29","American Tree Excavation","americantreeexcavation.com/","(253) 468-1505","","Website Development","Studio29","Delivered"),
 ("Around29","Around Cricket","aroundcricket.com/","(812) 121-2561","","Website Development","Custom","Delivered"),
 ("Around29","ASL Camguard","aslcamguard.com/","","","Website Development","Custom","Delivered"),
 ("Around29","Axle Surgeons of Seattle","axlesurgeonseattle.com","(253) 777-8811","mobileaxleservice@gmail.com","Website Development","Studio29","Delivered"),
 ("Around29","Brothers Micro Market","brothersmicromarket.com","(818) 367-8580","peter@brosdist.com","Website Development","Studio29","Delivered"),
 ("Around29","Calvary Cemetery","calvarycemetery.org/","(918) 299-7348","","Website Development","Custom","Delivered"),
 ("Around29","Chili On The Green","chilionthegreen.com/","","","Website Development","Studio29","Delivered"),
 ("Around29","Clean and Clean by Cliff","cleanandclearbycliff.com/","(253) 350-0457","","Website Development","Studio29","Delivered"),
 ("Around29","Cunning Dental Group","cunningdental.com/","(855) 328-6646","","Website Development","Custom","Delivered"),
 ("Around29","cunningsmiles implant experts","cunningsmiles.implant-experts.com/","","","Website Development","Studio29","Changes in Progress"),
 ("Around29","DBSA OK","dbsaok.org/","(405) 254-3994","office@dbsaok.org","Website Development","Custom","Delivered"),
 ("Around29","Kiwanis Club of Tulsa","kiwaniscluboftulsa.org/","(918) 202-5000","","Website Development","Studio29","Delivered"),
 ("Around29","La Jolla Grooming Co","ljgrooming.com/","(858) 246-6235","","Website Development","Studio29","Delivered"),
 ("Around29","Lab Rescue","labrescue.net","","","Website Development","Studio29","Delivered"),
 ("Around29","Next Level Prospect","nextlevelprospect.com/","(626) 437-3020","","Website Development","Studio29","Changes in Progress"),
 ("Around29","NorthWest Eco Clean","northwestecoclean.com/","(206) 825-6998","","Website Development","Studio29","Delivered"),
 ("Around29","Occasions Paper","occasionspaper.com/","(405) 217-8467","","Website Development","Studio29","Delivered"),
 ("Around29","Ocean View Lodging","oceanviewlodging.com/","(707) 964-7366","","Website Development","Studio29","Delivered"),
 ("Around29","Orion Opticals","orionoptical.com","(925) 349-4777","james@premomediagroup.com","Website Development","Studio29","Delivered"),
 ("Around29","Ornamental Grasses","ornamental-grasses.com/","(360) 507-8403","","Website Development","Studio29","Delivered"),
 ("Around29","Pinpoint Resource","pinpointresource.com/","(918) 622-5027","","Website Development","Studio29","Delivered"),
 ("Around29","Prime Care Dental Indy","primecaredentalindy.com/","(317) 426-1562","","Website Development","Studio29","Delivered"),
 ("Around29","Rosewood Parke","rosewoodparke.com/","","","Website Development","Studio29","Delivered"),
 ("Around29","Superior Coatings NW","superiorcoatingsnw.com/","(253) 405-5424","","Website Development","Studio29","Delivered"),
 ("Around29","Tag OK","tagok.org/","","","Website Development","Studio29","Delivered"),
 ("Around29","The Bartan Company","thebartancompany.com/","(970) 477-0796","","Website Development","Studio29","Delivered"),
 ("Around29","Top Dollar Pawn and Check Cashing","topdollartulsa.com","(918) 838-0004","","Website Development","Studio29","Delivered"),
 ("Around29","Trans Landscaping","trans-landscaping.com/","(253) 984-6802","","Website Development","Studio29","Delivered"),
 ("Around29","VIP Pest Solutions","vippestsolutions.com/","80560833847","","Website Development","Studio29","Delivered"),
 ("Around29","Wheeler Sonoma Printing","wheeler-sonoma.com/","(707) 643-6383","","Website Development","Studio29","Delivered"),
 ("Around29","Will Rogers Stage Foundation","willrogersstage.com/","","","Website Development","Custom","Delivered"),
 ("Around29","Workhub Tulsa","workhubtulsa.com/","(918) 345-1390","","Website Development","Studio29","Delivered"),
 ("Around29","Zellersins","zellersgroup.com/","(707) 996-5282","","Website Development","Studio29","Delivered"),
]
# Internal rows 2..10 (row 1 is a merged title cell, no headers)
INTERNAL = [
 ("Around29","Around29 Center for Enriched Studies","around29schools.com","9.16E+11","","Website Development","Studio29","Delivered"),
 ("Around29","Around29 Digital Media Solutions","around29.com/","(253) 954-8009","","Website Development","Studio29","Build in Progress"),
 ("Around29","Search29","","","","Website Development","Studio29","Delivered"),
 ("Around29","Send29","send29.com/","","","Website Development","Custom","Build in Progress"),
 ("Around29","Lead You","leadyou.io/","","","Website Development","Studio29","Delivered"),
 ("Around29","Around29 themes","studio29themes.com/","","","Website Development","Studio29","Delivered"),
 ("Around29","Around29.us","around29.us/","","","Website Development","Studio29","Delivered"),
 ("Around29","Starling Education","starling.education","6305992630","","Website Development","Studio29","Delivered"),
 ("Around29","Starling Wonder Kids","starlingwonderkids.com/","9.19E+11","","Website Development","Studio29","Delivered"),
]
# Actual numeric values stored behind the scientific-notation cells (source_row -> digit string), patched after the grid read
INTERNAL_PHONE_ACTUAL = {2: "916306000000", 10: "918640000000"}

AREA_HINT = {
 "206":"Seattle, WA", "253":"Tacoma / South Puget Sound, WA", "360":"Western Washington outside the Seattle metro, WA",
 "916":"Sacramento, CA", "818":"San Fernando Valley (Los Angeles), CA", "858":"San Diego (north), CA",
 "626":"San Gabriel Valley (Los Angeles area), CA", "707":"North Coast / Napa / Sonoma, CA", "925":"East Bay (Contra Costa County), CA",
 "405":"Oklahoma City, OK", "918":"Tulsa, OK", "317":"Indianapolis, IN", "970":"Colorado outside the Denver metro, CO",
 "812":"Southern Indiana, IN", "855":"Toll-free (no region)", "630":"Chicago western suburbs, IL",
}
FREEMAIL = {"gmail.com","yahoo.com","hotmail.com","outlook.com","aol.com","icloud.com","comcast.net","live.com","msn.com","me.com"}
ROLE_LOCALS = {"info","office","contact","sales","admin","support","hello","team","customerservice","mail","enquiries","inquiries"}
PARTNER_TOKENS = {"around29"}

def digits(s): return re.sub(r"\D", "", s or "")

def nanp_ok(d10):
    return len(d10) == 10 and d10[0] in "23456789" and d10[3] in "23456789"

def clean_phone(raw, actual=None):
    """returns dict(e164, display, area, hint, status, note)"""
    raw = (raw or "").strip()
    if raw == "":
        return dict(e164="Unknown", display="Unknown", area="", hint="", status="Unknown", note="")
    src = actual if actual else raw
    d = digits(src)
    if len(d) == 11 and d[0] == "1":
        d = d[1:]
    if nanp_ok(d):
        area = d[:3]
        return dict(e164="+1"+d, display=f"({d[:3]}) {d[3:6]}-{d[6:]}", area=area, hint=AREA_HINT.get(area, "Area code not in reference list"),
                    status="Valid", note="")
    # invalid
    if len(d) == 10:
        reason = f"exchange code {d[3:6]} is not valid under North American numbering (must start with 2 to 9)" if d[3] not in "23456789" else f"area code {d[:3]} is not valid"
        return dict(e164="Needs Verification", display=raw, area=d[:3], hint="n/a (number invalid)", status="Needs Verification: "+reason, note=reason)
    if actual and re.fullmatch(r"\d\.\d+E\+\d+", raw):
        reason = f"{len(d)}-digit value stored as a number and displayed as {raw}; not a 10-digit North American number" + ("; trailing zeros suggest digits were lost when the cell was stored as a number" if d.endswith("000000") else "")
    else:
        reason = f"{len(d)} digits, does not match a 10-digit North American number (with or without country code 1)"
    return dict(e164="Needs Verification", display=raw, area="", hint="", status="Needs Verification: "+reason, note=reason)

def clean_url(raw):
    raw = (raw or "").strip()
    if raw == "":
        return dict(domain="Unknown", root="Unknown", url="Unknown", slash=False)
    u = raw.lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    slash = u.endswith("/")
    u = u.rstrip("/")
    labels = u.split(".")
    root = ".".join(labels[-2:]) if len(labels) >= 2 else u
    return dict(domain=u, root=root, url=f"https://{u}/", slash=slash)

def clean_name(raw):
    s = re.sub(r"\s+", " ", (raw or "").strip())
    changed = []
    if s != (raw or ""):
        changed.append("whitespace trimmed")
    if s and s == s.lower() and re.search(r"[a-z]", s):
        s = " ".join(w.capitalize() for w in s.split(" "))
        changed.append("all-lowercase name converted to Title Case")
    return s, changed

def clean_email(raw, root_domain):
    raw0 = (raw or "").strip()
    if raw0 == "":
        return dict(std="Unknown", domain="", dtype="Unknown", status="Unknown", hint="Unknown", notes=[])
    e = raw0.lower()
    notes = []
    if e != raw0: notes.append("lower-cased")
    if not re.fullmatch(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", e):
        return dict(std="Needs Verification", domain="", dtype="Invalid syntax", status="Needs Verification", hint="Unknown", notes=["invalid syntax"])
    local, dom = e.split("@")
    if dom == root_domain:
        dtype, status = "Matches website domain", "Known"
    elif dom in FREEMAIL:
        dtype, status = "Free-mail provider", "Needs Verification"
    else:
        dtype, status = "Different business domain", "Needs Verification"
    hint = "Unknown"
    if local.isalpha() and len(local) <= 8 and local not in ROLE_LOCALS:
        hint = f"{local.capitalize()} (first name in email address; Needs Verification)"
    return dict(std=e, domain=dom, dtype=dtype, status=status, hint=hint, notes=notes)

HEADER = ["record_id","source_tab","source_row","partner","business_name_original","business_name_std",
          "website_url_original","domain_std","root_domain","url_std",
          "phone_original","phone_e164","phone_display","phone_area_code","area_code_region_hint","phone_status",
          "email_original","email_std","email_domain","email_domain_type","email_status",
          "contact_name","contact_name_hint","city","state","country","industry_category",
          "service_delivered","plan","website_project_status",
          "duplicate_class","duplicate_of","duplicate_reason","flag_count","high_severity_flags"]

records = []
for i, row in enumerate(PROSPECTS):
    records.append(dict(rid=f"P-{i+1:02d}", tab="Prospects", srow=i+2, raw=row))
for i, row in enumerate(INTERNAL):
    records.append(dict(rid=f"I-{i+1:02d}", tab="Internal", srow=i+2, raw=row))

flags = []
def flag(rec, field, code, sev, original, detail, action):
    flags.append([rec["rid"], rec["raw"][1], rec["tab"], rec["srow"], field, code, sev, original if original != "" else "(blank)", detail, action])

rule_counts = Counter()
cleaned = {}
for rec in records:
    partner, name, url, phone, email, service, plan, status = rec["raw"]
    name_std, name_changes = clean_name(name)
    for c in name_changes:
        rule_counts["R1 business name: "+c] += 1
    if "Title Case" in " ".join(name_changes):
        flag(rec, "business_name", "NAME_CASE_STANDARDIZED", "Low", name, f"All-lowercase name written as '{name_std}'; original kept in business_name_original", "Confirm the brand's preferred capitalisation")
    u = clean_url(url)
    if u["domain"] == "Unknown":
        flag(rec, "website_url", "URL_MISSING", "High", url, "No website URL in the source", "Obtain the website address or mark the record as having no site")
    else:
        if u["slash"]: rule_counts["R2 URL: trailing slash removed"] += 1
        rule_counts["R2 URL: lower-cased, scheme/www removed, https:// convention applied"] += 1
        if u["root"] != u["domain"]:
            flag(rec, "website_url", "URL_THIRD_PARTY_SUBDOMAIN", "Medium", url, f"Site is a subdomain of {u['root']}, a different root domain from the business name", "Verify who owns the root domain and whether this is the business's primary site")
        # name vs domain comparison
        name_key = re.sub(r"[^a-z0-9]", "", name.lower())
        dom_key = re.sub(r"[^a-z0-9]", "", u["domain"].split(".")[0])
        if name_key and dom_key:
            first_tok = re.sub(r"[^a-z0-9]", "", name.lower().split(" ")[0])
            mismatch = None
            if name_key.startswith("cleanandclean") and dom_key.startswith("cleanandclear"):
                mismatch = ("Medium", "Name says 'Clean and Clean' but the domain says 'cleanandclear'")
            elif name_key == "zellersins" and dom_key == "zellersgroup":
                mismatch = ("Medium", "Name 'Zellersins' does not match domain 'zellersgroup'")
            elif name_key == "orionopticals" and dom_key == "orionoptical":
                mismatch = ("Low", "Name is plural 'Opticals', domain is singular 'orionoptical'")
            elif name_key == "around29themes" and dom_key == "studio29themes":
                mismatch = ("Low", "Name 'Around29 themes' vs domain 'studio29themes'")
            if mismatch:
                flag(rec, "business_name / website_url", "NAME_DOMAIN_MISMATCH", mismatch[0], f"{name} | {url}", mismatch[1], "Confirm the legal/trading name and the correct website")
    if re.fullmatch(r"[a-z0-9]+", name.lower()) and (name.lower().endswith("ins") or "." in name):
        pass
    if name in ("Zellersins", "Around29.us"):
        flag(rec, "business_name", "NAME_LOOKS_LIKE_HANDLE", "Low", name, "Name reads like a domain or account handle rather than a trading name", "Confirm the trading name")

    actual = INTERNAL_PHONE_ACTUAL.get(rec["srow"]) if rec["tab"] == "Internal" else None
    p = clean_phone(phone, actual)
    if p["status"] == "Unknown":
        flag(rec, "phone", "PHONE_MISSING", "High", phone, "No phone number in the source", "Obtain a phone number")
    elif p["status"] == "Valid":
        rule_counts["R3 phone: normalised to E.164 (+1) and (XXX) XXX-XXXX display"] += 1
        if re.fullmatch(r"\d{10}", phone.strip()):
            flag(rec, "phone", "PHONE_UNFORMATTED_IN_SOURCE", "Low", phone, "Stored as 10 bare digits; formatted in the cleaned data", "None")
    else:
        if actual:
            flag(rec, "phone", "PHONE_STORED_AS_NUMBER", "High", f"{phone} (stored value {actual})", p["note"], "Re-enter the phone as text in the correct format after confirming the number")
        else:
            flag(rec, "phone", "PHONE_INVALID_FORMAT", "High", phone, p["note"], "Confirm the correct number with the client")
    if phone.strip() == "" :
        pass

    e = clean_email(email, u["root"])
    if e["status"] == "Unknown":
        flag(rec, "email", "EMAIL_MISSING", "High", email, "No email address in the source", "Obtain a contact email")
    else:
        if e["notes"]: rule_counts["R4 email: lower-cased/trimmed"] += 1
        rule_counts["R4 email: syntax validated, domain extracted and compared with website domain"] += 1
        if e["dtype"] == "Free-mail provider":
            extra = "; address does not contain the business name" if rec["rid"] == "P-07" else ""
            flag(rec, "email", "EMAIL_FREEMAIL", "Medium", email, f"Free-mail address ({e['domain']}); ownership and role cannot be confirmed{extra}", "Confirm the address belongs to the business and identify the person behind it")
        elif e["dtype"] == "Different business domain":
            flag(rec, "email", "EMAIL_DOMAIN_MISMATCH", "Medium", email, f"Email domain {e['domain']} differs from the website domain {u['domain']}", "Confirm whether this is the owner, a parent company or a third party")
        elif e["dtype"] == "Matches website domain" and e["std"].split("@")[0] in ROLE_LOCALS:
            flag(rec, "email", "EMAIL_ROLE_MAILBOX", "Low", email, "Generic role mailbox, not a named person", "Identify the decision maker behind the mailbox")
        if e["hint"] != "Unknown":
            flag(rec, "contact_name", "CONTACT_NAME_HINT", "Low", email, f"First name '{e['hint'].split(' ')[0]}' appears in the email address; no surname or title in the source", "Verify the person's full name and role")

    if status != "Delivered":
        flag(rec, "website_project_status", "WEBSITE_NOT_DELIVERED", "Medium", status, "Website project is not marked Delivered in the source", "Confirm the site is live before any campaign planning")
    if rec["tab"] == "Internal":
        flag(rec, "record", "INTERNAL_TAB_RECORD", "Medium", name, "Record comes from the Internal tab (no header row); names suggest Around29-owned properties", "Confirm whether this record is a prospect at all")

    cleaned[rec["rid"]] = dict(rec=rec, name_std=name_std, u=u, p=p, e=e)

# ---- duplicate handling ----
def norm_tokens(name):
    toks = [re.sub(r"[^a-z0-9]", "", t) for t in name.lower().split()]
    return [t for t in toks if t]

dup_class = {r: "Unique" for r in cleaned}
dup_of = {r: "" for r in cleaned}
dup_reason = {r: "No other record shares its name, domain, phone or email" for r in cleaned}
ids = list(cleaned.keys())
for a_i in range(len(ids)):
    for b_i in range(a_i+1, len(ids)):
        a, b = ids[a_i], ids[b_i]
        A, B = cleaned[a], cleaned[b]
        an, bn = A["rec"]["raw"][1], B["rec"]["raw"][1]
        same_dom = A["u"]["domain"] != "Unknown" and A["u"]["domain"] == B["u"]["domain"]
        same_phone = A["p"]["e164"].startswith("+") and A["p"]["e164"] == B["p"]["e164"]
        same_email = A["e"]["std"] not in ("Unknown","Needs Verification") and A["e"]["std"] == B["e"]["std"]
        same_name = re.sub(r"[^a-z0-9]","",an.lower()) == re.sub(r"[^a-z0-9]","",bn.lower())
        cls = reason = None
        if same_name and same_dom and same_phone and same_email:
            cls, reason = "Exact duplicate", "identical name, domain, phone and email"
        elif same_dom or same_phone or same_email:
            what = [w for w, s in (("domain", same_dom), ("phone", same_phone), ("email", same_email)) if s]
            cls, reason = "Likely duplicate", "same " + " and ".join(what) + " with a different name"
        else:
            ta, tb = norm_tokens(an), norm_tokens(bn)
            if ta and tb:
                fa, fb = ta[0], tb[0]
                if not any(fa.startswith(t) or fb.startswith(t) for t in PARTNER_TOKENS) and len(min(fa, fb, key=len)) >= 6 and (fa == fb or fa.startswith(fb) or fb.startswith(fa)):
                    cls = "Possible duplicate"
                    reason = f"shared leading name token '{min(fa, fb, key=len)}' while domains differ ({A['u']['domain']} vs {B['u']['domain']}); may be one organisation with two sites or a sub-brand"
        if cls:
            for x, y in ((a, b), (b, a)):
                dup_class[x] = cls
                dup_of[x] = (dup_of[x] + "; " if dup_of[x] else "") + y
                dup_reason[x] = f"{cls} of {y}: {reason}. Needs Verification"
            sev = "High" if cls == "Exact duplicate" else "Medium"
            for x, y in ((a, b), (b, a)):
                flag(cleaned[x]["rec"], "record", cls.upper().replace(" ", "_"), sev, cleaned[x]["rec"]["raw"][1], f"{reason} (other record: {y})", "Confirm whether the two records are the same business before merging")

# related entity signal: shared area code + exchange (not treated as a duplicate)
seen = {}
for r, C in cleaned.items():
    if C["p"]["status"] == "Valid":
        key = C["p"]["e164"][2:8]
        seen.setdefault(key, []).append(r)
for key, rs in seen.items():
    if len(rs) > 1:
        for r in rs:
            others = [o for o in rs if o != r]
            flag(cleaned[r]["rec"], "phone", "POSSIBLE_RELATED_ENTITY", "Low", cleaned[r]["p"]["display"], f"Shares area code and exchange {key[:3]}-{key[3:]} with {', '.join(others)}; names and domains differ, so not treated as a duplicate", "Check whether the businesses are under common ownership")

# dataset-level flags
DATASET_FLAGS = [
 ["ALL","(all records)","Prospects + Internal","","contact_name","CONTACT_FIELD_ABSENT","High","(no column)","No contact person, title or decision-maker column exists in the source; 45 of 45 records are Unknown","Add decision-maker name, title, direct phone and email during enrichment"],
 ["ALL","(all records)","Prospects + Internal","","city / state / country","LOCATION_FIELD_ABSENT","High","(no column)","No address, city, state or country column exists; 45 of 45 records are Unknown. Phone area codes are shown only as hints","Add verified location fields during enrichment"],
 ["ALL","(all records)","Prospects + Internal","","industry_category","INDUSTRY_FIELD_ABSENT","High","(no column)","No industry or category column exists; the Service column describes Around29's deliverable (Website Development)","Classify industry in the next step and record the source of each classification"],
 ["ALL","(all records)","Internal","1","header row","INTERNAL_TAB_NO_HEADER","Medium","[merged] Internal","Internal tab has a merged title cell instead of a header row; columns were mapped by position to match the Prospects tab","Add a header row to the Internal tab or merge both tabs with a record-type column"],
 ["ALL","(all records)","Prospects + Internal","","workbook","SHARING_ANYONE_CAN_EDIT","Medium","anyone with the link: writer","Workbook is editable by anyone holding the link","Restrict editing to named accounts"],
 ["ALL","(all records)","Prospects + Internal","","url_std","URL_SCHEME_UNVERIFIED","Low","(none in source)","url_std uses https:// as a convention; the source has no scheme and no URL was fetched in this step","Verify live URLs during enrichment"],
]

# ---- assemble CLEANED_DATA rows ----
rows = []
for n, (rid, C) in enumerate(cleaned.items(), start=2):
    rec, u, p, e = C["rec"], C["u"], C["p"], C["e"]
    partner, name, url, phone, email, service, plan, status = rec["raw"]
    actual = INTERNAL_PHONE_ACTUAL.get(rec["srow"]) if rec["tab"] == "Internal" else None
    phone_orig = phone if not actual else f"{phone} (stored value {actual})"
    rows.append([rid, rec["tab"], rec["srow"], partner, name, C["name_std"],
                 url if url else "(blank)", u["domain"], u["root"], u["url"],
                 phone_orig if phone_orig else "(blank)", p["e164"], p["display"], p["area"] or "Unknown", p["hint"] or "Unknown", p["status"],
                 email if email else "(blank)", e["std"], e["domain"] or "Unknown", e["dtype"], e["status"],
                 "Unknown", e["hint"], "Unknown", "Unknown", "Unknown", "Unknown",
                 service, plan, status,
                 dup_class[rid], dup_of[rid] or "None", dup_reason[rid],
                 f"=COUNTIF(DATA_QUALITY_FLAGS!$A:$A,$A{n})",
                 f"=COUNTIFS(DATA_QUALITY_FLAGS!$A:$A,$A{n},DATA_QUALITY_FLAGS!$G:$G,\"High\")"])

FLAG_HEADER = ["record_id","business_name","source_tab","source_row","field","flag_code","severity","original_value","detail","recommended_action"]
sev_rank = {"High":0,"Medium":1,"Low":2}
flags_sorted = sorted(flags, key=lambda f: (0 if f[0].startswith('P') else 1, int(f[0].split("-")[1]), sev_rank[f[6]], f[5]))
flag_rows = DATASET_FLAGS + flags_sorted

# ---- outputs ----
def sheet_cell(v, is_formula=False):
    if isinstance(v, (int, float)) or is_formula:
        return v
    s = str(v)
    if re.match(r"^[+\-=(0-9']", s):
        return "'" + s
    return s

cleaned_payload = [HEADER] + [[sheet_cell(v, is_formula=(j >= len(HEADER)-2)) for j, v in enumerate(r)] for r in rows]
flags_payload = [FLAG_HEADER] + [[sheet_cell(v) for v in r] for r in flag_rows]
os.makedirs(SP, exist_ok=True)
json.dump(cleaned_payload, open(os.path.join(SP, "cleaned_payload.json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump(flags_payload, open(os.path.join(SP, "flags_payload.json"), "w", encoding="utf-8"), ensure_ascii=False)
for fname, hdr, data in (("cleaned_data.csv", HEADER, rows), ("data_quality_flags.csv", FLAG_HEADER, flag_rows)):
    with open(os.path.join(PROJ, fname), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(hdr); w.writerows(data)

# ---- summary ----
with open(os.path.join(SP, "cleaned_lines.jsonl"), "w", encoding="utf-8") as fh:
    fh.write(chr(10).join(json.dumps(r, ensure_ascii=False) for r in cleaned_payload))
with open(os.path.join(SP, "flags_lines.jsonl"), "w", encoding="utf-8") as fh:
    fh.write(chr(10).join(json.dumps(r, ensure_ascii=False) for r in flags_payload))
print("records:", len(rows), "| flags:", len(flag_rows), f"(dataset-level {len(DATASET_FLAGS)}, record-level {len(flags_sorted)})")
print("\nRULE COUNTS")
for k, v in sorted(rule_counts.items()): print(f"  {k}: {v}")
print("\nFLAG COUNTS by code")
for code, c in sorted(Counter(f[5] for f in flag_rows).items()): print(f"  {code}: {c}")
print("\nFLAG COUNTS by severity:", dict(Counter(f[6] for f in flag_rows)))
print("\nDUPLICATE CLASSES:", dict(Counter(dup_class.values())))
for rid in cleaned:
    if dup_class[rid] != "Unique": print(f"  {rid} {cleaned[rid]['rec']['raw'][1]}: {dup_reason[rid]}")
print("\nPHONE STATUS:", dict(Counter(r[15].split(":")[0] for r in rows)))
print("EMAIL STATUS:", dict(Counter(r[20] for r in rows)))
print("EMAIL TYPES:", dict(Counter(r[19] for r in rows)))
print("payload sizes:", len(json.dumps(cleaned_payload)), len(json.dumps(flags_payload)))
