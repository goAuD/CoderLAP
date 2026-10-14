# Standards ANSI ISO IEEE

## Schneller visueller Überblick

| Abkürzung | Name | Hauptrolle |
|---|---|---|
| ANSI | American National Standards Institute | Koordination des amerikanischen nationalen Normensystems |
| ISO | International Organization for Standardization | Herausgabe internationaler Normen |
| IEEE | Institute of Electrical and Electronics Engineers | Entwicklung technischer und IT-Standards |

## Warum sind Normen in der Informatik wichtig?

Weil die Informatik auf der Zusammenarbeit vieler verschiedener Systeme aufbaut.

Ohne Normen wäre Folgendes häufig:

- inkompatible Geräte
- unterschiedliche Datenverarbeitung
- schwierigere Integration
- geringere Zuverlässigkeit

Normen helfen dabei, dass:

- denselben Begriff alle ähnlich verstehen
- Systeme kommunizieren können
- Entwicklungen langfristig wartbar bleiben

## Welche Rolle spielt ANSI?

ANSI ist ein wichtiger koordinierender Akteur im amerikanischen nationalen Normensystem.

Wichtige Klarstellung:

- ANSI entwickelt die Standards nicht selbst
- es koordiniert eher die Normungsprozesse und Genehmigungsrahmen

## Welche Rolle spielt ISO?

ISO gibt internationale Normen in vielen Bereichen heraus.

In der Informatik und verwandten Bereichen ist das wichtig, weil:

- es einheitliche Anforderungen bietet
- es die internationale Zusammenarbeit unterstützt
- es die Qualitätssicherung und Interoperabilität fördert

## Welche Rolle spielt IEEE?

IEEE ist besonders bekannt für seine technischen und informatischen Standards.

Typische Beispiele:

- Netzwerktechnologien
- hardwarenahe Standards
- Protokolle
- Zahlendarstellung und elektrotechnische Bereiche

Zum Beispiel ist die `IEEE 802`-Familie in der Welt der Netzwerktechnologien sehr wichtig.

## Was darf man nicht verwechseln?

| Begriff | Bedeutung |
|---|---|
| Standard | konkrete Vorschrift oder Spezifikation |
| Normungsorganisation | eine Organisation, die Standards pflegt oder koordiniert |
| ANSI / ISO / IEEE | Organisationen oder normende Akteure, nicht an sich "ein Standard" |

## Warum ist das für Entwickler nützlich?

- Es wird besser verständlich, warum man sich an präzise Spezifikationen halten muss
- es ist leichter, kompatible Systeme zu bauen
- klarere Dokumentation und Kommunikation entstehen
- Qualitätssicherung und Tests können sich ebenfalls auf Normen stützen

## Konkrete Standards mit konkreten Aufgaben verbinden

`IEEE 802.3` betrifft Ethernet, `IEEE 802.11` drahtlose lokale Netze.
`IEEE 754` definiert Gleitkommadarstellungen und Operationen. Letzteres ist
direkt im Programm sichtbar: JavaScripts `Number` verwendet binäre
64-Bit-Gleitkommazahlen mit doppelter Genauigkeit.

Eine in Node.js ausführbare Beobachtung:

<!-- example:run -->

```javascript
console.log(0.1 + 0.2);
console.log(0.1 + 0.2 === 0.3);
console.log(10 + 20 === 30);
```

```text
0.30000000000000004
false
true
```

`0.1` und `0.2` besitzen keine exakte endliche Binärbruchdarstellung. Speicherung
und Addition erfordern deshalb Rundung. Das ergibt sich aus der Darstellung.
Die Summe kleiner ganzzahliger Centbeträge ist dagegen exakt; bei großen Werten
ist zusätzlich die Grenze genauer Ganzzahlen zu beachten. Eine Rundung für die
Anzeige verändert nicht rückwirkend die Mathematik der Berechnung.

Beim Verweis auf eine Spezifikation nennen wir Kennung, Ausgabe und relevante
Anforderung. „Standardkonform“ allein ist kein hinreichend genaues
Abnahmekriterium. Standardentwicklung, Konformitätsprüfung und Zertifizierung
sind unterschiedliche Aufgaben. ISO entwickelt Standards, führt aber selbst
keine Zertifizierung von Organisationen durch.

## Prüfungstaugliche Formulierung

> ANSI, ISO und IEEE sind wichtige Akteure in der Welt der Normung.  
> Das Ziel von Normen ist,
> dass informatische Systeme kompatibel, sicher
> und nach einheitlichen Prinzipien funktionieren.  
> ANSI ist vor allem bei der Koordination der amerikanischen Normung wichtig,
> ISO gibt internationale Normen heraus
> und IEEE ist besonders bedeutend
> im Bereich technischer und informatischer Standards.

## Schnelle Selbstkontrolle

1. Warum sind Normen in der Informatik wichtig?
2. Welche Rolle hat ANSI kurz zusammengefasst?
3. Welche Rolle hat ISO kurz zusammengefasst?
4. Warum ist IEEE in der IT bekannt?
5. Was ist der Unterschied zwischen Organisation und Standard?

## Kurzantworten zur Selbstkontrolle

1. Sie bieten Kompatibilität und Einheitlichkeit
2. Koordination der amerikanischen Normung
3. Herausgabe internationaler Normen
4. Pflegt viele technische und IT-Standards
5. Die Organisation erstellt oder koordiniert, der Standard ist die Vorschrift selbst

## Quellen

Geprüft: `2026-10-14`.

- [ANSI: Standards FAQs](https://www.ansi.org/standards-faqs): ANSI koordiniert und genehmigt, entwickelt aber keine Standards.
- [IEEE 802.3](https://www.ieee802.org/3/): Ethernet-Standardisierung.
- [IEEE 802.11](https://www.ieee802.org/11/): WLAN-Standardisierung.
- [MDN: Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number): IEEE754 und Zahlengenauigkeit.
- [ISO: Certification](https://www.iso.org/certification.html): Trennung von Standard und Zertifizierung.


1. ANSI - Introduction to American National Standards process by ANSI  
   https://www.ansi.org/american-national-standards/ans-introduction/overview  
   Verwendung: offizieller Überblick über ANSI und die Rolle der amerikanischen Normung.

2. ISO - Standards  
   https://www.iso.org/standards.html  
   Verwendung: offizielle Darstellung der Rolle von ISO in der Welt internationaler Normen.

3. IEEE SA - About Us  
   https://standards.ieee.org/about/  
   Verwendung: offizielle Quelle zur Rolle und Funktionsweise der IEEE Standards Association.

4. MDN - Web standards  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards  
   Verwendung: Entwicklerkontext dafür, warum Standards im Web und für die Interoperabilität wichtig sind.

Abgerufen: `2026-04-08`
