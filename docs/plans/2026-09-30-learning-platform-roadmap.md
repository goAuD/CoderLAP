# Coder tanulóműhely — következő lépések

Frissítve: **2026-09-30**. Ez a három projekt közös sorrendjének egyetlen
karbantartott listája; a részletes megvalósítási jegyzetek a saját repójukban
maradnak. Egy feladat = külön ág és ellenőrizhető PR. Ez tervezési állapot,
nem új funkciók vagy infrastruktúra elkészültének igazolása.

## Ellenőrzött kiinduló állapot

- [x] A három dokumentációs PR összevonva: LAP #36, Quiz #13, Coaster #4.
- [x] LAP: `main` = `6d6343b`, `dev` = `aa366ba`. A két ág fájltartalmának
  különbsége csak `docs/project/next-thread-handoff.md` 22 sora; a webes kód
  azonos. A korábbi keretdeployból nem maradt ki felületi javítás.
- [x] Quiz: `dev` = `ed0c41c`. A 35 + 35 + 30 programozási kérdés jóváhagyott,
  külön előnézeti bankokban érhető el; a gyökéroldal még a régi DSGVO-bankot tölti.
- [x] Coaster: `main` = `b3863bc`. A két kezdőjegyzet nem része az ágak
  történetének; helyben ignorált fájlok. A karbantartott átadás a README.
- [x] SkillDisplay: a bejelentkezett felület és a SkillSet-katalógus olvasva.
  Nem történt önértékelés, igazoláskérés, fiókmódosítás vagy üzenetküldés.
- [x] Szerver: olvasási SSH-ellenőrzés alapján Debian, működő Caddy és MariaDB;
  16 GB RAM és két közel 500 GB-os SSD, az új lemez `/srv/data` alatt csatolva.
  A LAP Caddy-konfigurációjában Basic Auth és hozzáférési naplózás szerepel;
  Quiz-, Coaster- és auth-hostnév, illetve `forward_auth` még nem szerepel benne.
  Ez kapacitás- és konfigurációs pillanatkép, nem teljes biztonsági audit.
- [ ] A Quiz/Coaster élő DNS-, szerver-, TLS- és belépési beállításait még
  ellenőrizni kell; a nyitott Cloudflare-lap önmagában nem bizonyít telepítést.

Az ágazonosítók dátumhoz kötött pillanatképek. Kiadás előtt friss fetch és diff
kell. A most hiányzó LAP-dokumentációt a következő `dev` → `main` kiadási PR
viheti át; pusztán emiatt nincs sürgős weboldal-deploy.

## Végrehajtási sorrend

| Sorrend | Feladat | Repo | Késznek tekintjük, ha… |
| --- | --- | --- | --- |
| 0 | Közös belépés és adatkezelés megtervezése | közös infrastruktúra + LAP | Üzemeltető, felhasználói kör, választott belépés, adatfolyam, megőrzés és visszaállítás tisztázott; még nincs éles fiókmigráció. |
| 1 | Publikálható Quiz-kezdőlap és statikus csomag | Quiz | A LAP-programozási kérdések normál indítással elérhetők, külön Python-előnézeti trükk nélkül; a régi mentések nem keverednek az új bankkal. |
| 2 | Védett Quiz/Coaster élesítés és keresztlinkek | mindhárom | DNS, TLS, szerverútvonal, belépés, visszaállítás és mobilos elérés ellenőrzött; csak ezután élnek a LAP eszközlinkjei. |
| 3 | Főoldali haladásjelölés és állapotszűrő | LAP | Egy téma a kártyán jelölhető és visszaállítható; a számlálók és a témaoldal azonos mentést használnak. |
| 4 | Keresés rangsorolása és szókezdetek | LAP | A fontos címtalálatok előre kerülnek, a gépelés közbeni keresés és a meglévő DE/HU aliasok együtt működnek. |
| 5 | Következő tananyagrész és vegyes gyakorlás | Quiz | A következő főtéma kis, forrásolt DE/HU adagokban ellenőrzött; a témák csoportosítása pontosan tisztázott. |
| 6 | Öt tanulási célból álló SkillDisplay-próba | LAP + tanári egyeztetés | Aktív készségazonosítók, tanulási célok és igazolási szerepek tisztázottak; első körben csak hivatkozások készülnek. |

