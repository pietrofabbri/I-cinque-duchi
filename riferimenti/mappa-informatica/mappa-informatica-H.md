# Mappa dell'informatica — Area H: Ingegneria del software (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** costruire software di qualità in gruppo e nel tempo: ciclo di vita, processi, modellazione, progettazione, controllo di versione, test, rilascio, documentazione, gestione di progetto, requisiti, architettura, manutenzione, operazioni, metriche, economia, sicurezza, pratica professionale. La struttura segue le aree di conoscenza di SWEBOK v4 (vedi la verifica di copertura nel documento madre).

---

## H1 Ciclo di vita del software
- **H1.1** Programma e prodotto software; le qualità attese · [2] · ⟵ G1.8
- **H1.2** Le fasi: requisiti, analisi, progettazione, realizzazione, verifica, rilascio, manutenzione · [2] · ⟵ H1.1
- **H1.3** La "crisi del software" e la nascita dell'ingegneria del software · [2] · ⟵ H1.2
- **H1.4** Ruoli nel gruppo di sviluppo · [2] · ⟵ H1.2

## H2 Modelli di processo
- **H2.1** Modello a cascata · [2] · ⟵ H1.2
- **H2.2** Modelli iterativi e incrementali; prototipazione; modello a spirale · [2] · ⟵ H2.1
- **H2.3** Il manifesto agile e i suoi principi · [2] · ⟵ H2.2
- **H2.4** Scrum: ruoli, sprint, backlog, cerimonie · [2] · ⟵ H2.3
- **H2.5** Kanban e lean · [2] · ⟵ H2.3
- **H2.6** Extreme Programming: programmazione in coppia, integrazione continua · [2–3] · ⟵ H2.3
- **H2.7** DevOps: cultura e ciclo continuo · [3] · ⟵ H2.3
- **H2.8** Scegliere il processo in base al contesto · [3] · ⟵ H2.4, H2.1

## H3 Modellazione
- **H3.1** Perché modellare; UML: panoramica dei diagrammi · [2] · ⟵ H1.2
- **H3.2** Diagramma dei casi d'uso · [2] · ⟵ H3.1
- **H3.3** Diagramma delle classi · [2] · ⟵ H3.1, G3.2.4
- **H3.4** Diagrammi di sequenza e di attività · [2] · ⟵ H3.1
- **H3.5** Diagrammi di stato · [2–3] · ⟵ H3.1, F1.1
- **H3.6** Diagrammi dei componenti e di dislocamento · [3] · ⟵ H3.3
- **H3.7** I modelli E/R all'interno del progetto software · [2] · ⟵ L3.4
- **H3.8** Sviluppo guidato dai modelli · [4] · ⟵ H3.3, G8.3
- **H3.9** Diagrammi come codice (PlantUML, Mermaid) · [3] · ⟵ H3.3 · (v1.1, approfondimento)

## H4 Progettazione
- **H4.1** Modularità, astrazione, occultamento dell'informazione · [2] · ⟵ G1.15, E6.3.5
- **H4.2** Coesione e accoppiamento · [2] · ⟵ H4.1
- **H4.3** Principi SOLID · [3] · ⟵ H4.2, G3.2.6
- **H4.4** Design pattern creazionali (factory, singleton, builder) · [3] · ⟵ H4.3
- **H4.5** Design pattern strutturali (adapter, composite, decorator) · [3] · ⟵ H4.3
- **H4.6** Design pattern comportamentali (observer, strategy, command) · [3] · ⟵ H4.3
- **H4.7** Progettare le API · [3] · ⟵ H4.2
- **H4.8** Code smell e antipattern · [3] · ⟵ H4.3
- **H4.9** Architettura a strati e MVC · [2–3] · ⟵ H4.2 · ⟶ K6, K7

## H5 Controllo di versione
- **H5.1** Controllo di versione: storia, versioni, differenze · [1–2] · ⟵ I5.2
- **H5.2** Git: repository, commit, stato, cronologia · [2] · ⟵ H5.1, I7.1
- **H5.3** Rami e fusioni; conflitti · [2] · ⟵ H5.2
- **H5.4** Repository remoti (GitHub, GitLab); push e pull · [2] · ⟵ H5.2
- **H5.5** Flussi di lavoro collaborativi: fork, pull request, revisione · [2–3] · ⟵ H5.3, H5.4
- **H5.6** Contribuire a un progetto open source · [3] · ⟵ H5.5, U4.4
- **H5.7** Buone pratiche: messaggi di commit, .gitignore, tag · [2] · ⟵ H5.2
- **H5.8** Storia dei sistemi di controllo di versione · [2] · ⟵ H5.1 · (v1.1, approfondimento)

