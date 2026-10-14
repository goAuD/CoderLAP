# Assembler

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

## Regiszter, utasítás és objektumfájl

Az alábbi **szemléltető részlet** x86 Intel-szintaxist használ. Nem teljes
program, hiányzik a belépési pont és az operációs rendszerhez tartozó lezárás.

```asm
mov eax, 7
add eax, 5
```

Az `eax` egy 32 bites regiszter. Az első utasítás 7-et tölt bele, a második
hozzáad 5-öt, így a regiszter értéke 12. Ez önmagában nem ír ki semmit a
képernyőre. Intel-szintaxisban a céloperandus van elöl; más szintaxis más
sorrendet is használhat, ezért mindig megnevezzük az architektúrát és a jelölést.

Az assembler az utasításokat kódolja, és általában objektumfájlt készít. A linker
kapcsolja össze a külön fordított részeket. A regiszternevek és utasítások nem
vihetők át változtatás nélkül ARM processzorra. Magas szintű nyelvnél ezt a
célarchitektúrához igazítást nagyrészt a fordító végzi. A kézzel írt assembly
teljesítményelőnyét mérni kell; a modern fordító is végez optimalizálásokat.

## Vizsgán jól használható megfogalmazás

> Az assembler egyrészt egy alacsony szintű programnyelvhez kapcsolódó fogalom, másrészt az a fordítóeszköz, amely az  
> assembly utasításokat gépközeli kóddá alakítja.  
> Az assembly nyelv közel áll a processzor utasításkészletéhez, ezért hardverfüggőbb és nehezebben kezelhető, mint a  
> magas szintű programozási nyelvek.  
> Előnye a pontos vezérlés, hátránya a bonyolultság és a gyengébb hordozhatóság.

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

Ellenőrizve: `2026-10-14`.

- [GNU as: x86 syntax](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html): Intel/AT&T szintaxis és architektúrafüggés.


1. GNU Binutils - Using as  
   https://sourceware.org/binutils/docs/as/  
   Használat: hivatalos elsődleges forrás a GNU assembler működéséhez.

2. GCC - Overall Options  
   https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html  
   Használat: kiegészítő háttér a fordítási folyamat és az assembly szint helyének megértéséhez.

Megnyitva: `2026-04-09`
