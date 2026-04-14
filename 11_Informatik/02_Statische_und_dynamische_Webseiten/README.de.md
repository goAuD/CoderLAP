# Statische und dynamische Webseiten

## Schneller visueller Überblick

| Typ | Merkmal | Beispiel |
|---|---|---|
| statisch | vorab erstellte Datei | einfache Präsentationsseite |
| dynamisch | zur Laufzeit generierter oder veränderter Inhalt | Webshop, eingeloggte Benutzeroberfläche |

## Was ist eine statische Webseite?

Bei einer statischen Seite liefert der Server in der Regel:

- fertige HTML-, CSS-, JS-Dateien aus

Der Inhalt:

- ändert sich nicht unbedingt pro Benutzer
- ist oft schnell und einfach

Beispiele:

- Firmenpräsentationsseite
- Portfolio
- Dokumentationsseite

## Was ist eine dynamische Webseite?

Bei einer dynamischen Seite kann der Inhalt:

- aus einer Datenbank stammen
- je nach Benutzer variieren
- während der Anfrage erstellt werden

Beispiele:

- Webshop-Produktliste
- eingeloggtes Admin-Panel
- Forum
- Buchungssystem

## Wie kann etwas dynamisch sein?

Zwei häufige Wege:

### 1. Serverseitig

Der Server:

- ruft Daten ab
- führt Logik aus
- sendet personalisiertes HTML oder Daten

### 2. Clientseitig

Der Browser:

- modifiziert die Oberfläche mit JavaScript
- fordert Daten von einer API an
- zeigt neue Inhalte ohne Seitenneuladung an

## Warum ist der Unterschied wichtig?

Weil sich Folgendes unterscheidet:

- die Entwicklungslogik
- die Leistung
- das Caching
- die Sicherheitsüberlegungen
- die Wartung

## Wichtige Klarstellung

Viele heutige Webseiten sind gemischt.

Zum Beispiel:

- die Grundseite kann statisch wirken
- aber ein Teil des Inhalts wird dynamisch geladen

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| statische Seite | vorab erstellter Inhalt |
| dynamische Seite | zur Laufzeit generierter oder veränderter Inhalt |
| interaktive Seite | nicht immer dasselbe wie dynamisch |

## Prüfungstaugliche Formulierung

> Eine statische Webseite besteht aus vorab erstellten Dateien,
> daher sendet der Server typischerweise jedem Besucher denselben Inhalt.  
> Eine dynamische Webseite hingegen kann zur Laufzeit
> basierend auf Daten und Logik Inhalte erstellen,
> zum Beispiel angepasst an den Benutzer oder die Datenbank.  
> Heutige Webanwendungen kombinieren häufig beide Ansätze.

## Häufige Prüfungsfehler

- Behaupten, dass auf einer statischen Seite kein JavaScript sein kann.
- Eine dynamische Seite ausschließlich mit einer Datenbank gleichsetzen.
- Serverseitige und clientseitige Dynamik nicht unterscheiden.
- Glauben, dass das moderne Web nur das eine oder das andere sein kann.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche einer statischen Seite?
2. Was ist das Wesentliche einer dynamischen Seite?
3. Nenne zwei Beispiele für statische Seiten.
4. Nenne zwei Beispiele für dynamische Seiten.
5. Kann eine Webseite teils statisch, teils dynamisch sein?

## Kurzantworten zur Selbstkontrolle

1. Liefert vorab erstellte Inhalte aus
2. Kann sich zur Laufzeit ändern oder generiert werden
3. Portfolio, Firmenpräsentationsseite
4. Webshop, Forum
5. Ja

## Quellen

1. MDN - Server-side website programming first steps  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps  
   Verwendung: offizielle Quelle zum Unterschied zwischen statischen und dynamischen Webseiten.

2. MDN - Introduction to the server side  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction  
   Verwendung: detailliertere offizielle Erklärung, wie dynamischer Inhalt entsteht.

3. MDN - HTML basics  
   https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics  
   Verwendung: als Ausgangspunkt für den Aufbau statischer Grundseiten und clientseitiger Webinhalte.

Abgerufen: `2026-04-08`
