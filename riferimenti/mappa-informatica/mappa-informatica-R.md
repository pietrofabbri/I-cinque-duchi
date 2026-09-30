# Mappa dell'informatica — Area R: Robotica, automazione, sistemi embedded e IoT (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** l'informatica che agisce nel mondo fisico: sensori, attuatori, microcontrollori, programmazione embedded, controlli automatici, automazione industriale, robotica, robotica autonoma, veicoli e droni, Internet delle cose, sistemi cyber-fisici, robotica educativa, cibernetica.

---

## R1 Sensori e attuatori
- **R1.1** Sistemi che percepiscono e agiscono: sensori, controllore, attuatori · [1] · ⟵ —
- **R1.2** Sensori digitali e analogici · [1] · ⟵ R1.1, B1.2
- **R1.3** Sensori comuni: luce, temperatura, distanza (ultrasuoni, infrarossi), pulsanti · [1] · ⟵ R1.2
- **R1.4** Sensori avanzati: accelerometro, giroscopio, unità inerziali, encoder, telecamera, LIDAR · [2–3] · ⟵ R1.3
- **R1.5** Rumore e calibrazione; filtraggio semplice · [2] · ⟵ R1.3, A7.1.3
- **R1.6** Attuatori semplici: LED, cicalini, relè · [1] · ⟵ R1.1
- **R1.7** Motori in corrente continua, passo-passo, servomotori · [1–2] · ⟵ R1.6, C1.3
- **R1.8** Pilotare i motori: ponte H e driver · [2] · ⟵ R1.7, C4.1

## R2 Microcontrollori
- **R2.1** Schede per la didattica: micro:bit, Arduino, Raspberry Pi Pico · [1] · ⟵ R1.1
- **R2.2** Ingressi e uscite digitali (GPIO) · [1] · ⟵ R2.1, B1.6
- **R2.3** Ingressi analogici · [1–2] · ⟵ R2.2, R1.2
- **R2.4** Uscite PWM · [1–2] · ⟵ R2.2
- **R2.5** Comunicazione seriale con il computer · [2] · ⟵ R2.2, C11.5
- **R2.6** Bus per sensori: I²C e SPI · [2–3] · ⟵ R2.5, C11.7
- **R2.7** Alimentazione e consumi dei progetti · [2] · ⟵ R2.1, C13.1
- **R2.8** Raspberry Pi come computer embedded con Linux · [2] · ⟵ R2.1, I8.1

## R3 Programmazione embedded
- **R3.1** Il ciclo principale (setup e loop) · [1] · ⟵ R2.1, E3.4
- **R3.2** Programmare a blocchi (MakeCode) e in testo (C++ per Arduino, MicroPython) · [1–2] · ⟵ R3.1, G1.7
- **R3.3** Temporizzazione non bloccante · [2] · ⟵ R3.1
- **R3.4** Interruzioni · [2–3] · ⟵ R3.3, D9.3
- **R3.5** Macchine a stati nei dispositivi · [2–3] · ⟵ R3.3, F1.1
- **R3.6** Vincoli di memoria e di tempo reale · [3] · ⟵ R3.4, D13.1
- **R3.7** Sistemi operativi real-time per microcontrollori · [3–4] · ⟵ R3.6, I8.5
- **R3.8** Debugging sull'hardware · [2–3] · ⟵ R3.2, C1.9

## R4 Controlli automatici
- **R4.1** Sistemi ad anello aperto e ad anello chiuso · [1–2] · ⟵ R1.1
- **R4.2** Controllo on-off con isteresi (termostato) · [1–2] · ⟵ R4.1
- **R4.3** Modellare un sistema dinamico · [3] · ⟵ R4.1, A6.4.2
- **R4.4** Funzione di trasferimento e schemi a blocchi · [3] · ⟵ R4.3, A6.4.6
- **R4.5** Il controllore PID: azioni proporzionale, integrale, derivativa · [2–3] · ⟵ R4.2, A6.2.1
- **R4.6** Taratura del PID · [3] · ⟵ R4.5
- **R4.7** Stabilità · [3] · ⟵ R4.4, A6.4.3
- **R4.8** Controllo digitale e campionamento · [3] · ⟵ R4.5, B7.2
- **R4.9** Controllo nello spazio degli stati e controllo ottimo · [4] · ⟵ R4.7, A5.3.1
- **R4.10** Controllo fuzzy e basato sull'apprendimento · [4] · ⟵ R4.5, O3.5

## R5 Automazione industriale
- **R5.1** L'automazione industriale: dalla catena di montaggio a Industria 4.0 · [1–2] · ⟵ R4.1
- **R5.2** Controllori a logica programmabile (PLC) · [2] · ⟵ R5.1, D1.2
- **R5.3** Linguaggi IEC 61131-3: ladder, testo strutturato, SFC · [2–3] · ⟵ R5.2, F1.1
- **R5.4** Sensori e attuatori industriali; pneumatica · [2] · ⟵ R5.1, R1.4
- **R5.5** SCADA e interfacce operatore (HMI) · [3] · ⟵ R5.2
- **R5.6** Reti e protocolli industriali (Modbus, OPC UA) · [3] · ⟵ R5.5, J3.3
- **R5.7** Sicurezza dei sistemi industriali · [3–4] · ⟵ R5.6, N7.3

## R6 Robotica

### R6.1 Tipi di robot e cinematica
- **R6.1.1** Tipi di robot (manipolatori, mobili, umanoidi); gradi di libertà · [1–2] · ⟵ R1.1
- **R6.1.2** Robot mobili su ruote: cinematica differenziale · [2–3] · ⟵ R6.1.1, A6.1.2
- **R6.1.3** Cinematica diretta dei manipolatori · [3] · ⟵ R6.1.1, A5.2.3
- **R6.1.4** Cinematica inversa · [3–4] · ⟵ R6.1.3, A10.2.1

