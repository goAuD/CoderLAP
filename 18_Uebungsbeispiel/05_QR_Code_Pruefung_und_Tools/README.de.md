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

> **Wichtig (2026):** Der `CodeTwo QR Code Desktop Reader` hat auf der Herstellerseite den Status **deprecated** - er
> steht nicht mehr zum Download bereit und wird nicht mehr aktualisiert. Die PDF nennt noch dieses Tool, daher ist es
> ratsam, den Namen für die Prüfung zu kennen, aber in der Praxis kann auch ein alternativer QR-Reader benötigt werden,
> zum Beispiel die Handykamera, ein browserbasierter Online-Decoder oder ein anderer kostenloser Desktop-Scanner.

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

## Prüfungstaugliche Formulierung

> Die Korrektheit des generierten QR-Codes muss separat mit einem Lesegerät oder Desktop-Scanner überprüft werden.  
> Ziel ist der Nachweis, dass der Code tatsächlich den gewünschten Inhalt enthält, also den Text `Richtig` oder  
> `Falsch`.  
> Die PDF nennt dafür als Beispiel die Verwendung des `CodeTwo QR Code Desktop Reader`.

## Häufige Prüfungsfehler

- Den QR-Code nicht durch Rücklesen zu überprüfen.
- Sich nur auf das Erscheinungsbild zu verlassen.
- Nicht mit gültigen und ungültigen Beispielnummern zu testen.
- Die Lesbarkeit des QR-Codes nicht bei kleinerer Bildschirmgröße zu prüfen.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Verwendung: Für das empfohlene Tool und das Überprüfungsprinzip.

2. CodeTwo QR Code Desktop Reader  
   https://www.codetwo.com/freeware/qr-code-desktop-reader/  
   Verwendung: Offizielle Seite des in der PDF genannten Überprüfungstools.

Abgerufen: `2026-04-09`
