# 03 — Candidati seri: fattibilità, modello di business, distribuzione, test AI, avvocato del diavolo (Stadi 3–7)

Valutazioni ad alto livello, **senza scrivere codice**. Le stime di tempo assumono **uno sviluppatore competente con strumenti di coding AI**. I costi sono ordini di grandezza in €/mese e **non vanno presi alla lettera**.

Regola di lettura:

- **[OSSERVATO]** = visto in una fonte
- **[IPOTESI]** = stima o inferenza mia
- **[DA VERIFICARE]** = da chiudere con esperimenti o due diligence tecnica

---

## Stadio 3 — Fattibilità per un fondatore solo

| Cand. | Difficoltà /5 | Prototipo | MVP funzionale | V1 produzione | Manutenzione | Costo operativo stimato (100 / 1.000 / 10.000 utenti) | Rischi di dipendenza tecnica |
|---|---|---|---|---|---|---|---|
| **C1** Audit fatture 3PL | 3 | 1 settimana (1 formato, es. API Billing ShipBob + CSV) | 3–5 settimane | 6–10 settimane | Media | ~50–150 / 500–1.500 / 5.000–15.000 (estrazione AI da PDF a consumo, storage) | variabilità dei formati di fattura (PDF eterogenei), API dei 3PL non sempre disponibili, costo e accuratezza dell'estrazione AI, dati commerciali sensibili (sicurezza) |
| **C2** Advisory edge per MSP | 3 | 1 settimana (2 vendor, import CSV) | 3–4 settimane (6–8 vendor, matching, alert, report per cliente) | 6–8 settimane (integrazioni RMM/Auvik/Domotz, dati EOL, billing) | Media | ~30–80 / 150–400 / 1.000–3.000 (job schedulati, email) | parsing di feed eterogenei per vendor (RSS, JSON, CSAF, HTML), confronto versioni non semver (FortiOS 7.2.10 vs 7.2.9, treni IOS-XE), applicabilità legata alla configurazione, API RMM a pagamento o soggette a rate limit, responsabilità in caso di falso negativo |
| **C3** Kit CRA embedded | 4 | 1–2 settimane (import CycloneDX + monitoraggio OSV + orologio di segnalazione) | 4–6 settimane (triage/VEX, template di segnalazione, periodo di supporto) | 8–12 settimane (rilevamento componenti C bare-metal, pacchetto documentale Allegato VII) | Media-Alta | ~30–100 / 300–800 / 3.000–8.000 | identificazione dei componenti C vendored (lwIP, mbedTLS, FreeRTOS, FatFs…) senza package manager; qualità di NVD/OSV per C/C++; evoluzione delle norme armonizzate e delle linee guida CRA; requisiti formali della piattaforma di segnalazione ENISA |
| C4 Estrazione K-1 | 4–5 | 2 settimane | 6–8 settimane | 3–4 mesi | Alta | basso fuori stagione, picchi a feb–apr e set–ott | accuratezza (statement aggiuntivi, stati), formati di import proprietari (UltraTax, CCH), responsabilità professionale, stagionalità |
| C5 No-profit grant | 2 | 1 settimana | 2–4 settimane | 5–6 settimane | Bassa-Media | ~20–60 / 150–400 / 1.000–3.000 | template dei finanziatori molto diversi, integrazione con il payroll |
| C6 Rendiconti PM | 2–3 | 1 settimana | 3–4 settimane | 6 settimane | Media | ~30 / 300 / 2.500 | export AppFolio/Buildium che cambiano, dati finanziari sensibili |
| C7 Perdita spedizioni Shopify | 2 | 3–5 giorni | 2–3 settimane | 4–6 settimane | Media | ~20 / 150 / 1.500 | API Shopify e revisione dell'App Store, etichette acquistate fuori da Shopify (ShipStation ecc.) |
| C8 Spesa Copilot multi-tenant | 3 | 1 settimana | 3 settimane | 6 settimane | Alta | ~30 / 200 / 1.500 | API Partner Center/Graph in evoluzione, consenso GDAP per tenant, Microsoft o Pax8 che chiudono il gap |
| C9 Draw costruzione | 2 | 1 settimana | 3 settimane | 6 settimane | Bassa | ~20 / 150 / 1.200 | variabilità dei processi tra lender |
| C10 Claims broker | 2 | 1 settimana | 3 settimane | 6 settimane | Media | ~20 / 200 / 1.500 | integrazione con il TMS, gestione documenti |

## Stadio 4 — Modello di business

Prezzi ipotizzati su comparabili osservati. Il calcolo indica i **clienti paganti necessari** per livello di MRR: si dividono le soglie per l'ARPA (ricavo medio mensile per cliente) in forma di intervallo, **senza falsa precisione**.

