# SMTP und SMTPS

## Lényeg 30 másodpercben

Az `SMTP` a levelek küldésére és továbbítására szolgáló protokoll.

Nem erre való:

- levelek olvasása

Ezért:

- `SMTP` = küldés / továbbítás
- `IMAP` vagy `POP3` = olvasás / hozzáférés

A `SMTPS` kifejezés ma jellemzően ezt jelenti:

- SMTP-szerű levélbeküldés titkosított kapcsolattal, tipikusan `465` porton

## Gyors vizuális kép

| Protokoll / használat | Tipikus port | Fő cél |
|---|---|---|
| SMTP relay | `25` | szerverek közti továbbítás |
| message submission | `587` | kliens felől levélbeküldés |
| implicit TLS submission / "SMTPS" | `465` | titkosított beküldés |

## Mire jó az SMTP?

Az SMTP a levelek:

- beküldésére
- továbbítására
- kézbesítési útjának szerveroldali kezelésére

Példák:

- kliens elküldi a levelet a saját szolgáltatójának
- egy szerver továbbítja a levelet a címzett szerverének

## Miért van több port?

Mert nem ugyanaz a feladat:

- `25` = klasszikus szerver-szerver kommunikáció
- `587` = kliensoldali submission
- `465` = titkosított submission, történelmileg `SMTPS` néven is ismert

## Mi az SMTPS?

Vizsgaszinten így érdemes fogalmazni:

- az `SMTPS` a titkosított SMTP-használatra utal

Fontos pontosítás:

- a mai szabványos világban inkább `SMTP over TLS` vagy `message submission over implicit TLS` a pontosabb megnevezés

## Mire figyelj?

Az SMTP:

- nem postafiók-olvasási protokoll
- nem mappaszinkronizálásra való

Erre továbbra is:

- `IMAP`
- `POP3`

használatos.

## Ne keverd össze

| Fogalom | Mire való? |
|---|---|
| SMTP | küldés és továbbítás |
| SMTPS | titkosított SMTP-jellegű beküldés |
| IMAP | postafiók szinkronizálása |
| POP3 | levelek letöltése |

## Vizsgán jól használható megfogalmazás

> Az SMTP a levelek küldésére és továbbítására szolgáló protokoll.  
> Kliensoldali levélbeküldésre ma gyakran a `587` portot használják, titkosított submissionhöz pedig elterjedt a `465` port is.  
> Az SMTP nem a levelek olvasására való, arra tipikusan IMAP vagy POP3 szolgál.

## Gyakori vizsgahibák

- Az SMTP-t olvasási protokollnak mondani.
- A `25`, `587` és `465` port szerepét összekeverni.
- Azt hinni, hogy a `SMTPS` minden kontextusban külön protokoll.
- Elfelejteni, hogy ma a titkosított beküldés az elvárt.

## Gyors önellenőrzés

1. Mire való az SMTP?
2. Melyik port a klasszikus SMTP relay port?
3. Melyik port a tipikus submission port?
4. Melyik portot társítják gyakran az SMTPS-hez?
5. Levelek olvasására SMTP-t használunk?

## Rövid válaszok az önellenőrzéshez

1. Küldésre és továbbításra
2. A `25`
3. A `587`
4. A `465`
5. Nem

## Források

1. RFC 5321 - Simple Mail Transfer Protocol  
   https://datatracker.ietf.org/doc/html/RFC5321  
   Használat: az SMTP elsődleges szabványforrása.

2. RFC 6409 - Message Submission for Mail  
   https://www.rfc-editor.org/rfc/rfc6409.html  
   Használat: a kliensoldali levélbeküldés (`587`) szerepéhez.

3. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Használat: modern ajánlás titkosított levélbeküldéshez, beleértve a `465` portot.

4. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Használat: hivatalos portregiszter a `25`, `465` és `587` portokhoz.

Megnyitva: `2026-04-08`
