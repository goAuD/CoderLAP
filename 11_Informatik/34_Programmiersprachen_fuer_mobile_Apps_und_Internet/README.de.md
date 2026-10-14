# Programmiersprachen fuer mobile Apps und Internet

## Schneller visueller Überblick

| Bereich | Typische Sprachen |
|---|---|
| Android | `Kotlin`, teilweise `Java` |
| iOS | `Swift` |
| Cross-Platform Mobil | `Dart`, `JavaScript` / `TypeScript`, `C#` |
| Web-Frontend | `JavaScript`, `TypeScript` |
| Web-Backend | `PHP`, `Java`, `C#`, `Python`, `JavaScript` |

## Für mobile Apps verwendete Sprachen

### Natives Android

- `Kotlin`
- in bestimmten Fällen `Java`

### Natives iOS

- `Swift`

### Cross-Platform

- `Dart` in `Flutter`-Umgebung
- `JavaScript` / `TypeScript` in `React Native`-Umgebung
- `C#` in `.NET MAUI`-Umgebung

## Für Internetanwendungen verwendete Sprachen

### Frontend

- `JavaScript`
- `TypeScript`

### Backend

- `PHP`
- `Java`
- `C#`
- `Python`
- `JavaScript` / `Node.js`

## Nativ und Cross-Platform: nicht verwechseln

| Ansatz | Vorteil | Nachteil |
|---|---|---|
| nativ | bessere Plattformintegration | separate Entwicklung pro Plattform |
| Cross-Platform | gemeinsame Codebasis | Kompromisse möglich |

## Worauf muss man achten?

- Die Sprache allein ist nicht alles, das Framework und die Toolchain zählen auch.
- Bei Mobilgeräten ist die Anpassung an die Plattform wichtig.
- Bei Internetanwendungen muss man Frontend und Backend trennen.
- In der Prüfung sollte man in Kategorien denken, nicht durcheinander aufzählen.

## Ein Dienst mit mehreren Clients

**Beispiel:** Eine Person markiert dasselbe Thema unter Android, auf dem iPhone
oder im Web als gelernt. Die Sprache der Oberfläche darf unterschiedlich sein,
der Vertrag für den Datenaustausch kann gemeinsam sein. Das folgende Beispiel
ist nur ein gedachter API-Vertrag, keine Funktion der derzeitigen Website:

```http
PUT /api/me/progress/LAP-15-17 HTTP/1.1
Content-Type: application/json

{"completed":true}
```

Der Server ermittelt aus der authentifizierten Sitzung, wessen Fortschritt
geändert wird. Eine beliebige vom Client gesendete Benutzer-ID belegt keine
Berechtigung. Ein direktes Datenbankpasswort gehört nicht in die App. Mobile
Clients und Browser können beide über eine serverseitige API arbeiten.

| Schicht | Eine mögliche Lösung | Was bleibt zusätzlich zu lösen? |
|---|---|---|
| Android-Oberfläche | Kotlin | Plattformnavigation, Berechtigungen, Lebenszyklus |
| iPhone-Oberfläche | Swift | Plattformnavigation, Berechtigungen, Lebenszyklus |
| gemeinsamer Mobilcode | Flutter/Dart oder React Native/TypeScript | plattformspezifische Teile und Tests auf beiden Plattformen |
| Weboberfläche | HTML/CSS und JavaScript | Browser, Tastatur, responsives Layout |
| Backend | beispielsweise PHP oder Java | Zugriff, Validierung, Datenverwaltung |

Übliche Web-Toolchains übersetzen TypeScript in JavaScript. Node.js ist eine
Laufzeitumgebung, keine weitere Sprache. Wie viel Code plattformübergreifend
teilbar ist, hängt von der Aufgabe ab. Kamera, Benachrichtigungen, Offlinezustand
und Anmeldung erfordern besonders sorgfältige Tests auf echten Geräten.
Eine PWA ist eine weitere Weboption; ihre Möglichkeiten hängen von der
Unterstützung des jeweiligen Browsers und Betriebssystems ab.

## Prüfungstaugliche Formulierung

> Für die Entwicklung von mobilen Apps und Internetanwendungen werden verschiedene Programmiersprachen verwendet.
> In der nativen Android-Entwicklung ist Kotlin, in der nativen iOS-Entwicklung Swift typisch.
> Bei Cross-Platform-Mobillösungen ist zum Beispiel Dart mit `Flutter`
> oder JavaScript bzw. TypeScript mit `React Native` einsetzbar.
> Bei Internetanwendungen sind auf der Frontend-Seite
> hauptsächlich JavaScript und TypeScript,
> auf der Backend-Seite zum Beispiel PHP, Java, C# oder Python verbreitet.

## Schnelle Selbstkontrolle

1. Welche Sprache ist typisch für Android?
2. Welche Sprache ist typisch für iOS?
3. Nenne zwei Cross-Platform-Mobile-Richtungen.
4. Welche Sprachen sind typisch für Web-Frontend?
5. Welche Sprachen sind typisch für Backend?

## Kurzantworten zur Selbstkontrolle

1. Kotlin
2. Swift
3. Flutter/Dart und React Native/JS-TS
4. JavaScript und TypeScript
5. Zum Beispiel PHP, Java, C#, Python

## Quellen

Geprüft: `2026-10-14`.

- [Android Developers: Kotlin-first](https://developer.android.com/kotlin/first): Entwicklungsansatz für Android.
- [Apple: Swift](https://developer.apple.com/swift/): Swift und Apple-Plattformen.
- [React Native: Platform-specific code](https://reactnative.dev/docs/platform-specific-code): Gemeinsamer und plattformspezifischer Code.


1. Android Developers - Kotlin for Android
   https://developer.android.com/kotlin/first
   Verwendung: offizielle Android-Quelle zur hervorgehobenen Rolle von Kotlin.

2. Apple - Swift
   https://developer.apple.com/swift/
   Verwendung: offizielle Quelle zur Rolle von Swift in der iOS-Entwicklung.

3. Flutter
   https://flutter.dev/
   Verwendung: offizielle Cross-Platform-Mobil- und Multiplattform-Entwicklungsquelle.

4. React Native
   https://reactnative.dev/
   Verwendung: offizielle Quelle für JavaScript/TypeScript-basierte Mobilentwicklung.

5. .NET MAUI
   https://dotnet.microsoft.com/en-us/apps/maui
   Verwendung: offizielle Quelle für C#-basierte Cross-Platform-App-Entwicklung.

Abgerufen: `2026-04-08`
