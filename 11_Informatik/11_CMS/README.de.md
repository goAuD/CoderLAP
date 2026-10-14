# CMS

## Schneller visueller Überblick

| Teil | Aufgabe |
|---|---|
| Admin-Oberfläche | Inhalte verwalten |
| Datenbank | Inhalte und Einstellungen speichern |
| Template / Theme | Darstellung |
| Plugin / Modul | Zusatzfunktionen |
| Rechteverwaltung | wer was bearbeiten darf |

## Was ist ein CMS?

Ein CMS ist ein Softwaresystem, das bei der zentralen Verwaltung von Inhalten hilft.

Das bedeutet, dass der Benutzer in der Regel:

- sich in eine Admin-Oberfläche einloggt
- eine neue Seite oder einen Beitrag erstellt
- ein Bild hochlädt
- den Text bearbeitet
- den Inhalt veröffentlicht

ohne den gesamten HTML-, CSS- oder Backend-Code händisch schreiben zu müssen.

## Wie funktioniert es?

In einem typischen CMS sind Inhalt und Darstellung teilweise voneinander getrennt.

### Inhalt

- Text
- Bilder
- Mediendateien
- Artikel
- Seiten

### Darstellung

- Template
- Theme
- Layout

### Funktionserweiterung

- Plugin
- Modul
- Erweiterung

## Warum ist es nützlich?

- schnellere Inhaltsverwaltung
- auch für Nicht-Entwickler nutzbar
- leichtere Aktualisierung
- mehrere Benutzer können zusammenarbeiten
- Berechtigungen sind verwaltbar
- auch bei größeren Seiten übersichtlicherer Betrieb

## Wo wird es eingesetzt?

Häufige Bereiche:

- Unternehmenswebseite
- Nachrichtenportal
- Blog
- Teil eines Webshop-Backends
- Intranet
- Bildungs- oder Informationsportal

## CMS und individuelle Entwicklung: nicht verwechseln

| Lösung | Vorteil | Nachteil |
|---|---|---|
| CMS | schneller Start, leichtere Inhaltsverwaltung | Anpassung an die Möglichkeiten des gewählten Systems |
| individuelle Entwicklung | gezielte Anpassbarkeit | gemeinsame Grundfunktionen müssen ebenfalls umgesetzt werden |

## Was muss man als Entwickler sehen?

Ein CMS ist keine "Wunderbox", sondern eine Plattform.

Als Entwickler arbeiten wir häufig mit:

- Template-Erstellung
- Plugin-Entwicklung
- Gestaltung von Datenstrukturen
- Feinabstimmung von Berechtigungen
- Verbesserung von SEO und Leistung
- Updates und Sicherheit

## Worauf muss man achten?

- Zu viele Plugins können Instabilität verursachen.
- Das CMS muss regelmäßig aktualisiert werden.
- Template und Inhalt sollten nicht zu eng gekoppelt sein.
- Die Rechteverwaltung darf nicht auf die leichte Schulter genommen werden.
- Nicht für jedes Projekt ist ein CMS die beste Wahl.

## Inhaltsmodell und redaktioneller Ablauf

Eine Schulnachricht kann die Felder `Titel`, `Einleitung`, `Text`, `Sprache`
und `Veröffentlichungsstatus` besitzen. Die Redaktion bearbeitet diese Inhalte.
Das Template bestimmt ihre Darstellung. Ein neues Design erfordert deshalb
nicht, jede Nachricht neu zu schreiben.

Ein möglicher Ablauf:

1. Die Autorin erstellt einen Entwurf und ergänzt ein Bild mit Textalternative.
2. Die Redaktion prüft Inhalt und Sprachfassung in der Vorschau.
3. Eine berechtigte Person veröffentlicht die Nachricht. Speichern und
   Veröffentlichen sind in diesem Ablauf unterschiedliche Schritte.
4. Bei späteren Änderungen lässt sich die frühere Fassung in der Versionshistorie
   nachvollziehen.

TYPO3 Workspaces bietet dafür beispielsweise Prüfungsstufen und Versionierung.
Redakteure benötigen keine Administratorrechte zur Installation von Erweiterungen.
Ein Backup berücksichtigt neben Inhalten auch Medien und die für eine
Wiederherstellung erforderlichen Einstellungen.

Ein herkömmliches CMS kann die Darstellung selbst übernehmen. Ein Headless-CMS
stellt Inhalte über eine API für getrennte Frontends bereit. Ein CMS kann auch
dateibasiert speichern; eine Datenbank ist Teil des oben gezeigten typischen
Aufbaus, aber keine zwingende Begriffsbedingung. Individuelle Entwicklung und
CMS können zusammenwirken, etwa in einem eigenen Modul.

## Prüfungstaugliche Formulierung

> CMS, also Content Management System, ist ein System,
> das die Erstellung, Bearbeitung, Speicherung
> und Veröffentlichung digitaler Inhalte ermöglicht.  
> Sein Vorteil ist,
> dass nicht nur Entwickler es nutzen können,
> und es gleichzeitig mit Templates, Modulen
> und Rechteverwaltung erweiterbar ist.  
> Typische Einsatzgebiete sind zum Beispiel Unternehmenswebseiten, Blogs und Portale.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe eines CMS?
2. Warum ist ein CMS vorteilhaft?
3. Welche typischen Bestandteile hat es?
4. Worin unterscheidet es sich von individueller Entwicklung?
5. Welches Risiko kann bei zu vielen Plugins entstehen?

## Kurzantworten zur Selbstkontrolle

1. Verwaltung und Veröffentlichung von Inhalten
2. Schneller und einfacher nutzbar
3. Admin-Oberfläche, Datenbank, Theme, Plugin, Rechteverwaltung
4. Bietet fertige Inhaltsverwaltung; besondere Anforderungen können Konfiguration oder Entwicklung benötigen
5. Instabilität und Sicherheitsprobleme

## Quellen

Geprüft: `2026-10-14`.

- [TYPO3: Workspaces](https://docs.typo3.org/c/typo3/cms-workspaces/main/en-us/): Versionierung und redaktionelle Freigabe.


1. MDN - CMS  
   https://developer.mozilla.org/en-US/docs/Glossary/CMS  
   Verwendung: kurze, klare technische Definition des CMS-Begriffs.

2. WordPress.com - What Is a Content Management System and How to Choose the Best CMS for Your Needs  
   https://wordpress.com/go/tutorials/what-is-a-cms/  
   Verwendung: praktische Erklärung, wie ein CMS funktioniert und welche Hauptbestandteile es hat.

3. Drupal.org - Drupal CMS  
   https://www.drupal.org/drupal-cms  
   Verwendung: offizielles, modernes Beispiel dafür, wie CMS als echte Plattform in der Praxis erscheint.

Abgerufen: `2026-04-08`
