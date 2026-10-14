# Ablaufdiagramm Flowchart

## Schneller visueller Überblick

| Symbol | Typische Bedeutung |
|---|---|
| Oval | Start / Ende |
| Rechteck | Operation |
| Raute | Entscheidung |
| Pfeil | Flussrichtung |

## Was ist ein Flowchart?

Ein Flowchart beschreibt visuell:

- welche Schritte aufeinander folgen
- wo ein Entscheidungspunkt liegt
- in welche Richtung der Prozess weitergeht

Deshalb wird es verwendet für:

- Algorithmen
- Geschäftsprozesse
- Arbeitsabläufe
- Dokumentation

## Warum ist es nützlich?

- schnell überschaubar
- in technischem und nicht-technischem Umfeld verständlich
- hilft beim Erkennen von Fehlern und fehlenden Schritten
- unterstützt die Kommunikation

## Flowchart und Struktogramm: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Flowchart | mit Pfeilen verbundenes Ablaufdiagramm |
| Struktogramm | blockbasiertes, strukturiertes Algorithmusdiagramm |

## Wann ist es eine gute Wahl?

- wenn der Ablauf eines Prozesses gezeigt werden soll
- wenn es mehrere Entscheidungspunkte gibt
- wenn die Funktionsweise auch dem Team oder Kunden erklärt werden muss

## Zwei vollständige Wege durch eine Entscheidung

In der üblichen Notation sind Start und Ende abgerundet, eine Aktion rechteckig, eine Entscheidung rautenförmig und Ein- oder Ausgabe ein Parallelogramm. Pfeile zeigen die Ausführungsrichtung. Eine Legende ist besonders hilfreich, wenn eine Organisation andere Symbole verwendet.

Beispiel zur Vorzeichenprüfung einer ganzen Zahl:

```text
Start -> n einlesen -> [n >= 0?]
                        | ja   -> "nicht negativ" ausgeben -> Ende
                        | nein -> "negativ" ausgeben       -> Ende
```

Dies ist eine Textskizze; in der Zeichnung steht die Frage in einer Raute. Die Entscheidungskanten tragen Ja/Nein-Beschriftungen. Die Eingabe `0` folgt dem Ja-Zweig, `-3` dem Nein-Zweig. Das Beispiel setzt bereits eine gültige ganze Zahl voraus. Für ein echtes Eingabeformular müssen auch Prüfung und erneute Eingabe dargestellt werden.

## Prüfungstaugliche Formulierung

> Ein Flowchart oder Ablaufdiagramm ist eine grafische Darstellung,
> die mit Symbolen und Pfeilen die Schritte eines Prozesses
> oder Algorithmus zeigt.  
> Mit seiner Hilfe lassen sich die Reihenfolge der Operationen,
> Entscheidungspunkte und Verzweigungen gut veranschaulichen.  
> Sein Vorteil ist, dass es leicht überschaubar
> und sowohl im technischen als auch im nicht-technischen Umfeld
> gut einsetzbar ist.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche am Flowchart?
2. Wofür dient die Raute?
3. Warum ist es in der Dokumentation nützlich?
4. Worin unterscheidet es sich vom Struktogramm?
5. Wo kann es außerhalb der Programmierung verwendet werden?

## Kurzantworten zur Selbstkontrolle

1. Visuelle Beschreibung von Prozessen
2. Kennzeichnet einen Entscheidungspunkt
3. Weil es schnell überschaubar ist
4. Es ist ein Ablaufdiagramm mit Pfeilen, keine blockbasierte Struktur
5. Auch bei geschäftlichen und organisatorischen Prozessen

## Quellen

- [Lucid: Flowchart Symbols and Their Meanings](https://lucid.co/diagram/flowchart/symbols)  
  Offizieller Leitfaden des Diagrammwerkzeugs zu üblichen Flussdiagrammsymbolen.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Lucid - Flowchart Symbols and Their Meanings  
   https://lucid.co/diagram/flowchart/symbols  
   Verwendung: klare, moderne Zusammenfassung des Flowchart-Begriffs und -Zwecks.

2. Atlassian - Flowchart template  
   https://www.atlassian.com/software/confluence/templates/flowchart  
   Verwendung: praktischer Unternehmens- und Dokumentationskontext zur Flowchart-Nutzung.

3. inf-schule - Bausteine von Algorithmen  
   https://inf-schule.de/algorithmen/grundlagen/algorithmusbegriff/bausteine  
   Verwendung: vergleichendes Bildungsbeispiel zum Unterschied zwischen Flowchart und Struktogramm.

Abgerufen: `2026-04-08`
