# Teljes tartalmi felülvizsgálat

Állapot: a 235 téma bővítése kész, a helyi és GitHub-ellenőrzések zöldek;
a [#42 PR](https://github.com/goAuD/CoderLAP/pull/42) a dev ágba összevonva.
Kiadási mérföldkő: [v0.4.0-reviewed-content](../releases/release-notes-v0.4.0-reviewed-content.md).
Felülvizsgálat: 2026-10-14.

## Cél és keret

A 18 modul mind a 235 regisztrált témáját magyarul és németül ellenőrizzük.
A 2024-es, 2.0 verziójú hivatalos témakatalógus adja a vizsgatémák körét;
az időközben változó technológiák és jogi tények aktuális elsődleges forrást
kapnak. A katalógus régi technológiáit felismerhetően megtartjuk, történeti
szerepüket és a mai gyakorlatot külön megmagyarázzuk.

- Ténybeli hibák, félrevezető leegyszerűsítések és ellentmondó válaszok javítása.
- Témához illő, kidolgozott példa, döntési helyzet vagy ellenőrzési menet.
- Programozási és adatbázisos témákban szükség szerint futtatható kód,
  magyarázat és ellenőrzött kimenet. Részleteket és teljes példákat megkülönböztetünk.
- Közérthető szöveg, em dash nélkül. A helyes gondolatmenetet tanítjuk;
  nem készítünk új „Gyakori vizsgahibák” fejezeteket.
- A HU/DE tartalom, példák és önellenőrző válaszok együtt változnak.
- A meglévő azonosítók, útvonalak és külső források megmaradnak, kivéve
  az ellenőrzés során azonosított hibás vagy elavult hivatkozásokat.

## Kiinduló ellenőrzés

- A nyilvántartásban 235 téma van, mindegyikhez létezik német oldalfájl.
- A magyar törzs nagyjából 106 ezer szóból áll. A szöveg hossza önmagában
  nem igazolja a vizsgára való felkészüléshez szükséges tartalmi mélységet.
- Az automatikus korábbi tartalomellenőrző a fejezeteket és URL-eket nézi;
  a szakmai pontosságot és az érthetőséget külön kell ellenőrizni.
- Karbantartás: a Markdown 3.11.1 frissítése a #40 PR-ban a main ágra került,
  a #39 Dependabot PR ezzel kiváltva és lezárva. A #41 a dev ágra is átvezette.
  A frissítés 83 Python- és 35 Node-teszttel, kétnyelvű builddel és sikeres
  GitHub Actions build/deploy futással ellenőrzött.

## Elkészültségi feltételek

A modulonkénti lezárás felsorolja az átnézett témákat, a tényleges javításokat,
a forrásellenőrzést és a példák ellenőrzését. Az automatikus szerkezeti vizsgálat
nem számít önmagában tartalmi lektorálásnak.

A végén a két nyelv teljes buildje, a nyilvántartás, a források és belső
hivatkozások szerkezete, a meglévő regressziós tesztek és az új futtatható
példák ellenőrzése szükséges. A jogi szövegek oktatási összefoglalók,
konkrét ügyekre nem jelentenek személyre szabott jogi szakvéleményt.

## Modulonkénti eredmények

Az alábbi lefedettség a magyar törzs és a német oldalfájl közös áttekintését
jelenti. A modulon belül minden regisztrált témához tartozik bővítés;
az összetettebb informatikai és programozási részekben több kidolgozott kód is.

| Modul | Témák | Fő bővítés vagy javítás |
| --- | ---: | --- |
| 01. Információtechnikai alapok | 7 | Unicode, UTF-8, bit/byte és SI/IEC egységek; átváltás, kapacitástervezés, igazságtábla. |
| 02. Operációs rendszerek és szoftver | 10 | OS/kernel, firmware, támogatási életciklus, jogosultságok, fájlrendszer, futtatott PowerShell-példa. |
| 03. Mobil hardver | 6 | Eszközválasztás, Android/iOS jogosultságok és frissítés, QR-kód, alkalmazásterjesztés. |
| 04. Dokumentáció és bemutatás | 6 | Konkrét teszteset, technikai napló, használható útmutató, pilot és helyreállítási feltételek. |
| 05. Jogi szabályok | 16 | GDPR-jogalapok és jogok, DPO, incidens, szerzői jog, garancia/szavatosság, TKG/ECG, impresszum, képernyős munka. |
| 06. Hálózati szolgáltatások | 13 | DNS, HTTP/TLS, levelezési protokollok, STARTTLS, FTP, SLA, felhős felelősségek. |
| 07. IT-biztonság és üzembiztonság | 8 | Jogosultság és azonosítás, többtényezős védelem, sérülékenységek, tűzfal, RPO/RTO és mentés. |
| 08. Informatika és társadalom | 11 | Big Data-számítás, IoT/OT, hangasszisztens, eIDAS, követés, biometria, hálózatsemlegesség. |
| 09. Ergonómia | 6 | Munkaállomás közös beállítása, képernyő és fény, BS-V feltételei, mozgás és megszakítás. |
| 10. Szakmai tanácsadás | 5 | Igényfeltárás, teljes költség, érthető technikai magyarázat, panasz és incidens kezelése. |
| 11. Informatika | 43 | Webes alapok, HTML/CSS/JS/TS, adatformátumok, keretrendszerek, paradigmák, biztonságos webes példák, CI/CD. |
| 12. Projektmenedzsment | 20 | Követelmények, ütemezés, kritikus út, felelősségek, folyamatábra, költség és eltéréselemzés. |
| 13. Projektmódszerek és eszközök | 18 | Scrum szerepek és események, backlog, elfogadási feltételek, becslés, verziókezelés. |
| 14. Minőségbiztosítás | 7 | Statikus code review, asztali teszt, határértékek, lefedettség, SemVer és változáskezelés. |
| 15. Programozás alapjai | 20 | Algoritmusok és adatszerkezetek, scope, paraméterátadás, ciklusok, objektumok és OOP, futó JS-példák. |
| 16. Adatbázisok | 19 | Reláció és kapcsolat, kulcsok, normálformák, SQL NULL/constraint, JOIN, tranzakció, zárolás, PDO, mentés és visszaállítás. |
| 17. Rendszerfejlesztés és tesztelés | 13 | Fejlesztési fázisok, reprodukálhatóság, validáció, teszttervezés és végrehajtható példák. |
| 18. Vizsgafeladat | 7 | A bevezetővel együtt teljes feladatmenet, hivatalos SV-súlyozás, QR-tartalom és működő mintaprogram. |
| Összesen | **235** | **470 HU/DE témafájl.** |

## Lényeges tényjavítások

- Az ASCII, a Unicode-kódpont, a JavaScript UTF-16 kódegysége és az UTF-8 byte
  külön fogalom. A hexadecimális jelölés nem tömörítés. Hat átváltási példa
  címe eltért a helyes levezetéstől; a címek is javítva.
- JavaScriptben az objektumra mutató referencia értéke másolódik a paraméterbe.
  A hatókör és az élettartam, illetve a reaktív és az aszinkron működés
  különbsége gyakorlati példát kapott.
- Az elérhető javítással rendelkező, még nem frissített rendszer sérülékenysége
  ettől nem válik zero-day hibává. A POP3 nem feltétlenül törli a szerveren
  maradó levelet. Az offline, az offsite és az immutable mentés nem szinonima.
- SQL-ben a `NOT NULL` nem tiltja az üres szöveget, a `CHECK` és a `NULL`
  együtt értelmezendő. A normalizálás minden kulcsjelöltet figyelembe vesz;
  egy új `id` oszlop önmagában nem szünteti meg az üzleti függéseket.
- A Scrum Review és Retrospective a Sprint része. A Sprint Backlog célból,
  kiválasztott munkából és tervből áll. A SemVer a nyilvános API
  kompatibilitását jelöli, nem egyszerűen a változtatás méretét.
- A GDPR nem kizárólag hozzájárulást ismer. Az adatminimalizálás és a
  korlátozott megőrzés külön alapelv. A DPO-kötelezettség feltételei és
  a nyilvános szakmai elérhetőség külön szerepelnek a rövid válaszokban is.
- A 72 órás incidenshatáridő a tudomásszerzéstől indul. Az elektronikus
  aláírás jogi gyűjtőfogalma nem azonos minden esetben a kriptográfiai
  digitális aláírással. A hagyományos arcfotó nem automatikusan különleges
  biometrikus adatkezelés.
- A VGG 2026. október 1-jétől alkalmazandó javítási szabálya és az EAG-VO
  új visszavételi feltétele az aktuális RIS-szöveg alapján, alkalmazási
  feltételekkel együtt szerepel. A képernyős 50/10 szabály szintén
  feltételekhez és kivételekhez kötött; nem minden ülőmunkára szóló általános szabály.
- A vizsga PDF-je tiltja a telefont, ezért a QR-ellenőrzéshez előre egyeztetett
  asztali megoldást írunk le. A CodeTwo régi letöltése megszűnt.
  Az SV-minta nem javít át észrevétlenül betűs vagy túl hosszú bemenetet,
  inputváltozásra törli az előző eredményt, és megtartja a QR üres szegélyét.
  A formai megfelelés nem bizonyítja a szám tényleges kiadását vagy a biztosítást.

## Ellenőrzések és korlátok

Helyi eredmények:

| Ellenőrzés | Eredmény |
| --- | --- |
| Python regressziós tesztek | 87 sikeres |
| Node tesztek | 122 sikeres; benne 37 új konzolpélda kimenete és HU/DE egyezése |
| Tananyagszerkezet | 235/235 téma sikeres; a két nyelven egyező 1164 önellenőrző kérdéshez ugyanannyi válasz |
| Nyilvántartás | 235 ID, forrásútvonal és slug megmaradt; forrásszámok újragenerálva |
| Nyelvi fájlok | 470/470 módosított HU/DE témalap; nincs em dash, hibás UTF-8 helyettesítő karakter vagy régi vizsgahiba-fejezet |
| Kétnyelvű build | 512 HTML-fájl; nincs hiányzó helyi célfájlra mutató link vagy látható tesztjelölés |
| SQL/PDO | 14 nyelvi SQL-futtatás és 14 további adatbázis-ellenőrzés sikeres |
| PowerShell | A példa Windows PowerShell 5.1 és PowerShell 7 alatt is az elvárt eredményt adta |
| QR-minta | 13 regressziós teszt; mindkét QR-kép független visszaolvasása sikeres |
| Webes minták | Űrlapvalidálás, CSS-kaszkád, Grid, reszponzív töréspont, iframe, natív DOM és jQuery működése böngészőben ellenőrizve |
| Bibliográfiai URL-ek | 705 külön URL technikai próbája; 645 HTTP 200, a többi hozzáférési/hálózati korláttal külön vizsgálva |

A sima `git diff --check` 262 szándékos, két szóközös Markdown-sortörést
jelez. Más whitespace-hiba nincs; a Markdown-sortörések kivételével futtatott
`git -c core.whitespace=-blank-at-eol diff --check` tiszta. A sortöréseket
nem cseréljük a jelenlegi Markdown-renderelő által szövegként megjelenített
backslashre, és nem lazítjuk a repository Git-beállításait.

A kódellenőrzés során talált látható SQL/PDO-tesztjelölések javítva vannak;
a render-tesztek mindhárom használt marker elrejtését és kódblokkon belüli
megőrzését ellenőrzik. Az 01/05/18 modulok második olvasása után a DPO,
a reklámkövetés és a képernyős szünet rövid válaszai is pontosítva lettek.

- A tananyag közvetlenül olvasott és módosított szövege adja a tartalmi
  felülvizsgálat alapját. A kódtesztek a közölt példák működését igazolják;
  nem helyettesítenek tanári szaklektorálást vagy vizsgakövetelmény-változás követését.
- Az önálló JS-példákat a Markdownból futtatjuk, a HU/DE kódot és a közölt
  kimenetet együtt ellenőrizzük. A HTML/CSS-, keretrendszer- és konfigurációs
  részleteknek külön futtatási feltételeik vannak; nem mindegyik teljes alkalmazás.
  A RxJS-példa valódi RxJS 7.8.2-vel lefutott. A Spring- és ASP.NET-mintát
  nem állítjuk teljes szerverkörnyezetben teszteltnek.
- A böngészős mérések asztali Vivaldiban történtek, keskeny viewporttal és
  a mintákhoz megadott különböző méretű konténerekkel is. A kód a témalapon
  szövegként jelenik meg, hosszú sorai külön görgethetők. Fizikai iOS-eszközön
  ez a kör nem futott; az automatizált képrögzítés időtúllépése miatt
  a böngészős bizonyíték a működési próbák és a DOM-mérések eredménye.
- Az SQL- és PDO-ellenőrzés elkülönített, helyi MySQL 8.0.30 környezetben
  történt, szintetikus adatokkal. Sikeres volt a constraint/FK, rollback,
  kétkapcsolatos zárolás és dump-visszaállítás. A kiszolgáló szabályosan leállt.
  Tényleges deadlock, PITR és nagy adatmennyiséges teljesítménymérés nem történt.
  Ez egyszeri helyi vizsgálat; a GitHub CI Python- és Node-teszteket futtat,
  adatbázist nem indít.
- A forrásokhoz elsődleges dokumentációt, szabványkiadót vagy hivatalos
  jogszabályt használtunk. A régi megnyitási dátumot nem állítottuk át
  automatikusan: az új bővítési források saját ellenőrzési dátumot kaptak.
- A HTTP-linkpróba nem egyenlő a tartalom elolvasásával. Egyes oldalak
  automatizált lekérésre 403/404 választ, robotellenőrzést vagy hálózati hibát
  adtak, miközben webes megnyitással elérhetők voltak. Ezeket külön vizsgáltuk;
  egy sikertelen HTTP-kód alapján nem töröltünk forrást.
- A fizetős ISO-szabvány teljes szövegét nem olvastuk újra. Az ISO-katalógus
  és a hozzá kapcsolódó nyilvános hivatalos anyagok szolgáltak alapul.
- A forrásszámláló a számozott és a felsorolásos hivatkozásokat is számolja.
  A szerkezeti ellenőrző immár a 18-as modul regisztrált bevezetőjét is vizsgálja,
  így valóban 235 témára fut. A stabil azonosítók és URL-útvonalak megmaradnak.

## Következő lépés

A kiadás a szokásos dev/main folyamatot követi; a végleges deploy commitot és
az ellenőrzési futásokat a GitHub Release rögzíti. Ezután a következő
CoderQuiz-kérdéscsomag a javított tananyagra támaszkodhat.
SkillDisplay a tanári válaszig szünetel. A DNS, meghívásos belépés és
haladásszinkron terve a közös roadmapben marad.
