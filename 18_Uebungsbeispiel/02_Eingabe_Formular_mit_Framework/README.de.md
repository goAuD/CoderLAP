# Eingabe-Formular mit Framework

## Schneller visueller Überblick

| Pflichtfeld | Warum nötig? |
|---|---|
| Vorname | Stammdaten |
| Nachname | Stammdaten |
| SV-NR | Validierung und QR-Ergebnis |

## Warum ist `Bootstrap` hier gut geeignet?

- Man bekommt schnell ein ordentliches Formular
- Einfacher, ein responsives Layout zu erstellen
- Weniger eigenes CSS nötig

## Minimale Formularanforderungen

- Gut lesbare Feldbeschriftungen
- `Senden`- oder `Prüfen`-Button
- Kennzeichnung der Pflichtfelder
- Fehlermeldung, wenn ein Feld fehlt

## Worauf muss man achten?

- Nicht zu überladen gestalten
- Auf Mobilgeräten dürfen die Felder nicht verrutschen
- Die Fehlermeldung muss eindeutig sein

## Ausschnitt: Beschriftung und geeigneter Feldtyp

Dieser HTML-Ausschnitt für den Browser zeigt ein Formularfeld:

```html
<label for="svnummer">SV-NR</label>
<input id="svnummer" name="svnummer" type="text"
       inputmode="numeric" required aria-describedby="sv-help">
<p id="sv-help">10 Ziffern, zum Beispiel 4422 180599.</p>
```

`id` und `for` verbinden Beschriftung und Feld. `required` kennzeichnet das Pflichtfeld.
`inputmode` empfiehlt eine mobile Tastatur, **validiert aber nicht**.
Die SV-Nummer ist eine Kennung; wir behandeln sie als Text, nicht als Rechenwert im Feldtyp `number`.

Die Musterlösung verwendet `novalidate`, deshalb liefert ihr JavaScript die Rückmeldungen.
Durch `trim()` gilt auch ein Name nur aus Leerraum als leer.
Für Namen verwenden wir kein Buchstabenmuster, das Akzente, Bindestriche oder Apostrophe ausschließt.
Bei fehlenden Feldern stoppen wir; bei vollständiger Eingabe mit falscher SV-Nummer lautet der QR-Inhalt `Falsch`.

In Bootstrap stellt `col-12 col-md-6` die Namensfelder in schmalen Ansichten untereinander
und ab dem `md`-Breakpoint in zwei Spalten dar. Wir prüfen die Bedienbarkeit auch durch
tatsächliche Eingaben und mit der Tab-Taste.

Quellen: [MDN: required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required),
[MDN: inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode),
[Bootstrap-Raster](https://getbootstrap.com/docs/5.3/layout/grid/).

## Prüfungstaugliche Formulierung

> Der erste Teil der praktischen Aufgabe ist die Erstellung eines einfachen, responsiven HTML-Formulars mit den  
> Feldern `Vorname`, `Nachname` und `SV-NR`.  
> Die Verwendung von `Bootstrap` ist vorteilhaft, da es schnell ein ordentliches und mobilfreundliches Layout bietet.  
> Wichtig ist, dass die Ausfüllung der relevanten Felder beim Klick auf den Button überprüft wird.

## Schnelle Selbstkontrolle

1. Was bewirkt inputmode?
2. Warum verwenden wir trim() beim Namen?
3. Wie unterscheiden sich fehlende Felder und eine ausgefüllte, falsche SV-Nummer?

## Kurzantworten zur Selbstkontrolle

1. Es empfiehlt eine Tastatur, prüft aber nicht das Format.
2. Ein Name nur aus Leerraum soll als leer gelten.
3. Bei fehlenden Feldern kein QR; bei vollständiger Eingabe und falscher SV-Nummer entsteht Falsch.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Verwendung: Für die minimalen Pflichtelemente des Formulars.

2. Bootstrap Forms  
   https://getbootstrap.com/docs/5.3/forms/overview/  
   Verwendung: Offizielle Quelle für die schnelle und responsive Formularerstellung.

3. Bootstrap Layout  
   https://getbootstrap.com/docs/5.3/layout/grid/  
   Verwendung: Offizielle Quelle für die responsive Rasterstruktur.

Abgerufen: `2026-04-09`
