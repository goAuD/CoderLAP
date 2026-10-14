# CI CD Vorgaben

## Gyors vizuális kép

| Elvárás | Miért kell? |
|---|---|
| kötelező tesztek | hibás kód kiszűrése |
| védett branch | kontrollált merge |
| review és approval | minőség és biztonság |
| környezetvédelem | ne menjen bármi azonnal élesbe |
| naplózás | visszakövethetőség |

## Tipikus CI/CD-szabályok

- kötelező build és teszt merge előtt
- védett branch-ek
- required status checks
- kötelező code review
- deployment approval bizonyos környezetekhez
- secrets biztonságos kezelése
- rollback lehetőség
- verziózás és naplózás

## Miért fontosak a szabályok?

Mert az automatizálás önmagában nem elég.

Ha nincs governance, akkor:

- hibás kód átjuthat
- bárki közvetlenül élesbe tehet változást
- nincs kontroll vagy auditálhatóság

## Tipikus környezeti elvek

| Környezet | Jellemző elvárás |
|---|---|
| development | gyors tesztelés |
| staging | éleshez hasonló ellenőrzés |
| production | erős védelem, jóváhagyás, monitorozás |

## Mire kell figyelni?

- Az éles környezetre szigorúbb szabályok kellenek.
- A pipeline hibája is kockázat.
- A titkokat (`secrets`) nem szabad a kódban tárolni.
- A visszagörgetésnek is tervezettnek kell lennie.
- A szabályok legyenek világosak és következetesen betartottak.

## Konkrét előírásból ellenőrizhető bizonyíték

Egy kis csapat szabályai is lehetnek rövidek és számonkérhetők. A következő
példa nem a jelenlegi repository-beállítások leírása, hanem egy lehetséges
szabályrendszer:

| Előírás | Miből látszik, hogy teljesült? |
|---|---|
| változtatás PR-on át | a commit és a hozzá tartozó review visszakereshető |
| kötelező teszt és build | az adott összevonandó változathoz tartozó eredmény sikeres |
| függőség és eszköz verziója ismert | lockfile és rögzített futtatókörnyezet |
| éles telepítés korlátozott | csak engedett branch és telepítési identitás éri el |
| kiadás visszakövethető | commit, artifact, időpont és célkörnyezet rögzítve |
| helyreállítás tervezett | működési próba és kipróbált visszaállítási eljárás |

**A CI is kódot futtat.** Egy külső PR tesztje nem kaphat éles titkokat vagy
írható hozzáférést a kiszolgálóhoz. A telepítési lépés kapja csak a szükséges,
legkisebb jogosultságot. A GitHub Actions külső actionje teljes commit-SHA-ra
rögzíthető; ez rögzített kódot jelöl, de a kód megbízhatóságát és későbbi
frissítését továbbra is értékelni kell. A PR címét és más külső szöveget adatként
kezeljük, nem illesztjük ellenőrizetlenül shellparancsba.

A „zöld” ellenőrzés mögött tényleges munka legyen: vizsgáljuk meg, hogy a teszt
valóban lefutott-e, és nem lett-e feltétellel kihagyva vagy a hibája elnyelve.
A kötelező check neve, az adminisztrátori megkerülés és az érvényes szabályok
együtt határozzák meg, mennyit véd a beállítás. Naplóba a diagnózishoz szükséges
adat kerül, jelszó és token nem.

Az elvárásokat a projekt kockázatához igazítjuk. Egy statikus tananyag és egy
fizetéseket kezelő szolgáltatás nem ugyanolyan telepítési kapukat kíván, de
mindkettőnél érthetőnek kell lennie, mi futott, mi került ki és hogyan javítható.

## Vizsgán jól használható megfogalmazás

> A CI/CD előírások olyan szabályok,
> amelyek biztosítják,
> hogy a build, teszt, kiadás és telepítés folyamata
> ellenőrzött, biztonságos és visszakövethető legyen.  
> Ide tartozhatnak például a kötelező státuszellenőrzések,
> a védett branchek, a code review, a deployment jóváhagyás,
> a környezetvédelem, a titkok biztonságos kezelése
> és a rollback lehetősége.  
> Ezek a szabályok azért fontosak, mert az automatizálást kontrollal és minőségbiztosítással kell összekapcsolni.

## Gyors önellenőrzés

1. Mit jelent a CI/CD előírás?
2. Miért kellenek védett branchek?
3. Miért fontos a required status check?
4. Miért kell deployment approval?
5. Miért veszélyes a secretet a kódban tárolni?

## Rövid válaszok az önellenőrzéshez

1. A pipeline működését szabályozó elvárás
2. Mert kontrollálják a merge-et
3. Mert hibás kódot blokkolhat
4. Mert az élesbe jutást védi
5. Mert biztonsági kockázat

## Források

Ellenőrizve: `2026-10-14`.

- [GitHub: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use): legkisebb jogosultság, PR-kód, titkok és rögzített action-verzió.
- [GitHub: Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches): kötelező ellenőrzések és megkerülési szabályok.


1. GitHub Docs - About protected branches  
   https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches  
   Használat: branch protection, kötelező review és status check szabályok.

2. GitHub Docs - Deployments and environments  
   https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments  
   Használat: környezetek, environment rules és deployment védelem.

3. GitHub Docs - Reviewing deployments  
   https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments  
   Használat: jóváhagyási folyamat beillesztése deployment elé.

4. GitHub Docs - About continuous integration  
   https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration  
   Használat: a CI-rész kötelező ellenőrzési logikájának alapja.

Megnyitva: `2026-04-08`
