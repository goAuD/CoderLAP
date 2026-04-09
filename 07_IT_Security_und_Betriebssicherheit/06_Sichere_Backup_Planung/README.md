# Sichere Backup Planung

## Lényeg 30 másodpercben

A biztonságos backup nem abból áll, hogy "néha lementünk valamit".

Kell egy terv:

- mit mentünk
- milyen gyakran
- hova
- meddig őrizzük
- hogyan állítjuk vissza
- ki felel érte

## Gyors vizuális kép

| Kérdés | Miért fontos? |
|---|---|
| mit mentünk? | ne maradjon ki kritikus adat |
| milyen sűrűn? | adatvesztés mértéke ettől is függ |
| hova mentünk? | biztonság és visszaállítás |
| teszteltük-e? | működik-e valójában a restore |
| ki a felelős? | legyen egyértelmű felelősség |

## Mit kell először eldönteni?

### 1. Mit kell menteni?

Nem mindent ugyanolyan prioritással.

Kritikus lehet például:

- ügyféladat
- dokumentumok
- adatbázis
- konfiguráció
- levelezés
- projektfájlok

### 2. Milyen gyorsan kell visszaállni?

Itt jön elő két fontos fogalom:

- `RPO` = mennyi adatvesztés fér bele
- `RTO` = mennyi leállás fér bele

Vizsgán elég így érteni:

- `RPO` = mennyit veszíthetünk
- `RTO` = mennyi idő alatt kell újra működni

### 3. Milyen gyakran mentsünk?

Ez függ:

- az adatok fontosságától
- a változás gyakoriságától
- az elfogadható adatvesztéstől

## Milyen egy jó backup terv?

Tartalmazza:

- a mentendő rendszereket és adatokat
- a mentési ütemezést
- a használt mentési típust
- a tárolási helyet
- a titkosítás és hozzáférés szabályait
- a megőrzési időt
- a restore folyamatot
- a felelős személyeket

## Miért kell restore teszt?

Mert a nem tesztelt backup könnyen csak látszatbiztonság.

Tesztelni kell:

- visszaállítható-e
- sértetlen-e
- elég gyors-e a helyreállítás

## Miért legyen külön tárolt mentés is?

Ha a mentés mindig ugyanott van, ahol az eredeti adat:

- tűz
- lopás
- ransomware
- hardverhiba

egyszerre viheti el mindkettőt.

Ezért fontos:

- külön tárolás
- lehetőleg offline vagy elkülönített másolat

## Vizsgán jól használható megfogalmazás

> A biztonságos backup tervezésének alapja annak meghatározása, hogy mit kell menteni, milyen gyakran, milyen célidővel kell visszaállni, hol tároljuk a mentéseket, és hogyan ellenőrizzük a visszaállíthatóságot.  
> Egy jó backup terv tartalmazza a mentési ütemezést, a felelősségeket, a megőrzési időt, a hozzáférési szabályokat és a restore teszteket is.  
> A mentéseknek az eredeti rendszertől elkülönítve is rendelkezésre kell állniuk.

## Gyakori vizsgahibák

- Backup terv helyett csak egy eszközt vagy programot említeni.
- Kihagyni a restore tesztet.
- Nem megkülönböztetni a kritikus és kevésbé kritikus adatokat.
- Nem említeni az RPO / RTO logikáját.
- A mentést ugyanott tartani, ahol az eredeti rendszer van.

## Gyors önellenőrzés

1. Mi a két fő üzleti kérdés backupnál?
2. Mit jelent az RPO?
3. Mit jelent az RTO?
4. Miért kell restore teszt?
5. Miért jó az elkülönített mentés?

## Rövid válaszok az önellenőrzéshez

1. Mit mentünk, és milyen gyorsan kell visszaállni
2. Mennyi adatvesztés fér bele
3. Mennyi leállás fér bele
4. Hogy biztosan működjön a visszaállítás
5. Mert egy helyi incidens vagy ransomware nem visz el mindent egyszerre

## Források

1. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Használat: modern, hivatalos backup-tervezési forrás, külön RPO/RTO és recovery test említéssel.

2. BSI - Datensicherung – wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Használat: gyakorlati backup-logika és mentési módszerek közérthető összefoglalása.

3. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Használat: elsődleges, strukturált biztonsági backup-tervezési forrás.

Megnyitva: `2026-04-08`
