# Begriff QR-Code

## Schneller visueller Überblick

| Merkmal                     | Was bedeutet es?                                                     |
| --------------------------- | -------------------------------------------------------------------- |
| `2D`-Code                   | speichert Daten nicht nur in einer Zeile, sondern in zwei Richtungen |
| hohe Kapazität              | kann mehr Daten speichern als viele klassische Barcodes              |
| richtungsunabhängiges Lesen | von mehreren Seiten erkennbar                                        |
| Fehlerkorrektur             | teilweise beschädigter Code kann noch lesbar sein                    |

## Was ist ein QR-Code?

QR steht für `Quick Response`.

Es handelt sich um einen zweidimensionalen Code,
der Informationen in einem Quadratraster
aus schwarzen und weißen Modulen speichert.

Typischerweise kann er enthalten:

- Text
- URL
- Kennung
- Kontaktdaten
- Binärdaten

## Worin unterscheidet er sich von einem herkömmlichen Barcode?

| Herkömmlicher Barcode                 | QR-Code                        |
| ------------------------------------- | ------------------------------ |
| typischerweise 1D                     | 2D                             |
| weniger Daten                         | größere Datenmenge             |
| Leserichtung empfindlicher            | aus mehreren Richtungen lesbar |
| hauptsächlich einfache Identifikation | vielfältige Daten speicherbar  |

## Wie sieht er aus?

Die charakteristischsten Elemente des QR-Codes:

- quadratisches Modulmuster
- gut sichtbare Eckmuster
- Datenbereich

Dies ermöglicht dem Scanner zu erkennen:

- die Orientierung
- die Position
- den Inhalt

## Die wichtigsten Vorteile des QR-Codes

### 1. Größere Kapazität

Kann mehr Daten speichern als viele herkömmliche Barcodes.

### 2. Schnelles Lesen

Mobilkamera oder dedizierter Scanner können ihn schnell einlesen.

### 3. Aus mehreren Richtungen lesbar

Muss nicht immer genau in eine Richtung gehalten werden.

### 4. Fehlerkorrektur

Kann auch bei gewissem Grad an Verschmutzung oder Beschädigung noch funktionieren.

## Wofür wird er in der Praxis verwendet?

- Öffnen von Webseiten
- Menüs in Restaurants
- Veranstaltungstickets
- Paketidentifikation
- Produktidentifikation
- Zahlungslösungen
- Teilen von Wi-Fi-Daten
- digitale Visitenkarte

## Statischer und dynamischer QR-Code

### Statischer QR-Code

Der Inhalt des Codes ist direkt im Code enthalten.

Wenn sich der Inhalt ändert:

- wird ein neuer QR-Code benötigt

### Dynamischer QR-Code

Verwendet häufig einen Zwischenverweis oder einen Dienst, sodass das Ziel nachträglich geändert werden kann.

Für die Prüfung reicht es zu wissen:

- statisch = direkter Inhalt
- dynamisch = flexibler, es kann auch nachträglich veränderbare Logik dahinterstehen

## Risiken

Der QR-Code an sich ist nicht bösartig, aber der darin enthaltene Inhalt kann gefährlich sein.

Beispiele:

- bösartiger Link
- Phishing-Seite
- irreführende Zahlungsadresse

Deshalb ist es wichtig:

- QR-Code aus einer vertrauenswürdigen Quelle
- darauf achten, wohin er führt

## Durchgearbeiteter Fall: dauerhafter QR-Code im Klassenraum

Ein gedruckter Code enthält `https://example.org/lernen`. Das Punktmuster speichert diese Zeichenfolge und nicht die gesamte Webseite. Der Inhalt hinter der Adresse kann sich ohne Neudruck ändern. Verweist der Code auf einen Weiterleitungsdienst, lässt sich dort das Ziel ändern; die Daten im gedruckten Code bleiben unverändert. Das wird häufig „dynamischer QR-Code” genannt und bezeichnet keinen eigenen QR-Standard.

Beim Drucktest wird auf ausreichenden Kontrast und einen freien Rand von mindestens vier Modulen an allen Seiten eines gewöhnlichen QR-Codes geachtet. Der Code wird mit mehreren Telefonen aus dem vorgesehenen Abstand gescannt. Fehlerkorrektur hat Grenzen und bestätigt nicht die Identität des Linkbetreibers.

Nach dem Scannen wird die tatsächliche Adresse geprüft, besonders vor Anmeldung oder Zahlung. QR-Daten sind nicht von sich aus verschlüsselt: Ein darin gespeichertes Passwort ist für jeden lesbar, der den Code erhält.

## Prüfungstaugliche Formulierung

> Der QR-Code ist ein zweidimensionaler Barcode,
> der das schnelle und multidirektionale Einlesen
> großer Datenmengen ermöglicht.  
> Seine Vorteile sind die größere Datenspeicherkapazität, das schnelle Einlesen und die Fehlerkorrektur.  
> Er wird häufig für Links, Zahlungen, Tickets und Identifikation verwendet.

## Schnelle Selbstkontrolle

1. Wofür steht die Abkürzung QR?
2. Ist der QR-Code ein 1D- oder 2D-Code?
3. Was ist einer der Hauptvorteile gegenüber dem herkömmlichen Barcode?
4. Welche Gefahr kann bei der Nutzung eines QR-Codes bestehen?
5. Nenne drei praktische Anwendungsbeispiele.

## Kurzantworten zur Selbstkontrolle

1. Quick Response
2. 2D-Code
3. Speichert mehr Daten und ist schneller und flexibler lesbar
4. Bösartiger Link oder Phishing
5. Zahlung, Webseite, Ticket, Identifikation

## Quellen

1. QRcode.com - What is a QR Code?  
   https://www.qrcode.com/en/about/  
   Verwendung: Grundbegriff des QR-Codes, wichtigste Eigenschaften und standardisierte Merkmale.

2. QRcode.com - Types of QR Code  
   https://www.qrcode.com/en/codes/  
   Verwendung: QR-Code-Typen, Kapazität, Modulgröße und weiterentwickelte Varianten.

3. ISO/IEC 18004 overview on QRcode.com  
   https://www.qrcode.com/en/about/standards.html  
   Verwendung: Hintergrundinformationen zur Standardisierung des QR-Codes.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [DENSO WAVE: Code area](https://www.qrcode.com/en/howto/code.html): vier Module breite Ruhezone des gewöhnlichen QR-Codes.

Geprüft: `2026-10-14`.
