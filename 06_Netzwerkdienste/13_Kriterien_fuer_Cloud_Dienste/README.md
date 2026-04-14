# Kriterien fuer Cloud Dienste

## Gyors vizuális kép

| Szempont | Miért fontos? |
|---|---|
| security | az adatok és rendszerek védelme |
| SLA / availability | mennyire elérhető a szolgáltatás |
| data location | hol vannak az adatok |
| costs | hogyan és mennyiért számláznak |
| lock-in | mennyire nehéz később váltani |

## Milyen fő szempontokat nézzünk?

### 1. Biztonság

Kérdések:

- hogyan védik az adatokat
- van-e titkosítás
- milyen jogosultságkezelés érhető el

### 2. Adatvédelem és compliance

Kérdések:

- megfelel-e a jogi követelményeknek
- hol tárolják az adatokat
- milyen szerződéses és adatkezelési feltételek vannak

### 3. Rendelkezésre állás

Kérdések:

- van-e SLA
- milyen kiesési kockázat van
- milyen redundancia és backup lehetőség érhető el

### 4. Költség

Kérdések:

- használatalapú vagy fix díjas
- milyen extra költségek vannak
- hogyan skálázódik az ár

### 5. Teljesítmény és skálázás

Kérdések:

- bírja-e a terhelést
- mennyire gyorsan skálázható
- van-e megfelelő régió közel a felhasználókhoz

### 6. Integráció és hordozhatóság

Kérdések:

- jól kapcsolható-e a meglévő rendszerekhez
- mennyire könnyű migrálni
- mekkora a vendor lock-in veszélye

## Mi az a shared responsibility?

Fontos cloud alapelv:

- a biztonság nem csak a szolgáltató dolga

A szolgáltató és az ügyfél felelőssége megoszlik.

Ez modellenként eltérhet:

- IaaS-nál több marad az ügyfélnél
- SaaS-nál több feladatot visz a szolgáltató

## Vizsgán jól használható megfogalmazás

> Cloud szolgáltatás választásánál nemcsak a funkcionalitást és az árat kell nézni,
> hanem a biztonságot, a compliance-t, az adatlokációt,
> a rendelkezésre állást, a költségmodellt,
> a skálázhatóságot és a vendor lock-in kockázatát is.  
> Emellett fontos megérteni a shared responsibility modellt,
> vagyis azt, hogy a biztonsági felelősség
> a szolgáltató és az ügyfél között megoszlik.

## Gyakori vizsgahibák

- Csak az ár alapján dönteni.
- Azt hinni, hogy cloudban minden biztonsági feladat a szolgáltatóé.
- Nem megemlíteni az adatlokációt és compliance-t.
- Elfelejteni a vendor lock-in problémát.

## Gyors önellenőrzés

1. Mondj legalább öt cloud-választási szempontot.
2. Miért fontos az adatlokáció?
3. Mi az SLA?
4. Mi a vendor lock-in?
5. Mit jelent a shared responsibility?

## Rövid válaszok az önellenőrzéshez

1. Például biztonság, adatvédelem, SLA, költség, skálázhatóság
2. Mert jogi, adatvédelmi és teljesítménybeli jelentősége lehet
3. Szolgáltatási szintvállalás
4. Nehéz vagy drága másik szolgáltatóra váltani
5. A felelősség megoszlik a szolgáltató és az ügyfél között

## Források

1. NIST SP 800-146 - Cloud Computing Synopsis and Recommendations  
   https://csrc.nist.gov/pubs/sp/800/146/final  
   Használat: cloud választási és kockázati szempontok hivatalos, strukturált forrása.

2. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Használat: alapmodellek és a szolgáltatásjelleg hivatalos definíciója.

3. AWS - Shared Responsibility Model  
   https://aws.amazon.com/compliance/shared-responsibility-model/  
   Használat: a megosztott felelősség gyakorlati, modern szemléltetése.

4. Google Cloud - Global Locations  
   https://cloud.google.com/about/locations  
   Használat: adatlokáció, régió és földrajzi elhelyezés gyakorlati szempontjaihoz.

5. Microsoft - Service Level Agreements (SLA) for Online Services  
   https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1  
   Használat: rendelkezésre állás és SLA szempontjának hivatalos példája.

Megnyitva: `2026-04-08`
