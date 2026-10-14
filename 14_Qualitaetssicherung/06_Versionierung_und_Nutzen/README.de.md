# Versionierung und Nutzen

## Schneller visueller Überblick

| Version | Typische Bedeutung |
|---|---|
| `2.0.0` | inkompatible Änderung der öffentlichen API |
| `2.1.0` | neues, abwärtskompatibles Feature |
| `2.1.3` | abwärtskompatible Fehlerbehebung |

## Was ist Versionierung?

Softwareversionierung bedeutet, dass Releases bewusst eine Versionskennung erhalten.

Gängiges Schema:

```text
MAJOR.MINOR.PATCH
```

Dies ist die bekannteste Form der semantischen Versionierung (`Semantic Versioning`, `SemVer`).

## Warum ist das nützlich?

- das Release ist eindeutig identifizierbar
- es ist nachvollziehbar, welches Ausmaß die Änderung hat
- es hilft bei der Verknüpfung von Fehlermeldungen und Releases
- es unterstützt die Planung von Updates
- es ist wichtig bei der Verwaltung von Abhängigkeiten und Kompatibilität

## Typische Bedeutungen

### Major

- inkompatible Änderung der öffentlichen API

### Minor

- neue, abwärtskompatible Funktion

### Patch

- abwärtskompatible Fehlerbehebung

## Versionierung und Versionsverwaltung: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Versionierung | Nummerierung von Releases |
| Versionsverwaltung | Nachverfolgung von Änderungen in einem VCS, z.B. `Git` |

## Von Änderungsgröße zu Kompatibilität

SemVer bezieht sich auf den Vertrag der veröffentlichten API. Drei Beispiele für eine Bibliothek mit `sum(numbers)`:

| Ausgangspunkt: 2.3.4 | Änderung | Neue Version |
|---|---|---|
| dokumentiertes Verhalten korrigiert | leere Liste liefert die beschriebenen 0 | 2.3.5 |
| kompatible Erweiterung | neue Funktion `average(numbers)` | 2.4.0 |
| inkompatible Änderung | `sum` liefert ein Objekt statt einer Zahl | 3.0.0 |

Auch eine einzige inkompatible Codezeile kann Major erfordern. Minor und Patch sind bei SemVer verbindlich kompatibel und nicht nur meistens. Verwendet eine Anwendung eine andere Nummerierung, gelten deren dokumentierte Regeln.

`0.x.y` kennzeichnet anfängliche Entwicklung ohne zugesagte stabile öffentliche API. `2.4.0-rc.1` ist eine Vorabversion und nicht die endgültige Version `2.4.0`. Der Inhalt eines bereits veröffentlichten Pakets wird nicht ohne neue Versionskennung ausgetauscht; so bleibt eine im Fehlerbericht genannte Version nachvollziehbar.

## Prüfungstaugliche Formulierung

> Versionierung bezeichnet die bewusste Vergabe von Versionsnummern für Softwarereleases.  
> Ziel ist es, ein bestimmtes Release eindeutig zu identifizieren und das Ausmaß der Änderung sichtbar zu machen.  
> In der Praxis ist das Schema `major.minor.patch` verbreitet,
> das bei der Verwaltung von Kompatibilität,
> Fehlerverfolgung und Updates hilft.

## Schnelle Selbstkontrolle

1. Was ist das Wesen der Versionierung?
2. Warum ist eine Versionsnummer nützlich?
3. Was bezeichnet häufig `major`?
4. Was bezeichnet häufig `patch`?
5. Was ist der Unterschied zwischen Versionierung und Versionsverwaltung?

## Kurzantworten zur Selbstkontrolle

1. Die bewusste Nummerierung von Releases
2. Weil sie Releases identifizierbar und nachvollziehbar macht
3. Bei SemVer eine inkompatible Änderung der öffentlichen API, unabhängig von der Größe der Codeänderung.
4. Bei SemVer eine abwärtskompatible Fehlerbehebung.
5. Das eine nummeriert, das andere verwaltet Änderungen

## Quellen

- [Semantic Versioning 2.0.0](https://semver.org/)  
  Öffentliche API, Kompatibilität, Vorabversion und unverändertes veröffentlichtes Paket.

- [npm: About semantic versioning](https://docs.npmjs.com/about-semantic-versioning/)  
  Praktische Beispiele für Patch, Minor und Major.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Semantic Versioning 2.0.0  
   https://semver.org/  
   Verwendung: primäre, offizielle Quelle zur `major.minor.patch`-Logik.

2. npm Docs - About semantic versioning  
   https://docs.npmjs.com/about-semantic-versioning  
   Verwendung: moderne, praxisnahe Zusammenfassung zum Nutzen und zur Anwendung der Versionierung.

Abgerufen: `2026-04-08`
