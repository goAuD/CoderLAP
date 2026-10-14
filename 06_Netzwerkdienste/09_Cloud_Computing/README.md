# Cloud Computing

## Gyors vizuális kép

| Jellemző | Jelentés |
|---|---|
| on-demand | igény szerint használható |
| broad network access | hálózaton keresztül érhető el |
| resource pooling | megosztott erőforráskészlet |
| rapid elasticity | gyorsan skálázható |
| measured service | mérhető, gyakran használatalapú |

## Mi a cloud computing?

A NIST meghatározása szerint a cloud computing olyan modell, amely:

- igény szerint elérhető
- hálózaton keresztül használható
- megosztott erőforrásokra épül
- gyorsan bővíthető vagy csökkenthető
- jellemzően mérhető szolgáltatásként működik

Egyszerűen:

- nem feltétlenül a saját gépeden vagy saját szervertermedben fut minden
- az erőforrások szolgáltatásként vehetők igénybe, saját szervezeten belül vagy külső szolgáltatónál is

## Miért jó?

Tipikus előnyök:

- gyors indulás
- kevesebb saját hardver
- rugalmas bővítés
- sokszor egyszerűbb üzemeltetés

## Mire használható?

Például:

- webalkalmazás futtatása
- mentések tárolása
- fájlmegosztás
- fejlesztői és tesztkörnyezet
- levelezés és irodai csomag

## Mire kell figyelni?

A cloud nem varázslat.

Továbbra is fontos:

- adatvédelem
- jogosultságkezelés
- költségkontroll
- rendelkezésre állás
- vendor lock-in kockázata

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| cloud computing | általános modell |
| public cloud | nyilvános felhőmodell |
| SaaS | kész szoftver szolgáltatásként |
| saját szerver | nem cloud attól, hogy távolról elérhető |

## Kidolgozott eset: időszakos tanfolyami terhelés

Egy gyakorló alkalmazásnak hétköznap kevés, vizsga előtt sok egyidejű használója van. A vertikális skálázás egy példánynak ad több erőforrást, a horizontális skálázás több példányt indít. Az utóbbihoz például közösen elérhető adatkezelésre és megfelelő terheléselosztásra is szükség lehet.

Az elasztikusság azt jelenti, hogy az erőforrás a kereslethez igazodva bővíthető és visszavehető. A kapacitás, a kvóta és a költségkeret ettől még véges. A mintaterhelést ezért kipróbáljuk, felső korlátot állítunk be, és megmérjük a válaszidőt.

Az igény szerinti önkiszolgálás több annál, hogy e-mailt írunk egy új szerverért. A szolgáltatás erőforrásokat tud kiosztani és felszabadítani automatizált módon. Ugyanakkor egy kis, állandó terhelésű alkalmazás számára egy egyszerű saját szerver is megfelelő lehet; a cloud jellemzői nem teszik minden feladatra kötelezővé a modellt.

## Vizsgán jól használható megfogalmazás

> A cloud computing olyan modell,
> amelyben számítási erőforrásokat, tárhelyet, platformokat
> vagy teljes alkalmazásokat hálózaton keresztül, igény szerint veszünk igénybe.  
> Fő jellemzői az on-demand használat, a hálózati elérés,
> a megosztott erőforráskészlet, a gyors skálázhatóság
> és a mérhető szolgáltatásjelleg.  
> Előnye a rugalmasság, de figyelni kell a biztonsági, adatvédelmi és költségszempontokra is.

## Gyors önellenőrzés

1. Mi a cloud computing lényege?
2. Mondj két tipikus cloud erőforrást.
3. Mi az on-demand használat?
4. Mi a rapid elasticity?
5. Mire kell figyelni cloud használatánál?

## Rövid válaszok az önellenőrzéshez

1. IT-erőforrások hálózaton át, szolgáltatásként való használata
2. Például virtuális gép és tárhely
3. Igény szerinti, gyors használatba vétel
4. Gyors skálázási képesség
5. Például biztonságra, adatvédelemre és költségekre

## Források

1. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Használat: a cloud computing alapdefiníciójának elsődleges, széles körben hivatkozott forrása.

2. NIST SP 800-146 - Cloud Computing Synopsis and Recommendations  
   https://csrc.nist.gov/pubs/sp/800/146/final  
   Használat: a cloud előnyei, kockázatai és gyakorlati megértése vizsgaszinten.

3. AWS - What is Cloud Computing?  
   https://aws.amazon.com/what-is-cloud-computing/  
   Használat: aktuális, gyakorlati, szolgáltatói nézőpontból írt cloud-összefoglaló.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf): a felhő fogalma és telepítési modelljei.

Ellenőrizve: `2026-10-14`.
