# Adatvédelmi nyilatkozat

## Felelősi keret

- Projekt neve: CoderLAP
- Szolgáltatás típusa: statikus oktatási weboldal az osztrák LAP szoftverfejlesztés és coding vizsgához
- Jelenlegi közzétételi állapot: korlátozott hozzáférés `basic_auth` védelemmel
- Felelősi kapcsolati alap: lásd az impresszum oldalt és a nyilvános projektprofilt

## Milyen adatkezelés történhet jelenleg reálisan

- Az oldal felé irányuló kérések Cloudflare-nél és az origin szerveren technikai kapcsolati adatokat eredményezhetnek, például IP-címet, időbélyeget, kért URL-t, user agentet és hasonló kérés-metaadatokat
- A jelenlegi `basic_auth` belépési kapu a megadott hozzáférési adatokat csak webszerver-szintű összehasonlításra használja; ebből nem épülnek oldalon belüli felhasználói fiókok
- A böngésző a tanulási előrehaladás funkcióhoz helyben eltárolhat egy bejegyzést a `coderlap_progress` kulcs alatt
- Ez a böngészőoldali tárolás csak helyi témaállapotot és időbélyeget tartalmaz

## Mi nincs jelenleg tervben

- nincs alkalmazásszintű felhasználói fiókrendszer
- nincs nyilvános regisztrációs vagy kapcsolatfelvételi űrlap a közzétett oldalon
- nincs analitikai vagy marketingcélú nyomkövetés a jelenlegi alapbeállításban
- nincs komment- vagy közösségi funkció az oldalon belül

## Célok és jogalapok

- az oldal kiszolgálása, biztonsága és a visszaélések megelőzése a GDPR 6. cikk (1) bekezdés f) pont szerinti jogos érdek alapján
- a privát projektfázis hozzáférés-korlátozása szintén a GDPR 6. cikk (1) bekezdés f) pont szerinti jogos érdek alapján
- a böngészőoldali előrehaladás-tárolás kizárólag a kért tanulási funkcióhoz kapcsolódik

## Tárolási helyek és címzettek

- Cloudflare mint előtétes proxy és biztonsági réteg
- saját üzemeltetésű origin infrastruktúra Caddy-vel Debianon
- helyi böngészőtároló a látogató saját eszközén

## Megőrzési idő

- a böngészőoldali előrehaladás-adatok az eszközön maradnak, amíg a felhasználó nem törli őket vagy nem üríti a böngészőoldali webhelyadatokat
- a technikai proxy- és szervernaplókat csak addig célszerű megőrizni, amíg az üzemeltetéshez, visszaélés-felismeréshez vagy hibakereséshez szükségesek

## Az Ön jogai

- tájékoztatáshoz való jog
- hozzáférési jog
- helyesbítéshez való jog
- törléshez való jog, ha alkalmazható
- az adatkezelés korlátozásához való jog, ha alkalmazható
- tiltakozáshoz való jog, ha az adatkezelés jogos érdeken alapul
- panasztételhez való jog az osztrák adatvédelmi hatóságnál

## Panaszhatóság

- Österreichische Datenschutzbehörde
- Barichgasse 40-42, 1030 Wien, Ausztria
- `https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person`
- `https://dsb.gv.at/eingabe-an-die-dsb/beschwerde`

## Megjegyzés a jelenlegi projektfázishoz

- Ez az adatvédelmi nyilatkozat a jelenlegi, hozzáférés-védett privát rollout állapothoz készült
- Nyilvános, korlátozás nélküli indulás előtt a kapcsolati utat, a megőrzési időket és a végleges jogi besorolást újra ellenőrizni kell

## Források

- Österreichische Datenschutzbehörde, „Ihre Rechte als betroffene Person”
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person
  Az osztrák tájékoztatási kötelezettség és érintetti jogok gyakorlati keretéhez.
- Österreichische Datenschutzbehörde, „Beschwerde”
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde
  Az aktuális osztrák panasztételi út és hatósági elérhetőség alapjához.
- EUR-Lex, (EU) 2016/679 rendelet (GDPR)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj
  A jogalapokhoz, tájékoztatási kötelezettséghez és érintetti jogokhoz.
- RIS, Telekommunikationsgesetz 2021, 165. §
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Az osztrák végberendezésen történő információtárolás és -hozzáférés jogi keretéhez.
