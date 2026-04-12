# Powershell Grundlagen

## Schneller visueller Überblick

| Begriff       | Bedeutung                                          |
| ------------- | -------------------------------------------------- |
| Shell         | Kommandointerpreter-Umgebung                       |
| Cmdlet        | PowerShell-Befehl                                  |
| Objektbasiert | verarbeitet nicht nur reinen Text, sondern Objekte |
| Script        | aus Befehlen bestehende `.ps1`-Datei               |

## Was ist PowerShell?

PowerShell ist eine moderne Kommandozeilenumgebung und Skriptsprache.

Verwendbar für:

- Systemadministration
- Dateiverwaltung
- Prozessverwaltung
- Informationsabfragen
- Automatisierung

## Warum ist es besonders?

Viele herkömmliche Shells arbeiten hauptsächlich mit Text.  
PowerShell hingegen verarbeitet **Objekte**.

Das ist nützlich, weil:

- die Datenverarbeitung strukturierter ist
- Filtern, Sortieren und Verarbeiten leichter fallen

## Cmdlet-Namensgebung

Die typische Form von PowerShell-Befehlen:

- `Verb-Nomen`

Beispiele:

- `Get-Help`
- `Get-Command`
- `Get-ChildItem`
- `Set-Location`
- `Copy-Item`

## Wichtige Grundbefehle

### Hilfe und Befehlssuche

| Befehl        | Wofür?                    |
| ------------- | ------------------------- |
| `Get-Help`    | Hilfe anzeigen            |
| `Get-Command` | verfügbare Befehle suchen |

Beispiele:

```powershell
Get-Help Get-ChildItem
Get-Command *Item*
```

### Ort und Navigation

| Befehl         | Wofür?                 |
| -------------- | ---------------------- |
| `Get-Location` | aktuellen Ort anzeigen |
| `Set-Location` | Ordner wechseln        |

Beispiele:

```powershell
Get-Location
Set-Location C:\DEV_SCHOOL
```

### Dateien und Ordner auflisten

| Befehl          | Wofür?                       |
| --------------- | ---------------------------- |
| `Get-ChildItem` | Dateien und Ordner auflisten |

Beispiele:

```powershell
Get-ChildItem
Get-ChildItem -Force
Get-ChildItem -Recurse
```

### Erstellen, Kopieren, Verschieben, Löschen

| Befehl        | Wofür?                   |
| ------------- | ------------------------ |
| `New-Item`    | neues Element erstellen  |
| `Copy-Item`   | Kopieren                 |
| `Move-Item`   | Verschieben / Umbenennen |
| `Remove-Item` | Löschen                  |

Beispiele:

```powershell
New-Item -ItemType Directory -Path .\Teszt
Copy-Item .\a.txt .\backup\a.txt
Move-Item .\a.txt .\b.txt
Remove-Item .\b.txt
```

### Inhalt anzeigen

| Befehl        | Wofür?               |
| ------------- | -------------------- |
| `Get-Content` | Dateiinhalt ausgeben |

Beispiel:

```powershell
Get-Content .\jegyzet.txt
```

## Nützliche Aliase

In PowerShell häufige Kurzaliase:

| Alias | Originalbefehl  |
| ----- | --------------- |
| `ls`  | `Get-ChildItem` |
| `dir` | `Get-ChildItem` |
| `cd`  | `Set-Location`  |
| `cat` | `Get-Content`   |

Wichtig:

- in der Prüfung ist es besser, die originalen Cmdlet-Namen zu kennen

## Wofür wird es in der Praxis verwendet?

- Dateiverwaltung
- Abfrage von Systeminformationen
- automatisierte Administration
- Ausführung von Skripten
- Verwaltung von Server- und Client-Rechnern

## Prüfungstaugliche Formulierung

> PowerShell ist die objektbasierte Kommandozeilen-Shell und Automatisierungsumgebung von Microsoft.  
> Es verwendet Cmdlets,
> die typischerweise in der Form Verb-Nomen benannt sind,
> zum Beispiel `Get-Help` oder `Get-ChildItem`.  
> Es kann für Dateiverwaltung, Informationsabfragen und Automatisierung administrativer Aufgaben verwendet werden.

## Häufige Prüfungsfehler

- PowerShell mit dem alten `cmd` als völlig identisch betrachten.
- Nicht mindestens 4-5 Grundbefehle kennen.
- Nur die Aliase kennen, nicht die Cmdlet-Namen.
- Nicht wissen, wofür `Get-Help` da ist.
- Vergessen, dass PowerShell objektbasiert ist.

## Schnelle Selbstkontrolle

1. Was ist PowerShell?
2. Was macht `Get-Help`?
3. Was macht `Get-Command`?
4. Was macht `Get-ChildItem`?
5. Welcher Befehl wechselt den Ordner?
6. Was bedeutet es, dass PowerShell objektbasiert ist?

## Kurzantworten zur Selbstkontrolle

1. Microsoft-Shell und Automatisierungsumgebung
2. Zeigt die Hilfe an
3. Sucht / listet Befehle auf
4. Listet Dateien und Ordner auf
5. `Set-Location`
6. Es arbeitet nicht nur mit reinem Text, sondern mit strukturierten Objekten

## Quellen

1. Microsoft Learn - PowerShell Documentation  
   https://learn.microsoft.com/en-us/powershell/  
   Verwendung: offizielle PowerShell-Grundlagendokumentation.

2. Microsoft Learn - Get-Help  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help?view=powershell-7.6  
   Verwendung: Grundlage des Hilfesystems.

3. Microsoft Learn - Get-Command  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.6  
   Verwendung: Befehlssuche und Cmdlet-Erkennung.

4. Microsoft Learn - Get-ChildItem  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.6  
   Verwendung: Auflistung im Dateisystem und bei anderen Providern.

5. Microsoft Learn - Set-Location  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-location?view=powershell-7.6  
   Verwendung: Ordnerwechsel und Verwaltung des aktuellen Orts.

6. Microsoft Learn - Copy-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.6  
   Verwendung: einfaches Kopieren von Dateien und Ordnern.

7. Microsoft Learn - Remove-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.6  
   Verwendung: Löschen von Elementen.

Abgerufen: `2026-04-08`
