# Multitasking Betriebssystem

## Schneller visueller Überblick

| Situation                  | Was macht das Multitasking-OS?                             |
| -------------------------- | ---------------------------------------------------------- |
| Browser + Musik + Download | plant die Prozesse                                         |
| mehrere Fenster offen      | verwaltet CPU-Zeit und Speicher                            |
| Hintergrund-Update läuft   | organisiert Hintergrund- und Vordergrundaufgaben gemeinsam |

## Was ist Multitasking?

Multitasking bedeutet, dass das Betriebssystem mehrere Prozesse gleichzeitig verwaltet.

Das kann sein:

- echte Parallelität bei mehreren CPU-Kernen
- schnelles Wechseln auf einem Kern, was dem Benutzer wie gleichzeitige Ausführung erscheint

## Was macht das Betriebssystem dabei?

Das OS:

- plant die Aufgaben
- teilt CPU-Zeit zu
- verwaltet den Speicher
- entscheidet, welcher Prozess wann laufen soll
- stellt sicher, dass die Prozesse sich nicht gegenseitig stören

## Beispiel aus der Praxis

Auf einem Laptop laufen gleichzeitig:

- Browser
- Teams oder Chat
- Virenschutz
- Dateisynchronisation
- Musikplayer

Wenn das OS kein Multitasking könnte:

- könnte man nur eine Aufgabe auf einmal normal erledigen

## Warum ist das nützlich?

- verbessert das Benutzererlebnis
- erhöht die Effizienz
- ermöglicht Hintergrundaufgaben
- unterstützt das Zusammenleben moderner Anwendungen

## Vordergrund- und Hintergrundaufgaben

Ein Multitasking-System kann verwalten:

- **im Vordergrund laufende** Aufgaben
- **im Hintergrund laufende** Aufgaben

Beispiele:

- Vordergrund: Dokumentenbearbeitung
- Hintergrund: Update, Synchronisation, Antivirus

## Verwandte Begriffe

### Prozess (`process`)

Eine laufende Instanz eines Programms.

### Thread (`thread`)

Eine Ausführungseinheit innerhalb eines Prozesses.

### Scheduling (`scheduling`)

Der Mechanismus, mit dem das OS entscheidet, welche Aufgabe wann laufen soll.

## Multitasking vs Multiprocessing

| Begriff         | Bedeutung                                            |
| --------------- | ---------------------------------------------------- |
| Multitasking    | Verwaltung mehrerer Aufgaben in einem Betriebssystem |
| Multiprocessing | Nutzung mehrerer Prozessoren / Kerne                 |

Beides hängt zusammen, ist aber nicht dasselbe.

## Multitasking vs Multithreading

| Begriff        | Bedeutung                                               |
| -------------- | ------------------------------------------------------- |
| Multitasking   | Verwaltung mehrerer Prozesse / Aufgaben auf Systemebene |
| Multithreading | Nutzung mehrerer Threads innerhalb eines Programms      |

## Prüfungstaugliche Formulierung

> Ein Multitasking-Betriebssystem ist in der Lage, mehrere Prozesse oder Aufgaben so zu verwalten, dass sie dem Benutzer als gleichzeitig erscheinen.  
> Dazu plant das System die Prozesse, teilt CPU-Zeit zu, verwaltet den Speicher und koordiniert Hintergrund- und Vordergrundaufgaben.  
> Moderne Desktop-Betriebssysteme sind in der Regel Multitasking-Systeme.

## Häufige Prüfungsfehler

- Multitasking mit dem Mehrkernprozessor verwechseln.
- Behaupten, dass Multitasking nur echte Parallelität sein kann.
- Kein Beispiel für einen Hintergrundprozess nennen können.
- Die Begriffe Prozess und Programm als völlig identisch betrachten.
- Multitasking mit Multithreading verwechseln.

## Schnelle Selbstkontrolle

1. Was bedeutet Multitasking?
2. Was ist die Aufgabe eines Multitasking-Betriebssystems?
3. Nenne ein Beispiel für eine Vordergrund- und eine Hintergrundaufgabe.
4. Sind Multitasking und Multiprocessing dasselbe?
5. Warum ist Scheduling wichtig?

## Kurzantworten zur Selbstkontrolle

1. Verwaltung mehrerer Aufgaben gleichzeitig
2. Verwaltung von CPU-Zeit, Speicher und Prozessen
3. Vordergrund: Browser, Hintergrund: Update oder Synchronisation
4. Nein, Multiprocessing bezieht sich auf die Nutzung mehrerer Prozessorkerne
5. Weil entschieden werden muss, welche Aufgabe wann Ressourcen bekommt

## Quellen

1. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Verwendung: Prozessverwaltung, Ressourcenzuweisung und Verwaltung mehrerer Prozesse.

2. Oracle Linux Blog - CFS Group Scheduling  
   https://blogs.oracle.com/linux/post/cfs-group-scheduling  
   Verwendung: moderner Linux-Kernel-Scheduling-Hintergrund und Kontext der „ideal multitasking CPU".

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Verwendung: allgemeinverständliche Zusammenfassung moderner OS-Aufgaben.

Abgerufen: `2026-04-08`
