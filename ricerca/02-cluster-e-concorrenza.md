# 02 — Cluster e filtro competitivo (Stadio 2)

I 122 segnali di [`01-segnali.md`](01-segnali.md) sono raggruppati in **28 problemi di fondo** (P01–P28). Per ognuno ho cercato attivamente prodotti esistenti con l'obiettivo di **uccidere l'idea**.

Legenda concorrenza (dal metodo originale):

- **A**: nessuna soluzione dedicata trovata
- **B**: soluzioni scarse o datate
- **C**: soluzioni costose
- **D**: soluzioni troppo complesse
- **E**: prodotti forti che risolvono bene (normalmente si scarta)

Etichette usate in tutto il rapporto:

- **[OSSERVATO]**: fatto visto in una fonte citata
- **[IPOTESI]**: mia inferenza non ancora verificata
- **[DA VERIFICARE]**: domanda aperta da chiudere con esperimenti o due diligence

## Osservazione trasversale (importante)

**[OSSERVATO]** Nel 2026 quasi ogni dolore *visibile online* ha già 2–10 micro-prodotti dedicati, spesso lanciati nel giro di settimane da sviluppatori che usano strumenti di coding AI. Esempi verificati durante questa ricerca:

- pulsante di recesso UE: 5+ app Shopify entro giugno 2026
- modello N2 spagnolo: Partee, Chekin, HolaHuesped, DepositoNRUA, n2facil
- fatture ricorrenti Xero: Ratelift, Invoice X
- file `.pub` di Publisher: Univik, PrivConvert, MyPublisherFiles, FreeConvert
- certificati di esenzione su Shopify: Paperwork, Exemptra, ExemptSync
- bundle Etsy: Sumtracker, Shuttle
- refrigeranti EPA: RefriTrak, RefriComply

Inoltre molti post "is there a tool…" su Reddit sono di builder, non di acquirenti.

**Conseguenza per il metodo:** l'esistenza di un micro-concorrente non basta a scartare un'idea (spesso non ha trazione), ma alza il peso di **distribuzione**, **profondità verticale** e **complessità tecnica difendibile**. Ho quindi privilegiato i problemi in cui:

1. la domanda emerge da **utenti indipendenti con engagement** e non da post di builder;
2. gli incumbent sono **sales-led, costosi o generici**;
3. c'è una barriera tecnica o di dominio che scoraggia la copia in un weekend.

## Tabella dei cluster

