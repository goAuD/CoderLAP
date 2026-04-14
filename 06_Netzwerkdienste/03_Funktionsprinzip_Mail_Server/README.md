# Funktionsprinzip Mail Server

## Gyors vizuális kép

| Szereplő | Feladat |
|---|---|
| felhasználó / MUA | levelet ír, olvas |
| mail submission server | a kliens ide adja fel a levelet |
| mail transfer server | továbbítja más szerverek felé |
| mailbox server | tárolja a bejövő leveleket |

## Hogyan megy ki egy e-mail?

Tipikus folyamat:

1. a felhasználó a kliensben megírja a levelet
2. a kliens SMTP-n keresztül beküldi a levelet a kiszolgálónak
3. a szerver továbbítja a címzett domainjének levelezőszerveréhez
4. a címzett szervere eltárolja a levelet

## Hogyan olvassa el a címzett?

A címzett levelezőprogramja a szerverhez csatlakozik, és a leveleket általában:

- `IMAP`-pal szinkronizálja
- vagy `POP3`-mal letölti

## Miért nem elég csak az SMTP?

Mert az SMTP alapvetően:

- levélküldésre és továbbításra való

Nem erre való:

- kényelmes postafiók-szinkronizálásra
- levelek szerveroldali mappakezelésére

Ezért van külön:

- `IMAP`
- `POP3`

## Miért fontos ez?

Mert vizsgán gyakori kérdés:

- melyik protokoll mire való
- hogyan jut el az e-mail A-ból B-be

## Ne keverd össze

| Fogalom | Mire való? |
|---|---|
| SMTP | levélküldés és továbbítás |
| IMAP | szerveren tárolt levelek szinkronizálása |
| POP3 | levelek letöltése |

## Vizsgán jól használható megfogalmazás

> A levelezőrendszer több komponensből áll.  
> A felhasználó klienssel ír és olvas levelet,
> a levél beküldése és továbbítása SMTP-vel történik,
> a bejövő levelek elérésére pedig jellemzően IMAP vagy POP3 szolgál.  
> A mail server tehát nemcsak tárol, hanem fogad, továbbít és kiszolgál is.

## Gyakori vizsgahibák

- Azt mondani, hogy az SMTP-vel "olvasunk" levelet.
- Az IMAP-ot és a POP3-at küldési protokollnak gondolni.
- Nem felismerni, hogy több szerver is részt vehet a továbbításban.

## Gyors önellenőrzés

1. Melyik protokollt használjuk tipikusan levélküldésre?
2. Melyik kettőt használjuk tipikusan levélolvasásra?
3. Mi a különbség az SMTP és az IMAP között?
4. Egy e-mail átmehet több szerveren is?
5. A mailbox server mire való?

## Rövid válaszok az önellenőrzéshez

1. Az SMTP-t
2. Az IMAP-ot és a POP3-at
3. Az SMTP küld, az IMAP postafiókot kezel és szinkronizál
4. Igen
5. A levelek tárolására és kiszolgálására

## Források

1. RFC 5321 - Simple Mail Transfer Protocol  
   https://datatracker.ietf.org/doc/html/RFC5321  
   Használat: az SMTP elsődleges szabványforrása.

2. RFC 6409 - Message Submission for Mail  
   https://www.rfc-editor.org/rfc/rfc6409.html  
   Használat: a kliensoldali beküldés (`submission`) mai szerepéhez.

3. RFC 9051 - IMAP4rev2  
   https://www.rfc-editor.org/rfc/rfc9051.html  
   Használat: modern IMAP-alapdefiníció és a szerveroldali postaláda-kezelés megértéséhez.

4. RFC 1939 - POP3  
   https://www.rfc-editor.org/rfc/rfc1939.html  
   Használat: a POP3 klasszikus alapdefiníciója.

Megnyitva: `2026-04-08`
