# SOAP und WSDL

## Gyors vizuális kép

| Fogalom | Szerep |
|---|---|
| SOAP | XML-alapú üzenetküldés |
| WSDL | a szolgáltatás géppel olvasható leírása |

## Mi az a SOAP?

A `SOAP` (`Simple Object Access Protocol`) XML-alapú üzenetstruktúrát használó protokoll a rendszerek közötti kommunikációhoz.

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
- a SOAP ténylegesen továbbítja az XML-üzeneteket

Tehát:

- a WSDL inkább szerződés
- a SOAP inkább kommunikációs forma

## Miért volt fontos?

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
| adatcsere | tipikusan XML | gyakran JSON |
| leírás | formális szerződés, WSDL | nem kötelező egységes leíró nyelv |
| stílus | kötöttebb | könnyebb, webközelibb |

## Vizsgán jól használható megfogalmazás

> A SOAP egy XML-alapú üzenetküldési protokoll, amelyet web service kommunikációra használnak.  
> A WSDL ezzel szemben a szolgáltatás leírására szolgál: megadja a műveleteket, üzenettípusokat és elérési pontokat.  
> Klasszikus vállalati rendszerekben a SOAP és WSDL gyakran együtt jelent meg,
> mert pontos, formális szerződést
> és szabványos kommunikációt biztosítottak.

## Gyakori vizsgahibák

- A SOAP-ot és a WSDL-t ugyanannak nevezni.
- Azt mondani, hogy a WSDL maga küldi az adatot.
- Nem megemlíteni az XML szerepét.
- A SOAP-ot modern frontend API-k tipikus alapmegoldásának nevezni.

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
