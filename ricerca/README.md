# Ricerca parallela — App per un solo fondatore (ottobre 2026)

Nuovo filone di ricerca, **indipendente** dal progetto precedente. Non ne usa classifiche, punteggi o conclusioni e non lo modifica. Segue il metodo originale (Stadi 1–7, valutazione finale, top 5, tabella comparativa, handoff) con i vincoli aggiuntivi:

- esclusione delle tre idee già selezionate e delle loro varianti cosmetiche;
- solo ricerca, nessun software costruito.

**Data della ricerca:** 4 ottobre 2026.

## Esito in breve

> **Research funnel complete. I recommend moving these opportunities to Codex technical due diligence.**
>
> In italiano: l'imbuto di ricerca è completo. Raccomando di passare queste opportunità alla due diligence tecnica.

| # | Opportunità | Punteggio | Kill risk |
|---|---|---|---|
| 1 | **Tracker MSP di advisory, EOL e licenze per firewall/VPN dei clienti** | 65/100 | Medio |
| 2 | **Audit self-service delle fatture 3PL per brand DTC piccoli** | 63/100 | Medio |
| 3 | **Kit CRA per piccoli team embedded (SBOM bare-metal, vulnerabilità, segnalazione 24h, documentazione)** | 58/100 | Medio (tendente ad alto) |

Nessuna delle tre ha ancora prove di **disponibilità a pagare**. Il passaggio raccomandato è alla **due diligence tecnica** e, in parallelo, agli esperimenti di validazione. **Non** è un via libera alla costruzione.

## Imbuto

| Stadio | Risultato | Documento |
|---|---|---|
| 1 — Scavenger | **122 segnali** datati, con fonte | [01-segnali.md](01-segnali.md) · [dati/segnali.tsv](dati/segnali.tsv) |
| 2 — Filtro competitivo | **28 problemi** → 10 candidati seri (3 con varco credibile) | [02-cluster-e-concorrenza.md](02-cluster-e-concorrenza.md) |
| 3–7 — Fattibilità, business, distribuzione, test AI, avvocato del diavolo | per i 10 candidati | [03-candidati-seri.md](03-candidati-seri.md) |
| Valutazione finale | punteggio /100 | [04-punteggi.md](04-punteggi.md) |
| Shortlist | top 5 con scheda completa | [05-top5.md](05-top5.md) |
| Confronto | tabella finale | [06-tabella-comparativa.md](06-tabella-comparativa.md) |
| Handoff | pacchetti di due diligence tecnica per le prime 3 | [07-codex-handoff.md](07-codex-handoff.md) |

## Risultato trasversale più importante

Nel 2026 quasi ogni dolore visibile online ha già da 2 a 10 micro-prodotti, spesso costruiti in poche settimane con strumenti AI. Tra i casi verificati: pulsante di recesso UE, modello N2 spagnolo, fatture ricorrenti Xero, file `.pub` di Publisher, bundle Etsy, certificati di esenzione, registri refrigeranti EPA.

Inoltre molti post "is there a tool…" sono scritti da builder, non da acquirenti. Per questo ho dato più peso a:

1. domanda di utenti indipendenti con engagement;
2. incumbent sales-led o costosi;
3. barriere tecniche o di dominio.

Dettagli in `02`.

## Fonti e metodo

| Fonte | Come è stata usata |
|---|---|
| **Reddit** | tramite l'archivio pubblico **Arctic Shift**, perché l'accesso diretto a Reddit era bloccato dall'ambiente: scansioni sistematiche di ~80 subreddit professionali (MSP, contabilità, fisco USA, studi legali, e-commerce, logistica, edilizia, no-profit, embedded, sanità ambulatoriale, IT scolastico, comunità italiane…) e lettura completa dei thread chiave con i commenti |
| **Hacker News** | API Algolia |
| **Forum Discourse** | Shopify Community |
| **Bacheche di richieste funzioni** | Xero Product Ideas, Webflow Wishlist, Calendly Community |
| **Siti di vendor, comparatori e documentazione** | ricerche web mirate per il filtro competitivo |
| **Fonti istituzionali** | CISA, Commissione UE/ENISA (tramite fonti secondarie), HMRC, RENTRI |

Gli script usati per interrogare gli archivi sono in [`strumenti/`](strumenti/), per riproducibilità.

## Limiti dichiarati

- **Fonti non coperte o coperte poco:** X/Twitter, Discord privati, YouTube, Quora, recensioni G2/Capterra in forma sistematica (pagine spesso bloccate), App Store e Play Store. Le recensioni dei marketplace sono state usate solo in modo indiretto.
- **Metriche:** upvote e commenti provengono dall'archivio e possono differire leggermente dai valori attuali.
- **Fonti di parte:** prezzi e funzioni dei concorrenti vengono dai loro siti o da comparatori e vanno riconfermati prima di decisioni.
- **Distinzione evidenze/ipotesi:** ogni affermazione nei documenti è marcata **[OSSERVATO]**, **[IPOTESI]** o **[DA VERIFICARE]** dove la distinzione conta. **Nessun esperimento è stato eseguito**: quelli in `05` sono proposte.
