# BI- und BW-Systeme

## Schneller visueller Überblick

| Begriff | Hauptrolle |
|---|---|
| `BI` | aus Daten werden Informationen und geschäftliche Insights |
| `BW` / Data Warehouse | Sammlung, Bereinigung und historische Speicherung von Daten |

## Was ist `BI`?

`BI` ist eine Sammlung von Methoden und Werkzeugen, die helfen bei:

- Erstellung von Reports
- Datenanalyse
- Erkennung von Trends
- Entscheidungsunterstützung

## Was ist ein `BW`?

Ein `BW` oder Data Warehouse:

- sammelt Daten aus mehreren Quellen
- vereinheitlicht und bereitet sie auf
- speichert sie in einer für Analysen optimierten Form

Häufig enthält es:

- historische Daten
- aggregierte Daten
- aus geschäftlicher Sicht strukturierte Modelle

## Warum ist der Unterschied wichtig?

Weil:

- `BI` eher die Nutzungs- und Analyseseite ist
- `BW` eher die Datengrundlage und Infrastrukturseite ist

## Typischer Zusammenhang

```text
Operative Systeme
    -> Datenextraktion / Transformation
    -> BW / Data Warehouse
    -> BI-Reports, Dashboards, Analyse
```

## Wofür sind sie im Unternehmen nützlich?

- Management-Reporting
- Trendanalyse
- Leistungsmessung
- strategische Entscheidungsunterstützung

## `BI`, `BW`, `ERP` - nicht verwechseln

| Begriff | Fokus |
|---|---|
| `ERP` | operativer Unternehmensbetrieb |
| `BW` | zentrale, für Analysen vorbereitete Datenspeicherung |
| `BI` | Reporting und Analyse |

## Durchgearbeiteter Bericht und Datengranularität

**BI** umfasst Business Intelligence und Analysewerkzeuge. **BW** begegnet häufig als Name der Produktfamilie SAP Business Warehouse; die allgemeine Bezeichnung lautet Data Warehouse oder DWH. Nicht jede BI-Lösung benötigt ein separates Warehouse, vereinheitlichte historische Daten unterstützen jedoch viele Analysen.

Operative transaktionale Verarbeitung (**OLTP**) erfasst einzelne Bestellungen. Analytische Verarbeitung (**OLAP**) vergleicht Auswertungen vieler Bestellungen. Bei ETL folgen auf Extraktion erst Transformation und dann Laden; bei ELT erfolgt die Transformation nach dem Laden.

**MySQL 8.0 / InnoDB, leere Übungsdatenbank:** Eine Zeile steht hier für eine Verkaufsposition. Ihr Betrag ergibt sich aus Menge mal Stückpreis.

<!-- example:mysql -->
```sql
CREATE TABLE sales (
  id INT PRIMARY KEY,
  category VARCHAR(20) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(8,2) NOT NULL
) ENGINE=InnoDB;
INSERT INTO sales VALUES
  (1, 'book', 2, 10.00), (2, 'book', 1, 20.00), (3, 'tool', 3, 5.00);
SELECT category, SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY category
ORDER BY category;
```

```text
book 40.00
tool 15.00
```

Die Faktentabelle eines Warehouses enthält Messwerte; Dimensionen beschreiben beispielsweise Produkt, Datum und Kategorie. Zuerst wird die Bedeutung einer Zeile, die **Granularität**, festgelegt. Wird der gesamte Bestellbetrag bei jeder Position wiederholt, kann einfaches Summieren denselben Umsatz mehrfach zählen.

Zeitraum, Währung, Netto-/Bruttobedeutung und letzter Aktualisierungszeitpunkt müssen beim Bericht klar sein. Eine aggregierte Zahl erklärt die Ursache einer Abweichung nicht von selbst; dazu gehört eine überprüfbare fachliche Interpretation.

## Prüfungstaugliche Formulierung

> `BI`-Systeme dienen der Analyse, Visualisierung und Entscheidungsunterstützung auf Basis von Geschäftsdaten.  
> `BW`- oder Data-Warehouse-Systeme hingegen sammeln Daten aus verschiedenen Quellen, vereinheitlichen sie und  
> speichern sie in einer für Analysen geeigneten Form.  
> Einfach ausgedrückt: das `BW` stellt die Datengrundlage bereit, und `BI` macht daraus verwertbare Informationen und
> geschäftliche Insights.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel von `BI`?
2. Was ist das Hauptziel eines `BW`?
3. Was ist der Unterschied zwischen beiden?
4. Wie hängt es mit dem `ERP` zusammen?
5. Warum ist historische Datenspeicherung wichtig?

## Kurzantworten zur Selbstkontrolle

1. Analyse und Entscheidungsunterstützung
2. Zentrale Datenspeicherung für Analysen
3. `BI` nutzt die Daten, `BW` bereitet sie vor
4. `ERP` kann eine der Hauptdatenquellen sein
5. Weil so auch Trends untersucht werden können

## Quellen

1. IBM - What is business intelligence (BI)?  
   https://www.ibm.com/topics/business-intelligence  
   Verwendung: offizielle, moderne Quelle zum Begriff und Zweck von `BI`.

2. SAP - What is a data warehouse?  
   https://www.sap.com/sea/products/data-cloud/datasphere/what-is-a-data-warehouse.html  
   Verwendung: offizielle Quelle zur Rolle des Data Warehouse.

3. SAP - Business Warehouse in Business Data Cloud  
   https://www.sap.com/products/data-cloud/business-warehouse.html  
   Verwendung: zeitgemäße, offizielle Quelle zum `BW`-Begriff im unternehmerischen Kontext.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [Microsoft: Star schema](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema): Fakten, Dimensionen und Granularität
- [IBM: Business Intelligence](https://www.ibm.com/think/topics/business-intelligence): Analyse und geschäftliche Interpretation
- [SAP: Business Warehouse](https://www.sap.com/products/data-cloud/business-warehouse.html): BW als SAP-Produktbezeichnung

Geprüft: `2026-10-14`.