| Cand. | Modello più plausibile | Comparabili osservati | ARPA ipotizzato | €500 | €2k | €5k | €10k | €25k |
|---|---|---|---|---|---|---|---|---|
| **C1** | abbonamento a fasce per spesa/ordini 3PL (es. 79 / 149 / 299 €) + audit iniziale a pagamento opzionale | Implentio da 1.000 $/mese; Mockly 30% dei recuperi; cost accountant 1–2 h/settimana (S109) | 80–150 € | 4–7 | 14–25 | 34–63 | 67–125 | 167–313 |
| **C2** | abbonamento per dispositivo edge monitorato con minimo mensile (es. 49 € fino a 50 device, 149 € fino a 250, 299 € fino a 750) | VulniPulse 15 $/mese (singolo utente, nessuna funzione MSP); Liongard da ~33 $ al mese per unità/ambiente | 70–150 € | 4–8 | 14–29 | 34–72 | 67–143 | 167–358 |
| **C3** | abbonamento per linea di prodotto/firmware (es. 49–149 €/mese) o annuale (490–1.490 €) | Interlynk free tier; ONEKEY/Cybellum su richiesta (enterprise); consulenti CRA | 60–150 € | 4–9 | 14–34 | 34–84 | 67–167 | 167–417 |
| C4 | a documento (4–8 € per K-1), pacchetti stagionali | K1x 60–75 $ per K-1 sotto 50; Lido 29 $/mese | 40–120 € (equivalente annualizzato) | 5–13 | 17–50 | 42–125 | 84–250 | 209–625 |
| C5 | abbonamento per organizzazione | ClickTime, WeWorked | 30–60 € | 9–17 | 34–67 | 84–167 | 167–334 | 417–834 |
| C6 | abbonamento per numero di immobili | add-on di reportistica PM | 40–90 € | 6–13 | 23–50 | 56–125 | 112–250 | 278–625 |
| C7 | app Shopify a canone basso | Bloom Analytics, BeProfit | 10–30 € | 17–50 | 67–200 | 167–500 | 334–1.000 | 834–2.500 |
| C8 | per tenant | (Pax8 in arrivo, nativo Microsoft gratuito) | 40–100 € | 5–13 | 20–50 | 50–125 | 100–250 | 250–625 |
| C9 | per costruttore attivo | Buildertrend/JobTread (suite) | 30–60 € | 9–17 | 34–67 | 84–167 | 167–334 | 417–834 |
| C10 | per utente broker | FreightClaims.com | 50–100 € | 5–10 | 20–40 | 50–100 | 100–200 | 250–500 |

