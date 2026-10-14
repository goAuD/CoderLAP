# Zeichensatz ASCII

## Gyors vizuális kép

| Tartomány | Típus                | Példa                   | Mire való                         |
| --------- | -------------------- | ----------------------- | --------------------------------- |
| `0-31`    | vezérlőkarakter      | `LF`, `CR`, `TAB`       | nem látható jelek, hanem vezérlés |
| `32`      | szóköz               | `SPACE`                 | elválasztás                       |
| `33-126`  | nyomtatható karakter | `A`, `a`, `7`, `?`, `#` | szöveg megjelenítése              |
| `127`     | vezérlőkarakter      | `DEL`                   | törléshez kapcsolódó jel          |

## Mi az ASCII?

Az ASCII neve: **American Standard Code for Information Interchange**.  
Lényege, hogy a karakterekhez egy-egy **számkódot** rendel.

Például:

| Karakter | Decimális | Hexadecimális | 7 bites bináris |
| -------- | --------: | ------------: | --------------: |
| `A`      |      `65` |          `41` |       `1000001` |
| `a`      |      `97` |          `61` |       `1100001` |
| `0`      |      `48` |          `30` |       `0110000` |
| `?`      |      `63` |          `3F` |       `0111111` |

Fontos:

- Az ASCII **7 bites**, nem 8 bites.
- A gyakorlatban ugyan gyakran **1 byte** helyen tárolják, de az ASCII eredeti tartománya csak `0-127`.
- Az internetes és szabványos név gyakran **`US-ASCII`**.

## Mit tartalmaz?

### 1. Vezérlőkarakterek

Ezek nem látható betűk vagy számok, hanem valamilyen műveletet, vezérlést jelölnek.

Gyakori példák:

- `TAB` - tabulátor
- `LF` - soremelés
- `CR` - kocsivissza
- `ESC` - escape
- `DEL` - törlés

Ezek főleg régi adatátvitelben, nyomtatásban, termináloknál, illetve ma is fájlformátumokban és protokollokban fontosak.

### 2. Nyomtatható karakterek

Ide tartoznak:

- nagybetűk: `A-Z`
- kisbetűk: `a-z`
- számjegyek: `0-9`
- gyakori írásjelek és jelek: `.` `,` `:` `;` `!` `?` `@` `#` `$` `%` `&`

## Miért fontos még ma is?

Az ASCII önmagában már nem elég a modern, többnyelvű rendszerekhez, de továbbra is alapvető, mert:

- sok technikai szabvány történetileg erre épült
- sok fájlformátum és protokoll ASCII-barát
- az `U+0000–U+007F` Unicode-kódpontokat az **UTF-8** az ASCII-val azonos, egybyte-os kóddal tárolja
- programozásban, hálózatokban, logokban, HTTP-fejlécekben, konfigurációkban ma is gyakran előjön

## ASCII, Unicode, UTF-8: ne keverd össze

| Fogalom     | Mit jelent?                                             | Példa                                            |
| ----------- | ------------------------------------------------------- | ------------------------------------------------ |
| **ASCII**   | 7 bites, 128 karakteres régi szabvány                   | `A`, `7`, `?`                                    |
| **Unicode** | általános karakterkészlet és kódtér nagyon sok nyelvhez | `á`, `ö`, `Ж`, `中`, `€`                         |
| **UTF-8**   | a Unicode egyik elterjedt tárolási/kódolási formája     | az ASCII karaktereket változatlanul viszi tovább |

Egyszerűen:

- **ASCII** = szűk, régi alapkészlet
- **Unicode** = nagy, modern karaktervilág
- **UTF-8** = a Unicode gyakori gyakorlati kódolási formája

## Mit nem tud az ASCII?

Az ASCII **nem tartalmazza**:

- magyar ékezetes betűk: `á`, `é`, `í`, `ó`, `ö`, `ő`, `ú`, `ü`, `ű`
- német különleges karakterek: `ä`, `ö`, `ü`, `ß`
- egyéb írásrendszerek karakterei
- modern szimbólumok, például sok pénznemjel vagy emoji

Ezért ha egy rendszer csak ASCII-t vár, akkor az ilyen karakterek:

- elveszhetnek
- hibásan jelenhetnek meg
- kérdőjellé vagy furcsa karakterré válhatnak

## Kidolgozott példa: karakterből byte

Egy űrlap `Aő` szövegét UTF-8 kódolással mentjük. Az `A` az ASCII-tartományba tartozik,
az `ő` Unicode-kódpontja `U+0151`, ezért az utóbbihoz több byte kell.
A következő önálló JavaScript böngésző konzoljában vagy modern Node.js-ben futtatható.

