"""Steps 7 and 8: Google Ads opportunity research and sales-pitch intelligence for Tier 1/2 prospects.

Inputs already verified in Steps 3-6 (website text 8 Oct 2026, enrichment JSON, lp_facts.json).
No search volumes are asserted. Landing-page issues are limited to facts observable in the saved HTML
or confirmed by the Step 6 research. Inferred business problems are prefixed 'Potential problem'.
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"
LP = json.load(open(os.path.join(HERE, "lp_facts.json"), encoding="utf-8"))

# (rid, name, tier, score)
ORDER = [("P-25", "Prime Care Dental Indy"), ("P-12", "Cunning Dental Group"), ("P-01", "AA Roofing and Decking"),
         ("P-32", "VIP Pest Solutions"), ("P-02", "Affordable Junk Removal"), ("P-22", "Orion Opticals"),
         ("P-27", "Superior Coatings NW"), ("P-07", "Axle Surgeons of Seattle"), ("P-31", "Trans Landscaping"),
         ("P-04", "American Tree Excavation"), ("P-35", "Workhub Tulsa"), ("P-03", "Alignments Northwest LLC"),
         ("P-21", "Ocean View Lodging"), ("P-36", "Zellersins"), ("P-19", "NorthWest Eco Clean"),
         ("P-16", "La Jolla Grooming Co"), ("P-09", "Calvary Cemetery"), ("P-11", "Clean and Clean by Cliff"),
         ("P-33", "Wheeler Sonoma Printing"), ("P-13", "Cunningsmiles Implant Experts")]


def lpfacts(rid):
    """Verifiable landing-page facts string from saved HTML."""
    r = LP.get(rid)
    if not r:
        return "Site not live on 8 Oct 2026 (403/404); no landing page to assess."
    h = r.get("home") or {}
    st = r.get("page_status", {})
    bits = []
    bits.append("home HTML %d KB" % (h.get("bytes", 0) // 1024))
    bits.append("viewport meta present" if h.get("viewport_meta") else "NO viewport meta")
    bits.append("%d tel: link(s) on home" % len(h.get("tel_links", [])))
    bits.append("%d <form> element(s) on home" % h.get("forms", 0))
    bits.append("booking widget: " + (", ".join(h.get("booking_widgets")) if h.get("booking_widgets") else "none detected"))
    bits.append("CTA wording: " + (", ".join(h.get("cta_words")) if h.get("cta_words") else "none of the standard CTA phrases found in links/buttons"))
    missing = [k for k, v in st.items() if v == "404" and k in ("about", "contact")]
    if st.get("about") == "404" and st.get("about-us") == "404":
        bits.append("/about and /about-us return 404")
    if st.get("contact") == "404" and st.get("contact-us") == "404":
        bits.append("/contact and /contact-us return 404")
    return "; ".join(bits)


# Step 7 and Step 8 content. Keys: po primary_opportunity, hv high_value_service, kw keyword_themes, geo, conv, camp, lp (issues/opportunities,
# analyst reading of facts), ev evidence, conf confidence | why, prob, adsopp, strat, mvc, hook, ready, rreason, contact
D = {}

D["P-25"] = dict(
 po="Appointment-driven dental Search campaigns for two Indianapolis offices, split by location, leading with implants, Invisalign and emergency dentistry.",
 hv="Dental implants; Invisalign and braces; porcelain veneers / smile makeover; sedation dentistry; emergency dental care (same-day appointments advertised).",
 kw="Service + city: 'dentist Indianapolis', 'dental implants Indianapolis', 'Invisalign Indianapolis', 'emergency dentist Indianapolis'; near me: 'dentist near me', 'emergency dentist near me'; neighbourhood: 'dentist Lawrence IN', 'dentist 86th street Indianapolis'; cost: 'dental implant cost', 'Invisalign cost'; insurance/Medicaid: 'dentist that accepts Medicaid Indianapolis' (children); appointment: 'same day dentist', 'book dentist appointment'. Spanish-language variants (site advertises bilingual staff). No volumes asserted.",
 geo="Two radius targets around the published offices: 8180 Pendleton Pike (east Indianapolis / Lawrence) and 8660 Purdue Rd (northwest Indianapolis), each roughly 8-12 miles, with location-specific ad copy and location extensions. Exclude overlap only if budgets are separate.",
 conv="Calls (five tel: links on the home page; per-location numbers) and online 'Book My Appointment' form submissions. Most valuable: a booked new-patient appointment for implants or Invisalign.",
 camp="Search (non-brand, by service and location) is the core. Brand Search to protect the practice name cheaply. Local campaign / Performance Max with location assets for Google Maps placement near each office. Remarketing to visitors of implant and Invisalign pages. Shopping not applicable.",
 lp="Positive: online booking forms per office and same-day appointment messaging exist. Issues: service-specific pages exist (12 service links) but there is no dedicated contact page (/contact-us and /about return 404; contact sits on the home page); no 'free consultation' or cost/financing wording detected on the home page for high-ticket implants. Recommend dedicated implant and Invisalign landing pages with a consult offer and the per-office booking form embedded. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /locations/, dentist bio page); Step 6 enrichment (two offices, phone verified, no email published); lp_facts: viewport present, 5 tel links, 0 <form> elements on home (booking uses buttons/links), 404 on /about.",
 conf="High",
 why="Two-office family and cosmetic dental practice in Indianapolis with very high case values (implants, Invisalign, veneers), constant local search demand and an existing online booking path. Highest Step 5 score (92.5).",
 prob="Potential problem: filling new-patient slots for high-margin procedures (implants, Invisalign) across two offices rather than routine cleanings; the site advertises same-day appointments, which suggests capacity to absorb demand. Not verified with the practice.",
 adsopp="Advertise implants, Invisalign, veneers/smile makeover, sedation and emergency dentistry to adults within ~10 miles of each office, plus children's dentistry with Medicaid acceptance to parents in the Lawrence area; drive calls and 'Book My Appointment' submissions.",
 strat="Start with two Search campaigns (one per office) built around implant, Invisalign and emergency themes with call extensions and location extensions; add a small Brand campaign; after 30 days of conversion data add Performance Max with the office locations and a remarketing list for implant/Invisalign page visitors. Build two service landing pages with the booking form embedded before launch.",
 mvc="Booked new-patient appointment for an implant or Invisalign consultation (tracked via booking-form submission and call tracking per office).",
 hook="You run two offices and already offer same-day appointments and online booking, but when someone in Lawrence or northwest Indy searches 'dental implants near me' tonight, nothing points them to your Pendleton Pike or 86th Street office. A per-office Search campaign on implants, Invisalign and emergency visits would put each office in front of those searches and send them straight to your existing 'Book My Appointment' form.",
 ready="Ready to Contact", rreason="Phone verified on the official site for both offices; dentist named on site; clear service and booking path. Email not published, so first touch is a call or the site form.",
 contact="Dr. Vijaya Palaparthi, DDS (dentist; owner status unknown) via (317) 426-1562 (Pendleton Pike office) or (317) 426-0299 (86th Street office).")

D["P-12"] = dict(
 po="Implant and full-arch ('Teeth in 1 Day' / All-on-4) Search campaigns across the Inland Empire and San Gabriel Valley service area, with sedation and financing messaging.",
 hv="Dental implants; Teeth in 1 Day / All-on-4 full-arch restorations; sedation dentistry; veneers; braces/clear aligners; Zoom whitening. On-site lab is a differentiator for same-day work.",
 kw="Service + city: 'dental implants Montclair CA', 'all on 4 Inland Empire', 'dental implants Chino Hills / Ontario / West Covina' (the site already has city pages); near me: 'dental implants near me', 'sedation dentist near me'; cost/financing: 'all on 4 cost', 'dental implant financing', 'teeth in a day cost'; PPO: 'dentist that takes PPO insurance' (site says PPO only). No volumes asserted.",
 geo="Montclair office radius plus the eleven named service-area cities (Chino Hills, Eastvale, Fontana, Ontario Ranch, Rialto, Covina, Diamond Bar, Glendora, La Verne, San Dimas, West Covina). Full-arch implant patients travel further, so a 20-25 mile radius for implant campaigns and a tighter radius for general dentistry.",
 conv="Calls to the new-patient line (855) 328-6646 and /contact/ 'Make An Appointment' form submissions (with SMS opt-in). Most valuable: an implant or full-arch consultation booked.",
 camp="Non-brand Search on implant/full-arch/sedation themes (expensive but very high value). Brand Search (the 'Group' name attracts competitor bidding risk). Remarketing is important for a long implant decision cycle. Performance Max with location assets once conversions are tracked. Shopping not applicable.",
 lp="Issues verifiable: home page HTML is ~950 KB (heaviest of all prospects), a page-speed risk for paid traffic; contact is form-only (no email), no third-party online scheduler; 'Make An Appointment' links go to the generic /contact/ page rather than a procedure-specific page. Positive: financing and special-offers pages exist, city pages exist, strong implant/full-arch content. Recommend a dedicated full-arch landing page with financing, before/after gallery and the form embedded, and a page-weight review. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us/, /contact/, city pages); Step 6 enrichment (single published office, founder Dr. Ronald Cunning, current owner Not Found); lp_facts: 974 KB home HTML, 1 tel link, 0 <form> on home, financing wording present.",
 conf="High",
 why="Full-service implant and cosmetic practice with on-site lab branded as a group, serving a large Inland Empire footprint; full-arch cases are among the highest-value transactions in local services. Step 5 score 91.5.",
 prob="Potential problem: generating implant and full-arch consultations at predictable cost in a crowded, expensive keyword market; the practice has invested in financing and special-offer pages and city pages, which suggests lead generation for high-ticket work is a priority. Ownership may have changed ('under new management' banner seen on a job board, unverified), which could mean marketing is being re-evaluated.",
 adsopp="Advertise Teeth in 1 Day / All-on-4, implants, sedation dentistry and financing to adults 45+ across the eleven service-area cities; secondary campaign for veneers/aligners; drive calls to the new-patient line and consultation form submissions.",
 strat="Phase 1: Non-brand Search on full-arch and implant themes with a dedicated landing page, call tracking and the SMS-opt-in form; Brand Search to defend the name. Phase 2 (after 30-45 days): remarketing across Display/YouTube to implant-page visitors, then Performance Max. Fix page weight before scaling spend.",
 mvc="Booked implant or full-arch consultation (form submission or tracked call to the new-patient line).",
 hook="Your site already does the hard part for full-arch cases: city pages for eleven Inland Empire towns, financing, an on-site lab and 'Teeth in 1 Day'. What it lacks is paid visibility when someone in Chino Hills or West Covina searches 'all on 4 cost' or 'dental implants near me'. A Search campaign on those exact searches, landing on a full-arch page with your financing options, would turn that content into consultation requests on your (855) new-patient line.",
 ready="Contact After Research", rreason="Phone and address verified, but the current owner is Not Found and the only named manager comes from a 2023 TV segment that may be stale; a job-board banner suggests new management. Confirm the decision-maker by calling the new-patient line before pitching. No email published.",
 contact="Main line (855) 328-6646; ask for the practice owner or office manager (Katherine Pohjola, GM per 2023 source, unverified).")

D["P-01"] = dict(
 po="Roof replacement and repair Search campaigns for south King County and Pierce County, with a seasonal deck-building campaign in spring and summer.",
 hv="Full roof replacement / re-roof (all roof types incl. metal, tile, TPO/PVC, commercial); roof repair; custom and composite deck builds; patio covers and pergolas; financing available (Enhancify).",
 kw="Service + city: 'roofing contractor Auburn WA', 'roof replacement Kent / Federal Way / Puyallup', 'metal roofing Tacoma'; near me: 'roofers near me', 'roof repair near me'; emergency: 'emergency roof repair', 'roof leak repair'; cost/financing: 'roof replacement cost', 'roof financing'; quote: 'free roofing estimate'; seasonal: 'deck builder Auburn WA', 'composite deck installation', 'patio cover installation'. No volumes asserted.",
 geo="Service area is unverified (site says 'Pacific NW'; BBB says Auburn and surrounding; a job post says King and Pierce counties). Likely a 20-25 mile radius around Auburn covering south King and north Pierce County, to be confirmed on the call before launch.",
 conv="Phone calls (tel link in header) and contact-form submissions for a free estimate. Most valuable: a scheduled roof-replacement estimate.",
 camp="Non-brand Search (roofing first, decks seasonally). Brand Search is low value (short brand name) but cheap. Local Services Ads are worth raising separately since the WA contractor licence is displayed (not a Google Ads campaign type, flagged for the pitch). Remarketing to estimate-form abandoners. Performance Max later with photo assets from the gallery.",
 lp="Issues verifiable: only one service link detected from the home page and a generic 'Contact us' CTA; /about and /about-us return 404 (no About page); no street address or service-area cities on the site. Positive: phone and email in header, free-estimate wording for re-roof on the roofing page, financing page present. Recommend a roof-replacement landing page with a quote form, service-area cities and licence number, plus a deck page for summer. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /roofing, /contact-us/); Step 6 enrichment (BBB A+ accredited, licence AAROORD797KC on site, owner per BBB); lp_facts: 1 tel link, 0 <form> on home, 1 service link, financing wording present, 404 on about pages.",
 conf="Medium (service area unverified)",
 why="Licensed, BBB-accredited roofing and deck contractor in the Seattle-Tacoma corridor; roof replacements are multi-thousand-dollar, urgent, call-driven jobs and the owner is reachable. Step 5 score 90.5.",
 prob="Potential problem: inconsistent lead flow for high-ticket roof replacements between seasons, and no way for searchers to find the company by city because the site names no service area; a young company (founded 2021 per BBB) typically needs a steadier pipeline than referrals alone. Not verified.",
 adsopp="Advertise roof replacement and repair (metal, composition, flat/TPO) to homeowners in Auburn, Kent, Federal Way and Puyallup, with financing as the differentiator, and deck/patio-cover builds in spring and summer; generate estimate calls and quote-form submissions.",
 strat="Launch a single Search campaign with roofing ad groups (replacement, repair, metal, leak/emergency) and a call-first landing page; add a seasonal deck campaign in March. Confirm the service-area cities on the first call before setting geo targets. Add remarketing after the first month.",
 mvc="Scheduled free estimate for a roof replacement (tracked call or quote-form submission).",
 hook="Your site lists every roof type you install and offers financing, but it never says which cities you serve, and nothing shows up when a homeowner in Kent or Federal Way searches 'roof replacement near me'. A roofing Search campaign aimed at south King and Pierce County, landing on a page with your licence number, financing and a free-estimate form, would turn those searches into estimate calls on (206) 280-0536.",
 ready="Ready to Contact", rreason="Phone and email verified on the official site; owner/managing member named by BBB (needs confirming on the call); service area to be confirmed but not a blocker for a first conversation.",
 contact="Ahmed R. Al-Jebori, Managing Member (per BBB) via (206) 280-0536 or Aaroofinganddecking@gmail.com.")

D["P-32"] = dict(
 po="Termite and recurring pest-control Search campaigns across San Luis Obispo, Santa Barbara and Ventura counties, with real-estate termite inspections as a low-cost lead-in.",
 hv="Termite fumigation and treatments/repairs; recurring pest-control plans (monthly/bimonthly/quarterly); rodent control and exclusion; commercial pest plans; $95 real-estate termite inspections.",
 kw="Service + city: 'pest control Santa Maria', 'termite inspection San Luis Obispo', 'exterminator Santa Barbara', 'pest control Ventura County'; near me: 'pest control near me', 'termite company near me'; urgent: 'rodent removal', 'ant exterminator'; cost: 'termite fumigation cost', 'termite inspection cost'; real estate: 'escrow termite inspection'. No volumes asserted.",
 geo="Three-county service area verified on the contact page (San Luis Obispo, Santa Barbara, Ventura); base in Santa Maria. Prioritise Santa Maria / SLO / Santa Barbara metros first, expand to Ventura County once cost per lead is known.",
 conv="Phone calls (24/7 per home page) and the 'Schedule Now' contact form with a service-type dropdown. Most valuable: a termite inspection booked (leads to fumigation/treatment) or a recurring pest plan sign-up.",
 camp="Non-brand Search by service and county. Brand Search under both names ('VIP Pest Solutions' and 'Veritas Innovative Pest') to catch the legal-name searches. Local campaign / Performance Max with the Santa Maria location. Remarketing to inspection-page visitors. Shopping not applicable.",
 lp="Positive: two <form> elements on the home page, free-estimate wording, emergency/24-7 wording, three-county service area stated. Issues verifiable: no service-specific landing links detected from home (service_link_count 0 by our pattern); the /our-location/ page returns 404; the vanity phone format '608-3VIP/3847' may confuse call tracking copy. Recommend termite and recurring-plan landing pages with the form and the $95 inspection offer. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us/, /contact-us/); Step 6 enrichment (correct phone (805) 608-3847, email, CA corporation Active, BBB accredited A+); lp_facts: 2 forms, free estimate and emergency wording present, 0 service links by pattern.",
 conf="High",
 why="Family-run, BBB-accredited pest and termite company covering three Central Coast counties, with recurring-revenue plans and high-ticket termite work; contact data is now fully verified after correcting the phone on file. Step 5 score 88.",
 prob="Potential problem: growing recurring pest-plan customers and termite jobs across a wide three-county area against national franchises, and capturing real-estate termite inspections that lead to treatment work. Not verified.",
 adsopp="Advertise termite inspections ($95), fumigation/treatment, recurring pest plans and rodent exclusion to homeowners and property managers in Santa Maria, San Luis Obispo, Santa Barbara and Ventura County; generate 24/7 calls and 'Schedule Now' form submissions.",
 strat="Search campaign with termite, general pest and rodent ad groups geo-targeted to the three counties, call extensions on the corrected number, and a termite landing page carrying the $95 inspection offer; Brand Search under both business names; add Performance Max with location assets after 30 days.",
 mvc="Booked termite inspection or recurring pest-plan sign-up (tracked call or form submission).",
 hook="You already serve three counties and offer a $95 termite inspection, which is exactly the kind of offer that wins a 'termite inspection near me' search in San Luis Obispo or Santa Barbara. A Search campaign on termite and pest terms across your service area, landing on a page with that offer and your 'Schedule Now' form, would bring in inspections that turn into fumigation and recurring-plan customers.",
 ready="Ready to Contact", rreason="Phone (corrected), email, address and service area all verified on the official site; CEO named on the BBB accredited profile.",
 contact="Jamie Parkins, CEO (BBB) via (805) 608-3847 or info@vippestsolutions.com. Note the phone on the Prospects tab is wrong.")

D["P-02"] = dict(
 po="Same-day junk removal Search campaigns for Sacramento and Rocklin, with a separate commercial and property-management cleanout campaign.",
 hv="Hoarder-house cleanouts; commercial, office and warehouse cleanouts; property-management turnovers; construction debris removal; spa/hot-tub removal; same-day pickup.",
 kw="Service + city: 'junk removal Sacramento', 'junk hauling Rocklin', 'hot tub removal Sacramento'; near me: 'junk removal near me', 'furniture removal near me'; urgency: 'same day junk removal'; cost/quote: 'junk removal prices', 'free junk removal quote'; commercial: 'office cleanout Sacramento', 'construction debris removal', 'estate cleanout'. No volumes asserted.",
 geo="Sacramento metro plus Rocklin (dedicated page) and surrounding Placer/Sacramento County suburbs; a 20-mile radius around the 95826 base, with Rocklin as a separate location target.",
 conv="Online 'Book An Appointment' form with 2-hour slots and photo upload, quote form, and calls. Most valuable: a booked pickup (especially commercial or whole-house cleanouts).",
 camp="Non-brand Search (residential same-day plus a commercial ad group). Brand Search is needed because the generic name 'Affordable Junk Removal' is easily poached by competitors and franchises. Local campaign / Performance Max with the Sacramento location. Remarketing to quote-page visitors. Shopping not applicable.",
 lp="Positive: two <form> elements, booking form with time slots and photo upload, 'get a free quote' and 'schedule' CTAs, free-estimate wording. Issues verifiable: home HTML ~505 KB (heavy); street address absent from the site (ZIP only) and conflicting across BBB/Yelp, which weakens location extensions until fixed. Recommend a commercial-cleanout landing page and resolving the address for Google Business Profile consistency. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /contact-us/, Rocklin page); Step 6 enrichment (phone and email on file match, owner Ashley Ramirez per BBB accredited profile, address conflict); lp_facts: 517 KB home, 2 forms, quote/schedule CTAs.",
 conf="High",
 why="Owner-operated junk-removal company with online booking, same-day service, a strong review footprint and a named owner; junk removal is a high-intent, call-and-book category with repeat commercial accounts. Step 5 score 87.",
 prob="Potential problem: competing against national junk-removal franchises for 'near me' searches and getting enough higher-value commercial and property-management jobs rather than single-item pickups; the generic business name also makes brand defence necessary. Not verified.",
 adsopp="Advertise same-day junk removal, hot-tub and appliance removal to homeowners in Sacramento and Rocklin, and cleanouts/debris removal to property managers, offices and contractors; generate online bookings with photo upload and quote calls.",
 strat="Two Search campaigns: residential (same-day, item-specific) and commercial (cleanouts, debris, property management), both with call extensions and the booking form as the landing destination; Brand Search from day one; Performance Max with location assets after conversion volume builds. Resolve the street address first for consistent location extensions.",
 mvc="Booked pickup via the online booking form (ideally a commercial or whole-house cleanout) or a tracked quote call.",
 hook="Your booking form with two-hour slots and photo upload is better than most national franchises offer, but 'junk removal near me' searches in Sacramento and Rocklin are going to those franchises because they advertise and you don't. A Search campaign for same-day residential pickups plus a separate one for office and property-management cleanouts would send that demand to your booking form, and a small brand campaign would stop competitors buying your name.",
 ready="Ready to Contact", rreason="Phone and email verified and match the file; owner named on BBB accredited profile; online booking already in place. Address conflict is a housekeeping item, not a blocker.",
 contact="Ashley Ramirez, Owner (BBB) via (916) 730-8387 or affordablejunkremoval916@gmail.com.")

D["P-22"] = dict(
 po="Local Search and Maps campaigns for eye exams and designer eyewear in Concord and central Contra Costa County, with online scheduling as the conversion.",
 hv="Comprehensive digital eye exams (no-dilation); designer/luxury frames (Cartier, Prada, Lindberg, Oliver Peoples); contact-lens fittings; FSA/HSA year-end eyewear purchases.",
 kw="Service + city: 'eye exam Concord CA', 'optometrist Concord', 'eyeglasses Walnut Creek / Pleasant Hill'; near me: 'eye exam near me', 'optical store near me'; brand/product: 'Cartier glasses Bay Area', 'Lindberg frames near me', 'Oliver Peoples Concord'; appointment: 'book eye exam online', 'same day eye exam'; seasonal: 'use FSA on glasses'. No volumes asserted.",
 geo="Single store in the Veranda shopping centre, Concord CA; radius 8-10 miles covering Concord, Pleasant Hill, Walnut Creek, Martinez and Clayton; extend for luxury-frame brand searches to the wider East Bay.",
 conv="Online appointment scheduling via the revintake widget, calls, and store visits. Most valuable: a booked eye exam (which leads to an eyewear sale).",
 camp="Non-brand Search (exams and frame brands). Brand Search ('Orion Optical' is short and ambiguous, so protect it). Local campaign / Performance Max with store location for Maps and directions. Shopping is possible in future if frames were listed online (not today: no e-commerce detected). Remarketing to scheduler abandoners.",
 lp="Positive: online scheduling widget embedded, 'book now' and 'schedule' CTAs, hours and address on site. Issues verifiable: home HTML ~380 KB; no contact form and no email on the site (phone/widget only); no service-specific landing links detected by pattern. Recommend an eye-exam landing page with the scheduler embedded and a luxury-frames page per brand. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /contact-us/); Step 6 enrichment (phone matches, address verified, email on file belongs to a Tacoma agency, no owner named); lp_facts: revintake/schedulewidget detected, 0 forms, 1 tel link.",
 conf="Medium (decision-maker and marketing ownership unclear)",
 why="Independent optical boutique with on-site eye exams, luxury frame brands and an online scheduler in an affluent East Bay suburb; appointment-plus-retail model with repeat visits. Step 5 score 85.5.",
 prob="Potential problem: filling exam slots and selling high-margin designer frames against chain optical retailers and online eyewear, where Maps and 'eye exam near me' visibility decide the visit. The on-file email suggests an outside agency may already handle marketing, so the real problem may be performance of existing efforts. Not verified.",
 adsopp="Advertise digital eye exams and designer frames to adults in Concord, Walnut Creek and Pleasant Hill, plus FSA/HSA year-end messaging in Q4; generate online exam bookings, calls and store directions.",
 strat="Search campaign with exam and frame-brand ad groups, call and location extensions, landing on an exam page with the scheduler embedded; Brand Search; Performance Max with store location for Maps presence; a Q4 FSA/HSA push. Clarify first whether Premo Media Group currently runs marketing to avoid channel conflict.",
 mvc="Booked eye exam through the online scheduler (tracked widget conversion) or a tracked call.",
 hook="You carry Cartier, Lindberg and Oliver Peoples and have online exam booking already live, yet someone in Walnut Creek searching 'Lindberg frames near me' or 'eye exam Concord' won't find Orion Optical in the ads or the map pack. A local Search and Maps campaign on exams and your frame brands, landing on your scheduler, would fill exam slots that turn into frame sales, with an FSA push before year end.",
 ready="Contact After Research", rreason="Phone and address verified, but no owner is named anywhere and the email on file is a third-party marketing agency (Premo Media Group); confirm who makes marketing decisions and whether an agency is already engaged before pitching.",
 contact="Store line (925) 349-4777; ask for the owner (only 'Lynda' is named on the site, role not stated). Do not use the on-file agency email for the pitch.")

D["P-27"] = dict(
 po="Exterior and interior painting Search campaigns for Pierce County / South Puget Sound, with a commercial-painting ad group.",
 hv="Exterior residential repaints; commercial painting (site cites Verizon South Sound stores); industrial coatings; cabinet refinishing; deck and fence staining.",
 kw="Service + city: 'house painters Puyallup', 'exterior painting Tacoma', 'commercial painting contractor Pierce County'; near me: 'painters near me', 'cabinet painting near me'; quote: 'free painting estimate', 'painting quote'; cost: 'cost to paint house exterior'; seasonal: 'exterior house painting' (spring-summer). No volumes asserted.",
 geo="South Puget Sound / Pierce County verified on site; base in Puyallup per directories. Radius 15-20 miles around Puyallup covering Tacoma, Sumner, Bonney Lake, Lakewood, Federal Way.",
 conv="'Request a Quote' form (one <form> on home) and calls; free-estimate CTA. Most valuable: a booked exterior-repaint or commercial estimate.",
 camp="Non-brand Search (residential exterior/interior, cabinet, commercial). Brand Search (name conflict between 'Superior Coatings NW' and 'Superior Coatings Inc' makes brand defence useful). Remarketing for quote abandoners. Performance Max later with gallery images. Shopping not applicable.",
 lp="Positive: quote form on home, 'free estimate' CTA, licence number displayed, service area stated. Issues verifiable: no street address on the site; entity name inconsistent between footer ('Superior Coatings Inc.') and About ('Superior Coatings NW, LLC'); only two service links detected. Recommend an exterior-painting landing page with gallery and quote form and a separate commercial page. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us/, /contact-us/); Step 6 enrichment (phone and email verified, owner per BBB/Chamber, WA LLC Active via registry mirror, address from directories); lp_facts: 1 form, free estimate CTA, 2 service links.",
 conf="High",
 why="Licensed owner-operated painting contractor with residential, commercial and industrial work in the South Sound; exterior repaints and commercial jobs are high-ticket and quote-driven. Step 5 score 85.",
 prob="Potential problem: smoothing the seasonal swing in exterior work and winning more commercial contracts, where the company has proof (named retail-store work) but no paid visibility. Not verified.",
 adsopp="Advertise exterior and interior house painting, cabinet refinishing and commercial painting to homeowners and facility managers in Puyallup, Tacoma and Pierce County; generate quote-form submissions and estimate calls.",
 strat="One Search campaign with residential (exterior, interior, cabinets) and commercial ad groups, call extensions and the quote form as the landing destination; run exterior-heavy from March to September and shift to interior/cabinets in winter; Brand Search throughout; remarketing after month one.",
 mvc="Scheduled free estimate for an exterior repaint or commercial project (quote form or tracked call).",
 hook="You've painted retail stores for a national carrier and you offer free estimates, but a Puyallup homeowner searching 'exterior house painters near me' this spring won't see you. A Search campaign for Pierce County painting, landing on a page with your licence, your commercial work and your quote form, would fill the summer exterior calendar and bring in the commercial enquiries your portfolio deserves.",
 ready="Ready to Contact", rreason="Phone and email verified on the official site; owner named consistently by BBB, Chamber and the state registry agent record (confirm on call); service area verified.",
 contact="Donovan (Donny) Peters, Owner via (253) 405-5424 or superiorcoatings123@gmail.com.")

D["P-07"] = dict(
 po="24/7 emergency and fleet Search campaigns for mobile truck/trailer axle and spindle repair across the Seattle-Tacoma freight corridor.",
 hv="Trailer and drive-axle spindle replacement ('a quarter of the cost of new'); spindle plus spider-plate combination jobs; king-pin sleeving; trunnion shaft replacement; fleet accounts.",
 kw="B2B emergency: 'mobile axle repair Seattle', 'trailer spindle replacement Tacoma', 'truck spindle repair near me', 'mobile semi truck repair Kent WA'; fleet: 'fleet axle repair Washington', 'on-site trailer repair'; product/part: 'king pin sleeving', 'trailer axle spindle replacement cost'. Low-volume but very high intent; no volumes asserted.",
 geo="Seattle/Tacoma verified on site; mobile service from Tacoma base (2323 E Q St). Target the I-5 corridor from Everett to Olympia plus the Port of Tacoma and Kent Valley industrial areas; include truck-stop and freight-yard locations.",
 conv="Calls ('call to make an appointment anytime 24/7') and the contact form. Most valuable: an emergency dispatch call for a spindle replacement, or a fleet account enquiry.",
 camp="Non-brand Search only (category is too niche for Shopping or Performance Max to add much). Brand Search for 'Axle Surgeons Seattle/Tacoma' to capture people who know the national brand and want the local operator. Call-only ads with 24/7 scheduling are a natural fit. Remarketing has limited value for emergency repairs but can work for fleet managers.",
 lp="Issues verifiable: none of the standard CTA phrases found in links or buttons on the home page; contact form only (no email on the site); address exists only as a Maps embed, not text; /contact-us returns 404 (/contact works). Positive: 24/7 and emergency wording present, service pages exist. Recommend a call-first mobile landing page with a tap-to-call button above the fold and a fleet-enquiry form. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /services/, /contact/); Step 6 enrichment (phone verified, email on file unverified, no person named, national-brand relationship unconfirmed); lp_facts: no CTA phrases detected, 0 forms on home, emergency wording present.",
 conf="Medium (no decision-maker; brand relationship unclear)",
 why="Niche B2B emergency repair with little local competition, very high intent per search and repeat fleet work; mobile on-site service across the region's busiest freight corridor. Step 5 score 84.",
 prob="Potential problem: being found at the moment a trailer is down on the roadside or in a yard, when the dispatcher searches 'mobile axle repair' and calls the first result; also converting one-off emergency jobs into fleet accounts. Not verified.",
 adsopp="Advertise 24/7 mobile spindle and axle repair to truck drivers, dispatchers and fleet managers along I-5 and in the Port of Tacoma and Kent Valley; generate immediate emergency calls and fleet-account enquiries.",
 strat="A compact Search campaign with call-only ads scheduled 24/7 on emergency and spindle/axle terms, geo-targeted to the freight corridor; a fleet ad group landing on an enquiry form; Brand Search for the Axle Surgeons name plus Seattle/Tacoma. Confirm the franchise/brand relationship first so ads respect the national brand's rules.",
 mvc="Emergency dispatch call for a spindle or axle repair (tracked call), with fleet-account enquiry as the secondary conversion.",
 hook="When a trailer is down at the Port of Tacoma, the dispatcher searches 'mobile axle repair near me' and calls whoever appears first. You offer 24/7 on-site spindle replacement at a quarter of the cost of a new axle, but you're not in those results. A call-only Search campaign along the I-5 corridor would put your (253) number in front of that search at the exact moment it happens.",
 ready="Contact After Research", rreason="Phone verified but no owner, manager or entity name is published anywhere, the email on file is unverified, and the relationship to the national Axle Surgeons brand (which may restrict local advertising) is unconfirmed. Call the main line to identify the operator before pitching.",
 contact="Main line (253) 777-8811; ask for the owner/operator. Do not rely on mobileaxleservice@gmail.com (unverified).")

D["P-31"] = dict(
 po="Hardscape and landscape-installation Search campaigns for Pierce County, seasonal, led by patios, retaining walls and irrigation.",
 hv="Concrete and paver patios; flagstone walkways; retaining walls; decks and fences; irrigation systems; sod installation.",
 kw="Service + city: 'landscaping Puyallup', 'paver patio installation Spanaway', 'retaining wall contractor Pierce County', 'landscaper Graham WA'; near me: 'landscapers near me', 'patio installers near me'; quote: 'free landscaping estimate'; cost: 'paver patio cost', 'retaining wall cost'; seasonal: 'sprinkler system installation' (spring). No volumes asserted.",
 geo="All of Pierce County verified on site with named cities (Spanaway, Puyallup, South Hill, Auburn, Bonney Lake, Sumner, Edgewood, Milton, Graham); radius 15 miles around Spanaway.",
 conv="Phone (free estimate, 7 days a week) and the contact form. Most valuable: a scheduled estimate for a patio, retaining wall or full landscape install.",
 camp="Non-brand Search (hardscape, irrigation, general landscaping ad groups), seasonal March-October. Brand Search low value. Performance Max with gallery images once conversions exist (visual category). Remarketing to gallery visitors. Shopping not applicable.",
 lp="Positive: 'get a quote' CTA, free-estimate wording, service-area cities in footer, gallery page. Issues verifiable: no About page (/about and /about-us 404); no street address on site; only one service link detected from home; last home-page modification 2024 per schema. Recommend a hardscape landing page with gallery, the city list and the estimate form. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /services/, /contact-us/); Step 6 enrichment (phone verified, email published, legal name Tran's Landscaping and Gardening LLC, licence on site, no person named); lp_facts: quote CTA, free estimate wording, 0 forms on home, 404 about.",
 conf="Medium (no decision-maker named)",
 why="Licensed landscape-installation contractor with high-ticket hardscape work (patios, retaining walls) and a verified nine-city Pierce County service area; estimate-driven, seasonal demand. Step 5 score 83.5.",
 prob="Potential problem: filling the spring-to-autumn calendar with larger hardscape projects rather than maintenance jobs, and standing out against many Pierce County landscapers for the same 'landscapers near me' searches. Not verified.",
 adsopp="Advertise paver and concrete patios, retaining walls, decks/fences and irrigation installs to homeowners in Puyallup, Spanaway, Bonney Lake and surrounding Pierce County cities; generate estimate calls and quote-form submissions.",
 strat="Seasonal Search campaign (March-October) with hardscape, irrigation and general landscaping ad groups, call extensions and a gallery-led landing page with the estimate form; add Performance Max with project photos in year two; remarketing to gallery visitors.",
 mvc="Scheduled free estimate for a hardscape or full-yard installation (tracked call or form).",
 hook="Your footer already lists nine Pierce County cities and your gallery shows the patios and retaining walls that make up the big jobs, but when a Puyallup homeowner searches 'paver patio installers near me' in April, you're not there. A seasonal Search campaign on hardscape terms across those nine cities, landing on your gallery with the free-estimate form, would book the larger projects before the summer calendar fills.",
 ready="Contact After Research", rreason="Phone and email verified but no owner or contact name is published anywhere (testimonials mention a 'Tom', role unknown); street address rests on directories. Call the main line to identify the decision-maker.",
 contact="Main line (253) 984-6802 or trans_landscaping@yahoo.com; ask for the owner.")

D["P-04"] = dict(
 po="Emergency and hazardous tree-removal Search campaigns for Puyallup / Pierce County with stump grinding as the add-on.",
 hv="Tree removal (large or hazardous trees near structures, storm damage); 24-hour emergency service; stump grinding; pruning/thinning. (Excavation and land clearing are in the name but not described on the website.)",
 kw="Service + city: 'tree removal Puyallup', 'tree service Tacoma', 'stump grinding Pierce County'; near me: 'tree removal near me', 'arborist near me'; emergency: 'emergency tree removal', 'storm damage tree removal', '24 hour tree service'; cost/quote: 'tree removal cost', 'free tree removal estimate'. No volumes asserted.",
 geo="Pierce County per BBB; Puyallup base (two conflicting street addresses in directories). Website states no service area, so confirm on the call. Likely a 20-mile radius around Puyallup covering Tacoma, Sumner, Bonney Lake, Graham and Spanaway.",
 conv="Calls (click-to-call) and the Contact Form 7 quote form. Most valuable: an emergency or large-tree removal estimate call.",
 camp="Non-brand Search with an always-on emergency ad group (call-only, 24/7 schedule) and a standard removal/stump ad group. Brand Search low value. Local Services Ads worth raising separately (licence displayed). Remarketing limited. Performance Max later.",
 lp="Positive: 24-hour emergency wording, free-estimate wording, coupons ($150 off $1000+ projects), click-to-call. Issues verifiable: no address, city or service area anywhere on the site; no About page (404); only one service link detected; generic 'Contact us' CTA; no email on the site. Recommend an emergency tree-removal landing page with city list, tap-to-call and the quote form, and clarify whether excavation is actually offered. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /services/, /contact-us/); Step 6 enrichment (phone verified, owner per BBB accredited profile, address conflict, service area only from BBB); lp_facts: emergency and free-estimate wording, 0 forms on home, 1 service link, 404 about.",
 conf="Medium (service area not on site)",
 why="BBB-accredited, licensed tree service with 24-hour emergency work in a storm-prone region; hazardous tree removal is urgent and high-ticket, and the owner is named. Step 5 score 80.",
 prob="Potential problem: capturing emergency and large-removal calls when storms hit, and being findable by city when the website names no location at all; also possible confusion from the 'Excavation' name if that service is not offered. Not verified.",
 adsopp="Advertise emergency and hazardous tree removal, stump grinding and pruning to homeowners and property managers in Puyallup, Tacoma and Pierce County; generate estimate and emergency calls plus quote-form submissions.",
 strat="Search campaign with an emergency call-only ad group running 24/7 and a planned-removal/stump ad group in business hours, both geo-targeted to Pierce County, landing on a page that finally states the service area; add the $150 coupon in ad copy; confirm whether to include land clearing/excavation.",
 mvc="Emergency or large-tree removal estimate call (tracked), with stump-grinding bookings secondary.",
 hook="Your site promises 24-hour emergency service and a certified arborist, but it never says where you work, so a Tacoma homeowner with a tree on the roof after a windstorm can't find you by city. A Pierce County Search campaign with a 24/7 emergency ad group and your $150-off coupon would put (253) 468-1505 in front of that search while the storm is still blowing.",
 ready="Ready to Contact", rreason="Phone verified on the official site; owner named on BBB accredited profile (confirm on call); clear emergency service proposition. Address and service area need confirming for geo-targeting but not for a first call.",
 contact="Kristian Guttu, Owner/Partner (BBB) via (253) 468-1505; email on file is a Facebook-snippet value, unverified.")

D["P-35"] = dict(
 po="Private-office lease Search campaigns for Tulsa with tour requests as the conversion, timed to the November 2026 pre-leasing.",
 hv="Private office suite leases (small from $695/mo, medium $895, large $1,195, with first-3-months promos); conference/training room access for members.",
 kw="Service + city: 'private office space Tulsa', 'executive suites Tulsa', 'office space for rent Tulsa', 'coworking Tulsa', 'midtown Tulsa office space'; near me: 'office space near me'; cost: 'office space Tulsa monthly', 'small office rent Tulsa'; intent: 'furnished office Tulsa', 'month to month office Tulsa', 'schedule office tour'. No volumes asserted.",
 geo="Single building at 6539 E 31st St, Midtown Tulsa; target the Tulsa metro (Tulsa, Broken Arrow, Jenks, Bixby, Owasso) since tenants commute to one site; add 'Midtown' and ZIP 74145 modifiers.",
 conv="Online tour requests (/schedule-a-tour/ two-step form, GTM event already tagged) and calls. Most valuable: a completed tour request for a medium or large suite.",
 camp="Non-brand Search (office space, executive suites, coworking). Brand Search to separate 'Workhub Tulsa' from the Texas WorkHub brand and other 'work hub' searches. Remarketing is valuable (office decisions take weeks). Performance Max with the building location later. Shopping not applicable.",
 lp="Positive: pricing published, tour-request form with event tracking, Bookly plugin present, 24/7 access and amenities listed. Issues verifiable: /about, /about-us, /contact and /contact-us all return 404, so contact details live only in the footer; footer shows info@ but the mailto links to carla@ (inconsistent); /shared-workspaces/ link 404. Recommend fixing the 404s and sending ads to /private-offices/ with the tour form embedded. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /private-offices/, /schedule-a-tour/); Step 6 enrichment (phone verified, address verified, independent operator, pre-leasing for 1 Nov 2026); lp_facts: bookly detected, 'schedule a tour' CTA, 404 on about/contact.",
 conf="High",
 why="Independent 32-suite private office building in Midtown Tulsa with published pricing and a tour-booking funnel already tagged for tracking; office leases are high lifetime value and six suites are being pre-leased for 1 November 2026. Step 5 score 79.",
 prob="Potential problem: filling the six suites coming available on 1 November 2026 and keeping occupancy high in a single building, where each empty medium suite is roughly $895 of lost monthly revenue; the site's broken About/Contact pages may also be losing enquiries. Not verified.",
 adsopp="Advertise furnished private office suites from $695/month with first-three-months promos to professionals, remote workers and small firms in the Tulsa metro; generate tour requests and calls.",
 strat="Launch a Tulsa Search campaign immediately on office-space and executive-suite terms, landing on /private-offices/ with the tour form, timed to the November pre-leasing; Brand Search to disambiguate the name; remarketing to pricing-page visitors; pause or reduce when occupancy is full and restart as leases turn over.",
 mvc="Completed tour request for a private suite (tour_form_submit event), leading to a signed lease.",
 hook="You're pre-leasing six suites for November 1 and you already publish pricing and a tour-request form, which most Tulsa office operators don't. A Search campaign on 'private office space Tulsa' and 'executive suites Tulsa' pointed at your pricing page would fill those tour slots before the month starts, and a small brand campaign would stop the Texas WorkHub brand catching your name searches.",
 ready="Ready to Contact", rreason="Phone and address verified; a named on-site contact (Carla, property manager per a review) and an official mailto exist; clear time-bound opportunity (1 Nov pre-leasing). Confirm which inbox is monitored and who owns marketing decisions.",
 contact="Carla (Property Manager, surname not published) via (918) 345-1390; email carla@workhubtulsa.com (official mailto) or info@workhubtulsa.com (displayed).")

D["P-03"] = dict(
 po="B2B Search campaigns for mobile heavy-truck alignment and suspension repair across the Puget Sound freight corridor, with fleet accounts as the goal.",
 hv="Mobile on-site heavy truck/trailer alignments; complete suspension overhauls; king-pin replacement and axle-eye boring/sleeving; steering knuckle machining.",
 kw="B2B service: 'heavy truck alignment Tacoma', 'semi truck alignment near me', 'mobile truck alignment Seattle', 'trailer alignment Washington'; repair: 'king pin replacement Tacoma', 'truck suspension repair'; fleet: 'fleet alignment service', 'commercial truck alignment Kent'. Low volume, high intent; no volumes asserted.",
 geo="Tacoma base (2323 E Q St, same address as Axle Surgeons of Seattle, suggesting a shared yard or related operators); service area not stated. Target the I-5 corridor Everett-Olympia, Port of Tacoma and Kent Valley pending confirmation.",
 conv="Calls ('call to make an appointment anytime'), email and the contact form. Most valuable: a fleet-account enquiry or a mobile alignment appointment.",
 camp="Non-brand Search only (niche B2B). Call-first ads during business hours. Brand Search minimal. Remarketing to fleet managers who visit the services page. Performance Max and Shopping not applicable.",
 lp="Positive: 22 service links detected (detailed service pages), phone and email published. Issues verifiable: generic 'Contact us' CTA only; no forms on home; social icons link to '#' placeholders; service area absent; About page gives no city. Recommend a mobile-alignment landing page with service area, tap-to-call and a fleet enquiry form. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us, /contact-us, service pages); Step 6 enrichment (phone and email match file, address verified, first names Jordan and Austin as phone-line labels, no owner named); lp_facts: 22 service links, 0 forms, generic CTA, placeholder social links.",
 conf="Medium (service area and decision-maker unconfirmed)",
 why="Second-generation mobile heavy-vehicle alignment specialist with little direct competition, repeat fleet work and detailed service pages; B2B jobs are high value and recurring. Step 5 score 78.5.",
 prob="Potential problem: reaching fleet maintenance managers who search for alignment and suspension specialists only when a truck is pulling or tyres wear unevenly, and converting them into recurring fleet accounts rather than one-off jobs. Not verified.",
 adsopp="Advertise mobile heavy-truck and trailer alignments, suspension overhauls and king-pin work to owner-operators and fleet managers across the Puget Sound corridor; generate appointment calls and fleet-account enquiries.",
 strat="Compact Search campaign on alignment, suspension and king-pin terms geo-targeted to the freight corridor, call extensions during business hours, landing on a mobile-alignment page with a fleet form; remarketing to service-page visitors; coordinate with Axle Surgeons of Seattle if the operators are related (same address).",
 mvc="Fleet-account enquiry or booked mobile alignment appointment (tracked call or form).",
 hook="Your service pages cover everything from Truck Cam alignments to king-pin replacement, but a fleet manager in Kent searching 'mobile truck alignment near me' won't find them. A targeted Search campaign along I-5 and the Port of Tacoma would put your mobile alignment rig in front of that search and turn one-off jobs into fleet accounts; and since you share a yard with Axle Surgeons, the two services could cross-promote in the same ads.",
 ready="Ready to Contact", rreason="Phone and email verified and match the file; two first-name contacts labelled on the site; address verified. Owner not named, so confirm on the call. Service area must be confirmed before launch.",
 contact="Jordan (253) 777-7092 or Austin (253) 777-8811, roles not stated; alignmentsnw@gmail.com.")

D["P-21"] = dict(
 po="Direct-booking Search campaigns for an ocean-view Fort Bragg lodge, defending the brand and targeting Mendocino Coast travel searches from the Bay Area and Sacramento.",
 hv="Direct online bookings for premium rooms (King Whirlpool Fireplace, Honeymoon Suite); Romance and Celebration packages; gift certificates.",
 kw="Destination + property type: 'Fort Bragg ocean view hotel', 'Mendocino coast lodging', 'hotels Fort Bragg CA'; feature: 'ocean view room Fort Bragg', 'whirlpool suite Mendocino', 'romantic getaway Mendocino coast'; brand: 'Ocean View Lodge Fort Bragg' (defend against OTA bidding); event: 'Fort Bragg hotels near Glass Beach', 'Skunk Train hotels'. No volumes asserted.",
 geo="Target feeder markets, not the property location: San Francisco Bay Area, Sacramento, Santa Rosa and Redding, plus travellers already searching in Mendocino County. Single property at 1141 N Main St, Fort Bragg.",
 conv="Online bookings via the ThinkReservations engine (purchase), gift-certificate purchases, calls and contact form. Most valuable: a direct room booking (avoids OTA commission).",
 camp="Brand Search is the first priority (OTAs typically bid on hotel names); non-brand Search on destination and feature terms; Performance Max for travel goals / hotel campaigns if the booking engine supports it; remarketing to booking-engine abandoners; Shopping not applicable.",
 lp="Positive: 'Book now' into a real booking engine, FareHarbor discount link, room pages, policies. Issues verifiable: the site shows (707) 964-1951 while the Prospects tab has a different number, so call tracking must use the site number; no forms on home (booking engine is external); no About 404. Recommend room-specific landing pages for whirlpool/honeymoon suites with direct-booking incentive messaging. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /contact-us, rooms, policies); Step 6 enrichment (email and address verified, phone conflict, no owner/manager found); lp_facts: thinkreservations and fareharbor detected, 'book now' CTA.",
 conf="Medium (operator unknown; phone conflict)",
 why="Independent single-property ocean-view lodge with an online booking engine; direct bookings carry high value and avoid OTA commissions, and destination demand is steady. Step 5 score 78.5.",
 prob="Potential problem: losing bookings and margin to online travel agencies that bid on 'Fort Bragg hotels' and even on the lodge's own name, and filling premium rooms midweek and off-season. Not verified.",
 adsopp="Advertise ocean-view rooms, whirlpool/fireplace suites and romance packages to Bay Area and Sacramento travellers planning a Mendocino Coast trip; generate direct bookings through the existing booking engine and gift-certificate sales.",
 strat="Start with Brand Search to recapture name searches from OTAs, then a destination Search campaign targeted at feeder markets with room-feature ad groups, landing on room pages; remarketing to booking abandoners; test hotel/Performance Max for travel after conversion tracking is in place on the booking engine.",
 mvc="Direct room booking completed in the ThinkReservations engine (purchase conversion).",
 hook="Every room at Ocean View Lodge faces the Pacific and guests can book directly on your site, but when a San Francisco couple searches 'Fort Bragg ocean view hotel' the results are booking sites that take a commission on your room. A campaign that defends your name and targets Bay Area travellers with your whirlpool and honeymoon suites would move those bookings back to your own engine.",
 ready="Contact After Research", rreason="Email and address verified, but the phone on file conflicts with the site and no owner, manager or operating entity could be found. Call the site number to identify the decision-maker before pitching.",
 contact="Front desk (707) 964-1951 (site) or info@oceanviewlodging.com; ask for the owner or general manager. The on-file number (707) 964-7366 is unverified.")

D["P-36"] = dict(
 po="Medicare and small-business group-health quote campaigns for Sonoma, Napa and Marin, timed to Medicare Annual Enrollment (15 Oct to 7 Dec) and Covered California open enrollment.",
 hv="Medicare plan guidance and enrollment; small-business group health (1-100 employees); Covered California individual plans; life, long-term care and annuities.",
 kw="Service + city: 'Medicare agent Sonoma', 'Medicare advisor Napa', 'health insurance broker Marin County', 'small business health insurance Sonoma County'; near me: 'Medicare insurance agent near me'; seasonal: 'Medicare open enrollment help', 'Covered California enrollment Sonoma'; intent: 'compare Medicare supplement plans', 'independent insurance agent Sonoma'. No volumes asserted.",
 geo="Sonoma Valley office; service area verified as Marin, Napa and Sonoma counties (plus other states, lower priority). Target the three counties with office location extensions; Sonoma Valley radius for walk-in intent.",
 conv="'Get a Quote' form, calls and email. Most valuable: a Medicare or group-health consultation request (multi-year client value).",
 camp="Non-brand Search on Medicare and group-health terms (expensive but very high lifetime value; Medicare advertising must follow CMS marketing rules). Brand Search under 'Zellers Group' and 'Zellers Insurance'. Remarketing during enrollment windows. Performance Max optional. Shopping not applicable.",
 lp="Positive: 'Get a quote' CTA, team page with named licensed agents, legal name and privacy notice present. Issues verifiable: no forms on home (quote CTA leads to the contact page); minor hours inconsistency between footer and contact section; no online scheduling. Recommend a Medicare landing page with a short quote/consult form and the agents' photos, compliant with CMS disclaimer rules. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us, /contact-us, privacy notice PDF); Step 6 enrichment (phone, email, address verified; President Dean Zellers named; legal name confirmed); lp_facts: 'get a quote' CTA, 3 service links, 0 forms on home.",
 conf="High",
 why="Independent insurance agency with five named licensed agents, a Medicare specialty and small-group health, serving three affluent North Bay counties; policies carry multi-year commission value and the president is reachable. Step 5 score 77.",
 prob="Potential problem: generating qualified Medicare and group-health consultations during the short enrollment windows, when national carriers and lead aggregators dominate the search results and the agency's trading name recently changed (zellersins.com now redirects to zellersgroup.com). Not verified.",
 adsopp="Advertise Medicare plan guidance to people turning 65 and current beneficiaries in Sonoma, Napa and Marin during Annual Enrollment, and group health to small employers year-round; generate quote-form submissions and consultation calls.",
 strat="A Medicare Search campaign scheduled around the 15 Oct to 7 Dec Annual Enrollment window with CMS-compliant copy and a dedicated landing page; a year-round small-group health campaign; Brand Search under both names; remarketing to quote-page visitors. Launch the Medicare campaign immediately given the window has just opened.",
 mvc="Medicare or group-health consultation request (quote form or tracked call) leading to an enrolled policy.",
 hook="Medicare Annual Enrollment opened on 15 October and your team has four agents who specialise in exactly that, but someone in Napa searching 'Medicare agent near me' this week sees national carriers and lead-gen sites, not Zellers Group. A compliant Medicare Search campaign across Sonoma, Napa and Marin, landing on a page with your agents and a short consultation form, would fill the next seven weeks with local enrollment appointments.",
 ready="Ready to Contact", rreason="Phone, email and address verified on the official site; President Dean Zellers named on the About page; time-sensitive opportunity (Annual Enrollment underway).",
 contact="Dean Zellers, President / Independent Agent via (707) 996-5282 or dz@zellersins.com.")

D["P-19"] = dict(
 po="Subscription bin-cleaning Search campaigns for Renton, Seattle, Bellevue and King County, with an HOA and commercial dumpster-sanitising B2B campaign.",
 hv="Recurring residential bin-cleaning subscriptions; HOA and apartment-community contracts; commercial dumpster sanitising (restaurants, school districts, facilities).",
 kw="Service + city: 'trash can cleaning Renton', 'garbage bin cleaning Seattle', 'bin cleaning service Bellevue', 'dumpster cleaning King County'; near me: 'trash bin cleaning near me'; intent: 'curbside bin cleaning subscription', 'HOA trash can cleaning', 'restaurant dumpster cleaning service', 'eco friendly bin cleaning'. No volumes asserted.",
 geo="Service area verified: Renton, Seattle, Bellevue and King County; mobile service with a Renton mailing address. Target King County with a focus on single-family suburbs (Renton, Kent, Bellevue, Issaquah) for residential and commercial districts for dumpster work.",
 conv="Online scheduling through the jobatory portal (booking), calls, contact form. Most valuable: a recurring residential subscription sign-up or a commercial/HOA contract enquiry.",
 camp="Non-brand Search (residential subscription and commercial ad groups). Brand Search modest. Performance Max with the service area could work for an educational category. Remarketing is useful because bin cleaning is a new-to-market service many searchers consider twice. Shopping not applicable.",
 lp="Positive: 'schedule' CTA into a real online scheduler, customer portal, newsletter, verified official social links. Issues verifiable: no street address (PO Box only) and conflicting addresses across LinkedIn/BBB, which weakens location extensions; no forms on home (scheduler is external); home HTML ~218 KB. Recommend a residential-subscription landing page with pricing and the scheduler embedded, and a separate HOA/commercial page. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us, /contact-us); Step 6 enrichment (phone verified, two official emails, owner per BBB and KING 5 article, address conflict); lp_facts: jobatory detected, 'schedule' CTA.",
 conf="High",
 why="Locally owned recurring-revenue bin-sanitising service with online scheduling, serving the Seattle metro's affluent suburbs and commercial districts; each residential sign-up is a subscription and each HOA or commercial account is a contract. Step 5 score 75.5.",
 prob="Potential problem: building subscriber density route by route (the economics of bin cleaning depend on many customers per neighbourhood) and winning HOA and commercial contracts in a category many homeowners do not yet know exists. Not verified.",
 adsopp="Advertise curbside bin-cleaning subscriptions to homeowners in Renton, Bellevue, Kent and Issaquah, and dumpster sanitising to restaurants, property managers and school districts across King County; generate online schedule bookings and contract enquiries.",
 strat="Search campaign with a residential subscription ad group (neighbourhood-targeted to build route density) and a commercial/HOA ad group, both landing on pages with the scheduler; remarketing to explain the service to first-time visitors; Performance Max once conversions are tracked in jobatory.",
 mvc="Recurring residential subscription booked through the scheduler, or an HOA/commercial contract enquiry.",
 hook="Bin cleaning works when you own a neighbourhood, and your scheduler already lets a Renton or Bellevue homeowner sign up in a minute, but nobody searching 'trash can cleaning near me' sees Northwest Eco Clean today. A Search campaign aimed at the suburbs you already drive, plus an HOA and restaurant ad group, would stack subscriptions onto existing routes and bring in the contracts that make each route pay.",
 ready="Ready to Contact", rreason="Phone and two emails verified on the official site; owner named by BBB (confirm on call); online scheduling in place. Address conflict is a housekeeping item.",
 contact="Martez Johnson, Owner/Member (BBB) via (206) 825-6998 or customersupport@northwestecoclean.com.")

D["P-16"] = dict(
 po="Local Search and Maps campaigns for dog grooming in La Jolla and coastal San Diego, with the daycare-plus-grooming combo as the upsell.",
 hv="Full Groom and Spa Service; daycare plus grooming combo (Doggie Beach Lounge); Breath Savers non-anesthesia dental; deshedding and spa add-ons.",
 kw="Service + area: 'dog groomer La Jolla', 'dog grooming Pacific Beach / UTC', 'pet grooming near me', 'mobile vs salon grooming La Jolla'; appointment: 'book dog grooming appointment', 'same week dog grooming'; niche: 'non anesthesia dog teeth cleaning San Diego', 'doodle groomer La Jolla', 'dog daycare and grooming La Jolla'. No volumes asserted.",
 geo="Single salon at 7709 Fay Ave, La Jolla; radius 5-7 miles (La Jolla, Pacific Beach, UTC, Bird Rock, Del Mar edge). Service area not stated on site; grooming is hyperlocal.",
 conv="Appointment request form (followed up by phone within 24 hours) and calls; daycare booked via separate portal. Most valuable: a new-client full-groom appointment (repeat every 4-8 weeks).",
 camp="Non-brand Search (grooming, dental, daycare combo). Brand Search cheap and useful ('LJ Grooming' variants). Local campaign / Performance Max with store location for Maps. Remarketing minor. Shopping not applicable.",
 lp="Positive: 'book an appointment' and 'call now' CTAs, team page with founder, services detailed. Issues verifiable: no About page (404); no online self-booking for grooming (request form only, followed by a call), which adds friction versus salons with instant booking; no forms on home; home HTML ~278 KB. Recommend an instant-booking option or at least a request form on a grooming landing page with price ranges. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /contact-us/, /meet-the-team/); Step 6 enrichment (phone, email, address verified; founder Garrett Larson; second phone on Yelp unverified); lp_facts: appointment and call CTAs, 0 forms on home, 404 about.",
 conf="High",
 why="Family-owned grooming salon in an affluent coastal neighbourhood with repeat-visit economics, a daycare sister brand for upsell and a named founder. Step 5 score 75.",
 prob="Potential problem: keeping groomer chairs full with new clients in a capacity-limited single location and converting one-off groomers into recurring 4-8 week clients, while mobile groomers and chains bid on 'dog groomer near me'. Not verified.",
 adsopp="Advertise full-groom and spa services, non-anesthesia dental cleaning and the daycare-plus-grooming combo to dog owners within a few miles of Fay Avenue; generate appointment requests and calls.",
 strat="A tight-radius Search campaign on grooming and dental terms with call extensions and a Maps-focused local campaign, landing on a grooming page with the appointment request form; Brand Search; budget scaled to chair capacity (pause when booked out).",
 mvc="New-client full-groom appointment booked (request form or tracked call), valued as a recurring client.",
 hook="Garrett built La Jolla Grooming into a family salon with a dental service most groomers don't offer, and the Doggie Beach Lounge gives you a daycare-plus-groom combo nobody nearby matches. But a dog owner in Bird Rock searching 'dog groomer near me' still sees the chains first. A small-radius Search and Maps campaign around Fay Avenue would keep every chair booked with clients who come back every six weeks.",
 ready="Ready to Contact", rreason="Phone, email and address verified on the official site; founder and groomer named on the team page.",
 contact="Garrett Larson, Founder and Groomer via (858) 246-6235 or info@ljgrooming.com.")

D["P-09"] = dict(
 po="Pre-need (pre-planning) and cremation-options Search campaigns for Catholic families in the Tulsa metro, with monuments and memorials as a second theme.",
 hv="Pre-need burial and cremation planning (the diocese cited a strengthening pre-need sales programme and new memorial gardens); Catholic cremation options; monuments and markers.",
 kw="Service + city: 'Catholic cemetery Tulsa', 'cemetery plots Tulsa', 'pre-plan burial Tulsa', 'cremation niche Tulsa'; near me: 'cemetery near me'; intent: 'how to pre plan a funeral', 'buy burial plot', 'Catholic cremation rules', 'headstone Tulsa'; brand: 'Calvary Cemetery Tulsa' (disambiguate from Calvary cemeteries in other cities). No volumes asserted.",
 geo="Tulsa metro (Tulsa, Broken Arrow, Jenks, Bixby, Owasso, Sand Springs) with the single location at 9101 S Harvard Ave; Catholic-affinity audiences where available.",
 conv="Calls and the contact form (no online booking). Most valuable: a pre-need planning appointment request.",
 camp="Non-brand Search on pre-need and cremation terms (sensitive category; copy must be respectful and compliant). Brand Search with 'Tulsa' qualifier to avoid other Calvary cemeteries. Remarketing modest and must respect sensitive-category rules. Performance Max and Shopping not appropriate.",
 lp="Positive: 'schedule' and 'contact us' CTAs, planning guides, memorialisation guidebook, office hours and address. Issues verifiable: no About page (404); team/staff menu link is a placeholder (href '#'); no forms on home; no online appointment booking for pre-planning. Recommend a pre-planning landing page with a consultation request form and the guides as downloads. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /contact-us/, /planning/); Step 6 enrichment (phone, email, address verified; executive director retired Oct 2025, successor not found; diocesan governance Needs Verification); lp_facts: 0 forms, 404 about, 'schedule' CTA.",
 conf="Medium (leadership in transition)",
 why="Diocesan cemetery with an active pre-need sales programme, new memorial gardens and cremation facilities; pre-need sales are high-value, planned purchases with steady local search demand. Step 5 score 71.",
 prob="Potential problem: growing pre-need sales and awareness of Catholic cremation options among Tulsa families who search online before calling, while the executive director role is in transition and the site has no appointment path. Not verified.",
 adsopp="Advertise pre-planning consultations, Catholic cremation options and monuments to Catholic families and adults 55+ in the Tulsa metro; generate planning-appointment calls and form requests.",
 strat="A respectful Search campaign on pre-need, plot and cremation terms with a 'Tulsa' brand campaign, landing on a pre-planning page with a consultation form and downloadable guides; business-hours call extensions; no remarketing until approved by the organisation. Engage after the new executive director is identified.",
 mvc="Pre-need planning appointment request (tracked call or form).",
 hook="The diocese has said it wants to strengthen pre-need sales and has opened new memorial gardens, yet a Tulsa family searching 'pre-plan burial Tulsa' or 'Catholic cremation Tulsa' finds no path to Calvary's planning office. A Search campaign on pre-need and cremation terms, landing on your planning guides with a consultation request form, would bring those families to you before they call a commercial cemetery.",
 ready="Contact After Research", rreason="Phone, email and address verified, but the executive director retired in October 2025 and the successor is unknown; decisions likely involve the Catholic Cemetery Association board. Identify the current director before pitching.",
 contact="Cemetery office (918) 299-7348 or info@calvarycemetery.org; ask for the executive director.")

D["P-11"] = dict(
 po="Residential and commercial window-cleaning Search campaigns for east Pierce County, plus a seasonal Christmas-light-hanging campaign (October-December).",
 hv="Recurring commercial window washing contracts; Christmas light hanging (seasonal, higher ticket); residential window washing via the 'Window Care' maintenance programme; hard-water stain removal.",
 kw="Service + city: 'window cleaning Bonney Lake', 'window washing Puyallup', 'commercial window cleaning Tacoma', 'window cleaners Lake Tapps'; near me: 'window cleaning near me'; quote: 'free window cleaning quote'; seasonal: 'Christmas light installation Puyallup', 'holiday light hanging service near me'; niche: 'hard water stain removal windows'. No volumes asserted.",
 geo="Base Bonney Lake / Lake Tapps (directories); jobs recorded in Gig Harbor, Tacoma, Auburn and Bonney Lake. Radius 15-20 miles around Bonney Lake covering Puyallup, Sumner, Auburn, Tacoma; confirm on call.",
 conv="Housecall Pro online booking ('Get a Free Quote') and calls. Most valuable: a commercial recurring contract or a Christmas-light install (seasonal), with residential Window Care sign-ups as the volume play.",
 camp="Non-brand Search (residential, commercial, seasonal lights). Brand Search cheap. Performance Max optional later. Remarketing for quote abandoners. Shopping not applicable.",
 lp="Positive: Housecall Pro booking embedded, 'get a free quote' CTA, free estimates, Window Care programme described. Issues verifiable: no address on the site; the on-file business name is a typo of the real trading name (Clean & Clear by Cliff), so brand terms must use the correct name; no forms on home (booking is external). Recommend a Christmas-lights landing page (seasonal) and a commercial page. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about-us/, /contact/); Step 6 enrichment (phone and email verified, owner via LinkedIn snippet, base per Facebook/Yelp); lp_facts: housecallpro detected, 'get a free quote' CTA.",
 conf="Medium (service area and owner surname unverified)",
 why="Family-run window-cleaning service with 32 years in business, online booking through Housecall Pro and recurring commercial and residential programmes; the owner is the brand. Step 5 score 71.",
 prob="Potential problem: filling the autumn Christmas-light calendar and growing recurring commercial contracts beyond referrals, in a service where searchers book whoever appears with an instant quote. Not verified.",
 adsopp="Advertise window washing (residential Window Care programme and commercial contracts) and, from October to December, Christmas light hanging to homeowners and businesses in Bonney Lake, Puyallup, Sumner and Auburn; generate Housecall Pro bookings and quote calls.",
 strat="Launch the seasonal Christmas-lights Search campaign immediately (October), then a year-round window-cleaning campaign with residential and commercial ad groups, both landing on pages with the Housecall Pro booking embedded; Brand Search under the correct trading name.",
 mvc="Christmas-light install booked (seasonal) or a commercial recurring contract; residential Window Care sign-up as volume conversion.",
 hook="Cliff, you already take bookings through Housecall Pro and you hang Christmas lights every season, which is the highest-ticket job on your menu and the one Puyallup homeowners are searching for right now. A Search campaign on 'Christmas light installation near me' for the next ten weeks, landing straight on your booking page, would fill the ladder schedule, and a year-round window-cleaning campaign would keep the Window Care programme growing after the holidays.",
 ready="Ready to Contact", rreason="Phone and email verified on the official site; owner is the named brand ('by Cliff'); online booking in place. Surname and base address rest on directories (confirm on call).",
 contact="Cliff (McIntosh per LinkedIn snippet, unverified), Owner via (253) 350-0457 or cliffmc598@gmail.com.")

D["P-33"] = dict(
 po="B2B Search campaigns for specialty printing (engraving, letterpress, foil, wine labels) across the North Bay and Bay Area, targeting law firms, financial firms and wineries.",
 hv="Engraved corporate stationery; wine labels; foil-stamped, letterpress and embossed invitations and announcements; political campaign materials.",
 kw="Specialty + region: 'engraved business cards Bay Area', 'letterpress printing Napa', 'wine label printing Napa Valley', 'foil stamping printer Bay Area', 'commercial printer Vallejo'; B2B: 'law firm stationery engraving', 'engraved letterhead'; event: 'letterpress wedding invitations Sonoma', 'campaign printing Solano County'. No volumes asserted.",
 geo="Vallejo (Solano County) base; service area 'Bay Area and Napa Valley' verified on site. Target Napa and Sonoma wine country for labels, San Francisco/Oakland for engraved corporate stationery, Solano County for local commercial print.",
 conv="Calls and email (no contact form, no online ordering portal visible). Most valuable: a quote request for engraved stationery or a wine-label run (repeat B2B accounts).",
 camp="Non-brand Search on specialty terms (lower competition than generic 'printing'). Brand Search modest ('Wheeler-Sonoma'). Remarketing to specialty-page visitors. Shopping possible later if an online ordering catalogue is launched (About page mentions online ordering but none is visible). Performance Max later.",
 lp="Issues verifiable: no contact form anywhere (phone and email only), no online quote or ordering path despite the About page claiming online ordering was added; generic 'Contact us' CTA; two service links detected. Positive: detailed services and industries pages, address and hours. Recommend quote-request forms on specialty pages (engraving, wine labels) before sending paid traffic. Mobile rendering not tested.",
 ev="Website text and HTML 8 Oct 2026 (home, /about/, /services/, /contact-us/); Step 6 enrichment (phone, email, address verified; owner Baird Conner on About page); lp_facts: 0 forms, generic CTA, 2 service links.",
 conf="High",
 why="Historic (1940) specialty printer with engraving, letterpress and foil capabilities few competitors have, serving law firms, financial institutions and wineries; B2B orders repeat and the owner is named on the site. Step 5 score 70.",
 prob="Potential problem: generic online printers taking commodity work, leaving the shop dependent on legacy accounts; the high-margin specialty work (engraving, wine labels) is what searchers would pay for but the site offers no way to request a quote online. Not verified.",
 adsopp="Advertise engraved stationery, letterpress and foil work, and wine-label printing to law firms, financial firms, wineries and event planners across the Bay Area and Napa Valley; generate quote calls and emails (form once added).",
 strat="Add quote-request forms to the engraving and wine-label pages first, then launch a specialty Search campaign with ad groups for engraving, letterpress/invitations and wine labels, geo-targeted to the Bay Area and Napa/Sonoma; Brand Search; remarketing to specialty-page visitors.",
 mvc="Quote request for an engraving or wine-label job (tracked call, email or new form).",
 hook="Wheeler-Sonoma still runs engraving, letterpress and foil in-house, which almost no online printer can offer a Napa winery or a San Francisco law firm. But those buyers search 'engraved business cards Bay Area' and 'wine label printer Napa' and never see you, and when they reach your site there's no way to request a quote. A specialty Search campaign plus a simple quote form would put 85 years of craft in front of the exact buyers who pay for it.",
 ready="Ready to Contact", rreason="Phone, email and address verified on the official site; owner Baird Conner named on the About page and listed as President by the Vallejo Chamber.",
 contact="Baird Conner, Owner/President via (707) 643-6383 or customerservice@wheeler-sonoma.com.")

D["P-13"] = dict(
 po="None assessable: the website is not live and no business facts could be verified.",
 hv="Unknown (name suggests dental implants).", kw="Not assessed - no verified services or location.", geo="Unknown - no location found.",
 conv="Unknown.", camp="Not assessed.", lp="Site returns 403 at root and 404 on subpages (8 Oct 2026); there is no landing page.",
 ev="Step 6 enrichment: all fields Not Found; no link to Cunning Dental Group found.", conf="Low",
 why="Only the name suggests a dental implant practice, which would be a strong category; nothing else is verified.",
 prob="Potential problem: unknown. Cannot be stated without a live site or any business record.",
 adsopp="Cannot be defined until the business, location and services are confirmed.", strat="Verify whether this is a live business or a dead microsite of Cunning Dental Group before any further work.",
 mvc="Unknown.", hook="Not written - no verified facts to personalise.",
 ready="Missing Critical Information", rreason="No phone, email, address, services or decision-maker found; website not live; relationship to P-12 unverifiable.",
 contact="None. Ask the Around29 account team how this record entered the Prospects list.")

H7 = ["record_id", "business_name_std", "tier", "total_score", "primary_opportunity", "high_value_service", "keyword_themes", "geographic_opportunity",
      "conversion_opportunity", "campaign_opportunity", "landing_page_opportunity", "landing_page_facts_verified", "evidence", "confidence"]
H8 = ["record_id", "business_name_std", "tier", "total_score", "why_this_business_is_a_prospect", "likely_business_problem", "google_ads_opportunity",
      "recommended_strategy", "most_valuable_conversion", "sales_hook", "outreach_readiness", "readiness_reason", "contact_to_use"]


def tier_f(i, tabrow):
    return ('=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$O$46,15,FALSE),"Unknown")' % tabrow,
            '=IFERROR(VLOOKUP($A%d,GOOGLE_ADS_OPPORTUNITY_SCORE!$A$2:$N$46,14,FALSE),"Unknown")' % tabrow)


rows7, rows8, csv7, csv8 = [], [], [], []
SC = {r["record_id"]: (r["tier"], r["total_score"]) for r in csv.DictReader(open(os.path.join(PROJ, "google_ads_opportunity_score.csv"), encoding="utf-8"))}
for i, (rid, name) in enumerate(ORDER, start=2):
    d = D[rid]
    t, s = tier_f(i, i)
    r7 = [rid, name, t, s, d["po"], d["hv"], d["kw"], d["geo"], d["conv"], d["camp"], d["lp"], lpfacts(rid), d["ev"], d["conf"]]
    r8 = [rid, name, t, s, d["why"], d["prob"], d["adsopp"], d["strat"], d["mvc"], d["hook"], d["ready"], d["rreason"], d["contact"]]
    rows7.append(r7); rows8.append(r8)
    csv7.append([rid, name, SC[rid][0], SC[rid][1]] + r7[4:])
    csv8.append([rid, name, SC[rid][0], SC[rid][1]] + r8[4:])

json.dump(rows7, open(os.path.join(HERE, "step7_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump(rows8, open(os.path.join(HERE, "step8_rows.json"), "w", encoding="utf-8"), ensure_ascii=False)
with open(os.path.join(PROJ, "google_ads_market_opportunity.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(H7); w.writerows(csv7)
with open(os.path.join(PROJ, "sales_pitch_intelligence.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(H8); w.writerows(csv8)
from collections import Counter
print(len(rows7), len(rows8), Counter(r[10] for r in rows8), Counter(r[13] for r in rows7))
print("max cell", max(len(str(c)) for r in rows7 + rows8 for c in r))
