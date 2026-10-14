# Systemprogramm und Anwendungsprogramm

## Gyors vizuális kép

| Típus             | Mire való?                      | Példa                             |
| ----------------- | ------------------------------- | --------------------------------- |
| rendszerprogram   | a rendszer működését biztosítja | operációs rendszer, driver, shell |
| alkalmazásprogram | a felhasználó feladatát végzi   | Word, Chrome, Photoshop           |

## Mi az a rendszerprogram?

Olyan program, amely a számítógép alapvető működéséhez szükséges, vagy azt támogatja.

Ide sorolható például:

- operációs rendszer
- eszközmeghajtó (`driver`)
- parancsértelmező / shell
- rendszereszközök
- segédprogramok (`utilities`)

Fő jellemzői:

- közel áll a rendszerhez
- a hardver és az alkalmazások között is szerepe lehet
- nem feltétlenül közvetlen felhasználói munkaeszköz

## Mi az az alkalmazásprogram?

Olyan program, amely egy konkrét felhasználói célt szolgál.

Példák:

- szövegszerkesztő
- webböngésző
- média-lejátszó
- grafikai program
- csevegőalkalmazás
- könyvelőprogram

Fő jellemzői:

- a felhasználó valamilyen konkrét feladatát oldja meg
- az operációs rendszer szolgáltatásaira támaszkodik

## A két fogalom közti különbség

| Szempont         | Rendszerprogram                             | Alkalmazásprogram              |
| ---------------- | ------------------------------------------- | ------------------------------ |
| fő cél           | a rendszer működtetése / támogatása         | felhasználói feladat megoldása |
| hardverközelség  | általában közelebb áll a hardverhez         | távolabb áll a hardvertől      |
| függés az OS-től | része lehet vagy szorosan kapcsolódik hozzá | az OS-en fut                   |
| példa            | Windows, driver, PowerShell                 | Excel, Firefox, VLC            |

## Tipikus rendszerprogramok

### 1. Operációs rendszer

Példa:

- Windows
- macOS
- Linux

### 2. Illesztőprogramok

Feladatuk:

- az operációs rendszer és a hardver közti kapcsolat

### 3. Shell / parancsértelmező

Példa:

- PowerShell
- Bash

### 4. Segédprogramok

Példa:

- lemezkezelő
- biztonsági mentő eszköz
- rendszerfigyelő

## Tipikus alkalmazásprogramok

- Microsoft Word
- Google Chrome
- Mozilla Firefox
- VLC Media Player
- Adobe Photoshop
- Visual Studio Code

## Határterületek

Nem mindig éles a határ.

Például:

- egy vírusirtó részben rendszerközeli
- egy fájlkezelő lehet rendszerhez kötődő, de felhasználói eszköz is
- egy terminálalkalmazás alkalmazásként fut, de rendszerközeli feladatokra is használható

Vizsgán viszont az alapelv a fontos:

- rendszerprogram = a rendszer működéséhez kapcsolódik
- alkalmazásprogram = felhasználói feladatot old meg

## Kidolgozott eset: mi kell a nyomtatáshoz?

Egy PDF-olvasóban megnyomjuk a Nyomtatás gombot. A PDF-olvasó alkalmazásprogram: a dokumentum megjelenítése és a felhasználói feladat tartozik hozzá. Az OS nyomtatási szolgáltatása a feladat sorba állítását végzi, a meghajtó pedig az adott eszközzel való együttműködést támogatja. A nyomtató saját firmware-e vezérli a készüléket.

Így egy problémát szerepkör szerint szűkíthetünk: minden alkalmazásból sikertelen a nyomtatás, vagy csak egy dokumentumnál? A feladat bekerül a sorba? Elérhető az eszköz? Ez célzottabb, mint minden komponenst újratelepíteni.

A rendszerprogram besorolás a **feladatot** írja le. Nem jelenti automatikusan azt, hogy a program kernel módban vagy rendszergazdai joggal fut. A shell rendszerközeli eszköz, de normál felhasználói fiókkal is használható.

## Vizsgán jól használható megfogalmazás

> A rendszerprogram a számítógép alapműködését biztosító vagy támogató
> szoftver, például az operációs rendszer, az illesztőprogramok
> vagy a shell.  
> Az alkalmazásprogram ezzel szemben konkrét felhasználói feladatot végez,
> például szövegszerkesztést, böngészést vagy médialejátszást.  
> Az alkalmazásprogramok az operációs rendszer szolgáltatásait használják.

## Gyors önellenőrzés

1. Mi a rendszerprogram fő feladata?
2. Mi az alkalmazásprogram fő feladata?
3. Mondj két példát rendszerprogramra.
4. Mondj két példát alkalmazásprogramra.
5. Miért függ az alkalmazásprogram az operációs rendszertől?

## Rövid válaszok az önellenőrzéshez

1. A rendszer működését biztosítja vagy támogatja
2. Konkrét felhasználói feladatot old meg
3. Operációs rendszer, driver, shell
4. Böngésző, szövegszerkesztő, médialejátszó
5. Mert az OS szolgáltatásait használja

## Források

1. NIST CSRC Glossary - application  
   https://csrc.nist.gov/glossary/term/application  
   Használat: az alkalmazás mint futtatható szoftver fogalma.

2. NIST CSRC Glossary - Operating system  
   https://csrc.nist.gov/glossary/term/operating_system_  
   Használat: az operációs rendszer mint rendszer-szoftver háttéralapja.

3. Microsoft Learn - PowerShell Documentation  
   https://learn.microsoft.com/en-us/powershell/  
   Használat: shell és rendszereszköz mint rendszerközeli szoftverpélda.

4. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Használat: rendszerfunkciók és az alkalmazások OS-függő működésének kontextusa.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [Microsoft: User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode): védelmi szintek és elkülönítés.

Ellenőrizve: `2026-10-14`.
