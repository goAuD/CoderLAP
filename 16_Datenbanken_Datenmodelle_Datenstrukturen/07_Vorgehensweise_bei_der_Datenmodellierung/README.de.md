# Vorgehensweise bei der Datenmodellierung

## Schneller visueller Überblick

```text
Anforderungen verstehen
    -> Entitäten und Attribute identifizieren
    -> Beziehungen bestimmen
    -> Schlüssel festlegen
    -> Normalisierung
    -> logisches / physisches Modell
```

## Was ist das Ziel der Datenmodellierung?

Es soll:

- klar sein, welche Daten gespeichert werden müssen
- wie diese miteinander zusammenhängen
- welche Regeln für sie gelten

## Typische Schritte

### 1. Anforderungen sammeln

Es muss verstanden werden:

- welche Daten gespeichert werden müssen
- welche Fragen beantwortet werden sollen
- welche Operationen unterstützt werden müssen

### 2. Entitäten identifizieren

Zum Beispiel:

- Kunde
- Bestellung
- Produkt
- Mitarbeiter

### 3. Attribute bestimmen

Zum Beispiel bei einem Kunden:

- Name
- Adresse
- E-Mail
- Kennung

### 4. Beziehungen angeben

Zum Beispiel:

- ein Kunde kann mehrere Bestellungen haben
- eine Bestellung kann mehrere Produkte enthalten

### 5. Schlüssel und Regeln festlegen

Hier wird entschieden:

- was der Primärschlüssel sein soll
- wo ein Fremdschlüssel nötig ist
- welche Integritätsregeln erforderlich sind

### 6. Normalisierung

Ziel:

- weniger Redundanz
- bessere Datenkonsistenz

### 7. Logische und physische Umsetzung

Hier wird aus dem theoretischen Modell ein konkretes Datenbankschema.

## Konzeptionelles, logisches, physisches Modell

| Ebene | Bedeutung |
|---|---|
| konzeptionelles Modell | Beschreibung auf Geschäftsebene |
| logisches Modell | Tabellen, Schlüssel, Beziehungen |
| physisches Modell | konkrete, an ein `DBMS` angepasste Umsetzung |

## Prüfungstaugliche Formulierung

> Bei der Datenmodellierung werden die Daten realer oder geschäftlicher Prozesse in ein strukturiertes Modell  
> überführt.  
> Typische Schritte sind die Erhebung der Anforderungen, die Bestimmung von Entitäten und Attributen, die Festlegung  
> von Beziehungen und Schlüsseln sowie die Normalisierung und die Erstellung des konkreten Datenbankschemas.  
> Ziel ist die Schaffung einer übersichtlichen, erweiterbaren und konsistenten Datenstruktur.

## Häufige Prüfungsfehler

- Sofort mit Tabellen beginnen, ohne die Geschäftsbegriffe zu verstehen.
- Die Modellierung nur als Zeichnen betrachten.
- Schlüssel und Beziehungen nicht erwähnen.
- Konzeptionelles und physisches Modell verwechseln.

## Schnelle Selbstkontrolle

1. Was ist das Ziel der Datenmodellierung?
2. Welche typischen Hauptschritte gibt es?
3. Was ist eine Entität?
4. Was ist der Unterschied zwischen logischem und physischem Modell?
5. Warum ist die Normalisierung bei der Modellierung wichtig?

## Kurzantworten zur Selbstkontrolle

1. Erstellung eines strukturierten Datenmodells
2. Anforderungserhebung, Entitäten, Attribute, Beziehungen, Schlüssel, Normalisierung
3. Ein Objekt oder eine Sache, über die Daten gespeichert werden
4. Das eine ist allgemeiner, das andere auf ein konkretes `DBMS` zugeschnitten
5. Weil sie Redundanz reduziert und Konsistenz erhöht

## Quellen

1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Verwendung: offizielle, moderne Quelle zu den Ebenen logischer, relationaler und physischer Modellierung.

2. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Verwendung: praktische, offizielle Quelle zu den Grundschritten des relationalen Entwurfsprozesses.

Abgerufen: `2026-04-09`
