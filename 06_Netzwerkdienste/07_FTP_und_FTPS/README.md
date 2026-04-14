# FTP und FTPS

## Gyors vizuális kép

| Protokoll | Tipikus port | Védelem |
|---|---|---|
| FTP | `21` | nincs megfelelő modern titkosítás |
| FTPS | `21` vagy `990` | TLS-védelem |

## Mi a FTP?

A FTP egy klasszikus protokoll fájlok átvitelére.

Jellemzői:

- külön vezérlő- és adatkapcsolat
- régi, de sok helyen még ismert technológia

Gyakori felhasználás:

- webtárhely feltöltés
- fájlok mozgatása szerver és kliens között

## Mi a gond a sima FTP-vel?

Az alap FTP-nél a forgalom és a hitelesítési adatok könnyen lehallgathatók lehetnek.

Ezért mai szemmel:

- önmagában nem tekinthető megfelelően biztonságosnak

## Mi az FTPS?

Az FTPS az FTP TLS-sel védett változata.

Két tipikus működési mód:

- explicit TLS
- implicit TLS

Vizsgaszinten elég ezt tudni:

- az FTPS a sima FTP-nél biztonságosabb, mert a kapcsolat titkosítható

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| FTP | fájlátvitel titkosítás nélkül |
| FTPS | FTP TLS-sel |
| SFTP | SSH-alapú másik protokoll, nem ugyanaz mint FTPS |

## Miért fontos?

Mert sokan összekeverik:

- `FTPS`
- `SFTP`

Pedig ezek nem ugyanazok.

## Vizsgán jól használható megfogalmazás

> Az FTP klasszikus fájlátviteli protokoll kliens és szerver között.  
> A sima FTP nem nyújt megfelelő modern titkosítást,
> ezért biztonságosabb alternatíva az FTPS,
> amely TLS-sel védi a kapcsolatot.  
> Az FTPS nem ugyanaz, mint az SSH-alapú SFTP.

## Gyakori vizsgahibák

- Azt mondani, hogy az FTP önmagában biztonságos.
- Az FTPS-t és az SFTP-t összekeverni.
- Nem megemlíteni, hogy az FTP külön adat- és vezérlőkapcsolatot használhat.
- Elfelejteni a `21` portot.

## Gyors önellenőrzés

1. Mire való az FTP?
2. Melyik port a tipikus FTP-port?
3. Mi a fő különbség az FTP és FTPS között?
4. Ugyanaz az FTPS és az SFTP?
5. Miért problémás a sima FTP?

## Rövid válaszok az önellenőrzéshez

1. Fájlátvitelre
2. A `21`
3. Az FTPS TLS-t használ
4. Nem
5. Mert nincs megfelelő modern titkosítása

## Források

1. RFC 959 - File Transfer Protocol  
   https://www.rfc-editor.org/rfc/rfc959  
   Használat: az FTP klasszikus elsődleges szabványforrása.

2. RFC 4217 - Securing FTP with TLS  
   https://www.rfc-editor.org/rfc/rfc4217  
   Használat: az FTPS elsődleges szabványforrása.

3. MDN - FTP  
   https://developer.mozilla.org/en-US/docs/Glossary/FTP  
   Használat: rövid, modern technikai összefoglaló FTP-ről és biztonsági kontextusáról.

4. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Használat: hivatalos portregiszter a `21` és `990` portokhoz.

Megnyitva: `2026-04-08`
