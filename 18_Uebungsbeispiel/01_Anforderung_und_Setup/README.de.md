# Anforderung und Setup

## Schneller visueller Überblick

| Benötigt | Nicht benötigt |
|---|---|
| HTML | Datenbank |
| responsives CSS, hier `Bootstrap` | Benutzerverwaltung |
| JavaScript | Admin-Oberfläche |
| QR-Library | Extra-Features |

## Was verlangt die Aufgabe?

Auf Basis der PDF:

- Stammdaten-Formular
- Responsive Design
- `SV-Nr` Validierung
- `QR`-Code Generierung
- `QR` Überprüfung mit einem Tool

## Minimales Setup

- `Browser`
- `Code Editor`
- Einfacher Projektordner
- `Bootstrap`
- Eine lokale `QR`-Code Library

## Empfohlene Ordnerstruktur

```text
Musterloesung_Minimal/
  index.html
  styles.css
  app.js
  vendor/
    qrcode.js
```

## Warum ist das eine gute Prüfungsstrategie?

- Schnell überschaubar
- Leicht debugbar
- Besteht aus wenigen beweglichen Teilen
- Auch unter Zeitdruck realistisch

## Von der Aufgabenliste zum ersten lauffähigen Stand

Wir erstellen zunächst das HTML-Grundgerüst und die leere JavaScript-Datei und öffnen die Seite.
Die Entwicklerwerkzeuge zeigen, ob alle Dateien geladen wurden.
Danach entstehen getrennt Formular, Prüffunktion und QR-Ausgabe.
Bei einem Problem können wir dadurch gezielt die betroffene Schicht untersuchen.

Die Seite lässt sich direkt als Datei öffnen. Benötigt die Umgebung einen lokalen
Webserver, ist aus dem Repository-Hauptverzeichnis beispielsweise möglich:

```powershell
py -m http.server 8780 --bind 127.0.0.1 --directory 18_Uebungsbeispiel/06_Musterloesung_Minimal
```

Die Adresse lautet `http://127.0.0.1:8780`. `Strg+C` beendet den Server.
Das ist statische Dateiauslieferung, kein Backend zur Datenverarbeitung.

Die QR-Bibliothek liegt lokal vor, das Bootstrap-CSS wird derzeit von einem CDN geladen.
Für eine vollständig netzfreie Prüfungsumgebung muss daher auch das benötigte CSS
vorab lokal bereitliegen und ohne Netzwerk getestet werden.
Ein Framework ist laut PDF nach Möglichkeit zu verwenden; die responsive Funktion ist erforderlich.

Quellen: Katalog, Seite 11; [Python: http.server](https://docs.python.org/3/library/http.server.html),
[Bootstrap: Download](https://getbootstrap.com/docs/5.3/getting-started/download/).

## Prüfungstaugliche Formulierung

> Bei dieser praktischen Aufgabe ist das minimale Ziel, ein funktionierendes, responsives HTML-Formular zu erstellen,  
> das die Gültigkeit der österreichischen `SV-Nr` prüft und basierend auf dem Ergebnis einen `QR`-Code generiert.  
> Die einfachste Lösung ist ein frontend-basierter Ansatz mit `HTML`, `Bootstrap` und `JavaScript`, mit einer lokalen  
> QR-Library.  
> Da die PDF keine Datenspeicherung verlangt, sind Datenbank und Backend kein Pflichtbestandteil der minimalen Lösung.

## Schnelle Selbstkontrolle

1. Welche drei Felder sind nötig?
2. Wie bereiten wir uns auf eine netzfreie Umgebung vor?
3. Warum erstellen wir die Prüffunktion getrennt?

## Kurzantworten zur Selbstkontrolle

1. Vorname, Nachname und SV-NR.
2. Abhängigkeiten einschließlich CSS lokal vorbereiten und ohne Netzwerk testen.
3. Die Logik lässt sich mit eigenen Eingaben schon vor Fertigstellung der Oberfläche prüfen.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Verwendung: Primärer Aufgabentext.

2. Python - http.server
   https://docs.python.org/3/library/http.server.html

3. Bootstrap - Download
   https://getbootstrap.com/docs/5.3/getting-started/download/

Verwendung: lokale statische Vorschau und Bereitstellung des CSS.

Abgerufen: `2026-10-14`
