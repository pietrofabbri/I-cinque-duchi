# Mappa dell'informatica — Area N: Sicurezza informatica e crittografia (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** concetti di sicurezza, crittografia dalla classica alla post-quantistica, protocolli sicuri, autenticazione, sicurezza del software, delle reti, dell'hardware e dell'IA, fattore umano, privacy, informatica forense, governance. I nodi offensivi sono trattati a livello concettuale e difensivo.

---

## N1 Concetti di base
- **N1.1** Sicurezza informatica: riservatezza, integrità, disponibilità · [1] · ⟵ —
- **N1.2** Autenticità, non ripudio, responsabilità · [2] · ⟵ N1.1
- **N1.3** Minacce, vulnerabilità, attacchi, rischio · [1–2] · ⟵ N1.1
- **N1.4** Chi attacca e perché · [2] · ⟵ N1.3
- **N1.5** Principi di progettazione: privilegio minimo, difesa in profondità, sicurezza predefinita · [2–3] · ⟵ N1.3
- **N1.6** Superficie d'attacco e modellazione delle minacce (STRIDE) · [3] · ⟵ N1.5

## N2 Crittografia classica
- **N2.1** Storia e terminologia: testo in chiaro, testo cifrato, chiave · [1] · ⟵ —
- **N2.2** Cifrari a sostituzione: il cifrario di Cesare · [1] · ⟵ N2.1, A1.4.1
- **N2.3** Crittoanalisi con l'analisi delle frequenze · [1] · ⟵ N2.2, A7.1.2
- **N2.4** Il cifrario di Vigenère e come si rompe · [1–2] · ⟵ N2.3
- **N2.5** Cifrari a trasposizione · [1] · ⟵ N2.1
- **N2.6** Principio di Kerckhoffs · [2] · ⟵ N2.4
- **N2.7** One-time pad e sicurezza perfetta · [2] · ⟵ N2.4, A2.1.3
- **N2.8** Enigma e le macchine cifranti · [1–2] · ⟵ N2.4
- **N2.9** Steganografia: nascondere l'esistenza di un messaggio · [1] · ⟵ N2.1 · (v1.1, approfondimento)
- **N2.10** Cifrari del Rinascimento: il disco di Leon Battista Alberti · [1–2] · ⟵ N2.4 · (v1.1, approfondimento)

## N3 Crittografia moderna

### N3.1 Crittografia simmetrica
- **N3.1.1** Cifrari a blocchi e a flusso · [2–3] · ⟵ N2.7, B2.3.5
- **N3.1.2** DES e AES · [3] · ⟵ N3.1.1
- **N3.1.3** Modalità operative (ECB, CBC, CTR, GCM) · [3] · ⟵ N3.1.2
- **N3.1.4** Generatori di numeri casuali crittograficamente sicuri · [3] · ⟵ A7.2.5

### N3.2 Funzioni hash
- **N3.2.1** Funzioni hash crittografiche e loro proprietà · [2–3] · ⟵ E6.5.1
- **N3.2.2** SHA-2 e SHA-3 · [3] · ⟵ N3.2.1
- **N3.2.3** Codici di autenticazione dei messaggi (HMAC) · [3] · ⟵ N3.2.1, N3.1.1
- **N3.2.4** Memorizzare le password: sale e funzioni lente (bcrypt, Argon2) · [2–3] · ⟵ N3.2.1
- **N3.2.5** Paradosso del compleanno e collisioni · [3] · ⟵ N3.2.1, A7.2.2

### N3.3 Crittografia asimmetrica
- **N3.3.1** L'idea della crittografia a chiave pubblica · [2] · ⟵ N2.6
- **N3.3.2** Scambio di chiavi Diffie-Hellman · [2–3] · ⟵ N3.3.1, A1.4.1
- **N3.3.3** RSA · [3] · ⟵ N3.3.1, A1.4.4, A1.3.5
- **N3.3.4** Crittografia su curve ellittiche · [4] · ⟵ N3.3.1, A4.4.6
- **N3.3.5** Cifratura ibrida · [3] · ⟵ N3.3.3, N3.1.2

