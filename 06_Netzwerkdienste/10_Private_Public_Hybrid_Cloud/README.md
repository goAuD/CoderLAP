# Private Public Hybrid Cloud

## Lényeg 30 másodpercben

A cloudnak több telepítési modellje van.

Vizsgán a három legfontosabb:

- `private cloud`
- `public cloud`
- `hybrid cloud`

Röviden:

- `private` = dedikáltabb, szervezeten belüli vagy dedikált környezet
- `public` = nyilvános cloudszolgáltatónál igénybe vett erőforrás
- `hybrid` = a kettő kombinációja

## Gyors vizuális kép

| Modell | Lényeg |
|---|---|
| private cloud | egy szervezetnek dedikáltabb cloudkörnyezet |
| public cloud | külső szolgáltató által nyújtott cloud |
| hybrid cloud | private + public együtt |

## Mi a private cloud?

A private cloud olyan cloudkörnyezet, amely:

- egyetlen szervezethez kapcsolódik
- erősebben kontrollált
- gyakran belső vagy dedikált erőforrásokra épül

Előny lehet:

- nagyobb kontroll
- speciális compliance- vagy adatvédelmi igények kezelése

## Mi a public cloud?

A public cloudnál:

- egy külső szolgáltató biztosítja az infrastruktúrát
- az erőforrások hálózaton keresztül érhetők el
- a szolgáltatás jellemzően rugalmasan bővíthető

Tipikus példák:

- AWS
- Microsoft Azure
- Google Cloud

## Mi a hybrid cloud?

A hybrid cloud azt jelenti, hogy:

- egy szervezet private és public megoldásokat együtt használ

Például:

- érzékeny adatok private környezetben maradnak
- a skálázódó webalkalmazás public cloudban fut

## Miért fontos ez?

Mert a megfelelő modell kiválasztása függhet:

- költségtől
- kontrolligénytől
- adatvédelemtől
- meglévő infrastruktúrától

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| private cloud | dedikáltabb szervezeti cloudkörnyezet |
| public cloud | nyilvános szolgáltatói cloud |
| hybrid cloud | több modell kombinációja |
| on-premises | helyben üzemeltetett rendszer, nem feltétlenül cloud |

## Vizsgán jól használható megfogalmazás

> A private, public és hybrid cloud a cloud telepítési modelljei.  
> A private cloud egy szervezethez kötött, nagyobb kontrollt adó környezet, a public cloud külső szolgáltató által biztosított megoldás, míg a hybrid cloud ezek kombinációja.  
> A választásnál fontos szempont a költség, a rugalmasság, a biztonság és a compliance.

## Gyakori vizsgahibák

- A private cloudot sima lokális szervernek nevezni minden további nélkül.
- A hybrid cloudot egyszerű backup-megoldásnak gondolni.
- Nem felismerni, hogy a public cloudnál is marad ügyféloldali felelősség.
- A deployment modellt összekeverni a szolgáltatási modellel.

## Gyors önellenőrzés

1. Mi a private cloud lényege?
2. Mi a public cloud lényege?
3. Mi a hybrid cloud?
4. Deployment modell vagy szolgáltatási modell a public/private/hybrid?
5. Mondj két választási szempontot.

## Rövid válaszok az önellenőrzéshez

1. Dedikáltabb, szervezethez kötött cloudkörnyezet
2. Külső szolgáltató által nyújtott cloud
3. Private és public kombinációja
4. Deployment modell
5. Például költség és compliance

## Források

1. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Használat: a deployment modellek (`private`, `public`, `hybrid`) elsődleges definíciói.

2. NIST SP 800-146 - Cloud Computing Synopsis and Recommendations  
   https://csrc.nist.gov/pubs/sp/800/146/final  
   Használat: gyakorlati háttér a deployment modellek előnyeihez és kockázataihoz.

3. AWS - What is a Public Cloud?  
   https://aws.amazon.com/what-is/public-cloud/  
   Használat: közérthető, mai public cloud összefoglaló.

4. AWS - What is Hybrid Cloud Computing?  
   https://aws.amazon.com/what-is/hybrid-cloud-computing/  
   Használat: gyakorlati magyarázat hybrid cloud használati mintákhoz.

Megnyitva: `2026-04-08`
