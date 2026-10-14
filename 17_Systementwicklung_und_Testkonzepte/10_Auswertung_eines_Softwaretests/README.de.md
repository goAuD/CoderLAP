# Auswertung eines Softwaretests

## Schneller visueller Überblick

| Schritt | Frage |
|---|---|
| Testdurchführung | was ist tatsächlich passiert? |
| Vergleich | haben wir das erwartet? |
| Bewertung | bestanden oder nicht? |
| Bericht | was muss festgehalten und weitergegeben werden? |

## Was bedeutet die Auswertung eines Tests?

Bei der Auswertung:

- betrachten wir das Testergebnis
- vergleichen es mit der Spezifikation oder dem Testfall
- dokumentieren Abweichungen
- entscheiden über den nächsten Schritt

## Welche Ergebnisse sind möglich?

### Erfolgreicher Test

- das tatsächliche Ergebnis entspricht dem erwarteten

### Fehlgeschlagener Test

- es gibt eine Abweichung zwischen dem erwarteten und dem tatsächlichen Ergebnis

### Nicht eindeutiges Ergebnis

- es kann ein Umgebungsproblem sein
- es können falsche Testdaten sein
- es kann ein nicht reproduzierbarer Fehler sein

## Was muss dokumentiert werden?

Typischerweise:

- Testfall-Kennung
- Eingaben
- erwartetes Ergebnis
- tatsächliches Ergebnis
- Status
- Fehlerbeschreibung

## Warum ist eine gute Auswertung wichtig?

- unterstützt die Fehlerbehebung
- macht die Qualität nachverfolgbar
- hilft bei der Entscheidung, ob die Software freigegeben werden kann
- macht das Testen objektiver

## Testauswertung und Fehlerbehebung: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Auswertung | Vergleich des Ergebnisses mit der Erwartung |
| Fehlerbehebung | Beseitigung der Fehlerursache |

## Vom Ergebnis zur nachvollziehbaren Entscheidung

Testfall `FOG-03` sendet zwei identische Buchungsanfragen. Erwartet wird genau eine
gespeicherte Buchung. Der Bericht enthält Anwendungsversion, Testdatenkennung,
Ausführungsumgebung und tatsächliche Datensatzanzahl. Die genaue Schrittfolge
erlaubt anderen, die Prüfung zu wiederholen.

| Status | Beispiel | Nächster Schritt |
|---|---|---|
| Passed | eine Buchung bleibt | Nachweis aufbewahren |
| Failed | zwei Buchungen entstehen | Abweichung untersuchen, nach Korrektur nachtesten |
| Blocked | Testdatenbank unerreichbar | Umgebung wiederherstellen |
| Not run | Fall noch nicht ausgeführt | Ausführung planen |

Ein blockierter Fall ist kein bestandener Test. Sind von 100 geplanten Fällen
90 erfolgreich, 5 fehlgeschlagen und 5 blockiert, genügt „90% erfolgreich“ allein
nicht für eine Freigabe. Auch die Auswirkungen zählen: Ein Datenverlust kann
schwerer wiegen als viele kosmetische Abweichungen. **Schweregrad** beschreibt
die Auswirkung, **Priorität** die Dringlichkeit der Behebung. Nach einer Korrektur
prüfen wir den konkreten Fehler erneut und anschließend verwandtes Verhalten mit Regressionstests.

## Prüfungstaugliche Formulierung

> Bei der Auswertung eines Softwaretests wird das tatsächliche Ergebnis mit dem erwarteten Ergebnis verglichen.  
> Wenn beide übereinstimmen, ist der Test erfolgreich; bei einer Abweichung ist der Test fehlgeschlagen, und der  
> Fehler oder die Anomalie muss dokumentiert werden.  
> Eine ordnungsgemäße Auswertung unterstützt die Fehlerverfolgung, die Qualitätsmessung und weitere Entwicklungsentscheidungen.

## Schnelle Selbstkontrolle

1. Was ist die Grundlage der Testauswertung?
2. Wann ist ein Test erfolgreich?
3. Was muss bei einem fehlgeschlagenen Test dokumentiert werden?
4. Warum ist der objektive Vergleich wichtig?
5. Was ist der Unterschied zwischen Auswertung und Fehlerbehebung?

## Kurzantworten zur Selbstkontrolle

1. Der Vergleich von erwartetem und tatsächlichem Ergebnis
2. Wenn sie übereinstimmen
3. Abweichung, Umstände, Status, Fehlerbeschreibung
4. Weil die Qualitätsbewertung so zuverlässiger ist
5. Die eine bewertet, die andere behebt

## Quellen

Geprüft: `2026-10-14`.

- [ISTQB CTFL 4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf): Ergebnisverfolgung, Fehlermanagement, Nachtest und Regression.


1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: offizielle Quelle zur Auswertung von Testergebnissen, Fehlerdokumentation und Grundlagen des Testprozesses.

2. GitHub Docs - About continuous integration with GitHub Actions  
   https://docs.github.com/en/actions/about-github-actions/about-continuous-integration-with-github-actions  
   Verwendung: modernes, offizielles Beispiel dafür, wie Testergebnisse in der Praxis angezeigt und bewertet werden können.

Abgerufen: `2026-04-09`