### N3.4 Firme digitali, certificati, PKI
- **N3.4.1** Firma digitale · [2–3] · ⟵ N3.3.1, N3.2.1
- **N3.4.2** Certificati X.509 e autorità di certificazione · [3] · ⟵ N3.4.1
- **N3.4.3** PKI, catene di fiducia, revoca · [3] · ⟵ N3.4.2
- **N3.4.4** Firma elettronica qualificata e regolamento eIDAS · [2–3] · ⟵ N3.4.1

### N3.5 Crittografia avanzata
- **N3.5.1** Prove a conoscenza zero · [4] · ⟵ N3.3.1, F11.3
- **N3.5.2** Crittografia omomorfica · [4] · ⟵ N3.3.1, A4.4.3
- **N3.5.3** Calcolo multiparte sicuro · [4] · ⟵ N3.3.1
- **N3.5.4** Condivisione di segreti (schema di Shamir) · [3–4] · ⟵ A1.5.4, A4.4.3

## N4 Protocolli sicuri
- **N4.1** TLS: handshake, negoziazione, certificati · [3] · ⟵ N3.3.5, N3.4.2, J7.4
- **N4.2** SSH: chiavi e autenticazione · [2–3] · ⟵ N3.3.1, J7.6
- **N4.3** Posta sicura (PGP, S/MIME) e autenticazione del dominio (SPF, DKIM, DMARC) · [3] · ⟵ N3.4.1, J7.5
- **N4.4** Messaggistica cifrata da estremo a estremo (protocollo Signal) · [3–4] · ⟵ N3.3.2
- **N4.5** DNSSEC · [3–4] · ⟵ N3.4.1, J7.1
- **N4.6** Sicurezza del Wi-Fi (WPA2, WPA3) · [2–3] · ⟵ J4.9, N3.1.1

## N5 Autenticazione e controllo degli accessi
- **N5.1** Identificazione, autenticazione, autorizzazione · [1–2] · ⟵ N1.1
- **N5.2** Fattori di autenticazione; password robuste e gestori di password · [1] · ⟵ N5.1
- **N5.3** Autenticazione a più fattori; codici monouso · [1–2] · ⟵ N5.2
- **N5.4** Passkey e FIDO2 · [2–3] · ⟵ N5.3, N3.3.1
- **N5.5** Identità digitale: SPID, CIE · [1–2] · ⟵ N5.3
- **N5.6** Modelli di controllo degli accessi: DAC, MAC, RBAC, ABAC · [3] · ⟵ N5.1, I5.4
- **N5.7** Single sign-on e federazione delle identità · [3] · ⟵ N5.6
- **N5.8** Biometria · [2–3] · ⟵ N5.2

## N6 Sicurezza del software
- **N6.1** Vulnerabilità e loro classificazione (CVE, CWE, CVSS) · [2–3] · ⟵ N1.3
- **N6.2** Validazione dell'input · [2] · ⟵ N6.1, G1.14
- **N6.3** Iniezioni (SQL, comandi) · [2–3] · ⟵ N6.2, L5.12
- **N6.4** Cross-site scripting (XSS) e CSRF · [3] · ⟵ N6.2, K4.2
- **N6.5** Buffer overflow e corruzione della memoria · [3] · ⟵ G4.5, D7.4
- **N6.6** Mitigazioni: ASLR, canary, DEP, linguaggi sicuri per la memoria · [3–4] · ⟵ N6.5, I4.8
- **N6.7** Gestire in modo sicuro i segreti nel codice · [2–3] · ⟵ N6.1
- **N6.8** Divulgazione responsabile e bug bounty · [3] · ⟵ N6.1

## N7 Sicurezza di reti e sistemi
- **N7.1** Malware: virus, worm, trojan, ransomware (concetti) · [1–2] · ⟵ N1.3
- **N7.2** Antivirus e rilevamento · [2] · ⟵ N7.1
- **N7.3** Attacchi di rete: intercettazione, spoofing, man-in-the-middle, DoS e DDoS · [2–3] · ⟵ N1.3, J3.4
- **N7.4** Difesa perimetrale: firewall, IDS/IPS · [3] · ⟵ N7.3, J11.1
- **N7.5** Architettura zero trust · [3–4] · ⟵ N7.4, N5.6
- **N7.6** Sicurezza dei sistemi operativi: aggiornamenti, privilegi, hardening · [2–3] · ⟵ N7.1, I11.1
- **N7.7** Penetration testing e competizioni CTF (in ambito etico) · [3] · ⟵ N7.3, N6.3
- **N7.8** Centri operativi di sicurezza (SOC) e SIEM · [3–4] · ⟵ N7.4, I11.4

