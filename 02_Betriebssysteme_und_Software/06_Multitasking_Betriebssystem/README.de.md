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
- begrenzt durch Trennung und Ressourcenverwaltung gegenseitige Beeinträchtigungen

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

## Ein Kern, drei Aufgaben

In einem einfachen Modell rechnen A und B, während C auf eine Netzwerkantwort wartet. Auf einem CPU-Kern erhält zunächst ein Thread von A Rechenzeit, anschließend B. Während des Wartens benötigt C keine durchgehende CPU-Ausführung; nach Eingang der Antwort kann C wieder ausführungsbereit werden.

Bei **präemptivem Scheduling** kann das OS einem Thread die CPU entziehen und einen anderen auswählen. Im **kooperativen Modell** müssen die Aufgaben bei der Übergabe zusammenarbeiten. Ein Wechsel benötigt das Sichern von Zustand und verursacht deshalb Aufwand.

Auf zwei Kernen können A und B tatsächlich parallel arbeiten. „Das Programm läuft” bedeutet aber nicht, dass jeder seiner Threads gerade auf einer CPU ausgeführt wird. Gemeinsam verwendete Daten können Sperren oder andere Synchronisation benötigen; der OS-Scheduler verhindert nicht von selbst alle Race Conditions der Anwendung.

## Prüfungstaugliche Formulierung

> Ein Multitasking-Betriebssystem ist in der Lage,
> mehrere Prozesse oder Aufgaben so zu verwalten,
> dass sie dem Benutzer als gleichzeitig erscheinen.  
> Dazu plant das System die Prozesse, teilt CPU-Zeit zu,
> verwaltet den Speicher
> und koordiniert Hintergrund- und Vordergrundaufgaben.  
> Moderne Desktop-Betriebssysteme sind in der Regel Multitasking-Systeme.

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

### Geprüfte Quellen zur Ergänzung

- [Microsoft: Processes and threads](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads): Prozess, Thread und Scheduling.

Geprüft: `2026-10-14`.
