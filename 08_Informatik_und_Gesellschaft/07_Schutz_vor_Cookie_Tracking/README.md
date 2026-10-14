# Schutz vor Cookie Tracking

## Gyors vizuális kép

| Kockázat | Védekezés |
|---|---|
| profilalkotás | marketing sütik elutasítása |
| cross-site követés | harmadik fél cookie-k blokkolása |
| túl sok adatgyűjtés | privacy beállítások és kiegészítők |
| rejtett követés | tájékozódás és tudatos kattintás |

## Mi az a cookie?

A cookie egy kis adat, amit a weboldal a böngészőben eltárolhat.

Lehet hasznos is, például:

- bejelentkezés megjegyzése
- kosár tartalmának tárolása

De lehet követési célú is:

- marketing
- analitika
- profilozás

## Mi a tracking lényege?

A tracking célja lehet:

- szokások megfigyelése
- hirdetési profil készítése
- több oldal közötti követés

## Melyik cookie problémásabb?

Jellemzően:

- a nem szükséges
- különösen a harmadik féltől származó
- marketing vagy követési célú sütik

szoktak nagyobb privacy kockázatot jelenteni.

## Hogyan lehet védekezni?

### 1. Ne fogadj el mindent automatikusan

Ha lehet:

- csak a szükséges sütiket engedélyezd

### 2. Használj böngészőbeállításokat

Lehet:

- sütik törlése
- harmadik fél sütijeinek blokkolása
- privát böngészés

### 3. Használj privacy-eszközöket

Például:

- trackerblokkoló kiegészítők
- külön böngészőprofilok

### 4. Figyelj a hozzájárulásra

A jó gyakorlat:

- a nem szükséges cookie-khoz aktív hozzájárulás kell

## Mire kell figyelni?

A böngészőben a "Do Not Track" vagy hasonló funkció:

- nem mindig elég
- nem minden weboldal tartja tiszteletben

## Sütik nélkül is lehet követés

Egy oldal böngésző-ujjlenyomatot képezhet a technikai jellemzőkből, vagy bejelentkezett fiókhoz kapcsolhatja az aktivitást. A `localStorage`, egy követőképpont vagy URL-ben átadott azonosító szintén része lehet követésnek. A „cookieless” ezért nem azonos azzal, hogy nincs személyes adatkezelés vagy szükség hozzájárulásra.

Egy osztrák tanulói oldal bejelentkezési sütijénél megvizsgáljuk, valóban szükséges-e a kért szolgáltatáshoz. A reklámkövetés külön cél, nem válik szükségessé attól, hogy a fejlesztő hasznosnak tartja. A DSB szerint ha csak technikailag szükséges sütik vannak, önmagukban ezekhez nincs szükség hozzájárulási bannerre. A tájékoztatási és egyéb adatvédelmi kötelezettségeket ettől még vizsgálni kell.

A privát böngészés főként a helyi előzményeket és a munkamenet tárolását kezeli. A szolgáltató számára nem tesz automatikusan névtelenné. Egy saját oldal ellenőrzésénél a hálózati kéréseket és a tényleges adattovábbítást is megnézzük, nem csak a sütik listáját.

## Vizsgán jól használható megfogalmazás

> A cookie tracking során a weboldalak vagy harmadik felek
> sütik és hasonló technológiák segítségével
> követhetik a felhasználó online viselkedését.  
> A védekezéshez fontos a nem szükséges cookie-k elutasítása,
> a harmadik fél sütijeinek korlátozása,
> a böngésző privacy beállításai
> és szükség esetén trackerblokkoló eszközök használata.  
> Adatvédelmi szempontból különösen a marketing és cross-site követés problémás.

## Gyors önellenőrzés

1. Mi a cookie tracking?
2. Melyik sütik jelentenek gyakrabban privacy kockázatot?
3. Mondj három védekezési módot.
4. Elég-e mindig a privát böngészés?
5. Miért problémás a cross-site tracking?

## Rövid válaszok az önellenőrzéshez

1. Online viselkedés követése sütikkel és hasonló technológiákkal
2. A nem szükséges, főleg harmadik fél marketing sütik
3. Elutasítás, blokkolás, törlés, kiegészítők használata
4. Nem
5. Mert több oldal között is profilozhat

## Források

- [Datenschutzbehörde: Datenschutz & Cookies](https://dsb.gv.at/faqs/datenschutz-cookies)  
  Osztrák követelmények és technikai szükségesség.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. ICO - Cookies  
   https://ico.org.uk/for-the-public/online/cookies/  
   Használat: hivatalos, közérthető forrás arról, mik a cookie-k és hogyan lehet őket kezelni felhasználói oldalon.

2. ICO - Cookies and similar technologies  
   https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/  
   Használat: hivatalos magyarázat arra, hogy a nem szükséges cookie-khoz aktív hozzájárulás kell.

3. EDPB - Report of the work undertaken by the Cookie Banner Taskforce  
   https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf  
   Használat: európai adatvédelmi hatósági közös álláspont a cookie bannerek tipikus hibáiról.

4. EUR-Lex - ePrivacy-Richtlinie 2002/58/EG, Art. 5 Abs. 3  
   https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A02002L0058-20091219  
   Használat: a tárolás és hozzáférés hozzájárulási feltétele, valamint a szükséges működés kivétele a hatályos konszolidált szövegben; ellenőrizve 2026-10-14.

Megnyitva: `2026-04-08`
