# Suchalgorithmen: sequentiell / binaer

## Schneller visueller Überblick

| Algorithmus | Voraussetzung | Typische Zeitkomplexität |
|---|---|---|
| sequenziell / linear | keine sortierte Liste nötig | `O(n)` |
| binär | sortierte Liste erforderlich | `O(log n)` |

## Was ist die sequenzielle Suche?

Die sequenzielle Suche:

- untersucht die Elemente der Reihe nach
- geht weiter, bis der gesuchte Wert gefunden wird
- oder die Liste zu Ende ist

Vorteil:

- sehr einfach
- kein sortierter Datensatz erforderlich

Nachteil:

- kann bei großen Listen langsam sein

## Was ist die binäre Suche?

Die binäre Suche ist nur bei **sortierten** Daten anwendbar.

Schritte:

1. das mittlere Element anschauen
2. mit dem gesuchten Wert vergleichen
3. entscheiden, ob links oder rechts weitergesucht werden muss
4. den verbleibenden Teil erneut halbieren

Deshalb kann sie viel schneller sein.

## Einfaches Beispiel

Gesuchter Wert: `42`

### Sequenzielle Suche

```text
5 -> 11 -> 19 -> 42
```

Man muss die Elemente der Reihe nach durchgehen.

### Binäre Suche

```text
sortierte Liste
-> mittleres Element
-> linke oder rechte Hälfte
-> neue Mitte
```

## Wann welche?

### Sequenzielle Suche

- bei kleinen Datenmengen
- bei unsortierten Daten
- als schnell implementierbare Lösung

### Binäre Suche

- bei größeren Datensätzen
- wenn die Daten sortiert sind
- wenn viele Suchvorgänge durchgeführt werden müssen

## Binäre Suche: wichtige Voraussetzung

Das ist ein Schlüsselpunkt bei der Prüfung:

- wenn die Daten nicht sortiert sind, ist die binäre Suche nicht direkt anwendbar

## Prüfungstaugliche Formulierung

> Die sequenzielle Suche untersucht die Elemente der Reihe nach, bis sie den gesuchten Wert findet oder das Listenende erreicht.  
> Die binäre Suche hingegen halbiert stets den Suchbereich und ist daher schneller, aber nur bei sortierten Daten anwendbar.  
> Der wichtigste Unterschied zwischen den beiden Algorithmen liegt im Funktionsprinzip und in der Sortierungsvoraussetzung.

## Häufige Prüfungsfehler

- Zu vergessen, dass die binäre Suche eine sortierte Liste erfordert.
- Zu behaupten, dass die binäre Suche immer besser ist.
- Die Einfachheit der linearen Suche nicht zu erwähnen.
- Die binäre Suche mit dem binären Baum zu verwechseln.

## Schnelle Selbstkontrolle

1. Wie funktioniert die sequenzielle Suche?
2. Was ist die Grundidee der binären Suche?
3. Was ist die Voraussetzung der binären Suche?
4. Welche ist einfacher?
5. Welche ist schneller bei einer großen sortierten Liste?

## Kurzantworten zur Selbstkontrolle

1. Sie untersucht die Elemente der Reihe nach
2. Den Suchbereich stets halbieren
3. Sortierte Daten
4. Die sequenzielle Suche
5. Die binäre Suche

## Quellen

1. NIST DADS - linear search  
   https://xlinux.nist.gov/dads/HTML/linearSearch.html  
   Verwendung: offizielle Definition und Komplexitätshintergrund zur sequenziellen Suche.

2. NIST DADS - binary search  
   https://xlinux.nist.gov/dads/HTML/binarySearch.html  
   Verwendung: offizielle Definition und Funktionshintergrund zur binären Suche.

Abgerufen: `2026-04-09`
