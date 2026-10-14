# CMS

## Schneller visueller Überblick

| Element | Rolle |
|---|---|
| Admin-Oberfläche | Verwaltung von Inhalten |
| Datenbank | Speicherung von Inhalten, Benutzern, Einstellungen |
| Theme / Vorlage | Darstellung |
| Plugin / Modul | Funktionserweiterung |

## Was ist ein CMS?

Das Ziel eines `CMS` ist, dass die Inhaltsverwaltung:

- nicht nur für Entwickler möglich ist
- strukturiert erfolgt
- mehrere Benutzer gemeinsam arbeiten können

Typische Aufgaben:

- Verwaltung von Seiten und Artikeln
- Verwaltung von Mediendateien
- Berechtigungsverwaltung
- Veröffentlichung
- Verwaltung von Kategorien und Metadaten

## Was hat das mit Datenbanken zu tun?

Ein typisches `CMS` speichert viele Daten in einer Datenbank:

- Inhalte von Artikeln und Seiten
- Benutzer
- Rollen
- Menüs
- Einstellungen
- Plugin- oder Moduldaten

Das heißt, ein `CMS` ist häufig ein **auf einer Datenbank basierendes Anwendungssystem**.

## Warum ist es wichtig, das hier zu kennen?

Weil es ein gutes Beispiel dafür ist, wie zusammenspielen:

- Datenmodell
- Datenbank
- Anwendungslogik
- Benutzeroberfläche

## `CMS` und `DBMS` - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| `CMS` | Inhaltsverwaltungsanwendung |
| `DBMS` | Datenbankverwaltungssoftware |

Ein `CMS` verwendet häufig ein `DBMS` im Hintergrund.

## Praktische Beispiele

- `WordPress`
- `Drupal`
- `Joomla`

## Durchgearbeiteter Ablauf: Lernmaterial veröffentlichen

Eine Redaktion erstellt einen Artikel in der Administrationsoberfläche des CMS, prüft den Entwurf in der Vorschau und lässt ihn von einer berechtigten Person freigeben. Danach wird veröffentlicht. Besucher sehen im Frontend die freigegebene Fassung. Ob frühere Versionen wiederhergestellt oder Veröffentlichungszeiten geplant werden können, ist am konkreten CMS zu prüfen.

Auch **TYPO3** ist ein CMS. Das Backend dient Redaktion und Administration, das Frontend ist die für Besucher sichtbare Website. Ein Theme gestaltet die Darstellung, eine Erweiterung ergänzt Funktionen. Beides ist vom gespeicherten Inhalt zu unterscheiden.

Für den Betrieb können neben dem Datenbank-Dump auch hochgeladene Bilder, Konfiguration und passende Code-/Erweiterungsversionen erforderlich sein. Eine erfolgreich eingespielte Datenbank beweist noch nicht, dass Bilder und Website funktionieren. Prüfe bei der Abnahme Erstellung, Berechtigungen, Veröffentlichung und Wiederherstellung eines Inhalts.

Es gibt auch dateibasierte CMS und CMS mit statischer Ausgabe. Ein eigener Datenbankserver ist daher keine Voraussetzung für den CMS-Begriff.

## Prüfungstaugliche Formulierung

> Ein `CMS`, also Content Management System, ist ein Anwendungssystem, das die Erstellung, Bearbeitung, Speicherung  
> und Veröffentlichung digitaler Inhalte unterstützt.  
> Im Hintergrund verwendet es in vielen Fällen eine Datenbank zur Verwaltung von Inhalten, Benutzern, Berechtigungen  
> und Einstellungen.  
> Daher ist ein `CMS` ein gutes Beispiel dafür, wie eine Anwendung eine Datenbank zur Verwaltung strukturierter
> Informationen nutzt.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel eines `CMS`?
2. Warum hängt es mit Datenbanken zusammen?
3. Was ist der Unterschied zwischen `CMS` und `DBMS`?
4. Nenne zwei typische `CMS`.
5. Welche Daten kann es im Hintergrund speichern?

## Kurzantworten zur Selbstkontrolle

1. Verwaltung und Veröffentlichung von Inhalten
2. Weil es die Daten häufig in einer Datenbank speichert
3. Das eine ist eine Anwendung, das andere eine Datenbankverwaltungssoftware
4. WordPress, Drupal
5. Inhalte, Benutzer, Berechtigungen, Einstellungen

## Quellen

1. MDN - CMS  
   https://developer.mozilla.org/en-US/docs/Glossary/CMS  
   Verwendung: kurze, klare technische Definition des CMS-Begriffs.

2. Drupal.org - Drupal CMS  
   https://new.drupal.org/drupal-cms  
   Verwendung: offizielles, modernes Beispiel dafür, wie ein CMS als echte Plattform funktioniert.

3. WordPress.com - What Is a CMS?  
   https://wordpress.com/go/tutorials/what-is-a-cms/  
   Verwendung: praktische Erklärung zu den Hauptbestandteilen und der Funktionsweise eines CMS.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [TYPO3: Concepts](https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Concepts/Index.html): Backend/Frontend und CMS-Struktur
- [MDN: CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS): Begriff der Inhaltsverwaltung

Geprüft: `2026-10-14`.
