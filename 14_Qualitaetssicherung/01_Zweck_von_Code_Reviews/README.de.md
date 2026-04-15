# Zweck von Code Reviews

## Schneller visueller Überblick

| Ziel | Was bringt es? |
|---|---|
| Früherkennung von Fehlern | weniger späte Korrekturen |
| Qualitätsverbesserung | besser lesbarer, einheitlicherer Code |
| Wissensaustausch | mehr Personen verstehen das System |
| Risikominimierung | weniger Einpersonenwissen |

## Was ist ein Code Review?

Beim Code Review schaut sich jemand anderes den geänderten Code an.

Typischerweise wird geprüft:

- ob die Lösung korrekt ist
- ob der Code verständlich ist
- ob die Teamregeln eingehalten werden
- ob Risiken oder Nebenwirkungen bestehen
- ob Tests oder Dokumentation fehlen

## Was ist das Hauptziel?

Das Code Review ist nicht nur Fehlersuche.

Hauptziele:

- Früherkennung technischer Fehler
- Verbesserung der Codequalität
- Einhaltung einheitlicher Stile und Regeln
- Teamweites Lernen
- Sichereres Merging

## Wofür ist es nicht gedacht?

- nicht als persönliche Kritik
- nicht als Machtinstrument
- nicht nur als Suche nach formalen Fehlern
- es soll nicht zu endlosen Diskussionen werden

## Code Review und Testen: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Code Review | ein Mensch sieht sich den Code an |
| Testen | das Verhalten wird zur Laufzeit überprüft |

Beide ergänzen sich, ersetzen sich aber nicht.

## Prüfungstaugliche Formulierung

> Ziel des Code Reviews ist es,
> dass der Quellcode vor dem produktiven Einsatz oder dem Merge
> von einem anderen Entwickler überprüft wird.  
> Dadurch können Fehler frühzeitig erkannt,
> die Codequalität verbessert
> und der Wissensaustausch im Team gestärkt werden.  
> Das Code Review ist somit nicht nur ein Werkzeug zur Fehlersuche,
> sondern auch ein Instrument
> der Qualitätssicherung und Zusammenarbeit.

## Häufige Prüfungsfehler

- Das Code Review lediglich als Rechtschreibprüfung betrachten.
- Den Wissensaustausch nicht erwähnen.
- Behaupten, dass das Code Review das Testen ersetzt.
- Persönliche Kritik mit fachlicher Überprüfung verwechseln.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel des Code Reviews?
2. Warum sollte es vor dem Merge durchgeführt werden?
3. Wie unterstützt es das Team?
4. Warum ist es nicht dasselbe wie Testen?
5. Welche Arten von Problemen können dabei aufgedeckt werden?

## Kurzantworten zur Selbstkontrolle

1. Früherkennung von Fehlern und Qualitätsverbesserung
2. Weil es günstiger ist, Fehler früh zu beheben
3. Durch Wissensaustausch und ein gemeinsames Qualitätsniveau
4. Weil es eine menschliche Überprüfung ist, keine Laufzeitkontrolle
5. Logische, stilistische, sicherheitsrelevante oder wartungsbezogene Probleme

## Quellen

1. GitHub - Code review  
   https://github.com/features/code-review  
   Verwendung: offizielle, moderne Quelle zur Rolle von Code Reviews im Entwicklungsprozess.

2. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: offizieller Hintergrund zur Rolle von statischem Testen und Reviews in der Qualitätssicherung.

Abgerufen: `2026-04-08`
