"""Step 3: business and industry classification for the 45 cleaned records.

Evidence tiers: Verified = the business's own website text (title, meta description, page text) fetched 8 Oct 2026;
Inferred = business name, domain or phone area code only; Unknown = no usable evidence.
"""
import json, csv, os
from collections import Counter

SP = r"C:\Users\Aroun\AppData\Local\Temp\claude\C--Users-Aroun-Desktop-Projects-Google-Ads-Prospects\e134b08f-71c9-4529-bc4f-df5bd3dad2a6\scratchpad\scripts"
PROJ = r"C:\Users\Aroun\Desktop\Projects\Google Ads Prospects"

HEADER = ["record_id", "business_name_std", "primary_industry", "industry_evidence", "secondary_industry",
          "business_model", "model_evidence", "customer_type", "customer_acquisition_model", "acquisition_evidence",
          "service_type", "geographic_scope", "geographic_basis", "classification_confidence", "evidence_source", "classification_notes"]

INF = "Inferred (from business type)"
R = [
 ("P-01", "AA Roofing and Decking", "Home Services", "Verified (website)", "Construction",
  "Local service; Lead generation; High-ticket service; Project-based; B2C", "Verified (website)", "B2C (homeowners); some B2B",
  "Local search; Google/Search; Referral", INF, "Roofing, weatherproofing, custom decks, patio covers, pergolas",
  "Local", "Verified: site states Auburn, Washington", "High",
  "Title 'Weatherproof Roofing Services'; description: licensed, bonded and insured roofing contractor in Auburn, Washington", "None"),
 ("P-02", "Affordable Junk Removal", "Home Services", "Verified (website)", "Logistics (hauling)",
  "Local service; Lead generation; B2C; B2B", "Verified (website)", "B2C and B2B (homes and businesses)",
  "Google/Search; Local search; Referral; Repeat customers (business accounts)", INF, "Same-day junk removal, pickup and hauling",
  "Regional", "Verified: based in Sacramento, CA; serves Rocklin and surrounding areas", "High",
  "Title 'Same-Day Junk Pickup & Hauling'; description covers homes and businesses; address Sacramento, CA 95826", "None"),
 ("P-03", "Alignments Northwest LLC", "Automotive", "Verified (website)", "B2B Services",
  "Local service; Appointment-based; B2B; Recurring service (fleet maintenance)", "Mixed: service verified, recurring inferred", "B2B (fleet operators and truck owners)",
  "Google/Search; Referral; Repeat customers", INF, "Heavy-vehicle (truck) wheel alignment",
  "Local", "Verified: address Tacoma, WA 98421", "High",
  "Title 'Heavy Vehicle Wheel Alignments'; description: second-generation alignment specialist with Truck Cam heavy-vehicle equipment", "Shares the 253-777 phone exchange with P-07 (related-entity flag)"),
 ("P-04", "American Tree Excavation", "Home Services", "Verified (website)", "Construction (excavation, land clearing)",
  "Local service; Lead generation; High-ticket service; Project-based; B2C", "Verified (website)", "B2C (homeowners); some B2B",
  "Local search; Google/Search; Referral", INF, "Tree removal and excavation",
  "Local", "Inferred: 253 area code; site does not state a city", "Medium",
  "Title 'Tree Removal and Excavation Services'; description: crew creates safe outdoor spaces", "Location not stated on the site"),
 ("P-05", "Around Cricket", "Retail", "Verified (website)", "Ecommerce",
  "Retail; Ecommerce; B2C", "Verified: cart and checkout pages on site", "B2C (cricketers)",
  "Ecommerce; Social media; Walk-in; Google/Search", "Partly verified (online store present)", "Cricket bats, equipment and accessories",
  "Local (India)", "Verified: title names Hyderabad; online reach unknown", "High",
  "Title 'Hyderabad's Ultimate Cricket Store'; description: cricket gear by cricketers, for cricketers; cart/checkout present", "Outside the US market"),
 ("P-06", "ASL Camguard", "Automotive", "Verified (website)", "Manufacturing; Ecommerce",
  "Manufacturer; Ecommerce; B2C; B2B (dealers, distributors)", "Mixed: product and online store verified, distribution inferred", "B2C and B2B",
  "Ecommerce; Google/Search; Partnerships (dealers, distributors); Repeat customers", "Partly verified (add-to-cart present)", "Engine oil supplements (CamGuard)",
  "National", "Inferred: toll-free number and product brand; site names Tulsa, OK as base", "Medium",
  "Title 'Advanced Engine Protection | CamGuard'; description: oil supplements in Tulsa, OK; add-to-cart buttons on site", "Product brand rather than a local service"),
 ("P-07", "Axle Surgeons of Seattle", "Automotive", "Verified (website)", "B2B Services",
  "Local service; Emergency service (24/7 mobile road service); B2B; Lead generation", "Verified (website)", "B2B (trucking companies, owner-operators)",
  "Google/Search; Local search; Referral; Repeat customers", INF, "Mobile truck and trailer axle repair, roadside service",
  "Regional", "Verified: Seattle and Tacoma named; '24/7 mobile service area' section", "High",
  "Title 'Truck and Trailer Services | Seattle'; description: fast road service", "Shares the 253-777 phone exchange with P-03"),
 ("P-08", "Brothers Micro Market", "Unknown", "Unknown (site offline)", "Unknown",
  "Unknown", "Unknown", "Unknown",
  "Unknown", "Unknown", "Unknown (name suggests a self-serve micro market or vending operation)",
  "Unknown", "Unknown: 818 area code hint only", "Low",
  "Site returned 503 'Under Maintenance' on 8 Oct 2026; no description available", "Re-classify when the site is back; email domain brosdist.com differs from website"),
 ("P-09", "Calvary Cemetery", "Other (cemetery and funeral services)", "Verified (website)", "None",
  "Local service; High-ticket service; Consultation-based (pre-need plans); B2C", "Verified: burial, cremation and plans on site", "B2C (families); religious community",
  "Referral (parishes, funeral homes); Local search; Google/Search; Partnerships", INF, "Catholic cemetery: burial grounds, cremation, memorialization",
  "Local", "Verified: Tulsa, OK; 9101 S. Harvard Ave", "High",
  "Title 'Tulsa's Sacred Burial Grounds'; description: burial grounds and cremation services for all faiths", "Probably a religious nonprofit (.org); not verified"),
 ("P-10", "Chili On The Green", "Other (community event / fundraiser)", "Verified (website)", "Restaurant/Food (chili cook-off)",
  "Other (annual ticketed event); B2C; nonprofit-run", "Verified (website)", "B2C (attendees); B2B (sponsors)",
  "Social media; Partnerships (Kiwanis, sponsors); Referral; Local search", INF, "State chili championship event presented by Kiwanis Club of Tulsa",
  "Regional", "Verified: 'State of Oklahoma Chili Championship' held in Tulsa", "High",
  "Title 'The Official State of Oklahoma Chili Championship'; description: presented by The Kiwanis Club of Tulsa, sanctioned by the International Chili Society", "Verified relationship with P-15 Kiwanis Club of Tulsa"),
 ("P-11", "Clean and Clean by Cliff", "Home Services", "Verified (website)", "B2B Services (commercial cleaning)",
  "Local service; Recurring service; Lead generation; B2C; B2B", "Verified: residential and commercial stated", "B2C and B2B",
  "Local search; Google/Search; Referral; Repeat customers", INF, "Residential and commercial window cleaning",
  "Local", "Inferred: 253 area code; site does not state a city", "Medium",
  "Title 'Commercial and Residential Window Cleaning | Clean & Clear By Cliff'", "Site brand is 'Clean & Clear By Cliff' (name mismatch flag)"),
 ("P-12", "Cunning Dental Group", "Dental", "Verified (website)", "Healthcare",
  "Appointment-based; Local service; High-ticket service (implants, sedation); Emergency service (24/7 emergency dentistry); Multi-location (Needs Verification); B2C", "Mixed: appointment and emergency verified, multi-location needs verification", "B2C (patients)",
  "Google/Search; Local search; Referral; Repeat customers; Partnerships (insurance networks)", "Partly verified (online appointment scheduling present)", "General, cosmetic, sedation and implant dentistry; 24/7 emergency dentistry",
  "Regional", "Verified: Montclair, CA plus surrounding Southern California (Chino Hills, Covina)", "High",
  "Title 'General & Cosmetic Dentist Near You in Montclair, CA'; description: 56 years of full-service dental care, 24/7 emergency dentistry", "Possible duplicate pair with P-13"),
 ("P-13", "Cunningsmiles Implant Experts", "Dental", "Inferred (name)", "Healthcare",
  "Appointment-based; High-ticket service (implants)", "Inferred (name)", "B2C (patients)",
  "Google/Search", "Inferred (name)", "Dental implants (from name)",
  "Unknown", "Unknown: site returns 403; probably the same market as P-12 (Needs Verification)", "Low",
  "Site returned 403 Forbidden on 8 Oct 2026; classification rests on the name and the relationship to P-12", "Possible duplicate or sub-brand of P-12; website status Changes in Progress"),
 ("P-14", "DBSA OK", "Healthcare", "Verified (website)", "Other (nonprofit organization)",
  "Other (nonprofit: donations, membership, free support services); B2C", "Verified: donate, nonprofit and members on site", "B2C (individuals and families); donors and members",
  "Referral (clinicians); Partnerships (treatment providers); Google/Search; Social media", "Partly verified (donation page present)", "Peer support, wellness resources and treatment connections for behavioral health",
  "Regional", "Verified: statewide ('Oklahomans'); Oklahoma City address", "High",
  "Title 'Support & Wellness Services: Depression and Bipolar Alliance, OK'; description: primary source of support for Oklahomans", "Nonprofit"),
 ("P-15", "Kiwanis Club of Tulsa", "Other (nonprofit service club)", "Verified (website)", "None",
  "Other (membership organization; nonprofit); B2C", "Verified: membership pages", "Members, donors and sponsors",
  "Referral; Partnerships; Social media; Local search", INF, "Community service projects, leadership development, membership",
  "Local", "Verified: Tulsa", "High",
  "Title 'Kiwanis Club of Tulsa: Serving Children & Communities'; description: service projects and leadership development", "Presents Chili On The Green (P-10)"),
 ("P-16", "La Jolla Grooming Co", "Other (pet services)", "Verified (website)", "None",
  "Local service; Appointment-based; Recurring service; B2C", "Verified: 'book an appointment' on site", "B2C (dog owners)",
  "Local search; Google/Search; Referral; Repeat customers; Walk-in", "Partly verified (online booking present)", "Dog grooming",
  "Local", "Verified: La Jolla / Bird Rock, San Diego", "High",
  "Title 'Dog Grooming Shop | La Jolla | Dog Groomers | Bird Rock'; description: stress-free grooming near The Cottage in La Jolla", "No pet-services class in the category list; filed under Other"),
 ("P-17", "Lab Rescue", "Other (animal rescue nonprofit)", "Verified (website)", "None",
  "Other (nonprofit: adoption fees, donations, volunteers); B2C", "Verified: volunteer and donate pages", "Adopters, fosters and donors (B2C)",
  "Social media; Referral; Partnerships (shelters, vets); Google/Search", "Partly verified (donation and volunteer pages)", "Labrador Retriever rescue and adoption",
  "Regional", "Verified: 'Oklahoma' in title; Broken Arrow address; 'based in Tulsa'", "High",
  "Title 'Lab Rescue Inc. | Oklahoma'; description: eliminating unnecessary euthanasia of Labrador Retrievers", "Nonprofit"),
 ("P-18", "Next Level Prospect", "Education", "Verified (website)", "Other (nonprofit organization)",
  "Consultation-based; Other (nonprofit, donations); B2C", "Verified: nonprofit, 501(c)(3) and donations on site", "B2C (student-athletes and families)",
  "Referral (coaches); Social media; Partnerships (schools, clubs); Google/Search", "Partly verified (donation page)", "Student-athlete college recruiting assessment and guidance",
  "National", "Verified wording: 'Colleges nationwide'; base location not stated (626 area code hint)", "Medium",
  "Title 'Next Level Prospects | Student Athlete | Nonprofit organization'; description: bridging student-athletes and colleges nationwide", "Website status Changes in Progress"),
 ("P-19", "NorthWest Eco Clean", "Home Services", "Verified (website)", "B2B Services (commercial dumpster cleaning)",
  "Local service; Recurring service; Subscription (service plans, inferred); B2C; B2B", "Mixed: residential/commercial verified, subscription inferred", "B2C and B2B",
  "Local search; Google/Search; Social media (Meta pixel on site); Repeat customers", "Partly verified (Meta pixel indicates social advertising)", "Trash bin, dumpster and odor cleaning",
  "Regional", "Verified: Renton, King County, Seattle, Bellevue", "High",
  "Title 'Residential Dumpster Cleaning | Garbage Trash Bin Odor Removal'; description: residential and commercial in greater Washington areas", "None"),
 ("P-20", "Occasions Paper", "Retail", "Verified (website)", "None (online sales not evident)",
  "Retail; B2C", "Verified: store and authorized dealer", "B2C",
  "Walk-in; Local search; Social media; Repeat customers; Referral", INF, "Fine stationery, gifts and gourmet; MacKenzie-Childs dealer",
  "Local", "Verified: Norman, OK; 2001 W Main St", "High",
  "Description: 'fine stationery and gifts... authorized MacKenzie-Childs dealer in Norman, Oklahoma'", "Online sales not evident"),
 ("P-21", "Ocean View Lodging", "Hospitality", "Verified (website)", "Travel",
  "Other (reservation-based lodging; online booking); B2C", "Verified: 'Book Hotel Guest Rooms', book now", "B2C (travelers)",
  "Google/Search; Partnerships (online travel agencies); Repeat customers; Referral", "Partly verified (online booking present)", "Motel guest rooms near the ocean",
  "Local", "Verified: Fort Bragg, CA (destination market draws visitors from outside)", "High",
  "Title 'Book Hotel Guest Rooms CA | Ocean View Lodging'; description lists room amenities", "None"),
 ("P-22", "Orion Opticals", "Medical (optometry)", "Verified (website)", "Retail (eyewear)",
  "Appointment-based; Retail; Local service; Recurring service (annual exams); B2C", "Verified: eye exams, eyewear, 'book online'", "B2C (patients)",
  "Local search; Google/Search; Walk-in (shopping center); Referral; Repeat customers; Partnerships (vision insurance)", "Partly verified (online booking)", "Eye exams, contact lenses, designer eyewear",
  "Local", "Verified: Concord, CA (Veranda Shopping Center)", "High",
  "Title 'Orion Optical | Comprehensive Eye Care in Concord, CA'; description: eye exams, contact lenses, designer eyewear", "Source email belongs to a third-party domain"),
 ("P-23", "Ornamental Grasses", "Retail (plant nursery)", "Verified (website text mentions a nursery)", "Other (horticulture)",
  "Retail; Appointment-based (visits by appointment); B2C", "Mixed: nursery verified, appointment basis weak", "B2C (gardeners); possibly B2B (landscapers)",
  "Local search; Referral; Google/Search; Walk-in", INF, "Ornamental grasses (plants) and growing information",
  "Local", "Verified: Olympia, WA 98506", "Medium",
  "Title 'Ornamental Grasses | Add Texture and Beauty to Your Garden'; page text mentions nursery and appointment", "Reads partly as an information site; retail model not fully evident"),
 ("P-24", "Pinpoint Resource", "Retail", "Verified (website)", "None",
  "Retail; B2C", "Verified: store address", "B2C (men; wedding parties)",
  "Walk-in; Local search; Referral; Social media; Repeat customers", INF, "Menswear for work, weddings and everyday",
  "Local", "Verified: Tulsa, OK; 5201 S. Sheridan", "High",
  "Title 'Menswear in Tulsa for Work, Weddings & More'; description with store address", "'cart' text present but online sales not confirmed"),
 ("P-25", "Prime Care Dental Indy", "Dental", "Verified (website)", "Healthcare",
  "Appointment-based; Local service; Multi-location (two addresses on site); High-ticket service (implants, Invisalign); Emergency service; B2C", "Verified (website)", "B2C (patients)",
  "Google/Search; Local search; Referral; Repeat customers; Partnerships (insurance)", INF, "Family and cosmetic dentistry, Invisalign, implants",
  "Local", "Verified: Indianapolis (Lawrence, East Indianapolis, Cumberland); two locations", "High",
  "Title 'Dentist in Lawrence, IN, Cosmetic and Family Dentistry 46226'; two street addresses on site", "None"),
 ("P-26", "Rosewood Parke", "Other (homeowners / community association)", "Verified (website)", "None",
  "Other (resident association; member dues); not a commercial business", "Verified (website)", "Members (residents)",
  "Not applicable (word of mouth among residents)", "Verified: no commercial acquisition", "Community park and neighborhood communication",
  "Local", "Verified: Maple Valley, WA", "High",
  "Title 'Rosewood Parke Maple Valley WA'; description: park for all residents of Maple Valley", "Not a business; officer role emails only"),
 ("P-27", "Superior Coatings NW", "Home Services", "Verified (website)", "Construction",
  "Local service; Project-based; High-ticket service; Lead generation; B2C; B2B (commercial painting)", "Verified (website)", "B2C and B2B",
  "Local search; Google/Search; Referral", INF, "Interior and exterior home painting; commercial painting and coatings",
  "Regional", "Verified: 'Serving the South Puget Sound'; Pierce County", "High",
  "Title 'Interior and Exterior Home Painting NW | Commercial Painting'", "None"),
 ("P-28", "Tag OK", "Other (animal welfare nonprofit)", "Verified (website)", "None",
  "Other (nonprofit program; donations, volunteers); B2C", "Verified: volunteer pages", "Pet owners (B2C); donors",
  "Social media; Partnerships (shelters, vets); Referral", INF, "Low-to-no-cost pet ID tagging",
  "Regional", "Verified: Oklahoma ('OK' in title); Broken Arrow address", "High",
  "Title 'TagOK | Pet Population Control | Pet Tagging | Save Lives | OK'", "Nonprofit"),
 ("P-29", "The Bartan Company", "Other (event services)", "Verified (website)", "Hospitality",
  "Project-based (per event); Local service; B2C; B2B (weddings, corporate events)", "Verified (website)", "B2C and B2B",
  "Referral; Social media; Partnerships (event planners); Google/Search", INF, "Eco-friendly event solutions (reusable tableware, waste-minimizing services)",
  "Local (India)", "Verified: Hyderabad, India named on site; +91 phone numbers", "High",
  "Title 'Eco-Friendly Event Solutions by The Bartan Company'; description: sustainable services for weddings and corporate events", "Outside the US market"),
 ("P-30", "Top Dollar Pawn and Check Cashing", "Financial Services", "Verified (website)", "Retail (resale of jewelry, firearms, electronics)",
  "Retail; B2C", "Verified (website)", "B2C",
  "Walk-in; Local search; Google/Search; Repeat customers", INF, "Pawn loans, check cashing, buying and selling jewelry, firearms, electronics",
  "Local", "Verified: Tulsa, OK", "High",
  "Title 'Top Dollar Pawn Tulsa, OK - Buy, Sell, & Pawn Jewelry Etc'; description lists jewelry, firearms, electronics", "Regulated categories (firearms, loans)"),
 ("P-31", "Trans Landscaping", "Home Services", "Verified (website)", "Construction (landscape installation)",
  "Local service; Project-based; High-ticket service; Lead generation; B2C", "Verified (website)", "B2C (homeowners)",
  "Local search; Google/Search; Referral", INF, "Residential landscape design and installation",
  "Regional", "Verified: serves Spanaway, Puyallup, South Hill, Auburn, Bonney Lake, Sumner, Edgewood, Milton and Graham", "High",
  "Title 'Landscape and Design | Tran's Landscaping | Washington'; 'We Serve' town list", "Site spells the name 'Tran's Landscaping'"),
 ("P-32", "VIP Pest Solutions", "Home Services", "Verified (website)", "B2B Services (commercial pest control)",
  "Local service; Recurring service; Subscription (service plans on site); B2C; B2B", "Verified: plans, residential and commercial on site", "B2C and B2B",
  "Google/Search; Local search; Referral; Repeat customers", INF, "Residential and commercial pest control",
  "Regional", "Verified: Santa Maria, CA; serves San Luis Obispo, Santa Barbara and Ventura Counties", "High",
  "Title 'VIP Pest Solutions | Pest Control | Santa Maria, CA'; description: protect your home and office space", "None"),
 ("P-33", "Wheeler Sonoma Printing", "B2B Services", "Verified (website)", "Manufacturing (print production)",
  "B2B; Project-based; Recurring service (repeat orders, inventory management); Local service", "Verified (website)", "B2B (law firms, financial institutions, real estate, wine, hospitality, local government)",
  "Referral; Repeat customers; Outbound sales; Google/Search", INF, "Commercial printing and engraving",
  "Regional", "Verified: Vallejo, CA; name references Sonoma", "High",
  "Title 'Customized Engraving Printing Services Vallejo CA | Wheeler-Sonoma'; description lists client industries", "None"),
 ("P-34", "Will Rogers Stage Foundation", "Other (performing arts nonprofit / venue)", "Verified (website)", "None",
  "B2C; Ecommerce (online ticket sales); Other (nonprofit: donations, members, volunteers)", "Verified: tickets, donate, member, volunteer on site", "Audiences (B2C); donors and members",
  "Ecommerce (ticketing); Social media; Google/Search; Partnerships; Repeat customers", "Partly verified (online ticketing and donation pages)", "Live performances and ticket sales",
  "Local", "Verified: Tulsa", "High",
  "Title 'Buy Tickets for Upcoming Shows | Will Rogers Stage'; description lists upcoming shows", "Nonprofit foundation"),
 ("P-35", "Workhub Tulsa", "Real Estate (flexible office / coworking)", "Verified (website)", "B2B Services",
  "B2B; Subscription (memberships); Recurring service; Local service", "Verified: members, 24/7 access", "B2B (small businesses, remote workers, freelancers)",
  "Google/Search; Local search; Referral; Social media; Partnerships", INF, "Coworking: private offices, conference rooms, memberships",
  "Local", "Verified: Tulsa; 6539 E. 31st St", "High",
  "Title 'Workhub, Tulsa's top co-working destination'; description: private offices, conference rooms", "None"),
 ("P-36", "Zellersins", "Insurance", "Verified (website text: insurance, coverage, quotes)", "Financial Services",
  "Consultation-based; Lead generation; Recurring service (policy renewals); B2C; B2B", "Mixed: insurance verified, lines of business inferred", "B2C and B2B (policyholders)",
  "Google/Search; Referral; Repeat customers; Local search", INF, "Insurance agency (coverage and quotes)",
  "Local", "Inferred: 707 area code; site title gives no location", "Medium",
  "Title 'Home - Zellers Group'; page text uses 'insurance' 37 times plus 'coverage' and 'quote'", "Name 'Zellersins' vs site brand 'Zellers Group'"),
 ("I-01", "Around29 Center for Enriched Studies", "Education", "Verified (website)", "None",
  "Appointment-based (book a visit); Subscription (tuition, inferred); B2C", "Mixed", "B2C (families)",
  "Referral; Local search; Social media; Google/Search", INF, "Daycare to secondary-level schooling (A.C.E.S)",
  "Unknown", "Unknown: no location on site; phone unusable", "Medium",
  "Title 'Around29 Center for Enriched Studies (A.C.E.S) - Future Ready'; description: holistic learning from daycare to secondary level, book a visit", "Internal tab record"),
 ("I-02", "Around29 Digital Media Solutions", "Professional Services (digital marketing and web agency)", "Verified (website)", "Technology",
  "B2B; Project-based; Recurring service (retainers, inferred)", "Mixed", "B2B (small and mid-size businesses)",
  "Referral; Google/Search; Partnerships; Outbound sales", INF, "Digital solutions: web, SEO, marketing",
  "Unknown", "Inferred: 253 area code (Tacoma area); site does not state a location", "Medium",
  "Title 'Affordable, Scalable & On Demand Digital Solutions | Around29'; description: comprehensive digital solutions for business goals", "The Partner organisation itself; website status Build in Progress"),
 ("I-03", "Search29", "Unknown", "Unknown (no website in source)", "Unknown",
  "Unknown", "Unknown", "Unknown",
  "Unknown", "Unknown", "Unknown",
  "Unknown", "Unknown", "Low",
  "No URL, phone or email in the source; name follows Around29's product naming (Send29, Studio29)", "Internal tab record"),
 ("I-04", "Send29", "Technology (SaaS email marketing)", "Verified (website)", "Professional Services",
  "B2B; Subscription / pay-per-use; Ecommerce (self-serve online platform)", "Verified: 'pay per send' pricing", "B2B (small businesses)",
  "Google/Search; Ecommerce (self-serve signup); Partnerships; Social media", "Partly verified (self-serve platform)", "Email marketing platform, pay per send",
  "National/International (online)", "Inferred: online platform; no location stated", "Medium",
  "Title 'Affordable Email Marketing for Small Business | Send29'; description: pay per send, not per contact", "Website status Build in Progress; Internal record"),
 ("I-05", "Lead You", "Technology (SaaS)", "Verified (website)", "B2B Services",
  "B2B; Subscription (inferred); Ecommerce (online platform)", "Mixed", "B2B",
  "Google/Search; Partnerships; Outbound sales; Social media", INF, "AI lead generation and sales automation platform",
  "National/International (online)", "Inferred: online platform", "Medium",
  "Title 'LeadYou | AI Lead Generation & Sales Automation Platform'; description: capture, qualify and convert leads with AI tools", "Internal record"),
 ("I-06", "Around29 themes", "Technology (website themes)", "Verified (weak: title 'Themes')", "Ecommerce",
  "Ecommerce (digital products, inferred); B2B; B2C", "Inferred", "B2B and B2C (site owners)",
  "Ecommerce; Google/Search; Partnerships", INF, "Website themes / templates",
  "National/International (online)", "Inferred: online product", "Low",
  "Title 'Themes'; no description; theme-related text only", "Name vs domain mismatch (studio29themes.com); Internal record"),
 ("I-07", "Around29.us", "Professional Services (web design and development)", "Verified (website)", "Technology",
  "B2B; Project-based", "Verified (website)", "B2B",
  "Referral; Google/Search; Partnerships", INF, "Web design, development, content, SEO, digital marketing",
  "Unknown", "Unknown: no location stated", "Medium",
  "Title 'Web Design & Development Built Around Your Business | Around29'; description: responsive websites, SEO and digital marketing under one roof", "Second Around29 agency site (see I-02); Internal record"),
 ("I-08", "Starling Education", "Education", "Inferred (name and .education domain)", "None",
  "Unknown", "Unknown", "B2C (inferred)",
  "Unknown", "Unknown", "Education services (from name)",
  "Unknown", "Unknown: 630 area code hint only", "Low",
  "Site did not respond (connection failed) on 8 Oct 2026", "Possible duplicate pair with I-09; Internal record"),
 ("I-09", "Starling Wonder Kids", "Education (preschool / early learning)", "Verified (page text: education, learning, preschool)", "None",
  "Appointment-based (inferred); Subscription (tuition, inferred); B2C", "Inferred", "B2C (families)",
  "Referral; Local search; Social media", INF, "Preschool / early learning",
  "Unknown", "Unknown: no location on page; phone unusable", "Medium",
  "Title 'Home - Starling Wonderkids'; page text mentions education, learning, preschool, school", "Possible duplicate pair with I-08; Internal record"),
]
assert len(R) == 45 and all(len(r) == len(HEADER) for r in R)

