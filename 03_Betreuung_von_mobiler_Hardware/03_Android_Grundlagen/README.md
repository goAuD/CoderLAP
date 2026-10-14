# Android Grundlagen

## Gyors vizuális kép

| Jellemző          | Android                                 |
| ----------------- | --------------------------------------- |
| platformalap      | `AOSP`                                  |
| eszközök          | sok gyártó, sok modell                  |
| appterjesztés     | Google Play és más források is lehetnek |
| testreszabhatóság | általában nagyobb                       |
| frissítések       | gyártótól és modelltől is függhetnek    |

## Mi az Android?

Az Android egy mobil operációs rendszer-platform, amelyet:

- telefonokon
- tableteken
- más okoseszközökön

használnak.

Az alap nyílt forrású projekt neve:

- **AOSP** (`Android Open Source Project`)

Ez fontos, mert az Android nem csak egyetlen készülékhez vagy egyetlen hardvercsaládhoz kötődik.

## Az Android fő jellemzői

## 1. Nyílt forrású alap

Az Android alapja nyílt forrású.

Ez azt jelenti, hogy:

- a platform alapja nyilvánosan elérhető
- gyártók testre szabhatják
- sokféle eszköz készülhet rá

## 2. Sokféle készülék

Android fut:

- belépőszintű telefonokon
- csúcskategóriás telefonokon
- tableteken
- hajlítható eszközökön

Ez nagy előny, de sokféleséget és eltéréseket is jelent.

## 3. Alkalmazás-ökoszisztéma

Az Android-appok tipikusan:

- `AAB` kiadási csomagból is terjeszthetők; a készülékre települő csomag formátuma `APK`
- leggyakrabban a **Google Play**-en keresztül jutnak el a felhasználóhoz

De az Android világában más terjesztési módok is létezhetnek.

## 4. Jogosultságok és biztonság

Az Androidban fontos szerepe van:

- az appengedélyeknek
- az alkalmazások elkülönítésének
- a platformbiztonságnak
- a Play Protect jellegű védelmeknek

## 5. Testreszabhatóság

Az Android egyik gyakran említett előnye:

- sok gyártó saját felületeket, beállításokat és funkciókat adhat hozzá

Példák:

- launcher
- widgetek
- gyártói kezelőfelület
- eltérő rendszeralkalmazások

## Android a gyakorlatban

Az Android használható:

- hívásra
- üzenetküldésre
- böngészésre
- navigációra
- appfuttatásra
- fizetésre
- fotózásra
- munkahelyi használatra is

## Android előnyei

- nagy eszközválaszték
- széles ársáv
- rugalmasabb ökoszisztéma
- nagyobb testreszabhatóság
- sok gyártó támogatja

## Android kihívásai

- a készülékek és gyártók közötti különbségek
- eltérő frissítési politika
- nagyobb fragmentáció
- a felhasználói élmény nem mindig teljesen egységes

## Fontos fogalmak

### AOSP

Az Android nyílt forrású alapprojektje.

### Google Play

A legfontosabb Android app piactér.

### Sideload / külső telepítés

Az Androidon bizonyos feltételekkel nem csak az elsődleges app store-ból lehet appot telepíteni.

Ez rugalmas, de biztonsági kockázatot is jelenthet.

## Android vs iOS

| Android                    | iOS                                   |
| -------------------------- | ------------------------------------- |
| nyitottabb ökoszisztéma    | zártabb ökoszisztéma                  |
| sok gyártó                 | Apple-központú                        |
| többféle eszköz és felület | egységesebb hardver-szoftver kontroll |
| több terjesztési lehetőség | erősebben ellenőrzött terjesztés      |

## Kiadási csomag és telepített alkalmazás

Az **AAB** (`Android App Bundle`) kiadásra szolgáló csomag. A Google Play ebből az eszköznek megfelelő APK-kat állíthat elő. Az AAB ezért nem azonos egy közvetlenül telepítendő APK-fájllal. Az AOSP nyílt alapja pedig nem jelenti, hogy minden készüléken eleve megtalálható a Google Play vagy az összes Google-szolgáltatás.

## Kidolgozott eset: QR-olvasó alkalmazás

A QR-olvasó kameraképet kér, ezért a kamerahasználat indításakor indokolt a kameraengedély. Egy egyszerű kódbeolvasáshoz a teljes névjegyzék olvasása nem szükséges. A tesztben az engedély megtagadását is kipróbáljuk: az app magyarázza el a következményt, és maradjon használható, ahol ez lehetséges.

Az appok elkülönítését a platform sandboxa támogatja. A megadott engedély viszont tényleges hozzáférést adhat, ezért a felhasználói jóváhagyás és az adattakarékos működés együtt fontos. Eszköztámogatásnál az Android-verzió mellett a biztonsági javítás szintjét és a gyártó vállalt támogatási idejét is ellenőrizzük.

## Vizsgán jól használható megfogalmazás

> Az Android egy széles körben használt mobil operációs rendszer-platform, amely nyílt forrású alapokra épül.  
> Sok gyártó sokféle smartphone-ján és tabletjén fut, ezért rugalmas és széles körben elterjedt.  
> Az Android fontos jellemzői az alkalmazások futtatása,
> a jogosultságkezelés, a Google Play ökoszisztéma,
> valamint a nagyobb testreszabhatóság.

## Gyors önellenőrzés

1. Mi az AOSP?
2. Mi az Android egyik nagy előnye?
3. Mi az Android egyik gyakori kihívása?
4. Mi a Google Play szerepe?
5. Miben más az Android, mint az iOS?

## Rövid válaszok az önellenőrzéshez

1. Az Android Open Source Project, a nyílt forrású alap
2. A nagy eszközválaszték és a testreszabhatóság
3. A fragmentáció és az eltérő frissítési modellek
4. Fontos appterjesztési piactér
5. Általában nyitottabb és több gyártó eszközein fut

## Források

1. Android Open Source Project - Architecture overview  
   https://source.android.com/docs/core/architecture  
   Használat: az Android mint teljes mobilplatform és az AOSP szerepe.

2. Android Developers - Application fundamentals  
   https://developer.android.com/guide/topics/fundamentals  
   Használat: Android appmodell, jogosultságok, hardver- és szoftverképességek.

3. Android Developers - Publish your app  
   https://developer.android.com/studio/publish/  
   Használat: Android appterjesztés, Google Play és egyéb kiadási módok.

4. Android Developers - Play Integrity overview  
   https://developer.android.com/google/play/integrity/overview  
   Használat: Play Protect / integritásvédelem és biztonsági környezet.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [Android: App Bundles](https://developer.android.com/guide/app-bundle): AAB kiadási formátum és APK generálás.
- [Android: Permissions](https://developer.android.com/guide/topics/permissions/overview): funkcióhoz kötött engedély és elutasítás kezelése.
- [AOSP: Application Sandbox](https://source.android.com/docs/security/app-sandbox): alkalmazások elkülönítése.

Ellenőrizve: `2026-10-14`.
