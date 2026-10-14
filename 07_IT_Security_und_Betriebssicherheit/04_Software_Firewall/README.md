# Software Firewall

## Gyors vizuális kép

| Típus | Hol működik? |
|---|---|
| software / host firewall | egy adott gépen |
| network firewall | hálózatok vagy hálózati részek közti forgalmat szűr |

## Mi az a software firewall?

A software firewall:

- a kliens PC-n vagy szerveren fut
- a hálózati kapcsolatokat helyben szabályozza

Szabályozhat például:

- program alapján
- port alapján
- IP-cím alapján
- bejövő vagy kimenő irány szerint

## Mire jó?

Segít:

- blokkolni a nem kívánt bejövő kapcsolatokat
- korlátozni bizonyos kimenő kapcsolatokat
- csökkenteni a hálózati támadási felületet

## Miért fontos kliensgépnél?

Mert a kliens nem mindig biztonságos hálózaton van.

Példák:

- nyilvános Wi-Fi
- otthoni hálózat
- iskolai vagy céges hálózat

Ilyenkor különösen fontos, hogy a gép maga is védje magát.

## Mire kell figyelni?

- ne kapcsoljuk ki csak azért, mert valami nem működik elsőre
- inkább célzott kivételt adjunk
- public hálózaton szigorúbb szabály kell

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| software firewall | hostszintű tűzfal a gépen |
| hálózati tűzfal | több rendszer forgalmát szűri; lehet külön készülék vagy virtuális/szoftveres megoldás |
| antivirus | malware-felismerés, nem ugyanaz mint a tűzfal |

## Kidolgozott eset: helyi webes előnézet elérése

A fejlesztő gépén megnyílik a `http://127.0.0.1:8767`, a telefonon viszont nem. A `127.0.0.1` mindig az azt használó eszköz saját loopback címe. Ha a kiszolgáló csak erre figyel, egy tűzfalszabály önmagában nem teszi elérhetővé a helyi hálózaton.

Az ellenőrzés sorrendje: fut-e a szolgáltatás, melyik címen és porton figyel, elérhető-e a gép LAN-címe, majd engedi-e a szükséges kapcsolatot a tűzfal. Egy indokolt helyi szabály például **bejövő TCP, 8767-es célport, privát profil és a szükséges helyi alhálózat** lehet. Ez tervezési példa, nem minden hálózatra alkalmazandó kész szabály. Nyilvános Wi-Fi-n más hozzáférési igény érvényes.

Az állapottartó tűzfal követi a kapcsolatok állapotát. Egy engedélyezett, kifelé kezdeményezett kapcsolat válaszforgalmához ezért általában nem kell minden bejövő portot kinyitni. Egy port engedélyezése nem bizonyítja, hogy a rajta érkező alkalmazási adat biztonságos. A host/network a védelem helyét, a software/hardware a megvalósítását írja le.

## Vizsgán jól használható megfogalmazás

> A software firewall a helyi gépen futó tűzfal,
> amely szűri a hálózati forgalmat
> és szabályok alapján engedi vagy tiltja a kapcsolatokat.  
> Segít megakadályozni a jogosulatlan bejövő hozzáférést, és bizonyos esetekben a kimenő kapcsolatokat is korlátozza.  
> Különösen fontos kliensgépeknél és nem megbízható hálózati környezetben.

## Gyors önellenőrzés

1. Mi a software firewall?
2. Mire jó egy kliens PC-n?
3. Milyen szabály alapján dönthet?
4. Ugyanaz-e, mint az antivírus?
5. Mi a jobb megoldás: teljes kikapcsolás vagy célzott kivétel?

## Rövid válaszok az önellenőrzéshez

1. A gépen futó helyi tűzfal
2. A hálózati forgalom szűrésére és a támadási felület csökkentésére
3. Például port, IP-cím vagy alkalmazás alapján
4. Nem
5. A célzott kivétel

## Források

1. NIST CSRC Glossary - Firewall  
   https://csrc.nist.gov/glossary/term/firewall  
   Használat: hivatalos, szabványos definíció a tűzfal fogalmára.

2. Microsoft Support - Firewall and Network Protection in the Windows Security App  
   https://support.microsoft.com/en-us/windows/firewall-and-network-protection-in-the-windows-security-app-ec0844f7-aebd-0583-67fe-601ecf5d774f  
   Használat: gyakorlati, modern Windows-forrás a host firewall működéséhez.

3. Microsoft Support - Windows Security App Overview  
   https://support.microsoft.com/en-us/office/windows-security-app-overview-ae70cc96-a9cd-4443-a210-e41cb973d3a6  
   Használat: kontextus a helyi tűzfal és a többi kliensvédelmi komponens kapcsolatáról.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [Microsoft: Windows Firewall](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/): cím-, protokoll-, port- és profilalapú szabályok, válaszforgalom

Ellenőrizve: `2026-10-14`.
