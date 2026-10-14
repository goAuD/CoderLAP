# Personenbezogene und sensible Daten

## Schneller visueller Überblick

| Datentyp | Beispiel | Schutzniveau |
|---|---|---|
| personenbezogene Daten | Name, E-Mail, IP-Adresse | geschützt |
| besondere Kategorien personenbezogener Daten | Gesundheitsdaten, Biometrie zur eindeutigen Identifizierung, Religion | besonders geschützt |
| strafrechtliche Daten | Daten zu Verurteilungen oder Straftaten | unterliegen gesonderten Regelungen |

## Was sind personenbezogene Daten?

Nach der GDPR sind personenbezogene Daten:

- alle Informationen
- die sich auf eine natürliche Person beziehen
- und diese direkt oder indirekt identifizierbar machen

Nicht nur der Name gilt als personenbezogenes Datum.

Personenbezogene Daten können zum Beispiel sein:

- E-Mail-Adresse
- Kundenkennung
- Kennzeichen
- IP-Adresse
- Standortdaten
- Foto

## Was zählt zu den besonderen Kategorien?

Art. 9 der GDPR behandelt die besonders geschützten Daten gesondert.

Dazu können zum Beispiel gehören:

- rassische oder ethnische Herkunft
- politische Meinungen
- religiöse oder weltanschauliche Überzeugungen
- Gewerkschaftszugehörigkeit
- genetische Daten
- biometrische Daten zur eindeutigen Identifizierung
- Gesundheitsdaten
- Daten zum Sexualleben oder zur sexuellen Orientierung

Wichtig:

- deren Verarbeitung ist grundsätzlich **verboten**
- zusätzlich zur Rechtsgrundlage nach Art. 6 ist eine passende Ausnahme nach Art. 9 Abs. 2 erforderlich

## Wie ist es mit strafrechtlichen Daten?

Daten über strafrechtliche Verurteilungen und Straftaten
sind nicht dasselbe wie besondere Kategorien personenbezogener Daten.

Dafür gilt **Art. 10** der GDPR.

Die beiden Kategorien haben unterschiedliche Rechtsgrundlagen:

- **Art. 9** = besondere Kategorien
- **Art. 10** = strafrechtliche Verurteilungen und Daten im Zusammenhang mit Straftaten

## Warum ist das wichtig?

Weil es einen Unterschied macht:

- welche Daten wir erheben
- auf welcher Rechtsgrundlage wir sie verarbeiten
- wie streng der Schutz sein muss
- ob eine gesonderte Information oder ausdrückliche Einwilligung erforderlich ist

Beispiel:

- Name + E-Mail bei einem Webshop: personenbezogene Daten
- ärztlicher Befund oder Krankengeschichte: besondere Kategorie personenbezogener Daten

## Nicht verwechseln

| Begriff | Was bedeutet er? |
|---|---|
| personenbezogene Daten | jede einer Person zuordenbare Information |
| besondere Kategorien personenbezogener Daten | besonders geschützte personenbezogene Daten |
| anonyme Daten | nicht mehr einer Person zuordenbar |
| pseudonymisierte Daten | können noch rückverknüpft werden, daher können weiterhin Datenschutzregeln gelten |

## Einordnungsaufgabe: Kennung statt Name

In einer Übungsdatenbank steht `user-42` statt `Anna`; eine separate Tabelle enthält
weiterhin die Zuordnung. Das ist **Pseudonymisierung**, keine vollständige Anonymisierung:
Der Verantwortliche mit Zugriff auf die Zuordnung kann die Person wieder identifizieren.
Wir schützen die Zuordnung mit getrennten Zugriffsrechten und behandeln auch den
pseudonymisierten Datensatz weiterhin als personenbezogen.

Bei anonymen Daten ist eine Identifizierung mit vernünftigerweise wahrscheinlich
eingesetzten Mitteln nicht möglich. Nur den Namen zu entfernen genügt dafür oft nicht:
Ein seltener Beruf, ein genaues Geburtsdatum und ein kleiner Wohnort können zusammen
auf eine Person hinweisen. Die Beurteilung berücksichtigt auch verfügbare Zusatzinformationen.

Ein gewöhnliches Profilfoto kann personenbezogen sein, ist aber nicht automatisch
ein besonderes biometrisches Datum nach Art. 9. Eine zur eindeutigen Gesichtserkennung
erstellte und verwendete Vorlage ist anders zu beurteilen. Ein Passwort ist sicherheitskritisch,
gehört für sich genommen aber nicht zu den in Art. 9 aufgezählten besonderen Kategorien.

**Schlussfolgerung:** Der technische Schutzbedarf hängt nicht allein vom Namen der
rechtlichen Kategorie ab. Auch gewöhnliche Kontaktdaten können großen Schaden verursachen,
wenn sie zu einer gefährdeten Person gehören.

Quelle: [DSB: besondere Datenkategorien](https://dsb.gv.at/faqs/besondere-datenkategorien),
Art. 4, 6, 9, 10 und Erwägungsgründe 26, 51 DSGVO. Geprüft: 2026-10-14.

## Prüfungstaugliche Formulierung

> Personenbezogene Daten sind alle Informationen,
> die sich auf eine identifizierte oder identifizierbare natürliche Person beziehen.
> Besondere Kategorien personenbezogener Daten,
> wie Gesundheitsdaten oder biometrische Daten zur eindeutigen Identifizierung,
> stehen unter besonderem Schutz
> und ihre Verarbeitung ist grundsätzlich verboten,
> nur unter bestimmten Ausnahmen zulässig.
> Daten über strafrechtliche Verurteilungen und Straftaten unterliegen einer gesonderten Regelung nach Art. 10 der GDPR.

## Schnelle Selbstkontrolle

1. Was sind personenbezogene Daten?
2. Nenne drei Beispiele für personenbezogene Daten.
3. Was gehört zu den besonderen Kategorien?
4. Welcher GDPR-Artikel behandelt die besonderen Kategorien?
5. Sind strafrechtliche Daten dasselbe wie besondere Kategorien?

## Kurzantworten zur Selbstkontrolle

1. Einer Person zuordenbare Information
2. Name, E-Mail-Adresse, IP-Adresse
3. Zum Beispiel Gesundheitsdaten, biometrische Daten zur eindeutigen Identifizierung, religiöse Überzeugung
4. Art. 9
5. Nein, strafrechtliche Daten werden gesondert in Art. 10 geregelt

## Quellen

1. EUR-Lex - Regulation (EU) 2016/679
   https://eur-lex.europa.eu/eli/reg/2016/679/oj
   Verwendung: primäre Rechtsquelle für personenbezogene Daten, besondere Kategorien und strafrechtliche Daten.

2. Datenschutzbehörde - Besondere Datenkategorien
   https://dsb.gv.at/faqs/besondere-datenkategorien
   Verwendung: österreichische behördliche Zusammenfassung der ehemals als „sensible Daten" bezeichneten Datenkategorien.

3. Datenschutzbehörde - Ihre Rechte als betroffene Person
   https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person
   Verwendung: behördliche Definitionen zu personenbezogenen Daten und dem Begriff der betroffenen Person.

4. oesterreich.gv.at - Datenschutz
   https://www.oesterreich.gv.at/de/lexicon/D/Seite.991455
   Verwendung: österreichische Regierungsübersicht mit praktischen Beispielen zu personenbezogenen Daten.

Abgerufen: `2026-04-08`
