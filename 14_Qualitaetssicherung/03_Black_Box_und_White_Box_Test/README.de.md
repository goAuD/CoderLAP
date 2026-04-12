# Black Box und White Box Test

## Schneller visueller Überblick

| Testtyp | Worauf liegt der Fokus? |
|---|---|
| Black-Box | Eingabe und Ausgabe |
| White-Box | interne Logik, Zweige, Bedingungen, Codestruktur |

## Was ist ein Black-Box-Test?

Hier prüft der Tester:

- was das System als Eingabe erhält
- welche Ausgabe es liefert
- ob es den Anforderungen entspricht

Die interne Implementierung muss nicht im Detail bekannt sein.

## Was ist ein White-Box-Test?

Hier ist auch die interne Funktionsweise wichtig.

Die Testgrundlage kann sein:

- Kontrollpfade
- Verzweigungen
- Bedingungen
- Schleifen
- Abdeckung

Dafür muss man in der Regel die Funktionsweise des Codes oder der internen Struktur kennen.

## Wann ist welcher nützlich?

### Black-Box

- zur Überprüfung von Anforderungen
- zum Testen von Funktionen
- aus der Benutzerperspektive

### White-Box

- zur Überprüfung der Codelogik
- zur Verbesserung der Abdeckung
- zum Finden interner Fehler

## Black-Box und White-Box: nicht zu starr gegenüberstellen

In der Praxis nutzen viele Projekte **beide**, denn:

- Black-Box prüft das Verhalten
- White-Box verbessert die interne Qualität und Abdeckung

## Prüfungstaugliche Formulierung

> Beim Black-Box-Test wird das externe Verhalten des Systems anhand von Eingaben und Ausgaben geprüft, ohne die interne Implementierung im Detail zu berücksichtigen.  
> Der White-Box-Test stützt sich hingegen auch auf die interne Struktur, beispielsweise Verzweigungen, Bedingungen und Codepfade.  
> Die beiden Ansätze werden nicht als Ersatz, sondern ergänzend zueinander eingesetzt.

## Häufige Prüfungsfehler

- Behaupten, dass der Black-Box-Test kein echtes Testen ist.
- Den White-Box-Test ausschließlich mit Unit-Tests gleichsetzen.
- Die Kenntnis der internen Struktur nicht erwähnen.
- Die beiden Methoden als absolute Gegensätze behandeln.

## Schnelle Selbstkontrolle

1. Was ist das Wesen des Black-Box-Tests?
2. Was ist das Wesen des White-Box-Tests?
3. Bei welchem ist die Kenntnis der internen Logik wichtig?
4. Welcher prüft eher das anforderungsgemäße Verhalten?
5. Warum ist es gut, beide zusammen einzusetzen?

## Kurzantworten zur Selbstkontrolle

1. Prüfung des externen Verhaltens
2. Prüfung der internen Logik und Struktur
3. Beim White-Box-Test
4. Beim Black-Box-Test
5. Weil sie unterschiedliche Fehlerarten aufdecken

## Quellen

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: offizielle, aktuelle Grundquelle zu den Begriffen Black-Box- und White-Box-Test.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Verwendung: offizieller begrifflicher Hintergrund zur Definition der Testtypen.

Abgerufen: `2026-04-08`
