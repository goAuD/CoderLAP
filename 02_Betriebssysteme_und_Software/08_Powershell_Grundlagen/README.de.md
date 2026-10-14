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

Häufige PowerShell-Aliase unter Windows; auf anderen Plattformen kann die Verfügbarkeit abweichen:

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

## Ausführbares Beispiel: Objekte filtern und sortieren

Aufgabe: Aus einer erfundenen Datenträgerliste werden die Volumes mit weniger als 10 GiB freiem Platz nach Namen ausgegeben. Das Beispiel funktioniert in PowerShell 5.1 und 7 und arbeitet nur im Arbeitsspeicher.

```powershell
$volumes = @(
    [pscustomobject]@{ Name = 'DATA'; FreeGiB = 18 }
    [pscustomobject]@{ Name = 'CACHE'; FreeGiB = 4 }
    [pscustomobject]@{ Name = 'BACKUP'; FreeGiB = 8 }
)
$volumes |
    Where-Object { $_.FreeGiB -lt 10 } |
    Sort-Object Name |
    ForEach-Object { '{0}: {1} GiB' -f $_.Name, $_.FreeGiB }
```

Erwartete Ausgabe:

```text
BACKUP: 8 GiB
CACHE: 4 GiB
```

`|` reicht Objekte weiter, `$_` bezeichnet das gerade bearbeitete Objekt. Der Filter vergleicht Zahlenwerte, die Sortierung verwendet die Eigenschaft `Name`. Erst im letzten Schritt entsteht Text. Externe Kommandozeilenprogramme liefern dagegen häufig Textausgabe.

Windows PowerShell 5.1 und die plattformübergreifende PowerShell 7 sind getrennte Ausgaben. `Get-Command ls` zeigt die tatsächliche Auflösung des Alias. Die früheren Dateibefehle sind illustrative Ausschnitte und setzen vorhandene Dateien und Verzeichnisse voraus. Vor Änderungen hilft bei unterstützten Befehlen `-WhatIf`, die beabsichtigte Aktion zu prüfen.

## Prüfungstaugliche Formulierung

> PowerShell ist die objektbasierte Kommandozeilen-Shell und Automatisierungsumgebung von Microsoft.  
> Es verwendet Cmdlets,
> die typischerweise in der Form Verb-Nomen benannt sind,
> zum Beispiel `Get-Help` oder `Get-ChildItem`.  
> Es kann für Dateiverwaltung, Informationsabfragen und Automatisierung administrativer Aufgaben verwendet werden.

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

### Geprüfte Quellen zur Ergänzung

- [Microsoft: about_Pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines): Objekte in der Pipeline.

Geprüft: `2026-10-14`.
