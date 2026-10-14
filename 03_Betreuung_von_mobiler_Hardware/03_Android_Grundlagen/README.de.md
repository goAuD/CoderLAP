# Android Grundlagen

## Schneller visueller Überblick

| Merkmal        | Android                                     |
| -------------- | ------------------------------------------- |
| Plattformbasis | `AOSP`                                      |
| Geräte         | viele Hersteller, viele Modelle             |
| App-Vertrieb   | Google Play und auch andere Quellen möglich |
| Anpassbarkeit  | im Allgemeinen größer                       |
| Updates        | können von Hersteller und Modell abhängen   |

## Was ist Android?

Android ist eine mobile Betriebssystem-Plattform, die auf:

- Telefonen
- Tablets
- anderen Smart-Geräten

verwendet wird.

Der Name des zugrunde liegenden Open-Source-Projekts ist:

- **AOSP** (`Android Open Source Project`)

Das ist wichtig, weil Android nicht nur an ein einzelnes Gerät oder eine einzelne Hardwarefamilie gebunden ist.

## Die wichtigsten Merkmale von Android

## 1. Open-Source-Basis

Die Grundlage von Android ist Open Source.

Das bedeutet:

- die Plattformbasis ist öffentlich zugänglich
- Hersteller können sie anpassen
- es können viele verschiedene Geräte dafür hergestellt werden

## 2. Vielfalt an Geräten

Android läuft auf:

- Einstiegstelefonen
- High-End-Telefonen
- Tablets
- faltbaren Geräten

Das ist ein großer Vorteil, bedeutet aber auch Vielfalt und Unterschiede.

## 3. App-Ökosystem

Android-Apps sind typischerweise:

- auch aus einem `AAB`-Veröffentlichungspaket verteilt werden; auf dem Gerät werden `APK`-Pakete installiert
- am häufigsten über **Google Play** für den Nutzer erhältlich

In der Android-Welt können aber auch andere Vertriebswege existieren.

## 4. Berechtigungen und Sicherheit

Bei Android spielen eine wichtige Rolle:

- App-Berechtigungen
- Isolierung von Anwendungen
- Plattformsicherheit
- Schutzmechanismen wie Play Protect

## 5. Anpassbarkeit

Einer der häufig genannten Vorteile von Android:

- viele Hersteller können eigene Oberflächen, Einstellungen und Funktionen hinzufügen

Beispiele:

- Launcher
- Widgets
- herstellerspezifische Benutzeroberfläche
- unterschiedliche System-Apps

## Android in der Praxis

Android kann verwendet werden für:

- Telefonieren
- Nachrichtenversand
- Surfen
- Navigation
- App-Ausführung
- Bezahlung
- Fotografieren
- auch berufliche Nutzung

## Vorteile von Android

- große Geräteauswahl
- breite Preisspanne
- flexibleres Ökosystem
- größere Anpassbarkeit
- wird von vielen Herstellern unterstützt

## Herausforderungen von Android

- Unterschiede zwischen Geräten und Herstellern
- unterschiedliche Update-Politik
- größere Fragmentierung
- das Benutzererlebnis ist nicht immer vollständig einheitlich

## Wichtige Begriffe

### AOSP

Das Open-Source-Basisprojekt von Android.

### Google Play

Der wichtigste Android-App-Marktplatz.

### Sideload / externe Installation

Unter Android ist es unter bestimmten Bedingungen möglich, Apps nicht nur aus dem primären App Store zu installieren.

Das ist flexibel, kann aber auch ein Sicherheitsrisiko darstellen.

## Android vs iOS

| Android                             | iOS                                        |
| ----------------------------------- | ------------------------------------------ |
| offeneres Ökosystem                 | geschlosseneres Ökosystem                  |
| viele Hersteller                    | Apple-zentriert                            |
| verschiedene Geräte und Oberflächen | einheitlichere Hardware-Software-Kontrolle |
| mehr Vertriebsmöglichkeiten         | stärker kontrollierter Vertrieb            |

## Veröffentlichungspaket und installierte Anwendung

Das **AAB** (`Android App Bundle`) ist ein Veröffentlichungsformat. Google Play kann daraus die für das Gerät geeigneten APKs erzeugen. Ein AAB ist daher nicht dasselbe wie eine unmittelbar installierbare APK-Datei. Die offene AOSP-Basis bedeutet außerdem nicht, dass jedes Gerät Google Play oder sämtliche Google-Dienste mitbringt.

## Durchgearbeiteter Fall: QR-Scanner-App

Der QR-Scanner benötigt ein Kamerabild. Beim Start der Kamerafunktion ist deshalb eine Kameraerlaubnis sinnvoll. Für das reine Einlesen eines Codes ist dagegen kein Zugriff auf das gesamte Adressbuch nötig. Im Test wird auch die Ablehnung der Erlaubnis geprüft: Die App erklärt die Folge und bleibt soweit möglich benutzbar.

Die Sandbox des Systems unterstützt die Trennung der Apps. Eine erteilte Berechtigung kann aber tatsächlichen Datenzugriff ermöglichen; bewusste Zustimmung und datensparsames Verhalten gehören deshalb zusammen. Beim Gerätesupport werden neben der Android-Version auch der Sicherheits-Patchstand und der zugesagte Supportzeitraum des Herstellers kontrolliert.

## Prüfungstaugliche Formulierung

> Android ist eine weit verbreitete mobile Betriebssystem-Plattform, die auf Open-Source-Grundlagen aufbaut.  
> Sie läuft auf Smartphones und Tablets vieler Hersteller und ist daher flexibel und weit verbreitet.  
> Wichtige Merkmale von Android sind die App-Ausführung,
> die Berechtigungsverwaltung, das Google-Play-Ökosystem
> sowie die größere Anpassbarkeit.

## Schnelle Selbstkontrolle

1. Was ist AOSP?
2. Was ist einer der großen Vorteile von Android?
3. Was ist eine der häufigen Herausforderungen von Android?
4. Welche Rolle spielt Google Play?
5. Worin unterscheidet sich Android von iOS?

## Kurzantworten zur Selbstkontrolle

1. Das Android Open Source Project, die Open-Source-Basis
2. Die große Geräteauswahl und die Anpassbarkeit
3. Die Fragmentierung und die unterschiedlichen Update-Modelle
4. Wichtiger App-Vertriebsmarktplatz
5. Im Allgemeinen offener und läuft auf Geräten vieler Hersteller

## Quellen

1. Android Open Source Project - Architecture overview  
   https://source.android.com/docs/core/architecture  
   Verwendung: Android als vollständige mobile Plattform und die Rolle von AOSP.

2. Android Developers - Application fundamentals  
   https://developer.android.com/guide/topics/fundamentals  
   Verwendung: Android-App-Modell, Berechtigungen, Hardware- und Software-Fähigkeiten.

3. Android Developers - Publish your app  
   https://developer.android.com/studio/publish/  
   Verwendung: Android-App-Vertrieb, Google Play und andere Veröffentlichungswege.

4. Android Developers - Play Integrity overview  
   https://developer.android.com/google/play/integrity/overview  
   Verwendung: Play Protect / Integritätsschutz und Sicherheitsumgebung.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Android: App Bundles](https://developer.android.com/guide/app-bundle): AAB als Veröffentlichungsformat und APK-Erzeugung.
- [Android: Permissions](https://developer.android.com/guide/topics/permissions/overview): funktionsbezogene Erlaubnis und Umgang mit Ablehnung.
- [AOSP: Application Sandbox](https://source.android.com/docs/security/app-sandbox): Trennung der Anwendungen.

Geprüft: `2026-10-14`.
