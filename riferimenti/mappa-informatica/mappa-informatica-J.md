# Mappa dell'informatica — Area J: Reti e telecomunicazioni (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** dalla comunicazione di base ai protocolli di Internet, strato per strato; reti mobili, programmazione di rete, gestione, reti moderne e quantistiche, standard. Il livello fisico dei mezzi trasmissivi è nell'area C; la crittografia dei protocolli sicuri è nell'area N.

---

## J1 Fondamenti di comunicazione
- **J1.1** Sistema di comunicazione: sorgente, trasmettitore, canale, ricevitore · [1] · ⟵ B1.2
- **J1.2** Banda, velocità di trasmissione, latenza · [1–2] · ⟵ J1.1, B3.4
- **J1.3** Trasmissione analogica e digitale; modulazione · [2] · ⟵ J1.1, C14.1
- **J1.4** Multiplazione a divisione di tempo, di frequenza, di codice · [2–3] · ⟵ J1.3
- **J1.5** Capacità di un canale; legge di Shannon-Hartley · [3] · ⟵ J1.2, A8.3.2, C14.5
- **J1.6** Simplex, half-duplex, full-duplex; trasmissione sincrona e asincrona · [1–2] · ⟵ J1.1

## J2 Tipi e topologie di rete
- **J2.1** Che cos'è una rete: nodi, collegamenti, vantaggi · [1] · ⟵ J1.1
- **J2.2** Classificazione per estensione: PAN, LAN, MAN, WAN · [1] · ⟵ J2.1
- **J2.3** Topologie fisiche e logiche: bus, stella, anello, maglia · [1] · ⟵ J2.1, A4.3.1
- **J2.4** Commutazione di circuito e di pacchetto · [2] · ⟵ J2.1
- **J2.5** Architetture client-server e peer-to-peer · [1–2] · ⟵ J2.1
- **J2.6** Dispositivi di rete: scheda di rete, hub, switch, router, access point, modem · [1–2] · ⟵ J2.3

## J3 Modelli a strati
- **J3.1** Perché gli strati: protocollo, servizio, interfaccia · [2] · ⟵ J2.4
- **J3.2** Il modello ISO/OSI · [2] · ⟵ J3.1
- **J3.3** La pila TCP/IP e il confronto con OSI · [2] · ⟵ J3.2
- **J3.4** Incapsulamento: intestazioni e unità di dati (trama, pacchetto, segmento) · [2] · ⟵ J3.3
- **J3.5** Analizzare il traffico con Wireshark · [2–3] · ⟵ J3.4, B2.2.3
- **J3.6** Protocolli di comunicazione prima di Internet: telegrafo, telefono, X.25 · [2–3] · ⟵ J3.3 · (v1.1, approfondimento)

## J4 Livello fisico e di collegamento
- **J4.1** Livello fisico: cablaggio strutturato, connettori, categorie di cavi · [2] · ⟵ C14.2, J3.2
- **J4.2** Livello di collegamento: trame e indirizzi MAC · [2] · ⟵ J3.4, B2.2.3
- **J4.3** Controllo degli errori sul collegamento (CRC) · [2] · ⟵ J4.2, B10.2.1
- **J4.4** Accesso al mezzo: CSMA/CD e CSMA/CA · [2–3] · ⟵ J4.2
- **J4.5** Ethernet: evoluzione e velocità · [2] · ⟵ J4.4
- **J4.6** Lo switch: tabella MAC, apprendimento, domini di collisione e di broadcast · [2] · ⟵ J4.5
- **J4.7** VLAN · [3] · ⟵ J4.6
- **J4.8** Spanning Tree Protocol · [3] · ⟵ J4.6, E7.3.6
- **J4.9** Wi-Fi (IEEE 802.11): standard, canali, SSID · [2] · ⟵ J4.4, C14.4
- **J4.10** Bluetooth, Zigbee e reti personali · [2] · ⟵ J4.2, C14.4
- **J4.11** Protocollo ARP · [2] · ⟵ J4.2, J5.1

## J5 Livello di rete
- **J5.1** Indirizzi IPv4: struttura, notazione, classi storiche · [2] · ⟵ J3.4, B2.1.4
- **J5.2** Maschere di sottorete e CIDR; calcolo delle sottoreti · [2] · ⟵ J5.1, B2.3.5
- **J5.3** Indirizzi privati e pubblici; NAT · [2] · ⟵ J5.1
- **J5.4** Instradamento: tabelle di routing, gateway predefinito · [2] · ⟵ J5.2
- **J5.5** Protocolli di instradamento: distance vector (RIP) e link state (OSPF) · [3] · ⟵ J5.4, E7.3.4, E7.3.5
- **J5.6** ICMP: ping e traceroute · [2] · ⟵ J5.1
- **J5.7** IPv6: indirizzamento, autoconfigurazione, transizione · [2–3] · ⟵ J5.2, B2.2.1
- **J5.8** Frammentazione e MTU · [3] · ⟵ J5.1
- **J5.9** Configurare una rete in un simulatore (Packet Tracer) · [2] · ⟵ J5.4, J4.6
- **J5.10** IPv6 in pratica: gli indirizzi della propria rete · [2–3] · ⟵ J5.7 · (v1.1, approfondimento)

