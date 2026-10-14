# Systemprogramm und Anwendungsprogramm

## Schneller visueller Überblick

| Typ                | Wofür?                             | Beispiel                       |
| ------------------ | ---------------------------------- | ------------------------------ |
| Systemprogramm     | stellt den Systembetrieb sicher    | Betriebssystem, Treiber, Shell |
| Anwendungsprogramm | erledigt die Aufgabe des Benutzers | Word, Chrome, Photoshop        |

## Was ist ein Systemprogramm?

Ein Programm, das für den grundlegenden Betrieb des Computers notwendig ist oder diesen unterstützt.

Dazu gehören zum Beispiel:

- Betriebssystem
- Gerätetreiber (`Driver`)
- Kommandointerpreter / Shell
- Systemwerkzeuge
- Hilfsprogramme (`Utilities`)

Hauptmerkmale:

- steht dem System nahe
- kann zwischen Hardware und Anwendungen eine Rolle spielen
- ist nicht unbedingt ein direktes Arbeitswerkzeug des Benutzers

## Was ist ein Anwendungsprogramm?

Ein Programm, das einem konkreten Benutzerzweck dient.

Beispiele:

- Textverarbeitung
- Webbrowser
- Mediaplayer
- Grafikprogramm
- Chat-Anwendung
- Buchhaltungsprogramm

Hauptmerkmale:

- löst eine konkrete Aufgabe des Benutzers
- stützt sich auf die Dienste des Betriebssystems

## Der Unterschied zwischen beiden Begriffen

| Aspekt              | Systemprogramm                                | Anwendungsprogramm                     |
| ------------------- | --------------------------------------------- | -------------------------------------- |
| Hauptzweck          | Betrieb / Unterstützung des Systems           | Lösung einer Benutzeraufgabe           |
| Hardwarenähe        | steht der Hardware in der Regel näher         | steht weiter von der Hardware entfernt |
| Abhängigkeit vom OS | kann Teil davon sein oder eng damit verbunden | läuft auf dem OS                       |
| Beispiel            | Windows, Treiber, PowerShell                  | Excel, Firefox, VLC                    |

## Typische Systemprogramme

### 1. Betriebssystem

Beispiel:

- Windows
- macOS
- Linux

### 2. Gerätetreiber

Aufgabe:

- Verbindung zwischen dem Betriebssystem und der Hardware

### 3. Shell / Kommandointerpreter

Beispiel:

- PowerShell
- Bash

### 4. Hilfsprogramme

Beispiel:

- Datenträgerverwaltung
- Datensicherungstool
- Systemüberwachung

## Typische Anwendungsprogramme

- Microsoft Word
- Google Chrome
- Mozilla Firefox
- VLC Media Player
- Adobe Photoshop
- Visual Studio Code

## Grenzfälle

Die Grenze ist nicht immer scharf.

Zum Beispiel:

- ein Antivirenprogramm ist teilweise systemnah
- ein Dateimanager kann systembezogen sein, aber auch ein Benutzerwerkzeug
- eine Terminalanwendung läuft als Anwendung, kann aber für systemnahe Aufgaben verwendet werden

In der Prüfung ist jedoch das Grundprinzip wichtig:

- Systemprogramm = steht im Zusammenhang mit dem Systembetrieb
- Anwendungsprogramm = löst eine Benutzeraufgabe

## Durchgearbeiteter Fall: Welche Programme braucht das Drucken?

In einem PDF-Reader wird Drucken gewählt. Der Reader ist ein Anwendungsprogramm: Er zeigt das Dokument an und bearbeitet die Benutzeraufgabe. Der Druckdienst des OS verwaltet die Warteschlange, der Treiber unterstützt die Zusammenarbeit mit dem konkreten Gerät. Die Firmware des Druckers steuert das Gerät selbst.

Damit lässt sich eine Störung nach Verantwortungsbereich eingrenzen: Scheitert das Drucken aus allen Anwendungen oder nur bei einem Dokument? Erscheint der Auftrag in der Warteschlange? Ist das Gerät erreichbar? Das ist gezielter, als alle Komponenten neu zu installieren.

Die Einordnung als Systemprogramm beschreibt den **Zweck**. Sie bedeutet nicht automatisch Kernelmodus oder Administratorrechte. Eine Shell ist ein systemnahes Werkzeug und kann trotzdem mit einem normalen Benutzerkonto arbeiten.

## Prüfungstaugliche Formulierung

> Ein Systemprogramm ist Software, die den Grundbetrieb des Computers
> sicherstellt oder unterstützt, zum Beispiel das Betriebssystem,
> Gerätetreiber oder die Shell.  
> Ein Anwendungsprogramm hingegen erledigt eine konkrete Benutzeraufgabe,
> zum Beispiel Textverarbeitung, Webbrowsing oder Medienwiedergabe.  
> Anwendungsprogramme nutzen die Dienste des Betriebssystems.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe eines Systemprogramms?
2. Was ist die Hauptaufgabe eines Anwendungsprogramms?
3. Nenne zwei Beispiele für Systemprogramme.
4. Nenne zwei Beispiele für Anwendungsprogramme.
5. Warum hängt das Anwendungsprogramm vom Betriebssystem ab?

## Kurzantworten zur Selbstkontrolle

1. Es stellt den Systembetrieb sicher oder unterstützt ihn
2. Es löst eine konkrete Benutzeraufgabe
3. Betriebssystem, Treiber, Shell
4. Browser, Textverarbeitung, Mediaplayer
5. Weil es die Dienste des OS nutzt

## Quellen

1. NIST CSRC Glossary - application  
   https://csrc.nist.gov/glossary/term/application  
   Verwendung: der Begriff Anwendung als ausführbare Software.

2. NIST CSRC Glossary - Operating system  
   https://csrc.nist.gov/glossary/term/operating_system_  
   Verwendung: das Betriebssystem als Systemsoftware-Hintergrund.

3. Microsoft Learn - PowerShell Documentation  
   https://learn.microsoft.com/en-us/powershell/  
   Verwendung: Shell und Systemwerkzeug als Beispiel für systemnahe Software.

4. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Verwendung: Kontext zu Systemfunktionen und der OS-abhängigen Funktionsweise von Anwendungen.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Microsoft: User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode): Schutzebenen und Trennung.

Geprüft: `2026-10-14`.
