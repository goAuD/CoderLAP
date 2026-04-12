# Ausgabe eines QR-Codes

## Schneller visueller Überblick

| Ergebnis | QR-Code Inhalt |
|---|---|
| gültige SV-Nr | `Richtig` |
| ungültige SV-Nr | `Falsch` |

## Was ist hier eine gute Lösung?

Bei einer einfachen Prüfungslösung:

- Nach dem Klick auf den Button wird die Gültigkeit bestimmt
- Aus dem Ergebnis wird ein QR-Code generiert
- Der QR-Code wird direkt im Browser angezeigt

## Worauf muss man achten?

- Keinen kompletten Datenblock hineinkodieren
- Keinen Extra-Export oder Download einbauen, wenn nicht verlangt
- Die QR-Generierung soll erst nach der Überprüfung erfolgen

## Prüfungstaugliche Formulierung

> Laut Aufgabenstellung darf der Inhalt des generierten QR-Codes ausschließlich `Richtig` oder `Falsch` sein.  
> Das bedeutet, dass das Programm zuerst die Gültigkeit der `SV-Nr` feststellen muss und dann entsprechend den QR-Code erstellen soll.  
> Die einfachste Lösung ist eine im Browser laufende JavaScript-basierte QR-Generierung.

## Häufige Prüfungsfehler

- Den vollständigen Namen und die SV-Nummer in den QR-Code schreiben.
- Die QR-Generierung ohne eigene Logik durchführen.
- Sich auf einen externen Online-QR-Generator statt auf eine lokale Library verlassen.
- Nicht überprüfen, ob der QR-Code tatsächlich das erwartete Wort enthält.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Verwendung: Für die genaue Erwartung an den QR-Payload.

2. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator  
   Verwendung: Technische Grundlage für die einfache, lokale QR-Generierung im Browser.

Abgerufen: `2026-04-09`
