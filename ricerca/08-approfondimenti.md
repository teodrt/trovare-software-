# 08 — Approfondimenti sui tre finalisti (4 ottobre 2026, seconda sessione)

Obiettivo: chiudere, con la sola ricerca, le domande **[DA VERIFICARE]** dei pacchetti di handoff (`07`) che non richiedono la due diligence tecnica. Non è stato costruito software. Le verifiche sono state fatte con richieste HTTP dirette agli endpoint pubblici e con ricerche web.

## C2 — Tracker MSP per apparati edge

### Fonti dati dei vendor

| Fonte | Esito della verifica | Implicazione |
|---|---|---|
| **Palo Alto Networks** — `https://security.paloaltonetworks.com/json/` | **[OSSERVATO]** HTTP 200, JSON con 25 advisory recenti. Ogni voce ha `product`, `version` (treno, es. "PAN-OS 11.1"), `affected` e `fixed` come espressioni testuali per treno con hotfix (es. `< 11.1.4-h36, < 11.1.6-h38`), severità, data e soluzione | Dati **strutturati e utilizzabili**. Confermano però che il confronto versioni richiede un parser specifico per vendor: hotfix `-hN`, più rami nello stesso treno, note con asterisco |
| **CISA KEV** — `known_exploited_vulnerabilities.json` | **[OSSERVATO]** HTTP 200, catalogo versione 2026.10.02 con 1.733 voci | Fonte affidabile per la priorità "sfruttata attivamente" |
| **Fortinet** | **[OSSERVATO]** feed RSS ufficiale (`/rss/ir.xml`; dall'ambiente di test la connessione è stata resettata); ogni advisory è scaricabile in CVRF/CSAF/STIX. Nessun `provider-metadata.json` CSAF trovato al percorso standard (404) | Fattibile: RSS per la scoperta + CSAF per singolo advisory. **[DA VERIFICARE]** stabilità e limiti di frequenza |
| **Cisco** | openVuln API (chiave gratuita). Il `provider-metadata.json` CSAF ha risposto 403 dall'ambiente di test | Usare l'API openVuln |
| **SonicWall** | **[OSSERVATO]** il sito PSIRT è un'app JavaScript con reCAPTCHA; nessuna API pubblica documentata trovata | **Rischio:** servirebbe scraping o inserimento curato a mano. Va trattato come vendor "semi-manuale" nella V1 |
| **WatchGuard** | pagina advisory HTML (redirect 301) | scraping HTML |
| **Lista CISA degli apparati EOS (BOD 26-02)** | **[OSSERVATO]** non pubblica: dataset controllato distribuito solo alle agenzie federali | Non utilizzabile come fonte EOL |
| **eol.network** | **[OSSERVATO]** database di date EoS/EoL con 92.203 SKU di 59 vendor, ricerca massiva, API e correlazione con KEV; nessuna funzione MSP o multi-tenant dichiarata; prezzi non pubblicati | Da un lato è un **nuovo concorrente parziale** sull'EOL; dall'altro è una **possibile fonte dati licenziabile**, che riduce il rischio tecnico **[DA VERIFICARE]** |

### Effetto sulla valutazione

- **Rischio tecnico:** invariato o leggermente ridotto. Palo Alto e KEV sono pronti; Fortinet e Cisco hanno canali ufficiali; SonicWall e WatchGuard richiedono scraping o cura manuale.
- **Gap competitivo:** leggermente ridotto (eol.network si aggiunge a VulniPulse sul fronte single-tenant).
- **Cuneo:** resta il multi-tenant MSP con evidenze per cliente.
- **Punteggio:** invariato (65). Le variazioni si compensano.

## C1 — Audit fatture 3PL

### Dati disponibili dai 3PL

| 3PL / WMS | Esito della verifica | Implicazione |
|---|---|---|
| **ShipBob** | **[OSSERVATO]** Billing API con `GET /2026-07/invoices`, `POST /2026-07/transactions:query`, `GET /2026-07/invoices/{id}/transactions` e `GET /2026-07/transaction-fees`. Ogni transazione riporta importo, data, tipo di fee (es. "Shipping", "WMS - Fuel Surcharge"), `reference_id` della spedizione, magazzino e tracking. Autenticazione con PAT con scope `billing_read`; alcune fee arrivano fino a 6 ore dopo l'etichetta | Il 3PL più citato dai brand piccoli offre dati di fatturazione **a livello di spedizione**: il join con gli ordini è fattibile senza PDF |
| **ShipMonk** | **[OSSERVATO]** fatture esportabili in PDF e CSV; tabella "Invoice Item" nel Merchant Data Catalog; API REST pubblica (ordini, spedizioni, costi di spedizione) | CSV strutturato disponibile. **[DA VERIFICARE]** se le righe fattura sono esposte anche via API |
| **ShipHero (WMS usato da molti 3PL)** | **[OSSERVATO]** modulo "3PL Billing" con fee standardizzate (ricorrenti, ricezione, storage, spedizioni, picking, resi, ad hoc) e portale cliente | Tutti i 3PL che fatturano con ShipHero producono fatture con **struttura simile**: un solo parser copre molti 3PL |
| **Extensiv (3PL Warehouse Manager)** | **[OSSERVATO]** oltre 1.200 3PL clienti; billing automatizzato con export verso QuickBooks/Sage | Stesso effetto leva di ShipHero **[DA VERIFICARE]** il formato delle fatture ricevute dai brand |

### Segnali aggiuntivi

- **[OSSERVATO]** r/ecommerce, 2026-03-12: "Shipbob alternatives… their pricing went up" ([link](https://reddit.com/r/ecommerce/comments/1rs60cg)).
- **[OSSERVATO]** r/ecommerce, 2026-02-21: "Leaving shipbob, narrowed it down to shipmonk and shiphype" ([link](https://reddit.com/r/ecommerce/comments/1ramz0d)).
- **[OSSERVATO]** r/ecommerce, 2026-03-24: "Best 3pl for 1 to 5k orders per month" (12 commenti, [link](https://reddit.com/r/ecommerce/comments/1s21nur)).

Questi post confermano attrito sui costi nel segmento target, ma non sono prove dirette di disponibilità a pagare per un audit.

### Effetto sulla valutazione

- **Rischio tecnico:** ridotto. I formati più diffusi sono strutturati (API ShipBob, CSV ShipMonk, WMS comuni); l'estrazione AI da PDF diventa un ripiego, non il percorso principale.
- **Punteggio:** "Semplicità tecnica" passa da 5 a 6, quindi il totale sale da 76 a 77/120 (**64/100**).
- **Ordine:** resta secondo per un punto.

## C3 — Kit CRA embedded

### Piattaforma di segnalazione ENISA

**[OSSERVATO]** La Single Reporting Platform è attiva dall'11/9/2026. ENISA dichiara che **al rilascio iniziale non c'è un'API**: le notifiche si inviano dall'interfaccia web. Le organizzazioni possono però automatizzare tutto il flusso interno fino all'invio; l'API "may be considered in a future phase" ([Help Net Security, 2026-09-14](https://www.helpnetsecurity.com/2026/09/14/enisa-cra-single-reporting-platform/), [ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)).

**Implicazione:** il prodotto deve preparare i contenuti e il registro; l'invio resta manuale. Questo semplifica l'MVP e riduce la dipendenza da integrazioni esterne.

### Costi delle alternative

**[OSSERVATO, fonti di settore non indipendenti]**:

- consulenti CRA: 900–1.400 €/giorno; prima conformità di un prodotto 30.000–60.000 € con consulenza, 10.000–27.000 € di lavoro interno ([Porta Regulus](https://portaregulus.com/cra-sme-time-and-cost));
- prodotti con autovalutazione: 20.000–50.000 € una tantum per linea di prodotto;
- gestione delle vulnerabilità continua: almeno mezza persona a tempo pieno.

**[IPOTESI]** Un canone di 49–149 €/mese è trascurabile rispetto a queste cifre. Il prezzo non è quindi l'ostacolo: lo sono la fiducia e la percezione di "basta il gratuito".

### Finanziamenti pubblici come leva di vendita

**[OSSERVATO]** Il progetto UE **SECURE** cofinanzia al 50% le PMI (produttori, importatori, distributori, sviluppatori software) fino a 30.000 € per progetto per misure di conformità al CRA. La prima call è durata dal 28/1 al 29/3/2026 con 5 M€; la seconda ha almeno 11,5 M€ ([DIGITAL SME](https://www.digitalsme.eu/fundings/open-call-for-smes-to-strengthen-cyber-resilience/), [ACN](https://www.acn.gov.it/portale/en/w/progetto-secure-al-via-il-primo-bando-per-sostenere-le-pmi-nell-attuazione-del-cyber-resilience-act-1), [InnexHub](https://www.innexhub.it/secure-second-open-call-for-proposals/)).

Le fonti citano come costi ammissibili "security testing, consulting and process measures". **[DA VERIFICARE]** se gli abbonamenti software siano ammissibili: in caso positivo diventano un canale di vendita (bundle "kit + consulente partner" finanziabile).

### Rumore competitivo

**[OSSERVATO]** Proliferano siti di contenuti e strumenti CRA (cra-toolkit.com, portaregulus, venvera, cyberresilienceact.eu con calcolatore di costi, craevidence). Il canale SEO generico "CRA" sarà molto competitivo. Il posizionamento deve restare tecnico e di nicchia (firmware MCU, SBOM bare-metal).

### Effetto sulla valutazione

- Disponibilità a pagare: argomento economico più forte (costi delle alternative), ma ancora nessuna prova diretta.
- Distribuzione: nuovo canale possibile (bandi SECURE), da verificare.
- Concorrenza: in aumento sul fronte dei contenuti.
- **Punteggio:** invariato (58).

## Riepilogo

| Domanda | Stato |
|---|---|
| Esistono feed strutturati per i vendor edge principali? | **Sì** per Palo Alto, KEV, Cisco (API) e Fortinet (RSS + CSAF per advisory); **no** per SonicWall (nessuna API pubblica trovata) |
| La lista EOS di CISA è utilizzabile? | **No**, non è pubblica; eol.network è un'alternativa da valutare |
| I 3PL espongono dati di fatturazione strutturati? | **Sì** per ShipBob (API) e ShipMonk (CSV); ShipHero ed Extensiv standardizzano le fatture di molti 3PL |
| La piattaforma ENISA ha un'API? | **No** al lancio; l'invio è manuale |
| Esistono fondi per le PMI CRA? | **Sì** (SECURE, fino a 30.000 € al 50%); ammissibilità del software **da verificare** |

**Classifica aggiornata:** C2 65 · C1 64 · C3 58. Le conclusioni di `07` restano valide.
