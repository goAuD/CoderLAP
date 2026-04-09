# HTTP und HTTPS

## Lényeg 30 másodpercben

A `HTTP` a web alap protokollja.

Feladata:

- kliens és szerver közötti kérés-válasz kommunikáció

A `HTTPS` nem külön "másik web", hanem:

- **HTTP TLS-sel védve**

Röviden:

- `HTTP` = titkosítás nélkül
- `HTTPS` = titkosított, hitelesített kapcsolat

## Gyors vizuális kép

| Protokoll | Port | Védelem |
|---|---|---|
| HTTP | `80` | nincs beépített titkosítás |
| HTTPS | `443` | TLS védi |

## Mi a HTTP?

A HTTP egy stateless, azaz állapotmentes kérés-válasz protokoll.

A tipikus folyamat:

1. a kliens kérést küld
2. a szerver választ ad
3. a válasz tartalmazhat HTML-t, JSON-t, képet vagy más tartalmat

Példák HTTP-metódusokra:

- `GET`
- `POST`
- `PUT`
- `DELETE`

## Mi a HTTPS?

A HTTPS azt jelenti, hogy a HTTP-forgalom TLS-en keresztül megy.

Ez három fontos dolgot ad:

- titkosítás
- integritásvédelem
- szerverhitelesítés

Ezért a HTTPS védi a forgalmat például:

- lehallgatás ellen
- egyszerű módosítás ellen
- hamis szerver elleni védelemben is segít

## Miért fontos?

Mert ma gyakorlatban a weben:

- bejelentkezésnél
- űrlapoknál
- fizetésnél
- API-hívásoknál

a HTTPS az alapelvárás.

## Mit nem tud a HTTPS?

Nem jelent automatikusan teljes biztonságot.

Például nem oldja meg önmagában:

- a gyenge jelszavakat
- a hibás jogosultságkezelést
- az XSS vagy SQL injection típusú alkalmazáshibákat

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| HTTP | webes kérés-válasz protokoll |
| HTTPS | HTTP TLS-sel védve |
| TLS | a kapcsolatot védő biztonsági protokoll |
| SSL | régi, elavult elődnév |

## Vizsgán jól használható megfogalmazás

> A HTTP a weben használt alapvető kérés-válasz protokoll.  
> A HTTPS ugyanez a protokoll TLS-védelemmel, ezért biztosítja az adatforgalom titkosítását, sértetlenségét és a szerver hitelesítését.  
> Gyakorlatban a modern webes szolgáltatásoknál a HTTPS a standard.

## Gyakori vizsgahibák

- Azt mondani, hogy a HTTPS teljesen más protokoll, mint a HTTP.
- A HTTP-t titkosítottnak gondolni.
- A TLS-t és az SSL-t mai értelemben szinonimaként kezelni.
- Elfelejteni a portokat.

## Gyors önellenőrzés

1. Mi a HTTP fő feladata?
2. Mi a különbség a HTTP és HTTPS között?
3. Melyik port a tipikus HTTP-port?
4. Melyik port a tipikus HTTPS-port?
5. A HTTPS önmagában minden alkalmazáshibát megold?

## Rövid válaszok az önellenőrzéshez

1. Kérés-válasz kommunikáció a weben
2. A HTTPS HTTP TLS-védelemmel
3. A `80`
4. A `443`
5. Nem

## Források

1. RFC 9110 - HTTP Semantics  
   https://www.rfc-editor.org/rfc/rfc9110  
   Használat: a HTTP szemantikájának elsődleges szabványforrása.

2. RFC 9114 - HTTP/3  
   https://www.rfc-editor.org/rfc/rfc9114  
   Használat: modern HTTP-verziók kontextusához és a mai HTTP-család megértéséhez.

3. MDN - Overview of HTTP  
   https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview  
   Használat: gyakorlati, fejlesztőbarát HTTP-összefoglaló.

4. MDN - HTTP  
   https://developer.mozilla.org/en-US/docs/Glossary/HTTP  
   Használat: rövid definíció HTTP-re és HTTPS-re.

5. MDN - Transport Layer Security (TLS)  
   https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security  
   Használat: a HTTPS mögötti TLS szerepének modern magyarázata.

6. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Használat: hivatalos portregiszter a `80` és `443` portokhoz.

Megnyitva: `2026-04-08`
