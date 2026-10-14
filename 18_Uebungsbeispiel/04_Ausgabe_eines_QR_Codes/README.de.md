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

## Entscheidung und QR-Bild sind getrennte Schritte

Dieser Browserausschnitt setzt das geladene lokale `vendor/qrcode.js` voraus.
`validation` enthält das Ergebnis der vollständigen SV-Prüfung, `qrCodeBox` ist das HTML-Ausgabeelement:

```javascript
const payload = validation.isValid ? "Richtig" : "Falsch";
const qr = qrcode(0, "M");
qr.addData(payload);
qr.make();
qrCodeBox.innerHTML = qr.createSvgTag(6);
```

`0` wählt die QR-Größe automatisch, `M` bezeichnet die Fehlerkorrekturstufe.
`make()` erstellt den Code. Die Ausgabe behält den standardmäßigen freien Rand von
vier Modulen bei; dieser trennt das Muster von seiner Umgebung.
Der Ausschnitt setzt die vorherige Pflichtfeldprüfung voraus.

Der QR-Payload enthält genau ein Wort. Namen und SV-Nummer werden nicht aufgenommen;
für die QR-Erzeugung ist keine externe Netzwerkanfrage nötig.
Fehlerkorrektur unterstützt die Lesbarkeit, bestätigt aber nicht die Wahrheit des Inhalts.
Beim Bearbeiten blenden wir das alte Ergebnis aus, damit neben der neuen Eingabe kein alter QR stehen bleibt.

Quelle: [qrcode-generator API](https://kazuhikoarase.github.io/qrcode-generator/js/).

## Prüfungstaugliche Formulierung

> Laut Aufgabenstellung darf der Inhalt des generierten QR-Codes ausschließlich `Richtig` oder `Falsch` sein.  
> Das bedeutet, dass das Programm zuerst die Gültigkeit der `SV-Nr` feststellen muss und dann entsprechend den QR-Code  
> erstellen soll.  
> Die einfachste Lösung ist eine im Browser laufende JavaScript-basierte QR-Generierung.

## Schnelle Selbstkontrolle

1. Warum muss das Ergebnis zuerst feststehen?
2. Wozu dient der freie QR-Rand?
3. Wo stehen die Namen im QR?

## Kurzantworten zur Selbstkontrolle

1. Die Entscheidung wählt den genauen Payload: Richtig oder Falsch.
2. Er unterstützt die Abgrenzung und das Einlesen des Codes.
3. Nirgends; der QR enthält nur das Ergebniswort.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Verwendung: Für die genaue Erwartung an den QR-Payload.

2. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator  
   Verwendung: Technische Grundlage für die einfache, lokale QR-Generierung im Browser.

Abgerufen: `2026-04-09`
