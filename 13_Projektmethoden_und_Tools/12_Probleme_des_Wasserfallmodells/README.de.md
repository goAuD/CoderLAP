# Probleme des Wasserfallmodells

## Schneller visueller Überblick

| Typisches Problem | Warum ist es ein Problem? |
|---|---|
| wenig Flexibilität | sich ändernde Anforderungen sind schwer zu handhaben |
| spätes Testen | Fehler werden spät sichtbar |
| wenig frühes Feedback | die Entwicklung kann in die falsche Richtung gehen |
| hoher Dokumentationsaufwand | kann die Arbeit verlangsamen |

## Warum kann das Wasserfallmodell problematisch sein?

Das Modell ist linear:

- zuerst Anforderungen
- dann Entwurf
- dann Entwicklung
- danach Test

Das kann in einer stabilen Umgebung funktionieren,
aber wenn sich die Anforderungen während des Projekts ändern,
kann das Modell schwerfällig werden.

## Typische Probleme

### 1. Änderungen sind teuer

Wenn sich erst spät herausstellt,
dass etwas anders gemacht werden müsste,
muss auf mehrere frühere Phasen zurückgegriffen werden.

### 2. Der Benutzer sieht spät ein Ergebnis

Lange gibt es nur Dokumente und Pläne, wenig funktionierendes Ergebnis.

### 3. Fehler werden spät sichtbar

Wenn das Testen gegen Ende des Prozesses stattfindet, kann die Fehlerbehebung teurer sein.

### 4. Umgang mit Unsicherheit ist schwach

Für neue oder sich schnell ändernde Projekte ist es oft zu starr.

## Wann kann es dennoch gut sein?

- wenn die Anforderungen stabil sind
- wenn die Umgebung stark reguliert ist
- wenn die Dokumentation besonders wichtig ist

Es ist also kein schlechtes Modell, nur nicht in jeder Situation ideal.

## Späte Erkenntnis und früherer Nachweis

Ein Kunde hat die Anforderung „Monatsbericht“ auf Papier freigegeben. Drei Monate später zeigt die Vorführung: Sein Monat ist kein Kalendermonat, sondern eine Abrechnungsperiode. Fertige Datenabfrage, Oberfläche und Tests müssen möglicherweise gemeinsam geändert werden. Ursache ist ein zuvor ungeklärter Geschäftsbegriff.

Zwei konkrete Musterberichte, ein früher Prototyp und gemeinsam geprüfte Periodengrenzen können das bereits in der Anforderungsphase abfangen. Auch ein wasserfallorientiertes Vorgehen kann frühes Feedback nutzen. Entscheidend ist, dass echtes Verständnis einen Phasenabschluss stützt.

In regulierten Umgebungen können Nachweise und Rückverfolgbarkeit vorgeschrieben sein. Daraus folgt allein keine Pflicht zum ausschließlichen Wasserfallmodell. Der gewählte Prozess muss sowohl Anforderungsänderungen als auch überprüfbare Konformität ermöglichen.

## Prüfungstaugliche Formulierung

> Eines der Hauptprobleme des Wasserfallmodells ist sein starrer, linearer Aufbau.  
> Sich ändernde Anforderungen werden nur schwer gehandhabt,
> und Fehler oder Missverständnisse werden oft erst spät erkannt,
> wenn die Korrektur bereits teurer ist.  
> Deshalb ist es bei unsicheren oder sich schnell ändernden Projekten oft weniger vorteilhaft als iterative oder agile Ansätze.

## Schnelle Selbstkontrolle

1. Was ist die größte Schwäche des Wasserfallmodells?
2. Warum ist spätes Testen ein Problem?
3. Warum ist Änderungsmanagement darin schwierig?
4. Bei welchem Projekttyp kann es dennoch gut sein?
5. Warum sieht der Benutzer das Ergebnis erst spät?

## Kurzantworten zur Selbstkontrolle

1. Die Starrheit und das schwierige Änderungsmanagement
2. Weil Fehler erst spät erkannt werden
3. Weil die Phasen aufeinander aufbauen
4. Bei stabilen, gut definierten Projekten
5. Weil das funktionierende Ergebnis erst später erscheint

## Quellen

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Frühe Prüfung und unterschiedliche Entwicklungslebenszyklen.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Atlassian - Waterfall methodology  
   https://www.atlassian.com/agile/project-management/waterfall-methodology  
   Verwendung: moderne, praxisnahe Quelle zu Vorteilen und Grenzen des Wasserfallmodells.

2. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Verwendung: Überblick über die praktischen Unterschiede zwischen linearen und iterativen Entwicklungsmodellen.

Abgerufen: `2026-04-08`
