# Gueltigkeitspruefung der SV-Nummer

## Gyors vizuális kép

```text
L L L P T T M M J J

L L L   = Laufnummer
P       = Prüfziffer
T T M M J J = Geburtsdatum oder fingiertes Datum
```

## Hivatalos Prüfziffer-logika

A hivatalos osztrák leírás alapján:

- a három Laufnummer-számjegy súlyai: `3`, `7`, `9`
- a `TTMMJJ` rész súlyai: `5`, `8`, `4`, `2`, `1`, `6`
- az összeg `mod 11` maradéka adja a Prüfziffert
- ha a maradék `10`, az a szám ebben a formában nem használható

## Mit érdemes a megoldásban ellenőrizni?

- csak számjegyek legyenek
- `10` számjegy legyen
- Prüfziffer stimmeljen
- a dátumrész legalább formailag életszerű legyen

## Példák a PDF-ből

### Érvényes

- `4422 180599`
- `3567 010705`
- `5884 050902`

### Érvénytelen

- `2511 010100`
- `5255 121299`
- `4999 070700`

## Vizsgán jól használható megfogalmazás

> Az osztrák `SV-Nr` érvényességvizsgálatánál a szám formátumát és a hivatalos Prüfziffer-logikát kell ellenőrizni.  
> A három első Laufnummer-számjegyet és a `TTMMJJ` részt meghatározott súlyokkal kell szorozni, majd az összeg  
> `11`-gyel vett maradékát össze kell hasonlítani a `4.` pozícióban lévő Prüfzifferrel.  
> Ha az ellenőrzés nem egyezik, a szám érvénytelen.

## Gyakori vizsgahibák

- Rossz számjegypozíciókat használni a szorzáshoz.
- A Prüfziffert a rossz helyről kiolvasni.
- Nem levenni a szóközöket feldolgozás előtt.
- Nem tesztelni a PDF-ben adott mintaszámokkal.

## Források

1. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Használat: elsődleges hivatalos forrás a Prüfziffer-logikához.

2. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Használat: a mintaszámok és a feladatelvárás miatt.

Megnyitva: `2026-04-09`
