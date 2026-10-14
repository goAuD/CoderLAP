# Erste drei Normalformen

## Ziel der Normalisierung

Normalisierung zerlegt Tabellen anhand der Abhängigkeiten zwischen Daten. Sie reduziert unnötige Wiederholung sowie Einfüge-, Änderungs- und Löschanomalien. Eine Abhängigkeit ist eine Geschäftsregel, keine Schlussfolgerung aus zufällig gleichen Beispielwerten.

`X -> Y` bedeutet: Zu demselben X-Wert gehört immer derselbe Y-Wert. Ein **Schlüsselkandidat** ist eine minimale Spaltenmenge, die eine Zeile eindeutig identifiziert. Daraus wird der Primärschlüssel gewählt. Bei der Normalisierung werden auch die anderen Schlüsselkandidaten berücksichtigt.

## 1NF: ein Wert aus der gewählten Domäne

Es gibt keine wiederholten Spaltengruppen wie `product1`, `product2`, `product3` und keine kommaseparierte Produktliste in einer Zelle. Eine Bestellposition bildet eine Zeile. „Atomar“ hängt von der Verwendung im Datenmodell ab: Ein Datum darf ein einzelner DATE-Wert bleiben, obwohl man Jahr und Monat daraus bestimmen kann.

## 2NF: vollständige Abhängigkeit von jedem Schlüsselkandidaten

Zusätzlich zur 1NF hängt jedes Attribut, das zu keinem Schlüsselkandidaten gehört, vollständig von jedem Schlüsselkandidaten ab, nicht nur von einem Teil davon. Bei zusammengesetzten Schlüsseln ist das gesondert zu prüfen. Bestehen alle Schlüsselkandidaten aus jeweils einer Spalte, gibt es keine solche partielle Abhängigkeit.

## 3NF: transitive Abhängigkeiten behandeln

In einfachen Fällen mit eindeutigem Schlüssel soll ein Nicht-Schlüsselattribut nicht über ein anderes Nicht-Schlüsselattribut vom Schlüssel abhängen. Beispielsweise gilt `customer_id -> customer_name`. Der Kundenname gehört daher zum Kunden und wird nicht in jeder Bestellung erneut gespeichert.

Präziser gilt für jede nicht triviale Abhängigkeit `X -> A`: X ist ein Superschlüssel oder A gehört zu einem Schlüsselkandidaten. Ein Superschlüssel identifiziert eindeutig, darf aber im Gegensatz zum minimalen Schlüsselkandidaten überflüssige Spalten enthalten. Diese Formulierung deckt auch mehrere Schlüsselkandidaten ab.

## Durchgearbeitete Zerlegung: Bestellpositionen

Ausgangspunkt: `order_id, product_id, order_date, customer_id, customer_name, product_name, quantity`. Nach der Beispielregel kommt ein Produkt je Bestellung einmal vor; Schlüsselkandidat ist `(order_id, product_id)`.

1. **1NF:** Jedes Produkt steht in einer eigenen Zeile. Die Menge ist eine einzelne Zahl.
2. **2NF:** Bestelldatum und Kunde hängen nur von `order_id` ab, der Produktname nur von `product_id`. Sie werden in `orders` und `products` ausgelagert. `order_items(order_id, product_id, quantity)` enthält die Menge, die zum gesamten Paar gehört.
3. **3NF:** In `orders` bestünde die Kette `order_id -> customer_id -> customer_name`. Der Name kommt nach `customers(customer_id, customer_name)`; in der Bestellung bleibt der Fremdschlüssel des Kunden.

Das Ergebnis sind vier Tabellen: `customers`, `orders`, `products`, `order_items`. Über Schlüssel und Joins lässt sich dieselbe Bestellung wieder zusammensetzen, während der aktuelle Kundenname nur an einer Stelle geändert wird. Preis oder Lieferadresse zum Bestellzeitpunkt können eigenständige historische Daten sein. Ihre Bedeutung wird zuerst geklärt, statt sie automatisch zu entfernen.

## Prüfungstaugliche Formulierung

> Die 1NF beseitigt Wiederholungsgruppen. Die 2NF prüft Abhängigkeiten von Teilen eines Schlüsselkandidaten. Die 3NF beseitigt zusätzlich ungeeignete transitive Abhängigkeiten. Ziel ist eine Aufteilung, in der Geschäftsfakten konsistent verwaltet und benötigte Daten durch Verknüpfung wiedergewonnen werden können.

## Schnelle Selbstkontrolle

1. Warum stehen zwei Produkte einer Bestellung in getrennten Zeilen?
2. Was ist eine partielle Abhängigkeit?
3. Warum kann der Kundenname in eine eigene Tabelle gehören?
4. Löst eine zusätzliche `id`-Spalte allein alle Normalisierungsprobleme?
5. Woher kennt man die funktionalen Abhängigkeiten?

## Kurzantworten zur Selbstkontrolle

1. So entsteht keine wiederholte Produktliste innerhalb eines Feldes.
2. Ein Nicht-Schlüsselattribut hängt nur von einem Teil eines zusammengesetzten Schlüsselkandidaten ab.
3. Er wird durch die Kundenkennung bestimmt und ist kein eigener Sachverhalt der Bestellung.
4. Nein. Fachliche Schlüssel und Abhängigkeiten bleiben bestehen.
5. Aus Anforderungen und geprüften Geschäftsregeln.

## Quellen

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Verwendung: offizielle, gut verständliche Erklärung der ersten drei Normalformen.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Verwendung: offizieller Hintergrund zum Zweck der Normalisierung und zur praktischen Interpretation von `1NF`, `2NF`,
   `3NF`.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [Microsoft: Database normalization](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/microsoft-365/microsoft-365-apps/access/database-normalization-description): Grundsätze der Normalisierung und Tabellenzerlegung
- [Microsoft: Database design basics](https://support.microsoft.com/en-us/access/database-design-basics): Entwurf von Abhängigkeiten, Schlüsseln und Beziehungen

Geprüft: `2026-10-14`.
