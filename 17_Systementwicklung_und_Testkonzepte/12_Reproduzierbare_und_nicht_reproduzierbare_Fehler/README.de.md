# Reproduzierbare und nicht reproduzierbare Fehler

## Schneller visueller Überblick

| Fehlertyp | Merkmal |
|---|---|
| reproduzierbar | mit denselben Schritten erneut auslösbar |
| nicht reproduzierbar / intermittierend | zeitweilig, unsicher, "flaky" |

## Was ist ein reproduzierbarer Fehler?

Wenn unter denselben Bedingungen:

- dieselbe Eingabe
- dieselbe Umgebung
- dieselbe Schrittfolge

erneut derselbe Fehler auftritt, dann ist der Fehler reproduzierbar.

## Was ist ein nicht reproduzierbarer Fehler?

In diesem Fall:

- tritt der Fehler nicht immer auf
- Umgebungsfaktoren können ihn beeinflussen
- Timing, Zustand, Netzwerk, Parallelität können ebenfalls eine Rolle spielen

In der Praxis wird dies häufig auch als:

- intermittierender Fehler
- oder bei Tests als `flaky` Problem bezeichnet

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
| instabiler Test | die Testumgebung oder der Testaufbau selbst ist unsicher |

## Prüfungstaugliche Formulierung

> Ein reproduzierbarer Fehler ist ein Fehler, der mit denselben Eingaben und Schritten zuverlässig erneut ausgelöst werden kann.  
> Ein nicht reproduzierbarer oder intermittierender Fehler tritt hingegen nicht jedes Mal auf, weshalb er schwieriger zu analysieren und zu beheben ist.  
> Bei solchen Fehlern ist eine detaillierte Fehlerdokumentation, die Logs und die Dokumentation der Umgebungsbedingungen besonders wichtig.

## Häufige Prüfungsfehler

- Denken, dass ein nicht reproduzierbarer Fehler "kein echter Fehler" ist.
- Umgebungsfaktoren nicht erwähnen.
- Einen flaky Test automatisch als Anwendungsfehler betrachten.
- Die Rolle der detaillierten Dokumentation auslassen.

## Schnelle Selbstkontrolle

1. Was ist ein reproduzierbarer Fehler?
2. Was ist ein nicht reproduzierbarer Fehler?
3. Warum ist Letzterer schwerer zu beheben?
4. Welche Ursachen können dahinterstecken?
5. Was kann bei der Aufklärung helfen?

## Kurzantworten zur Selbstkontrolle

1. Ein stabil erneut auslösbarer Fehler
2. Ein Fehler, der nicht vorhersehbar auftritt
3. Weil er schwerer zuverlässig zu beobachten ist
4. Timing, Zustand, Netzwerk, Parallelität
5. Logs, genaue Schritte, Dokumentation der Umgebung

## Quellen

1. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Verwendung: offizieller begrifflicher Hintergrund zur Präzisierung von Fehler, Failure, Incident und verwandter Testterminologie.

2. Selenium - Avoid sharing state  
   https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/  
   Verwendung: offizielle, moderne Quelle dazu, wie Shared State intermittierendes oder flaky Testverhalten verursachen kann.

Abgerufen: `2026-04-09`
