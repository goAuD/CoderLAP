# Zeichensatz ASCII

## Schneller visueller Überblick

| Bereich  | Typ               | Beispiel                | Wofür                                       |
| -------- | ----------------- | ----------------------- | ------------------------------------------- |
| `0-31`   | Steuerzeichen     | `LF`, `CR`, `TAB`       | keine sichtbaren Zeichen, sondern Steuerung |
| `32`     | Leerzeichen       | `SPACE`                 | Trennung                                    |
| `33-126` | druckbare Zeichen | `A`, `a`, `7`, `?`, `#` | Textdarstellung                             |
| `127`    | Steuerzeichen     | `DEL`                   | löschbezogenes Zeichen                      |

## Was ist ASCII?

ASCII steht für: **American Standard Code for Information Interchange**.  
Das Wesentliche ist, dass jedem Zeichen ein **Zahlencode** zugeordnet wird.

Zum Beispiel:

| Zeichen | Dezimal | Hexadezimal | 7-Bit Binär |
| ------- | ------: | ----------: | ----------: |
| `A`     |    `65` |        `41` |   `1000001` |
| `a`     |    `97` |        `61` |   `1100001` |
| `0`     |    `48` |        `30` |   `0110000` |
| `?`     |    `63` |        `3F` |   `0111111` |

Wichtig:

- ASCII ist **7-Bit**, nicht 8-Bit.
- In der Praxis wird es zwar oft auf **1 Byte** gespeichert, aber der ursprüngliche ASCII-Bereich umfasst nur `0-127`.
- Die Internet- und Standardbezeichnung lautet häufig **`US-ASCII`**.

## Was enthält es?

### 1. Steuerzeichen

Diese sind keine sichtbaren Buchstaben oder Zahlen, sondern bezeichnen eine Operation oder Steuerung.

Häufige Beispiele:

- `TAB` - Tabulator
- `LF` - Zeilenvorschub (Line Feed)
- `CR` - Wagenrücklauf (Carriage Return)
- `ESC` - Escape
- `DEL` - Löschen (Delete)

Diese sind vor allem bei älteren Datenübertragungen, beim Drucken, bei Terminals und auch heute noch in Dateiformaten und Protokollen wichtig.

### 2. Druckbare Zeichen

Dazu gehören:

- Großbuchstaben: `A-Z`
- Kleinbuchstaben: `a-z`
- Ziffern: `0-9`
- häufige Satz- und Sonderzeichen: `.` `,` `:` `;` `!` `?` `@` `#` `$` `%` `&`

## Warum ist es heute noch wichtig?

ASCII allein reicht für moderne, mehrsprachige Systeme nicht mehr aus, ist aber nach wie vor grundlegend, weil:

- viele technische Standards historisch darauf aufbauen
- viele Dateiformate und Protokolle ASCII-kompatibel sind
- die ersten `128` Zeichen von **UTF-8** genau mit ASCII übereinstimmen
- in der Programmierung, in Netzwerken, in Logs, HTTP-Headern und Konfigurationen ASCII immer noch häufig vorkommt

## ASCII, Unicode, UTF-8: nicht verwechseln

| Begriff     | Was bedeutet es?                                             | Beispiel                            |
| ----------- | ------------------------------------------------------------ | ----------------------------------- |
| **ASCII**   | 7-Bit, 128 Zeichen umfassender alter Standard                | `A`, `7`, `?`                       |
| **Unicode** | allgemeiner Zeichensatz und Coderaum für sehr viele Sprachen | `á`, `ö`, `Ж`, `中`, `€`            |
| **UTF-8**   | eine verbreitete Speicher-/Kodierungsform von Unicode        | übernimmt ASCII-Zeichen unverändert |

Einfach gesagt:

- **ASCII** = eng begrenzter, alter Grundzeichensatz
- **Unicode** = große, moderne Zeichenwelt
- **UTF-8** = die häufig verwendete praktische Kodierungsform von Unicode

## Was kann ASCII nicht?

ASCII **enthält nicht**:

