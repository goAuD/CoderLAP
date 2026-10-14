# QR-Code Pruefung und Tools

## Gyors vizuális kép

```text
Űrlap kitöltése
    -> QR generálás
    -> scannerrel beolvasás
    -> tartalom ellenőrzése
```

## Mit javasol a PDF?

A PDF külön említi:

- `CodeTwo QR Code Desktop Reader`

Ez arra jó, hogy:

- képernyőn megjelenő QR-kódot is ellenőrizni lehessen
- telefon nélkül is visszaolvasható legyen a generált kód

> A CodeTwo eszközét a gyártó már nem kínálja letöltésre és nem támogatja.
> A PDF ugyanakkor vizsgán kifejezetten tiltja a telefonhasználatot.
> Ezért előre egyeztetett, engedélyezett asztali QR-olvasóval készülünk,
> és a vizsgakörnyezetben is kipróbáljuk. Otthoni telefonos próba nem helyettesíti ezt.

## Mit kell ellenőrizni?

- tényleg olvasható-e a QR
- a tartalom pontosan `Richtig` vagy `Falsch`
- a valid és invalid tesztpéldáknál jól vált-e

## Egyszerű ellenőrzési lépések

1. futtasd a mintamegoldást
2. adj meg érvényes `SV-Nr`-t
3. olvasd vissza a QR-t
4. ismételd meg érvénytelen `SV-Nr`-rel
5. ellenőrizd, hogy az eredmény helyes-e

## Kis átvételi próba

1. Kitalált nevek és `4422 180599` mellett a külön olvasó `Richtig` szót olvas.
2. Ugyanabban az űrlapban `2511 010100` beírásakor a korábbi QR eltűnik.
   Új ellenőrzés után a visszaolvasott szó `Falsch`.
3. Az SV-mező kiürítése és elküldése hiányzó mezőt jelez, QR nélkül.
4. Új érvényes adat után ismét `Richtig` olvasható. Így az egymást követő állapotokat is vizsgáltuk.

A QR melletti felirat ellenőrzése önmagában kevés: az olvasónak a **képből** kell
visszaállítania ugyanazt a szót. A kód legyen teljes egészében látható, megfelelő kontraszttal
és üres szegéllyel. A nagyítást és a keskeny nézetet is próbáljuk ki.
Az olvasó telepítését, engedélyezését és működését előre tisztázzuk.

Forrás: a katalógus 12. oldala és a [CodeTwo aktuális gyártói tájékoztatója](https://www.codetwo.com/freeware/qr-code-desktop-reader/).
Ellenőrizve: `2026-10-14`.

## Vizsgán jól használható megfogalmazás

> A generált QR-kód helyességét külön ellenőrizni kell egy olvasóeszközzel vagy desktop scannerrel.  
> A cél annak igazolása, hogy a kód valóban a kívánt tartalmat, vagyis `Richtig` vagy `Falsch` szöveget tartalmazza.  
> A PDF ehhez példaként a `CodeTwo QR Code Desktop Reader` használatát említi.

## Gyors önellenőrzés

1. Mi igazolja a QR tényleges tartalmát?
2. Milyen eszközre készülünk a PDF szerinti vizsgán?
3. Miért próbálunk egymás után két különböző számot?

## Rövid válaszok az önellenőrzéshez

1. Egy külön olvasó a képből visszaállítja a várt szót.
2. Előre egyeztetett, engedélyezett asztali olvasóra, telefon nélkül.
3. Így a régi eredmény törlését és az új eredmény megjelenését is ellenőrizzük.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: a javasolt tool és az ellenőrzési elv miatt.

2. CodeTwo QR Code Desktop Reader  
   https://www.codetwo.com/freeware/qr-code-desktop-reader/  
   Használat: a PDF-ben említett ellenőrző eszköz hivatalos oldala.

Megnyitva: `2026-04-09`
