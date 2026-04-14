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

Ahhoz REST-szerű legyen, kell:

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

- A `GET` legyen lekérdezés, ne végezzen rejtett módosítást.
- A HTTP státuszkódokat következetesen használjuk.
- Az endpointnevek legyenek erőforrás-alapúak.
- Az API legyen dokumentált és kiszámítható.

## Vizsgán jól használható megfogalmazás

> A REST API olyan webes programozási interfész, amely a REST architekturális elveit követi.  
> Erőforrásokat URI-kkal azonosít, és a műveleteket szabványos HTTP-metódusokkal végzi.  
> Jellemző rá az állapotmentes működés, az egységes interfész és a gyakori JSON-alapú adatcsere.

## Gyakori vizsgahibák

- A REST-et protokollnak nevezni.
- Azt mondani, hogy minden JSON API REST.
- Nem megemlíteni a stateless működést.
- Az HTTP-módszerek szerepét kihagyni.

## Gyors önellenőrzés

1. Mi a REST lényege?
2. Mi a REST API egyik fő jellemzője?
3. Mire használjuk a `GET` és `POST` metódust tipikusan?
4. Miért fontos a stateless működés?
5. Mi a különbség REST és SOAP között?

## Rövid válaszok az önellenőrzéshez

1. Erőforrás-alapú, webközeli architektúra
2. URI-k és HTTP-módszerek használata
3. `GET` lekér, `POST` létrehoz
4. Mert minden kérés önállóan értelmezhető
5. A REST stílus, a SOAP protokoll

## Források

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
