# iOS Grundlagen

## Schneller visueller Überblick

| Merkmal      | iOS                                        |
| ------------ | ------------------------------------------ |
| Hersteller   | Apple                                      |
| Hauptgerät   | iPhone                                     |
| App-Vertrieb | App Store-zentriert                        |
| Erlebnis     | einheitlicher, kontrollierter              |
| Updates      | stärker zentral gesteuertes Apple-Modell   |
| Sicherheit   | starke Sandbox, Review, Plattformkontrolle |

## Was ist iOS?

iOS ist ein mobiles Betriebssystem, das von Apple entwickelt wird und auf iPhone-Geräten eingesetzt wird.

Seine Aufgabe:

- den Betrieb des Geräts steuern
- Apps ausführen
- die Benutzeroberfläche bereitstellen
- Sicherheits- und Datenschutzmechanismen verwalten

## Die wichtigsten Merkmale von iOS

## 1. Enge Hardware-Software-Integration

Apple setzt auf eigene Hardware und eigene Software.

Das kann Vorteile bieten bei:

- Leistung
- Optimierung
- Stabilität
- Benutzererlebnis

## 2. Einheitlicheres Ökosystem

Da Apple kontrolliert:

- die Geräte
- das Betriebssystem
- den Hauptvertriebskanal für Apps

ist die iOS-Welt typischerweise einheitlicher.

## 3. App-Store-Zentrierung

Im iOS-Ökosystem nimmt der **App Store** eine zentrale Rolle ein.

Das bedeutet:

- die Verfügbarkeit von Apps ist stark plattformreguliert
- Überprüfung und Review werden betont

## 4. Sicherheit und Datenschutz

Apple betont stark:

- das Sandbox-Modell
- die Berechtigungsverwaltung
- die Privacy-Kontrollen
- die Sichtbarkeit des Datenschutzes für den Nutzer

## 5. Benutzererlebnis

Eines der wichtigen Kennzeichen von iOS:

- konsistentere Benutzeroberfläche
- einheitlicheres Design
- vorhersehbareres Systemerlebnis

## Wofür wird iOS verwendet?

- Telefonieren
- Nachrichtenversand
- Web
- Kamera
- Navigation
- Bezahlung
- Gesundheit und Fitness
- Produktivität
- kreative und alltägliche App-Nutzung

## Vorteile von iOS

- einheitlicheres Ökosystem
- stabiler und optimierter Betrieb
- starke Kontrolle auf Plattformebene
- betonter Datenschutz- und Sicherheitsansatz
- gute Integration zwischen Apple-Geräten

## Einschränkungen oder Kompromisse von iOS

- weniger Freiheit über die Plattform
- geschlosseneres App-Vertriebsmodell
- weniger Anpassungsmöglichkeiten in bestimmten Bereichen
- stärkere Herstellerkontrolle

## iOS vs Android

| iOS                                   | Android                                          |
| ------------------------------------- | ------------------------------------------------ |
| Apple-zentriertes Ökosystem           | viele Hersteller, offenere Basis                 |
| kontrollierterer Vertrieb             | flexiblerer Vertrieb                             |
| einheitlicheres Erlebnis              | vielfältigere Geräte- und Oberflächen-Landschaft |
| enge Hardware-Software-Zusammenarbeit | größere Plattformstreuung                        |

## Durchgearbeiteter Fall: Zugriffe einer Anwendung

Eine Lernanwendung benötigt ein Profilbild. Kann über die Bildauswahl des Systems ein einzelnes Foto ausgewählt werden, ist nicht unbedingt der Zugriff auf die ganze Mediathek erforderlich. Die Sandbox trennt die eigenen App-Daten; auf andere Daten wird über bereitgestellte Systemfunktionen und deren Regeln zugegriffen.

Beim Wartungstest werden OS-Updates, App-Berechtigungen und eine wiederherstellbare Sicherung geprüft. Synchronisation und Backup sind unterschiedliche Funktionen: Die Synchronisation kann eine Löschung auch auf andere Geräte übertragen. Die Prüfung im App Store ersetzt ebenfalls nicht das Verständnis des App-Zwecks und der Datenverarbeitung.

**Vertrieb, Stand 2026-10-14:** Der App Store ist ein wichtiger zentraler Kanal. In der EU sind unter bestimmten Voraussetzungen aber auch alternative Marktplätze und Webvertrieb verfügbar. Die konkreten Möglichkeiten werden anhand der aktuellen Regions- und Systemanforderungen geprüft.

## Prüfungstaugliche Formulierung

> iOS ist das mobile Betriebssystem von Apple für das iPhone.  
> Charakteristisch sind die enge Hardware-Software-Integration,
> der App-Store-zentrierte Anwendungsvertrieb,
> das einheitlichere Benutzererlebnis
> und das starke Sicherheits- und Datenschutzmodell.  
> In der heutigen Apple-Plattformbenennung heißt das System des iPhone iOS, während das des iPad iPadOS heißt.

## Schnelle Selbstkontrolle

1. Was ist iOS?
2. An welches Gerät ist es primär gebunden?
3. Welche Rolle spielt der App Store im iOS-Ökosystem?
4. Was ist einer der wichtigen Vorteile von iOS?
5. Was ist heute der Unterschied zwischen der Bezeichnung iOS und iPadOS?

## Kurzantworten zur Selbstkontrolle

1. Das mobile Betriebssystem von Apple für das iPhone
2. An das iPhone
3. Zentraler Kanal für App-Vertrieb und Überprüfung
4. Einheitlicheres Erlebnis, starke Integration, Sicherheitskontrolle
5. Auf dem iPhone heißt es iOS, auf dem iPad iPadOS als offizieller Plattformname

## Quellen

1. Apple - OS Overview  
   https://www.apple.com/os/  
   Verwendung: Aktuelle Apple-Plattformbezeichnungen und die Trennung von iOS / iPadOS.

2. Apple Support - iPhone User Guide  
   https://support.apple.com/guide/iphone/welcome/ios  
   Verwendung: Offizielle Übersicht der iOS-Funktionen und des iPhone-Systems.

3. Apple - iOS and iPadOS Deployment Overview  
   https://www.apple.com/in/business/docs/site/iOS_and_iPadOS_Deployment_Overview.pdf  
   Verwendung: Plattformübersicht von iOS / iPadOS aus Unternehmens- und technischer Perspektive.

4. Apple Developer - App Review Guidelines  
   https://developer.apple.com/appstore/resources/approval/guidelines.html  
   Verwendung: App Store Review, Plattformkontrolle, Sicherheits- und Qualitätsregulierung.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Apple: Runtime security](https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web): Sandbox und geregelter Datenzugriff.
- [Apple: Alternative app distribution](https://support.apple.com/en-us/118110): alternative Vertriebswege in der EU.

Geprüft: `2026-10-14`.