## N8 Sicurezza dell'hardware
- **N8.1** Attacchi fisici ai dispositivi · [3] · ⟵ N1.3, C11.1
- **N8.2** Canali laterali: tempi, consumo, emissioni · [3–4] · ⟵ N8.1, N3.1.2
- **N8.3** Spectre e Meltdown · [4] · ⟵ D10.6, D8.4
- **N8.4** Moduli di sicurezza hardware: TPM, enclave sicure · [3–4] · ⟵ N3.3.1, I10.2
- **N8.5** Sicurezza della filiera dell'hardware · [4] · ⟵ C8.6, N8.1

## N9 Fattore umano
- **N9.1** Ingegneria sociale · [1] · ⟵ N1.1
- **N9.2** Phishing: riconoscerlo e difendersi · [1] · ⟵ N9.1
- **N9.3** Igiene digitale: aggiornamenti, backup, password · [1] · ⟵ N9.1
- **N9.4** Sicurezza dei dispositivi mobili e delle reti pubbliche · [1–2] · ⟵ N9.3
- **N9.5** Consapevolezza e formazione nelle organizzazioni · [2–3] · ⟵ N9.2

## N10 Crittografia post-quantistica
- **N10.1** La minaccia quantistica a RSA e alle curve ellittiche · [3] · ⟵ N3.3.3, T5.3
- **N10.2** Famiglie post-quantistiche: reticoli, hash, codici · [4] · ⟵ N10.1, A11.4
- **N10.3** Standard NIST (ML-KEM, ML-DSA) e migrazione · [4] · ⟵ N10.2
- **N10.4** "Raccogli ora, decifra dopo" · [3] · ⟵ N10.1

## N11 Tecnologie per la privacy
- **N11.1** Tracciamento e profilazione online: come funzionano · [2] · ⟵ U7.2
- **N11.2** Anonimato, pseudonimato, reidentificazione · [3] · ⟵ N11.1, L1.1
- **N11.3** k-anonimato · [3] · ⟵ N11.2
- **N11.4** Privacy differenziale · [4] · ⟵ N11.2, A7.3.3
- **N11.5** Reti di anonimato (Tor) · [3] · ⟵ N11.2, N3.3.5, J5.4
- **N11.6** Tecniche per la privacy nell'IA: apprendimento federato · [4] · ⟵ N11.4, O4

## N12 Informatica forense
- **N12.1** Principi e catena di custodia · [3] · ⟵ N1.3
- **N12.2** Acquisizione e analisi di dischi e memorie · [3–4] · ⟵ N12.1, I5.3
- **N12.3** Analisi del traffico di rete e dei log · [3–4] · ⟵ N12.1, J3.5
- **N12.4** Analisi forense dei dispositivi mobili · [4] · ⟵ N12.2

## N13 Sicurezza dell'IA
- **N13.1** Esempi avversari · [4] · ⟵ O5.2
- **N13.2** Avvelenamento dei dati e backdoor · [4] · ⟵ O4.3
- **N13.3** Prompt injection e sicurezza degli agenti · [3] · ⟵ O6.7
- **N13.4** Estrazione del modello e attacchi alla privacy (membership inference) · [4] · ⟵ O4.3, N11.2
- **N13.5** L'IA per difendere e per attaccare · [3] · ⟵ O4.3.3, N7.4

## N14 Governance della sicurezza
- **N14.1** Gestione del rischio informatico · [3] · ⟵ N1.3
- **N14.2** Politiche di sicurezza e classificazione delle informazioni · [3] · ⟵ N14.1
- **N14.3** Standard: ISO/IEC 27001, framework NIST · [3] · ⟵ N14.2
- **N14.4** Normativa: NIS2, sicurezza del trattamento nel GDPR, ruolo dell'Agenzia per la cybersicurezza nazionale · [3] · ⟵ N14.2, U4.9
- **N14.5** Risposta agli incidenti · [3] · ⟵ N14.1
- **N14.6** Continuità operativa e disaster recovery · [3] · ⟵ N14.5, I11.3
