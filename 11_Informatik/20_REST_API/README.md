# REST API

## Gyors vizuális kép

| Elem | Példa |
|---|---|
| erőforrás | `users`, `orders`, `products` |
| URI | `/api/users/42` |
| művelet | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| válasz | gyakran JSON |

## Mi az a REST?

A REST nem konkrét protokoll, hanem architekturális stílus.

Lényege, hogy a rendszer:

- erőforrásokkal dolgozik
- azokhoz szabványos módon fér hozzá
- a kommunikáció állapotmentes legyen

Ez jól illeszkedik a web természetéhez és a HTTP működéséhez.

## Mi az a REST API?

Olyan API, amely:

- webes erőforrásokat tesz elérhetővé
- URL-ekkel azonosítja őket
- HTTP-módszerekkel hajt végre műveleteket
- a válaszokat szabványos formában adja vissza

Példák:

- `GET /api/products` = termékek lekérése
- `GET /api/products/5` = egy termék lekérése
- `POST /api/products` = új termék létrehozása
- `DELETE /api/products/5` = törlés

## Fontos REST-jellemzők

### 1. Erőforrás-orientáltság

Nem "parancsokat", hanem erőforrásokat modellezünk.

### 2. Stateless működés

Minden kérés önmagában értelmezhető.

### 3. Egységes interfész

A HTTP-módszerek és státuszkódok következetes használata fontos.

### 4. Rétegezhetőség

A kliensnek nem kell feltétlenül tudnia, milyen rétegek vannak közte és a szerver között.

## REST és "sima HTTP API": ne keverd össze

Nem minden HTTP-n működő JSON API lesz automatikusan REST.

Ahhoz, hogy REST-szerű legyen, kell:

- jó erőforrásmodell
- következetes URI-k
- helyes HTTP-szemantika
- stateless szemlélet

## REST és SOAP: ne keverd össze

| Szempont | REST API | SOAP |
|---|---|---|
| jelleg | architekturális stílus | protokoll |
| adatcsere | gyakran JSON | tipikusan XML |
| használat | webközelibb, könnyebb | kötöttebb, formálisabb |

## Mire kell figyelni?

- A `GET` lekérdezést kérjen; járulékos naplózás történhet, de üzleti módosítást ne erre építsünk.
- A HTTP státuszkódokat következetesen használjuk.
- Az endpointnevek legyenek erőforrás-alapúak.
- Az API legyen dokumentált és kiszámítható.

## HTTP-szerződés és tényleges klienskód

Egy lehetséges kurzus-API műveleteit így különítjük el:

| Metódus | Szándék és ismétlés |
|---|---|
| `GET /courses/15` | lekérés; a kliens nem kér üzleti állapotváltozást |
| `POST /courses` | példánkban létrehozás; ismételve több rekord is keletkezhet |
| `PUT /courses/15` | a cél állapotának megadása/cseréje; idempotens |
| `PATCH /courses/15` | részleges módosítás; idempotenciája a művelettől függ |
| `DELETE /courses/15` | eltávolítás; ugyanazon szándék ismétlése idempotens |

Az idempotencia az ismétlés **kért hatásáról** szól, nem azonos válaszszövegről.
Egy második törlés például `404`-et adhat, miközben a kurzus továbbra is hiányzik.
Sikeres létrehozásra gyakori a `201` és `Location`; sikeres, törzs nélküli
válaszra `204`. A `401` hitelesítési problémát, a `403` megtagadott hozzáférést
jelez. Minden erőforráshoz szerveroldali jogosultság-ellenőrzés kell.

**Böngészős példa:** azonos eredeten már működő `/api/courses/15` végpontot
feltételez, amely `200` mellett `{"id":15,"title":"Schleifen"}` JSON-t ad.
Enélkül nem önálló demó. A várt konzolkimenet `Schleifen`:

```javascript
async function loadCourse() {
  const response = await fetch("/api/courses/15", {
    headers: { Accept: "application/json" },
    signal: AbortSignal.timeout(5000),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const course = await response.json();
  if (course === null || typeof course !== "object" ||
      course.id !== 15 || typeof course.title !== "string") {
    throw new Error("Unexpected course data");
  }
  return course.title;
}
loadCourse().then(console.log).catch((error) => console.error(error.message));
```

A `fetch` önmagában a `404` választól nem utasítja el a Promise-t, ezért kell
az `ok` ellenőrzés. A JSON feldolgozása után a várt adatot is ellenőrizzük.
A várakozás legfeljebb öt másodperc, a hibaág kezeli a hálózati, HTTP- és
adatfeldolgozási hibát.

A REST további része a gyorsítótárazhatóság, a kliens/szerver szétválasztás és
az egységes interfész. Ebbe az erőforrás reprezentációja és a következő lépésekre
mutató linkek is beletartoznak. A letölthető kód opcionális REST-korlát.
Az állapotmentesség nem adatbázis nélküli szervert jelent: a kérés értelmezéséhez
nem kell elrejtett korábbi klienskérésre támaszkodni.

## Vizsgán jól használható megfogalmazás

> A REST API olyan webes programozási interfész, amely a REST architekturális elveit követi.  
> Erőforrásokat URI-kkal azonosít, és a műveleteket szabványos HTTP-metódusokkal végzi.  
> Jellemző rá az állapotmentes működés, az egységes interfész és a gyakori JSON-alapú adatcsere.

## Gyors önellenőrzés

1. Mi a REST lényege?
2. Mi a REST API egyik fő jellemzője?
3. Mire használjuk a `GET` és `POST` metódust tipikusan?
4. Miért fontos a stateless működés?
5. Mi a különbség REST és SOAP között?

## Rövid válaszok az önellenőrzéshez

1. Erőforrás-alapú, webközeli architektúra
2. URI-k és HTTP-módszerek használata
3. `GET` lekér, `POST` az erőforrás szerződése szerinti feldolgozást kér, például létrehozást
4. Mert minden kérés önállóan értelmezhető
5. A REST stílus, a SOAP protokoll

## Források

Ellenőrizve: `2026-10-14`.

- [Fielding: REST](https://roy.gbiv.com/pubs/dissertation/rest_arch_style.htm): REST-korlátok és egységes interfész.
- [IETF: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): metódusok, idempotencia és állapotok.
- [MDN: Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch): HTTP-hiba és feldolgozási hiba különbsége.


1. Roy Fielding - Architectural Styles and the Design of Network-based Software Architectures,  
   Chapter 5: Representational State Transfer (REST)  
   https://roy.gbiv.com/pubs/dissertation/rest_arch_style.htm  
   Használat: az eredeti REST architekturális háttér.

2. MDN - REST  
   https://developer.mozilla.org/en-US/docs/Glossary/REST  
   Használat: rövid, fejlesztői összefoglaló a REST fogalmáról.

3. RFC 9110 - HTTP Semantics  
   https://www.rfc-editor.org/rfc/rfc9110  
   Használat: a HTTP-módszerek és szemantika hivatalos szabványi háttere.

Megnyitva: `2026-04-08`