| # | Problema di fondo | Segnali | Concorrenza trovata | Classe | Esito |
|---|---|---|---|---|---|
| P01 | **MSP: tracciare quali firewall/VPN dei clienti sono esposti ad advisory firmware critici, EOL e licenze scadute** | S53, S69, S103, S120–S122 | VulniPulse (15 $/mese, watchlist manuale, nessuna funzione MSP); Lansweeper (audit CVE, piattaforma generalista); Liongard (firmware/licenze SonicWall-Fortinet, piattaforma MSP ampia); Auvik (lifecycle Cisco); Cisco Software Checker (solo Cisco, manuale); FortiGate security rating (solo Fortinet) | C/D | **TENUTO** |
| P02 | MSP: riconciliare licenze/dispositivi tra RMM, M365/Pax8 e fatturazione | S100, S101 | Gradient Synthesize (gratuito / 99 $ al mese, 80+ vendor), MSPbots, Augmentt | E | Scartato |
| P03 | MSP: eventi Microsoft multi-tenant (Copilot a consumo dal 2/11/2026, fine di EWS) | S99, S102 | Microsoft Cost Management per tenant (budget, alert, cap); Pax8 sta costruendo un pannello Copilot multi-tenant con Microsoft; CIPP (open source) per gli audit | C→E | Tenuto come candidato debole (C8) |
| P04 | **Brand DTC: verificare le fatture 3PL contro il contratto e trovare dove si perde margine su fulfillment/spedizione** | S63, S105–S112 | Implentio (da 1.000 $/mese, sales-led); BillSharp (servizio, solo ShipBob); FreightOptics (sales-led, grandi shipper); Mockly (30% di commissione sui recuperi); progetto open source su GitHub; per la sola spedizione: Bloom Analytics, BeProfit | C | **TENUTO** (C1); sotto-problema "spedizione addebitata vs etichetta" tenuto come C7 |
| P05 | **Micro-produttori di software/firmware nel CRA UE: SBOM, gestione vulnerabilità, segnalazione 24/72h/14g, documentazione** | S01, S115–S119 | Enterprise: ONEKEY, Cybellum, Finite State, Timesys Vigiles (prezzi su richiesta). Gratuiti/economici: Dependency-Track (OSS, self-hosted), Interlynk (free tier), sbomify, EMBA; nuovi: CRAcheck, craevidence, CVD Portal; plugin WordPress CRA gratuiti | C/D (embedded piccolo) – E (WordPress) | **TENUTO** solo per l'embedded piccolo (C3) |
| P06 | Commercialisti: promemoria SMS, scadenze annual report | S19, S27, S28, S59, S60 | CorpNet/Bizee tracciano gratis; TaxDome + Twilio; commenti molto contrari (91 e 50 upvote) | E + contro-evidenza | Scartato |
| P07 | Estrazione K-1/W-2/1099 per piccoli studi fiscali | S29–S32, S93 | K1x (5k $/anno, minimo 250 K-1; 60–75 $ per K-1), SurePrep, GruntWorx (a consumo), Lido (29 $/mese), k1taxsoftware, Juno | C/E | Tenuto come candidato debole (C4) |
| P08 | Estratti conto/fatture PDF → Excel o contabilità | S07, S10, S14, S33 | Decine di convertitori (DocuClipper, BankStatementConverter…), Dext, Hubdoc; Lido | E | Scartato (mercato provato ma saturo) |
| P09 | Modifiche massive mancanti in Xero/QBO | S02, S03, S18, S23 | Ratelift, Invoice X; app di import/export | E | Scartato |
| P10 | Report mensile per il commercialista e IVA da Shopify | S44, S45 | A2X, Link My Books, app di report IVA | E | Scartato |
| P11 | Lacune funzionali Shopify (zone di consegna, Royal Mail, backup, recesso UE, esenzioni) | S43, S46–S48, S50 | App dedicate per ciascun caso (Zapiet, Rewind/Talon, 5+ app di recesso, 3 app di esenzione) | E | Scartato |
| P12 | Inventario multicanale/bundle; dismissione di Stocky | S49, S51, S57, S86 | Sumtracker, Shuttle, 14+ alternative a Stocky; channel manager | E | Scartato (S51 è anche vicino all'idea esclusa sui listini) |
| P13 | Adempimenti host affitti brevi (N2, SES) e conti dei co-host | S36, S37, S39, S85 | Partee, Chekin, HolaHuesped, DepositoNRUA, n2facil; CoHostBooks, MagicBNB; Modello 21 abolito | E | Scartato |
| P14 | Migrazioni forzate (Publisher `.pub`, link Excel, UAD 3.6, cambio fornitore K-12) | S16, S35, S70, S94 | Convertitori `.pub` (5+), CloudFuze/ReplaceMagic, incumbent UAD; uso una tantum | E + one-shot | Scartato |
| P15 | Fatture elettroniche XML illeggibili (Peppol BE, XRechnung DE) | S04, S40 | Viewer gratuito ufficiale ELSTER, molti viewer gratuiti, gestionali | E | Scartato |
| P16 | Registri regolatori IT/UK (RENTRI, MTD ITSA, 770) | S34, S38, S42, S104 | Servizi pubblici gratuiti RENTRI + molti vendor; HMRC ha chiuso a nuovi prodotti MTD 2026-27 | E / barriera | Scartato |
| P17 | Strumenti documentali per piccoli studi legali (oscuramento, proofreading, confronto) | S24–S26, S61, S62 | Adobe Acrobat (redazione per pattern), PerfectIt (70 $ all'anno), Draftable (129 $ all'anno), clausul (249 $ all'anno), DocXtools | E | Scartato |
| P18 | Tracciamento di COI, licenze e crediti formativi | S21, S81, S83 | myCOI, TrackMyVendor, BCS, Jones; Agenzee, AgentSync, RenewOps | E | Scartato |
| P19 | Rendiconti ai proprietari e report per property manager | S05, S06, S84 | Report builder di AppFolio, report personalizzabili di Buildium, molti tool di lease abstraction | E/C | Tenuto come candidato debole (C6) |
| P20 | No-profit: ore per grant, report multi-finanziatore, frodi BEC, check-in eventi | S17, S87–S89 | ClickTime, WeWorked, Hour Timesheet, TimeRewards; Apricot/Bonterra; check-in gratuiti | C/E | Tenuto come candidato debole (C5) |
| P21 | Back-office logistica (claims, RFQ, rate con, eModal, detention, tracking) | S08, S20, S77–S80 | FreightClaims.com (piano per piccoli broker), Claimable; Terminal49, PortPro; ELD/MacroPoint (detention) | C/E + contro-evidenza | Claims tenuto come candidato debole (C10); il resto è scartato |
| P22 | Costruttori: draw del mutuo di costruzione, gare SAM.gov | S75, S76 | Rabbet/Built (lato lender), Buildertrend/JobTread; HigherGov, GovSpend, avvisi SAM gratuiti | C (draw) / E (gare) | Draw tenuto come candidato debole (C9) |
| P23 | Report e monitoraggio per agenzie/PPC/prezzi concorrenti | S12, S58, S64, S65 | Optmyzr, script Google Ads, AgencyAnalytics, Prisync e simili | E | Scartato |
| P24 | Prezzi per utente e strumenti "overkill" per micro-imprese | S15, S22, S66–S68, S74, S90, S91, S113, S114 | Baserow, NocoDB, Grist; TutorBird; Jobber; HACCP digitale… | E | Scartato (ma S113–S114 informano il pricing) |
| P25 | Matching/riconciliazione dati generici in Excel | S09, S11, S13 | Power Query, add-on, CRM | E | Scartato |
| P26 | Questionari di sicurezza, firme email, analisi PCAP | S41, S95, S98 | 10+ tool AI per questionari; Signitic/WiseStamp; tool enterprise | E | Scartato |
| P27 | Recruiting/HR (ATS sovradimensionati, sourcing da LinkedIn, approvazione turni) | S54–S56 | Mercato ATS affollato; rischio di piattaforma LinkedIn | E | Scartato |
| P28 | Nicchie varie (foto per periti, laboratori, Notion, policy assicurative, credito export) | S52, S71–S73, S82, S92, S96, S97 | Funzioni nei software di settore; bassa disponibilità a pagare (lab); dati proprietari (credito) | E/varie | Scartato |

## Riduzione a 10 candidati seri

Il metodo chiede 10–15 candidati. Con la saturazione osservata, solo **3 hanno un varco credibile**. Ho comunque portato avanti altri 7 candidati più deboli, per mostrare perché perdono nei confronti diretti degli Stadi 3–7:

| Codice | Candidato | Da cluster | Cuneo potenziale |
|---|---|---|---|
| **C1** | Audit self-service delle fatture 3PL per brand DTC piccoli | P04 | più economico, self-service, niente commissione o contratto annuale, specifico per brand da 500–10.000 ordini al mese, normalizzazione multi-3PL |
| **C2** | Tracker MSP di advisory, EOL e licenze per dispositivi edge (firewall/VPN) | P01 | multi-tenant MSP, import da RMM/Auvik/CSV, applicabilità consapevole della configurazione, report di evidenze per assicurazione e cliente |
| **C3** | Kit CRA per piccoli team embedded (SBOM bare-metal → vulnerabilità → orologio 24/72h/14g → documentazione) | P05 | specifico per firmware MCU senza package manager, prezzo per piccole aziende, flusso CRA completo, UE/GDPR |
| C4 | Estrazione K-1 per studi a basso volume | P07 | nessun minimo, prezzo a documento, Excel pronto per l'import |
| C5 | No-profit: ore per grant + report multi-finanziatore | P20 | un dataset → N template per finanziatore |
| C6 | Rendiconti personalizzati per property manager a partire dagli export del gestionale | P19 | un formato per proprietario, batch mensile |
| C7 | Monitor della perdita sulle spedizioni (addebitato vs etichetta) per Shopify | P04 | alert per SKU/zona, correzione dei pesi |
| C8 | Spesa Copilot/consumi Microsoft su tutti i tenant di un MSP | P03 | vista aggregata multi-tenant + rifatturazione |
| C9 | Tracker dei draw del mutuo di costruzione per piccoli costruttori | P22 | lato costruttore, budget vs draw vs ispezioni |
| C10 | Gestione claims per piccoli broker merci | P21 | economico, integrato con la posta |

### Nota sulle esclusioni del progetto

Nessuno dei candidati coincide con le tre idee escluse. Per trasparenza segnalo la vicinanza più rilevante:

- **C1 vs idea esclusa n. 1** (confronto listini fornitori con equivalenze di codici e normalizzazione di confezioni). C1 confronta **addebiti di servizi logistici** (storage, pick, spedizione, accessori) con un **contratto di servizio** e con i dati degli ordini. Non confronta listini di prodotti tra fornitori, né equivalenze di codici articolo. Il problema centrale è la verifica di una fatturazione di servizi, non il confronto di prezzi d'acquisto. **[DA VERIFICARE]**: se ritieni che questa distanza non basti, C1 va scartato e il n. 4 sale di posizione.
- **C2/C3 vs idea esclusa n. 2** (verifica di pacchetti di documenti tecnici contro un registro). C2 e C3 confrontano **versioni software** con **advisory di sicurezza**, non file, nomi e revisioni di documenti.
- Nessun candidato riguarda i file di caricamento dei cataloghi Amazon.
