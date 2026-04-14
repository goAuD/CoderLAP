# Software Firewall

## Schneller visueller Überblick

| Typ | Wo läuft sie? |
|---|---|
| Software / Host Firewall | auf einem bestimmten Rechner |
| Network / Hardware Firewall | an der Netzwerkgrenze oder vor mehreren Geräten |

## Was ist eine Software Firewall?

Eine Software Firewall:

- läuft auf dem Client-PC oder Server
- regelt die Netzwerkverbindungen lokal

Sie kann beispielsweise filtern nach:

- Programm
- Port
- IP-Adresse
- eingehender oder ausgehender Richtung

## Wofür ist sie gut?

Sie hilft:

- unerwünschte eingehende Verbindungen zu blockieren
- bestimmte ausgehende Verbindungen einzuschränken
- die Netzwerkangriffsfläche zu reduzieren

## Warum ist sie bei Client-Rechnern wichtig?

Weil der Client nicht immer in einem sicheren Netzwerk ist.

Beispiele:

- öffentliches Wi-Fi
- Heimnetzwerk
- Schul- oder Firmennetzwerk

In solchen Fällen ist es besonders wichtig, dass der Rechner sich selbst schützt.

## Worauf muss man achten?

- nicht abschalten, nur weil etwas beim ersten Mal nicht funktioniert
- lieber eine gezielte Ausnahme hinzufügen
- in öffentlichen Netzwerken strengere Regeln verwenden

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Software Firewall | hostbasierte Firewall auf dem Rechner |
| Hardware / Network Firewall | separates Netzwerkgerät oder zentraler Schutz |
| Antivirus | Malware-Erkennung, nicht dasselbe wie eine Firewall |

## Prüfungstaugliche Formulierung

> Die Software Firewall ist eine auf dem lokalen Rechner laufende Firewall,
> die den Netzwerkverkehr filtert
> und Verbindungen anhand von Regeln erlaubt oder blockiert.  
> Sie hilft, unbefugten eingehenden Zugriff zu verhindern,
> und kann in bestimmten Fällen
> auch ausgehende Verbindungen einschränken.  
> Sie ist besonders wichtig bei Client-Rechnern und in nicht vertrauenswürdigen Netzwerkumgebungen.

## Häufige Prüfungsfehler

- Die Firewall mit dem Antivirus verwechseln.
- Sagen, dass sie nur auf Servern wichtig ist.
- Glauben, dass bei einer Blockierung die beste Lösung das vollständige Abschalten der Firewall ist.
- Nicht zwischen Host- und Netzwerk-Firewall unterscheiden.

## Schnelle Selbstkontrolle

1. Was ist eine Software Firewall?
2. Wofür ist sie auf einem Client-PC gut?
3. Nach welchen Kriterien kann sie entscheiden?
4. Ist sie dasselbe wie ein Antivirus?
5. Was ist die bessere Lösung: vollständiges Abschalten oder gezielte Ausnahme?

## Kurzantworten zur Selbstkontrolle

1. Die lokal auf dem Rechner laufende Firewall
2. Zum Filtern des Netzwerkverkehrs und zur Reduzierung der Angriffsfläche
3. Zum Beispiel nach Port, IP-Adresse oder Anwendung
4. Nein
5. Die gezielte Ausnahme

## Quellen

1. NIST CSRC Glossary - Firewall  
   https://csrc.nist.gov/glossary/term/firewall  
   Verwendung: offizielle, standardisierte Definition des Firewall-Begriffs.

2. Microsoft Support - Firewall and Network Protection in the Windows Security App  
   https://support.microsoft.com/en-us/windows/firewall-and-network-protection-in-the-windows-security-app-ec0844f7-aebd-0583-67fe-601ecf5d774f  
   Verwendung: praktische, moderne Windows-Quelle zur Funktionsweise der Host-Firewall.

3. Microsoft Support - Windows Security App Overview  
   https://support.microsoft.com/en-us/office/windows-security-app-overview-ae70cc96-a9cd-4443-a210-e41cb973d3a6  
   Verwendung: Kontext zur Verbindung zwischen lokaler Firewall und anderen Client-Schutzkomponenten.

Abgerufen: `2026-04-08`