### R6.2 Dinamica
- **R6.2.1** Forze, coppie, inerzia · [3] · ⟵ R6.1.3
- **R6.2.2** Controllo del moto dei giunti · [3–4] · ⟵ R6.2.1, R4.5

### R6.3 Pianificazione del moto
- **R6.3.1** Seguire una linea, evitare ostacoli: comportamenti reattivi · [1–2] · ⟵ R6.1.1, R1.3
- **R6.3.2** Mappe a griglia e ricerca del percorso · [2–3] · ⟵ R6.3.1, E7.3.1
- **R6.3.3** Pianificazione nello spazio delle configurazioni; algoritmi a campionamento (RRT) · [4] · ⟵ R6.3.2, R6.1.4
- **R6.3.4** Generazione di traiettorie · [3–4] · ⟵ R6.3.2, A10.2.2

### R6.4 Localizzazione e mappatura
- **R6.4.1** Odometria e deriva · [2–3] · ⟵ R6.1.2, R1.4
- **R6.4.2** Localizzazione probabilistica · [4] · ⟵ R6.4.1, O3.4
- **R6.4.3** Mappatura e SLAM · [4] · ⟵ R6.4.2

### R6.5 Percezione
- **R6.5.1** Fusione di sensori · [3–4] · ⟵ R1.5, A7.2.4
- **R6.5.2** Visione per i robot · [3–4] · ⟵ Q5.5, R6.5.1
- **R6.5.3** Nuvole di punti e percezione 3D · [4] · ⟵ R6.5.2, Q5.3

### R6.6 Software per robot *(nuovo in v1.0)*
- **R6.6** ROS (Robot Operating System) · [3] · ⟵ R6.3.2, M3.10

## R7 Robotica autonoma e apprendimento
- **R7.1** Architetture di controllo: reattive, deliberative, ibride · [3] · ⟵ R6.3.1, O1.5
- **R7.2** Apprendimento per rinforzo in robotica; dalla simulazione al reale · [4] · ⟵ R7.1, O4.4.5
- **R7.3** Apprendimento per imitazione · [4] · ⟵ R7.1, O4.1.2
- **R7.4** Modelli di fondazione per la robotica · [4] · ⟵ R7.2, O6.2

## R8 Robot collaborativi, sociali, umanoidi
- **R8.1** Robot collaborativi e sicurezza nell'interazione fisica · [3] · ⟵ R6.2.2
- **R8.2** Robot sociali e interazione uomo-robot · [3] · ⟵ R7.1, Q8.3
- **R8.3** Robot umanoidi e locomozione su gambe · [4] · ⟵ R6.2.2, R4.9
- **R8.4** Robot di servizio e di assistenza · [3] · ⟵ R8.2
- **R8.5** Etica della robotica · [2–3] · ⟵ R6.1.1, U3.4

## R9 Veicoli autonomi e droni
- **R9.1** Livelli di automazione della guida · [2] · ⟵ R6.1.1
- **R9.2** Architettura di un veicolo autonomo: percezione, previsione, pianificazione, controllo · [4] · ⟵ R6.4.3, R6.5.2, R6.3.3
- **R9.3** Droni: stabilizzazione e controllo del volo · [3–4] · ⟵ R4.5, R1.4
- **R9.4** Norme e questioni di responsabilità · [2–3] · ⟵ R9.1, U3.4

## R10 Internet delle cose
- **R10.1** L'Internet delle cose: dal sensore al cloud · [2] · ⟵ R2.1, J2.1
- **R10.2** Connettività: Wi-Fi, Bluetooth Low Energy, LoRa · [2] · ⟵ R10.1, J4.9
- **R10.3** Protocolli IoT: MQTT · [2–3] · ⟵ R10.2, J7.8
- **R10.4** Piattaforme IoT e dashboard · [2–3] · ⟵ R10.3, M4.1
- **R10.5** Sicurezza e privacy dei dispositivi IoT · [3] · ⟵ R10.1, N1.3
- **R10.6** Domotica e città intelligenti · [2] · ⟵ R10.1
- **R10.7** Agricoltura di precisione e monitoraggio ambientale · [2–3] · ⟵ R10.4 · ⟶ S6

## R11 Sistemi cyber-fisici e gemelli digitali
- **R11.1** Sistemi cyber-fisici: definizione · [3] · ⟵ R10.1, R4.1
- **R11.2** Gemelli digitali · [3–4] · ⟵ R11.1, S1.4
- **R11.3** Sistemi critici per la sicurezza: requisiti e certificazione · [4] · ⟵ R11.1, F9.2

## R12 Robotica educativa
- **R12.1** Robot didattici programmabili (Bee-Bot, LEGO, mBot) · [1] · ⟵ E1.6
- **R12.2** Competizioni di robotica (First LEGO League, RoboCup Junior) · [1–2] · ⟵ R12.1
- **R12.3** Progetti di coding fisico in classe · [1] · ⟵ R12.1, R2.1

## R13 Cibernetica e teoria dei sistemi
- **R13.1** Wiener e la cibernetica: comunicazione e controllo · [2–3] · ⟵ R4.1
- **R13.2** La retroazione nei sistemi naturali e sociali · [2–3] · ⟵ R13.1
- **R13.3** Omeostasi e autoregolazione · [3] · ⟵ R13.2
- **R13.4** Cibernetica di secondo ordine e autopoiesi · [4] · ⟵ R13.3
