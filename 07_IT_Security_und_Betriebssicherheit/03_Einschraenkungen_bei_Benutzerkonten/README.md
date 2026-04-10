# Einschraenkungen bei Benutzerkonten

## Gyors vizuális kép

| Fióktípus | Mire jó? | Kockázat |
|---|---|---|
| standard user | napi használat | kisebb |
| administrator | rendszerbeavatkozás, telepítés | nagyobb |

## Miért kell korlátozni a jogosultságokat?

Mert ha egy felhasználó vagy program túl sok jogot kap:

- nagyobb kárt tud okozni
- könnyebben módosíthat rendszerbeállítást
- malware esetén a támadó is többhez fér hozzá

## Mi az a standard user megközelítés?

A biztonságosabb alapelv:

- a felhasználó napi munkát normál joggal végez
- admin jogot csak külön jóváhagyással vagy külön admin fiókkal használ

Ez csökkenti:

- a véletlen hibák számát
- a káros kód hatását

## Mi a szerepe a UAC-nak?

A `User Account Control` (`UAC`) a Windows egyik védelmi eleme.

Feladata:

- jelezni, ha egy művelet magasabb jogosultságot kér
- megakadályozni, hogy minden automatikusan admin joggal fusson

## Jó gyakorlatok

- külön admin és külön napi fiók használata
- admin jog csak indokolt esetben
- UAC bekapcsolva hagyása
- ismeretlen programot ne futtassunk emelt joggal

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| standard user | korlátozottabb napi felhasználó |
| admin account | magas jogosultságú fiók |
| UAC | emelési jóváhagyási mechanizmus |
| least privilege | csak a szükséges minimum jogot adni |

## Vizsgán jól használható megfogalmazás

> A felhasználói fiókok korlátozásának célja a legkisebb szükséges jogosultság elvének érvényesítése.  
> Napi munkára célszerű standard user fiókot használni, és csak indokolt esetben emelni admin szintre.  
> Ez csökkenti a hibák, a jogosulatlan rendszer-módosítások és a malware által okozható károk mértékét.

## Gyakori vizsgahibák

- Azt mondani, hogy mindenki legyen admin, mert úgy egyszerűbb.
- A UAC-t összekeverni magával az admin fiókkal.
- Nem megemlíteni a least privilege elvet.
- Azt hinni, hogy a felhasználói korlátozás csak kényelmetlenség, de nem biztonsági előny.

## Gyors önellenőrzés

1. Miért jó a standard user napi használatra?
2. Mi a least privilege elv?
3. Mire való a UAC?
4. Miért veszélyes a folyamatos admin használat?
5. Mi a jó gyakorlat admin jogoknál?

## Rövid válaszok az önellenőrzéshez

1. Mert kisebb a kár lehetősége
2. Csak a szükséges minimum jogosultságot adni
3. Emelt jogosultságú műveletek kontrolljára
4. Mert hiba vagy malware esetén nagyobb a kár
5. Csak szükség esetén, külön vagy ideiglenes admin joggal használni

## Források

1. Microsoft Learn - User Account Control  
   https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/  
   Használat: hivatalos Windows-forrás a UAC és a jogosultságemelés szerepéhez.

2. Microsoft Learn - How User Account Control works  
   https://learn.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works  
   Használat: a standard user alapműködés és az emelési folyamat részletesebb leírása.

3. Microsoft Learn - Local Accounts  
   https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts  
   Használat: Microsoft ajánlás arra, hogy napi munkára ne a beépített admin megközelítés legyen az alap.

4. CISA - Zero Trust  
   https://www.cisa.gov/topics/cybersecurity-best-practices/zero-trust  
   Használat: hivatalos CISA-forrás a least privilege elv modern biztonsági jelentőségéhez.

Megnyitva: `2026-04-08`
