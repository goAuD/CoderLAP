# Userinterface

## Schneller visueller Überblick

| UI-Element | Aufgabe |
|---|---|
| Button | eine Aktion starten |
| Menü | Navigation |
| Eingabefeld | Dateneingabe |
| Icon | visuelle Bedeutung |
| Feedback | Zustandsmitteilung |

## Was ist ein User Interface?

Die Benutzeroberfläche ist das physische oder logische Werkzeugsystem,
mit dem der Benutzer eine Anwendung, ein Gerät oder einen Prozess nutzen kann.

In einer Webumgebung ist das typischerweise:

- Seitenstruktur
- Navigation
- Formulare
- Buttons
- Tabellen
- Zustandsanzeigen
- Fehlermeldungen

## Warum ist das wichtig?

Weil der Benutzer nicht den Quellcode sieht, sondern die Oberfläche.

Ein gutes UI:

- ist verständlich
- ist konsistent
- ist leicht bedienbar
- ist schnell erlernbar
- gibt eindeutiges Feedback

Ein schlechtes UI:

- ist verwirrend
- verlangsamt die Arbeit
- erhöht die Fehlerwahrscheinlichkeit
- verringert die Zufriedenheit

## Die Grundprinzipien eines guten UI

- Eindeutigkeit
- Konsistenz
- übersichtliche Navigation
- gute Lesbarkeit
- sichtbares Feedback
- Barrierefreiheit

## UI und UX: nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| UI | die Oberfläche selbst und ihre Elemente |
| UX | das gesamte Benutzererlebnis |

UI umfasst die bedienbare Oberfläche einschließlich Tastatur und assistiver Technik. UX betrachtet das gesamte Nutzungserlebnis und seine Effizienz.

## Worauf muss man als Entwickler achten?

- Die Oberfläche sollte auf den ersten Blick verständlich sein.
- Für Fehler sollte es klare Fehlermeldungen geben.
- Formulare sollten logisch aufgebaut sein.
- Unterschiede zwischen Mobil- und Desktop-Ansicht müssen geplant werden.
- Barrierefreiheit ist kein optionales Extra, sondern eine Qualitätsanforderung.

## Eine kleine Oberfläche mit vollständiger Rückmeldung

Der folgende HTML-Ausschnitt gehört in `body` eines im Browser geöffneten
Dokuments. Er zeigt ein Ziel an und speichert es nicht in einer Datenbank:

```html
<form id="goal-form">
  <label for="minutes">Lernzeit in Minuten (1 bis 120)</label>
  <input id="minutes" name="minutes" type="number" min="1" max="120" required>
  <button type="submit">Lernziel anzeigen</button>
</form>
<p id="goal-status" role="status"></p>
<script>
  const form = document.querySelector("#goal-form");
  const minutes = document.querySelector("#minutes");
  const status = document.querySelector("#goal-status");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    status.textContent = `Lernziel: ${minutes.valueAsNumber} Minuten`;
  });
</script>
```

Nach Eingabe von `25` und Aktivieren des Buttons erscheint
`Lernziel: 25 Minuten`. Ein leeres Feld sowie `0` oder `121` werden durch die
normale Formularvalidierung des Browsers zurückgewiesen. Dann läuft der
`submit`-Handler nicht. Werden Daten an einen Server gesendet, muss dieser
dieselben Bedingungen nochmals prüfen.

Das sichtbare `label` gehört durch übereinstimmende `for`- und `id`-Werte zum
Feld. Der native Button lässt sich auch per Tastatur aktivieren; ein klickbares
`div` ist unnötig. `role="status"` meldet das aktualisierte Ergebnis auch an
assistive Technologien. Zur Prüfung bedienen wir das Formular ausschließlich
mit Tab, Shift+Tab und Enter und erhalten die sichtbare Fokusmarkierung.

Dies ist eine UI-Aufgabe: Beschriftung, Eingabegrenzen, Aktion und Rückmeldung
wirken zusammen. Zur Bewertung der gesamten UX prüfen wir zusätzlich, ob das
Ziel verständlich ist, wie aufwendig seine Eingabe ist und ob es beim Lernen hilft.

## Prüfungstaugliche Formulierung

> Das User Interface ist der Teil des Systems, über den der Benutzer mit der Anwendung oder dem Gerät interagiert.  
> Dazu gehören zum Beispiel Buttons, Menüs, Formulare, Icons und Feedback-Elemente.  
> Eine gute Benutzeroberfläche ist verständlich, konsistent, leicht bedienbar und unterstützt fehlerfreie Nutzung.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von UI?
2. Nenne vier typische UI-Elemente.
3. Warum ist Konsistenz wichtig?
4. Was ist der Unterschied zwischen UI und UX?
5. Warum ist Barrierefreiheit wichtig?

## Kurzantworten zur Selbstkontrolle

1. Die Schnittstelle zwischen Mensch und System
2. Button, Menü, Eingabefeld, Icon
3. Weil sie die Nutzung erleichtert
4. UI ist die Oberfläche, UX ist das gesamte Erlebnis
5. Weil sie das System für verschiedene Benutzer nutzbar macht

## Quellen

- [W3C: role=status](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22): semantische Kennzeichnung dynamischer Statusmeldungen. Geprüft: `2026-10-14`.

Geprüft: `2026-10-14`.

- [W3C WAI: Labeling controls](https://www.w3.org/WAI/tutorials/forms/labels/): sichtbare, programmatisch verbundene Beschriftungen.


1. NIST CSRC Glossary - User interface  
   https://csrc.nist.gov/glossary/term/user_interface  
   Verwendung: kurze, offizielle Definition des UI-Begriffs.

2. W3C WAI - Introduction to Web Accessibility  
   https://www.w3.org/WAI/fundamentals/accessibility-intro/  
   Verwendung: offizieller Hintergrund dafür, dass eine gute Oberfläche nicht nur schön, sondern auch zugänglich sein muss.

3. MDN - Accessibility  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility  
   Verwendung: aus Entwicklersicht die praktische Verbindung zu einer gut gestalteten Benutzeroberfläche.

Abgerufen: `2026-04-08`
