# SOAP und WSDL

## Gyors vizuális kép

| Fogalom | Szerep |
|---|---|
| SOAP | XML-alapú üzenetküldés |
| WSDL | a szolgáltatás géppel olvasható leírása |

## Mi az a SOAP?

A `SOAP` XML-alapú üzenetstruktúrát használó protokoll a rendszerek közötti kommunikációhoz. A `Simple Object Access Protocol` történeti névfeloldás; a SOAP 1.2 szabvány már nem rövidítésként kezeli a nevet.

Jellemzői:

- XML-alapú
- strukturált üzenet
- formálisabb és kötöttebb felépítés
- gyakran vállalati integrációkban használják

Tipikus elemek:

- envelope
- header
- body

## Mi az a WSDL?

A `WSDL` (`Web Services Description Language`) leírja, hogyan lehet egy szolgáltatást használni.

Általában megadja:

- milyen műveletek érhetők el
- milyen üzeneteket vár
- milyen válaszokat ad
- milyen címen érhető el
- milyen kötésen keresztül használható

## Mi a kapcsolat közöttük?

A klasszikus modellben:

- a WSDL leírja a szolgáltatást
- a SOAP meghatározza az XML-üzenetek felépítését és feldolgozását

Tehát:

- a WSDL inkább szerződés
- a SOAP inkább kommunikációs forma

## Miért fontos vállalati integrációkban?

Mert erősen szabványosított és pontos működést tesz lehetővé:

- formális interfész
- egyértelmű szerződés
- enterprise környezetben jól kezelhető
- eszközökkel generálható kliens és szerveroldali kód

## Mi a hátránya?

- nehezebb és "beszédesebb", mint a modern, könnyű HTTP+JSON megoldások
- az XML hosszabb és összetettebb
- sok esetben túl nehéz egyszerű webes integrációhoz

## SOAP/WSDL és REST: ne keverd össze

| Szempont | SOAP/WSDL | REST |
|---|---|---|
| adatcsere | XML-alapú SOAP-üzenet | gyakran JSON, de nem kötött formátum |
| leírás | formális szerződés, WSDL | nem kötelező egységes leíró nyelv |
| stílus | kötöttebb | könnyebb, webközelibb |

## Egy SOAP-üzenet és a hozzá tartozó szerződés

Ez egy szemléltető **SOAP 1.2** XML-üzenet, nem önmagában futtatható program:

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope"
              xmlns:c="urn:example:courses">
  <env:Body>
    <c:GetCourse>
      <c:id>15</c:id>
    </c:GetCourse>
  </env:Body>
</env:Envelope>
```

Az `Envelope` a teljes üzenet kerete, a kötelező `Body` az alkalmazás adatait
tartalmazza. A `Header` opcionális, ezért itt nincs. A `c:GetCourse` és `c:id`
saját példabeli elemek, nem a SOAP szabvány által definiált kurzusműveletek.
A névterek választják el az alkalmazás és a protokoll elemeit.

A WSDL-szerződés leírhatja, milyen bemenetet és választ vár ez a művelet,
milyen típusa van az azonosítónak, melyik cím és protokollkötés használható.
A WSDL 1.1 és 2.0 eltérő szerkezetű, ezért a kódgenerátorhoz a szolgáltatás
valós verzióját választjuk. Egy szolgáltatáshiba strukturált SOAP `Fault`
üzenetként is érkezhet, amit külön fel kell dolgozni.

A SOAP üzenetformátumot és feldolgozási szabályokat ad. A tényleges továbbítást
például HTTP biztosítja, de a SOAP nem kizárólag HTTP-hez köthető. Az alap SOAP
önmagában nem titkosít és nem ad teljes hitelesítési megoldást. Az integráció
szerződéséhez a biztonsági beállítások is hozzátartoznak.

## Vizsgán jól használható megfogalmazás

> A SOAP egy XML-alapú üzenetküldési protokoll, amelyet web service kommunikációra használnak.  
> A WSDL ezzel szemben a szolgáltatás leírására szolgál: megadja a műveleteket, üzenettípusokat és elérési pontokat.  
> Vállalati rendszerekben a SOAP és WSDL gyakran együtt használatos,
> mert pontos, formális szerződést
> és szabványos kommunikációt biztosítanak.

## Gyors önellenőrzés

1. Mi a SOAP szerepe?
2. Mi a WSDL szerepe?
3. Mi a kapcsolat közöttük?
4. Miért kedvelték vállalati környezetben?
5. Miben más, mint a REST?

## Rövid válaszok az önellenőrzéshez

1. XML-alapú üzenetküldés
2. A szolgáltatás leírása
3. A WSDL leír, a SOAP kommunikál
4. Mert formális és szabványos
5. Nehezebb és kötöttebb, gyakran XML-es

## Források

Ellenőrizve: `2026-10-14`.

- [W3C: SOAP 1.2](https://www.w3.org/TR/soap12-part1/): Envelope, opcionális Header, Body, Fault és protokollkötés.
- [W3C: WSDL 2.0 Primer](https://www.w3.org/TR/wsdl20-primer/): szerződés, típusok, binding és verzió.


1. W3C - SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)  
   https://www.w3.org/TR/soap12-part1/  
   Használat: hivatalos SOAP-szabvány az üzenetstruktúra és szerep megértéséhez.

2. W3C - Web Services Description Language (WSDL) Version 2.0 Part 0: Primer  
   https://www.w3.org/TR/wsdl20-primer/  
   Használat: hivatalos, könnyebben érthető bevezetés a WSDL szerepéhez.

3. W3C - Web Services Architecture  
   https://www.w3.org/TR/ws-arch/wsa.pdf  
   Használat: a SOAP/WSDL tágabb web service környezetbe helyezéséhez.

Megnyitva: `2026-04-08`
