# Programmspezifikation

## Schneller visueller Überblick

| Teil der Spezifikation | Was beschreibt es? |
|---|---|
| funktionale Anforderungen | was das Programm tun soll |
| Eingaben | welche Daten es erhält |
| Ausgaben | was es zurückgibt |
| Regeln / Bedingungen | welche Einschränkungen gelten |
| Fehlerbehandlung | was bei Problemen passieren soll |

## Was ist eine Programmspezifikation?

Die Programmspezifikation ist eine Beschreibung, die Folgendes festhält:

- das Ziel des Programms
- die Aufgabe
- die erforderlichen Funktionen
- die Verarbeitungsregeln
- die erwarteten Ergebnisse

Dies kann sein:

- eine kürzere Aufgabenbeschreibung
- eine detaillierte Anforderungsspezifikation
- Teil einer Entwicklungs- oder Produktspezifikation

## Warum ist das wichtig?

- reduziert Missverständnisse
- hilft den Entwicklern zu wissen, was umgesetzt werden muss
- hilft den Testern zu wissen, was überprüft werden muss
- bleibt als nachvollziehbare Referenz erhalten

## Was kann sie enthalten?

Typischerweise:

- Programmziel
- Eingaben und Ausgaben
- Hauptprozesse
- Geschäftsregeln
- Ausnahmen und Fehlerbehandlung
- Einschränkungen und nicht-funktionale Anforderungen

## Spezifikation und Lösung: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Spezifikation | was das Programm können muss |
| Entwurf / Design | wie wir es aufbauen |
| Implementierung | wie wir es konkret schreiben |

## Eigenschaften einer guten Spezifikation

- klar
- eindeutig
- überprüfbar
- nicht widersprüchlich
- beschreibt sowohl das Ziel als auch die Regeln

## Ein überprüfbarer Vertrag für eine Buchung

Den Wunsch „schnell und sicher“ zerlegen wir in konkrete Bedingungen. Beispiel
für die Buchung eines Kursplatzes:

| Teil | Vereinbarung |
|---|---|
| Vorbedingung | angemeldete Person, existierender Kurs |
| Eingabe | Kurskennung; die Person identifiziert der Server |
| Erfolg | eine Buchung entsteht und wird in der Bestätigung identifiziert |
| Voller Kurs | verständliche Ablehnung, keine Buchung |
| Wiederholte Anfrage | keine weitere Buchung derselben Person für denselben Kurs |
| Leistung | Messung mit festgelegtem Testrechner, Datenbestand und Last |

Die Nachbedingung beschreibt, was nach erfolgreicher Ausführung gelten soll.
Eine Anforderung erhält beispielsweise die Kennung `FOG-01`, auf die ein Testfall
verweist. Bei Änderungen werden betroffene Tests dadurch sichtbar. Eine vage
Zeitvorgabe präzisieren wir gemeinsam, etwa: 95% der Anfragen antworten bei
definierter Last innerhalb einer Sekunde. Das ist ein Ziel dieses Beispiels,
keine allgemeine Vorschrift.

## Prüfungstaugliche Formulierung

> Die Programmspezifikation ist eine Beschreibung, die festhält, welche Aufgabe das Programm erfüllen muss, mit  
> welchen Eingaben es arbeitet, welche Ausgaben es liefert und nach welchen Regeln es funktioniert.  
> Das Ziel der Spezifikation ist die eindeutige Festlegung der Anforderungen, damit Entwicklung und Testen auf  
> demselben erwarteten Verhalten aufbauen können.  
> Die Spezifikation beschreibt also nicht den Code, sondern das erwartete Verhalten.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche einer Programmspezifikation?
2. Warum ist sie vor der Entwicklung wichtig?
3. Was beschreibt die Spezifikation?
4. Was ist der Unterschied zwischen Spezifikation und Implementierung?
5. Warum ist sie auch für das Testen wichtig?

## Kurzantworten zur Selbstkontrolle

1. Die Beschreibung des erwarteten Verhaltens
2. Weil sie die Anforderungen klärt
3. Ziel, Eingabe, Ausgabe, Regeln, Fehlerbehandlung
4. Die eine beschreibt Erwartungen, die andere die Umsetzung
5. Weil anhand dessen die korrekte Funktionsweise überprüft werden kann

## Quellen

Geprüft: `2026-10-14`.

- [Atlassian: Product specifications](https://www.atlassian.com/agile/product-management/product-specification): messbares Ziel und Umfang; eigenes Buchungsbeispiel.


1. IEEE SA - IEEE/ISO/IEC P29148  
   https://standards.ieee.org/ieee/29148/12262  
   Verwendung: offizielle Standardseite zu den Grundbegriffen des Requirements Engineering und guter Anforderungen.

2. Atlassian - What are Product Specifications?  
   https://www.atlassian.com/agile/product-management/product-specification  
   Verwendung: moderne, praxisnahe Quelle zur geschäftlichen und entwicklungsbezogenen Rolle der Spezifikation.

Abgerufen: `2026-04-09`
