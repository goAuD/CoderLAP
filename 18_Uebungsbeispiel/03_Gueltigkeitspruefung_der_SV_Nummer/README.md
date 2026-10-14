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

- a megengedett szóközök eltávolítása után csak számjegyek legyenek
- a Laufnummer `100–999` közé essen
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

## Lépésenként: a 4422 180599 ellenőrzőszáma

A negyedik számjegy `2`, ezt hasonlítjuk majd a kiszámított maradékhoz.
A többi számjegy súlyozott összege:

```text
4×3 + 4×7 + 2×9 + 1×5 + 8×8 + 0×4 + 5×2 + 9×1 + 9×6
= 200
200 mod 11 = 2
```

A negyedik helyet a következő, önálló Node.js-példa nulla súllyal hagyja ki.
Ez a rész **a formátumot és az ellenőrzőszámot** vizsgálja; a dátumrész ellenőrzése
a teljes mintaprogram külön függvénye.

<!-- example:run -->
```javascript
function hasMatchingCheckDigit(rawValue) {
  const digits = rawValue.replace(/\s/g, "");
  if (!/^[1-9]\d{9}$/.test(digits)) return false;
  const weights = [3, 7, 9, 0, 5, 8, 4, 2, 1, 6];
  const sum = [...digits].reduce((total, digit, index) => {
    return total + Number(digit) * weights[index];
  }, 0);
  const remainder = sum % 11;
  return remainder !== 10 && remainder === Number(digits[3]);
}

console.log(hasMatchingCheckDigit("4422 180599"));
console.log(hasMatchingCheckDigit("2511 010100"));
console.log(hasMatchingCheckDigit("4422x180599"));
```

```text
true
false
false
```

A megengedett szóközt eltávolítjuk, a betűt és egyéb hibás karaktert megőrizzük,
hogy a formátumellenőrzés felismerje. A Laufnummer első számjegye nem nulla.
A maradék `10` esetén nincs megfelelő egyjegyű ellenőrzőszám.

## A dátumrész és a vizsgálat határa

A szokásos `01–12` hónapnál létező naptári napot keresünk.
A hivatalos leírás fiktív hónapokat is megenged (`13, 14, 15, …`), ezért egy általános
születésidő-mező ellenőrzése nem helyettesíti az SV-logikát. A századot a kétjegyű év
nem tartalmazza. A mintaprogram 1900-as és 2000-es évvel is ellenőrzi a naptári lehetőséget,
nem állapítja meg a személy korát.

Még helyes ellenőrzőszám és megengedett dátumrész mellett is csak **formai megfelelésről**
beszélünk. A tényleges kiadást és a biztosítási jogosultságot ez az offline feladat nem ellenőrzi.

Forrás: a lent hivatkozott Dachverband-dokumentum D.61 fejezete, 40–41. oldal;
[Sozialversicherung: a biztosítási szám felépítése](https://www.sozialversicherung.gv.at/cdscontent/?contentid=10007.820902).
Ellenőrizve: `2026-10-14`.

## Vizsgán jól használható megfogalmazás

> Az osztrák `SV-Nr` érvényességvizsgálatánál a szám formátumát és a hivatalos Prüfziffer-logikát kell ellenőrizni.  
> A három első Laufnummer-számjegyet és a `TTMMJJ` részt meghatározott súlyokkal kell szorozni, majd az összeg  
> `11`-gyel vett maradékát össze kell hasonlítani a `4.` pozícióban lévő Prüfzifferrel.  
> Ha az ellenőrzés nem egyezik, a szám érvénytelen.

## Gyors önellenőrzés

1. Melyik pozíció tartalmazza az ellenőrzőszámot?
2. Mi történik 10-es maradéknál?
3. Miért kezeljük külön a dátumrészt?

## Rövid válaszok az önellenőrzéshez

1. A negyedik, JavaScriptben a 3-as index.
2. A számsorhoz nincs használható egyjegyű ellenőrzőszám.
3. Létezhet fiktív hónap, és a kétjegyű évből nem derül ki a század.

## Források

1. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Használat: elsődleges hivatalos forrás a Prüfziffer-logikához.

2. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: a mintaszámok és a feladatelvárás miatt.

Megnyitva: `2026-04-09`
