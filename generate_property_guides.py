#!/usr/bin/env python3
"""
Generate expanded property buying guides for all countries (except Australia + South Korea).
Each guide: 900-1200 words of country-specific content.
Run from the repo root: python3 generate_property_guides.py
"""

COUNTRIES = {
    "belgium": {
        "name": "Belgium", "iso": "BE", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Brussels, Antwerp, Ghent, and Liège",
        "priceRange": "€200,000 for apartments in smaller cities to €500,000+ in central Brussels",
        "deposit": "10-20%",
        "transferTax": "Registration duties range from 6% in Flanders to 12.5% in Wallonia and Brussels, making region choice a major cost factor",
        "agentTerm": "estate agent (immokantoor/agence immobilière)",
        "lawyerTerm": "notary (notaris/notaire)",
        "legalProcess": "All property sales in Belgium must pass through a notary, who handles the deed transfer, title searches, and registration. The buyer and seller can use the same notary or appoint separate ones. The compromise (preliminary contract) is binding once signed, with a 10% deposit typically required",
        "uniqueFeature": "Belgium's market is split between three regions — Flanders, Wallonia, and Brussels — each with different registration duties, tax incentives, and market dynamics. Flanders recently reformed its registration duty to a flat 3% for primary residences (down from 6%), making it significantly cheaper for owner-occupiers",
        "govSupport": "Flanders offers a reduced 3% registration duty for primary residences. Brussels has an abatement scheme exempting the first €200,000 from registration duties on purchases up to €600,000. Wallonia offers reduced rates for modest homes. The housing bonus (woonbonus) tax deduction has been abolished in most regions but replaced with other incentives",
        "terms": "15-25 years, with 20-year terms most common",
        "ltv": "Historically up to 90-100%, but National Bank guidelines now recommend maximum 90% LTV for primary residences, with 80% for non-first-time buyers",
        "keyLenders": "BNP Paribas Fortis, KBC, ING Belgium, Belfius, and AXA Bank",
        "buyingCosts": "10-15% in Wallonia/Brussels, 5-8% in Flanders",
        "inspectionNote": "Belgian homes are sold 'as seen' unless specific guarantees are included in the contract. A professional inspection is strongly recommended but not legally required",
        "foreignBuyer": "No restrictions on foreign buyers in Belgium. Non-EU buyers face the same process as Belgian citizens, though mortgage approval may require Belgian-based income or a larger deposit"
    },
    "brazil": {
        "name": "Brazil", "iso": "BR", "currency": "BRL", "symbol": "R$",
        "centralBank": "Central Bank of Brazil",
        "cities": "São Paulo, Rio de Janeiro, Brasília, Belo Horizonte, and Curitiba",
        "priceRange": "R$200,000 for apartments in mid-tier cities to R$1,000,000+ in premium São Paulo and Rio neighbourhoods",
        "deposit": "20-30%",
        "transferTax": "ITBI (Imposto de Transmissão de Bens Imóveis) ranges from 2-3% depending on the municipality",
        "agentTerm": "real estate broker (corretor de imóveis)",
        "lawyerTerm": "property lawyer (advogado imobiliário)",
        "legalProcess": "Property transfers require registration at the Cartório de Registro de Imóveis (Real Estate Registry Office). The buyer must obtain a matrícula (property certificate) confirming ownership history and any encumbrances. The escritura pública (public deed) is executed at a Tabelionato de Notas (notary office)",
        "uniqueFeature": "Brazil uses a system called Minha Casa Minha Vida (My House My Life), a massive government housing programme that provides subsidised financing for low and middle-income families. The programme offers below-market interest rates through Caixa Econômica Federal, the state-owned bank that dominates residential lending",
        "govSupport": "Minha Casa Minha Vida provides subsidised interest rates as low as 4-5% (compared to market rates of 9-12%) for qualifying families. Income limits and property value caps apply by region. FGTS (Workers' Severance Fund) can be used toward the deposit or to reduce monthly payments",
        "terms": "Up to 35 years, with 20-30 year terms most common",
        "ltv": "Typically 70-80% through conventional banks, with Caixa offering up to 80% for FGTS-eligible buyers",
        "keyLenders": "Caixa Econômica Federal (dominant market share), Banco do Brasil, Itaú Unibanco, Bradesco, and Santander Brasil",
        "buyingCosts": "4-6% including ITBI, registry fees, notary fees, and broker commission",
        "inspectionNote": "Professional property inspections are not standard practice in Brazil. Buyers should independently verify structural condition, check for irregular constructions (obras irregulares), and confirm all municipal permits are in order",
        "foreignBuyer": "Foreigners can buy most property types in Brazil with a CPF (tax registration number). Rural land near borders and coastal land have restrictions. Foreigners cannot access FGTS or Minha Casa Minha Vida benefits"
    },
    "canada": {
        "name": "Canada", "iso": "CA", "currency": "CAD", "symbol": "$",
        "centralBank": "Bank of Canada",
        "cities": "Toronto, Vancouver, Montreal, Calgary, Ottawa, and Edmonton",
        "priceRange": "$300,000 in mid-tier cities to $1,000,000+ in Toronto and Vancouver",
        "deposit": "5-20%",
        "transferTax": "Land transfer tax varies by province — Ontario charges 0.5-2.5% on a sliding scale, British Columbia charges 1-5%, while Alberta has no land transfer tax. Toronto adds an additional municipal land transfer tax",
        "agentTerm": "real estate agent or REALTOR®",
        "lawyerTerm": "real estate lawyer or notary (in Quebec and BC)",
        "legalProcess": "The buyer makes an offer through their agent, which becomes binding once accepted. A deposit (typically 5%) is held in trust. The lawyer handles title searches, mortgage registration, and closing. Most provinces allow a condition period for financing and inspection",
        "uniqueFeature": "Canada's mortgage system is unique in that most mortgages have terms of only 5 years (the amortisation period is 25-30 years, but the rate is renegotiated every 5 years). The federal government also requires mortgage stress testing — buyers must qualify at the contract rate plus 2% or the Bank of Canada's qualifying rate, whichever is higher",
        "govSupport": "The First Home Savings Account (FHSA) allows tax-deductible contributions up to $40,000 for a first home deposit. The Home Buyers' Plan lets you withdraw up to $60,000 from your RRSP tax-free for a first home. First-time buyers also receive a land transfer tax rebate in Ontario and BC, and may access the First-Time Home Buyer Incentive for shared equity support",
        "terms": "Amortisation up to 25 years (30 years with 20%+ deposit). Mortgage terms typically 1-5 years, with 5-year fixed being most popular",
        "ltv": "Up to 95% with CMHC mortgage insurance (mandatory for LTV over 80%). Properties over $1 million require minimum 20% deposit",
        "keyLenders": "RBC, TD Bank, Scotiabank, BMO, CIBC, National Bank, plus credit unions and monoline lenders like First National and MCAP",
        "buyingCosts": "3-5% including land transfer tax, legal fees, title insurance, and home inspection",
        "inspectionNote": "Professional home inspections are standard and highly recommended. Most offers include an inspection condition, though competitive markets have seen buyers waiving inspections — a risky practice",
        "foreignBuyer": "The Prohibition on the Purchase of Residential Property by Non-Canadians Act restricts foreign buyers from purchasing residential property in most areas. Exceptions exist for permanent residents, refugees, and some work permit holders. Check current rules as this legislation is reviewed periodically"
    },
    "denmark": {
        "name": "Denmark", "iso": "DK", "currency": "DKK", "symbol": "kr",
        "centralBank": "Danmarks Nationalbank",
        "cities": "Copenhagen, Aarhus, Odense, and Aalborg",
        "priceRange": "kr 1,500,000 for apartments outside Copenhagen to kr 5,000,000+ in central Copenhagen",
        "deposit": "5% minimum by law",
        "transferTax": "Registration duty (tinglysningsafgift) is 0.6% of the property value plus a fixed fee of kr 1,850. Mortgage registration carries an additional 1.45% plus kr 1,850",
        "agentTerm": "estate agent (ejendomsmægler)",
        "lawyerTerm": "property lawyer (advokat)",
        "legalProcess": "Denmark's system is transparent and well-regulated. The seller's agent prepares a comprehensive sales prospectus including an energy certificate, tilstandsrapport (condition report), and el-installation report. The buyer typically has a 6-business-day cooling-off period after signing the purchase agreement. Legal ownership transfers through the Land Registry (Tinglysning)",
        "uniqueFeature": "Denmark has a unique mortgage system based on covered bonds (realkreditobligationer). Mortgage banks like Nykredit, Realkredit Danmark, and Totalkredit issue bonds on the capital market, passing the rate directly to borrowers. This creates some of the lowest mortgage rates in Europe and extremely long fixed-rate terms — 30-year fixed rates are standard",
        "govSupport": "Denmark does not have major first-time buyer subsidies. However, the mortgage interest tax deduction allows homeowners to deduct a portion of mortgage interest from taxable income (at approximately 33% for interest up to kr 50,000 per person, reducing above that threshold). Some municipalities offer discounted plots to attract new residents",
        "terms": "Up to 30 years for covered bond mortgages, with 30-year terms being standard",
        "ltv": "Maximum 80% through covered bond lenders, with the remaining 15% available as a bank top-up loan. Minimum 5% cash deposit required by law",
        "keyLenders": "Nykredit/Totalkredit (largest), Realkredit Danmark (Danske Bank group), Jyske Realkredit, Nordea Kredit, and DLR Kredit",
        "buyingCosts": "2-5% including registration duty, mortgage registration, lawyer fees, and agent commission (paid by seller)",
        "inspectionNote": "The tilstandsrapport (condition report) is typically paid for by the seller and is a standard part of the sales package. The buyer can purchase an ejerskifteforsikring (change-of-ownership insurance) based on this report to cover hidden defects",
        "foreignBuyer": "Non-EU citizens need permission from the Danish Ministry of Justice to buy property in Denmark unless they have lived in the country for at least 5 years. EU/EEA citizens can buy freely if the property will be their primary residence"
    },
    "france": {
        "name": "France", "iso": "FR", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Paris, Lyon, Marseille, Bordeaux, Toulouse, and Nice",
        "priceRange": "€150,000 for apartments in smaller cities to €500,000+ in Paris, with premium arrondissements exceeding €1,000,000",
        "deposit": "10-20%",
        "transferTax": "Notary fees (frais de notaire) include registration taxes and notary charges, totalling approximately 7-8% for existing properties and 2-3% for new builds",
        "agentTerm": "estate agent (agent immobilier)",
        "lawyerTerm": "notary (notaire)",
        "legalProcess": "French property purchases follow a structured legal process. After agreeing on price, both parties sign a compromis de vente (preliminary contract) and the buyer pays a 5-10% deposit. A mandatory 10-day cooling-off period follows. The notaire conducts extensive searches and checks over the next 2-3 months before the acte authentique (final deed) is signed",
        "uniqueFeature": "France offers exceptionally long fixed-rate mortgages — 20 and 25-year fully fixed rates are standard, giving buyers long-term payment certainty that is rare in other European markets. French lenders also assess affordability based on a strict 35% debt-to-income ratio cap, regulated by the Haut Conseil de Stabilité Financière (HCSF)",
        "govSupport": "The Prêt à Taux Zéro (PTZ) is a zero-interest government loan available to first-time buyers purchasing new-build or heavily renovated properties. It covers up to 40% of the purchase price in eligible zones, with income limits varying by region and household size. The Prêt d'Accession Sociale (PAS) provides subsidised rates for lower-income buyers",
        "terms": "Up to 25 years (27 years for new builds with deferred start), with 20-25 year fixed rates most common",
        "ltv": "Typically 80-90%, though 100% financing was once common and is now restricted by HCSF rules. Most buyers need at least 10% deposit plus funds for notary fees",
        "keyLenders": "Crédit Agricole (largest), BNP Paribas, Société Générale, Crédit Mutuel, Banque Populaire/Caisse d'Épargne (BPCE), and La Banque Postale",
        "buyingCosts": "8-12% for existing properties (dominated by notary fees), 4-6% for new builds",
        "inspectionNote": "Sellers must provide mandatory diagnostic reports (DDT) covering energy performance, asbestos, lead, termites, natural risks, and electrical/gas installations. Buyers should consider additional independent inspections for structural issues not covered by mandatory reports",
        "foreignBuyer": "No restrictions on foreign property ownership in France. Non-residents can obtain French mortgages from French banks, though the process requires more documentation and some banks specialise in non-resident lending"
    },
    "germany": {
        "name": "Germany", "iso": "DE", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Berlin, Munich, Hamburg, Frankfurt, Düsseldorf, and Stuttgart",
        "priceRange": "€200,000 for apartments in eastern German cities to €600,000+ in Munich, Hamburg, and Frankfurt",
        "deposit": "20-30%",
        "transferTax": "Grunderwerbsteuer (real estate transfer tax) ranges from 3.5% to 6.5% depending on the federal state. Bavaria and Saxony charge 3.5%, while Brandenburg, North Rhine-Westphalia, Schleswig-Holstein, and Thuringia charge 6.5%",
        "agentTerm": "real estate agent (Immobilienmakler)",
        "lawyerTerm": "notary (Notar)",
        "legalProcess": "A notary is legally required for all property transactions in Germany. The notary drafts the purchase contract, reads it aloud to both parties, handles the land registry transfer, and manages the payment process through a Notaranderkonto (escrow account) if requested. The buyer must be registered in the Grundbuch (land registry) to become the legal owner",
        "uniqueFeature": "Germany is traditionally a nation of renters — homeownership rates are among the lowest in Europe at around 50%. This means the buying process is thorough and heavily regulated, with strong buyer protections. The Baukindergeld (building child benefit) was a popular subsidy for families but has ended, leaving fewer government incentives for buyers",
        "govSupport": "Germany currently offers limited direct buyer subsidies at the federal level following the end of Baukindergeld. Some federal states (Länder) offer individual programmes — for example, reduced transfer tax rates or KfW-subsidised energy-efficient building loans. KfW Bank provides below-market-rate loans for energy-efficient new builds and renovations through programmes like KfW 261",
        "terms": "10-30 years amortisation, but interest rate is typically fixed for 10-15 year periods (Zinsbindung), after which the rate is renegotiated",
        "ltv": "Conservative lending culture — 70-80% LTV is standard, with 100% financing rare and expensive. Banks expect buyers to cover transfer tax, notary fees, and agent commission from savings",
        "keyLenders": "Deutsche Bank, Commerzbank, Sparkassen (savings banks), Volksbanken (cooperative banks), ING-DiBa, Interhyp (broker), and Dr. Klein (broker)",
        "buyingCosts": "10-15% including transfer tax (3.5-6.5%), notary fees (~1.5%), land registry (~0.5%), and agent commission (3-6% split between buyer and seller)",
        "inspectionNote": "Professional building inspections (Baugutachten) are not standard practice in Germany but are strongly recommended, particularly for older properties. The seller has limited disclosure obligations compared to other countries",
        "foreignBuyer": "No restrictions on foreign property ownership in Germany. Non-residents can obtain German mortgages, though banks typically require a higher deposit (30-40%) and proof of German-based income or substantial foreign income"
    },
    "hong-kong": {
        "name": "Hong Kong", "iso": "HK", "currency": "HKD", "symbol": "$",
        "centralBank": "Hong Kong Monetary Authority",
        "cities": "Hong Kong Island, Kowloon, New Territories, and Lantau Island",
        "priceRange": "HK$4,000,000 for small apartments in New Territories to HK$15,000,000+ on Hong Kong Island",
        "deposit": "10-50% depending on property value and MIP eligibility",
        "transferTax": "Ad Valorem Stamp Duty at Scale 2 rates for first-time permanent residents (HK$100 to 4.25%), or flat 15% for non-first-time buyers and non-permanent residents",
        "agentTerm": "estate agent (licensed under the Estate Agents Authority)",
        "lawyerTerm": "solicitor (律師)",
        "legalProcess": "Property purchases follow a structured process — the buyer signs a Provisional Agreement for Sale and Purchase and pays a preliminary deposit (typically 3-5%). Within 14 days, the Formal Agreement is signed with a further deposit (typically bringing total to 10%). The solicitor conducts title searches and handles the assignment/transfer. Completion typically takes 2-3 months",
        "uniqueFeature": "Hong Kong is one of the most expensive property markets in the world relative to income, with average price-to-income ratios exceeding 20x. The market is dominated by a small number of major developers (Sun Hung Kai, CK Asset, Henderson Land, New World). Government subsidised housing through the Hong Kong Housing Authority serves a significant portion of the population",
        "govSupport": "The Home Ownership Scheme (HOS) sells subsidised flats at 30-40% below market value to eligible residents. The Green Form Subsidised Home Ownership (GSH) scheme targets public housing tenants. The White Form Secondary Market Scheme (WFSM) allows eligible buyers to purchase HOS resale flats. The Mortgage Insurance Programme (MIP) allows higher LTV ratios up to 90%",
        "terms": "Up to 30 years, with 25-30 year terms most common",
        "ltv": "50-60% without mortgage insurance, up to 80-90% with HKMC Mortgage Insurance Programme for eligible properties",
        "keyLenders": "HSBC, Hang Seng Bank, Bank of China (Hong Kong), Standard Chartered, and Bank of East Asia",
        "buyingCosts": "5-20% depending on stamp duty bracket and buyer status, plus legal fees, agent commission (1%), and mortgage insurance premium",
        "inspectionNote": "Professional building inspections are recommended for older buildings. The seller provides a Property Information Form but buyers should independently verify building orders, unauthorised building works, and the building's maintenance condition through the Buildings Department",
        "foreignBuyer": "No restrictions on foreign property ownership in Hong Kong. However, non-permanent residents pay 15% stamp duty instead of the lower Scale 2 rates, significantly increasing purchase costs"
    },
    "india": {
        "name": "India", "iso": "IN", "currency": "INR", "symbol": "₹",
        "centralBank": "Reserve Bank of India",
        "cities": "Mumbai, Delhi NCR, Bangalore, Hyderabad, Chennai, Pune, and Kolkata",
        "priceRange": "₹30,00,000 for apartments in tier-2 cities to ₹2,00,00,000+ in Mumbai and premium Delhi locations",
        "deposit": "10-25%",
        "transferTax": "Stamp duty ranges from 3% to 8% depending on the state — Maharashtra charges 5% (6% in Mumbai), Karnataka 5%, Delhi 4-6%, and Tamil Nadu 7%. Registration charges add 1% in most states",
        "agentTerm": "property dealer or real estate broker (registered under RERA)",
        "lawyerTerm": "property lawyer or advocate",
        "legalProcess": "The buyer verifies the title through a lawyer, checking encumbrance certificates, khata, and property tax records. For under-construction properties, the developer must be RERA-registered. The sale deed is executed on stamp paper at the Sub-Registrar's Office. Buyers should verify the complete chain of ownership documents and ensure there are no pending litigation or municipal dues",
        "uniqueFeature": "India's Real Estate Regulatory Authority (RERA) introduced in 2016 fundamentally changed the market by requiring all projects above a certain size to be registered, with escrow accounts for buyer funds and penalties for delays. Each state has its own RERA portal where buyers can verify project registration and developer track record",
        "govSupport": "Pradhan Mantri Awas Yojana (PMAY) provides interest subsidy on home loans for economically weaker sections and lower-income groups — up to ₹2.67 lakh subsidy on loans. Section 80C allows tax deduction up to ₹1.5 lakh on principal repayment. Section 24(b) provides deduction up to ₹2 lakh on home loan interest for self-occupied property. First-time buyers get additional deduction under Section 80EEA",
        "terms": "Up to 30 years, with 15-20 year terms most common",
        "ltv": "Up to 90% for loans under ₹30 lakh, 80% for loans between ₹30-75 lakh, and 75% for loans above ₹75 lakh (as per RBI guidelines)",
        "keyLenders": "State Bank of India (largest), HDFC Bank, ICICI Bank, Bank of Baroda, LIC Housing Finance, PNB Housing, and Bajaj Housing Finance",
        "buyingCosts": "7-12% including stamp duty, registration fees, GST (for under-construction), legal fees, and brokerage (1-2%)",
        "inspectionNote": "For under-construction properties, verify RERA registration, occupancy certificate status, and CERSAI charges. For resale, obtain an encumbrance certificate for at least 30 years and verify property tax clearance. Physical inspection should check for structural integrity, water supply, and legal compliance",
        "foreignBuyer": "NRIs (Non-Resident Indians) and PIOs (Persons of Indian Origin) can buy residential and commercial property freely. Foreign nationals of non-Indian origin cannot buy residential property but can buy commercial property. All purchases must be in Indian rupees through normal banking channels"
    },
    "ireland": {
        "name": "Ireland", "iso": "IE", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Dublin, Cork, Galway, Limerick, and Waterford",
        "priceRange": "€200,000 for properties outside Dublin to €450,000+ in Dublin",
        "deposit": "10% minimum (Central Bank rules)",
        "transferTax": "Stamp duty is 1% on properties up to €1 million and 2% on the balance above €1 million for residential purchases",
        "agentTerm": "estate agent or auctioneer",
        "lawyerTerm": "solicitor",
        "legalProcess": "The buyer's solicitor conducts title investigations, raises requisitions on title, and reviews the contract for sale. The buyer signs the contract and pays a booking deposit (typically €5,000-€10,000) followed by the balance of 10% on contract exchange. Closing typically takes 4-8 weeks from contract signing. The Property Registration Authority handles land registry transfers",
        "uniqueFeature": "Ireland's property market is characterised by strict Central Bank lending rules introduced in 2015 — first-time buyers need a minimum 10% deposit, while second-time buyers need 20%. The Help to Buy scheme partially offsets this for new builds. Gazumping is legal in Ireland, meaning a seller can accept a higher offer after agreeing to sell to you, until contracts are formally exchanged",
        "govSupport": "The Help to Buy (HTB) scheme provides a tax refund of up to €30,000 for first-time buyers purchasing or building a new home (the refund equals the lesser of €30,000, 10% of purchase price, or income tax/DIRT paid over the previous 4 years). The First Home Scheme provides shared equity support of up to 30% for new builds. The Local Authority Home Loan Scheme offers low-interest mortgages for lower-income applicants",
        "terms": "Up to 35 years, with 25-30 year terms most common",
        "ltv": "90% for first-time buyers, 80% for second and subsequent buyers (Central Bank macroprudential rules). LTI capped at 4x gross income for first-time buyers, 3.5x for others",
        "keyLenders": "Bank of Ireland, AIB (Allied Irish Banks), Permanent TSB, Avant Money, Finance Ireland, and ICS Mortgages",
        "buyingCosts": "3-5% including stamp duty (1%), legal fees, valuation, survey, and mortgage protection insurance",
        "inspectionNote": "Professional building surveys are strongly recommended in Ireland, particularly for older properties. A structural engineer's report (Type 2 or Type 3 survey) can identify issues ranging from pyrite contamination to structural defects. The BER (Building Energy Rating) certificate is legally required for all property sales",
        "foreignBuyer": "No restrictions on foreign property ownership in Ireland. Non-residents can obtain Irish mortgages, though options are more limited and larger deposits may be required"
    },
    "italy": {
        "name": "Italy", "iso": "IT", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Rome, Milan, Florence, Naples, Bologna, and Turin",
        "priceRange": "€80,000 for properties in southern Italy and rural areas to €500,000+ in central Milan and Rome",
        "deposit": "20-30%",
        "transferTax": "For primary residences, the imposta di registro is 2% of the cadastral value (significantly lower than market value) when buying from a private seller, or 4% VAT on the full price when buying new from a developer. Non-primary residences pay 9% or 10% VAT respectively",
        "agentTerm": "estate agent (agente immobiliare)",
        "lawyerTerm": "notary (notaio)",
        "legalProcess": "Italian property purchases follow a three-stage process. First, the proposta d'acquisto (purchase offer) is submitted. Second, once accepted, both parties sign the compromesso (preliminary contract) and the buyer pays a caparra confirmatoria (deposit, typically 10-20%). Third, the rogito (final deed) is signed before a notary, who handles all legal checks, tax payments, and land registry registration",
        "uniqueFeature": "Italy has a unique cadastral value system where property taxes are based on rendita catastale (cadastral income), which is typically far below market value. This means stamp duty on primary residences is calculated on a much lower base, making the effective tax rate very favourable. Italy also offers attractive schemes for buying €1 properties in depopulating villages, though renovation costs can be substantial",
        "govSupport": "First-time buyers under 36 with ISEE income below €40,000 receive exemption from registration tax, mortgage tax, and cadastral tax, plus a VAT credit for new builds. The Fondo di Garanzia Prima Casa provides government-backed mortgage guarantees of up to 80% of the property value for eligible buyers, allowing access to higher LTV mortgages",
        "terms": "Up to 30 years, with 20-25 year terms most common",
        "ltv": "Typically 60-80%. First-time buyers under 36 can access up to 100% LTV through the Fondo di Garanzia",
        "keyLenders": "Intesa Sanpaolo (largest), UniCredit, BPER Banca, Banco BPM, Credem, and MPS (Monte dei Paschi di Siena)",
        "buyingCosts": "5-10% for primary residences from private sellers, 8-14% for non-primary or developer purchases",
        "inspectionNote": "Professional building inspections are not standard practice in Italy but are recommended. Buyers should verify the conformità urbanistica e catastale (urban planning and cadastral compliance) — properties with irregular modifications can cause significant legal and financial problems. The APE (energy performance certificate) is mandatory",
        "foreignBuyer": "EU citizens can buy freely. Non-EU citizens can buy if their home country has a reciprocity agreement with Italy (most do). The codice fiscale (tax identification number) is required for any property purchase"
    },
    "japan": {
        "name": "Japan", "iso": "JP", "currency": "JPY", "symbol": "¥",
        "centralBank": "Bank of Japan",
        "cities": "Tokyo, Osaka, Yokohama, Nagoya, Sapporo, and Fukuoka",
        "priceRange": "¥15,000,000 for apartments in regional cities to ¥60,000,000+ in central Tokyo",
        "deposit": "10-20%",
        "transferTax": "Registration and license tax (登録免許税) is 0.3% for transfer registration, plus real estate acquisition tax (不動産取得税) of 3% for residential land and 3% for buildings. Stamp duty (印紙税) applies to the contract based on transaction value",
        "agentTerm": "real estate agent (不動産業者/fudōsan gyōsha, licensed under takken)",
        "lawyerTerm": "judicial scrivener (司法書士/shihō shoshi)",
        "legalProcess": "After agreeing on terms, the buyer pays earnest money (手付金, typically 5-10%) and signs the contract. A judicial scrivener handles the ownership transfer registration at the Legal Affairs Bureau (法務局). There is no escrow system — payment is typically exchanged directly for keys at the settlement meeting. Title insurance is not standard in Japan",
        "uniqueFeature": "Japanese property is unique in that buildings depreciate rapidly — wooden houses are considered worthless after about 22 years, and even reinforced concrete apartments lose most building value within 47 years. Land value is what retains worth. This means buyers often purchase older properties for land value alone and rebuild. Japan also has extremely low fixed mortgage rates, with some lenders offering rates below 1%",
        "govSupport": "The housing loan tax deduction (住宅ローン控除) allows buyers to deduct 0.7% of the remaining loan balance from income tax annually for 13 years on new homes (10 years for existing homes). Sumai-Kyufu-Kin (すまい給付金) provided cash grants to buyers based on income level but has been replaced by other schemes. Reduced registration tax rates apply for properties meeting certain quality standards",
        "terms": "Up to 35 years, with 35-year terms common for first-time buyers. The Flat 35 programme offers 35-year fully fixed rates",
        "ltv": "Up to 100% through the Flat 35 programme. Banks typically lend 80-100% for primary residences",
        "keyLenders": "MUFG Bank, Sumitomo Mitsui Banking, Mizuho Bank, Resona Bank, ARUHI (Flat 35 specialist), SBI Sumishin Net Bank, and Japan Housing Finance Agency (Flat 35)",
        "buyingCosts": "6-10% including agent commission (up to 3% + ¥60,000), registration taxes, stamp duty, and judicial scrivener fees",
        "inspectionNote": "Professional building inspections (建物状況調査/tatemono jōkyō chōsa) have become more common since 2018 law reforms required agents to explain whether an inspection has been conducted. For apartments, review the management association records (管理組合) for maintenance history, repair fund adequacy, and planned works",
        "foreignBuyer": "No restrictions on foreign property ownership in Japan. Foreigners can buy freely even without residency. However, obtaining a Japanese mortgage typically requires permanent residency or a Japanese spouse. Non-residents may access loans through specialist lenders at higher rates"
    },
    "malaysia": {
        "name": "Malaysia", "iso": "MY", "currency": "MYR", "symbol": "RM",
        "centralBank": "Bank Negara Malaysia",
        "cities": "Kuala Lumpur, Penang, Johor Bahru, Kota Kinabalu, and Malacca",
        "priceRange": "RM200,000 for apartments in secondary cities to RM800,000+ in central KL and premium Penang locations",
        "deposit": "10% minimum",
        "transferTax": "Stamp duty on transfer (Memorandum of Transfer) is tiered: 1% on the first RM100,000, 2% on RM100,001-500,000, 3% on RM500,001-1,000,000, and 4% above RM1,000,000. Legal fees follow a similar tiered structure",
        "agentTerm": "real estate negotiator or estate agent (registered with BOVAEA)",
        "lawyerTerm": "lawyer or advocate and solicitor",
        "legalProcess": "After agreeing on price, the buyer pays a booking fee (typically 2-3%) and signs a Letter of Offer. The Sale and Purchase Agreement (SPA) is signed within 14 days, with 7% balance to make 10% total deposit. The SPA is stamped at the Inland Revenue Board (LHDN). For new developments, developers use standardised SPAs regulated by the Housing Development Act. Transfer is completed at the local land office",
        "uniqueFeature": "Malaysia has minimum property purchase thresholds for foreign buyers, which vary by state — ranging from RM600,000 to RM2,000,000 depending on the state and property type. The country also distinguishes between freehold and leasehold land (typically 99-year leases), with leasehold properties trading at 10-20% below freehold equivalents",
        "govSupport": "Stamp duty exemption is available for first-time buyers purchasing properties up to RM500,000 — full exemption on the instrument of transfer and loan agreement. The MyFirst Home Scheme allows first-time buyers to obtain 100% financing for properties up to RM500,000. EPF (Employees Provident Fund) withdrawals from Account 2 can be used for property deposits and mortgage payments",
        "terms": "Up to 35 years, with maximum age of 70 at loan maturity",
        "ltv": "Up to 90% for first and second residential properties, 70% for third and subsequent properties (Bank Negara guidelines)",
        "keyLenders": "Maybank, CIMB Bank, Public Bank, RHB Bank, Hong Leong Bank, and AmBank",
        "buyingCosts": "5-8% including stamp duty, legal fees, valuation fees, and agent commission (typically paid by seller)",
        "inspectionNote": "For under-construction properties, the Housing Development Act provides a defect liability period of 24 months after vacant possession. For completed properties, engage a professional inspector to check for structural issues, particularly water damage and settlement. Strata-title properties should be checked for outstanding maintenance charges",
        "foreignBuyer": "Foreigners can buy property above state-set minimum thresholds (typically RM600,000-RM2,000,000). Foreign ownership is restricted in Malay Reserved Land, low and medium-cost properties, and agricultural land. MM2H (Malaysia My Second Home) visa holders may have additional advantages"
    },
    "mexico": {
        "name": "Mexico", "iso": "MX", "currency": "MXN", "symbol": "$",
        "centralBank": "Bank of Mexico",
        "cities": "Mexico City, Guadalajara, Monterrey, Cancún, Mérida, and Puebla",
        "priceRange": "$1,500,000 MXN for apartments in mid-tier cities to $5,000,000+ MXN in premium Mexico City and resort areas",
        "deposit": "10-30%",
        "transferTax": "ISAI (Impuesto Sobre Adquisición de Inmuebles) is the acquisition tax, typically 2-5% depending on the state and municipality. Mexico City charges approximately 5.5%",
        "agentTerm": "real estate agent (agente inmobiliario)",
        "lawyerTerm": "notary public (notario público)",
        "legalProcess": "A notario público (a government-appointed legal professional, different from US notaries) handles all property transactions. The notary verifies the title, ensures tax compliance, registers the deed with the Public Registry of Property (Registro Público de la Propiedad), and collects all transfer taxes. The escritura pública (public deed) is the definitive proof of ownership",
        "uniqueFeature": "Mexico's Restricted Zone (zona restringida) covers all land within 50km of the coast and 100km of international borders. Foreigners cannot directly own property in this zone but can purchase through a fideicomiso (bank trust), where a Mexican bank holds the title on behalf of the foreign buyer while giving them full rights of use, enjoyment, and sale. The trust costs approximately $500 USD/year plus setup fees",
        "govSupport": "INFONAVIT is Mexico's largest housing finance institution, funded by mandatory employer contributions (5% of salary). Workers can use their INFONAVIT balance for a deposit or combine it with bank financing. FOVISSSTE provides similar benefits for government employees. Both offer below-market rates for qualifying buyers. The Cofinavit programme combines INFONAVIT credits with bank mortgages for higher-value properties",
        "terms": "Up to 20-30 years, with 15-20 year terms most common",
        "ltv": "Typically 70-80% through commercial banks, up to 90% through INFONAVIT for qualifying properties",
        "keyLenders": "BBVA México (largest mortgage lender), Banorte, Santander México, HSBC México, Scotiabank México, INFONAVIT, and FOVISSSTE",
        "buyingCosts": "6-10% including ISAI, notary fees, registry fees, appraisal, and agent commission (typically 3-6% paid by seller)",
        "inspectionNote": "Professional building inspections are not standard practice in Mexico. Buyers should independently verify construction quality, check for structural issues (especially seismic damage history in earthquake zones), and confirm all construction permits and municipal approvals are in order",
        "foreignBuyer": "Foreigners can buy property directly outside the Restricted Zone. In the Restricted Zone (coast/border), a fideicomiso (bank trust) is required — this gives full beneficial ownership rights for renewable 50-year terms. Mexican corporations with foreign shareholders can also hold property"
    },
    "netherlands": {
        "name": "Netherlands", "iso": "NL", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Amsterdam, Rotterdam, The Hague, Utrecht, and Eindhoven",
        "priceRange": "€250,000 for apartments outside the Randstad to €500,000+ in Amsterdam",
        "deposit": "0% (100% financing available, but savings for costs needed)",
        "transferTax": "Overdrachtsbelasting (transfer tax) is 2% for primary residences. First-time buyers aged 18-35 purchasing properties up to €510,000 (2026 threshold) are exempt. Investment properties are taxed at 10.4%",
        "agentTerm": "buying agent (aankoopmakelaar) — highly recommended in the competitive Dutch market",
        "lawyerTerm": "civil-law notary (notaris)",
        "legalProcess": "The process starts with a written offer. Once accepted, the koopovereenkomst (purchase agreement) is signed, and the buyer has a 3-day statutory cooling-off period. A notary handles the transfer, mortgage registration, and key handover. The buyer typically engages an aankoopmakelaar (buying agent) to negotiate on their behalf, as the seller's agent represents the seller's interests",
        "uniqueFeature": "The Netherlands is one of the few countries where 100% mortgage financing is standard — Dutch banks routinely offer loans covering the full purchase price. However, buyers must fund the additional costs (notary, transfer tax, valuation) from savings. Dutch mortgage interest is tax-deductible (hypotheekrenteaftrek), which historically made buying very attractive, though the deduction rate is being gradually reduced",
        "govSupport": "First-time buyers aged 18-35 are exempt from transfer tax on properties up to €510,000 (adjusted annually). The National Mortgage Guarantee (NHG) provides a government-backed guarantee for mortgages up to €435,000 (2026), offering lower interest rates (typically 0.3-0.6% discount) and protection against residual debt if the property must be sold at a loss. NHG costs 0.6% of the mortgage amount",
        "terms": "Up to 30 years, with full repayment required over the term to qualify for interest deductibility",
        "ltv": "Up to 100% of the property value, but not above the appraised value. NHG loans cap at €435,000. Additional costs (typically 4-6%) must come from savings",
        "keyLenders": "ABN AMRO, ING, Rabobank, ASN Bank, Obvion (Rabobank subsidiary), and various insurance company lenders like Aegon and Nationale-Nederlanden",
        "buyingCosts": "4-6% including transfer tax (0-2%), notary fees, valuation, and buying agent commission",
        "inspectionNote": "A bouwkundige keuring (structural building inspection) is strongly recommended and increasingly required by mortgage lenders. The inspector produces a detailed report on the property's condition and estimated maintenance costs. For apartments, review the VvE (homeowners' association) maintenance plan and reserve fund",
        "foreignBuyer": "No restrictions on foreign property ownership in the Netherlands. Non-residents can obtain Dutch mortgages, though options are more limited. Some international banks like ING and ABN AMRO have dedicated non-resident mortgage programmes"
    },
    "new-zealand": {
        "name": "New Zealand", "iso": "NZ", "currency": "NZD", "symbol": "$",
        "centralBank": "Reserve Bank of New Zealand",
        "cities": "Auckland, Wellington, Christchurch, Hamilton, and Tauranga",
        "priceRange": "$500,000 for properties in regional areas to $1,000,000+ in central Auckland",
        "deposit": "20% standard, 5% minimum with low-deposit schemes",
        "transferTax": "No stamp duty or transfer tax in New Zealand — one of the major cost advantages for buyers",
        "agentTerm": "real estate agent (licensed under the REAA)",
        "lawyerTerm": "solicitor or conveyancer",
        "legalProcess": "New Zealand uses a conditional offer system. The buyer submits a Sale and Purchase Agreement with conditions (typically finance, building inspection, LIM report, and due diligence). Once conditions are met, the agreement becomes unconditional. The solicitor handles title searches, settlement, and registration with Land Information New Zealand (LINZ). Settlement is typically 20-30 working days",
        "uniqueFeature": "New Zealand abolished stamp duty decades ago, making it one of the few developed markets with zero transfer taxes. The market is highly influenced by the RBNZ's LVR (loan-to-value ratio) restrictions, which limit the percentage of high-LVR lending banks can do. The Bright-line test taxes capital gains on investment properties sold within specified holding periods",
        "govSupport": "First Home Grants provide up to $5,000 per person ($10,000 for couples) toward new builds and $3,000 per person for existing homes, for buyers meeting income and house price caps. KiwiSaver first-home withdrawal allows accessing your KiwiSaver retirement savings for a deposit. The First Home Loan scheme (formerly Welcome Home Loan) enables 5% deposits through participating lenders with underwriting support from Kāinga Ora",
        "terms": "Up to 30 years, with 25-30 year terms most common",
        "ltv": "Standard 80% LTV. First-home buyers may access 90-95% LTV through the First Home Loan scheme. RBNZ imposes speed limits on the percentage of high-LVR lending each bank can do",
        "keyLenders": "ANZ, ASB, BNZ, Westpac, Kiwibank (state-owned), plus SBS Bank and TSB Bank",
        "buyingCosts": "2-4% including solicitor/conveyancer fees, building inspection, LIM report, and moving costs. No stamp duty",
        "inspectionNote": "Building inspections are standard and highly recommended. A LIM (Land Information Memorandum) report from the local council reveals resource consents, building permits, hazard zones, and rates. Moisture testing is particularly important in New Zealand due to the leaky building crisis that affected homes built between 1994 and 2004",
        "foreignBuyer": "The Overseas Investment Act heavily restricts foreign buyers. Most non-residents and non-citizens cannot buy existing residential properties. Exceptions exist for Australian and Singaporean citizens (free trade agreements), new build apartments in large developments, and holders of specific visa types with residency pathways"
    },
    "norway": {
        "name": "Norway", "iso": "NO", "currency": "NOK", "symbol": "kr",
        "centralBank": "Norges Bank",
        "cities": "Oslo, Bergen, Trondheim, Stavanger, and Tromsø",
        "priceRange": "kr 2,000,000 for apartments outside major cities to kr 5,000,000+ in central Oslo",
        "deposit": "15% minimum (regulatory requirement)",
        "transferTax": "Dokumentavgift (document duty) is 2.5% of the property's market value. First-time buyers and co-op (borettslag) purchases are exempt from this tax",
        "agentTerm": "estate agent (eiendomsmegler)",
        "lawyerTerm": "the estate agent handles legal aspects (lawyers are optional but available)",
        "legalProcess": "Norwegian property sales are well-regulated. The seller's agent arranges viewings and an open bidding process (budrunde) — bidding is transparent, with all bids logged and available to other bidders. The buyer must allow 24 hours for the seller to consider each bid. Once accepted, the purchase is binding. The megler (agent) handles the contract, payment transfer through a client account, and registration with the Kartverket (land registry)",
        "uniqueFeature": "Norway's bidding process (budrunde) is uniquely transparent — all bids, including amounts and bidder identities, are recorded and made available to competing bidders. This prevents hidden bidding wars common in other markets. Norway also has a high rate of cooperative housing (borettslag), where you buy a share in the housing cooperative rather than the physical unit, which has different legal and tax implications",
        "govSupport": "Norway has limited direct buyer subsidies. First-time buyers are exempt from the 2.5% document duty. Husbanken (the Norwegian State Housing Bank) provides start loans (startlån) for buyers who cannot obtain conventional financing — typically young buyers, single parents, or those with low income. BSU (boligsparing for ungdom) was a tax-advantaged savings scheme for young buyers that offered a 20% tax deduction on savings up to kr 27,500/year",
        "terms": "Up to 30 years, though 25 years is standard",
        "ltv": "Maximum 85% (Norwegian Financial Supervisory Authority regulation). In Oslo, a stricter 60% LTV applies to secondary/investment properties. Minimum 15% equity required for all purchases",
        "keyLenders": "DNB (largest), Nordea, SpareBank 1, Handelsbanken, Danske Bank, and various local savings banks (sparebanker)",
        "buyingCosts": "3-6% including document duty (2.5%, exempt for first-time buyers and borettslag), agent fees (paid by seller), and minor legal/registration costs",
        "inspectionNote": "The seller provides a tilstandsrapport (condition report) prepared by a certified building inspector. Buyers can also commission their own inspection. Norwegian law provides a 5-year warranty period on property defects through the avhendingslova (Property Sales Act), which was strengthened in 2022 to eliminate 'as-is' sales",
        "foreignBuyer": "No restrictions on foreign property ownership in Norway. Non-residents can buy freely but obtaining a Norwegian mortgage typically requires Norwegian income or substantial assets. Some banks offer mortgages to Nordic residents"
    },
    "portugal": {
        "name": "Portugal", "iso": "PT", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Lisbon, Porto, Faro (Algarve), Braga, and Funchal (Madeira)",
        "priceRange": "€100,000 for apartments in interior regions to €400,000+ in Lisbon and prime Algarve locations",
        "deposit": "10-30%",
        "transferTax": "IMT (Imposto Municipal sobre Transmissões Onerosas de Imóveis) ranges from 0% to 8% on a sliding scale based on property value and whether it is a primary or secondary residence. Primary residences up to €101,917 are IMT-exempt. Stamp duty (Imposto do Selo) adds a flat 0.8%",
        "agentTerm": "estate agent (agente imobiliário, licensed with AMI number)",
        "lawyerTerm": "lawyer (advogado) and notary (notário) — both typically involved",
        "legalProcess": "After negotiation, the buyer and seller sign a Contrato Promessa de Compra e Venda (promissory contract) with a 10-30% deposit. The buyer's lawyer conducts title checks through the Land Registry (Conservatória do Registo Predial) and tax authority. The final deed (escritura) is signed before a notary or at a Casa Pronta (one-stop property transaction office). Registration with the land registry completes the transfer",
        "uniqueFeature": "Portugal became one of Europe's hottest property markets partly due to the Golden Visa programme, which offered residency permits to property investors. While the programme ended for real estate investment in 2023, its legacy boosted prices particularly in Lisbon, Porto, and the Algarve. The Non-Habitual Resident (NHR) tax regime, which offered tax benefits to new residents, has also been reformed",
        "govSupport": "First-time buyers under 35 are exempt from IMT on properties up to a certain value threshold. The government provides affordable housing programmes through IHRU (Instituto da Habitação e da Reabilitação Urbana). Young buyers may access bonificação do juro (interest subsidy) on mortgages. Some municipalities offer reduced IMT rates or property tax exemptions for primary residences for initial years",
        "terms": "Up to 40 years for borrowers under 30, 37 years for ages 30-35, and 35 years for over 35 (Bank of Portugal recommendation)",
        "ltv": "Up to 90% for primary residences and 80% for secondary/investment properties (Bank of Portugal recommendation). Non-residents typically limited to 70-80%",
        "keyLenders": "Caixa Geral de Depósitos (state-owned, largest), Millennium BCP, Novo Banco, Santander Totta, BPI (CaixaBank group), and Bankinter",
        "buyingCosts": "6-10% including IMT (0-8%), stamp duty (0.8%), notary/lawyer fees, and registration costs",
        "inspectionNote": "Professional building inspections are not a standard requirement but are strongly recommended, especially for older buildings which may have structural issues, outdated electrical systems, or asbestos. The Caderneta Predial (property booklet from tax authority) and Certidão do Registo Predial (land registry certificate) are essential verification documents",
        "foreignBuyer": "No restrictions on foreign property ownership in Portugal. The country actively welcomes foreign buyers. NIF (Número de Identificação Fiscal) is required for any property transaction. Non-EU buyers may appoint a fiscal representative. Portuguese banks offer mortgages to non-residents, typically at 60-70% LTV"
    },
    "saudi-arabia": {
        "name": "Saudi Arabia", "iso": "SA", "currency": "SAR", "symbol": "ر.س",
        "centralBank": "Saudi Central Bank",
        "cities": "Riyadh, Jeddah, Dammam, Mecca, and Medina",
        "priceRange": "SAR 500,000 for apartments in secondary cities to SAR 2,000,000+ in premium Riyadh and Jeddah locations",
        "deposit": "10-30%",
        "transferTax": "Real estate transaction tax (RETT) of 5% replaced the 15% VAT on property sales in 2020, significantly reducing transaction costs",
        "agentTerm": "real estate broker (licensed with Ejar platform)",
        "lawyerTerm": "lawyer (محامي) — increasingly common though not mandatory",
        "legalProcess": "Property transactions are registered through the Ministry of Justice's electronic system. The buyer and seller attend the notary court (كتابة العدل) to execute the transfer deed, or complete the process electronically through the Nafaz platform. Title verification is done through the Ifragh electronic system. Payment is often handled through escrow via the Wafi platform for off-plan purchases",
        "uniqueFeature": "Saudi Arabia's property market is undergoing massive transformation under Vision 2030, with mega-projects like NEOM, The Line, Jeddah Tower, and Diriyah Gate creating entirely new urban areas. The kingdom introduced mortgage lending relatively recently through the Real Estate Development Fund (REDF), and home ownership has grown rapidly from around 47% to over 60% in recent years",
        "govSupport": "Sakani (سكني) is the government's primary housing programme, offering subsidised housing products, free land (through the Ministry of Housing), and interest-free mortgage support through the Real Estate Development Fund (REDF). REDF provides profit-free financing up to SAR 500,000 for eligible Saudi citizens. The programme targets Saudi nationals only and has supported hundreds of thousands of families since its expansion",
        "terms": "Up to 25-30 years through conventional and Islamic financing",
        "ltv": "Up to 90% for primary residences with REDF support, typically 70-85% through commercial banks",
        "keyLenders": "Saudi National Bank (SNB), Al Rajhi Bank, Riyad Bank, Banque Saudi Fransi, Saudi Awwal Bank (SAB), and the Real Estate Development Fund (REDF)",
        "buyingCosts": "6-8% including RETT (5%), agency fees, and legal/registration costs",
        "inspectionNote": "Professional building inspections are becoming more common but are not standard. For off-plan purchases (common in Saudi Arabia), buyers should verify the developer's registration with Wafi and review the escrow account arrangements. The Saudi Building Code sets construction standards that should be verified for new builds",
        "foreignBuyer": "The 2021 property ownership reforms allow foreign residents to purchase property for personal use with approval from the Ministry of Investment. GCC nationals can own property more freely. Foreign ownership is still restricted in Mecca and Medina. The Premium Residency visa programme allows holders to own property"
    },
    "singapore": {
        "name": "Singapore", "iso": "SG", "currency": "SGD", "symbol": "$",
        "centralBank": "Monetary Authority of Singapore",
        "cities": "Singapore is a city-state — key areas include Central Business District, Orchard, Marine Parade, Bukit Timah, and Jurong",
        "priceRange": "$400,000 for HDB resale flats to $1,500,000+ for private condominiums, with landed property exceeding $5,000,000",
        "deposit": "25% minimum (5% cash, 20% can come from CPF)",
        "transferTax": "Buyer's Stamp Duty (BSD) ranges from 1% to 6% on a sliding scale. Additional Buyer's Stamp Duty (ABSD) applies: 0% for first-time Singapore Citizens on HDB, 20% for second property, 30% for third+. Permanent Residents pay 5% ABSD on first property, foreigners pay 60% ABSD",
        "agentTerm": "property agent (registered with CEA — Council for Estate Agencies)",
        "lawyerTerm": "conveyancing lawyer",
        "legalProcess": "For HDB resale: the buyer and seller register the transaction on the HDB Resale Portal, exercise the Option to Purchase (OTP) within 21 days, and complete the resale application. For private property: the buyer exercises the OTP (paying 5% option fee then 20% within 14 days) and the conveyancing lawyer handles legal completion. HDB completion takes about 8 weeks, private sales about 8-12 weeks",
        "uniqueFeature": "Singapore has a unique dual-market system. About 80% of the population lives in HDB (Housing Development Board) public housing, which can only be purchased by Singapore Citizens (and PRs for resale). The private market includes condominiums, landed houses, and executive condominiums. HDB flats have a 99-year lease from the government and come with ethnic integration quotas and minimum occupation periods",
        "govSupport": "CPF Housing Grants provide up to $80,000 for eligible first-time buyers of HDB resale flats (Enhanced CPF Housing Grant). The Step-Up CPF Housing Grant provides $15,000 for second-timer families moving to a larger flat. BTO (Build-To-Order) flats are sold directly by HDB at subsidised prices, often 20-30% below market value. CPF (Central Provident Fund) savings can be used for deposits and monthly mortgage payments",
        "terms": "Up to 25 years for HDB loans, 30-35 years for bank loans (capped at age 65 for HDB, no hard cap for bank but TDSR applies)",
        "ltv": "75% for bank loans (first property), 45% for second property. HDB loans offer up to 80% LTV. TDSR (Total Debt Servicing Ratio) caps total debt repayments at 55% of gross monthly income",
        "keyLenders": "DBS, OCBC, UOB (the three local banks dominate), plus HSBC, Standard Chartered, Maybank, and HDB (for HDB Concessionary Loans to eligible buyers)",
        "buyingCosts": "4-8% for citizens buying first property (BSD only), dramatically higher for foreigners due to 60% ABSD. Plus legal fees, valuation, and agent commission (1-2%)",
        "inspectionNote": "For resale HDB and private properties, engage a professional inspector to check for structural defects, water leaks, and electrical issues. For new condominiums, a defect inspection should be done during the Defects Liability Period (typically 12 months from completion). Check the building's sinking fund and maintenance fee history for condominiums",
        "foreignBuyer": "Foreigners can buy private condominiums and apartments freely but pay 60% ABSD. Landed property (houses, bungalows) requires approval from the Land Dealings Approval Unit. Foreigners cannot buy HDB flats. Sentosa Cove is the only area where foreigners can buy landed property without special approval"
    },
    "south-africa": {
        "name": "South Africa", "iso": "ZA", "currency": "ZAR", "symbol": "R",
        "centralBank": "South African Reserve Bank",
        "cities": "Johannesburg, Cape Town, Durban, Pretoria, and Port Elizabeth",
        "priceRange": "R800,000 for properties in smaller cities to R3,000,000+ in premium Cape Town and Johannesburg suburbs",
        "deposit": "0-20% (100% bonds available for qualifying buyers)",
        "transferTax": "Transfer duty is progressive: 0% on properties up to R1,100,000, then 3% to 13% on a sliding scale above that. Properties below R1,100,000 are transfer-duty-free, benefiting first-time buyers",
        "agentTerm": "estate agent (registered with the PPRA — Property Practitioners Regulatory Authority)",
        "lawyerTerm": "conveyancing attorney (transferring attorney)",
        "legalProcess": "After the offer to purchase is signed by both parties, the buyer arranges financing and the seller appoints a conveyancing attorney to handle the transfer. The attorney conducts a title deed search at the Deeds Office, obtains rates clearance and compliance certificates (electrical, plumbing, gas, beetle, electric fence), and registers the transfer. The process typically takes 8-12 weeks",
        "uniqueFeature": "South Africa has a relatively accessible property market with 100% home loan bonds available from most banks for qualifying buyers, meaning zero deposit needed. The market also has a strong tradition of sectional title (apartment/complex) ownership governed by the Sectional Titles Schemes Management Act, and community scheme levies are a significant ongoing cost",
        "govSupport": "The FLISP (Finance Linked Individual Subsidy Programme) provides a once-off subsidy of R30,001 to R130,505 for first-time buyers earning between R3,501 and R22,000 per month. The subsidy helps cover the deposit gap. Transfer duty exemption on properties below R1,100,000 effectively serves as first-time buyer relief. The National Housing Finance Corporation provides wholesale lending to expand housing finance access",
        "terms": "Up to 30 years, with 20-year terms most common",
        "ltv": "Up to 100% from most major banks for well-qualified borrowers. First-time buyers with good credit profiles frequently obtain 100% bonds",
        "keyLenders": "Standard Bank, Absa, FNB (First National Bank), Nedbank, Capitec Bank, and SA Home Loans",
        "buyingCosts": "3-8% including transfer duty (0-13%), conveyancing fees, bond registration fees, and rates/levies clearance",
        "inspectionNote": "Several compliance certificates are mandatory for property sales in South Africa: electrical, plumbing, gas (if applicable), beetle/wood borer, and electric fence. These are the seller's responsibility. Buyers should additionally commission a structural inspection, particularly for older properties",
        "foreignBuyer": "No restrictions on foreign property ownership in South Africa. Foreign buyers can obtain mortgages from South African banks, typically up to 50% LTV, subject to Reserve Bank approval and compliance with exchange control regulations"
    },
    "spain": {
        "name": "Spain", "iso": "ES", "currency": "EUR", "symbol": "€",
        "centralBank": "European Central Bank",
        "cities": "Madrid, Barcelona, Valencia, Seville, Málaga, and Palma de Mallorca",
        "priceRange": "€80,000 for properties in inland Spain to €400,000+ in Madrid, Barcelona, and coastal premium areas",
        "deposit": "20-30%",
        "transferTax": "ITP (Impuesto de Transmisiones Patrimoniales) ranges from 6% to 10% depending on the autonomous community for resale properties. New builds attract 10% IVA (VAT) plus 0.5-1.5% AJD (stamp duty). The Canary Islands have reduced rates",
        "agentTerm": "estate agent (agente inmobiliario or API — Agente de la Propiedad Inmobiliaria)",
        "lawyerTerm": "lawyer (abogado) and notary (notario)",
        "legalProcess": "After agreeing terms, the buyer signs a contrato de arras (reservation contract) paying a 10% deposit. If the buyer withdraws, they forfeit the deposit; if the seller withdraws, they must return double. The abogado conducts nota simple (land registry check), verifies debts and community charges, and checks municipal planning status. The escritura de compraventa (deed of sale) is signed before a notary, who registers the transfer",
        "uniqueFeature": "Spain has 17 autonomous communities, each with different tax rates and some with unique property laws. The Balearic and Canary Islands, Valencia, Andalucía, and Catalonia all have distinct tax regimes. Spain also has significant legacy issues with illegal constructions — particularly in rural and coastal areas — where properties were built without proper licences, making legal due diligence critical",
        "govSupport": "Limited national-level subsidies exist, but individual autonomous communities offer programmes. Some regions reduce ITP for first-time buyers, young buyers (under 32-35), or purchases in rural depopulation areas. The ICO (Instituto de Crédito Oficial) has introduced guarantee schemes allowing first-time buyers to access mortgages with lower deposits. Valencia and Andalucía offer reduced transfer tax rates for lower-value properties",
        "terms": "Up to 30 years, with maximum borrower age of 75 at maturity",
        "ltv": "Typically 70-80% for residents, 50-70% for non-residents. Some banks offer up to 90% for young first-time buyers",
        "keyLenders": "CaixaBank (largest), Santander, BBVA, Bankinter, Sabadell, Unicaja, and Kutxabank",
        "buyingCosts": "10-15% including ITP/IVA (6-10%), notary fees (~0.5%), land registry (~0.3%), lawyer fees (1%), and agent commission (typically paid by seller)",
        "inspectionNote": "Professional building surveys are not standard practice in Spain but are strongly recommended, particularly for resale properties and rural fincas. Verify the nota simple from the land registry to confirm ownership, charges, and boundaries. Check the ITE (Inspección Técnica de Edificios) report for apartment buildings over 50 years old. The Certificado de Eficiencia Energética (energy certificate) is mandatory for sales",
        "foreignBuyer": "No restrictions on foreign property ownership in Spain. Foreigners need a NIE (Número de Identidad de Extranjero) for any property transaction. Spanish banks offer mortgages to non-residents, typically at 50-70% LTV. Golden Visa options exist for investments over €500,000"
    },
    "sweden": {
        "name": "Sweden", "iso": "SE", "currency": "SEK", "symbol": "kr",
        "centralBank": "Sveriges Riksbank",
        "cities": "Stockholm, Gothenburg, Malmö, Uppsala, and Linköping",
        "priceRange": "kr 1,500,000 for apartments outside major cities to kr 5,000,000+ in central Stockholm",
        "deposit": "15% minimum (regulatory requirement)",
        "transferTax": "Lagfart (registration fee) is 1.5% of the purchase price for individuals (4.25% for legal entities) plus a fixed administrative fee. Mortgage registration (pantbrev) costs 2% of new mortgage amounts — but existing pantbrev registered to the property transfer free",
        "agentTerm": "estate agent (fastighetsmäklare — legally neutral, representing neither party exclusively)",
        "lawyerTerm": "the estate agent handles the legal process (lawyers are optional)",
        "legalProcess": "Sweden's system is unique in that the estate agent is legally required to be neutral — representing neither buyer nor seller exclusively. Bidding is typically done through the agent, though Swedish bidding is not legally binding until the contract is signed. After agreeing on price, the buyer and seller sign the köpekontrakt (purchase contract) and the buyer pays a deposit (typically 10%). The tillträdesdag (access day) is when keys are handed over and the balance is paid",
        "uniqueFeature": "Sweden has a large bostadsrätt (cooperative housing) market, particularly in cities. When you buy a bostadsrätt, you are purchasing shares in a housing cooperative that grant the right to occupy a specific apartment — not the apartment itself. The cooperative charges a monthly fee (avgift) covering building maintenance, heating, and often water. This fee can be substantial (kr 3,000-8,000/month) and should be factored into affordability calculations",
        "govSupport": "Sweden currently has limited direct buyer subsidies. The government introduced amortisation requirements in 2016 and 2018 — borrowers must repay at least 1% of the loan annually if LTV exceeds 50%, and 2% if LTV exceeds 70%. A further 1% amortisation is required if the loan exceeds 4.5x gross income. These rules, while not subsidies, fundamentally shape the buying landscape. Some municipalities offer discounted land for new construction",
        "terms": "Mortgages have no fixed end date in Sweden — technically they can be interest-only indefinitely, though amortisation requirements now mandate regular repayment. Rate fixing is typically for 1-5 year periods, with 3-month variable rates also popular",
        "ltv": "Maximum 85% (Finansinspektionen regulation). Minimum 15% cash deposit required. Mandatory amortisation above 50% LTV",
        "keyLenders": "Swedbank, SEB, Handelsbanken, Nordea, Danske Bank, Länsförsäkringar, and SBAB (government-owned)",
        "buyingCosts": "3-5% including registration fee (1.5%), mortgage registration (2% on new pantbrev), and agent fees (paid by seller)",
        "inspectionNote": "The buyer bears a significant investigation obligation (undersökningsplikt) under Swedish law — the buyer is expected to thoroughly inspect the property before purchase. A professional besiktning (building inspection) is standard practice and strongly recommended. Defects that could have been discovered through reasonable inspection cannot be claimed against the seller later",
        "foreignBuyer": "No restrictions on foreign property ownership in Sweden. Non-residents can buy freely. Obtaining a Swedish mortgage typically requires Swedish income, a personnummer (personal identity number), and being registered in Sweden"
    },
    "switzerland": {
        "name": "Switzerland", "iso": "CH", "currency": "CHF", "symbol": "CHF",
        "centralBank": "Swiss National Bank",
        "cities": "Zurich, Geneva, Basel, Bern, Lausanne, and Lugano",
        "priceRange": "CHF 400,000 for apartments in smaller cities to CHF 1,500,000+ in Zurich, Geneva, and lakeside locations",
        "deposit": "20% minimum (at least 10% must be non-pension savings)",
        "transferTax": "Property transfer tax varies by canton — from 0% in Zurich and Schwyz to 3.3% in Geneva. Some cantons charge both buyer and seller, others only one party. Many cantons have no transfer tax at all",
        "agentTerm": "estate agent (Immobilienmakler/agent immobilier)",
        "lawyerTerm": "notary (Notar/notaire) — required for the purchase deed in most cantons",
        "legalProcess": "Swiss property purchases must be notarised. The notary drafts and authenticates the purchase contract, conducts land registry checks, and registers the transfer with the Grundbuch (land registry). The process varies by canton — in some cantons (like Zurich) the buyer can choose the notary, while in others the notary is assigned. A pre-contract (Kaufvorvertrag) may be signed with a 10% deposit, followed by the public deed (öffentliche Urkunde)",
        "uniqueFeature": "Switzerland has a unique mortgage culture where homeowners traditionally do not fully repay their mortgages. Banks require amortisation of the second mortgage (the portion between 65-80% LTV) within 15 years or by retirement, but the first mortgage (up to 65% LTV) can be maintained indefinitely, with only interest payments. This is because mortgage interest is tax-deductible and the imputed rental value of owner-occupied property is taxed as income",
        "govSupport": "Pillar 2 (pension fund) and Pillar 3a (private retirement savings) can be used toward the minimum 20% deposit — up to 10% of the property value can come from pension funds, but at least 10% must be genuine equity. Some cantons offer subsidised construction loans or reduced-rate mortgages for families. The federal government has limited direct housing subsidies but promotes cooperative housing",
        "terms": "No fixed term — Swiss mortgages are typically renewed every 2-10 years. The underlying loan can theoretically continue indefinitely for the first mortgage tranche. Fixed-rate periods of 5-10 years are most common",
        "ltv": "Maximum 80% for residential property. The deposit must include at least 10% from non-pension assets. Second mortgage (65-80%) must be amortised within 15 years or by age 65",
        "keyLenders": "UBS, Credit Suisse (now UBS), Raiffeisen, Zürcher Kantonalbank (ZKB), PostFinance, and various cantonal banks (Kantonalbanken)",
        "buyingCosts": "3-5% including notary fees (0.1-1%), land registry (0.1-0.5%), transfer tax (0-3.3% depending on canton), and agent commission (typically paid by seller)",
        "inspectionNote": "Professional building inspections are recommended but not standard. Swiss construction quality is generally very high. Buyers should review the Gebäudeversicherung (building insurance) details, check the Minergie energy rating if applicable, and for apartments review the Stockwerkeigentümergemeinschaft (condominium association) regulations and renovation fund",
        "foreignBuyer": "Foreign buyers face restrictions under the Lex Koller law. Non-Swiss, non-EU/EFTA residents can only buy property with authorisation, which is generally only granted for holiday apartments in designated tourist areas (with size limits). EU/EFTA residents with a Swiss residence permit (B or C) can buy primary residences freely. Swiss citizens and C-permit holders have no restrictions"
    },
    "thailand": {
        "name": "Thailand", "iso": "TH", "currency": "THB", "symbol": "฿",
        "centralBank": "Bank of Thailand",
        "cities": "Bangkok, Chiang Mai, Phuket, Pattaya, and Hua Hin",
        "priceRange": "฿1,500,000 for condominiums in regional cities to ฿5,000,000+ in central Bangkok and premium resort areas",
        "deposit": "10-20%",
        "transferTax": "Transfer fee is 2% (typically split equally between buyer and seller). Specific business tax of 3.3% applies if the property is sold within 5 years. Stamp duty is 0.5% (waived if specific business tax applies). Withholding tax on the seller also affects net proceeds",
        "agentTerm": "real estate agent (agents are not required to be licensed in Thailand)",
        "lawyerTerm": "property lawyer (ทนายความ)",
        "legalProcess": "Property transfers are completed at the local Land Department office. Both parties (or authorised representatives) attend to sign the transfer documents and pay taxes. The buyer receives the Chanote (title deed) — the strongest form of Thai land title. The process is relatively quick once documentation is in order, often completed in a single day at the Land Office",
        "uniqueFeature": "Thailand has strict foreign property ownership laws — foreigners cannot directly own land. However, foreigners can own condominium units freehold, provided foreign ownership in each building does not exceed 49% of the total floor area. For houses and villas, foreigners typically use long-term leasehold arrangements (30+30+30 year leases) or set up Thai companies, though the latter carries legal risks if structured improperly",
        "govSupport": "The Thai government periodically introduces stimulus measures such as reduced transfer fees (from 2% to 0.01%) and mortgage registration fees for properties below certain values. The Government Housing Bank (GH Bank) provides below-market-rate loans for Thai nationals purchasing homes. First-time buyers may access special programmes through GH Bank with reduced rates and lower deposit requirements",
        "terms": "Up to 30 years for Thai nationals through commercial banks, typically 10-15 years through GH Bank programmes",
        "ltv": "Up to 90-100% for first-time buyers purchasing properties below ฿10 million (Bank of Thailand LTV rules). Second mortgages typically capped at 80%, third+ at 70%",
        "keyLenders": "Government Housing Bank (GH Bank), Bangkok Bank, Kasikornbank, Siam Commercial Bank, Krungthai Bank, and TMBThanachart Bank",
        "buyingCosts": "3-6% including transfer fee (2% typically split), stamp duty/SBT, legal fees, and agent commission",
        "inspectionNote": "Professional building inspections are not standard in Thailand. Foreign buyers should engage an independent property lawyer (not the agent's lawyer) to conduct due diligence on the Chanote title deed, verify the 49% foreign ownership quota for condominiums, check construction permits, and review the condominium juristic person's financial status",
        "foreignBuyer": "Foreigners can own condominium freehold (up to 49% foreign quota). Land cannot be owned directly — common alternatives are long-term leases (30-year terms, potentially renewable) or holding through a Thai-majority company. All foreign purchase funds must be remitted from overseas through a Thai bank with a Foreign Exchange Transaction Form (FETF/Thor Tor 3)"
    },
    "uae": {
        "name": "UAE", "iso": "AE", "currency": "AED", "symbol": "د.إ",
        "centralBank": "Central Bank of the UAE",
        "cities": "Dubai, Abu Dhabi, Sharjah, Ajman, and Ras Al Khaimah",
        "priceRange": "AED 500,000 for apartments in emerging areas to AED 3,000,000+ in premium Dubai locations like Palm Jumeirah and Downtown",
        "deposit": "20-25% for residents, 30-50% for non-residents",
        "transferTax": "Dubai charges 4% DLD (Dubai Land Department) transfer fee, split equally between buyer and seller (though negotiable). Abu Dhabi charges 2% registration fee. Oqood registration fee of 4% applies for off-plan properties in Dubai",
        "agentTerm": "real estate agent (registered with RERA — Real Estate Regulatory Agency in Dubai, or DED in other emirates)",
        "lawyerTerm": "property lawyer (not mandatory but recommended, especially for non-residents)",
        "legalProcess": "In Dubai, the process begins with signing a Memorandum of Understanding (MoU/Form F) through the agent. The buyer obtains a No Objection Certificate (NOC) from the developer. The transfer is completed at the Dubai Land Department (DLD) trustee office, where both parties attend and the new title deed is issued. The process is increasingly digital through the Dubai REST app. Abu Dhabi and other emirates have similar but distinct processes",
        "uniqueFeature": "The UAE property market is heavily driven by off-plan sales, with developers offering attractive payment plans — sometimes as low as 1% per month during construction. The market is also unique in being zero-income-tax, which makes property investment attractive for international buyers. Dubai allows 100% foreign freehold ownership in designated areas, a reform that transformed the market from 2002 onwards",
        "govSupport": "The UAE does not have traditional buyer subsidy schemes since there is no income tax. However, the Mohammed bin Rashid Housing Establishment provides housing for UAE nationals in Dubai, and the Abu Dhabi Housing Authority offers similar programmes for Emiratis. The Golden Visa programme provides 10-year residency for property investments of AED 2 million+, adding immigration value to property purchases",
        "terms": "Up to 25 years, with maximum borrower age of 65 (salaried) or 70 (self-employed) at maturity",
        "ltv": "Up to 80% for UAE nationals (first property), 75% for expat residents (first property under AED 5M), and 65-70% for non-residents. Off-plan LTV capped at 50%",
        "keyLenders": "Emirates NBD, Abu Dhabi Commercial Bank (ADCB), Dubai Islamic Bank, Mashreq Bank, HSBC UAE, Standard Chartered UAE, and FAB (First Abu Dhabi Bank)",
        "buyingCosts": "7-9% including DLD transfer fee (4%), agent commission (2%), NOC fee, mortgage registration (0.25%), and trustee fee",
        "inspectionNote": "For ready properties, commission a professional snagging inspection. For off-plan, review the developer's RERA registration and escrow account details. Check the DEWA (Dubai Electricity and Water Authority) connection status and service charges from the community management company. In Dubai, the DLD provides a property verification service",
        "foreignBuyer": "In Dubai, foreigners can buy freehold property in designated areas (most popular areas like Downtown, Marina, JBR, Palm Jumeirah are freehold zones). Abu Dhabi also allows foreign freehold ownership in investment zones. Other emirates have varying rules. Property purchase of AED 750,000+ can qualify for a 2-year resident visa, AED 2M+ for a Golden Visa"
    },
    "united-kingdom": {
        "name": "United Kingdom", "iso": "GB", "currency": "GBP", "symbol": "£",
        "centralBank": "Bank of England",
        "cities": "London, Manchester, Birmingham, Edinburgh, Bristol, Leeds, and Glasgow",
        "priceRange": "£150,000 for properties in northern England and Wales to £500,000+ in London and the South East",
        "deposit": "5-25%",
        "transferTax": "Stamp Duty Land Tax (SDLT) in England/NI: 0% up to £250,000, then 5% to £925,000, 10% to £1.5M, and 12% above. First-time buyers pay 0% up to £425,000 on properties up to £625,000. Scotland has LBTT with different thresholds. Wales has LTT. An additional 3% surcharge applies on second homes across the UK",
        "agentTerm": "estate agent",
        "lawyerTerm": "solicitor or licensed conveyancer",
        "legalProcess": "The buyer makes an offer through the estate agent. Once accepted, both parties instruct solicitors/conveyancers. The buyer's solicitor conducts local authority searches, environmental searches, and reviews the title. Exchange of contracts is when the sale becomes legally binding and the buyer pays a deposit (typically 10%). Completion (when keys are handed over) follows, usually 1-4 weeks after exchange. In Scotland, the process differs — offers are typically submitted after a Home Report and are legally binding once accepted",
        "uniqueFeature": "The UK property market is unique in several ways. England and Wales have no binding agreement until contracts are exchanged, leading to gazumping (seller accepting a higher offer) and gazundering (buyer lowering their offer at the last minute). Scotland's system is more secure with legally binding offers. Leasehold vs freehold ownership is a major distinction — many flats are leasehold with ground rent and service charges. Leasehold reform legislation is ongoing to address unfair practices",
        "govSupport": "First-time buyers receive SDLT relief up to £425,000. The Lifetime ISA provides a 25% government bonus on savings up to £4,000/year for first-time buyers aged 18-39. Shared Ownership allows buying 25-75% of a property and paying rent on the rest. The Mortgage Guarantee Scheme supports 95% LTV mortgages. Help to Buy equity loans ended in 2023 but Shared Ownership remains the primary government scheme. Various Scottish and Welsh programmes also exist",
        "terms": "Up to 40 years, with 25-30 year terms most common",
        "ltv": "Up to 95% with the Mortgage Guarantee Scheme, standard 90% widely available. Higher LTV products may require a higher interest rate. Loan-to-income typically capped at 4-4.5x income",
        "keyLenders": "Nationwide, Barclays, HSBC, NatWest, Santander, Halifax (Lloyds group), Virgin Money, and specialist lenders like Skipton and Leeds Building Society",
        "buyingCosts": "3-8% including SDLT (0-12%), solicitor fees (£1,000-2,000), survey (£300-1,500), and searches (£250-400)",
        "inspectionNote": "Three survey levels are available: a Condition Report (basic), a HomeBuyer Report (mid-level), and a Building Survey (full structural, recommended for older or unusual properties). In Scotland, the seller provides a Home Report including a survey and energy report. A separate mortgage valuation is conducted by the lender. Flood risk, subsidence, and Japanese knotweed are key UK-specific concerns",
        "foreignBuyer": "No restrictions on foreign property ownership in the UK. Non-residents pay a 2% SDLT surcharge on top of standard rates. UK mortgages are available to non-residents through specialist lenders, typically at 65-75% LTV with higher rates"
    },
    "united-states": {
        "name": "United States", "iso": "US", "currency": "USD", "symbol": "$",
        "centralBank": "Federal Reserve",
        "cities": "New York City, Los Angeles, Chicago, Houston, Phoenix, San Francisco, Miami, and Austin",
        "priceRange": "$200,000 in the Midwest and South to $800,000+ in coastal cities and $1,500,000+ in New York and San Francisco",
        "deposit": "3-20%",
        "transferTax": "Varies by state — some states have no transfer tax (e.g. Texas), while others charge 0.1% to 2.5%. Recording fees, title insurance, and other closing costs add to the total",
        "agentTerm": "real estate agent or REALTOR®",
        "lawyerTerm": "real estate attorney (required in some states, optional in others)",
        "legalProcess": "The buyer submits a purchase offer, which becomes a binding contract once the seller accepts. Earnest money (typically 1-3% of the purchase price) is deposited in escrow. The contract includes contingencies for financing, inspection, and appraisal. During the contingency period, the buyer arranges the mortgage and conducts inspections. At closing, a title company or attorney handles document signing, fund disbursement, and title recording. The process typically takes 30-60 days",
        "uniqueFeature": "The US offers 30-year fixed-rate mortgages — a product rare in most other countries. This gives buyers extraordinary payment certainty over three decades. The US also has a unique government-backed mortgage system through Fannie Mae, Freddie Mac, and Ginnie Mae, which buy mortgages from lenders and package them as mortgage-backed securities, enabling widespread 30-year fixed lending. Property taxes are an ongoing annual cost (typically 0.5-2.5% of assessed value) that significantly affects affordability",
        "govSupport": "FHA loans allow as little as 3.5% down payment with government-backed mortgage insurance, aimed at first-time and lower-income buyers. VA loans offer 0% down payment for military veterans and service members. USDA loans provide 0% down payment for rural properties. Conventional loans through Fannie Mae/Freddie Mac allow 3-5% down. First-time buyers can access tax-advantaged savings through state-run programmes and the mortgage interest tax deduction on loans up to $750,000",
        "terms": "15 or 30-year fixed rates are standard. Adjustable-rate mortgages (ARMs) offer lower initial rates fixed for 5, 7, or 10 years before adjusting annually",
        "ltv": "Up to 97% for conventional loans, 96.5% for FHA, 100% for VA and USDA loans. Private Mortgage Insurance (PMI) required for conventional loans above 80% LTV",
        "keyLenders": "United Wholesale Mortgage, Rocket Mortgage (Quicken Loans), Wells Fargo, JPMorgan Chase, Bank of America, loanDepot, and thousands of local banks, credit unions, and mortgage brokers",
        "buyingCosts": "3-6% including title insurance, attorney/escrow fees, appraisal, inspection, recording fees, and transfer tax (if applicable). Some costs may be negotiated to be paid by the seller",
        "inspectionNote": "Professional home inspections are standard and highly recommended. Most contracts include an inspection contingency allowing the buyer to negotiate repairs or withdraw. Inspections cover structure, roof, plumbing, electrical, HVAC, and more. Additional specialised inspections may be needed for radon, termites, mould, lead paint (pre-1978 homes), and septic systems. The appraisal is required by the lender and is separate from the inspection",
        "foreignBuyer": "No federal restrictions on foreign property ownership. Foreign buyers can purchase any property type. Financing is more limited — some US banks offer mortgages to non-residents at 60-70% LTV with higher rates. FIRPTA (Foreign Investment in Real Property Tax Act) requires withholding of 15% of the gross sale price when foreigners sell US property, applied against any capital gains tax owed"
    }
}

