# Adatvédelmi nyilatkozat

## Felelősi keret

- Érintett szolgáltatások: CoderLAP (`https://coderlap.com`) és CoderQuiz
  (`https://quiz.coderlap.com`)
- Mindkét szolgáltatás adatkezelője: Viktor Halupka, lásd az impresszumot
- Szolgáltatás típusa: statikus tananyag és böngészőben futó gyakorlókvíz
  az osztrák LAP szoftverfejlesztés és coding vizsgához
- Jelenlegi közzétételi állapot: korlátozott hozzáférés, átmeneti HTTP Basic
  Auth védelemmel
- Felelősi kapcsolati alap: lásd az impresszum oldalt és a nyilvános
  projektprofilt

## Milyen adatkezelés történhet jelenleg reálisan

- Az oldal felé irányuló kérések Cloudflare-nél és az origin szerveren technikai
  kapcsolati adatokat eredményezhetnek, például IP-címet, időbélyeget, kért
  URL-t, user agentet és hasonló kérés-metaadatokat
- A böngésző a HTTP Basic Auth hozzáférési adatokat HTTPS-kérésben küldi a
  webszerveres hozzáférés ellenőrzéséhez. Ebből nem keletkezik alkalmazáson
  belüli felhasználói fiók. A két webcímhez külön belépést is kérhet a böngésző;
  ez még nem közös bejelentkezési rendszer
- A CoderLAP tanulási előrehaladás funkciójához a böngésző helyben eltárolhat egy
  bejegyzést a `coderlap_progress` kulcs alatt
- Ez a CoderLAP-bejegyzés helyi témaállapotot és időbélyeget tartalmaz

## A CoderQuiz helyi mentései

A CoderQuiz a böngésző `localStorage` tárolóját használja a nyelvválasztás és
a gyakorlás folytathatósága érdekében:

- `cq-lang`: a választott felületi nyelv
- `cq-<bankId>-topics`: az adott kérdéscsomaghoz kiválasztott témák
- `cq-<bankId>-progress`: a kérdések azonosítói, revíziói és sorrendje, az
  aktuális kérdés és képernyő, a válaszlehetőségek kevert sorrendje, a megadott
  válaszok, kiértékelésük, pontszám és a kiválasztott témák

A `<bankId>` az adott kérdéscsomag azonosítója. A csomagok így külön helyi
mentést kapnak. Ezeket a nyelvi és gyakorlási adatokat az alkalmazás nem küldi
a szerverre vagy külső szolgáltatónak. Ettől külön kezelendők az oldal és a
kérdéscsomagok betöltésekor keletkező, fent felsorolt technikai kérésadatok.

A `coderlap.com` és a `quiz.coderlap.com` külön böngészős eredet, azaz origin.
Helyi mentéseik elkülönülnek; nincs automatikus haladásszinkron köztük vagy más
eszközökkel. A Quiz nyelvét, témaválasztását és mentett gyakorlását a böngésző
beállításaiban a `quiz.coderlap.com` webhelyadatainak törlésével lehet együtt
törölni. A CoderLAP mentéséhez külön a `coderlap.com` webhelyadatai tartoznak.

## Milyen funkciók nincsenek jelenleg

- nincs alkalmazásszintű felhasználói fiókrendszer
- nincs tanulási eredményeket tároló szerveres adatbázis
- nincs nyilvános regisztrációs vagy kapcsolatfelvételi űrlap a közzétett
  oldalon
- nincs analitikai vagy marketingcélú nyomkövetés a jelenlegi alapbeállításban
- nincs komment- vagy közösségi funkció az oldalon belül

## Célok és jogalapok

- az oldal kiszolgálása, biztonsága és a visszaélések megelőzése a GDPR 6. cikk
  (1) bekezdés f) pont szerinti jogos érdek alapján
- a privát projektfázis hozzáférés-korlátozása szintén a GDPR 6. cikk (1)
  bekezdés f) pont szerinti jogos érdek alapján
- a böngészőoldali mentések a választott nyelv megőrzését, a témaválasztást és
  a kért tanulási vagy gyakorlási funkció folytatását szolgálják

## Tárolási helyek és címzettek

- Cloudflare mint előtétes proxy és biztonsági réteg
- saját üzemeltetésű origin infrastruktúra Caddy-vel Debianon
- helyi böngészőtároló a látogató saját eszközén

## Megőrzési idő

- a böngészőoldali beállításoknak és előrehaladás-adatoknak nincs beállított
  lejárati idejük; a webhelyadatok törlésével eltávolíthatók
- a Quiz újrakezdése lecseréli a korábbi gyakorlást; a frissített kérdésekkel
  már nem összeegyeztethető mentést az alkalmazás elveti
- a technikai proxy- és szervernaplókat csak addig célszerű megőrizni, amíg az
  üzemeltetéshez, visszaélés-felismeréshez vagy hibakereséshez szükségesek

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

- Ez az adatvédelmi nyilatkozat a jelenlegi, hozzáférés-védett privát rollout
  állapothoz készült
- Nyilvános, korlátozás nélküli indulás előtt a kapcsolati utat, a megőrzési
  időket és a végleges jogi besorolást újra ellenőrizni kell

## Források

- MDN, „Window: localStorage property”
  https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
  A böngészős eredetenként elkülönülő, helyben megmaradó tárolás működéséhez.
- Caddy, „basic_auth”
  https://caddyserver.com/docs/caddyfile/directives/basic_auth
  A webszerver szintjén ellenőrzött HTTP Basic Auth működéséhez.
- Österreichische Datenschutzbehörde, „Ihre Rechte als betroffene Person”
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person Az
  osztrák tájékoztatási kötelezettség és érintetti jogok gyakorlati keretéhez.
- Österreichische Datenschutzbehörde, „Beschwerde”
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde Az aktuális osztrák
  panasztételi út és hatósági elérhetőség alapjához.
- EUR-Lex, (EU) 2016/679 rendelet (GDPR)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj A jogalapokhoz, tájékoztatási
  kötelezettséghez és érintetti jogokhoz.
- RIS, Telekommunikationsgesetz 2021, 165. §
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Az osztrák végberendezésen történő információtárolás és -hozzáférés jogi
  keretéhez.
