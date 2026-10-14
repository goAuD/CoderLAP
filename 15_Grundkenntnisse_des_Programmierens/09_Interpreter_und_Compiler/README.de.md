# Interpreter und Compiler

## Schneller visueller Überblick

| Werkzeug | Grundidee |
|---|---|
| Interpreter | den Code unmittelbarer interpretieren und ausführen |
| Compiler | den Code in eine andere Form, häufig Maschinencode, übersetzen |

## Was ist ein Compiler?

Der Compiler:

- liest den Quellcode ein
- analysiert die Sprachstruktur
- übersetzt ihn in eine andere Form

Das kann sein:

- Maschinencode
- Bytecode
- oder eine Zwischendarstellung

## Was ist ein Interpreter?

Der Interpreter verarbeitet den Code auf unmittelbarere Weise, und die Ausführung ist enger mit der Interpretation verknüpft.

Das erlaubt oft:

- flexiblere Entwicklung
- schnelles Ausprobieren
- funktioniert aber nicht auf dieselbe Weise wie ein klassischer vorausübersetzender Compiler

## Die moderne Realität: nicht immer schwarz-weiß

Heute nutzen viele Plattformen:

- sowohl Übersetzung
- als auch Interpretation
- oder `JIT`, also Übersetzung zur Laufzeit

Deshalb sollte man bei der Prüfung das Grundprinzip kennen, nicht einen vereinfachenden Mythos.

## Vor- und Nachteile kurz gefasst

| Aspekt | Interpreter | Compiler |
|---|---|---|
| schnelles Ausprobieren | oft Vorteil | variiert |
| Übersetzungszeitpunkt | direkte interpretierende Ausführung | vor der Ausführung (AOT) oder dabei (JIT) |
| Laufzeitleistung | variiert | oft günstig |
| Fehlererkennung | oft auch zur Laufzeit | viele Fehler schon beim Kompilieren |

## Compiler, Interpreter, Assembler: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Compiler | übersetzt eine Hochsprache |
| Interpreter | interpretiert und führt unmittelbarer aus |
| Assembler | wandelt Assembly-Sprache in maschinennahe Form um |

## Übersetzung und Ausführung sind getrennte Schritte

| Beispiel | Typische Verarbeitung |
|---|---|
| Natives C-Programm | Vorverarbeitung, Übersetzung, Assembly, Objektdatei, Linken |
| Java | Quelltext wird Bytecode; die JVM führt ihn aus und kann JIT einsetzen |
| JavaScript in V8 | Analyse, Bytecode, Interpreter und Übersetzungsstufen zur Laufzeit |

Der **Linker** verbindet Objektdateien und löst deren gegenseitige Verweise auf.
Das fertige Programm kann weiterhin eine Laufzeitumgebung oder dynamische
Bibliotheken benötigen. Ein **JIT-Compiler** ist ein echter Compiler, der während
der Ausführung arbeitet. „Ein Compiler übersetzt immer im Voraus“ ist deshalb
zu eng formuliert.

Eine erfolgreiche Übersetzung gibt Auskunft über Sprachprüfungen, beweist aber
nicht die Richtigkeit einer Geschäftsregel. Ein korrekt übersetztes Programm
kann trotzdem falsche Versandkosten berechnen. Syntaxprüfung, Laufzeitprüfung
und Tests erwarteter Ergebnisse ergänzen einander.

## Prüfungstaugliche Formulierung

> Der Compiler übersetzt Code in eine andere Darstellung, etwa Maschinen- oder Bytecode; dies kann vor oder während der Ausführung geschehen.  
> Der Interpreter hingegen führt die Code-Ausführung auf unmittelbarere Weise, zusammen mit der Interpretation, durch.  
> In modernen Systemen vermischen sich die beiden Ansätze häufig, aber der grundlegende Unterschied liegt weiterhin
> zwischen Übersetzung in eine andere Darstellung und unmittelbarer Ausführung.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe des Compilers?
2. Was ist das Hauptmerkmal des Interpreters?
3. Warum ist das Bild heute nicht rein schwarz-weiß?
4. Was ist der Unterschied zwischen Compiler und Assembler?
5. Welche Fehler können schon beim Kompilieren auftreten?

## Kurzantworten zur Selbstkontrolle

1. Die Übersetzung des Quellcodes
2. Unmittelbarere Interpretation und Ausführung
3. Weil es hybride und JIT-Systeme gibt
4. Der Compiler arbeitet mit Hochsprache, der Assembler mit Assembly
5. Syntaktische und bestimmte strukturelle Fehler

## Quellen

Geprüft: `2026-10-14`.

- [V8: Ignition](https://v8.dev/docs/ignition): Interpreter in einer modernen JavaScript-Engine.
- [V8: Sparkplug](https://v8.dev/blog/sparkplug): Übersetzungsstufe zur Laufzeit.


1. Python Docs - Using the Python Interpreter  
   https://docs.python.org/3/tutorial/interpreter.html  
   Verwendung: offizielle Quelle zur Funktionsweise der interpreterbasierten Ausführung.

2. GCC - Overall Options  
   https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html  
   Verwendung: offizieller Hintergrund zu den Schritten des Übersetzungsprozesses und zur Funktionsweise des Compilers.

Abgerufen: `2026-04-09`
