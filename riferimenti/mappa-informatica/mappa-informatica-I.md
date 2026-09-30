# Mappa dell'informatica — Area I: Sistemi operativi e software di sistema (dettaglio)

**Versione:** 1.0 · **Data:** 27/09/2026 · **Autore:** Pietro Fabbri (con Claude)
**Documento madre:** `mappa-informatica.md`. **Convenzioni e formato delle righe:** vedi `mappa-informatica-A.md`, §Convenzioni.
**Ambito:** come il software di sistema gestisce le risorse della macchina: processi, concorrenza, memoria, file, I/O, interfacce, virtualizzazione, avvio, amministrazione, prestazioni e affidabilità. Alcuni nodi d'uso (file e cartelle, riga di comando) sono di livello `[1]` e servono presto come prerequisiti pratici.

---

## I1 Ruolo del sistema operativo
- **I1.1** Che cos'è un sistema operativo; gli strati hardware, sistema operativo, applicazioni · [1] · ⟵ D4.2
- **I1.2** Funzioni: gestione delle risorse, astrazione, protezione · [1–2] · ⟵ I1.1
- **I1.3** Kernel e spazio utente; modalità privilegiata · [2] · ⟵ I1.2, D9.3
- **I1.4** Chiamate di sistema · [2–3] · ⟵ I1.3
- **I1.5** Architetture del kernel: monolitico, microkernel, ibrido · [3] · ⟵ I1.3
- **I1.6** Timer e interruzioni come base del multitasking · [2–3] · ⟵ I1.3, D9.3

## I2 Processi e thread
- **I2.1** Programma e processo; stati di un processo · [2] · ⟵ I1.2
- **I2.2** Descrittore di processo e cambio di contesto · [2–3] · ⟵ I2.1, D5.1
- **I2.3** Creazione e terminazione dei processi (fork, exec, wait) · [3] · ⟵ I2.1, I1.4
- **I2.4** Thread: thread utente e thread del kernel · [2–3] · ⟵ I2.1
- **I2.5** Scheduling: obiettivi e metriche · [2] · ⟵ I2.1
- **I2.6** Algoritmi di scheduling: FCFS, SJF, round robin, priorità, code multilivello · [2] · ⟵ I2.5, E6.3.2
- **I2.7** Scheduling real-time e multiprocessore · [3–4] · ⟵ I2.6, D11.1
- **I2.8** Comunicazione fra processi: pipe, memoria condivisa, messaggi, segnali · [3] · ⟵ I2.3

## I3 Concorrenza e sincronizzazione
- **I3.1** Sezione critica e race condition · [2–3] · ⟵ I2.4
- **I3.2** Mutua esclusione: soluzioni software (Peterson) e hardware (test-and-set) · [3] · ⟵ I3.1
- **I3.3** Semafori e mutex · [3] · ⟵ I3.2
- **I3.4** Monitor e variabili di condizione · [3] · ⟵ I3.3
- **I3.5** Problemi classici: produttore-consumatore, lettori-scrittori, filosofi a cena · [3] · ⟵ I3.3
- **I3.6** Stallo: condizioni, prevenzione, rilevazione; algoritmo del banchiere · [3] · ⟵ I3.3, A4.3.2
- **I3.7** Starvation e inversione di priorità · [3] · ⟵ I3.6, I2.6
- **I3.8** Strutture dati senza lock · [4] · ⟵ I3.2

## I4 Gestione della memoria
- **I4.1** Lo spazio degli indirizzi di un processo · [2–3] · ⟵ I2.1, D8.1
- **I4.2** Allocazione contigua e frammentazione · [3] · ⟵ I4.1
- **I4.3** Paginazione e tabella delle pagine · [3] · ⟵ I4.2, D8.7
- **I4.4** Segmentazione · [3] · ⟵ I4.2
- **I4.5** Memoria virtuale; page fault; paginazione su richiesta · [3] · ⟵ I4.3
- **I4.6** Algoritmi di sostituzione delle pagine: FIFO, LRU, orologio · [3] · ⟵ I4.5
- **I4.7** Thrashing e working set · [3] · ⟵ I4.6
- **I4.8** Protezione della memoria e randomizzazione degli indirizzi (ASLR) · [3] · ⟵ I4.3 · ⟶ N6
- **I4.9** File mappati in memoria; memoria condivisa · [3–4] · ⟵ I4.5, I5.3

## I5 File system
- **I5.1** File e cartelle: nomi, estensioni, percorsi assoluti e relativi · [1] · ⟵ —
- **I5.2** Operazioni sui file; metadati e attributi · [1–2] · ⟵ I5.1
- **I5.3** Struttura interna: blocchi, inode, allocazione · [3] · ⟵ I5.2, C10.4
- **I5.4** Permessi e controllo degli accessi (rwx di Unix, ACL) · [2] · ⟵ I5.2
- **I5.5** File system diffusi: FAT, NTFS, ext4, APFS · [2–3] · ⟵ I5.2
- **I5.6** Journaling e consistenza · [3] · ⟵ I5.3
- **I5.7** RAID e gestione dei volumi · [3] · ⟵ I5.3, B10.3.5
- **I5.8** File system di rete e distribuiti · [3–4] · ⟵ I5.3, J10

