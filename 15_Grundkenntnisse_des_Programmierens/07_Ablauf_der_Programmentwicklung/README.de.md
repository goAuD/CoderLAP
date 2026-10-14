# Ablauf der Programmentwicklung

## Schneller visueller Überblick

```text
Aufgabe verstehen
    -> Lösung entwerfen
    -> Codierung
    -> Ausführung / Kompilierung
    -> Fehlersuche
    -> Testen
    -> Korrektur / Verfeinerung
```

## Warum ist das anders als der gesamte Software-Lebenszyklus?

Die vorherigen, größeren Lebenszyklusphasen bieten eher eine Sicht auf Projektebene.  
Der `Ablauf der Programmentwicklung` beschreibt eher den praktischen Arbeitsablauf des Entwicklers.

## Typische Schritte im Detail

### 1. Aufgabe verstehen

Man muss verstehen:

- was das Ziel ist
- was die Eingabe ist
- was die Ausgabe ist
- welche Regeln befolgt werden müssen

### 2. Lösung entwerfen

Hier kommt:

- Algorithmus
- Pseudocode
- Flussdiagramm
- Auswahl der Datenstruktur

### 3. Codierung

Den Entwurf umwandeln in:

- konkrete Programmiersprachanweisungen
- Funktionen
- Variablen
- Strukturen

### 4. Ausführung oder Kompilierung

Hier zeigt sich zum Beispiel:

- ob Syntaxfehler vorhanden sind
- ob das Programm startet
- ob die Umgebung korrekt konfiguriert ist

### 5. Debugging

Wenn ein Fehler vorhanden ist:

- muss die Ursache gefunden werden
- müssen die Variablen beobachtet werden
- muss der Kontrollfluss überprüft werden

### 6. Testen

Hier zählt nicht nur, ob es "durchläuft", sondern auch:

- ob es das richtige Ergebnis liefert
- ob es auch in Randfällen korrekt funktioniert

### 7. Korrektur und Verfeinerung

Oft muss man zurück:

- zur Logik
- zum Code
- oder sogar zum Entwurf

## Das ist keine einmalige Reihenfolge, sondern ein Zyklus

Bei der Prüfung lohnt es sich zu sagen:

- die Entwicklung ist oft iterativ
- Fehlerbehebung und Testen wiederholen sich mehrmals

## Der vollständige Entwicklungszyklus einer kleinen Aufgabe

Anforderung: Ab 50 Euro ist der Versand kostenlos, darunter kostet er 4,90 Euro.
Beträge kommen als ganze Cent an; negative oder gebrochene Eingaben werden
abgewiesen. Zuerst legen wir die erwarteten Grenzfälle fest, dann implementieren
wir die Regel. Ausführung: Node.js.

<!-- example:run -->

```javascript
function shippingCents(totalCents) {
  if (!Number.isSafeInteger(totalCents) || totalCents < 0) {
    throw new RangeError("Nonnegative integer cents required");
  }
  return totalCents >= 5000 ? 0 : 490;
}
for (const [input, expected] of [[0, 490], [4999, 490], [5000, 0], [5001, 0]]) {
  console.log(input, shippingCents(input) === expected);
}
```

```text
0 true
4999 true
5000 true
5001 true
```

Der Wechsel zwischen `4999` und `5000` prüft die Bedeutung von „ab 50 Euro“.
Viermal `true` zeigt die Übereinstimmung von berechnetem und erwartetem Preis.
Die Fälle stammen aus der Spezifikation, nicht aus einer Wiederholung des Codes.
Für ungültige Eingaben erwarten wir in einem gesonderten Test einen `RangeError`.
Nach einer Änderung führen wir auch die bisherigen Fälle erneut aus: Das ist
eine Regressionsprüfung. Die kleine Funktion lässt sich getrennt von Oberfläche
und Datenbank testen.

## Prüfungstaugliche Formulierung

> Der praktische Ablauf der Programmentwicklung beginnt in der Regel mit dem Verstehen der Aufgabe, gefolgt vom  
> Entwurf der Lösung, der Codierung, der Ausführung oder Kompilierung, der Fehlersuche, dem Testen und der Korrektur.  
> Dieser Prozess ist in der Praxis oft iterativ, da der Entwickler aufgrund von Tests und Fehlern zu früheren  
> Schritten zurückkehren kann.  
> Das Ziel ist nicht nur ein lauffähiges Programm, sondern ein korrektes und zuverlässiges Programm.

## Schnelle Selbstkontrolle

1. Womit beginnt die Programmentwicklung?
2. Warum ist der Entwurf wichtig?
3. Was ist der Unterschied zwischen Ausführung und Testen?
4. Was ist die Rolle des Debuggers?
5. Warum ist der Prozess iterativ?

## Kurzantworten zur Selbstkontrolle

1. Mit dem Verstehen der Aufgabe
2. Weil man damit strukturierter codieren kann
3. Die Ausführung beweist noch keine korrekte Funktion
4. Er hilft, die Ursachen von Fehlern zu finden
5. Weil man wegen Fehlern zu früheren Schritten zurückkehren muss

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Number.isSafeInteger](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger): Prüfung ganzzahliger Centbeträge.


1. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Verwendung: Hintergrund zur logischen Reihenfolge der Entwicklungsschritte.

2. Atlassian - SDLC  
   https://www.atlassian.com/en/agile/software-development/sdlc  
   Verwendung: praxisnahe Zusammenfassung zum iterativen Charakter des Entwicklungsprozesses.

Abgerufen: `2026-04-09`
