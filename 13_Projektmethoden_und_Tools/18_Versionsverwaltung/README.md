# Versionsverwaltung

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| repository | a projekt tárolója |
| commit | elmentett változáscsomag |
| branch | külön fejlesztési ág |
| merge | ágak összevonása |

## Mi az a verziókezelés?

A verziókezelő rendszer nyomon követi:

- mikor történt változás
- ki végezte a változtatást
- mi változott
- hogyan lehet összehasonlítani vagy visszaállítani korábbi állapotokat

## Miért fontos?

- csapatmunkához alapvető
- csökkenti az elveszett munka kockázatát
- támogatja a hibakeresést
- biztonságosabbá teszi az új fejlesztések kipróbálását

## Központosított és elosztott rendszer

| Típus | Jelleg |
|---|---|
| központosított | központi szerveren van a fő verzió |
| elosztott | minden fejlesztőnél lehet teljes másolat |

A `Git` elosztott verziókezelő rendszer.

## Tipikus alapműveletek

- klónozás
- módosítás
- commit
- branch létrehozása
- merge
- pull / push

## Verziókezelés és backup: ne keverd össze

| Fogalom | Mire való? |
|---|---|
| verziókezelés | változások követése és együttműködés |
| backup | adatvesztés elleni biztonsági mentés |

Egy verziókezelő rendszer hasznos, de nem ugyanaz, mint a teljes backup-stratégia.

## Munkakönyvtár, staging és commit

A Gitben a módosított fájl először a munkakönyvtárban változik. A staging area az előkészített változásokat tartalmazza a következő commithoz. A commit a kiválasztott állapotot rögzíti a helyi történetben; a távoli tárolóba külön push juttatja el.

Az alábbi parancsok egy már megnyitott gyakorlórepositoryban mutatják a különbségeket, és nem módosítanak fájlt:

```bash
git status --short
git diff
git diff --staged
git log -3 --oneline
```

A `git diff` az előkészítés nélküli változást, a `git diff --staged` a következő commitba előkészített eltérést mutatja. Ha ugyanaz a sor két ágon eltérően változott, merge-konfliktus lehet: a szándékot kell összeegyeztetni, majd ellenőrizni az eredményt.

Megosztott történetben egy hibás commit hatását gyakran új, visszafordító committal (`git revert`) kezeljük. A `.gitignore` nem törli a már követett fájlokat vagy a történetet; véletlenül megosztott titkos kulcsot külön vissza kell vonni.

## Vizsgán jól használható megfogalmazás

> A verziókezelés a fájlok, különösen a forráskód változásainak nyomon követését és kezelését jelenti.  
> Segítségével visszanézhető, ki mit és mikor módosított,
> valamint lehetőség van korábbi állapotok visszaállítására
> és több fejlesztő munkájának összehangolására.  
> A modern szoftverfejlesztésben a Git az egyik legelterjedtebb elosztott verziókezelő rendszer.

## Gyors önellenőrzés

1. Mi a verziókezelés lényege?
2. Mire jó a `commit`?
3. Mi a `branch` szerepe?
4. Miért hasznos csapatmunkában?
5. Miért nem ugyanaz, mint a backup?

## Rövid válaszok az önellenőrzéshez

1. A változások követése és kezelése
2. Változások rögzítésére
3. Elkülönített fejlesztési ág létrehozására
4. Mert segít az együttműködésben és konfliktuskezelésben
5. Mert más a célja, mint a biztonsági mentésnek

## Források

- [Git: Recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)  
  Staging, diff, commit és az ignore szabályok határa.

- [Git: git-revert](https://git-scm.com/docs/git-revert)  
  Visszafordító commit történetátírás nélkül.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Git - About Version Control  
   https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control  
   Használat: elsődleges, hivatalos alapforrás a verziókezelés fogalmához.

2. Atlassian - What is version control?  
   https://www.atlassian.com/git/tutorials/what-is-version-control  
   Használat: modern, gyakorlati összefoglaló a VCS működéséről és előnyeiről.

Megnyitva: `2026-04-08`
