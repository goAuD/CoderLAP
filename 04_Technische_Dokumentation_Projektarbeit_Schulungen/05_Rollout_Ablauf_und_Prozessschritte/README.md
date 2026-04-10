# Roll-out Ablauf und Prozessschritte

## Gyors vizuális kép

| Fázis | Mit jelent? |
|---|---|
| tervezés | célok, érintettek, időzítés |
| előkészítés | környezet, jogosultság, mentések |
| pilot | kisebb körben kipróbálás |
| rollout | tényleges bevezetés |
| ellenőrzés | működés, monitoring, hibák |
| átadás | tudásátadás, dokumentáció |
| elfogadás | megerősítés, hogy a rendszer átvehető |
| rollback | visszaállás, ha a rollout nem sikeres |

## Mi a rollout célja?

Az, hogy az új rendszer vagy változás:

- biztonságosan
- tervezetten
- ellenőrizhetően

kerüljön be a működő környezetbe.

## Tipikus rollout folyamat

## 1. Tervezés

Először meg kell határozni:

- mit vezetünk be
- kiket érint
- mikor történik
- milyen kockázatok vannak
- mi számít sikeres bevezetésnek

## 2. Előkészítés

Ide tartozhat:

- környezet előkészítése
- jogosultságok
- verzióellenőrzés
- tesztelés
- biztonsági követelmények ellenőrzése
- backup készítése

## 3. Pilot vagy fokozatos bevezetés

Sok esetben nem rögtön mindenki kapja meg az új rendszert.

Előny:

- korábban észlelhető a probléma
- kisebb a kockázat

## 4. Tényleges rollout

Ez a tényleges éles bevezetés:

- telepítés
- konfiguráció
- aktiválás
- szolgáltatás átállítása

## 5. Ellenőrzés és monitoring

A rollout után figyelni kell:

- elindult-e minden
- működik-e a szolgáltatás
- vannak-e hibák
- kell-e beavatkozni

## 6. Oktatás és támogatás

Fontos lehet:

- felhasználói tájékoztatás
- oktatás
- rövid útmutató
- helpdesk vagy support felkészítése

## 7. Átadás és elfogadás

Ide tartozik:

- dokumentáció átadása
- felelősségek tisztázása
- ügyfél vagy megrendelő visszajelzése
- formális vagy informális elfogadás

## Fontos rollout elemek a témakatalógus szerint

## 1. Sicherheitsanforderungen

Ellenőrizni kell például:

- jogosultságokat
- hozzáférést
- adatvédelmet
- titkosítást, ha szükséges
- naplózást

## 2. Abbruch und Rückführung / Rollback

Ha a rollout sikertelen:

- legyen terv a visszaállásra
- lehessen korábbi állapotra visszatérni

Ez különösen fontos kritikus rendszereknél.

## 3. Datenmigration / Konvertierung

Ha adatot kell átvinni:

- ellenőrizni kell a formátumot
- migráció után validálni kell az eredményt
- számolni kell adatvesztési kockázattal

## 4. Anwenderschulung

A felhasználókat fel kell készíteni:

- új felületre
- új folyamatokra
- új szabályokra

## 5. Übergabe

Az átadás során világosnak kell lennie:

- ki felel a rendszerért
- hol van a dokumentáció
- hogyan történik a support

## 6. Abnahme

Az elfogadás azt jelenti, hogy a megrendelő vagy felelős fél visszajelzi:

- a rendszer a megállapodás szerint átvehető

## Mire kell figyelni?

- mindig legyen terv
- legyen pilot vagy tesztkör
- legyen rollback lehetőség
- adatmigration előtt legyen mentés
- a kommunikáció és oktatás ne maradjon el

## Vizsgán jól használható megfogalmazás

> A rollout egy új rendszer vagy alkalmazás tervezett bevezetése az éles környezetbe.  
> A folyamat tipikusan tartalmazza a tervezést, az előkészítést, a pilotot, a tényleges bevezetést, az ellenőrzést, az oktatást, az átadást és az elfogadást.  
> Fontos része a biztonsági követelmények figyelembevétele, az adatmigration, valamint a rollback lehetősége arra az esetre, ha a bevezetés nem sikerül.

## Gyakori vizsgahibák

- A rolloutot pusztán telepítésnek tekinteni.
- Nem említeni a rollback lehetőségét.
- Kihagyni a felhasználói oktatást.
- Nem gondolni adatmigrationra.
- Az átadás és elfogadás különbségét nem felismerni.

## Gyors önellenőrzés

1. Mi a rollout célja?
2. Miért fontos a pilot?
3. Mi a rollback szerepe?
4. Miért kritikus az adatmigration ellenőrzése?
5. Miért kell felhasználói oktatás?

## Rövid válaszok az önellenőrzéshez

1. Biztonságos és tervezett bevezetés
2. Mert kisebb körben csökkenti a kockázatot
3. Sikertelen bevezetés esetén visszaállást tesz lehetővé
4. Mert különben adatvesztés vagy hibás adatok keletkezhetnek
5. Mert a felhasználóknak tudniuk kell az új rendszert használni

## Források

1. Planning the Deployment - Microsoft Learn  
   https://learn.microsoft.com/en-us/iis/web-hosting/installing-infrastructure-components/planning-the-deployment  
   Használat: rollout tervezés, checklist, environment, monitoring, training team members.

2. Use Advisor for Teams roll out - Microsoft Learn  
   https://learn.microsoft.com/en-us/microsoftteams/use-advisor-teams-roll-out  
   Használat: rollout lépések, érintettek, előkészítés, fokozatos bevezetés.

3. Cloud Update - Microsoft 365 Apps admin center  
   https://learn.microsoft.com/en-us/microsoft-365-apps/admin-center/cloud-update  
   Használat: rollout hullámok, pilot, illetve visszavonás / rollback lehetőségek.

4. Migration best practices - Microsoft Entra architecture  
   https://learn.microsoft.com/de-de/entra/architecture/migration-best-practices  
   Használat: migráció és fokozatos átállás bevált gyakorlatai.

Megnyitva: `2026-04-08`
