# SSL

## Gyors vizuális kép

| Fogalom | Mai helyzet |
|---|---|
| SSL 2.0 / 3.0 | elavult, nem ajánlott |
| TLS 1.2 / 1.3 | modern, használatos |
| "SSL certificate" | hétköznapi, de technikailag pontatlan megnevezés |

## Mi volt az SSL?

Az SSL egy régebbi biztonsági protokollcsalád volt, amely a hálózati kapcsolat védelmét célozta.

Feladata hasonló volt a mai TLS-éhez:

- titkosítás
- integritás
- hitelesítés

## Miért nem ezt használjuk ma?

Mert az SSL régi verziói:

- gyenge vagy elavult megoldásokat tartalmaznak
- ismert biztonsági problémáik vannak

Ezért a modern rendszerekben a helyes megközelítés:

- `TLS`

## Mi a kapcsolat a HTTPS-sel?

A HTTPS ma gyakorlatban:

- HTTP TLS-sel

nem pedig "HTTP SSL-lel" a szó modern, pontos értelmében.

## Miért fontos ezt tisztán látni?

Mert vizsgán gyakran előkerül:

- "Mi az SSL?"
- "Mi a különbség az SSL és TLS között?"

A jó válasz lényege:

- az SSL történeti fogalom
- a TLS a mai helyes, modern protokoll

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| SSL | régi, elavult biztonsági protokoll |
| TLS | a mai, modern megoldás |
| HTTPS | HTTP TLS-sel védve |
| tanúsítvány | hitelesítési lánc része, nem maga a protokoll |

## Vizsgán jól használható megfogalmazás

> Az SSL a Secure Sockets Layer rövidítése, de ma már elavult technológia.  
> A modern rendszerekben helyette a TLS használatos, ezért a HTTPS valójában HTTP TLS-védelemmel.  
> A hétköznapokban az "SSL" szó még gyakran megmaradt, de technikailag a TLS a helyes mai fogalom.

## Gyakori vizsgahibák

- Azt mondani, hogy az SSL ma is a korszerű standard.
- A TLS-t és az SSL-t pontosan ugyanannak tekinteni.
- A tanúsítványt összekeverni a teljes protokollal.
- Azt hinni, hogy az SSL csak weboldalaknál létezik.

## Gyors önellenőrzés

1. Mit jelent az SSL rövidítés?
2. Használjuk-e ma modern ajánlásként az SSL-t?
3. Mi a mai helyes modern megfelelő?
4. Mit jelent hétköznapokban gyakran az "SSL certificate"?
5. A HTTPS ma SSL-re vagy TLS-re épül?

## Rövid válaszok az önellenőrzéshez

1. Secure Sockets Layer
2. Nem
3. A TLS-t
4. Többnyire TLS-tanúsítványt
5. TLS-re

## Források

1. RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3  
   https://www.rfc-editor.org/rfc/rfc8446  
   Használat: a mai modern TLS elsődleges szabványforrása.

2. MDN - TLS  
   https://developer.mozilla.org/en-US/docs/Glossary/TLS  
   Használat: rövid, modern technikai magyarázat a TLS szerepéről.

3. MDN - SSL  
   https://developer.mozilla.org/en-US/docs/Glossary/SSL  
   Használat: tömör összefoglaló arról, hogy az SSL történeti fogalom és ma már TLS a helyes.

4. MDN - Transport Layer Security (TLS)  
   https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security  
   Használat: gyakorlati háttér a TLS működéséhez és a webes biztonsághoz.

Megnyitva: `2026-04-08`
