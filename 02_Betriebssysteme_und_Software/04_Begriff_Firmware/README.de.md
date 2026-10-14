# Begriff Firmware

## Schneller visueller Überblick

| Begriff        | Was ist das?                                       | Beispiel               |
| -------------- | -------------------------------------------------- | ---------------------- |
| Hardware       | physisches Bauteil                                 | Mainboard, SSD, Router |
| Firmware       | in das Gerät geschriebene Steuerungssoftware       | UEFI, SSD-Firmware     |
| Betriebssystem | Systemsoftware, die den gesamten Rechner verwaltet | Windows, Linux         |
| Anwendung      | Benutzerprogramm                                   | Chrome, Word           |

## Was ist Firmware?

Firmware ist Programmcode und Daten,
die typischerweise fest an die Hardware gebunden gespeichert sind,
oft nicht als herkömmliche Datei,
sondern im eigenen Speicher des Geräts.

Ihre Aufgabe kann zum Beispiel sein:

- die Steuerung des Gerätestarts
- Bereitstellung von Grundfunktionen
- Kommunikation mit anderen Hardwarekomponenten
- Sicherstellung der Betriebslogik des Geräts

## Wo befindet sich die Firmware?

In der Regel:

- im ROM
- im Flash-Speicher
- in einem anderen nichtflüchtigen Speicher

Deshalb ist Firmware „näher an der Hardware" als eine normale Anwendung.

## Typische Beispiele

### 1. BIOS / UEFI

Einer der bekanntesten Firmware-Typen.

Aufgabe:

- Grundstart des Rechners
- Hardwareüberprüfung
- Vorbereitung des Boot-Vorgangs
- Ermöglichung des Starts des Betriebssystems

### 2. Router-Firmware

Aufgabe:

- Steuerung des Netzwerkbetriebs
- Bereitstellung der Admin-Oberfläche
- Sicherheits- und Verbindungsverwaltungsfunktionen

### 3. SSD- oder HDD-Firmware

Aufgabe:

- Steuerung der Datenspeicherungsvorgänge
- Fehlerbehandlung
- Leistungsoptimierung auf bestimmter Ebene

### 4. Firmware von Peripheriegeräten

Zum Beispiel:

- Drucker
- Monitor
- Tastatur
- Maus
- Kamera

## Firmware und allgemeine Anwendungssoftware

| Firmware                     | „Normale" Software                      |
| ---------------------------- | --------------------------------------- |
| direkt an ein Gerät gebunden | läuft in einem allgemeinen System       |
| steuert den Grundbetrieb     | führt Benutzer- oder Systemaufgaben aus |
| oft auf Flash-/ROM-Speicher  | wird auf Massenspeicher installiert     |
| gerätespezifisch             | oft portabler                           |

## Firmware vs Treiber

| Firmware                                | Treiber                               |
| --------------------------------------- | ------------------------------------- |
| steuert den Gerätebetrieb             | typischerweise im Betriebssystem      |
| steuert den internen Betrieb des Geräts | vermittelt zwischen OS und Gerät      |
| eng an die Hardware gebunden            | systemseitiges Schnittstellenprogramm |

Einfach gesagt:

- Firmware = interne Steuerung des Geräts
- Treiber = Verbindung auf Betriebssystemseite

## Warum ist ein Firmware-Update wichtig?

Denn ein Firmware-Update kann verbessern:

- Fehler
- Stabilität
- Kompatibilität
- Sicherheitsprobleme

Es birgt aber auch Risiken:

- bei einem fehlerhaften Update kann das Gerät funktionsunfähig werden

Deshalb sollte Firmware nur:

- aus einer vertrauenswürdigen Quelle
- für das genaue Modell
- mit Bedacht

aktualisiert werden.

## Start und Firmware-Update in der Praxis

Firmware ist ebenfalls **Software**. Ein vollständiges Router-Firmwarepaket kann sogar ein Betriebssystem enthalten. Bei anderen Geräten lädt der Treiber des Hostsystems den Steuerungscode erst beim Start. Der Speicherort allein definiert daher den Begriff nicht.

Die vereinfachte Startkette eines UEFI-PCs lautet: Firmware → Bootmanager / Bootloader → OS-Kernel → Dienste. Secure Boot prüft die Vertrauenswürdigkeit der Startkomponenten; die Verschlüsselung des Datenträgerinhalts ist eine eigene Aufgabe.

**Beispiel:** Für einen Laptop erscheint ein UEFI-Update. Geprüft werden exaktes Modell, Versionshinweise und das Updateverfahren des Herstellers. Stabile Stromversorgung, Datensicherung und bei verschlüsselten Datenträgern ein verfügbarer Wiederherstellungsschlüssel werden vorbereitet. Abschließend werden die neue Version und der normale Systemstart kontrolliert.

## Prüfungstaugliche Formulierung

> Firmware ist eine an die Hardware gebundene, eingebettete Steuerungssoftware.  
> Sie befindet sich in der Regel im nichtflüchtigen Speicher des Geräts und steuert dessen Grundbetrieb.  
> Ein typisches Beispiel ist das BIOS oder UEFI, aber auch in Routern, SSDs und Peripheriegeräten gibt es Firmware.  
> Firmware ist nicht dasselbe wie ein Betriebssystem oder eine Anwendung.

## Schnelle Selbstkontrolle

1. Was ist Firmware?
2. Worin unterscheidet sie sich von einer Anwendung?
3. Worin unterscheidet sie sich von einem Treiber?
4. Nenne zwei Beispiele für Firmware.
5. Warum kann ein Firmware-Update notwendig sein?

## Kurzantworten zur Selbstkontrolle

1. An die Hardware gebundene, eingebettete Steuerungssoftware
2. Die Anwendung ist ein Benutzerprogramm, die Firmware steuert den Grundbetrieb des Geräts
3. Firmware steuert die Hardware, der Treiber vermittelt auf OS-Seite; manche Firmware wird erst durch den Treiber geladen
4. BIOS/UEFI, Router-Firmware, SSD-Firmware
5. Zur Fehlerbehebung, Kompatibilität, Stabilität und Sicherheit

## Quellen

1. NIST CSRC Glossary - firmware  
   https://csrc.nist.gov/glossary/term/firmware  
   Verwendung: fachliche Definition des Begriffs Firmware.

2. Microsoft Support - How to use Surface UEFI  
   https://support.microsoft.com/en-us/surface/how-to-use-surface-uefi-df2c8942-dfa0-859d-4394-95f45eb1c3f9  
   Verwendung: UEFI als heute noch relevantes Firmware-Beispiel.

3. Ubuntu Desktop  
   https://ubuntu.com/download/desktop  
   Verwendung: Kontext zur Firmware-Update-Praxis auch in modernen Desktop-Umgebungen.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Linux Kernel: Firmware API](https://docs.kernel.org/driver-api/firmware/introduction.html): vom Hostsystem geladene Firmware.
- [Microsoft: Secure the Windows boot process](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process): Startkette und Secure Boot.

Geprüft: `2026-10-14`.
