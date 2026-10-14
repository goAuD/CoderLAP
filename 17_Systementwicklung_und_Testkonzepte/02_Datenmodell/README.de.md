# Datenmodell

## Schneller visueller Überblick

| Modellelement | Bedeutung |
|---|---|
| Entität | ein gespeichertes Objekt, z.B. Kunde |
| Attribut | Eigenschaft der Entität |
| Beziehung | Verhältnis zwischen den Entitäten |
| Schlüssel | Identifikation und Verknüpfung |

## Was ist der Zweck eines Datenmodells?

Das Datenmodell hilft:

- die Struktur der Daten zu verstehen
- Chaos in der Datenverwaltung zu vermeiden
- die Datenbank gut planbar zu machen
- Geschäftsregeln eindeutig zu machen

## Was enthält ein Datenmodell?

Typischerweise:

- Entitäten
- Attribute
- Beziehungen
- Schlüssel
- Einschränkungen oder Geschäftsregeln

## Welche Ebenen gibt es?

| Ebene | Fokus |
|---|---|
| konzeptionelles Modell | Geschäftsperspektive |
| logisches Modell | tabellennahe Struktur |
| physisches Modell | konkrete `DBMS`-spezifische Umsetzung |

## Beispiel

Bei einem Webshop könnten folgende Entitäten existieren:

- `Customer`
- `Order`
- `Product`

Beziehung:

- ein Kunde kann mehrere Bestellungen haben
- eine Bestellung kann mehrere Produkte enthalten

## Datenmodell und Datenbank: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Datenmodell | prinzipielle Strukturbeschreibung |
| Datenbank | die tatsächlich realisierte Speicherung |

## Warum ist es in der Systementwicklung wichtig?

- gibt den Entwicklern eine gute Grundlage
- unterstützt die konsistente Datenverarbeitung
- unterstützt Testen und Weiterentwicklung

## Regeln aus einer Beziehung ableiten

Zwischen Kursen und Teilnehmern besteht eine Viele-zu-viele-Beziehung: Eine
Person kann mehrere Kurse besuchen, ein Kurs mehrere Teilnehmer haben. Im
relationalen Modell verwenden wir dafür eine Zwischentabelle:

| Tabelle | Wichtige Felder und Regeln |
|---|---|
| `participant` | Primärschlüssel `id`, Anzeigename |
| `course` | Primärschlüssel `id`, Titel |
| `enrollment` | Fremdschlüssel `participant_id`, `course_id`; gemeinsam eindeutig |

Ein eigenes Attribut der Anmeldung ist etwa der Zeitpunkt `registered_at`.
Dieser beschreibt die Beziehung, nicht dauerhaft die Person oder den Kurs.
Die Eindeutigkeit des Kennungspaars verhindert doppelt gespeicherte Anmeldungen.
Fremdschlüssel stellen den Bezug auf existierende Zeilen sicher.

Zur Kardinalität gehört auch Optionalität: Darf ein Kurs null Teilnehmer haben?
Was geschieht beim Löschen einer Person? Das sind fachliche Entscheidungen;
`CASCADE` ist nicht automatisch die richtige Wahl. Vor dem physischen SQL prüfen
wir das Modell mit konkreten Datensätzen und einem Löschszenario.

## Prüfungstaugliche Formulierung

> Das Datenmodell ist die Beschreibung der Struktur und Beziehungen von Daten.  
> Es legt fest, welche Entitäten, Attribute und Relationen verwaltet werden müssen, sowie welche Regeln und Schlüssel  
> für sie gelten.  
> Das Datenmodell ist eine der wichtigsten Planungsgrundlagen für eine gut aufgebaute Datenbank und ein Datenverwaltungssystem.

## Schnelle Selbstkontrolle

1. Was ist ein Datenmodell?
2. Welche Elemente hat es?
3. Was ist der Unterschied zwischen Datenmodell und Datenbank?
4. Warum ist die Beschreibung der Beziehungen wichtig?
5. Welche Ebenen der Modellierung gibt es?

## Kurzantworten zur Selbstkontrolle

1. Die strukturelle Beschreibung der Daten
2. Entitäten, Attribute, Beziehungen, Schlüssel
3. Das eine ist ein Plan, das andere die Umsetzung
4. Weil Daten nicht isoliert sind
5. Konzeptionell, logisch, physisch

## Quellen

Geprüft: `2026-10-14`.

- [Oracle: Data Modeler FAQ](https://www.oracle.com/tools/technologies/faq-sql-developer-data-modeler.html): konzeptionelle, relationale und physische Modelle.


1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Verwendung: offizielle Quelle zu den Ebenen und Zielen der Datenmodellierung.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Verwendung: offizieller Hintergrund zu den Grundlagen der relationalen Datenorganisation und Modellierung.

Abgerufen: `2026-04-09`
