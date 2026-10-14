# QR-Code Pruefung und Tools

## Schneller visueller Überblick

```text
Formular ausfüllen
    -> QR generieren
    -> mit Scanner einlesen
    -> Inhalt überprüfen
```

## Was empfiehlt die PDF?

Die PDF erwähnt ausdrücklich:

- `CodeTwo QR Code Desktop Reader`

Dieser ist dafür geeignet:

- Einen am Bildschirm angezeigten QR-Code zu überprüfen
- Den generierten Code auch ohne Telefon zurücklesen zu können

> CodeTwo bietet das Werkzeug nicht mehr zum Download an und unterstützt es nicht mehr.
> Gleichzeitig verbietet die PDF die Handynutzung in der Prüfung ausdrücklich.
> Wir bereiten deshalb einen vorab abgestimmten, zugelassenen Desktop-Reader vor
> und testen ihn in der Prüfungsumgebung. Ein Handyscan zu Hause ersetzt das nicht.

## Was muss man überprüfen?

- Ob der QR-Code tatsächlich lesbar ist
- Ob der Inhalt genau `Richtig` oder `Falsch` lautet
- Ob bei den gültigen und ungültigen Testbeispielen korrekt gewechselt wird

## Einfache Überprüfungsschritte

1. Musterlösung starten
2. Eine gültige `SV-Nr` eingeben
3. Den QR-Code zurücklesen
4. Mit einer ungültigen `SV-Nr` wiederholen
5. Prüfen, ob das Ergebnis korrekt ist

## Kurze Abnahmeprüfung

1. Mit erfundenen Namen und `4422 180599` liest der separate Reader `Richtig`.
2. Beim Eintragen von `2511 010100` im selben Formular verschwindet der alte QR.
   Nach erneuter Prüfung lautet der zurückgelesene Inhalt `Falsch`.
3. Leeren und Absenden des SV-Felds meldet ein fehlendes Feld, ohne QR-Ausgabe.
4. Nach erneuter gültiger Eingabe ist wieder `Richtig` lesbar. Damit sind auch aufeinanderfolgende Zustände geprüft.

Die Beschriftung neben dem QR zu prüfen reicht nicht: Der Reader muss dasselbe Wort
**aus dem Bild** rekonstruieren. Der Code muss vollständig sichtbar sein, mit geeignetem
Kontrast und freiem Rand. Vergrößerung und schmale Ansicht gehören ebenfalls zur Probe.
Installation, Zulassung und Funktion des Readers klären wir vorab.

Quellen: Katalog, Seite 12 und [aktueller CodeTwo-Herstellerhinweis](https://www.codetwo.com/freeware/qr-code-desktop-reader/).
Geprüft: `2026-10-14`.

## Prüfungstaugliche Formulierung

> Die Korrektheit des generierten QR-Codes muss separat mit einem Lesegerät oder Desktop-Scanner überprüft werden.  
> Ziel ist der Nachweis, dass der Code tatsächlich den gewünschten Inhalt enthält, also den Text `Richtig` oder  
> `Falsch`.  
> Die PDF nennt dafür als Beispiel die Verwendung des `CodeTwo QR Code Desktop Reader`.

## Schnelle Selbstkontrolle

1. Was bestätigt den tatsächlichen QR-Inhalt?
2. Welches Werkzeug bereiten wir für die PDF-Prüfung vor?
3. Warum testen wir zwei verschiedene Nummern nacheinander?

## Kurzantworten zur Selbstkontrolle

1. Ein separater Reader rekonstruiert das erwartete Wort aus dem Bild.
2. Einen vorab abgestimmten, zugelassenen Desktop-Reader ohne Handynutzung.
3. So prüfen wir auch das Entfernen des alten und die Ausgabe des neuen Ergebnisses.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Verwendung: Für das empfohlene Tool und das Überprüfungsprinzip.

2. CodeTwo QR Code Desktop Reader  
   https://www.codetwo.com/freeware/qr-code-desktop-reader/  
   Verwendung: Offizielle Seite des in der PDF genannten Überprüfungstools.

Abgerufen: `2026-04-09`
