# Ablaufdiagramm Flowchart

## Gyors vizuális kép

| Szimbólum | Tipikus jelentés |
|---|---|
| ovális | kezdés / befejezés |
| téglalap | művelet |
| rombusz | döntés |
| nyíl | folyás iránya |

## Mi az a flowchart?

A flowchart vizuálisan leírja:

- milyen lépések követik egymást
- hol van döntési pont
- milyen irányba megy tovább a folyamat

Ezért használják:

- algoritmusokhoz
- üzleti folyamatokhoz
- munkafolyamatokhoz
- dokumentációhoz

## Miért hasznos?

- gyorsan áttekinthető
- technikai és nem technikai közegben is érthető
- segíti a hibák és hiányzó lépések észrevételét
- támogatja a kommunikációt

## Flowchart és struktogramm: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| flowchart | nyilakkal összekötött folyamatábra |
| struktogramm | blokkos, strukturált algoritmusábra |

## Mikor jó választás?

- amikor a folyamat útját kell megmutatni
- amikor több döntési pont van
- amikor csapatnak vagy ügyfélnek is el kell magyarázni a működést

## Egy döntés két teljes útvonala

A szokásos jelölésben a kezdő- és végpont lekerekített, a művelet téglalap, a döntés rombusz, a be- és kimenet paralelogramma. A nyíl a végrehajtás irányát mutatja. Az ábra jelmagyarázata különösen fontos, ha a szervezet más jelölést használ.

Példa egész szám előjelének vizsgálatára:

```text
Kezdés -> n beolvasása -> [n >= 0?]
                           | igen -> "nem negatív" kiírása -> Vége
                           | nem  -> "negatív" kiírása     -> Vége
```

Ez szöveges vázlat; rajzon a kérdés rombuszba kerül. A döntési éleken szerepel az igen/nem felirat. A `0` bemenet az igen ágon halad, a `-3` a nem ágon. A példában már érvényes egész számot feltételezünk; valódi beviteli űrlaphoz az ellenőrzési és újrapróbálási utat is meg kell rajzolni.

## Vizsgán jól használható megfogalmazás

> A flowchart vagy folyamatábra olyan grafikus ábrázolás,
> amely szimbólumokkal és nyilakkal mutatja meg
> egy folyamat vagy algoritmus lépéseit.  
> Segítségével jól szemléltethetők a műveletek sorrendjei, a döntési pontok és az elágazások.  
> Előnye, hogy könnyen áttekinthető és technikai, illetve nem technikai környezetben is jól használható.

## Gyors önellenőrzés

1. Mi a flowchart lényege?
2. Mire szolgál a rombusz?
3. Miért hasznos dokumentációban?
4. Miben más, mint a struktogramm?
5. Hol használható a programozáson kívül?

## Rövid válaszok az önellenőrzéshez

1. Folyamatok vizuális leírása
2. Döntési pontot jelöl
3. Mert gyorsan áttekinthető
4. Nyilas folyamatábra, nem blokkos struktúra
5. Üzleti és szervezeti folyamatoknál is

## Források

- [Lucid: Flowchart Symbols and Their Meanings](https://lucid.co/diagram/flowchart/symbols)  
  A diagramkészítő hivatalos útmutatója a szokásos folyamatábra-jelölésekhez.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Lucid - Flowchart Symbols and Their Meanings  
   https://lucid.co/diagram/flowchart/symbols  
   Használat: a flowchart fogalmának és céljának tiszta, modern összefoglalása.

2. Atlassian - Flowchart template  
   https://www.atlassian.com/software/confluence/templates/flowchart  
   Használat: gyakorlati vállalati és dokumentációs kontextus a flowchart használatához.

3. inf-schule - Bausteine von Algorithmen  
   https://inf-schule.de/algorithmen/grundlagen/algorithmusbegriff/bausteine  
   Használat: összehasonlító oktatási példa a flowchart és a struktogramm közti különbséghez.

Megnyitva: `2026-04-08`