A 0. feladatot az élesítés előtt lezárjuk; az 1. feladat közben is végezhető.
Ha az infra döntésre vár, a 3. feladat külön ágon haladhat. A tanári kérdések
összegyűjtése közben is végezhető; a SkillDisplay-integráció nem feltétele a helyi tanulásnak.

### 0. Közös belépés és későbbi szerveres mentés

**Javaslat, még nem elfogadott architektúra:** először egy közös belépési kapu
a három alkalmazás elé, később külön kis API a felhasználó által kért
haladásszinkronhoz. A Markdown-tananyag és a három önálló repo megmaradhat;
a fiókkezelés nem igényli a tananyag adatbázisba költöztetését.

| Lehetőség | Előny | Mérlegelendő |
| --- | --- | --- |
| Saját Authelia a Caddy mellett | Saját üzemeltetésű közös belépés; dokumentált Caddy-integráció és MariaDB/SQLite-tárolás. | Frissítés, fiókkezelés, helyreállítás, értesítés és mentés üzemeltetése ránk marad. |
| Cloudflare Access | Több domain közös belépése saját auth-szerver nélkül. | Az ellenőrzött Free csomag 50 felhasználós; külső azonosítás és naplózás adatfolyamát, feltételeit is értékelni kell. |

A saját üzemeltetés iránti igényhez első próbaként az Authelia illeszkedik.
A 20–30 tanuló egyetlen iskola jelenlegi becslése, nem a platform felső
határa; ezért a Cloudflare 50 fős Free kerete nem hosszú távú méretezési alap.
Tárolóként a már futó MariaDB külön adatbázissal és saját, korlátozott
jogosultságú felhasználóval használható; a meglévő adatbázisokhoz nem nyúlunk.
Az Authelia belépési fiókforrása és működési adatbázisa külön fogalom:
kis zárt körben fájlalapú fióklista is lehetséges, a MariaDB önmagában nem
ad regisztrációs felületet. Az értesítési és fiók-helyreállítási mód a próba része.
Saját szerveren a PostgreSQL/MariaDB nem szolgáltatói Free-csomagként fut;
az inaktivitás miatti szüneteltetés nem az SQL-adatbázis általános tulajdonsága.

- [x] Viktor visszajelzése: jelenleg saját, önkéntesen használható kiegészítő
  tanulóprojekt felnőttképzéshez, kiskorúak nélkül. Évente körülbelül 20–30
  tanuló és néhány tanár várható egy iskolából; nem kötelező feladatok vagy
  osztályozás rendszere. További iskolák bevonása előtt a fiókkezelési folyamatot
  és az adatkezelői szerepeket is felülvizsgáljuk.
- [ ] Az iskola/tanárok későbbi üzemeltetői átvétele még csak lehetőség.
  Átadás előtt külön tisztázzuk a felelősséget, hozzáféréseket és adattovábbítást.
  A fiókok életciklusát is tervezzük meg: az évente új csoport nem jelenti,
  hogy a korábbi csoportok fiókjai vagy adatai automatikusan megszűnnek.
- [ ] Két tesztfiókkal ellenőrizzük az egyszeri belépést, mindhárom céloldalt,
  kijelentkezést, lejáratot, visszavont hozzáférést és iPhone-os működést.
  A kapu kihagyásával az origin vagy az API ne legyen elérhető; a szolgáltatás
  kiesése se tegye nyilvánossá a védett tartalmat. Legyen kipróbált visszaállítás.
- [ ] Első körben csak meghívott fiókokat javaslunk; a tanulási haladás
  továbbra is helyi. A belépés nem indít automatikus eredményfeltöltést.
- [ ] Későbbi API esetén a felhasználói azonosságot a szerver hitelesítse;
  ne a böngésző által küldött azonosítót fogadja el. A tanulási adatok külön
  adatbázisba kerüljenek, felhasználónként ellenőrzött hozzáféréssel.
