# Assembler

## Schneller visueller Überblick

| Ebene | Beispiel |
|---|---|
| Hochsprache | `Python`, `Java`, `C#` |
| niedrige Sprache | Assembly |
| Maschinencode | direkt vom Prozessor verstandene Anweisungen |

## Was ist die Assembly-Sprache?

Assembly ist eine Sprache, in der die Maschinenanweisungen mit kurzen, für Menschen besser lesbaren Mnemoniks
geschrieben werden.

Zum Beispiel:

- `MOV`
- `ADD`
- `JMP`

Diese stehen bereits sehr nahe an der Funktionsweise des Prozessors.

## Was ist der Assembler als Werkzeug?

Das Assembler-Programm:

- liest den Assembly-Quellcode ein
- übersetzt ihn in maschinennahe Form
- erzeugt Objektcode oder linkbare Ausgabe

## Warum ist das wichtig?

- damit kann die interne Funktionsweise des Computers besser verstanden werden
- kann in eingebetteten Systemen oder hardwarenaher Entwicklung wichtig sein
- kommt bei leistungskritischen, niedrigen Aufgaben vor

## Vorteile

- sehr präzise hardwarenahe Kontrolle
- Möglichkeit kleiner und optimierter Lösungen
- tieferes Verständnis der Architektur

## Nachteile

- schwer zu schreiben und zu warten
- schlechtere Portabilität
- langsamere Entwicklung
- starke Prozessorabhängigkeit

## Assembler, Compiler, Interpreter: nicht verwechseln

| Begriff | Womit arbeitet er? |
|---|---|
| Assembler | mit Assembly-Sprache |
| Compiler | mit Hochsprache |
| Interpreter | mit zur Laufzeit interpretiertem Code |

## Register, Anweisung und Objektdatei

Der folgende **illustrative Ausschnitt** verwendet x86 mit Intel-Syntax. Er ist
kein vollständiges Programm; Einstiegspunkt und betriebssystemspezifischer
Abschluss fehlen.

```asm
mov eax, 7
add eax, 5
```

`eax` ist ein 32-Bit-Register. Die erste Anweisung lädt 7, die zweite addiert 5;
der Registerinhalt ist danach 12. Dadurch erscheint noch keine Bildschirmausgabe.
In Intel-Syntax steht das Ziel zuerst. Andere Syntaxformen können eine andere
Reihenfolge verwenden; deshalb nennen wir Architektur und Schreibweise.

Der Assembler codiert die Anweisungen und erstellt üblicherweise eine Objektdatei.
Der Linker verbindet getrennt übersetzte Teile. Registernamen und Befehle lassen
sich nicht unverändert auf ARM-Prozessoren übertragen. Bei Hochsprachen übernimmt
der Compiler einen großen Teil dieser Anpassung an die Zielarchitektur. Ein
Leistungsvorteil handgeschriebener Assembly muss gemessen werden; moderne
Compiler führen ebenfalls Optimierungen durch.

## Prüfungstaugliche Formulierung

> Der Assembler ist einerseits ein mit einer niedrigen Programmiersprache verbundener Begriff, andererseits das  
> Übersetzungswerkzeug, das Assembly-Anweisungen in maschinennahen Code umwandelt.  
> Die Assembly-Sprache steht nahe am Befehlssatz des Prozessors und ist deshalb hardwareabhängiger und schwerer  
> handhabbar als Hochsprachen.  
> Der Vorteil ist die präzise Kontrolle, der Nachteil die Komplexität und die geringere Portabilität.

## Schnelle Selbstkontrolle

1. Was ist die Assembly-Sprache?
2. Was ist der Assembler als Werkzeug?
3. Warum ist sie eine niedrige Sprache?
4. Was ist ein Hauptvorteil?
5. Was ist ein Hauptnachteil?

## Kurzantworten zur Selbstkontrolle

1. Hardwarenahe Programmiersprache
2. Ein Werkzeug, das aus Assembly maschinennahen Code erzeugt
3. Weil sie nahe an den Prozessoranweisungen steht
4. Präzise Kontrolle
5. Schwere Wartung und geringe Portabilität

## Quellen

Geprüft: `2026-10-14`.

- [GNU as: x86 syntax](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html): Intel-/AT&T-Syntax und Architekturabhängigkeit.


1. GNU Binutils - Using as  
   https://sourceware.org/binutils/docs/as/  
   Verwendung: offizielle Primärquelle zur Funktionsweise des GNU Assemblers.

2. GCC - Overall Options  
   https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html  
   Verwendung: ergänzender Hintergrund zum Verständnis des Übersetzungsprozesses und der Stellung der Assembly-Ebene.

Abgerufen: `2026-04-09`
