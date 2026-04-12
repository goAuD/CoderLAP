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
- az **UTF-8** első `128` karaktere pontosan megegyezik az ASCII-val
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

## Vizsgán jól használható megfogalmazás

> Az ASCII egy 7 bites karakterkódolási szabvány, amely 128 karaktert tartalmaz.  
> Ebben vannak vezérlőkarakterek, betűk, számok és írásjelek.  
> Az ASCII főleg az angol nyelv alapkaraktereit támogatja, ezért a modern rendszerekben önmagában már nem elég.  
> A mai gyakorlatban inkább Unicode-alapú kódolást, például UTF-8-at használunk, amely visszafelé kompatibilis az ASCII-val.

## Gyakori vizsgahibák

- Azt mondani, hogy az ASCII **8 bites**.
- Azt hinni, hogy az ASCII tud magyar ékezeteket.
- Összekeverni az ASCII-t a Unicode-dal vagy az UTF-8-cal.
- Azt állítani, hogy minden mai szövegfájl ASCII.
- Nem tudni példát mondani vezérlőkarakterre.

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
5. A UTF-8 első 128 karaktere megegyezik az ASCII-val

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
