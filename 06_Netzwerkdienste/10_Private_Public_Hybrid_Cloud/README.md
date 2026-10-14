# Private Public Hybrid Cloud

## Gyors vizuális kép

| Modell | Lényeg |
|---|---|
| private cloud | egy szervezet kizárólagos használatára szánt cloud |
| public cloud | a széles nyilvánosság számára igénybe vehető cloudszolgáltatás |
| hybrid cloud | private + public együtt |

## Mi a private cloud?

A private cloud olyan cloudkörnyezet, amely:

- egyetlen szervezet kizárólagos használatára van kialakítva
- erősebben kontrollált
- gyakran belső vagy dedikált erőforrásokra épül

Előny lehet:

- nagyobb kontroll
- speciális compliance- vagy adatvédelmi igények kezelése

## Mi a public cloud?

A public cloudnál:

- a szolgáltatás a széles nyilvánosság számára elérhető, megfelelő szerződéssel és fiókkal
- az erőforrások hálózaton keresztül érhetők el
- a szolgáltatás jellemzően rugalmasan bővíthető

Tipikus példák:

- AWS
- Microsoft Azure
- Google Cloud

## Mi a hybrid cloud?

A hybrid cloud azt jelenti, hogy:

- különálló cloudkörnyezeteket, például private és public cloudot, adat- vagy alkalmazáshordozhatóságot biztosító technológia kapcsol össze

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

## A tulajdonos, a helyszín és a hozzáférés külön kérdés

Private cloudot külső cég is üzemeltethet saját adatközpontjában, ha az adott környezet egy szervezet kizárólagos használatára szolgál. Az on-premises a helyszínre, a private/public a használati modellre utal. Public cloud esetén az ügyfél adatai és VM-jei ettől még nem nyilvánosan hozzáférhetők.

**Kidolgozott eset:** az iskola saját private cloudban tartja a gyakorló adatbázist, és ellenőrzött kapcsolaton public cloud erőforrásokkal bővíti egy alkalmazás kapacitását. Itt a kapcsolat és a hordozható munkaterhelés adja a hibrid működés lényegét. Egy helyi fájlszerver és egy ettől független SaaS-előfizetés puszta megléte még nem bizonyít NIST szerinti hybrid cloudot.

A NIST negyedik modellként **community cloudot** is megnevez: közös igényű szervezetek meghatározott közössége használja. A címben szereplő három modell tehát nem a teljes taxonómia.

## Vizsgán jól használható megfogalmazás

> A private, public és hybrid cloud a cloud telepítési modelljei.  
> A private cloud egy szervezethez kötött, nagyobb kontrollt adó környezet,
> a public cloud a széles nyilvánosság számára kínált szolgáltatás,
> míg a hybrid cloud ezek kombinációja.  
> A választásnál fontos szempont a költség, a rugalmasság, a biztonság és a compliance.

## Gyors önellenőrzés

1. Mi a private cloud lényege?
2. Mi a public cloud lényege?
3. Mi a hybrid cloud?
4. Deployment modell vagy szolgáltatási modell a public/private/hybrid?
5. Mondj két választási szempontot.

## Rövid válaszok az önellenőrzéshez

1. Egy szervezet kizárólagos használatára szánt cloudkörnyezet
2. Külső szolgáltató által nyújtott cloud
3. Különálló cloudkörnyezetek technikailag összekapcsolt kombinációja
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

4. AWS - What is Hybrid Cloud?  
   https://aws.amazon.com/what-is/hybrid-cloud/  
   Használat: gyakorlati magyarázat hybrid cloud használati mintákhoz.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf): a felhő fogalma és telepítési modelljei.

Ellenőrizve: `2026-10-14`.
