# Powershell Grundlagen

## Lényeg 30 másodpercben

A **PowerShell** a Microsoft parancssori shellje és automatizálási környezete.

Fő jellemzői:

- parancssoros használat
- objektum-alapú működés
- adminisztrációra és automatizálásra is alkalmas
- Windows mellett Linuxon és macOS-en is elérhető

Vizsgán legalább az alapötletet és néhány egyszerű parancsot tudni kell.

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| shell | parancsértelmező környezet |
| cmdlet | PowerShell-parancs |
| objektum-alapú | nem csak sima szöveget, hanem objektumokat kezel |
| script | parancsokból álló `.ps1` fájl |

## Mi az a PowerShell?

A PowerShell egy modern parancssori környezet és szkriptnyelv.

Használható:

- rendszeradminisztrációra
- fájlkezelésre
- folyamatkezelésre
- információlekérdezésre
- automatizálásra

## Miért különleges?

Sok hagyományos shell főleg szöveggel dolgozik.  
A PowerShell ezzel szemben **objektumokat** kezel.

Ez azért hasznos, mert:

- strukturáltabb az adatkezelés
- könnyebb szűrni, rendezni, feldolgozni

## Cmdlet névadás

A PowerShell-parancsok tipikus formája:

- `Ige-Főnév`

Példák:

- `Get-Help`
- `Get-Command`
- `Get-ChildItem`
- `Set-Location`
- `Copy-Item`

## Fontos alapparancsok

### Segítség és parancskeresés

| Parancs | Mire jó? |
|---|---|
| `Get-Help` | súgó megjelenítése |
| `Get-Command` | elérhető parancsok keresése |

Példák:

```powershell
Get-Help Get-ChildItem
Get-Command *Item*
```

### Hely és navigáció

| Parancs | Mire jó? |
|---|---|
| `Get-Location` | aktuális hely megjelenítése |
| `Set-Location` | mappaváltás |

Példák:

```powershell
Get-Location
Set-Location C:\DEV_SCHOOL
```

### Fájlok és mappák listázása

| Parancs | Mire jó? |
|---|---|
| `Get-ChildItem` | fájlok és mappák listázása |

Példák:

```powershell
Get-ChildItem
Get-ChildItem -Force
Get-ChildItem -Recurse
```

### Létrehozás, másolás, mozgatás, törlés

| Parancs | Mire jó? |
|---|---|
| `New-Item` | új elem létrehozása |
| `Copy-Item` | másolás |
| `Move-Item` | mozgatás / átnevezés |
| `Remove-Item` | törlés |

Példák:

```powershell
New-Item -ItemType Directory -Path .\Teszt
Copy-Item .\a.txt .\backup\a.txt
Move-Item .\a.txt .\b.txt
Remove-Item .\b.txt
```

### Tartalom megjelenítése

| Parancs | Mire jó? |
|---|---|
| `Get-Content` | fájl tartalmának kiírása |

Példa:

```powershell
Get-Content .\jegyzet.txt
```

## Hasznos aliasok

PowerShellben gyakori rövid aliasok:

| Alias | Eredeti parancs |
|---|---|
| `ls` | `Get-ChildItem` |
| `dir` | `Get-ChildItem` |
| `cd` | `Set-Location` |
| `cat` | `Get-Content` |

Fontos:

- vizsgán jobb az eredeti cmdlet-neveket ismerni

## Mire használják a gyakorlatban?

- fájlkezelés
- rendszerinformáció lekérdezés
- automatizált adminisztráció
- szkriptek futtatása
- szerver- és kliensgépek kezelése

## Vizsgán jól használható megfogalmazás

> A PowerShell a Microsoft objektum-alapú parancssori shellje és automatizálási környezete.  
> Cmdleteket használ, amelyek jellemzően ige-főnév formában vannak elnevezve, például `Get-Help` vagy `Get-ChildItem`.  
> Használható fájlkezelésre, információlekérdezésre és adminisztrációs feladatok automatizálására.

## Gyakori vizsgahibák

- A PowerShellt a régi `cmd`-vel teljesen azonosnak venni.
- Nem tudni legalább 4-5 alapparancsot.
- Csak az aliasokat ismerni, a cmdlet-neveket nem.
- Nem tudni, mire való a `Get-Help`.
- Elfelejteni, hogy PowerShell objektum-alapú.

## Gyors önellenőrzés

1. Mi a PowerShell?
2. Mit csinál a `Get-Help`?
3. Mit csinál a `Get-Command`?
4. Mit csinál a `Get-ChildItem`?
5. Melyik parancs vált mappát?
6. Mit jelent az, hogy a PowerShell objektum-alapú?

## Rövid válaszok az önellenőrzéshez

1. Microsoft shell és automatizálási környezet
2. Súgót jelenít meg
3. Parancsokat keres / listáz
4. Fájlokat és mappákat listáz
5. `Set-Location`
6. Nem csak sima szöveggel, hanem strukturált objektumokkal dolgozik

## Források

1. Microsoft Learn - PowerShell Documentation  
   https://learn.microsoft.com/en-us/powershell/  
   Használat: hivatalos PowerShell alapdokumentáció.

2. Microsoft Learn - Get-Help  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help?view=powershell-7.6  
   Használat: a súgórendszer alapja.

3. Microsoft Learn - Get-Command  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.6  
   Használat: parancskeresés és cmdlet-felfedezés.

4. Microsoft Learn - Get-ChildItem  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.6  
   Használat: listázás fájlrendszerben és más providereknél.

5. Microsoft Learn - Set-Location  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-location?view=powershell-7.6  
   Használat: mappaváltás és aktuális hely kezelése.

6. Microsoft Learn - Copy-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.6  
   Használat: egyszerű fájl- és mappamásolás.

7. Microsoft Learn - Remove-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.6  
   Használat: elemek törlése.

Megnyitva: `2026-04-08`
