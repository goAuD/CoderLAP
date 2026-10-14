# Reproduzierbare und nicht reproduzierbare Fehler

## Schneller visueller Überblick

| Fehlertyp | Merkmal |
|---|---|
| reproduzierbar | mit denselben Schritten erneut auslösbar |
| derzeit nicht reproduzierbar | Bedingungen zur Wiederholung sind noch unbekannt |
| intermittierend | tritt nur bei bestimmten Läufen auf |

## Was ist ein reproduzierbarer Fehler?

Wenn unter denselben Bedingungen:

- dieselbe Eingabe
- dieselbe Umgebung
- dieselbe Schrittfolge

erneut derselbe Fehler auftritt, dann ist der Fehler reproduzierbar.

## Was ist ein nicht reproduzierbarer Fehler?

Die beobachtete Abweichung lässt sich mit den derzeit bekannten Schritten nicht
zuverlässig erneut auslösen. Möglicherweise fehlt noch eine Umgebungsbedingung,
ein Zustand oder eine Timinginformation. Tritt die Abweichung gelegentlich
wieder auf, ist sie intermittierend. Bei Tests heißt ein wechselnd erfolgreiches
und fehlgeschlagenes Ergebnis häufig `flaky`.

## Warum ist dieser Unterschied wichtig?

- den reproduzierbaren Fehler kann man leichter analysieren und beheben
- beim nicht reproduzierbaren Fehler ist mehr Datenerhebung nötig
- die Qualität des Fehlertickets beeinflusst die Behebbarkeit erheblich

## Was kann bei nicht reproduzierbaren Fehlern helfen?

- genaue Logs
- Dokumentation der Umgebung
- Dokumentation der Testdaten
- Zeitstempel und Schritte dokumentieren
- Shared State reduzieren

## Fehler und Testinstabilität: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| echter Softwarefehler | fehlerhafte Funktionsweise des Systems |
| instabiles Testergebnis | Ursache kann Timing/Zustand in Anwendung, Test oder Umgebung sein |

## Wiederholbare Bedingungen schaffen

Aus der Meldung „speichert manchmal doppelt“ machen wir eine konkrete Prüfung:
Zwei schnelle Anfragen starten denselben Speichervorgang. Wir dokumentieren
Version, Reihenfolge der Anfragen, anonymisierte Testdaten und beide Antworten.
Den Doppelklick der Oberfläche und parallele Serveranfragen untersuchen wir
getrennt, weil sie unterschiedliche Schichten betreffen.

„Derzeit nicht reproduzierbar“ beschreibt den Untersuchungsstand: Uns fehlt
noch eine zuverlässige Schrittfolge. **Intermittierend** bedeutet, dass die
Erscheinung nur zeitweise auftritt. Auch ein intermittierender Fehler kann durch
kontrolliertes Timing reproduzierbar werden.

Im Test helfen ein fester Startwert des Zufallsgenerators, eine übergebene Uhr,
getrennte Testdaten und das Warten auf einen beobachtbaren Bereitschaftszustand.
Eine längere blinde Wartezeit kann ein Timingproblem lediglich verdecken.
Wir behalten Ergebnisse wiederholter Läufe; ein späterer Erfolg löscht den
Nachweis einer früheren Abweichung nicht. Protokolle enthalten die notwendigen
Diagnosedaten, aber keine Passwörter oder Sitzungstokens.

## Prüfungstaugliche Formulierung

> Ein reproduzierbarer Fehler ist ein Fehler, der mit denselben Eingaben und Schritten zuverlässig erneut ausgelöst  
> werden kann.  
> Bei einem derzeit nicht reproduzierbaren Fehler sind die Bedingungen zur Wiederholung noch unbekannt. Ein  
> intermittierender Fehler tritt nur zeitweise auf und kann unter passenden Bedingungen reproduzierbar werden.  
> Bei solchen Fehlern ist eine detaillierte Fehlerdokumentation, die Logs und die Dokumentation der Umgebungsbedingungen
> besonders wichtig.

## Schnelle Selbstkontrolle

1. Was ist ein reproduzierbarer Fehler?
2. Was ist ein nicht reproduzierbarer Fehler?
3. Warum ist Letzterer schwerer zu beheben?
4. Welche Ursachen können dahinterstecken?
5. Was kann bei der Aufklärung helfen?

## Kurzantworten zur Selbstkontrolle

1. Ein stabil erneut auslösbarer Fehler
2. Ein beobachteter Fehler, den wir mit den derzeit bekannten Schritten nicht zuverlässig wiederholen können
3. Weil er schwerer zuverlässig zu beobachten ist
4. Timing, Zustand, Netzwerk, Parallelität
5. Logs, genaue Schritte, Dokumentation der Umgebung

## Quellen

Geprüft: `2026-10-14`.

- [Selenium: Avoid sharing state](https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/): isolierte Testdaten und Ausführung.


1. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Verwendung: offizieller begrifflicher Hintergrund zur Präzisierung von Fehler, Failure, Incident und verwandter Testterminologie.

2. Selenium - Avoid sharing state  
   https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/  
   Verwendung: offizielle, moderne Quelle dazu, wie Shared State intermittierendes oder flaky Testverhalten verursachen
   kann.

Abgerufen: `2026-04-09`