INDUSTRIES = ["Home Services","Dental","Medical","Healthcare","Legal","Automotive","Construction","Real Estate","Financial Services","Insurance",
              "Hospitality","Restaurant/Food","Ecommerce","Retail","Professional Services","B2B Services","Education","Beauty & Wellness","Fitness",
              "Travel","Technology","Manufacturing","Logistics","Other","Unknown"]
MODELS = ["Local service","Appointment-based","Lead generation","Ecommerce","Retail","B2B","B2C","Subscription","Recurring service","High-ticket service",
          "Emergency service","Project-based","Consultation-based","Franchise","Multi-location","Manufacturer","Distributor","Marketplace","Other","Unknown"]
GEOS = ["Local","Local (India)","Regional","National","National/International (online)","Unknown"]
CONF = ["High","Medium","Low"]

rows = [list(r) for r in R]
n_data = len(rows)
last = n_data + 1  # last data row number in sheet
blank = [None] * len(HEADER)
def pad(a, b): return [a, b] + [None] * (len(HEADER) - 2)

payload = [HEADER] + rows
payload.append(blank)
start_ind = len(payload) + 1  # sheet row of the heading
payload.append(pad("Primary industry distribution", "Records"))
for i, ind in enumerate(INDUSTRIES):
    r = len(payload) + 1
    payload.append(pad(ind, f'=COUNTIF($C$2:$C${last},$A{r}&"*")'))
