# Anforderung und Setup

## Schneller visueller Überblick

| Benötigt | Nicht benötigt |
|---|---|
| HTML | Datenbank |
| `Bootstrap` | Benutzerverwaltung |
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

## Prüfungstaugliche Formulierung

> Bei dieser praktischen Aufgabe ist das minimale Ziel, ein funktionierendes, responsives HTML-Formular zu erstellen, das die Gültigkeit der österreichischen `SV-Nr` prüft und basierend auf dem Ergebnis einen `QR`-Code generiert.  
> Die einfachste Lösung ist ein frontend-basierter Ansatz mit `HTML`, `Bootstrap` und `JavaScript`, mit einer lokalen QR-Library.  
> Da die PDF keine Datenspeicherung verlangt, sind Datenbank und Backend kein Pflichtbestandteil der minimalen Lösung.

## Häufige Prüfungsfehler

- Ein zu großes Projekt aufbauen zu wollen.
- Unnötiges Backend oder eine Datenbank einzuführen.
- Die Zeit für Design-Extras zu verschwenden.
- Nicht auf die in der PDF angegebenen Mindestanforderungen zu optimieren.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Verwendung: Primärer Aufgabentext.

Abgerufen: `2026-04-09`
