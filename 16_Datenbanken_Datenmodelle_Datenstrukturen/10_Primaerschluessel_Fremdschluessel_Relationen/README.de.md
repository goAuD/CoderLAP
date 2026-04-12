# Primaerschluessel, Fremdschluessel, Relationen

## Schneller visueller Überblick

| Begriff | Rolle |
|---|---|
| Primärschlüssel | eindeutiger Datensatzidentifikator |
| Fremdschlüssel | Verweis auf eine andere Tabelle |
| Relation | Beziehung zwischen zwei Tabellen |

## Was ist ein Primärschlüssel?

Der Primärschlüssel:

- identifiziert eine Zeile eindeutig
- darf nicht `NULL` sein
- darf sich nicht wiederholen

Beispiel:

- `CustomerID`
- `OrderID`

## Was ist ein Fremdschlüssel?

Der Fremdschlüssel:

- verweist auf den Schlüssel einer anderen Tabelle
- stellt eine Beziehung her
- unterstützt die referentielle Integrität

Beispiel:

Wenn in der Tabelle `Orders` eine `CustomerID` vorhanden ist, die auf die Tabelle `Customers` verweist, dann ist das ein typischer Fremdschlüssel.

## Was ist eine Relation?

Unter Relation versteht man in diesem Thema typischerweise die Beziehung zwischen Tabellen.

Typische Beziehungen:

- Eins-zu-eins (`1:1`)
- Eins-zu-viele (`1:n`)
- Viele-zu-viele (`n:m`)

Die `n:m`-Beziehung wird in der Regel mit einer Verknüpfungstabelle umgesetzt.

## Warum sind sie wichtig?

- bieten eine geordnete Datenstruktur
- verknüpfen die Tabellen
- unterstützen Abfragen und Integrität

## Primärschlüssel und Fremdschlüssel - nicht verwechseln

| Kriterium | Primärschlüssel | Fremdschlüssel |
|---|---|---|
| Rolle | Identifikation des Datensatzes in der eigenen Tabelle | Verweis auf den Datensatz einer anderen Tabelle |
| Eindeutigkeit | obligatorisch | nicht unbedingt eindeutig |
| `NULL` | nicht erlaubt | je nach Regel erlaubt oder nicht |

## Prüfungstaugliche Formulierung

> Der Primärschlüssel dient der eindeutigen Identifikation eines Datensatzes innerhalb einer Tabelle.  
> Der Fremdschlüssel hingegen verweist auf den Schlüssel einer anderen Tabelle und stellt so eine Beziehung zwischen den Tabellen her.  
> Durch Relationen können getrennt gespeicherte Daten verknüpft werden, was die Grundlage des relationalen Datenbankmodells darstellt.

## Häufige Prüfungsfehler

- Den Primärschlüssel als Fremdschlüssel bezeichnen.
- Den Begriff Relation einfach als "Tabelle" übersetzen.
- Die Eindeutigkeit nicht erwähnen.
- Bei der `n:m`-Beziehung die Verknüpfungstabelle vergessen.

## Schnelle Selbstkontrolle

1. Was ist ein Primärschlüssel?
2. Was ist ein Fremdschlüssel?
3. Wozu dient eine Relation?
4. Was ist eine `1:n`-Beziehung?
5. Wie wird eine `n:m`-Beziehung umgesetzt?

## Kurzantworten zur Selbstkontrolle

1. Eindeutiger Datensatzidentifikator
2. Feld, das auf den Schlüssel einer anderen Tabelle verweist
3. Zur Verknüpfung von Tabellen
4. Einem Datensatz können mehrere zugehörige Datensätze zugeordnet sein
5. Mit einer Verknüpfungstabelle

## Quellen

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Verwendung: offizielle, anschauliche Quelle zu Schlüsseln und Beziehungen.

2. Microsoft Support - Guide to table relationships  
   https://support.microsoft.com/en-us/office/guide-to-table-relationships-30446197-4fbe-457b-b992-2f6fb812b58f  
   Verwendung: offizielle Quelle zur praktischen Interpretation von Relationen und Primär-/Fremdschlüsseln.

Abgerufen: `2026-04-09`
