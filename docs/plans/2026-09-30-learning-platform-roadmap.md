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
- [ ] A Quiz/Coaster élő DNS-, szerver-, TLS- és belépési beállításait még
  ellenőrizni kell; a nyitott Cloudflare-lap önmagában nem bizonyít telepítést.

Az ágazonosítók dátumhoz kötött pillanatképek. Kiadás előtt friss fetch és diff
kell. A most hiányzó LAP-dokumentációt a következő `dev` → `main` kiadási PR
viheti át; pusztán emiatt nincs sürgős weboldal-deploy.

## Végrehajtási sorrend

| Sorrend | Feladat | Repo | Késznek tekintjük, ha… |
| --- | --- | --- | --- |
| 1 | Publikálható Quiz-kezdőlap és statikus csomag | Quiz | A LAP-programozási kérdések normál indítással elérhetők, külön Python-előnézeti trükk nélkül; a régi mentések nem keverednek az új bankkal. |
| 2 | Védett Quiz/Coaster élesítés és keresztlinkek | mindhárom | DNS, TLS, szerverútvonal, belépés, visszaállítás és mobilos elérés ellenőrzött; csak ezután élnek a LAP eszközlinkjei. |
| 3 | Főoldali haladásjelölés és állapotszűrő | LAP | Egy téma a kártyán jelölhető és visszaállítható; a számlálók és a témaoldal azonos mentést használnak. |
| 4 | Keresés rangsorolása és szókezdetek | LAP | A fontos címtalálatok előre kerülnek, a gépelés közbeni keresés és a meglévő DE/HU aliasok együtt működnek. |
| 5 | Következő tananyagrész és vegyes gyakorlás | Quiz | A következő főtéma kis, forrásolt DE/HU adagokban ellenőrzött; a témák csoportosítása pontosan tisztázott. |
| 6 | Öt tanulási célból álló SkillDisplay-próba | LAP + tanári egyeztetés | Aktív készségazonosítók, tanulási célok és igazolási szerepek tisztázottak; első körben csak hivatkozások készülnek. |

Az 1. feladat és a 2. feladat olvasási előkészítése most indítható. Ha az infra
döntésre vár, a 3. feladat külön ágon haladhat. A tanári kérdések összegyűjtése
közben is végezhető; a SkillDisplay-integráció nem feltétele a helyi tanulásnak.

### 1–2. Publikálás

- [ ] Ajánlott Quiz-belépési pont: a három jóváhagyott programozási rész
  egyértelmű elérése közös kezdőlapról. A végleges navigációt kis előnézetben
  ellenőrizzük. A régi DSGVO-bankot és a meglévő böngészős mentéseket őrizzük meg.
- [ ] Ellenőrizzük, mi kerül a webgyökérbe: csak szükséges statikus fájlok,
  ne teljes repó, `.git`, helyi jegyzet vagy fejlesztői szerver.
- [ ] Célként javasolt `quiz.coderlap.com` és `coaster.coderlap.com`; ellenőrizzük
  a tényleges DNS-rekordokat és a meglévő Debian/Caddy kapacitást, beállításokat.
- [ ] Belépési döntés telepítés előtt: átmeneti Basic Auth külön originenként,
  vagy közös bejelentkezés. Azonos jelszó nem jelent automatikusan egy belépést.
  Új auth-szolgáltató és felhasználói adatbázis még nincs kiválasztva.
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