**[OSSERVATO]** S113 (113 upvote) e S114 (161 commenti) mostrano fatica da abbonamenti nelle micro-imprese. **[IPOTESI]** Un canone regge solo se il valore è ricorrente e misurabile in denaro (C1: € recuperati; C2: esposizione evitata o prova per l'assicurazione; C3: obbligo di legge continuo). Per i problemi "a scatti" conviene prevedere crediti o pagamenti una tantum.

## Stadio 5 — Distribuzione

| Cand. | Primi 100 utenti | Verso 1.000 utenti | Loop di acquisizione naturale | Difficoltà /5 |
|---|---|---|---|---|
| **C1** | contatto diretto con chi pubblica il problema (S105–S109) offrendo un audit gratuito; community DTC (r/ecommerce, r/shopify, Slack/Discord DTC); consulenti e contabili e-commerce come partner | SEO su "come leggere la fattura [3PL]" e "calcolatore storage fee", **un decoder gratuito per fattura ShipBob**; partnership con broker 3PL e fractional CFO; case study con € recuperati | report condivisibile "abbiamo recuperato X €" (soft); referral dei contabili che seguono più brand | 3 |
| **C2** | risposte utili (non promozionali) nei thread r/msp dopo ogni advisory critico (S69, S122); MSPGeek/Discord/Facebook MSP; offerta "report di esposizione edge gratuito" via upload CSV | **pagine SEO programmatiche per vendor/modello/versione** ("FortiOS 7.4.x: advisory e versione corretta"); digest settimanale gratuito degli advisory edge; integrazioni RMM/PSA (marketplace **[DA VERIFICARE]**); podcast e peer group MSP | report PDF per cliente finale con attribuzione; pagine pubbliche per versione che si posizionano su Google a ogni nuova CVE | 3 |
| **C3** | r/embedded, forum EEVblog, community ESP-IDF/Zephyr/STM32, LinkedIn dei founder hardware UE; webinar CRA; camere di commercio (IHK, CCIAA) | SEO ("SBOM STM32", "template segnalazione CRA 24h", "periodo di supporto CRA"); **generatore SBOM gratuito per progetti C bare-metal** come lead magnet; partnership con consulenti CRA, organismi notificati ed EMS; European Digital Innovation Hub | SBOM e dichiarazioni condivise con i clienti B2B, che chiedono lo stesso formato ai propri fornitori **[IPOTESI]** | 3–4 |
| C4 | r/taxpros, gruppi Facebook dei tax pro | stagionale, SEO | debole | 4 |
| C5 | r/nonprofit, associazioni di no-profit | marketplace dei software no-profit | debole | 4 |
| C6 | r/PropertyManagement, gruppi NARPM | integrazioni | report ai proprietari (attribuzione) | 4 |
| C7 | Shopify App Store | App Store + SEO | discovery nel marketplace | 3 (ma concorrenza alta) |
| C8 | r/msp (thread S99) | marketplace Pax8 **[DA VERIFICARE]** | debole | 4 |
| C9 | r/Contractor, r/RealEstateInvesting | SEO | debole | 4 |
| C10 | r/FreightBrokers | integrazioni TMS | debole | 4 |

## Stadio 6 — Test di sostituzione con l'AI generalista

| Cand. | Perché non basta ChatGPT/Claude/Gemini? | Rischio di sostituzione |
|---|---|---|
| **C1** | **[OSSERVATO]** un commento suggerisce già "fai convertire il PDF in CSV dal chatbot e analizza in 1–2 ore" (S105). **[IPOTESI]** Il valore sta altrove: rate card persistente, confronto con i dati d'ordine (Shopify/3PL API), job mensile, storico degli scostamenti, tracciamento delle contestazioni, più 3PL normalizzati. Un chatbot fa un'analisi una tantum, non il controllo ricorrente | Medio |
| **C2** | monitoraggio schedulato, inventario persistente per cliente, confronto versioni deterministico per vendor, storico datato come prova per assicurazione e audit; un LLM non "veglia" sui feed e può sbagliare il confronto di versione | Basso |
| **C3** | SBOM, monitoraggio continuo, orologi legali 24/72h/14g, registro VEX e documentazione versionata: tutto con stato persistente, scadenze e verificabilità. L'AI aiuta a redigere, non sostituisce il sistema di registrazione | Basso |
| C4 | batch di documenti + import nel software fiscale; ma i modelli multimodali generalisti leggono già bene la prima pagina del K-1 | Medio-Alto |
| C5 | stato persistente e approvazioni | Medio |
| C6 | batch mensile da export | Medio |
| C7 | integrazione dati Shopify | Basso-Medio |
| C8 | API multi-tenant | Basso |
| C9 | stato persistente | Medio |
| C10 | gestione documenti nel tempo | Medio |

## Stadio 7 — Avvocato del diavolo

| Cand. | Argomenti per uccidere l'idea | Kill risk |
|---|---|---|
| **C1** | (1) Il mercato è spartito tra servizi a commissione e piattaforme enterprise: i brand piccoli potrebbero preferire "nessun costo fisso" (commissione) **[DA VERIFICARE]**. (2) Formati di fattura eterogenei = complessità nascosta e supporto. (3) Disponibilità a pagare incerta per brand sotto 1.000 ordini/mese: il valore recuperabile (3–8% della spesa 3PL secondo fonti di settore, non verificato) potrebbe essere troppo piccolo. (4) Copycat facile nella versione base (già 1 repo open source e 2+ post di builder). (5) Dipendenza dalla collaborazione dei 3PL per i dati. (6) Vicinanza percepita all'idea esclusa n. 1 (vedi nota in 02). | **MEDIO** |
| **C2** | (1) VulniPulse e Lansweeper coprono parte del valore; Liongard copre firmware e licenze per alcuni vendor. (2) Il commento "usa i feed RSS" (S53) indica che alcuni MSP si arrangiano con script. (3) Un falso negativo crea responsabilità: va posizionato come aiuto, non come garanzia. (4) La regola di r/msp (karma minimo, anti-promo) rende difficile la distribuzione diretta. (5) I vendor (Fortinet, Cisco) migliorano i propri strumenti. (6) Mercato degli MSP grande ma con tanti strumenti già in uso: alta concorrenza per budget e attenzione. | **MEDIO** |
| **C3** | (1) Molti tool gratuiti o freemium (Dependency-Track, Interlynk, sbomify) per la parte SBOM e monitoraggio. (2) **[OSSERVATO]** parte del target reagisce uscendo dal mercato UE invece di comprare strumenti (S115). (3) Rischio di responsabilità sui contenuti di compliance: serve una formulazione "strumento", non "certificazione". (4) Le norme armonizzate non sono ancora pubblicate (S01): requisiti in movimento. (5) Il rilevamento dei componenti C bare-metal è tecnicamente difficile e potrebbe richiedere molto lavoro manuale. (6) Ciclo di vendita B2B più lento. | **MEDIO** (tendente ad alto) |
| C4 | complessità tecnica alta, concorrenti già economici (Lido, GruntWorx), stagionalità, responsabilità professionale | **ALTO** |
| C5 | concorrenti specifici esistenti, bassa disponibilità a pagare, prove deboli | **ALTO** |
| C6 | i gestionali hanno già report builder; prova debole (1 post) | **ALTO** |
| C7 | Bloom/BeProfit e simili; canone basso; App Store saturo | **ALTO** |
| C8 | Microsoft (cap/alert nativi) e Pax8 chiudono il gap; rischio di piattaforma | **ALTO** |
| C9 | un solo segnale; i lender gestiscono il processo | **ALTO** |
| C10 | concorrente dedicato con piano per piccoli broker | **ALTO** |
