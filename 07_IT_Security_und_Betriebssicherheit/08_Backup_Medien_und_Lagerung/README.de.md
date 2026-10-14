# Backup Medien und Lagerung

## Schneller visueller Überblick

| Medium | Vorteil | Zu beachten |
|---|---|---|
| externe HDD / SSD | einfach, günstig, schnell | muss physisch geschützt werden |
| NAS | komfortabel, zentral | gegen Ransomware allein nicht ausreichend |
| Tape | kann auch langfristig gut geeignet sein | spezielle Handhabung |
| Cloud Backup | Offsite-Vorteil | Zugriff, Verschlüsselung, Anbieter-Fragen |

## Welche Backup-Medien gibt es?

### Externe HDD / SSD

Vorteil:

- einfach
- schnell
- vielerorts eine günstige Lösung

### NAS

Vorteil:

- zentrale Speicherung
- automatisierbare Sicherungen

Achtung:

- wenn es ständig im Netzwerk erreichbar ist, kann es bei Ransomware gefährdet sein

### Tape

Vorteil:

- in größeren Umgebungen gut einsetzbar
- kann auch für längerfristige Archivierungs- oder Backup-Aufgaben geeignet sein

### Cloud Backup

Vorteil:

- getrennter, externer Standort
- oft leicht skalierbar

Achtung:

- Verschlüsselung
- Zugriffsverwaltung
- rechtliche und Anbieter-Fragen

## Was bedeutet sichere Aufbewahrung?

Das Backup muss so aufbewahrt werden, dass:

- es nicht am selben Ort wie das Originalsystem ist
- es nicht leicht unbefugt zugänglich ist
- es vor Feuer, Wasser, Diebstahl und unbefugtem Zugriff geschützt ist

## Warum ist Offsite- oder getrennte Aufbewahrung wichtig?

Weil ein lokaler Vorfall:

- Feuer
- Einbruch
- Hardwareausfall
- Ransomware

gleichzeitig die Primärdaten und die nahe Sicherung zerstören kann.

## Worauf muss man noch achten?

- Verschlüsselung, wenn sensible Daten in der Sicherung enthalten sind
- physischer Schutz
- Zugriffsrechte
- Beschriftung und Rotation
- regelmäßige Überprüfung und Restore-Test

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Backup-Medium | worauf die Sicherung physisch oder logisch gespeichert wird |
| Speicherort | wo sich die Sicherung befindet |
| online erreichbares Backup | komfortabel, aber angreifbarer |
| Offline / Air-Gapped Backup | getrennt, besser schützbar |

## Medienauswahl anhand des Wiederherstellungsziels

Eine Werkstatt muss 200 GB Daten innerhalb von vier Stunden wiederherstellen. Bei gemessenen dauerhaften 100 MB/s von einer externen Festplatte dauert das reine Kopieren theoretisch `200 000 / 100 = 2000` Sekunden, etwa 33 Minuten. Eine Internetverbindung mit 20 Mbit/s erreicht ideal höchstens 2,5 MB/s. Für dieselben Daten wären das rund 22,2 Stunden. Gerechnet wird mit dezimalen GB/MB; Protokollaufwand, viele kleine Dateien und Entschlüsselung können die Dauer erhöhen. Dieser Downloadweg allein erfüllt das Vier-Stunden-Ziel nicht.

Die lokale Kopie unterstützt schnellen Restore, eine räumlich getrennte Kopie schützt vor örtlichen Schäden. **Offsite** bedeutet anderer Standort, nicht automatisch offline. **Immutable** bedeutet, dass eine Sicherung gemäß dem eingerichteten Schutz für eine festgelegte Zeit nicht verändert oder gelöscht werden kann; das ist nicht dasselbe wie ein physisch getrenntes Medium.

Bei verschlüsselten Backups muss auch der Schlüssel separat geschützt und im Wiederherstellungsfall verfügbar sein. Dokumentiere Medienkennung, Datenstand, Aufbewahrung und Restore-Test. Für lange Aufbewahrung kann eine Migration auf neue Medien nötig werden, damit Laufwerk, Lesegerät und Software weiterhin verfügbar sind. Es gibt keine für jede HDD, SSD oder jedes Band garantierte Lebensdauer.

## Prüfungstaugliche Formulierung

> Beim Backup-Medium und der Aufbewahrung zählt nicht nur die Kapazität,
> sondern auch die Sicherheit und die Wiederherstellbarkeit.  
> Die Sicherungen sollten getrennt vom Originalsystem
> an einem angemessen geschützten Ort aufbewahrt
> und bei sensiblen Daten verschlüsselt werden.  
> Ein ständig im Netzwerk erreichbares Backup allein reicht nicht aus,
> daher kann auch eine Offline- oder Offsite-Kopie wichtig sein.

## Schnelle Selbstkontrolle

1. Nenne drei Backup-Medien.
2. Warum ist ein ständig online erreichbares Backup riskant?
3. Warum ist Offsite-Aufbewahrung wichtig?
4. Wann ist Verschlüsselung wichtig?
5. Reicht es, nur zu sichern, ohne zu testen?

## Kurzantworten zur Selbstkontrolle

1. Externe HDD/SSD, NAS, Tape, Cloud Backup
2. Weil auch ein Angriff oder Ransomware darauf zugreifen kann
3. Weil bei einer lokalen Katastrophe die Sicherung erhalten bleibt
4. Wenn sensible Daten enthalten sind
5. Nein

## Quellen

1. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Verwendung: primäre Quelle für sichere Backup-Medien, getrennte Aufbewahrung und Aufbewahrungsprinzipien.

2. BSI - Datensicherung - wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Verwendung: praktische Medien- und Sicherungsbeispiele, besonders für externe Laufwerke und einfache Sicherungslösungen.

3. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Verwendung: moderne, offizielle Empfehlung für getrennte und mehrkopierte Backup-Strategie.

4. CISA - Back Up Government Data  
   https://www.cisa.gov/audiences/state-local-tribal-and-territorial-government/secure-us-sltt/back-government-data  
   Verwendung: Restore- und Rollback-Aspekte sowie regelmäßige Überprüfung der Sicherungen.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [CISA: Protect stored data](https://www.cisa.gov/resources-tools/training/how-protect-data-stored-your-devices): Trennung externer Sicherungslaufwerke und Schutz gespeicherter Daten
- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide): getrennte, verschlüsselte Sicherungen und geprüfte Wiederherstellung

Geprüft: `2026-10-14`.
