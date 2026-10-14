# SMTP und SMTPS

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

## Kidolgozott beállítás és válaszértelmezés

Egy kliens a szolgáltató által megadott beküldési kiszolgálót használja. `465`-ön a TLS-kézfogás azonnal kezdődik, `587`-en a `STARTTLS` emeli TLS-re a kapcsolatot. A `587` tehát szintén lehet titkosított; a kliensben kötelezővé tesszük a sikeres TLS-t, nem engedünk csendes visszaesést védtelen küldésre. A felhasználó hitelesítése külön lépés.

| Szemléltető SMTP-válasz | Jelentés és következő lépés |
| --- | --- |
| `250` | a parancs sikeres; a teljes üzenet átvétele után kézbesítési felelősség átvétele |
| `451` | átmeneti feldolgozási hiba; későbbi újrapróbálás lehet indokolt |
| `550` | végleges elutasítás; a részletes üzenetet és címzést ellenőrizzük |

A `250` jelentése a parancs helyétől is függ, és nem olvasási visszaigazolás. Szerverek között tipikusan `25`-ös porton történik a továbbítás, ott is használható STARTTLS. A küldő fiók védelme és a nyílt továbbítás (`open relay`) megakadályozása külön feladat az átviteli titkosítás mellett.

## Vizsgán jól használható megfogalmazás

> Az SMTP a levelek küldésére és továbbítására szolgáló protokoll.  
> Kliensoldali levélbeküldésre ma gyakran a `587` portot használják,
> titkosított submissionhöz pedig elterjedt a `465` port is.  
> Az SMTP nem a levelek olvasására való, arra tipikusan IMAP vagy POP3 szolgál.

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

### A bővítés ellenőrzött forrásai

- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321.html): MX-kézbesítés és válaszosztályok.
- [RFC 8314: TLS for email](https://www.rfc-editor.org/rfc/rfc8314.html): implicit TLS, STARTTLS és tanúsítvány-ellenőrzés.

Ellenőrizve: `2026-10-14`.
