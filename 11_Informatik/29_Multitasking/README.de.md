# Multitasking

## Schneller visueller Überblick

| Situation | Was sieht der Benutzer? |
|---|---|
| Musik spielt, gleichzeitig surfen | mehrere Aufgaben laufen gleichzeitig |
| Datei kopieren und Dokument bearbeiten | System verwaltet mehrere Arbeiten |

## Was ist das Wesentliche von Multitasking?

Das Betriebssystem teilt die Prozessorzeit und andere Ressourcen zwischen mehreren Aufgaben auf.

Das kann geschehen durch:

- schnelle Zeiteinteilung
- Nutzung mehrerer Kerne
- Verwaltung von Prozessen und Threads

## Warum ist das wichtig?

- das System wird benutzerfreundlicher
- mehrere Anwendungen können gleichzeitig arbeiten
- es bietet eine bessere Benutzererfahrung
- Hintergrundaufgaben können während der Arbeit laufen

## Multitasking und Parallelität

| Begriff | Bedeutung |
|---|---|
| Multitasking | Verwaltung mehrerer Aufgaben in einem System |
| echte Parallelität | tatsächlich gleichzeitige Ausführung auf mehreren Kernen |
| Zeiteinteilung | sehr schnelles Wechseln zwischen Aufgaben |

## Wo tritt es auf?

- in Betriebssystemen
- in mobilen Systemen
- auf Servern
- teilweise auch in Browserumgebungen, z.B. bei Worker-Modellen

## Worauf muss man achten?

- Multitasking bedeutet nicht, dass alles immer wirklich gleichzeitig läuft.
- Mehr Aufgaben können mehr Ressourcen erfordern.
- Bei schlechter Belastung kann das System langsamer werden.
- Bei der Entwicklung muss man auf Thread-Sicherheit und gemeinsame Ressourcen achten.

## Prüfungstaugliche Formulierung

> Multitasking bedeutet,
> dass ein Betriebssystem mehrere Aufgaben oder Prozesse so verwaltet,
> dass sie für den Benutzer gleichzeitig erscheinen.
> Dies kann durch schnelle Zeiteinteilung oder durch Nutzung mehrerer Prozessorkerne erreicht werden.
> Ziel ist es, dass das System mehrere Anwendungen und Hintergrundoperationen effizient verwalten kann.

## Häufige Prüfungsfehler

- Multitasking vollständig mit echter Parallelität gleichsetzen.
- Die Rolle des Betriebssystems nicht erwähnen.
- Glauben, dass es auf einem einzelnen Prozessorkern kein Multitasking gibt.
- Nicht über Ressourcenteilung sprechen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Multitasking?
2. Was ist der Unterschied zwischen Multitasking und echter Parallelität?
3. Warum ist es für den Benutzer wichtig?
4. Wer verwaltet das typischerweise?
5. Was kann die technische Schwierigkeit sein?

## Kurzantworten zur Selbstkontrolle

1. Verwaltung mehrerer Aufgaben in einem System
2. Multitasking kann auch schnelles Umschalten sein, nicht nur echte gleichzeitige Ausführung
3. Weil man mehrere Dinge gleichzeitig nutzen kann
4. Das Betriebssystem
5. Ressourcenverwaltung und Thread-Sicherheit

## Quellen

1. Microsoft Support - How to multitask in Windows
   https://support.microsoft.com/en-us/windows/how-to-multitask-in-windows-b4fa0333-98f8-ef43-e25c-06d4fb1d6960
   Verwendung: praktisches, offizielles Beispiel für die Benutzerseite von Multitasking.

2. MDN - Thread
   https://developer.mozilla.org/en-US/docs/Glossary/Thread
   Verwendung: grundlegender begrifflicher Hintergrund zum Verständnis von Threads und Ausführungseinheiten.

3. MDN - Web Workers API
   https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API
   Verwendung: offizielles Beispiel für parallelere Aufgabenverarbeitung in der Browserumgebung.

Abgerufen: `2026-04-08`
