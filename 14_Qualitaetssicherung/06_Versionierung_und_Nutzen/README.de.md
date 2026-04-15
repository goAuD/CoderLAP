# Versionierung und Nutzen

## Schneller visueller Überblick

| Version | Typische Bedeutung |
|---|---|
| `2.0.0` | größere, nicht kompatible Änderung |
| `2.1.0` | neues Feature, in der Regel abwärtskompatibel |
| `2.1.3` | Fehlerbehebung |

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

- größere, brechende Änderung

### Minor

- neues Feature, in der Regel kompatible Erweiterung

### Patch

- kleinere Korrektur, Bugfix

## Versionierung und Versionsverwaltung: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Versionierung | Nummerierung von Releases |
| Versionsverwaltung | Nachverfolgung von Änderungen in einem VCS, z.B. `Git` |

## Prüfungstaugliche Formulierung

> Versionierung bezeichnet die bewusste Vergabe von Versionsnummern für Softwarereleases.  
> Ziel ist es, ein bestimmtes Release eindeutig zu identifizieren und das Ausmaß der Änderung sichtbar zu machen.  
> In der Praxis ist das Schema `major.minor.patch` verbreitet,
> das bei der Verwaltung von Kompatibilität,
> Fehlerverfolgung und Updates hilft.

## Häufige Prüfungsfehler

- Versionierung mit Versionsverwaltung verwechseln.
- Glauben, dass die Versionsnummer nur Dekoration ist.
- Die Kompatibilität nicht erwähnen.
- Nicht wissen, was `major`, `minor`, `patch` bedeutet.

## Schnelle Selbstkontrolle

1. Was ist das Wesen der Versionierung?
2. Warum ist eine Versionsnummer nützlich?
3. Was bezeichnet häufig `major`?
4. Was bezeichnet häufig `patch`?
5. Was ist der Unterschied zwischen Versionierung und Versionsverwaltung?

## Kurzantworten zur Selbstkontrolle

1. Die bewusste Nummerierung von Releases
2. Weil sie Releases identifizierbar und nachvollziehbar macht
3. Eine größere, brechende Änderung
4. Eine kleinere Fehlerbehebung
5. Das eine nummeriert, das andere verwaltet Änderungen

## Quellen

1. Semantic Versioning 2.0.0  
   https://semver.org/  
   Verwendung: primäre, offizielle Quelle zur `major.minor.patch`-Logik.

2. npm Docs - About semantic versioning  
   https://docs.npmjs.com/about-semantic-versioning  
   Verwendung: moderne, praxisnahe Zusammenfassung zum Nutzen und zur Anwendung der Versionierung.

Abgerufen: `2026-04-08`
