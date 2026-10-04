# Strumenti di raccolta

Script minimi usati il 4/10/2026 per interrogare gli archivi pubblici. Richiedono solo `python3` e `curl`.

| Script | Uso |
|---|---|
| `reddit_scansione.py SUB REGEX DOPO PRIMA PAGINE` | scorre i post di un subreddit (100 per pagina, dal più recente) tramite l'API di Arctic Shift e stampa quelli il cui titolo o testo corrisponde alla regex |
| `reddit_ricerca.py SUB "QUERY" [DOPO]` | ricerca full-text di Arctic Shift in un subreddit |
| `reddit_thread.py ID_POST [N_CARATTERI]` | stampa un post e i suoi commenti, ordinati per punteggio |
| `reddit_alto_engagement.py SUB REGEX DOPO PRIMA PAGINE MIN_UPVOTE MIN_COMMENTI` | come la scansione, ma solo i post con engagement alto |
| `hn_commenti.py "QUERY" [TAG] [N] [DA_EPOCH]` | ricerca su Hacker News (API Algolia) |
| `hn_thread.py ID` | thread di Hacker News |
| `discourse_ricerca.py BASE_URL "QUERY" [N]` | ricerca su forum Discourse (es. Shopify Community) |
| `sweep.sh SUB1 SUB2 …` | scansione in sequenza con la regex dei segnali ad alto valore |

L'API di Arctic Shift applica limiti di frequenza: gli script ritentano con pause.
