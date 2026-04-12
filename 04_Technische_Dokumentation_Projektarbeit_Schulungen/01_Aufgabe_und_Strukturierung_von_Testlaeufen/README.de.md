# Aufgabe und Strukturierung von Testläufen

## Schneller visueller Überblick

| Element                | Was bedeutet es?                 |
| ---------------------- | -------------------------------- |
| Testziel               | was wollen wir überprüfen        |
| Testumgebung           | wo läuft der Test                |
| Testdaten              | womit führen wir den Test durch  |
| Testschritte           | was muss ausgeführt werden       |
| Erwartetes Ergebnis    | was gilt als korrektes Verhalten |
| Tatsächliches Ergebnis | was ist tatsächlich passiert     |
| Status                 | `pass`, `fail`, `blocked` usw.   |

## Was ist die Aufgabe eines Testlaufs?

Das Ziel eines Testlaufs ist:

- Fehler zu finden
- Anforderungen zu überprüfen
- die Funktion nachzuweisen
- die Qualität zu bewerten
- Entscheidungsunterstützung vor Freigabe oder Übergabe

Einfach gesagt:

- es reicht nicht zu sagen, dass „es funktioniert"
- das muss auf überprüfbare, dokumentierte Weise belegt werden

## Was muss für einen Testlauf vorbereitet werden?

### 1. Testziel

Zum Beispiel:

- Überprüfung der Login-Funktion
- Validierung der Suche
- Überprüfung der Datenbankverbindung

### 2. Testumgebung

Folgendes muss angegeben werden:

- Systemversion
- Gerät oder Plattform
- Browser
- Betriebssystem
- Datenbank
- Netzwerkbedingungen

### 3. Testdaten

Zum Beispiel:

- Testbenutzer
- Beispieldatenbank
- gültige und ungültige Daten

### 4. Testfälle und Schritte

Es muss genau festgehalten werden:

- was der Tester tut
- in welcher Reihenfolge
- mit welchen Eingaben

### 5. Erwartetes Ergebnis

Das gibt an:

- was als korrektes Verhalten gilt

## Wie sollte ein Testlauf strukturiert werden?

## 1. Identifikation

Es muss eindeutig sein:

- Name oder Kennung des Testlaufs
- Datum
- Verantwortliche Person
- Getestete Version

## 2. Ziel und Umfang

Es muss beschrieben werden:

- was getestet wird
- was nicht getestet wird
- was das Ziel des Tests ist

## 3. Voraussetzungen

Beispiele:

- Benutzer wurde angelegt
- Datenbank wurde geladen
- System läuft
- Netzwerk ist erreichbar

## 4. Testschritte

Diese sollten sein:

- in der richtigen Reihenfolge
- eindeutig
- wiederholbar

## 5. Ergebnisse und Status

Am Ende des Tests muss dokumentiert werden:

- tatsächliches Ergebnis
- `pass`
- `fail`
- `blocked`
- Anmerkungen
- Verweis auf Fehlerticket

## Typische Testlauf-Status

| Status         | Bedeutung                                             |
| -------------- | ----------------------------------------------------- |
| `ready to run` | bereit zur Ausführung                                 |
| `pass`         | erfolgreich                                           |
| `fail`         | fehlerhaftes Ergebnis                                 |
| `blocked`      | kann wegen eines Hindernisses nicht ausgeführt werden |
| `skipped`      | absichtlich übersprungen                              |

## Worauf muss man achten?

- das erwartete Ergebnis muss eindeutig sein
- die Testschritte müssen reproduzierbar sein
- die Umgebung muss dokumentiert sein
- die Ergebnisse müssen genau festgehalten werden
- bei Fehlern muss ein Nachweis oder Verweis vorhanden sein

## Beispiel für einen einfachen Testlauf

### Testziel

Überprüfung der Anmeldung mit korrekten Daten

### Voraussetzung

Testbenutzer existiert

### Testschritte

1. Öffne die Login-Seite.
2. Gib den Benutzernamen ein.
3. Gib das Passwort ein.
4. Klicke auf den Anmelden-Button.

### Erwartetes Ergebnis

Das System meldet den Benutzer an und das Dashboard wird angezeigt.

### Tatsächliches Ergebnis

Der Benutzer wurde angemeldet, Dashboard wurde angezeigt.

### Status

`pass`

## Prüfungstaugliche Formulierung

> Die Aufgabe eines Testlaufs besteht darin zu überprüfen,
> ob eine Funktion oder ein System den Anforderungen entsprechend funktioniert.  
> Ein gut strukturierter Testlauf enthält das Testziel,
> die Testumgebung, die Testdaten, die Testschritte,
> das erwartete Ergebnis, das tatsächliche Ergebnis und den Teststatus.  
> Die Dokumentation des Testlaufs ist wichtig für die Fehlerverfolgung,
> die Qualitätssicherung und für Entscheidungen vor der Übergabe.

## Häufige Prüfungsfehler

- Es gibt kein eindeutiges erwartetes Ergebnis.
- Die Testschritte sind zu vage.
- Die Umgebung ist nicht dokumentiert.
- Ein Fehler wird erkannt, aber nicht genau festgehalten.
- Die Status `blocked` und `fail` werden verwechselt.

## Schnelle Selbstkontrolle

1. Was ist das Ziel eines Testlaufs?
2. Was muss im erwarteten Ergebnis angegeben werden?
3. Warum ist es wichtig, die Testumgebung festzuhalten?
4. Was ist der Unterschied zwischen `fail` und `blocked`?
5. Welche Daten müssen bei einem Testlauf mindestens dokumentiert werden?

## Kurzantworten zur Selbstkontrolle

1. Überprüfung und Dokumentation der Funktion
2. Was als korrektes Verhalten gilt
3. Weil der Test dadurch wiederholbar und nachvollziehbar wird
4. `fail` = fehlerhaftes Ergebnis, `blocked` = der Test kann nicht ausgeführt werden
5. Ziel, Umgebung, Schritte, Testdaten, erwartetes und tatsächliches Ergebnis, Status

## Quellen

1. ISTQB CTFL Syllabus v3.1.1  
   https://istqb.org/wp-content/uploads/2024/11/ISTQB-CTFL_Syllabus_2018_v3.1.1.pdf  
   Verwendung: test execution, logging, expected vs actual result, test execution work products.

2. Azure DevOps Test Plans - Manage test runs  
   https://learn.microsoft.com/en-us/azure/devops/test/test-runs  
   Verwendung: modernes, offizielles Beispiel für den Begriff Test Run, Metadaten und Status.

3. Azure DevOps - Publish Test Results task  
   https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/test/publish-test-results  
   Verwendung: Dokumentation und Reporting von Testergebnissen in modernen Prozessen.

Abgerufen: `2026-04-08`
