# Mobile First

## Schneller visueller Überblick

| Reihenfolge | Was bedeutet das? |
|---|---|
| 1. Mobil | inhaltliches Wesentliches, einfaches Layout |
| 2. Tablet | mehr Platz, Erweiterung |
| 3. Desktop | Layout nutzt mehr Platz, dieselben Kernaufgaben bleiben erhalten |

## Warum ist Mobile First gut?

Weil es dazu zwingt:

- sich auf das Wesentliche zu konzentrieren
- eine einfache, saubere Oberfläche zu gestalten
- die Seite nicht zu überladen

Das liefert oft bessere Ergebnisse, als wenn man eine große Desktop-Seite später zu "komprimieren" versucht.

## Wie funktioniert es technisch?

Häufiger Ansatz:

- Basis-CSS für die mobile Ansicht
- für größere Ansichten `min-width`-basierte Media Queries

Also:

- zuerst wird die Basislösung erstellt
- dann werden schrittweise die Erweiterungen hinzugefügt

## Mobile First und Responsive: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Mobile First | Designstrategie |
| Responsive | das anpassungsfähige Endergebnis |

## Warum ist das heute wichtig?

- die Mobilnutzung ist sehr stark
- viele Benutzer kommen zuerst vom Telefon
- Leistung und Einfachheit sind auf Mobilgeräten besonders kritisch

## Worauf muss man achten?

- Mobile First bedeutet nicht, dass man für Desktop nicht mehr gut gestalten muss.
- In der mobilen Ansicht muss der Inhalt priorisiert werden.
- Leistung und Navigation sind Schlüsselfragen.
- Die Logik der schrittweisen Erweiterung muss konsequent angewendet werden.

## Von der Aufgabe aus planen: ein Thema finden

Eine lernende Person sucht auch am Telefon ein Thema, öffnet die Erklärung und
kehrt zu den Treffern zurück. Diese Kernaufgabe ist am Desktop dieselbe. Zuerst
machen wir sie gut bedienbar: sichtbare Suche, verständliche Titel, funktionierender
Rückweg und lesbarer Inhalt. Bei mehr Platz kann später eine dauerhafte
Seitenleiste hinzukommen. Grundlegende Funktionen bleiben auch mobil verfügbar.

**CSS-Ausschnitt für den Browser:** In `.navigation` liegen normale HTML-Links.
Das Dokument verwendet einen üblichen Viewport-Metatag.

```css
.navigation {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

@media (min-width: 48rem) {
  .navigation { flex-direction: row; flex-wrap: wrap; }
}
```

Standardmäßig stehen die Links untereinander. Ab `48rem` Viewportbreite stehen
sie nebeneinander und brechen bei Bedarf um. `48rem` ist der gewählte Breakpoint
dieses Entwurfs, keine allgemeine Tablet-Grenze. CSS-Pixel sind auch nicht
identisch mit den physischen Gerätepixeln; beim Zoomen kann sich die verfügbare
CSS-Breite ändern.

**Progressive Enhancement:** Ein einfacher HTML-Link kann ohne JavaScript
navigieren; JavaScript ergänzt später schnelles Filtern oder Animationen. Davon
getrennt ist die Entscheidung, das Layout zuerst für schmale Ansichten zu
entwerfen. Mobile First garantiert keine gute Leistung: Wir messen auch die
übertragenen Bild- und Codemengen. Probiere die Aufgabe mit Tastatur, 200%
Vergrößerung und langsamer Verbindung aus.

## Prüfungstaugliche Formulierung

> Mobile First ist eine Webdesign-Strategie,
> die die Entwicklung mit der für den kleinsten Bildschirm optimierten Ansicht beginnt
> und dann die Oberfläche für größere Geräte erweitert.
> Der Vorteil ist,
> dass die Priorität von Inhalt und Funktionalität klarer sichtbar wird
> und die Oberfläche in der Regel einfacher,
> schneller und auch auf Mobilgeräten besser nutzbar wird.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Mobile First?
2. Warum ist das oft besser als vom Desktop aus zu starten?
3. Was ist der Zusammenhang mit Responsive Design?
4. Was muss man bei Mobile First zuerst entscheiden?
5. Warum ist die Leistung wichtig?

## Kurzantworten zur Selbstkontrolle

1. Wir starten vom Mobilgerät und erweitern von dort
2. Weil es zum Wesentlichen zwingt
3. Mobile First ist die Strategie, Responsive die umgesetzte Anpassung
4. Was der wichtigste Inhalt und die wichtigste Funktion ist
5. Weil der Benutzer auf Mobilgeräten besonders empfindlich darauf reagiert

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design): Mobile-First-Media-Queries, Viewport und skalierbare Oberfläche.


1. MDN - Mobile First
   https://developer.mozilla.org/en-US/docs/Glossary/Mobile_First
   Verwendung: kurze, präzise begriffliche Definition.

2. MDN - Responsive design
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
   Verwendung: technischer Hintergrund für aus Mobile First aufgebaute responsive Lösungen.

3. web.dev - Learn Design
   https://web.dev/learn/design/
   Verwendung: moderne praktische Richtlinien für mobilzentriertes Webdesign.

Abgerufen: `2026-04-08`