## H6 Qualità: test, debugging, revisione
- **H6.1** Verifica e validazione; errore, difetto, malfunzionamento · [2] · ⟵ H1.2
- **H6.2** Test di unità e framework di test (pytest, JUnit) · [2] · ⟵ H6.1, G1.8
- **H6.3** Progettare i casi di test: classi di equivalenza, valori limite · [2–3] · ⟵ H6.2
- **H6.4** Test a scatola bianca e copertura del codice · [3] · ⟵ H6.3, E3.3
- **H6.5** Test di integrazione, di sistema, di accettazione · [3] · ⟵ H6.2
- **H6.6** Sviluppo guidato dai test (TDD) · [3] · ⟵ H6.2
- **H6.7** Test di regressione e automazione dei test · [3] · ⟵ H6.5
- **H6.8** Debugging sistematico · [2] · ⟵ G1.12
- **H6.9** Revisione del codice · [2–3] · ⟵ H5.5
- **H6.10** Analisi statica e linter · [2–3] · ⟵ G1.11 · ⟶ F9.5
- **H6.11** Refactoring · [3] · ⟵ H4.8, H6.7
- **H6.12** Test basati su proprietà, mutation testing, fuzzing · [4] · ⟵ H6.3

## H7 Build e rilascio
- **H7.1** Sistemi di build (make, Maven, Gradle, cargo) · [3] · ⟵ G5.1.7
- **H7.2** Gestione delle dipendenze; versionamento semantico · [2–3] · ⟵ G1.15
- **H7.3** Integrazione continua · [3] · ⟵ H5.4, H6.7
- **H7.4** Consegna e rilascio continui · [3] · ⟵ H7.3
- **H7.5** Pacchettizzazione in container · [3] · ⟵ I9.4
- **H7.6** Infrastruttura come codice · [3–4] · ⟵ G3.5.4, H7.4
- **H7.7** Catena di fornitura del software; distinta dei componenti (SBOM) · [3–4] · ⟵ H7.2 · ⟶ N6

## H8 Documentazione e stile
- **H8.1** Documentazione per utenti e per sviluppatori · [2] · ⟵ U11.2
- **H8.2** Documentazione nel codice: docstring, generatori automatici · [2] · ⟵ G1.11
- **H8.3** Guide di stile e convenzioni di codifica · [2] · ⟵ G1.11
- **H8.4** Scegliere una licenza per il proprio software · [2–3] · ⟵ U4.4
- **H8.5** Documentare l'architettura e le decisioni di progetto · [3] · ⟵ H8.1, H12.1

## H9 Gestione di progetto
- **H9.1** Pianificazione: attività, dipendenze, diagrammi di Gantt · [2] · ⟵ A4.3.4
- **H9.2** Metodo del cammino critico (CPM/PERT) · [2–3] · ⟵ H9.1, E7.3.3
- **H9.3** Stima di costi e tempi (punti funzione, story point) · [3] · ⟵ H9.1
- **H9.4** Gestione del rischio · [3] · ⟵ H9.1
- **H9.5** Strumenti di gestione (issue tracker, bacheche) · [2] · ⟵ H9.1
- **H9.6** Comunicare con committenti e utenti · [2–3] · ⟵ U11.1

## H10 Sviluppo assistito dall'IA
- **H10.1** Completamento del codice e assistenti conversazionali · [2] · ⟵ G1.3
- **H10.2** Agenti di programmazione · [3] · ⟵ H10.1, O6.7
- **H10.3** Verificare il codice generato: test, revisione, sicurezza · [2–3] · ⟵ H10.1, H6.2
- **H10.4** Effetti su apprendimento, produttività e professione · [2–3] · ⟵ H10.1 · ⟶ W

