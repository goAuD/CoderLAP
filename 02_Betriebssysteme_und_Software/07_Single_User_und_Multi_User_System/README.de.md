# Single-User-System und Multi-User-System

## Schneller visueller Überblick

| Typ         | Merkmal                                                               |
| ----------- | --------------------------------------------------------------------- |
| Single-User | typischerweise wird es von einem Hauptbenutzer gleichzeitig verwendet |
| Multi-User  | mehrere Benutzer, Konten, Berechtigungen, Trennung                    |

## Was ist ein Single-User-System?

Ein klassisches Single-User-System ist für die Arbeit eines Benutzers ausgelegt, ohne mehrere getrennte, gleichzeitige Benutzersitzungen zu unterstützen. Ein historisches Beispiel auf Personalcomputern ist MS-DOS.

Davon zu unterscheiden ist die **Single-User-Nutzung**: Auch ein modernes OS mit mehreren Konten und Berechtigungen kann gerade von einer einzigen Person benutzt werden. Seine Fähigkeiten zur Benutzerverwaltung ändern sich dadurch nicht.

## Was ist ein Multi-User-System?

Ein System, das mehreren Benutzern Zugang, getrennte Berechtigungen und Ressourcenverwaltung bietet.

Es unterstützt typischerweise:

- separate Benutzerkonten
- Berechtigungsstufen
- parallelen Zugriff
- Ressourcenteilung
- Administration

Beispiele:

- Linux-Server
- Windows Server
- Unternehmens-Terminal- oder Serverumgebung

## Der wichtigste Unterschied

| Aspekt              | Single-User         | Multi-User                 |
| ------------------- | ------------------- | -------------------------- |
| primäre Nutzung     | ein Benutzer        | mehrere Benutzer           |
| Berechtigungssystem | kann einfacher sein | in der Regel detaillierter |
| paralleler Zugriff  | nicht das Hauptziel | ja, typisches Ziel         |
| Administration      | einfacher           | komplexer                  |

## Was muss man in der Prüfung wissen?

Die Hauptfrage ist nicht, wie viele Personen „vor dem Rechner sitzen", sondern ob das System:

- mehrere Benutzeridentitäten unterstützt
- Berechtigungen verwalten kann
- Ressourcen zwischen mehreren Benutzern regeln kann

## Beispiele

### Nutzung durch eine Person auf einem modernen OS

- Heim-Windows-PC
- persönliches MacBook
- eigener Entwicklerlaptop

### Multi-User-Beispiele

- Linux-Server mit mehreren Benutzerkonten
- Universitäts- oder Unternehmensserver
- Terminalserver
- Systeme mit mehreren Administratoren und Benutzern

## Wichtige Klarstellung

Ein modernes Betriebssystem kann:

- **Multitasking**-fähig sein
- und dabei **Single-User-Nutzung** haben

oder:

- **Multi-User**-fähig sein
- und dabei ebenfalls **Multitasking**-fähig sein

Also:

- Single-User / Multi-User und Multitasking **sind nicht dieselbe Frage**

## Sicherheitsbedeutung

Bei Multi-User-Systemen ist besonders wichtig:

- Authentifizierung
- Berechtigungsverwaltung
- Trennung
- Protokollierung

Denn mehrere Benutzer teilen sich dasselbe System oder dieselbe Infrastruktur.

## Durchgearbeiteter Fall: gemeinsam genutzter Schulrechner

Anna und Bela verwenden denselben Rechner mit eigenen Konten. Für ihre Dateien gelten getrennte Zugriffsregeln; zur Wartung gibt es ein eigenes Administratorkonto. Der Rechner besitzt auch dann ein Mehrbenutzer-Sicherheitsmodell, wenn am lokalen Bildschirm jeweils nur eine Person arbeitet.

Drei Fragen werden getrennt geprüft:

1. Gibt es getrennte Benutzeridentitäten und Berechtigungen?
2. Können mehrere Sitzungen angemeldet bleiben oder gleichzeitig arbeiten?
3. Welche Ausgabe, welcher Dienst und welche Lizenz erlauben Remotesitzungen?

Moderne Windows-, macOS- und Linux-Systeme lassen sich nicht pauschal als „Desktop, also Single-User” einordnen. Mehrbenutzerfähigkeit und Anzahl gleichzeitig benutzbarer interaktiver Desktops sind unterschiedliche Eigenschaften. Die Sitzungslimits verschiedener Windows-Client- und Serverausgaben können sich unterscheiden.

## Prüfungstaugliche Formulierung

> Ein Single-User-System ist in erster Linie für die direkte Nutzung durch einen Benutzer ausgelegt.  
> Ein Multi-User-System hingegen kann mehreren Benutzern Zugang,
> separate Berechtigungen und getrennte Arbeitsumgebungen bieten.  
> Multi-User-Systeme sind typischerweise in Server- oder Unternehmensumgebungen wichtig.

## Schnelle Selbstkontrolle

1. Was ist das Wesen eines Single-User-Systems?
2. Was ist das Wesen eines Multi-User-Systems?
3. Nenne ein Multi-User-Beispiel.
4. Sind Multi-User und Multitasking dasselbe?
5. Warum ist die Berechtigungsverwaltung bei Multi-User-Systemen wichtig?

## Kurzantworten zur Selbstkontrolle

1. Betrieb, der auf die Nutzung durch einen Benutzer ausgelegt ist
2. Fähig, mehrere Benutzer zu verwalten und zu trennen
3. Linux-Server oder Windows Server
4. Nein
5. Weil mehrere Benutzer die Ressourcen des Systems teilen

## Quellen

1. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Verwendung: Single-User- und Enterprise-/Multi-User-Kontext, Berechtigungen und Ressourcenverwaltung.

2. IBM - Mainframe Operating Systems  
   https://www.ibm.com/products/z/operating-systems  
   Verwendung: Beispiele für Betriebssysteme, die mehrere Benutzer und Unternehmensumgebungen bedienen.

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Verwendung: Beispiel für den modernen Desktop als Single-User-Nutzungskontext.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Microsoft: Manage user accounts](https://support.microsoft.com/en-us/windows/security/identity-signin/manage-user-accounts-in-windows): getrennte Konten und Zugriffe unter modernem Windows.

Geprüft: `2026-10-14`.