<!-- example:run -->
```javascript
const text = "Aő";
const bytes = new TextEncoder().encode(text);
console.log([...bytes].join(" "));
console.log(bytes.length);
console.log([...text].length);
```

Várt kimenet:

```text
65 197 145
3
2
```

Két kódpontot három byte tárol: az `A` kódja `65`, az `ő` UTF-8 byte-jai `197, 145`.
A kódpont egy karakter azonosítója, a kódolás pedig azt adja meg, milyen byte-sorozattá alakítjuk.
Ugyanazzal a kódolással kell visszaolvasni az adatot, amellyel kiírtuk.

A JavaScript `text.length` UTF-16 kódegységeket számol. Ebben a példában ez is `2`,
de egy emoji több kódegységet használhat. A `[...text].length` kódpontokat számol;
egy látható betűt pedig több kódpont, például betű és külön ékezet is alkothat.
Fájlmérethez a kódolt byte-ok száma kell, nem a látható betűké.

**Alkalmazás:** 100 darab ASCII `A` UTF-8-ban 100 byte, 100 darab előre összeállított
`ő` 200 byte. Ez megmagyarázza, miért lehet két azonos hosszúságúnak látszó mező
eltérő méretű a hálózaton.

Forrás a példához: [MDN: TextEncoder.encode](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/encode)
és [W3C: karakterek és kódolás](https://www.w3.org/International/articles/definitions-characters/index.en).

## Vizsgán jól használható megfogalmazás

> Az ASCII egy 7 bites karakterkódolási szabvány, amely 128 karaktert tartalmaz.  
> Ebben vannak vezérlőkarakterek, betűk, számok és írásjelek.  
> Az ASCII főleg az angol nyelv alapkaraktereit támogatja, ezért a modern rendszerekben önmagában már nem elég.  
> A mai gyakorlatban inkább Unicode-alapú kódolást, például UTF-8-at használunk, amely visszafelé kompatibilis az ASCII-val.

## Gyors önellenőrzés

1. Hány bites az ASCII?
2. Hány karaktert tud kódolni?
3. Mi a különbség a vezérlőkarakter és a nyomtatható karakter között?
4. Miért nem elég az ASCII magyar szöveghez?
5. Mi a kapcsolat az ASCII és a UTF-8 között?

## Rövid válaszok az önellenőrzéshez

1. **7 bites**
2. **128 karakter**
3. A vezérlőkarakter műveletet vezérel, a nyomtatható karakter megjelenik
4. Mert az ékezetes magyar betűk nem részei az ASCII-nak
5. Az ASCII 128 karakterét az UTF-8 ugyanazokkal az egybyte-os kódokkal tárolja

## Források

Az összefoglalóhoz friss, hivatalos vagy széles körben elfogadott technikai forrásokat használtam.  
Az ASCII történeti definíciójához az eredeti RFC-hivatkozást is megadom.

1. MDN Web Docs - ASCII  
   https://developer.mozilla.org/en-US/docs/Glossary/ASCII  
   Használat: rövid, mai definíció; 7 bit, 128 karakter, modern kontextus.

2. MDN Web Docs - UTF-8  
   https://developer.mozilla.org/en-US/docs/Glossary/UTF-8  
   Használat: ASCII és UTF-8 kapcsolatának tisztázása.

3. W3C - Choosing & applying a character encoding  
   https://www.w3.org/International/questions/qa-choosing-encodings  
   Használat: miért UTF-8 az ajánlott modern választás; ASCII mint UTF-8-részhalmaz.

4. W3C - Character encodings: Essential concepts  
   https://www.w3.org/International/articles/definitions-characters/index.en  
   Használat: karakter, bájt, kódolás alapfogalmai.

5. Unicode Standard, Chapter 1  
   https://www.unicode.org/versions/latest/core-spec/chapter-1/  
   Használat: Unicode mai szerepe, ASCII-hoz viszonyított helye.

6. IANA Character Sets Registry  
   https://www.iana.org/assignments/character-sets/character-sets.xhtml  
   Használat: a szabványos internetes elnevezés (`US-ASCII`) megerősítése.

7. IETF RFC 20 - ASCII format for Network Interchange  
   https://datatracker.ietf.org/doc/html/rfc20  
   Használat: az ASCII eredeti, történeti szabványos leírása és a vezérlőkarakterek.

Megnyitva: `2026-04-08`
