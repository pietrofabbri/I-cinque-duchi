# Mappa dell'informatica — Area K: Web e sviluppo di applicazioni (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** il web come piattaforma: HTML, CSS, JavaScript, accessibilità, framework front-end, back-end e API, pubblicazione, app mobili, web semantico, prestazioni, SEO e privacy, grafica per il web. I protocolli sottostanti sono nell'area J, la sicurezza approfondita nell'area N.

---

## K1 Come funziona il web
- **K1.1** Internet e Web: la differenza · [1] · ⟵ J2.1
- **K1.2** Browser, server web, pagine · [1] · ⟵ K1.1
- **K1.3** L'URL: schema, dominio, percorso, parametri · [1] · ⟵ K1.2
- **K1.4** Il ciclo richiesta-risposta visto dal browser; strumenti per sviluppatori · [2] · ⟵ K1.3, J7.3
- **K1.5** Siti statici e siti dinamici · [1–2] · ⟵ K1.2
- **K1.6** Il motore di rendering del browser: DOM, CSSOM, disegno della pagina · [3] · ⟵ K4.1, K3.1

## K2 HTML
- **K2.1** Il documento HTML: tag, elementi, attributi, struttura · [1] · ⟵ B4.2, K1.2
- **K2.2** Testo, titoli, paragrafi, elenchi · [1] · ⟵ K2.1
- **K2.3** Collegamenti e percorsi relativi · [1] · ⟵ K2.1, I5.1
- **K2.4** Immagini e contenuti multimediali · [1] · ⟵ K2.1, B6.6
- **K2.5** Tabelle · [1] · ⟵ K2.1
- **K2.6** Moduli e controlli di input · [1–2] · ⟵ K2.1
- **K2.7** HTML semantico (header, nav, main, article) · [1–2] · ⟵ K2.2
- **K2.8** Validazione del codice HTML · [1–2] · ⟵ K2.1
- **K2.9** Metadati della pagina e codifica dei caratteri · [1–2] · ⟵ K2.1, B4.4

## K3 CSS
- **K3.1** Regole, selettori, proprietà; cascata ed ereditarietà · [1] · ⟵ K2.1
- **K3.2** Colori e unità di misura · [1] · ⟵ K3.1, B5.3.3
- **K3.3** Tipografia web e font · [1] · ⟵ K3.1, B13.2
- **K3.4** Il box model · [1] · ⟵ K3.1
- **K3.5** Posizionamento e flusso del documento · [1–2] · ⟵ K3.4
- **K3.6** Flexbox · [2] · ⟵ K3.5
- **K3.7** Grid · [2] · ⟵ K3.5
- **K3.8** Design responsive: media query, approccio mobile first · [2] · ⟵ K3.6
- **K3.9** Transizioni e animazioni · [2] · ⟵ K3.1
- **K3.10** Preprocessori e framework CSS · [2–3] · ⟵ K3.8
- **K3.11** Temi chiari e scuri; variabili CSS · [2–3] · ⟵ K3.2 · (v1.1, approfondimento)
- **K3.12** CSS per la stampa · [2] · ⟵ K3.8 · (v1.1, approfondimento)

## K4 JavaScript nel browser
- **K4.1** Inserire script in una pagina; la console · [2] · ⟵ K2.1, G5.5.1
- **K4.2** Il DOM: selezionare e modificare elementi · [2] · ⟵ K4.1, E6.4.1
- **K4.3** Gli eventi del browser · [2] · ⟵ K4.2, G3.6.1
- **K4.4** Validazione dei moduli lato client · [2] · ⟵ K4.3, K2.6
- **K4.5** Richieste asincrone: fetch e JSON · [2–3] · ⟵ K4.1, G5.5.4, B11.4
- **K4.6** Archiviazione nel browser: cookie, localStorage, IndexedDB · [2–3] · ⟵ K4.1
- **K4.7** API del browser: canvas, geolocalizzazione, audio · [2–3] · ⟵ K4.2
- **K4.8** Moduli JavaScript e bundler · [3] · ⟵ K4.1, G5.5.5
- **K4.9** WebAssembly · [3–4] · ⟵ K4.1, G7.3.2

## K5 Accessibilità web
- **K5.1** Perché l'accessibilità; disabilità e tecnologie assistive · [1–2] · ⟵ U8.3
- **K5.2** Linee guida WCAG: principi e livelli di conformità · [2] · ⟵ K5.1
- **K5.3** Testi alternativi, struttura dei titoli, etichette dei moduli · [1–2] · ⟵ K5.1, K2.7
- **K5.4** Contrasto dei colori e navigazione da tastiera · [2] · ⟵ K5.2, B5.4.3
- **K5.5** ARIA · [3] · ⟵ K5.2, K4.2
- **K5.6** Verificare l'accessibilità: strumenti automatici e lettori di schermo · [2–3] · ⟵ K5.2
- **K5.7** Obblighi normativi (Legge Stanca, European Accessibility Act) · [2] · ⟵ K5.2

