# Sichere Backup Planung

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

## Kidolgozott terv: egy kis tanulási rendszer

A feladat szerint legfeljebb egy óra új munka veszhet el (**RPO: 1 óra**), és hiba után négy órán belül használható szolgáltatás kell (**RTO: 4 óra**). Ezek célértékek, nem egy mentőprogram automatikus garanciái.

Az adatbázis mellett a feltöltött fájlokat, a konfigurációt és a szükséges kulcsok helyreállítható példányát is fel kell venni a tervbe. A programkód másolatából önmagában nem áll vissza a felhasználói adat. Az óránkénti mentés csak akkor közelíti meg az RPO-t, ha sikeres, konzisztens, időben befejeződik és a megfelelő példány elérhető.

Példa: az utolsó helyreállítható állapot 13:00, a hiba 13:40-kor történik. Az adatvesztési időablak 40 perc. Ha a 13:00-s mentés hibás és csak 12:00 áll rendelkezésre, ez már 100 perc, tehát az egyórás cél nem teljesül.

A próbán mérd a hozzáférés megszerzését, a környezet felépítését, az adatok visszaállítását és a használhatóság ellenőrzését együtt. Legyen felelős, helyettes, hibajelzés és rögzített megőrzési rend. Az RTO nem csak a másolás sebességéről szól.

## Vizsgán jól használható megfogalmazás

> A biztonságos backup tervezésének alapja annak meghatározása,
> hogy mit kell menteni, milyen gyakran,
> milyen célidővel kell visszaállni,
> hol tároljuk a mentéseket,
> és hogyan ellenőrizzük a visszaállíthatóságot.  
> Egy jó backup terv tartalmazza a mentési ütemezést,
> a felelősségeket, a megőrzési időt,
> a hozzáférési szabályokat és a restore teszteket is.  
> A mentéseknek az eredeti rendszertől elkülönítve is rendelkezésre kell állniuk.

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

### A bővítés ellenőrzött forrásai

- [NIST: Recovery Point Objective](https://csrc.nist.gov/glossary/term/recovery_point_objective): helyreállítandó adatállapot időpontja
- [NIST: Recovery Time Objective](https://csrc.nist.gov/glossary/term/recovery_time_objective): helyreállítás célideje
- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide): elkülönített, titkosított mentések és ellenőrzött helyreállítás

Ellenőrizve: `2026-10-14`.
