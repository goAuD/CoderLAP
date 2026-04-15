# Call By Value und Call By Reference

## Schneller visueller Überblick

| Modus | Was passiert? |
|---|---|
| `call by value` | die Funktion arbeitet mit einer Kopie |
| `call by reference` | die Funktion ist mit den Originaldaten verbunden |

## Was ist `call by value`?

Dabei erhält die Funktion:

- eine Kopie des Parameterwerts
- die Änderung überschreibt in der Regel nicht direkt die Originalvariable

Vorteil:

- sicherer, da weniger unerwartete Seiteneffekte

## Was ist `call by reference`?

Dabei arbeitet die Funktion:

- nicht mit einer einfachen Kopie
- sondern erhält Zugriff so, dass auch die Originaldaten geändert werden können

Vorteil:

- in bestimmten Situationen effizienter
- ermöglicht direktere Änderungen

## Warum muss man vorsichtig formulieren?

Weil moderne Sprachen nicht immer rein das eine oder das andere implementieren.

Zum Beispiel:

- einige Sprachen verwenden nur Wertübergabe, aber mit Referenztypen
- andere unterstützen auch echte Referenzübergabe

Bei der Prüfung muss man daher das Grundprinzip gut verstehen:

- Kopie oder direkterer Zugriff auf das Original

## Wann ist das relevant?

- beim Entwurf von Funktionen
- beim Verständnis von Seiteneffekten
- bei der Fehlersuche
- im Hinblick auf Leistung und Speicher

## Seiteneffekt: Schlüsselbegriff

Wenn eine Funktion die von außen erhaltenen Daten verändert, kann das ein Seiteneffekt sein.

Daher ein guter Prüfungssatz:

- `call by reference`-artiges Verhalten kann stärkere Seiteneffekte verursachen

## Prüfungstaugliche Formulierung

> Bei `call by value` arbeitet die Funktion mit einer Kopie des Parameterwerts, daher beeinflusst die Änderung in der  
> Regel nicht direkt die Originalvariable.  
> Bei `call by reference` greift die Funktion über eine Referenz auf die Daten zu, daher kann auch der Originalwert  
> geändert werden.  
> Die genaue Implementierung kann je nach Programmiersprache unterschiedlich sein, aber der grundlegende Unterschied
> liegt zwischen Kopie und direkterem Zugriff.

## Häufige Prüfungsfehler

- Behaupten, dass alle Sprachen gleich funktionieren.
- Die Möglichkeit von Seiteneffekten nicht erwähnen.
- Referenz vollständig mit Pointer gleichsetzen.
- So tun, als wäre die Parameterübergabe nur ein technisches Detail.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von `call by value`?
2. Was ist das Wesentliche von `call by reference`?
3. Warum ist das bei Funktionen wichtig?
4. Was ist ein Risiko der referenzbasierten Änderung?
5. Warum muss man bei der Verallgemeinerung zwischen Sprachen vorsichtig sein?

## Kurzantworten zur Selbstkontrolle

1. Die Funktion erhält eine Kopie
2. Sie arbeitet verbunden mit dem Original
3. Weil es die Änderbarkeit und Fehler beeinflusst
4. Unerwarteter Seiteneffekt
5. Weil die genaue Implementierung unterschiedlich sein kann

## Quellen

1. Microsoft Learn - Method Parameters (C#) - Pass by value and pass by reference  
   https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters  
   Verwendung: offizielle, gut verständliche Quelle zum grundlegenden Unterschied der beiden Parameterübergabemodi.

2. Oracle - Pass-By-Value Example  
   https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html  
   Verwendung: offizielle Quelle dafür, dass die sprachliche Implementierung und der allgemeine begriffliche Unterschied
   nicht immer dasselbe sind.

Abgerufen: `2026-04-09`