payload.append(pad("Total", f"=SUM(B{start_ind+1}:B{start_ind+len(INDUSTRIES)})"))
payload.append(blank)
payload.append(pad("Business model tags (records carrying the tag)", "Records"))
for m in MODELS:
    r = len(payload) + 1
    payload.append(pad(m, f'=COUNTIF($F$2:$F${last},"*"&$A{r}&"*")'))
payload.append(blank)
payload.append(pad("Geographic scope", "Records"))
g0 = len(payload) + 1
for g in GEOS:
    r = len(payload) + 1
    payload.append(pad(g, f"=COUNTIF($L$2:$L${last},$A{r})"))
payload.append(pad("Total", f"=SUM(B{g0}:B{g0+len(GEOS)-1})"))
payload.append(blank)
payload.append(pad("Classification confidence", "Records"))
c0 = len(payload) + 1
for c in CONF:
    r = len(payload) + 1
    payload.append(pad(c, f"=COUNTIF($N$2:$N${last},$A{r})"))
payload.append(pad("Total", f"=SUM(B{c0}:B{c0+len(CONF)-1})"))
payload.append(blank)
payload.append(pad("Industry evidence", "Records"))
for lab in ["Verified", "Inferred", "Unknown"]:
    r = len(payload) + 1
    payload.append(pad(lab, f'=COUNTIF($D$2:$D${last},$A{r}&"*")'))

