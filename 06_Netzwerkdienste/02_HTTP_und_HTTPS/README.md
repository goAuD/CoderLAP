# HTTP und HTTPS

## Gyors vizuális kép

| Protokoll | Teljes név | Port | Védelem |
|---|---|---|---|
| HTTP | Hypertext Transfer Protocol | `80` | nincs beépített titkosítás |
| HTTPS | Hypertext Transfer Protocol Secure | `443` | TLS védi |

## Mi a HTTP?

A HTTP – teljes nevén **Hypertext Transfer Protocol** – egy stateless, azaz állapotmentes kérés-válasz protokoll.

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

A HTTPS – teljes nevén **Hypertext Transfer Protocol Secure** – azt jelenti, hogy a HTTP-forgalom TLS-en keresztül megy.

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

## Kidolgozott kérés-válasz példa

Az alábbi HTTP/1.1-részlet egy feladat lekérdezését szemlélteti. HTTPS használatakor ez az alkalmazási adat a védett kapcsolaton halad; a példa nem élő szervernek küldendő parancs.

```http
GET /api/tasks/7 HTTP/1.1
Host: example.org
Accept: application/json
```

Siker esetén `200 OK` és például `{"id":7,"done":false}` JSON-törzs érkezhet, `Content-Type: application/json` fejléccel. Nem létező feladatnál `404`, hiányzó vagy nem megfelelő hitelesítésnél `401`, tiltott műveletnél `403` lehet a megfelelő válasz a konkrét API szabályai szerint.

A `GET` olvasásra szolgál; a `POST` gyakran létrehozást vagy műveletet indít. A `PUT` és `DELETE` szemantikája idempotens: ugyanazt a kérést ismételve a kívánt szerveroldali hatás nem halmozódik. Ez nem garantál azonos válaszszöveget vagy státuszkódot.

Az állapotmentes HTTP mellett az alkalmazás sütivel vagy tokennel fenntarthat munkamenetet. A HTTPS a kapcsolatot védi és megfelelő tanúsítvány-ellenőrzéssel a kiszolgáló nevét hitelesíti; a weboldal állításainak igazságát nem igazolja. HTTP/3 esetén a szállítás QUIC-ra épül, TLS 1.3 integrációval.

## Vizsgán jól használható megfogalmazás

> A HTTP (Hypertext Transfer Protocol) a weben használt alapvető kérés-válasz protokoll.  
> A HTTPS (Hypertext Transfer Protocol Secure) ugyanez a protokoll TLS-védelemmel,
> ezért biztosítja az adatforgalom titkosítását,
> sértetlenségét és a szerver hitelesítését.
> Gyakorlatban a modern webes szolgáltatásoknál a HTTPS a standard.

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

### A bővítés ellenőrzött forrásai

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): metódusok, idempotencia és válaszkódok.
- [RFC 9114: HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html): QUIC-alapú HTTP.

Ellenőrizve: `2026-10-14`.