## J6 Livello di trasporto
- **J6.1** Porte e multiplazione delle applicazioni · [2] · ⟵ J5.1
- **J6.2** UDP · [2] · ⟵ J6.1
- **J6.3** TCP: connessione (three-way handshake), affidabilità, numeri di sequenza · [2–3] · ⟵ J6.1, B10.1.5
- **J6.4** Controllo di flusso: la finestra scorrevole · [3] · ⟵ J6.3
- **J6.5** Controllo della congestione · [3] · ⟵ J6.4
- **J6.6** QUIC e protocolli di trasporto recenti · [3–4] · ⟵ J6.5, J6.2
- **J6.7** I socket come interfaccia verso il trasporto · [2–3] · ⟵ J6.1

## J7 Livello applicativo
- **J7.1** DNS: nomi di dominio, gerarchia, risoluzione · [2] · ⟵ J6.2, A4.3.3
- **J7.2** DHCP · [2] · ⟵ J5.1, J6.2
- **J7.3** HTTP: richieste e risposte, metodi, codici di stato, intestazioni · [2] · ⟵ J6.3
- **J7.4** HTTPS e TLS: visione d'insieme · [2] · ⟵ J7.3 · ⟶ N4
- **J7.5** Posta elettronica: SMTP, IMAP, POP3 · [2] · ⟵ J6.3, J7.1
- **J7.6** Trasferimento di file (FTP, SFTP) e accesso remoto (SSH) · [2] · ⟵ J6.3
- **J7.7** Protocolli per il tempo reale e lo streaming (RTP, WebRTC) · [3] · ⟵ J6.2
- **J7.8** Protocolli per l'IoT (MQTT, CoAP) · [2–3] · ⟵ J6.3 · ⟶ R10
- **J7.9** Sincronizzazione dell'orologio (NTP) · [2–3] · ⟵ J6.2

## J8 Internet
- **J8.1** Struttura di Internet: provider, punti di interscambio, dorsali · [1–2] · ⟵ J2.2
- **J8.2** Sistemi autonomi e BGP · [3] · ⟵ J8.1, J5.5
- **J8.3** Cavi sottomarini e infrastruttura fisica globale · [1–2] · ⟵ J8.1
- **J8.4** Tecnologie di accesso: DSL, fibra, rete mobile, satellite · [1–2] · ⟵ J8.1
- **J8.5** Misurare la connessione: velocità, latenza, jitter · [1–2] · ⟵ J1.2

## J9 Reti mobili e wireless
- **J9.1** Reti cellulari: celle e handover · [2] · ⟵ C14.4, J2.2
- **J9.2** Generazioni dal 2G al 5G, verso il 6G · [2] · ⟵ J9.1
- **J9.3** Reti satellitari (orbite geostazionarie e basse) · [2] · ⟵ J9.1
- **J9.4** Reti a basso consumo e lungo raggio (LoRaWAN, NB-IoT) · [3] · ⟵ J9.1 · ⟶ R10
- **J9.5** Localizzazione: GPS e triangolazione · [2] · ⟵ C14.4, A5.1.3

## J10 Programmazione di rete
- **J10.1** Client e server con socket TCP · [2–3] · ⟵ J6.7, G1.8
- **J10.2** Socket UDP · [3] · ⟵ J10.1, J6.2
- **J10.3** Server concorrenti (thread, eventi) · [3] · ⟵ J10.1, G3.7.4
- **J10.4** Protocolli applicativi su misura; serializzazione dei messaggi · [3] · ⟵ J10.1, B11.4
- **J10.5** Chiamate di procedura remota (RPC, gRPC) · [3] · ⟵ J10.4
- **J10.6** Applicazioni peer-to-peer · [3] · ⟵ J10.1, J2.5

## J11 Gestione e sicurezza di rete
- **J11.1** Firewall: filtro dei pacchetti, stateful, applicativi · [2] · ⟵ J6.1
- **J11.2** VPN · [2–3] · ⟵ J11.1, J7.4
- **J11.3** Segmentazione della rete e DMZ · [3] · ⟵ J11.1, J4.7
- **J11.4** Monitoraggio della rete (SNMP, NetFlow) · [3] · ⟵ J6.2
- **J11.5** Qualità del servizio (QoS) · [3] · ⟵ J6.5
- **J11.6** Proxy e proxy inversi · [2–3] · ⟵ J7.3

## J12 Reti moderne
- **J12.1** Reti definite dal software (SDN) · [4] · ⟵ J5.5
- **J12.2** Reti per la distribuzione di contenuti (CDN) · [3] · ⟵ J7.1, J7.3
- **J12.3** Edge computing e reti 5G programmabili · [4] · ⟵ J9.2, J12.1
- **J12.4** Reti dei data center · [4] · ⟵ J4.6, J5.5
- **J12.5** Reti tolleranti al ritardo; reti interplanetarie · [4] · ⟵ J6.3

## J13 Reti quantistiche
- **J13.1** Distribuzione quantistica delle chiavi in rete · [4] · ⟵ T9
- **J13.2** Ripetitori quantistici e Internet quantistica · [4] · ⟵ J13.1, T2

## J14 Standard e governance di Internet
- **J14.1** Enti di standardizzazione: IETF, IEEE, ITU, W3C, ISO · [2] · ⟵ J3.1
- **J14.2** Le RFC: come nasce un protocollo · [2–3] · ⟵ J14.1
- **J14.3** Governance di Internet: ICANN, gestione di nomi e numeri · [2–3] · ⟵ J14.1, J7.1
- **J14.4** Neutralità della rete · [2] · ⟵ J8.1 · ⟶ U4
