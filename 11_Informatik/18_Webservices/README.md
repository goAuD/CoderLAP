# Webservices

## Gyors vizuális kép

| Szereplő | Feladat |
|---|---|
| szolgáltató | biztosítja a funkciót vagy adatot |
| kliens / requester | meghívja a szolgáltatást |
| interfész | meghatározza, hogyan lehet használni |
| üzenet | az adat, amit küldünk vagy kapunk |

## Mi az a web service?

A web service egy olyan szoftveres szolgáltatás, amely hálózaton keresztül érhető el, és meghatározott módon lehet vele kommunikálni.

Gyakori tulajdonságai:

- van címe vagy elérési pontja
- van meghívási módja
- van adatcsere-formátuma
- van valamilyen szerződése vagy leírása

## Mire használják?

- különböző rendszerek összekötése
- adatcsere
- külső szolgáltatások használata
- integráció vállalati rendszerek között
- mobilapp és backend összekapcsolása

## Milyen formában találkozunk vele?

A gyakorlatban gyakori:

- `SOAP` alapú web service
- `REST` jellegű webes API

Ezért sokszor a web service és az API fogalma részben átfed, de nem teljesen ugyanaz.

## Web service és API: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| API | általános programozási interfész |
| web service | hálózaton, webes technológiákkal elérhető szolgáltatás |

Minden web service tekinthető API-nak, de nem minden API web service.

## Tipikus összetevők

- endpoint
- protokoll
- üzenetformátum
- hívási szabályok
- hibakezelés
- biztonsági megoldások

## Miért fontos?

Mert a modern szoftverrendszerek ritkán állnak teljesen önmagukban.

A web service lehetővé teszi, hogy:

- külön komponensek együttműködjenek
- újrahasznosítható funkciókat adjunk
- szolgáltatásalapú rendszereket építsünk

## Vizsgán jól használható megfogalmazás

> A web service olyan hálózaton keresztül elérhető szolgáltatás, amelyet más programok szabályozott módon hívhatnak meg.  
> Fő célja a rendszerek közötti kommunikáció és integráció.  
> A gyakorlatban tipikusan valamilyen webes protokollt és strukturált üzenetformátumot használ, például SOAP-ot vagy REST-alapú HTTP-kommunikációt.

## Gyakori vizsgahibák

- A web service-t sima weboldalnak nevezni.
- Összekeverni az emberi felhasználói felülettel.
- Nem megemlíteni a rendszer-rendszer kommunikációt.
- A REST-et és SOAP-ot teljesen ugyanannak bemutatni.

## Gyors önellenőrzés

1. Mi a web service fő célja?
2. Kik használják tipikusan?
3. Miért fontos a rendszerek integrációjában?
4. Mi a kapcsolata az API-val?
5. Mondj két gyakori megközelítést.

## Rövid válaszok az önellenőrzéshez

1. Gépi kommunikáció rendszerek között
2. Más programok és rendszerek
3. Mert szabályozott adatcserét tesz lehetővé
4. A web service egy speciális, hálózaton elérhető API-fajta
5. SOAP és REST

## Források

1. W3C - Web Services Architecture  
   https://www.w3.org/TR/ws-arch/wsa.pdf  
   Használat: hivatalos fogalmi háttér a web services architektúrához és szereplőihez.

2. MDN - API  
   https://developer.mozilla.org/en-US/docs/Glossary/API  
   Használat: az API fogalom tisztázása, hogy a web service-t jól lehessen elhelyezni.

3. W3C - Web Services Description Language (WSDL) Version 2.0 Part 0: Primer  
   https://www.w3.org/TR/wsdl20-primer/  
   Használat: gyakorlati kontextus a klasszikus web service ökoszisztémához.

Megnyitva: `2026-04-08`