## H11 Ingegneria dei requisiti
- **H11.1** Requisiti funzionali e non funzionali · [2] · ⟵ H1.2
- **H11.2** Raccolta dei requisiti: interviste, osservazione, workshop · [2] · ⟵ H11.1
- **H11.3** Storie utente e criteri di accettazione · [2] · ⟵ H11.1
- **H11.4** Specifica dei requisiti (documento SRS) · [2–3] · ⟵ H11.2
- **H11.5** Validazione e tracciabilità dei requisiti · [3] · ⟵ H11.4
- **H11.6** Priorità (metodo MoSCoW) e gestione dei cambiamenti · [3] · ⟵ H11.4

## H12 Architettura del software
- **H12.1** Che cos'è l'architettura; gli attributi di qualità · [3] · ⟵ H4.2
- **H12.2** Stili architetturali: a strati, client-server, pipe and filter, a eventi · [3] · ⟵ H12.1
- **H12.3** Monoliti e microservizi · [3] · ⟵ H12.2, J10.5
- **H12.4** Architetture orientate ai servizi e alle API · [3] · ⟵ H12.2, H4.7
- **H12.5** Compromessi architetturali e loro valutazione · [3–4] · ⟵ H12.2
- **H12.6** Architetture per il cloud e serverless · [3–4] · ⟵ H12.3 · ⟶ M4

## H13 Gestione della configurazione e manutenzione
- **H13.1** Tipi di manutenzione: correttiva, adattativa, evolutiva, preventiva · [2–3] · ⟵ H1.2
- **H13.2** Gestione della configurazione: elementi, baseline, rilasci · [3] · ⟵ H5.3
- **H13.3** Software legacy e modernizzazione · [3] · ⟵ H13.1
- **H13.4** Reverse engineering; comprendere codice esistente · [3] · ⟵ H13.3
- **H13.5** Debito tecnico · [3] · ⟵ H13.1, H4.8

## H14 Operazioni (DevOps e SRE)
- **H14.1** Messa in esercizio di un servizio · [3] · ⟵ H7.4
- **H14.2** Osservabilità: log, metriche, tracce · [3] · ⟵ H14.1, I11.4
- **H14.3** Allarmi, gestione degli incidenti, analisi post-incidente · [3] · ⟵ H14.2
- **H14.4** Obiettivi di livello di servizio e margine d'errore · [3–4] · ⟵ H14.2, I12.5
- **H14.5** Ingegneria dell'affidabilità (SRE) · [4] · ⟵ H14.4

## H15 Misura e qualità del software
- **H15.1** Il modello di qualità ISO/IEC 25010 · [3] · ⟵ H6.1
- **H15.2** Metriche del codice: dimensione, complessità ciclomatica · [3] · ⟵ H15.1, A4.3.2
- **H15.3** Metriche di processo e di prodotto · [3] · ⟵ H15.1
- **H15.4** Analisi statistica delle metriche · [3–4] · ⟵ H15.3, A7.4.2
- **H15.5** Modelli di maturità e miglioramento dei processi (CMMI) · [3–4] · ⟵ H15.3

## H16 Economia del software
- **H16.1** Costi del ciclo di vita del software · [3] · ⟵ H1.2
- **H16.2** Costruire, comprare o riusare · [3] · ⟵ H16.1
- **H16.3** Valore del software e ritorno dell'investimento · [3] · ⟵ H16.1
- **H16.4** Economia del debito tecnico · [3–4] · ⟵ H16.1, H13.5

## H17 Sicurezza nel ciclo di vita del software
- **H17.1** Requisiti di sicurezza e modellazione delle minacce · [3] · ⟵ H11.1, N1
- **H17.2** Linee guida per lo sviluppo sicuro (OWASP) · [3] · ⟵ H17.1, N6
- **H17.3** Test di sicurezza nel ciclo continuo (SAST, DAST) · [3–4] · ⟵ H17.2, H7.3
- **H17.4** Gestione delle vulnerabilità delle dipendenze · [3] · ⟵ H7.7

## H18 Pratica professionale
- **H18.1** Lavorare in gruppo: ruoli, comunicazione, conflitti · [2] · ⟵ H1.4
- **H18.2** Comunicazione tecnica nel progetto · [2–3] · ⟵ U11.1
- **H18.3** Etica e responsabilità professionale · [2–3] · ⟵ U9.4
- **H18.4** Standard e certificazioni professionali · [3] · ⟵ U9.3
- **H18.5** Formazione continua · [2] · ⟵ H18.1
