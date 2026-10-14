# Sperrtabelle und Sperrverhalten

## Gyors vizuális kép

| Jelenség | Mit jelent? |
|---|---|
| lock / zárolás | más műveletek korlátozása ideiglenesen |
| várakozás | egyik tranzakció a másikra vár |
| deadlock | két tranzakció egymásra vár és megakad |

## Mi az a zárolás?

Ha több felhasználó vagy folyamat egyszerre dolgozik ugyanazzal az adattal, a `DBMS` gyakran zárolással védi a konzisztenciát.

Ez történhet például:

- sor szinten
- tábla szinten
- különféle lock-típusokkal

## Mi az a “Sperrtabelle”?

Vizsgás értelemben ez általában azt jelenti, hogy:

- a rendszer nyilvántartja, milyen zárolások vannak érvényben
- melyik tranzakció mit zárol

Nem feltétlenül egy felhasználó által kezelt “normál tábla”, hanem a zárolási állapot logikai vagy belső reprezentációja.

## Miért fontos a zárolási viselkedés?

- megakadályozza, hogy két művelet egyszerre ellentmondó módon írjon
- segít megőrizni a konzisztenciát
- befolyásolja a teljesítményt és a párhuzamosságot

## Lehetséges problémák

### Várakozás

Az egyik tranzakció vár, amíg a másik elengedi a lockot.

### Deadlock

Két tranzakció egymásra vár, és egyik sem tud továbbmenni.

### Túl erős zárolás

Rontja a párhuzamos teljesítményt.

## Zárolás és tranzakció: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| tranzakció | logikailag összetartozó műveletek egysége |
| zárolás | technikai mechanizmus az ütközések elkerülésére |

## Kidolgozott eset: az utolsó készlet lefoglalása

Egy termékből egy darab maradt. A és B kapcsolat egyszerre szeretné lefoglalni. **MySQL/InnoDB-ben** az A kapcsolat explicit tranzakcióban `SELECT ... FOR UPDATE` utasítással olvassa a termék sorát, majd módosítja. B ugyanennek a sornak a zároló olvasásánál vár, amíg A commitol vagy visszagörget. Ezután B a friss állapot alapján dönthet.

A szokásos, konzisztens `SELECT` MVCC-t, vagyis több verzión alapuló olvasást használhat, ezért nem minden olvasás vár az íróra. A `FOR UPDATE` más viselkedés. A lock a tranzakció lezárásáig él; ne várakozz közben felhasználói kattintásra vagy lassú külső szolgáltatásra.

| Helyzet | Jelentés |
|---|---|
| B vár A zárolására | normál ütközéskezelés lehet |
| A az 1-es sort, B a 2-es sort tartja, majd egymás sorát kérik | deadlock, körkörös várakozás |
| minden tranzakció ugyanabban a sorrendben kéri a sorokat | kisebb deadlock-kockázat |

Az InnoDB felismerhet egy holtpontot és visszavonhatja az egyik tranzakciót. Az alkalmazásnak az egész érintett tranzakció ellenőrzött újrapróbálására kell felkészülnie. A timeout nem feltétlenül ugyanúgy vonja vissza az egész tranzakciót, ezért a hibakezelésben explicit rollback is szükséges lehet.

A kizárólagos és megosztott zárak kompatibilitása, az indexek és az izolációs szint együtt határozzák meg a pontos viselkedést. A zárolási nyilvántartás például a MySQL `performance_schema.data_locks` és `data_lock_waits` tábláiból vizsgálható megfelelő jogosultsággal.

## Vizsgán jól használható megfogalmazás

> A zárolás célja, hogy több felhasználó egyidejű adatkezelése mellett is megmaradjon az adatkonzisztencia.  
> A `DBMS` különböző lock-mechanizmusokat alkalmazhat, és ezek viselkedése befolyásolja a várakozást, a  
> párhuzamosságot és a teljesítményt.  
> A helytelen vagy túl erős zárolás problémákhoz vezethet, például várakozáshoz vagy deadlockhoz.

## Gyors önellenőrzés

1. Miért van szükség zárolásra?
2. Mit jelent a zárolási viselkedés?
3. Mi a deadlock?
4. Mi a kapcsolat a tranzakció és lock között?
5. Miért okozhat teljesítménygondot a túl sok lock?

## Rövid válaszok az önellenőrzéshez

1. Az adatkonzisztencia védelmére
2. A lockok gyakorlati működését
3. Egymásra váró tranzakciók holtpontja
4. A tranzakció használhat lockokat a védelemhez
5. Mert csökkenti a párhuzamos hozzáférést

## Források

1. PostgreSQL - Explicit Locking  
   https://www.postgresql.org/docs/current/explicit-locking.html  
   Használat: hivatalos forrás a lockok típusaihoz és viselkedéséhez.

2. PostgreSQL - Transaction Isolation  
   https://www.postgresql.org/docs/current/transaction-iso.html  
   Használat: kiegészítő háttér a párhuzamos hozzáférés és konzisztencia kapcsolatának megértéséhez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [MySQL: Locking Reads](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html): FOR UPDATE és várakozás
- [MySQL: Deadlocks](https://dev.mysql.com/doc/refman/8.0/en/innodb-deadlocks-handling.html): deadlock kezelése és tranzakció újrapróbálása
- [MySQL: InnoDB error handling](https://dev.mysql.com/doc/refman/8.0/en/innodb-error-handling.html): timeout és teljes tranzakció visszavonásának különbsége

Ellenőrizve: `2026-10-14`.