- [ ] Az adatfolyamterv sorolja fel a fiókadatokat, szükséges belépési sütiket,
  biztonsági naplókat, későbbi haladásadatokat, címzetteket és szolgáltatókat.
  Minden célhoz jogalap, tényleges megőrzési idő, törlési mód és felelős kell.
  Becenév/felhasználóazonosító sem jelent automatikusan anonim adatot.
- [ ] Belépésváltás előtt a jelenlegi adatvédelmi tájékoztató, impresszum és
  üzemeltetési dokumentáció érintett részeit igazítsuk a tényleges rendszerhez.
  A rövid szükséges munkamenetsüti önmagában nem jelent kötelező sütibannert;
  az összes tényleges süti és böngészőtárolás célját külön ellenőrizzük.
- [ ] A tanári átnézés mellett kérdezzünk rá az intézmény adatvédelmi
  kapcsolattartójára. Ez a terv nem jogi megfelelőségi igazolás; a régi
  „privát rollout” minősítés sem igazolja automatikusan az új fiókrendszert.
- [ ] Szerveres személyes adatok előtt legyen korlátozott hozzáférésű,
  titkosított, gépen kívüli mentés és visszaállítási próba. A második belső SSD
  önmagában nem véd a teljes gép elvesztése ellen. A meglévő mentést még nem auditáltuk.

Ellenőrzött források, 2026-09-30:

- [Authelia + Caddy](https://www.authelia.com/integration/proxies/caddy/),
  [MariaDB-tárolás](https://www.authelia.com/configuration/storage/mysql/),
  [fájlalapú fiókok](https://www.authelia.com/configuration/first-factor/file/).
- [Cloudflare többdomaines belépés](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/)
  és [aktuális csomagok](https://www.cloudflare.com/plans/zero-trust-services/).
- [EU Bizottság: adatkezelői kötelezettségek és tájékoztatás](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en).
- [Osztrák DSB: adatvédelem és sütik](https://dsb.gv.at/faqs/datenschutz-cookies).

### 1–2. Publikálás

- [ ] Ajánlott Quiz-belépési pont: a három jóváhagyott programozási rész
  egyértelmű elérése közös kezdőlapról. A végleges navigációt kis előnézetben
  ellenőrizzük. A régi DSGVO-bankot és a meglévő böngészős mentéseket őrizzük meg.
- [ ] Ellenőrizzük, mi kerül a webgyökérbe: csak szükséges statikus fájlok,
  ne teljes repó, `.git`, helyi jegyzet vagy fejlesztői szerver.
- [ ] Célként javasolt `quiz.coderlap.com` és `coaster.coderlap.com`; ellenőrizzük
  a tényleges DNS-rekordokat és a meglévő Debian/Caddy kapacitást, beállításokat.
- [ ] Belépési döntés a 0. lépés alapján, telepítés előtt. A cél a közös
  belépés; azonos Basic Auth-jelszó nem jelent automatikusan egy munkamenetet.
  A végleges auth-megoldás még nincs kiválasztva vagy telepítve.
- [ ] Ellenőrizzük a TLS-t, a védett elérést, a kiadási/rollback útvonalat és
  mindkét app telefonos működését. A Coaster külső segédscriptjeit külön vegyük
  számba; teljes offline működést ne ígérjünk ellenőrzés nélkül.
- [ ] Ezután cseréljük az „In Entwicklung” célokat valódi linkekre; maradjon
  egységes fejléc/lábléc és közvetlen visszaút a LAP-hez.

### 3. Haladásjelölés — első kis UX-kör

- [ ] Kártyánként kör alakú, helyi Lucide pipás kapcsoló; önálló, legalább
  44 px érintési cél, külön a téma megnyitásától és a lenyíló paneltől.
- [ ] Rövid, visszafogott animáció; `prefers-reduced-motion` esetén mozgás nélkül.
  Billentyűzettel és képernyőolvasóval is egyértelmű állapot és felirat.
- [ ] „Feldolgoztam” / „Bearbeitet” jelölés, visszavonással. A meglévő
  `viewed` és `done` mentések megmaradnak; a megnyitás nem teljesítés.
- [ ] Témaköri és összesített számláló ugyanabból az állapotból frissül.
  A témakör összesítése nem jelöl egyszerre minden témát késznek.
- [ ] „Mind / Még nincs kész / Feldolgozott” szűrő; együtt működik a kereséssel
  és a témakörszűrővel. Jelölés után a billentyűzetfókusz ne vesszen el.
- [ ] Ellenőrzés: régi mentés, újratöltés, visszavonás, DE/HU váltás,
  tárolási hiba, csökkentett mozgás és iPhone. Első körben nincs fiókszinkron.

### 4–5. Keresés és tananyag

- [ ] Gyűjtsünk öt valós keresési példát elvárt találatokkal. Pontos címtalálat,
  címbeli szókezdet és további keresőkifejezés eltérő súlyt kapjon.
- [ ] Legyen találatszám, egyértelmű üres állapot és szűrőtörlés; maradjanak
  használhatók az ékezet nélküli és kétnyelvű keresések.
- [ ] A témák összevonásának jelentését tisztázzuk: vegyes kvíz, tanulási
  csomag vagy tömeges jelölés? A tartalmi forrásokat és témaazonosítókat ne vonjuk össze.
- [ ] Következő főtéma-javaslat: Informatik, kisebb ellenőrizhető adagokban.
  Utána IT Security. Pozitív válaszmagyarázatok, forráskapcsolat és futtatott
  kódpéldák maradnak az elvárás; külön válasz előtti hint nem szükséges.

### 6. SkillDisplay — feltárás, majd kis próba

A felületen négy igazolástípus látható: Self Assessment, Educational Verification,
Practical Expertise és Official Certification. Ezeket ne mossuk össze a LAP
helyi készre jelölésével vagy a Quiz gyakorlóeredményével.

A [Web Technologies / 74](https://my.skilldisplay.eu/en/skillset/74) csomag
2026-09-30-án „Dormant Skill” figyelmeztetést mutatott: egy vagy több inaktív
készség miatt a teljes csomag már nem igazolható. Ez egy konkrét csomag állapota,
nem az egész szolgáltatásé. A katalógusban Security és projektmenedzsment
csomagok is szerepelnek; ezek alkalmasságát még nem vizsgáltuk.

- [ ] Aktív készségcsomag és öt konkrét tanulási cél kiválasztása a tanárral.
- [ ] LAP-téma → tanulási cél → SkillDisplay-ID megfeleltetés; egy cím
  egyezése nem elég a kompetenciák azonosságához.
- [ ] Előbb egyszerű, önként megnyitható külső linkek. Automatikus adatküldés,
  igazolás vagy badge-kiadás előtt jogosultságot, költséget és adatfolyamot kell
  tisztázni. A tanulási szolgáltatás maradjon használható SkillDisplay nélkül.
- [ ] A [szervezeti feltételeket](https://www.skilldisplay.eu/pricing) az
  intézménnyel egyeztessük; egy tanulói fiókból nem következik igazolói/API-hozzáférés.

Angol kérdésvázlat a tanárnak, küldés nélkül:

> Which active SkillSets would you recommend for mapping an Austrian LAP
> learning project to SkillDisplay? The Web Technologies set (74) currently
> reports dormant skills. Is there a maintained successor?
>
> When you mentioned combining topics, did you mean a mixed practice quiz,
> a learning path/SkillSet, or selecting several topics at once?
>
> Could a small five-skill pilot use the school's existing educator setup,
> with clear criteria for what you would verify?

## Munkaszabály

Csak az aktuális kis feladat kerül megvalósításba. A kapcsolódó ellenőrzést
és dokumentációt ugyanabban a PR-ban frissítjük. A közös stílusfájl három
példánya azonos marad; nincs új keretrendszer, analitika vagy automatikus
külső kompetenciaigazolás a fenti terv alapján.
