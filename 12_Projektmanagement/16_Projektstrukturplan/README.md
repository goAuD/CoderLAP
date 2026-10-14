# Projektstrukturplan

## Gyors vizuális kép

| Szint | Példa |
|---|---|
| projekt | webshop bevezetés |
| fő rész | frontend, backend, teszt |
| alrész | login, termékkezelés |
| Arbeitspaket | konkrét, kezelhető feladatcsomag |

## Mi a PSP célja?

- átláthatóvá tenni a teljes projektet
- minden szükséges munkát láthatóvá tenni
- alapot adni az ütemezéshez, költségtervezéshez és felelősséghez

## Miért fontos?

Mert ha nincs jó feladatbontás:

- valami kimarad
- valami duplán szerepel
- nehezebb becsülni az időt és költséget

## Hogyan néz ki?

A PSP lehet:

- fa-struktúra
- számozott lista
- táblázatos bontás

A lényeg nem a forma, hanem a logikai felbontás.

## PSP és ütemterv: ne keverd össze

| Fogalom | Mit mutat? |
|---|---|
| PSP | miből áll a projekt |
| ütemterv | mikor történik valami |

## Egy kis PSP, amelyben a tesztelés is látható

Egy eszköznyilvántartó projekt lehetséges felbontása:

```text
1. Eszköznyilvántartó projekt
   1.1 Egyeztetett követelmények
   1.2 Működő alkalmazás
       1.2.1 Adatimport
       1.2.2 Keresés és módosítás
       1.2.3 Jogosultságkezelés
   1.3 Ellenőrzés és átadás
       1.3.1 Elfogadási tesztek
       1.3.2 Dokumentáció és betanítás
   1.4 Projektirányítás
```

A 100%-os szabály szerint a gyermekelemek együtt lefedik a szülő teljes munkatartalmát. A teszt, a dokumentáció és a vezetési munka is beleszámít; ugyanazt a munkát két helyen nem számoljuk el. A levélelemek tovább bonthatók, amíg jól becsülhető és kiosztható munkacsomagokká válnak.

A számozás hierarchiát mutat, nem végrehajtási sorrendet. A függőségeket és dátumokat külön ütemtervben határozzuk meg.

## Vizsgán jól használható megfogalmazás

> A Projektstrukturplan a projekt teljes munkájának hierarchikus felbontása.  
> Célja, hogy a projekt összes lényeges részfeladata
> és eredménye átláthatóvá váljon,
> és ez alapot adjon az ütemezéshez,
> költségtervezéshez és felelősségi körök kijelöléséhez.  
> A PSP tehát nem időterv, hanem a projekt logikai felbontása.

## Gyors önellenőrzés

1. Mi a PSP lényege?
2. Miért fontos a projekttervezésben?
3. Miben különbözik az ütemtervtől?
4. Mi található a PSP alsóbb szintjein?
5. Mire ad még alapot a PSP az ütemezésen kívül?

## Rövid válaszok az önellenőrzéshez

1. A projekt hierarchikus felbontása
2. Mert átláthatóvá teszi a teljes munkát
3. A PSP a tartalmat, az ütemterv az időt mutatja
4. Kisebb részek és munkacsomagok
5. Költségtervezésre és felelősségekre

## Források

- [PMI: Practice Standard for Work Breakdown Structures](https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063)  
  A PSP teljes munkatartalma, a 100%-os szabály és a projektirányítás szerepe.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Atlassian - Work breakdown structure template  
   https://www.atlassian.com/software/jira/templates/work-breakdown-structure  
   Használat: modern, vizuális és gyakorlati forrás a PSP / WBS logikájához.

2. PMI - Lexicon of Terms  
   https://www.pmi.org/standards/lexicon  
   Használat: hivatalos projektmenedzsment-fogalmak a WBS / PSP hátteréhez.

Megnyitva: `2026-04-08`
