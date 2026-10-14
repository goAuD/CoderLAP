# Datenminimierung

## Gyors vizuális kép

| Cél | Szükséges adat példája | Tervezési döntés |
|---|---|---|
| hírlevél kézbesítése | e-mail-cím | csak a kézbesítéshez és az engedély igazolásához szükséges adatok |
| csomag kiszállítása | név, szállítási cím | a kézbesítés indokolja a címadatot |
| felhasználói beállítás tárolása | belső fiókazonosító, beállítás | teljes ügyfélprofilt nem másolunk a beállítástáblába |
| hibakeresés | hibakód, szükséges technikai környezet | az űrlap személyes tartalmát kihagyjuk a naplóból |

## Hol szerepel a GDPR-ban?

Az adattakarékosság a GDPR **5. cikk (1) c)** pontjához kapcsolódik.

Lényege:

- az adat legyen
  - megfelelő
  - releváns
  - a szükségesre korlátozott

## Mit jelent ez a gyakorlatban?

Ha például egy webshop csak áruszállítást végez, akkor általában indokolt lehet:

- név
- szállítási cím
- kapcsolattartási adat

De általában **nem** indokolt például:

- családi állapot
- vallási meggyőződés
- személyes érdeklődési körök

ha ezek nem szükségesek a rendelés teljesítéséhez.

## Példák

### 1. Hírlevél feliratkozás

Ha valaki csak hírlevelet kér, általában elég lehet:

- e-mail-cím

Nem feltétlenül kell:

- lakcím
- születési dátum
- telefonszám

### 2. Álláspályázat

Csak olyan adat kérhető, ami a kiválasztáshoz indokolt.

### 3. Ügyfélregisztráció

Ne legyen túl sok kötelező mező, ha azok nem szükségesek a szolgáltatáshoz.

## Adattakarékosság és célhoz kötöttség

A két fogalom összefügg, de nem ugyanaz.

| Fogalom | Mit jelent? |
|---|---|
| célhoz kötöttség | világos cél kell az adatkezeléshez |
| adattakarékosság | csak a célhoz szükséges adat kezelhető |

## Adattakarékosság és megőrzési idő

Az adattakarékosság az adatok körét és részletességét korlátozza a célhoz szükségesre
(5. cikk (1) c)). A megőrzés idejét a különálló **korlátozott tárolhatóság** elve
szabályozza (5. cikk (1) e)). Együtt alkalmazzuk őket: megfelelő mennyiségű adatot
csak az indokolt ideig kezelünk.

## Miért fontos?

Mert ha kevesebb adatot kezelünk:

- kisebb a kockázat
- egyszerűbb a védelem
- kisebb a visszaélési lehetőség
- könnyebb megfelelni a GDPR-nak

## Űrlaptervezés indoklással

Egy javítási időpontfoglalóban a felhasználó nevét, elérhetőségét, az eszköz típusát
és a választott időpontot használjuk. A személyi igazolvány másolata nem szükséges
ahhoz, hogy az időpontot lefoglaljuk. Ha a visszajelzés e-mailben történik,
a telefonszám kötelezővé tételének szükségességét külön kell indokolni.

A döntést egy rövid adatjegyzékben rögzíthetjük: **mező → cél → szükségesség → hozzáférő → törlés**.
A hiba leírásához szabad szöveges mező helyett néhány kategória is elég lehet;
ha szöveget kérünk, jelezzük, hogy jelszót vagy más személy érzékeny adatait ne adják meg.
Az „opcionális” megjelölés önmagában nem tesz minden adatgyűjtést indokolttá.

A szerver is csak az engedélyezett mezőket dolgozza fel, a naplózás pedig ne mentse
le automatikusan a teljes kérést. Teszteléshez mesterséges adatot használunk.
Egy későbbi export ugyanilyen szűrést igényel: a címzett a feladatához szükséges
adatokat kapja, nem automatikusan a teljes táblát.

Forrás: [EDPB: adatkezelési alapelvek](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en),
GDPR 5. és 25. cikk. A foglaló példa saját tervezési gyakorlat. Ellenőrizve: 2026-10-14.

## Vizsgán jól használható megfogalmazás

> Az adattakarékosság a GDPR egyik alapelve.  
> Azt jelenti, hogy csak olyan személyes adat kezelhető,
> amely az adott adatkezelési célhoz szükséges, megfelelő és releváns.  
> A gyakorlatban ez azt jelenti, hogy nem kérhetünk be felesleges adatokat,
> a megőrzési időt pedig a kapcsolódó, különálló korlátozott tárolhatóság elve szerint határozzuk meg.

## Gyors önellenőrzés

1. Mit jelent az adattakarékosság?
2. Miért nem kérhetünk be felesleges adatokat?
3. Mi a kapcsolat a cél és az adattakarékosság között?
4. Csak a gyűjtésre vonatkozik-e ez az elv?
5. Mondj egy jó gyakorlati példát.

## Rövid válaszok az önellenőrzéshez

1. Csak a szükséges személyes adat kezelhető
2. Mert a GDPR ezt tiltja, ha az adat nem szükséges a célhoz
3. A szükségességet mindig a cél alapján kell megítélni
4. Nem, a felhasználás és a továbbítás adatkörét is korlátozza; a tárolási időt külön alapelv szabályozza
5. Hírlevélhez elég lehet csak az e-mail-cím

## Források

1. EUR-Lex - Regulation (EU) 2016/679  
   https://eur-lex.europa.eu/eli/reg/2016/679/oj  
   Használat: Art. 5(1)(c) - data minimisation mint elsődleges jogforrás.

2. USP - Datenschutz: allgemeine Informationen  
   https://www.usp.gv.at/it-geistiges-eigentum/datenschutz/allgemeine-informationen.html  
   Használat: osztrák, vállalkozásoknak szóló hivatalos magyarázat adatkezelési elvekről.

3. Datenschutzbehörde - Was ist Datenschutz?  
   https://dsb.gv.at/rechte-pflichten/was-ist-datenschutz  
   Használat: személyes adatok és adatvédelmi alapelvek osztrák hatósági áttekintése.

Megnyitva: `2026-04-08`