- ungarische Buchstaben mit Akzenten: `á`, `é`, `í`, `ó`, `ö`, `ő`, `ú`, `ü`, `ű`
- deutsche Sonderzeichen: `ä`, `ö`, `ü`, `ß`
- Zeichen anderer Schriftsysteme
- moderne Symbole, zum Beispiel viele Währungszeichen oder Emojis

Wenn ein System daher nur ASCII erwartet, können solche Zeichen:

- verloren gehen
- fehlerhaft dargestellt werden
- zu Fragezeichen oder seltsamen Zeichen werden

## Prüfungstaugliche Formulierung

> ASCII ist ein 7-Bit-Zeichenkodierungsstandard, der 128 Zeichen umfasst.  
> Darin enthalten sind Steuerzeichen, Buchstaben, Zahlen und Satzzeichen.  
> ASCII unterstützt hauptsächlich die Grundzeichen der englischen Sprache, weshalb es in modernen Systemen allein nicht mehr ausreicht.  
> In der heutigen Praxis verwenden wir eher Unicode-basierte Kodierungen wie UTF-8, die rückwärtskompatibel mit ASCII sind.

## Häufige Prüfungsfehler

- Zu sagen, dass ASCII **8-Bit** ist.
- Zu glauben, dass ASCII deutsche Umlaute oder Akzentbuchstaben kann.
- ASCII mit Unicode oder UTF-8 zu verwechseln.
- Zu behaupten, dass jede heutige Textdatei ASCII ist.
- Kein Beispiel für ein Steuerzeichen nennen zu können.

## Schnelle Selbstkontrolle

1. Wie viele Bits hat ASCII?
2. Wie viele Zeichen kann es kodieren?
3. Was ist der Unterschied zwischen Steuerzeichen und druckbaren Zeichen?
4. Warum reicht ASCII nicht für deutschen Text?
5. Was ist die Verbindung zwischen ASCII und UTF-8?

## Kurzantworten zur Selbstkontrolle

1. **7 Bit**
2. **128 Zeichen**
3. Steuerzeichen steuern Operationen, druckbare Zeichen werden angezeigt
4. Weil Umlaute und Sonderzeichen wie `ä`, `ö`, `ü`, `ß` nicht Teil von ASCII sind
5. Die ersten 128 Zeichen von UTF-8 stimmen mit ASCII überein

## Quellen

Für diese Zusammenfassung wurden aktuelle, offizielle oder allgemein anerkannte technische Quellen verwendet.  
Für die historische Definition von ASCII wird auch die Original-RFC-Referenz angegeben.

1. MDN Web Docs - ASCII  
   https://developer.mozilla.org/en-US/docs/Glossary/ASCII  
   Verwendung: kurze, aktuelle Definition; 7 Bit, 128 Zeichen, moderner Kontext.

2. MDN Web Docs - UTF-8  
   https://developer.mozilla.org/en-US/docs/Glossary/UTF-8  
   Verwendung: Klärung der Beziehung zwischen ASCII und UTF-8.

3. W3C - Choosing & applying a character encoding  
   https://www.w3.org/International/questions/qa-choosing-encodings  
   Verwendung: warum UTF-8 die empfohlene moderne Wahl ist; ASCII als UTF-8-Teilmenge.

4. W3C - Character encodings: Essential concepts  
   https://www.w3.org/International/articles/definitions-characters/index.en  
   Verwendung: Grundbegriffe zu Zeichen, Bytes und Kodierung.

5. Unicode Standard, Chapter 1  
   https://www.unicode.org/versions/latest/core-spec/chapter-1/  
   Verwendung: heutige Rolle von Unicode, Einordnung gegenüber ASCII.

6. IANA Character Sets Registry  
   https://www.iana.org/assignments/character-sets/character-sets.xhtml  
   Verwendung: Bestätigung der standardisierten Internet-Bezeichnung (`US-ASCII`).

7. IETF RFC 20 - ASCII format for Network Interchange  
   https://datatracker.ietf.org/doc/html/rfc20  
   Verwendung: die ursprüngliche, historische Standardbeschreibung von ASCII und der Steuerzeichen.

Abgerufen: `2026-04-08`
