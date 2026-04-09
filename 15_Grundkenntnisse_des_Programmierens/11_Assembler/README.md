# Assembler

## Lényeg 30 másodpercben

Az **assembler** két kapcsolódó dolgot jelenthet:

- egy alacsony szintű programnyelvet, azaz az assembly nyelvet
- vagy azt az eszközt, amely ezt gépközeli formára alakítja

Röviden:

- nagyon közel van a hardverhez
- erősen processzorfüggő
- nehezebb olvasni és írni, mint a magas szintű nyelveket

## Gyors vizuális kép

| Szint | Példa |
|---|---|
| magas szintű nyelv | `Python`, `Java`, `C#` |
| alacsony szintű nyelv | assembly |
| gépi kód | a processzor által közvetlenül értett utasítások |

## Mi az assembly nyelv?

Az assembly olyan nyelv, amelyben a gépi utasításokat ember számára olvashatóbb, rövid mnemonikákkal írjuk le.

Például:

- `MOV`
- `ADD`
- `JMP`

Ezek már nagyon közel állnak a processzor működéséhez.

## Mi az assembler mint eszköz?

Az assembler program:

- beolvassa az assembly forráskódot
- lefordítja gépközeli formára
- előállít objektumkódot vagy kapcsolható kimenetet

## Miért fontos?

- jobban megérthető vele a számítógép belső működése
- fontos lehet beágyazott rendszerekben vagy hardverközeli fejlesztésben
- teljesítménykritikus, alacsony szintű feladatoknál előfordulhat

## Előnyök

- nagyon pontos hardverközeli kontroll
- kis méretű és optimalizált megoldások lehetősége
- architektúra mélyebb megértése

## Hátrányok

- nehéz írni és karbantartani
- rosszabb hordozhatóság
- lassabb fejlesztés
- erős processzorfüggőség

## Assembler, compiler, interpreter: ne keverd össze

| Fogalom | Mivel dolgozik? |
|---|---|
| assembler | assembly nyelvvel |
| compiler | magas szintű nyelvvel |
| interpreter | futás közben értelmezett kóddal |

## Vizsgán jól használható megfogalmazás

> Az assembler egyrészt egy alacsony szintű programnyelvhez kapcsolódó fogalom, másrészt az a fordítóeszköz, amely az assembly utasításokat gépközeli kóddá alakítja.  
> Az assembly nyelv közel áll a processzor utasításkészletéhez, ezért hardverfüggőbb és nehezebben kezelhető, mint a magas szintű programozási nyelvek.  
> Előnye a pontos vezérlés, hátránya a bonyolultság és a gyengébb hordozhatóság.

## Gyakori vizsgahibák

- Az assemblert pusztán compilernek nevezni.
- Azt állítani, hogy az assembly = gépi kód.
- Nem megemlíteni a hardverfüggőséget.
- Összekeverni az assembly nyelvet az assembler programmal.

## Gyors önellenőrzés

1. Mi az assembly nyelv?
2. Mi az assembler mint eszköz?
3. Miért alacsony szintű?
4. Mi az egyik fő előnye?
5. Mi az egyik fő hátránya?

## Rövid válaszok az önellenőrzéshez

1. Hardverközeli programnyelv
2. Olyan eszköz, ami assemblyből gépközeli kódot készít
3. Mert közel áll a processzor utasításaihoz
4. Pontos kontroll
5. Nehéz karbantartás és gyenge hordozhatóság

## Források

1. GNU Binutils - Using as  
   https://sourceware.org/binutils/docs/as/  
   Használat: hivatalos elsődleges forrás a GNU assembler működéséhez.

2. GCC - Overall Options  
   https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html  
   Használat: kiegészítő háttér a fordítási folyamat és az assembly szint helyének megértéséhez.

Megnyitva: `2026-04-09`
