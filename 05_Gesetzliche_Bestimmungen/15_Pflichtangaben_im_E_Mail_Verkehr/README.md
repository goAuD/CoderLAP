# Pflichtangaben im E_Mail_Verkehr

## Gyors vizuális kép

| Kérdés | Rövid válasz |
|---|---|
| mire vonatkozik? | üzleti / céges e-mailekre |
| miért fontos? | azonosíthatóság és jogi megfelelés |
| ugyanaz minden cégnél? | nem, a jogi formától is függhet |
| kapcsolódik a weboldalhoz is? | igen, részben hasonló adatok jelennek meg |

## Miért vannak kötelező adatok?

Azért, hogy az üzleti partner vagy ügyfél tudja:

- melyik vállalkozás ír
- milyen jogi formában működik
- hol található
- milyen nyilvántartási adatokkal rendelkezik

Ez az üzleti átláthatóság része.

## Milyen adatok tipikusak?

A Firmenbuchba bejegyzett vállalkozásoknál tipikusan fontos lehet:

- cégnév / firma
- jogi forma
- székhely
- Firmenbuchnummer
- Firmenbuchgericht

Bizonyos esetekben további adatok is relevánsak lehetnek.

## Melyik szabály különösen fontos?

Vizsgaszinten főleg:

- **UGB 14. §**
- nem Firmenbuch-bejegyzett Gewerbetreibende esetén a **GewO 63. §** is releváns lehet

Ez nem minden vállalkozási formára pontosan ugyanúgy vonatkozik,
ezért a konkrét kötelező adattartalom a cég típusától is függhet.

## Miért fontos IT-s vagy webes munkánál?

Mert egy fejlesztő vagy rendszergazda:

- e-mail sablont készíthet
- CRM-ből automatikus céges levelet küldhet
- ticketing vagy support rendszert üzemeltethet

Ha ezekből kimaradnak a szükséges céges adatok, az jogi problémát okozhat.

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| e-mail kötelező adatai | üzleti levelezés jogi minimuma |
| impresszum | weboldalon közzétett kötelező adatok |
| aláírás / signature | technikai vagy vizuális elem, de jogi tartalmat is hordozhat |

## Példa: központi céges levélsablon

Egy bejegyzett GmbH üzleti leveléhez ilyen **kitöltendő vázlat** készülhet:

```text
[Firmenname] GmbH
Sitz: [Ort]
Firmenbuchnummer: [Nummer]
Firmenbuchgericht: [Gericht]
```

A szögletes zárójeles elemek helyőrzők, nem kitalált cégadatok.
Ez az UGB 14. § szerinti alapadatok szemléltetése, nem minden vállalkozásra teljes sablon.
Felszámolási állapotnál vagy különleges cégformánál további adatok szükségesek lehetnek.
Bejegyzett egyéni vállalkozónál a saját nevet is feltüntetjük, ha eltér a cégnévtől.
A cégjegyzékbe nem bejegyzett, Gewerbeordnung alá tartozó vállalkozásnál
a GewO 63. § szerinti név és a tevékenységi hely adatai irányadók.

Fejlesztőként egy központi sablonból adjuk ezeket a CRM, a számlázó és a támogatási
rendszer üzleti leveleihez. A szöveg egyszerű szöveges levélben is olvasható maradjon;
a csak képként beillesztett aláírás képek tiltásakor eltűnhet.
Név- vagy székhelyváltozáskor a sablon és az automatikus levelek próbája is frissül.

A levél végi szöveges aláírás azonosító információ. A kriptográfiai elektronikus aláírás
más fogalom: az eredet és sértetlenség ellenőrzését szolgálhatja.
A szabályos cégadatok önmagukban nem adnak engedélyt reklámlevél küldésére.

Forrás: [UGB 14. §](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702&Paragraf=14),
[GewO 63. §](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10007517&Paragraf=63).
Ellenőrizve: `2026-10-14`.

## Vizsgán jól használható megfogalmazás

> Az üzleti e-mail-forgalomban bizonyos vállalkozásoknak
> kötelező céges adatokat kell feltüntetniük,
> például a cégnevüket, jogi formájukat,
> székhelyüket és nyilvántartási adataikat.  
> Ez az üzleti átláthatóságot szolgálja,
> és különösen fontos automatikus
> vagy rendszerből küldött üzleti e-maileknél is.  
> A pontos kötelező adattartalom a vállalkozás jogi formájától függhet.

## Gyors önellenőrzés

1. Mire vonatkoznak a kötelező adatok az e-mail-forgalomban?
2. Mondj négy tipikus kötelező céges adatot.
3. Miért fontos ez automatikus leveleknél is?
4. Ugyanaz a szabály minden vállalkozási formánál?
5. Melyik osztrák jogszabályt érdemes itt elsőként megemlíteni?

## Rövid válaszok az önellenőrzéshez

1. Üzleti / céges e-mailekre
2. Cégnév, jogi forma, székhely, Firmenbuchnummer
3. Mert azok is üzleti kommunikációnak minősülhetnek
4. Nem teljesen
5. Az UGB 14. §-át

## Források

1. RIS - Unternehmensgesetzbuch, geltende Fassung  
   https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702  
   Használat: az üzleti kommunikációhoz kapcsolódó céges kötelező adatok elsődleges jogforrása.

2. RIS - Unternehmensgesetzbuch § 14  
   https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702&Paragraf=14&Uebergangsrecht=  
   Használat: a céges levelekre, bestellschein-ekre és weboldalakra vonatkozó kötelező adatok szabálya.

3. RIS - Gewerbeordnung 1994 § 63  
   https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10007517&Paragraf=63&Uebergangsrecht=  
   Használat: a nem Firmenbuch-bejegyzett Gewerbetreibende kötelező adataihoz kapcsolódó elsődleges jogforrás.

4. WKO - Das korrekte E-Mail Impressum für nicht im Firmenbuch eingetragene Einzelunternehmen  
   https://www.wko.at/internetrecht/das-korrekte-e-mail-impressum-nicht-im-fb  
   Használat: gyakorlati, megbízható osztrák kamarai összefoglaló arról, hogy a kötelező adattartalom jogi formától függhet.

5. RIS - Mediengesetz § 24  
   https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10000719&Paragraf=24&Uebergangsrecht=  
   Használat: hírlevelek és ismétlődő elektronikus médiumok esetén kapcsolódó impresszumkötelezettség.

Megnyitva: `2026-04-08`
