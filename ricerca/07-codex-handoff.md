# 07 — Pacchetti di passaggio alla due diligence tecnica

> **Research funnel complete. I recommend moving these opportunities to Codex technical due diligence.**
>
> In italiano: l'imbuto di ricerca è completo. Raccomando di passare queste tre opportunità alla due diligence tecnica.

**Ambito del passaggio:** la prima fase è **solo DUE DILIGENCE TECNICA**: API, librerie, architettura, dipendenze esterne, blocchi tecnici, hosting, sicurezza, complessità, tempi realistici. **Non** si costruisce l'MVP. La decisione di costruire si prende solo dopo che la due diligence conferma le ipotesi tecniche e, idealmente, dopo gli esperimenti di validazione di `05-top5.md`, che possono girare in parallelo.

> **Aggiornamento della seconda sessione.** Alcune domande aperte qui sotto sono state chiuse con la sola ricerca: vedi [`08-approfondimenti.md`](08-approfondimenti.md).
>
> - Palo Alto pubblica advisory in JSON strutturato e CISA KEV è scaricabile. Fortinet ha un feed RSS e CSAF per singolo advisory; Cisco ha l'API openVuln.
> - **SonicWall non ha un'API pubblica** e la **lista EOS di CISA non è pubblica**. eol.network (92k SKU, API) è una possibile fonte EOL.
> - ShipBob ha una Billing API a livello di spedizione e ShipMonk esporta CSV.
> - La piattaforma ENISA **non ha API** al lancio.
> - Il progetto UE SECURE cofinanzia le PMI CRA fino a 30.000 €.
>
> Codex deve comunque riconfermare questi punti nella due diligence tecnica.

## Verifica delle 10 condizioni del metodo