## I6 I/O e driver
- **I6.1** Il sottosistema di I/O; dispositivi a blocchi e a caratteri · [3] · ⟵ I1.2, D9.1
- **I6.2** Driver di dispositivo · [3] · ⟵ I6.1, D9.3
- **I6.3** Buffering, caching, spooling · [3] · ⟵ I6.1
- **I6.4** Scheduling del disco · [3] · ⟵ I6.1, C10.4
- **I6.5** Plug and play e gestione dell'energia · [3] · ⟵ I6.2, C13.3

## I7 Interfacce utente del sistema
- **I7.1** La riga di comando: shell, comandi di base, navigazione fra cartelle · [1] · ⟵ I5.1
- **I7.2** Interfacce grafiche: finestre, desktop, metafore · [1] · ⟵ —
- **I7.3** Uso consapevole del sistema: impostazioni, aggiornamenti, account · [1] · ⟵ I7.2
- **I7.4** Gestire i processi da utente (gestione attività, top, kill) · [1–2] · ⟵ I7.1
- **I7.5** Gestori di pacchetti e installazione del software · [2] · ⟵ I7.1

## I8 Famiglie di sistemi operativi
- **I8.1** Unix e Linux: filosofia, distribuzioni · [1–2] · ⟵ I7.1
- **I8.2** Windows · [1] · ⟵ I7.2
- **I8.3** macOS · [1] · ⟵ I7.2
- **I8.4** Sistemi mobili (Android, iOS); permessi delle app · [1–2] · ⟵ I7.2
- **I8.5** Sistemi operativi real-time (FreeRTOS, Zephyr) · [3] · ⟵ I2.7
- **I8.6** Sistemi embedded e firmware · [3] · ⟵ D13.1, I1.2
- **I8.7** Sistemi operativi distribuiti e per il cloud · [4] · ⟵ I9.2

## I9 Virtualizzazione e container
- **I9.1** La virtualizzazione: concetto e vantaggi · [2] · ⟵ I1.2
- **I9.2** Macchine virtuali e hypervisor di tipo 1 e 2 · [2–3] · ⟵ I9.1, I1.3
- **I9.3** Container: isolamento con namespace e cgroup · [3] · ⟵ I9.1, I2.1
- **I9.4** Docker: immagini, Dockerfile, registri · [2–3] · ⟵ I9.1, I7.1
- **I9.5** Orchestrazione di container (Kubernetes) · [3–4] · ⟵ I9.4, J5
- **I9.6** Emulazione e sandbox · [3] · ⟵ I9.2

## I10 Avvio e firmware
- **I10.1** Il processo di avvio del computer · [1–2] · ⟵ I1.1
- **I10.2** Firmware BIOS e UEFI; avvio sicuro · [2–3] · ⟵ I10.1, C10.3
- **I10.3** Bootloader e caricamento del kernel · [3] · ⟵ I10.2
- **I10.4** Processo init e gestione dei servizi (systemd) · [3] · ⟵ I10.3, I2.3

## I11 Amministrazione di sistema
- **I11.1** Utenti, gruppi, privilegi (sudo, amministratore) · [2] · ⟵ I5.4
- **I11.2** Installare e aggiornare il sistema · [1–2] · ⟵ I7.3
- **I11.3** Backup: strategia 3-2-1, backup incrementali e differenziali · [1–2] · ⟵ I5.2
- **I11.4** Log di sistema e monitoraggio · [2–3] · ⟵ I7.1
- **I11.5** Servizi, demoni, pianificazione di attività (cron) · [3] · ⟵ I10.4, G5.7.3
- **I11.6** Automazione dell'amministrazione (Ansible) · [3] · ⟵ I11.5, G3.5.4
- **I11.7** Messa in sicurezza di base del sistema · [2–3] · ⟵ I11.1 · ⟶ N7

## I12 Prestazioni e affidabilità dei sistemi
- **I12.1** Metriche: latenza, throughput, utilizzo · [2] · ⟵ I2.5
- **I12.2** Benchmarking e profilazione · [2–3] · ⟵ I12.1, E9.8
- **I12.3** Colli di bottiglia; legge di Little · [3] · ⟵ I12.1
- **I12.4** Teoria delle code applicata ai sistemi · [3] · ⟵ I12.3, A7.5.4
- **I12.5** Affidabilità e disponibilità; i "nove"; MTBF e MTTR · [2–3] · ⟵ I12.1, C17.1
- **I12.6** Tolleranza ai guasti: ridondanza, failover, checkpoint · [3] · ⟵ I12.5
- **I12.7** Pianificazione della capacità · [3] · ⟵ I12.4
- **I12.8** Misurare la propria connessione e il proprio computer: strumenti di benchmark · [2] · ⟵ I12.2 · (v1.1, approfondimento)
