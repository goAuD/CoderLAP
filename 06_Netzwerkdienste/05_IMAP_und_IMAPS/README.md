# IMAP und IMAPS

## Gyors vizuális kép

| Protokoll | Tipikus port | Fő cél |
|---|---|---|
| IMAP | `143` | szerveroldali postaláda-kezelés |
| IMAPS | `993` | ugyanez titkosítva |

## Mire jó az IMAP?

Az IMAP úgy működik, hogy a levelek alapvetően a szerveren maradnak, és a kliens:

- szinkronizál
- mappákat kezel
- állapotokat egyeztet

Ezért alkalmas például:

- laptop + telefon együttes használatára
- több kliens párhuzamos használatára

## Miért jobb sokszor, mint a POP3?

Mert az IMAP jobban kezeli:

- több eszközt
- közös állapotot
- szerveroldali mappákat
- keresést és rendezést

## Mi az IMAPS?

Az IMAPS az IMAP titkosított használata.

Ez azért fontos, mert így:

- a bejelentkezési adatok védettek
- a levélforgalom titkosított

## Mire figyelj?

Az IMAP:

- nem küldési protokoll
- nem helyettesíti az SMTP-t

Küldéshez továbbra is tipikusan:

- `SMTP`

szükséges.

## Ne keverd össze

| Fogalom | Mire való? |
|---|---|
| IMAP | szerveroldali postaláda-szinkron |
| IMAPS | IMAP titkosítva |
| POP3 | egyszerűbb letöltési modell |
| SMTP | levélküldés |

## Vizsgán jól használható megfogalmazás

> Az IMAP egy levelezési protokoll, amely a szerveren tárolt levelek és mappák szinkronizálására szolgál.  
> Több eszköz használatánál általában előnyösebb, mint a POP3,
> mert a levelek és állapotok központilag a szerveren maradnak.  
> Az IMAPS az IMAP TLS-sel védett, biztonságos változata.

## Gyakori vizsgahibák

- Az IMAP-ot küldési protokollnak mondani.
- Azt állítani, hogy az IMAP mindig letörli a levelet a szerverről.
- Nem tudni, hogy több eszköznél miért előnyös.
- Elfelejteni a portokat.

## Gyors önellenőrzés

1. Mire való az IMAP?
2. Melyik port az IMAP tipikus portja?
3. Melyik port az IMAPS tipikus portja?
4. Több eszközös használatra inkább IMAP vagy POP3 való?
5. Küldéshez elég az IMAP?

## Rövid válaszok az önellenőrzéshez

1. Postafiók szerveroldali kezelésére és szinkronizálására
2. A `143`
3. A `993`
4. Az IMAP
5. Nem

## Források

1. RFC 9051 - IMAP4rev2  
   https://www.rfc-editor.org/rfc/rfc9051.html  
   Használat: az IMAP modern elsődleges szabványforrása.

2. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Használat: modern ajánlás titkosított IMAP-hozzáféréshez, beleértve a `993` portot.

3. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Használat: hivatalos portregiszter a `143` és `993` portokhoz.

Megnyitva: `2026-04-08`
