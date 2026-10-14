# POP3 und POP3S

## Gyors vizuális kép

| Protokoll | Tipikus port | Fő cél |
|---|---|---|
| POP3 | `110` | levelek letöltése |
| POP3S | `995` | levelek letöltése titkosítva |

## Mire jó a POP3?

A POP3 arra való, hogy a kliens:

- csatlakozzon a szerverhez
- letöltse a leveleket

Hagyományosan a POP3-modell inkább ilyen:

- "vedd le a levelet a szerverről a gépemre"

Ezért egyszerű, de több eszköznél kevésbé kényelmes.

## Mire kell figyelni?

A POP3 általában kevésbé alkalmas erre:

- több eszköz közötti szinkron
- szerveroldali mappák kezelése
- komplex levelezési munkafolyamat

Erre sokszor jobb az `IMAP`.

## Mi a POP3S?

A POP3S a POP3 titkosított használata.

Ez azt jelenti:

- a kapcsolat TLS-en keresztül védett
- a bejelentkezési adatok és a forgalom nem mennek egyszerűen olvasható cleartext formában

## Miért fontos a titkosítás?

Mert levelezésnél érzékeny lehet:

- a jelszó
- a levél tartalma
- a csatolmány

Ezért ma a titkosított kapcsolat az elvárt megoldás.

## Ne keverd össze

| Fogalom | Mire való? |
|---|---|
| POP3 | levelek letöltése |
| POP3S | POP3 titkosítva |
| IMAP | szerveroldali szinkronizálás |
| SMTP | küldés és továbbítás |

## Kidolgozott eset: hol marad a levél?

Egy kliens POP3-mal letölt három levelet. A letöltés önmagában nem kötelező törlés: a kliens beállítható úgy, hogy másolatot hagyjon a szerveren. A POP3 `DELE` parancsa törlésre jelöl, a rendes `QUIT` utáni frissítési szakasz végzi a törlést. A szolgáltató megőrzési szabálya ettől külön kérdés.

Ha a laptop már eltávolította a levelet a szerverről, a később csatlakozó telefon nem tudja ugyanonnan letölteni. A helyben tárolt üzenetekhez külön mentés kell. Két eszköz közös olvasottsági állapotához és mappáihoz ezért jellemzően az IMAP a célszerűbb választás.

POP3S-nél a `995` porton rögtön TLS indul. A `110` porton az `STLS` kiterjesztés válthat TLS-re. A kliensnek sikeres TLS-t és érvényes tanúsítványt kell megkövetelnie a hitelesítési adatok küldése előtt; a portszám önmagában nem teljes biztonsági beállítás.

## Vizsgán jól használható megfogalmazás

> A POP3 egy levelezési protokoll, amely a bejövő e-mailek letöltésére szolgál.  
> Egyszerű modellje miatt elsősorban helyi letöltésre alkalmas,
> míg több eszközös szinkronhoz az IMAP gyakran jobb választás.  
> A POP3S a POP3 TLS-sel védett változata, ezért biztonságosabb.

## Gyors önellenőrzés

1. Mire való a POP3?
2. Melyik port tartozik tipikusan a POP3-hoz?
3. Melyik port tartozik tipikusan a POP3S-hez?
4. Mi a fő különbség a POP3 és POP3S között?
5. Több eszközös szinkronhoz gyakran melyik jobb: POP3 vagy IMAP?

## Rövid válaszok az önellenőrzéshez

1. Bejövő levelek letöltésére
2. A `110`
3. A `995`
4. POP3S esetén a TLS azonnal indul; a 110-es POP3-kapcsolat is védhető STLS-frissítéssel, ha támogatott és megkövetelt
5. Az IMAP

## Források

1. RFC 1939 - Post Office Protocol - Version 3  
   https://www.rfc-editor.org/rfc/rfc1939.html  
   Használat: a POP3 elsődleges szabványforrása.

2. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Használat: modern, titkosított e-mail-hozzáférési ajánlás, beleértve a `995` portot is.

3. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Használat: hivatalos portregiszter a `110` és `995` portokhoz.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [RFC 1939: POP3](https://www.rfc-editor.org/rfc/rfc1939.html): letöltés, törlésjelölés, UPDATE állapot.
- [RFC 2595: TLS with IMAP, POP3 and ACAP](https://www.rfc-editor.org/rfc/rfc2595.html): POP3 STLS mechanizmus, a korszerű TLS-beállításokkal együtt értelmezve.

Ellenőrizve: `2026-10-14`.
