# Backup Medien und Lagerung

## Gyors vizuális kép

| Médium | Előny | Figyelni kell rá |
|---|---|---|
| külső HDD / SSD | egyszerű, olcsó, gyors | fizikailag védeni kell |
| NAS | kényelmes, központi | ransomware ellen önmagában nem elég |
| tape | hosszú távra is jó lehet | speciális kezelés |
| cloud backup | offsite előny | hozzáférés, titkosítás, vendor kérdések |

## Milyen backup médiumok léteznek?

### Külső HDD / SSD

Előny:

- egyszerű
- gyors
- sok helyen olcsó megoldás

### NAS

Előny:

- központi tárolás
- automatizálható mentések

Figyelem:

- ha állandóan elérhető a hálózaton, ransomware esetén veszélyben lehet

### Tape

Előny:

- nagyobb környezetben jól használható
- hosszabb távú archiválási vagy backup feladatra is alkalmas lehet

### Cloud backup

Előny:

- elkülönített, külső helyszín
- sokszor könnyen skálázható

Figyelem:

- titkosítás
- hozzáféréskezelés
- jogi és szolgáltatói kérdések

## Mit jelent a biztonságos tárolás?

A backupot úgy kell tárolni, hogy:

- ne ugyanott legyen, mint az eredeti rendszer
- ne legyen könnyen illetéktelenül elérhető
- védve legyen tűz, víz, lopás és jogosulatlan hozzáférés ellen

## Miért fontos az offsite vagy elkülönített tárolás?

Mert egy helyi incidens:

- tűz
- betörés
- hardverhiba
- ransomware

egyszerre pusztíthatja el az elsődleges adatot és a közeli mentést.

## Mire kell még figyelni?

- titkosítás, ha érzékeny adat van a mentésben
- fizikai védelem
- hozzáférési jogok
- címkézés és rotáció
- időnkénti ellenőrzés és restore teszt

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| backup médium | amin a mentés fizikailag vagy logikailag tárolódik |
| tárolási hely | ahol a mentés van |
| online elérhető backup | kényelmes, de támadhatóbb |
| offline / air-gapped backup | leválasztott, jobban védhető |

## Vizsgán jól használható megfogalmazás

> A backup médiumnál és tárolásnál nemcsak a kapacitás számít, hanem a biztonság és a helyreállíthatóság is.  
> A mentéseket célszerű az eredeti rendszertől elkülönítve, megfelelően védett helyen tárolni, és érzékeny adatok esetén titkosítani.  
> A hálózaton állandóan elérhető mentés önmagában nem elég, ezért fontos lehet az offline vagy offsite példány is.

## Gyakori vizsgahibák

- A NAS-t automatikusan teljesen biztonságos backupnak tekinteni.
- Nem említeni az elkülönített tárolást.
- Elfelejteni a titkosítást és hozzáférésvédelmet.
- Azt hinni, hogy egyetlen médium minden célra optimális.

## Gyors önellenőrzés

1. Mondj három backup médiumot.
2. Miért kockázatos az állandóan online elérhető backup?
3. Miért fontos az offsite tárolás?
4. Mikor fontos a titkosítás?
5. Elég-e csak lementeni, teszt nélkül?

## Rövid válaszok az önellenőrzéshez

1. Külső HDD/SSD, NAS, tape, cloud backup
2. Mert támadás vagy ransomware is elérheti
3. Mert helyi katasztrófa esetén is megmaradhat a mentés
4. Ha érzékeny adat van benne
5. Nem

## Források

1. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Használat: elsődleges forrás a biztonságos backup-médiumok, elkülönített tárolás és megőrzési elvek számára.

2. BSI - Datensicherung – wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Használat: gyakorlati média- és mentési példák, különösen külső meghajtók és egyszerű mentési megoldások esetén.

3. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Használat: modern, hivatalos ajánlás elkülönített és többpéldányos backup-stratégiára.

4. CISA - Back Up Government Data  
   https://www.cisa.gov/audiences/state-local-tribal-and-territorial-government/secure-us-sltt/back-government-data  
   Használat: restore és rollback szempontok, valamint a mentések rendszeres ellenőrzése.

Megnyitva: `2026-04-08`
