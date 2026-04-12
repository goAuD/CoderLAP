# Begriff Betriebssystem

## Schneller visueller Überblick

| Schicht        | Rolle                                      |
| -------------- | ------------------------------------------ |
| Benutzer       | verwendet den Rechner                      |
| Anwendungen    | führen konkrete Aufgaben aus               |
| Betriebssystem | vermittelt, verwaltet, steuert             |
| Hardware       | CPU, RAM, SSD, Display, Tastatur, Netzwerk |

### Einfaches Modell

```text
Benutzer
   ↓
Anwendung
   ↓
Betriebssystem
   ↓
Hardware
```

## Was ist ein Betriebssystem?

Das Betriebssystem, kurz **OS** (`Operating System`), ist die zentrale Systemsoftware eines Computers.

Seine Aufgabe ist es:

- Prozesse zu starten und zu verwalten
- die Prozessorzeit aufzuteilen
- den Speicher zu verwalten
- Dateien und Ordner zu verwalten
- mit der Hardware zu kommunizieren
- eine Benutzeroberfläche bereitzustellen
- sicherzustellen, dass andere Programme ordnungsgemäß laufen können

## Welche Hauptaufgaben hat es?

### 1. Prozessverwaltung

Das Betriebssystem startet, plant und beendet Programme.

Zum Beispiel:

- der Browser läuft
- der Musikplayer läuft
- im Hintergrund läuft ein Update

Diese werden vom OS organisiert.

### 2. Speicherverwaltung

Das Betriebssystem entscheidet:

- welches Programm wie viel Speicher bekommt
- wie verhindert werden kann, dass Programme sich gegenseitig überschreiben

### 3. Dateiverwaltung

Das OS stellt die Verwaltung von Dateien und Ordnern sicher:

- Name
- Speicherort
- Zugriff
- Öffnen
- Speichern
- Löschen

### 4. Geräteverwaltung

Das Betriebssystem steuert den Betrieb der angeschlossenen Hardware:

- Tastatur
- Maus
- Drucker
- Monitor
- Netzwerkkarte
- Massenspeicher

### 5. Benutzeroberfläche

Das OS kann bereitstellen:

- **grafische Oberfläche** (`GUI`)
- **Kommandozeilenoberfläche** (`CLI`)

Beispiele:

- Windows-Desktop
- Linux-Terminal
- macOS Finder und Menüleiste

## Woraus besteht ein Betriebssystem?

Einfache, prüfungstaugliche Aufteilung:

- **Kernel**: der Kern des Systems
- **Treiber** (`Gerätetreiber`): Hardwarekommunikation
- **Dateisystemverwaltung**
- **Benutzeroberfläche**
- **Systemdienste**

## Warum ist es unverzichtbar?

Ohne Betriebssystem könnte der Benutzer nicht komfortabel:

- ein Programm starten
- Dateien verwalten
- das Internet nutzen
- drucken
- mehrere Aufgaben gleichzeitig ausführen

Das OS macht den Computer benutzbar.

## Einfache Beispiele

| Situation                    | Was macht das Betriebssystem?                                    |
| ---------------------------- | ---------------------------------------------------------------- |
| du öffnest eine Datei        | sucht sie, prüft die Berechtigung, übergibt sie an die Anwendung |
| du startest ein Programm     | lädt es in den Speicher, startet den Prozess                     |
| du verbindest dich mit Wi-Fi | verwaltet das Netzwerkgerät und die Verbindung                   |
| du druckst                   | leitet die Daten an das entsprechende Gerät weiter               |

## Betriebssystem vs Anwendung

| Betriebssystem                              | Anwendung                  |
| ------------------------------------------- | -------------------------- |
| stellt den Grundbetrieb des Rechners sicher | löst eine konkrete Aufgabe |
| verwaltet die Hardware                      | nutzt die Dienste des OS   |
| z.B. Windows, macOS, Linux                  | z.B. Word, Chrome, VLC     |

## Prüfungstaugliche Formulierung

> Das Betriebssystem ist die grundlegende Systemsoftware eines Computers,
> die die Hardware-Ressourcen verwaltet und eine Laufzeitumgebung
> für Anwendungen bereitstellt.  
> Es stellt die Verbindung zwischen Benutzer, Programmen und Hardware her.  
> Zu seinen Aufgaben gehören unter anderem die Prozessverwaltung,
> die Speicherverwaltung, die Dateiverwaltung, die Geräteverwaltung
> und die Bereitstellung der Benutzeroberfläche.

## Häufige Prüfungsfehler

- Das Betriebssystem mit Anwendungen verwechseln.
- Sagen, dass das OS nur „Fenster anzeigt".
- Die Rolle der Speicher- und Prozessverwaltung auslassen.
- Kein Beispiel für GUI und CLI nennen können.
- Den Kernel und das gesamte Betriebssystem als völlig identisch betrachten.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe des Betriebssystems?
2. Was ist der Unterschied zwischen einem Betriebssystem und einer Anwendung?
3. Welche Ressourcen verwaltet das OS?
4. Warum ist die Prozessverwaltung wichtig?
5. Welche Benutzeroberflächen kann ein Betriebssystem haben?

## Kurzantworten zur Selbstkontrolle

1. Es verwaltet die Hardware und stellt eine Umgebung für Anwendungen bereit
2. Das OS bildet die Grundlage, die Anwendung erledigt eine konkrete Aufgabe
3. CPU, Speicher, Dateien, Geräte, Netzwerk
4. Weil der gleichzeitige Ablauf mehrerer Programme organisiert werden muss
5. Grafisch (`GUI`) und kommandozeilenbasiert (`CLI`)

## Quellen

1. NIST CSRC Glossary - Operating system  
   https://csrc.nist.gov/glossary/term/operating_system_  
   Verwendung: fachliche Definitionsgrundlage zum Begriff Betriebssystem.

2. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Verwendung: Hauptfunktionen des Betriebssystems wie Prozess-, Speicher- und Dateiverwaltung.

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Verwendung: allgemeinverständliche, moderne Übersicht der Funktionen des Windows-Betriebssystems.

Abgerufen: `2026-04-08`