## K6 Framework front-end
- **K6.1** Single page application e rendering lato client · [3] · ⟵ K4.5
- **K6.2** Componenti, stato, proprietà · [3] · ⟵ K6.1, G3.2.1
- **K6.3** Framework diffusi: React, Vue, Svelte, Angular · [3] · ⟵ K6.2
- **K6.4** Gestione dello stato dell'applicazione · [3] · ⟵ K6.2, G3.6.3
- **K6.5** Routing lato client · [3] · ⟵ K6.1
- **K6.6** Rendering lato server e generazione statica · [3–4] · ⟵ K6.3, K7.1

## K7 Back-end e API
- **K7.1** Programmazione lato server: pagine dinamiche · [2–3] · ⟵ K1.5, G1.8
- **K7.2** Framework back-end (Flask, Django, Express, Spring) · [3] · ⟵ K7.1, H4.9
- **K7.3** API REST: risorse, metodi, codici di stato · [3] · ⟵ K7.1, J7.3
- **K7.4** GraphQL e altri stili di API · [3–4] · ⟵ K7.3
- **K7.5** Accesso ai dati dal back-end · [3] · ⟵ K7.1, L5.12
- **K7.6** Sessioni, cookie, autenticazione · [3] · ⟵ K7.1, K4.6, N5.1
- **K7.7** Autorizzazione delegata: OAuth 2.0 e OpenID Connect · [3–4] · ⟵ K7.6, N5
- **K7.8** WebSocket e comunicazione in tempo reale · [3] · ⟵ K7.1, J6.3
- **K7.9** Sicurezza delle applicazioni web: panoramica OWASP Top 10 · [3] · ⟵ K7.6 · ⟶ N6

## K8 Pubblicazione
- **K8.1** Hosting, domini e DNS per un sito · [2] · ⟵ J7.1, K1.2
- **K8.2** Pubblicare un sito statico (GitHub Pages, Netlify) · [2] · ⟵ K8.1, H5.4
- **K8.3** Generatori di siti statici (Hugo, Jekyll) · [2–3] · ⟵ K8.2, B13.5
- **K8.4** Certificati TLS per il proprio sito · [2–3] · ⟵ K8.1, J7.4
- **K8.5** Sistemi di gestione dei contenuti (WordPress) · [1–2] · ⟵ K1.5
- **K8.6** Pubblicare applicazioni dinamiche su server e cloud · [3] · ⟵ K7.2, I9.4

## K9 App mobili
- **K9.1** App native, ibride, web app progressive · [2] · ⟵ K1.5, I8.4
- **K9.2** Sviluppo Android (Kotlin, Java) · [3] · ⟵ K9.1, G5.4.5
- **K9.3** Sviluppo iOS (Swift) · [3] · ⟵ K9.1, G5.11
- **K9.4** Framework multipiattaforma (Flutter, React Native) · [3] · ⟵ K9.1, K6.2
- **K9.5** Progettare per schermi piccoli e sensori · [2–3] · ⟵ K9.1, K3.8
- **K9.6** Pubblicazione negli store e permessi · [2–3] · ⟵ K9.1

## K10 Web semantico e linked data
- **K10.1** Dati strutturati nelle pagine (schema.org, JSON-LD) · [3] · ⟵ K2.9, B11.4
- **K10.2** RDF: triple soggetto-predicato-oggetto · [3–4] · ⟵ A3.2.1, K10.1
- **K10.3** Ontologie (RDFS, OWL) · [4] · ⟵ K10.2, O2.3
- **K10.4** SPARQL e linked open data (Wikidata) · [3–4] · ⟵ K10.2, L5.3
- **K10.5** Grafi di conoscenza · [4] · ⟵ K10.3

## K11 Prestazioni, SEO, privacy
- **K11.1** Prestazioni web: tempi di caricamento e metriche · [3] · ⟵ K1.4
- **K11.2** Ottimizzazione: compressione, cache, immagini, CDN · [3] · ⟵ K11.1, J12.2
- **K11.3** Ottimizzazione per i motori di ricerca (SEO) · [2] · ⟵ K2.7, L11.1
- **K11.4** Analisi del traffico e A/B test · [3] · ⟵ K11.1, A7.4.5
- **K11.5** Cookie, tracciamento, consenso (GDPR, ePrivacy) · [2] · ⟵ K4.6, U4.1
- **K11.6** Progettazione orientata alla privacy · [3] · ⟵ K11.5

## K12 Grafica per il web
- **K12.1** Immagini nel web: formati e immagini responsive · [1–2] · ⟵ K2.4
- **K12.2** SVG nel web · [2] · ⟵ B6.7, K2.1
- **K12.3** Canvas 2D · [2–3] · ⟵ K4.7
- **K12.4** WebGL, WebGPU e librerie 3D (three.js) · [3–4] · ⟵ K12.3, Q2.7
- **K12.5** Visualizzazione di dati nel web (D3, Chart.js) · [3] · ⟵ K4.2, K12.2 · ⟶ Q9
- **K12.6** Animare la grafica SVG · [2–3] · ⟵ K12.2 · (v1.1, approfondimento)
- **K12.7** Progettare un'icona vettoriale · [2] · ⟵ K12.2 · (v1.1, approfondimento)