GUIDE_TEMPLATE = """---
title: "Complete Property Buying Guide — {name}"
country: "{code}"
slug: "property-buying-guide"
type: "property-buying"
metaTitle: "How to Buy Property in {name} 2026 | Complete Guide"
metaDescription: "Step-by-step guide to buying property in {name}. Covers budgeting, financing, legal process, taxes, and settlement in {name}."
primaryKeyword: "buying property {name}"
secondaryKeywords:
  - "how to buy a house in {name}"
  - "{name} real estate guide"
  - "{name} property market"
  - "{name} property tax"
publishDate: 2026-07-10
lastUpdated: 2026-08-18
wordCount: 1200
faqs:
  - question: "How much deposit do I need to buy property in {name}?"
    answer: "Most lenders in {name} require a deposit of {deposit} of the property price. {depositExtra}"
  - question: "What are the costs of buying property in {name}?"
    answer: "Beyond the purchase price, budget for {buyingCosts} on top of the purchase price. {transferTaxShort}"
  - question: "Can foreigners buy property in {name}?"
    answer: "{foreignBuyer}"
relatedBlogs:
  - "first-home-buyer-guide"
  - "buying-costs-explained"
  - "property-inspection-checklist"
published: true
---

## Understanding the {name} Property Market

{marketOverview}

The {centralBank} sets the benchmark interest rate, which influences mortgage pricing across all lenders. Use our [mortgage calculator](/calculator/?country={isoLower}) to estimate repayments based on current rates.

## Property Prices and Key Markets

Typical prices in {name} range from {priceRange}.

{uniqueFeatureDetail}

## Setting Your Budget

{budgetSection}

{transferTaxDetail}

Read our [buying costs guide](/{code}/blog/buying-costs-explained/) for a detailed breakdown of all purchase-related expenses.

## Getting Finance Approved

{financeSection}

Compare rates across major lenders including {keyLenders}. Our [mortgage types guide](/{code}/blog/mortgage-types-compared/) explains the differences between available loan products.

## Finding and Securing Property

{searchSection}

## Legal Process and Due Diligence

{legalDetail}

{inspectionNote}

See our [property inspection checklist](/{code}/blog/property-inspection-checklist/) for what to check before committing.

## Government Support for Buyers

{govSupportDetail}

Check our [government grants guide](/{code}/blog/government-grants-schemes/) for the latest programmes and eligibility criteria.

## Next Steps

Use our [mortgage calculator](/calculator/?country={isoLower}) to model different scenarios, browse [{name} FAQs](/{code}/faqs/) for quick answers, or read our [complete mortgage guide](/{code}/mortgage-guide/) for detailed information on rates and lenders.
"""