| Condizione | C2 Advisory edge MSP | C1 Audit 3PL | C3 Kit CRA embedded |
|---|---|---|---|
| 1. Prove credibili del problema | Sì | Sì | Sì |
| 2. Più utenti indipendenti | Sì (thread + commenti + eventi ricorrenti) | Sì (6+ post) | Sì (più thread r/embedded, HN) |
| 3. Concorrenza indagata | Sì | Sì | Sì |
| 4. Cuneo specifico | Sì | Sì | Sì |
| 5. Cliente chiaro | Sì | Sì | Sì |
| 6. MVP descrivibile | Sì | Sì | Sì |
| 7. Monetizzazione plausibile | Sì | Sì | Sì (disponibilità a pagare non provata) |
| 8. Acquisizione iniziale credibile | Sì | Sì | Parziale |
| 9. Nessun rischio fatale noto | Nessuno trovato; responsabilità sui falsi negativi da gestire | Nessuno trovato; dati sensibili | Nessuno trovato; rischio regolatorio e di posizionamento da gestire |
| 10. Tra i primi 1–3 | Sì (#1) | Sì (#2) | Sì (#3) |

**Nota onesta.** Nessuna delle tre ha ancora una prova di **disponibilità a pagare**: nessun pagamento, pre-ordine o LOI osservato. Le condizioni del metodo sono soddisfatte per la due diligence tecnica, non per la costruzione.

---

# 🚦 CODEX HANDOFF — 1) EdgeWatch per MSP (C2)

**THIS OPPORTUNITY IS READY FOR CODEX TECHNICAL VALIDATION.**

- **Opportunity name:** EdgeWatch per MSP *(nome provvisorio)*.
- **Problem:** gli MSP verificano a mano, su Excel, quali firewall e VPN dei clienti sono esposti agli advisory dei vendor, a fine supporto o senza licenza di aggiornamento. Gli RMM registrano la versione ma non la correlano agli advisory; serve anche una prova datata per assicurazioni e clienti.
- **Target user:** MSP con 2–30 tecnici e apparati multi-vendor (Fortinet, SonicWall, WatchGuard, Cisco, Palo Alto, Ubiquiti, MikroTik).
- **Evidence summary:**
  - r/msp 2026-07-23 (spreadsheet universale, confronto di versioni insidioso, prova per l'assicurazione);
  - 13+ thread su advisory edge critici tra 2024 e 2026 (FortiBleed 104 upvote; WatchGuard 34 e 27 upvote);
  - CISA BOD 26-02 (5/2/2026);
  - requisiti assicurativi sugli edge EOL (fonti di parte);
  - tool gratuiti nati da singoli MSP (luglio 2026).
- **Proposed product:** SaaS multi-tenant con import dell'inventario, monitoraggio dei feed ufficiali e di CISA KEV, confronto di versioni per vendor, applicabilità per funzione attiva, stato EOL e licenza, registro delle decisioni, report mensile per cliente.
- **MVP functionality:**
  - import CSV;
  - 6 vendor + KEV;
  - motore di confronto versioni con test;
  - dashboard per cliente;
  - alert email/Slack/Teams;
  - registro delle decisioni;
  - PDF mensile.
- **Important competitor findings:**
  - VulniPulse (15 $/mese, 32 vendor, watchlist manuale, nessuna funzione MSP);
  - Lansweeper (audit CVE, generalista);
  - Liongard (firmware e licenze per alcuni vendor, piattaforma MSP ampia);
  - Auvik (lifecycle Cisco);
  - Cisco Software Checker e FortiGate security rating (vendor singolo).
- **Expected pricing:** 49 / 149 / 299 € al mese per fasce di dispositivi.
- **Distribution thesis:** contatto diretto su r/msp e MSPGeek; pagine SEO programmatiche per vendor e versione aggiornate a ogni advisory; digest gratuito; integrazioni RMM; report al cliente finale con attribuzione.
- **Known technical risks:**
  - feed eterogenei (RSS, JSON, CSAF, HTML);
  - confronto di versioni non semver;
  - applicabilità legata alla configurazione;
  - falsi negativi e responsabilità;
  - limiti e costi delle API RMM.
- **Unknown technical questions:**
  - quali vendor pubblicano CSAF 2.0 o JSON strutturati con intervalli di versione affetti e corretti, con che latenza e licenza d'uso;
  - se si possa ottenere in modo affidabile modello, versione e licenza da NinjaOne, Datto RMM, N-able, Auvik e Domotz via API, e a quali condizioni;
  - se esistano fonti EOL machine-readable per Fortinet, SonicWall e WatchGuard (una issue GitHub segnala record mancanti per 15 vendor edge) e se la lista EOS di CISA sia scaricabile;
  - come rappresentare l'applicabilità condizionale ("vulnerabile solo se SSL-VPN attivo").
- **What Codex needs to verify:**
  1. Inventario delle fonti per i 6 vendor MVP: formato, completezza dei range di versione, termini d'uso, frequenza, presenza di API key.
  2. Fattibilità di un parser e comparatore di versioni per vendor, con un corpus di test di advisory reali (es. FortiOS, SonicOS, Fireware, ASA/FTD, PAN-OS, UniFi).
  3. API RMM e network monitoring: endpoint, scope, permessi, rate limit, costi partner.
  4. Fonti EOL disponibili e strategia di fallback (manuale o curata).
  5. Architettura: job schedulati, idempotenza, audit trail immutabile, multi-tenant con isolamento.
  6. Sicurezza: dati di inventario dei clienti degli MSP, SSO, cifratura, log.
  7. Hosting e costi a 100 / 1.000 / 10.000 MSP.
  8. Stima realistica di MVP e V1 e rischi di manutenzione dei parser.

---

# 🚦 CODEX HANDOFF — 2) Audit self-service delle fatture 3PL (C1)

**THIS OPPORTUNITY IS READY FOR CODEX TECHNICAL VALIDATION.** Vale con la riserva sull'esclusione n. 1 in `02-cluster-e-concorrenza.md`, da confermare con te.

- **Opportunity name:** 3PL Invoice Check *(nome provvisorio)*.
- **Problem:** i brand DTC ricevono fatture 3PL lunghe e codificate con errori ricorrenti (supplementi, storage, pick fee, markup sulle spedizioni). Il controllo è manuale, mensile, spesso affidato a fogli o assistenti, o del tutto assente.
- **Target user:** brand Shopify con 500–10.000 ordini/mese e 1–3 3PL.
- **Evidence summary:** r/ecommerce 2026-01-28 (140 upvote, 44 commenti), 2026-01-05 (errore ricorrente da 300 $), 2025-08-27 (assistente offshore che ricopia le righe ogni mese), 2026-04-07 (~30k $ di scostamento in 2 anni), 2026-02-13; r/shopify 2025-08-27; più builder e un repo open source sullo stesso tema.
- **Proposed product:** SaaS self-service che normalizza fatture (API, CSV, PDF), le confronta con la rate card versionata e con gli ordini Shopify, segnala gli scostamenti con le prove e prepara le contestazioni; storico multi-3PL.
- **MVP functionality:**
  - editor di rate card e template;
  - import da ShipBob Billing API, CSV generico e PDF via estrazione AI con revisione;
  - unione con gli ordini Shopify;
  - 5–6 regole di scostamento;
  - report mensile ed email di contestazione.
- **Important competitor findings:** Implentio (da 1.000 $/mese, sales-led); BillSharp (servizio, solo ShipBob); FreightOptics (sales-led, grandi shipper); Mockly (30% dei recuperi); repo open source su GitHub; Bloom e BeProfit per la sola spedizione.
- **Expected pricing:** 79 / 149 / 299 € al mese; primo audit di 3 mesi gratuito.
- **Distribution thesis:** audit concierge ai brand che espongono il problema; SEO con decoder delle fatture dei 3PL principali; partnership con contabili, fractional CFO e consulenti 3PL; case study con € recuperati.
- **Known technical risks:** eterogeneità dei formati PDF; mancanza di API per molti 3PL; accuratezza e costo dell'estrazione AI; join tra righe fattura e ordini (ID diversi); dati commerciali sensibili.
- **Unknown technical questions:**
  - quali 3PL e WMS diffusi tra i brand piccoli espongono API di billing (ShipBob sì: endpoint invoices/transactions, scope `billing_read`) o export strutturati (Extensiv, ShipHero, ShipMonk, Red Stag…);
  - quanto sia ripetibile la struttura delle fatture generate dallo stesso WMS;
  - precisione dell'estrazione AI su tabelle multipagina e costo per pagina;
  - quali campi d'ordine Shopify servono (peso, dimensioni, articoli) e se sono affidabili.
- **What Codex needs to verify:**
  1. Censimento di API ed export di billing di almeno 6 3PL o WMS rilevanti per i brand piccoli.
  2. Prova di estrazione su fatture campione: accuratezza, costo e casi limite.
  3. Modello dati di rate card versionata e regole di scostamento; fattibilità del join con Shopify.
  4. Requisiti di sicurezza e privacy dei documenti.
  5. Architettura, hosting e costi a 100 / 1.000 / 10.000 brand.
  6. Requisiti per il listing nello Shopify App Store, se serve.
  7. Stima realistica di MVP e V1.

---

# 🚦 CODEX HANDOFF — 3) Kit CRA per piccoli team embedded (C3)

**THIS OPPORTUNITY IS READY FOR CODEX TECHNICAL VALIDATION.** È raccomandato eseguire **in parallelo** l'esperimento di validazione: la disponibilità a pagare è il rischio principale.

- **Opportunity name:** CRA Kit Embedded *(nome provvisorio)*.
- **Problem:** i micro e piccoli produttori di firmware devono, ai sensi del CRA, gestire SBOM, vulnerabilità, segnalazioni 24h/72h/14 giorni (dall'11/9/2026), periodo di supporto e documentazione (dall'11/12/2027). Per i progetti C/CMake senza package manager non hanno un metodo né strumenti economici adatti.
- **Target user:** team firmware con 1–20 sviluppatori che vendono dispositivi connessi nell'UE (STM32, ESP32, nRF, Linux embedded).
- **Evidence summary:** r/embedded 2026-09-07 (31 upvote, 38 commenti: "for stm32 we have no idea", aziende che escono dall'UE), 2026-07-01 (SBOM C/C++, 21 upvote, 20 commenti), 2026-06-02 (regola delle 24h); HN 2026-09-01; r/opensource 2025-07-31 (51 upvote, 41 commenti).
- **Proposed product:** uno strumento a riga di comando, eseguibile in CI, per proporre l'SBOM dai repository firmware C, più una web app per monitoraggio, triage, VEX, orologi di segnalazione, periodo di supporto e documentazione.
- **MVP functionality:** import CycloneDX/SPDX ed editor dei componenti; monitoraggio OSV/NVD; triage ed export VEX; orologio di segnalazione con bozza; registro del periodo di supporto. Lo scanner bare-metal arriva in V1.
- **Important competitor findings:**
  - Dependency-Track (OSS), Interlynk (free tier), sbomify, EMBA;
  - esp-idf ha già un comando SBOM e Yocto produce SPDX;
  - ONEKEY, Cybellum, Finite State, Timesys (enterprise);
  - nuovi entranti CRAcheck, craevidence, CVD Portal, Dojo Five.
- **Expected pricing:** 49–149 € al mese per linea di prodotto, oppure 490–1.490 € all'anno.
- **Distribution thesis:** community embedded; SEO tecnico; generatore SBOM gratuito; partnership con consulenti CRA, organismi notificati ed EDIH.
- **Known technical risks:**
  - identificazione affidabile dei componenti C vendored e delle loro versioni;
  - rumore e lacune di NVD/OSV per le librerie embedded;
  - requisiti formali in evoluzione (norme armonizzate non ancora pubblicate);
  - responsabilità percepita.
- **Unknown technical questions:**
  - con quale precisione si riconoscono lwIP, mbedTLS, FreeRTOS, FatFs, CMSIS e le HAL dei vendor tramite firme, header e macro di versione;
  - se esista un'API o un formato di import per la piattaforma unica di segnalazione ENISA, oppure solo un form web;
  - quali campi richiede ciascuna fase (24h, 72h, 14 giorni) secondo la documentazione ENISA attuale;
  - quale copertura CPE/PURL serve per interrogare OSV/NVD su componenti C;
  - quali requisiti di BSI TR-03183 e dell'Allegato VII vadano coperti dal pacchetto documentale.
- **What Codex needs to verify:**
  1. Prototipo di fattibilità dello scanner su 5–10 repository embedded pubblici: misurare richiamo e precisione.
  2. Copertura dei dati di vulnerabilità per le librerie embedded più comuni.
  3. Interfacce e requisiti della piattaforma di segnalazione ENISA e della documentazione CRA rilevante (fonti primarie).
  4. Formati: CycloneDX 1.6 / SPDX 2.3–3.0, VEX (CSAF o CycloneDX).
  5. Architettura, hosting UE, sicurezza dei repository dei clienti (scansione locale vs upload).
  6. Costi e tempi realistici per MVP e V1.

---

## Prossimi passi suggeriti (da decidere tu)

1. Confermare se C1 è abbastanza distinto dall'idea esclusa n. 1.
2. Avviare in parallelo i tre esperimenti di validazione (`05-top5.md`) e la due diligence tecnica.
3. Decidere la costruzione **solo** dopo l'esito di entrambi.
