# Testkonzepte

## Schneller visueller Überblick

| Element des Testkonzepts | Frage |
|---|---|
| Testziel | was wollen wir nachweisen? |
| Teststufe | wo testen wir? |
| Testtyp | was prüfen wir? |
| Testdaten | womit probieren wir es aus? |
| Ergebniskriterium | woher wissen wir, dass es gut ist? |

## Was ist ein Testkonzept?

Es ist ein Plan oder Ansatz dafür, wie wir die Qualität der Software überprüfen.

Es kann enthalten:

- das Ziel der Tests
- die Teststrategie
- die Teststufen
- die Testtypen
- die Werkzeuge
- die Verantwortlichkeiten

## Wichtige Teststufen

| Stufe | Worauf fokussiert sie? |
|---|---|
| Unit Test | auf eine kleine Einheit |
| Integration Test | auf das Zusammenwirken von Einheiten |
| System Test | auf das Gesamtsystem |
| Acceptance Test | auf geschäftliche / Benutzerakzeptanz |

## Wichtige Testtypen

Zum Beispiel:

- funktionaler Test
- nicht-funktionaler Test
- Regressionstest
- Sicherheitstest
- Usability-Test

## Warum ist das Testkonzept wichtig?

- systematisiert das Testen
- reduziert die Chance auf übersprungene Bereiche
- unterstützt die Ressourcenplanung
- verbessert die Transparenz

## Testkonzept und Testfall: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Testkonzept | übergeordneter Ansatz |
| Testfall | konkrete Testbeschreibung |

## Aus Risiken Testfälle ableiten

In einer Buchungsanwendung sind doppelte Buchungen und Überbuchung des letzten
Platzes wichtige Risiken. Dafür entstehen Nachweise auf mehreren Ebenen:

| Stufe | Konkrete Prüfung |
|---|---|
| Unit | die Kapazitätsregel akzeptiert gültige Anzahlen |
| Integration | Anwendung und Datenbank sichern gemeinsam die Eindeutigkeit |
| System | bei zwei gleichzeitigen Anfragen erhält nur eine den letzten Platz |
| Abnahme | Benutzer verstehen Bestätigung und ausgebuchten Zustand |

Für eine erlaubte ganze Anzahl von `1..30` steht etwa 12 für eine gültige
Äquivalenzklasse. An den Grenzen wählen wir `0, 1, 2, 29, 30, 31`. Gebrochene
Zahlen, Text und fehlende Werte bilden weitere Eingabegruppen. Damit prüfen
wir konkrete Annahmen, nicht sämtliche möglichen Eingaben.

Die **Black-box**-Sicht leitet Fälle aus dem Vertrag ab. **White-box** nutzt
zusätzlich die innere Struktur, etwa beide Ausgänge einer Verzweigung.
Überdeckung hilft bei der Suche nach Lücken. Auch 100% Codeüberdeckung beweist
jedoch weder die richtige Anforderung noch die Prüfung aller wichtigen Zustandskombinationen.

## Prüfungstaugliche Formulierung

> Das Testkonzept legt fest, wie wir die Qualität der Software überprüfen wollen.  
> Es beschreibt das Testziel, die Teststufen, die Testtypen, die verwendeten Methoden und die Grundlage der  
> Ergebnisbewertung.  
> Ein gutes Testkonzept stellt sicher, dass das Testen nicht zufällig, sondern bewusst und geplant erfolgt.

## Schnelle Selbstkontrolle

1. Was ist ein Testkonzept?
2. Welche Elemente kann es enthalten?
3. Was ist der Unterschied zwischen Testkonzept und Testfall?
4. Welche Teststufen kennen Sie?
5. Warum ist es wichtig, das Testen im Voraus zu planen?

## Kurzantworten zur Selbstkontrolle

1. Die Beschreibung des Testansatzes
2. Ziele, Stufen, Typen, Werkzeuge, Verantwortlichkeiten
3. Das eine ist Strategie, das andere eine konkrete Prüfung
4. Unit, Integration, System, Acceptance
5. Weil es so übersichtlicher und vollständiger wird

## Quellen

Geprüft: `2026-10-14`.

- [ISTQB CTFL 4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf): Teststufen und Testentwurfstechniken.


1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: offizielle Primärquelle zu den grundlegenden Testbegriffen, Teststufen und Testtypen.

2. OWASP Web Security Testing Guide  
   https://owasp.org/www-project-web-security-testing-guide/  
   Verwendung: offizielles, modernes Beispiel dafür, wie ein Testkonzept in einem konkreten Testbereich umgesetzt wird.

Abgerufen: `2026-04-09`