import os

def generate_guide(code, data):
    iso_lower = data["iso"].lower()

    # Build dynamic sections
    market_overview = f"The property market in {data['name']} offers diverse opportunities across its key markets. {data['cities']} represent the main buying hotspots, with prices and demand varying significantly between regions."

    unique_detail = data["uniqueFeature"]

    budget_section = f"Beyond the purchase price, you need to budget for transaction costs that typically add {data['buyingCosts']} to the total. Your deposit requirement is {data['deposit']}, though this varies by lender and your buyer profile."

    transfer_detail = data["transferTax"]

    terms_clean = data['terms'].lstrip('Uu').lstrip('p to ') if data['terms'].lower().startswith('up to') else data['terms']
    ltv_clean = data['ltv'].lstrip('Uu').lstrip('p to ') if data['ltv'].lower().startswith('up to') else data['ltv']
    finance_section = f"Mortgage terms in {data['name']} extend up to {terms_clean}. Lenders typically offer up to {ltv_clean} loan-to-value, meaning you need at least the remainder as a deposit."

    search_section = f"Working with a qualified {data['agentTerm']} is the standard approach in {data['name']}. Research local areas thoroughly, attend viewings, and consider factors like transport links, amenities, and future development plans."

    legal_detail = f"Property transfers in {data['name']} require a qualified {data['lawyerTerm']} to handle the legal process. {data['legalProcess']}."

    gov_detail = data["govSupport"]

    deposit_extra = ""
    if "100%" in data.get("ltv", ""):
        deposit_extra = "Some lenders offer up to 100% financing for qualifying buyers."
    elif "90%" in data.get("ltv", ""):
        deposit_extra = "First-time buyers may access higher LTV products with lower deposits."

    transfer_short = data["transferTax"].split(".")[0] + "."

    content = GUIDE_TEMPLATE.format(
        name=data["name"],
        code=code,
        iso=data["iso"],
        isoLower=iso_lower,
        centralBank=data["centralBank"],
        cities=data["cities"],
        priceRange=data["priceRange"],
        deposit=data["deposit"],
        depositExtra=deposit_extra,
        transferTax=data["transferTax"],
        transferTaxShort=transfer_short,
        agentTerm=data["agentTerm"],
        lawyerTerm=data["lawyerTerm"],
        legalProcess=data["legalProcess"],
        uniqueShort=data["uniqueFeature"][:80].rsplit(" ", 1)[0],
        uniqueFeature=data["uniqueFeature"],
        uniqueFeatureDetail=unique_detail,
        govSupport=data["govSupport"],
        govSupportDetail=gov_detail,
        terms=data["terms"],
        ltv=data["ltv"],
        keyLenders=data["keyLenders"],
        buyingCosts=data["buyingCosts"],
        inspectionNote=data["inspectionNote"],
        foreignBuyer=data["foreignBuyer"],
        marketOverview=market_overview,
        budgetSection=budget_section,
        transferTaxDetail=transfer_detail,
        financeSection=finance_section,
        searchSection=search_section,
        legalDetail=legal_detail,
        symbol=data["symbol"],
        currency=data["currency"],
    )
    return content


# Generate all guides
REPO_ROOT = "."
GUIDES_DIR = os.path.join(REPO_ROOT, "src", "src", "content", "pillar-guides")
SKIP = {"australia", "south-korea"}  # Already have good content

count = 0
for code, data in sorted(COUNTRIES.items()):
    if code in SKIP:
        continue
    guide_dir = os.path.join(GUIDES_DIR, code)
    guide_path = os.path.join(guide_dir, "property-buying-guide.md")
    if not os.path.exists(guide_dir):
        print(f"⚠ Directory not found: {guide_dir} — skipping")
        continue
    content = generate_guide(code, data)
    with open(guide_path, "w") as f:
        f.write(content)
    word_count = len(content.split())
    count += 1
    print(f"✓ {data['name']}: {word_count} words")

print(f"\n=== {count} property buying guides generated ===")