def cell(v, formula_ok=True):
    if v is None or isinstance(v, (int, float)): return v
    s = str(v)
    if s.startswith("="): return s
    if s[:1] in "+-(0123456789'": return "'" + s
    return s
sheet_payload = [[cell(v) for v in row] for row in payload]
with open(os.path.join(SP, "class_lines.jsonl"), "w", encoding="utf-8") as fh:
    fh.write(chr(10).join(json.dumps(r, ensure_ascii=False) for r in sheet_payload))
with open(os.path.join(PROJ, "classification.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(HEADER); w.writerows(rows)

# distributions for the report
def base(v): return v.split(" (")[0]
ind_all = Counter(base(r[2]) for r in rows); ind_p = Counter(base(r[2]) for r in rows if r[0].startswith("P"))
print("rows:", len(sheet_payload), "cols:", len(HEADER))
print("INDUSTRY all:", dict(ind_all)); print("INDUSTRY prospects:", dict(ind_p))
tags = Counter(); tags_p = Counter()
for r in rows:
    for m in MODELS:
        if m.lower() in r[5].lower():
            tags[m] += 1
            if r[0].startswith("P"): tags_p[m] += 1
print("MODEL tags all:", dict(tags)); print("MODEL tags prospects:", dict(tags_p))
print("GEO all:", dict(Counter(r[11] for r in rows))); print("GEO prospects:", dict(Counter(r[11] for r in rows if r[0].startswith('P'))))
print("CONF all:", dict(Counter(r[13] for r in rows))); print("CONF prospects:", dict(Counter(r[13] for r in rows if r[0].startswith('P'))))
print("EVIDENCE industry:", dict(Counter(r[3].split(" ")[0] for r in rows)))
print("CUSTOMER type all:", dict(Counter(("B2B and B2C" if ("B2C" in r[7] and "B2B" in r[7]) else "B2C" if "B2C" in r[7] else "B2B" if "B2B" in r[7] else "Members/donors" if ("Members" in r[7] or "donors" in r[7]) else r[7]) for r in rows)))
print("ACQ channels (prospects):", dict(Counter(ch.split(" (")[0].strip() for r in rows if r[0].startswith('P') for ch in r[8].split(";"))))
