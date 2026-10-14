# Erste drei Normalformen

## A normalizálás célja

A normalizálás a táblák felosztása az adatok közti függések alapján. Célja a felesleges ismétlődés és a beszúrási, módosítási, törlési anomáliák csökkentése. A függés üzleti szabály, nem két véletlenül azonos mintaértékből levont következtetés.

A `X -> Y` jelölés azt mondja: ugyanahhoz az X értékhez mindig ugyanaz az Y tartozik. Egy **kulcsjelölt** minimális olyan oszlophalmaz, amely egyértelműen azonosítja a sort. Ezek közül választjuk az elsődleges kulcsot. A normalizálásnál a többi kulcsjelöltet is figyelembe vesszük.

## 1NF: egy érték a választott tartományból

Nincsenek ismétlődő oszlopcsoportok, például `product1`, `product2`, `product3`, és egy terméklista sem kerül vesszőkkel összefűzve egy cellába. Egy rendelési tétel egy sor. Az „atomi” az adatmodell használatától függ: egy dátum maradhat egyetlen DATE érték attól, hogy évre és hónapra bontható.

## 2NF: teljes függés minden kulcsjelölttől

Az 1NF mellett minden olyan attribútum, amely egyetlen kulcsjelöltnek sem része, teljesen függ minden kulcsjelölttől, nem csak annak egy részétől. Ez összetett kulcsnál jelent külön ellenőrzést. Ha minden kulcsjelölt egyetlen oszlopból áll, nincs ilyen részleges függés.

## 3NF: a tranzitív függések kezelése

Az egyszerű, egyértelmű kulcsú esetekben a nem kulcsadat ne egy másik nem kulcsadaton keresztül függjön a kulcstól. Például `customer_id -> customer_name`, ezért az ügyfél nevét nem minden rendelésben, hanem az ügyfélnél tároljuk.

Pontosabb szabály: minden nem triviális `X -> A` függésnél X szuperkulcs, vagy A valamely kulcsjelölt része. A szuperkulcs egyedileg azonosít, de a minimális kulcsjelölttel ellentétben tartalmazhat felesleges oszlopot is. Ez a megfogalmazás a több kulcsjelöltes eseteket is lefedi.

## Kidolgozott felbontás: rendelési tételek

Induljunk ebből: `order_id, product_id, order_date, customer_id, customer_name, product_name, quantity`. A példa szabálya szerint egy termék rendelésenként egyszer szerepel; a kulcsjelölt `(order_id, product_id)`.

1. **1NF:** minden termék saját sorban van. A mennyiség egyetlen szám.
2. **2NF:** a rendelés dátuma és ügyfele csak `order_id`-től, a termék neve csak `product_id`-től függ. Külön `orders` és `products` táblába kerülnek. Az `order_items(order_id, product_id, quantity)` a teljes párhoz tartozó mennyiséget őrzi.
3. **3NF:** az `orders` táblában `order_id -> customer_id -> customer_name` lánc lenne. A nevet átvisszük a `customers(customer_id, customer_name)` táblába; a rendelésben az ügyfél idegen kulcsa marad.

Az összesítés így négy tábla: `customers`, `orders`, `products`, `order_items`. Kulcsokkal és kapcsolásokkal ugyanaz a rendelés összeállítható, miközben egy aktuális ügyfélnév csak egy helyen változik. A rendeléskori ár vagy szállítási cím külön történeti adat lehet; a jelentését előbb tisztázni kell, nem automatikusan eltávolítani.

## Vizsgán jól használható megfogalmazás

> Az 1NF megszünteti az ismétlődő csoportokat. A 2NF a kulcsjelöltek részeitől való függést vizsgálja. A 3NF a nem megfelelő tranzitív függéseket is megszünteti. A cél olyan felosztás, amelyben ugyanazt az üzleti tényt következetesen kezeljük, és a szükséges adatok kapcsolással visszanyerhetők.

## Gyors önellenőrzés

1. Miért külön sor a rendelés két terméke?
2. Mit jelent a részleges függés?
3. Miért kerülhet külön táblába az ügyfél neve?
4. Megoldja-e önmagában egy új `id` oszlop az összes normalizálási problémát?
5. Honnan tudjuk a funkcionális függéseket?

## Rövid válaszok az önellenőrzéshez

1. Így nincs egy mezőbe csomagolt ismétlődő terméklista.
2. Egy nem kulcsattribútum az összetett kulcsjelöltnek csak egy részétől függ.
3. Az ügyfélazonosító határozza meg, nem a rendelés saját ténye.
4. Nem. Az üzleti kulcsok és függések ettől megmaradnak.
5. A követelményekből és üzleti szabályokból, megfelelő ellenőrzéssel.

## Források

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Használat: hivatalos, jól érthető magyarázat az első három normálformához.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Használat: hivatalos háttér a normalizálás céljához és a `1NF`, `2NF`, `3NF` gyakorlati értelmezéséhez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [Microsoft: Database normalization](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/microsoft-365/microsoft-365-apps/access/database-normalization-description): normalizálás és táblafelbontás alapelvei
- [Microsoft: Database design basics](https://support.microsoft.com/en-us/access/database-design-basics): függések, kulcsok és kapcsolatok tervezése

Ellenőrizve: `2026-10-14`.
