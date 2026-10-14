# Primaerschluessel, Fremdschluessel, Relationen

## Schneller visueller Überblick

| Begriff | Rolle |
|---|---|
| Primärschlüssel | eindeutiger Datensatzidentifikator |
| Fremdschlüssel | Verweis auf einen Schlüssel derselben oder einer anderen Tabelle |
| Relation | im relationalen Modell eine Menge von Tupeln, tabellarisch dargestellt |

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

- verweist auf einen referenzierten Schlüssel, auch innerhalb derselben Tabelle möglich
- stellt eine Beziehung her
- unterstützt die referentielle Integrität

Beispiel:

Wenn in der Tabelle `Orders` eine `CustomerID` vorhanden ist, die auf die Tabelle `Customers` verweist, dann ist das ein
typischer Fremdschlüssel.

## Was ist eine Relation?

Im relationalen Modell ist eine Relation eine Menge von Tupeln, die als Tabelle dargestellt wird. Eine Verknüpfung zwischen Tabellen heißt genauer Beziehung oder Relationship. Die Begriffe hängen zusammen, sind aber nicht identisch.

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
| Rolle | Identifikation des Datensatzes in der eigenen Tabelle | Verknüpfung einer Zeile mit einem referenzierten Schlüssel |
| Eindeutigkeit | obligatorisch | nicht unbedingt eindeutig |
| `NULL` | nicht erlaubt | je nach Regel erlaubt oder nicht |

## Durchgearbeitete Beziehungen und Pflichtangaben

| Anforderung | Umsetzung |
|---|---|
| Ein Kunde kann mehrere Bestellungen haben | Fremdschlüssel `orders.customer_id`, nicht eindeutig |
| Eine Person darf höchstens ein Profil haben | Fremdschlüssel `profiles.person_id` plus UNIQUE |
| Lernende besuchen mehrere Kurse und umgekehrt | Verknüpfungstabelle `enrollments` mit zwei Fremdschlüsseln |
| Ein Mitarbeiter kann einen Vorgesetzten haben | nullable `employees.manager_id` verweist auf `employees.id` |

`NOT NULL` macht den Verweis verpflichtend. `UNIQUE` erlaubt höchstens eine zugehörige Zeile, garantiert aber allein noch nicht, dass für jede Person tatsächlich ein Profil angelegt wird. Ein Fremdschlüssel ist ein Constraint: Der Spaltenname `customer_id` erzeugt ihn nicht automatisch.

Für Löschungen ist eine eigene Entscheidung nötig. `RESTRICT` kann das Löschen eines referenzierten Elternsatzes verhindern, `CASCADE` überträgt es auf Kindzeilen und `SET NULL` setzt einen nullable Verweis voraus. Wähle nach der aufzubewahrenden Geschäftshistorie. Rechnungen eines Kunden sollten beispielsweise nicht allein aus Bequemlichkeit automatisch verschwinden.

## Prüfungstaugliche Formulierung

> Der Primärschlüssel identifiziert eine Zeile eindeutig und ohne NULL; er kann mehrere Spalten umfassen. Der Fremdschlüssel stellt über einen referenzierten Schlüssel eine referentielle Beziehung sicher. Eine n:m-Beziehung wird mit einer Verknüpfungstabelle abgebildet. Die Relation ist die Tupelmenge des relationalen Modells, nicht einfach ein anderes Wort für die Beziehung zwischen Tabellen.

## Schnelle Selbstkontrolle

1. Was ist ein Primärschlüssel?
2. Was ist ein Fremdschlüssel?
3. Wie unterscheiden sich Relation und Beziehung zwischen Tabellen?
4. Was ist eine `1:n`-Beziehung?
5. Wie wird eine `n:m`-Beziehung umgesetzt?

## Kurzantworten zur Selbstkontrolle

1. Eindeutiger Datensatzidentifikator
2. Spalte oder Spaltengruppe, die einen Schlüssel referenziert, auch in derselben Tabelle
3. Eine Relation ist eine Tupelmenge; eine Beziehung beschreibt den Zusammenhang gespeicherter Entitäten
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

### Geprüfte Quellen zur Ergänzung

- [PostgreSQL: Glossary, Relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION): Definition der Relation als Tupelmenge
- [MySQL: FOREIGN KEY constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html): Verweise und Löschregeln

Geprüft: `2026-10-14`.
