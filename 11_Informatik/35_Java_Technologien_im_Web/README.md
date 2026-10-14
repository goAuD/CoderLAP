# Java Technologien im Web

## Gyors vizuális kép

| Technológia | Szerep |
|---|---|
| Servlet | HTTP-kérések kezelése |
| JSP / Jakarta Pages | karbantartott szerveroldali sablontechnológia |
| Spring Boot | modern Java backend és webapp fejlesztés |
| Jakarta EE | enterprise Java platform |

## Mire használják a Javát a weben?

- backend API-k készítésére
- üzleti logika megvalósítására
- nagyobb vállalati rendszerekhez
- skálázható szerveroldali alkalmazásokhoz

## Történeti és modern rétegek

### Klasszikus, továbbra is karbantartott alapok

- `Servlet`
- `JSP`

Ezek ma is létező szerveroldali technológiák; szerepük és használatuk projektfüggő.

### Mai tipikus irányok

- `Spring Boot`
- `Jakarta EE`
- REST API-k
- microservice alapú backendek

## Miért erős a Java a weben?

- stabil, érett ökoszisztéma
- sok vállalati környezetben bevált
- jó framework támogatás
- erős tooling és nagy közösség

## Java és JavaScript: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| Java | általános programozási nyelv, erős backend jelenléttel |
| JavaScript | elsősorban webes scripting nyelv, frontend és ma sok backend is |

## Mire kell figyelni?

- A Java webes szerepe főleg backend oldalon erős.
- A `JSP` Jakarta Pages néven továbbra is karbantartott; a nézettechnológia választása a projekt feladata.
- Vizsgán érdemes külön beszélni a régebbi és a mai technológiákról.

## Egy Java-webkérés útja és a mai Servlet szerepe

```text
Browser: GET /api/course
  -> Webserver / Servlet-Container
  -> Spring-Controller
  -> Java-Objekt
  -> JSON-Antwort
```

**Szemléltető controller:** egy már létrehozott, kompatibilis JDK-val futó
Spring Boot Web MVC-projekt `example.learning` csomagjában helyezhető el.
A Spring alkalmazás komponenskeresése érje el ezt a csomagot, és legyen
beállítva a szokásos JSON-szerializálás. Ez önmagában nem teljes indítható projekt.
A `GET /api/course` kérés várt válasza `200 OK` és az alábbi JSON-törzs:

```java
package example.learning;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CourseController {
    public record Course(int id, String title) {}

    @GetMapping("/api/course")
    public Course course() {
        return new Course(15, "Schleifen");
    }
}
```

```json
{"id":15,"title":"Schleifen"}
```

A `GetMapping` az útvonalat kapcsolja a metódushoz. A `RestController` miatt a
visszatérő rekordot a framework válaszadatként szerializálja; a böngésző JSON-t
kap, nem Java-osztályt futtat. A példa rögzített nyilvános adatot ad vissza;
adatbázist, bejelentkezést és jogosultságvizsgálatot nem tartalmaz.

A Servlet nem pusztán történeti előzmény: a Jakarta Servlet jelenleg is
fejlesztett szerveroldali API. A JSP utódneve **Jakarta Pages**, amely szintén
karbantartott specifikáció; sablonból Servletet készít. A projekt igénye alapján
választunk ilyen szerveroldali nézetet vagy JSON API-t és külön frontendet.
Spring Web MVC Servletre épít, de nem minden Java-webes megoldás Servlet-alapú.

Jakarta EE 9-től az érintett vállalati API-k `javax.*` csomagnevei `jakarta.*`
névre váltottak. Régi függőségek migrációjánál ezért a kódot, a szervert és a
librarykat együtt kell ellenőrizni. Ez nem jelenti minden Java SE `javax.*`
csomag átnevezését. Egy jól felépített monolit is lehet megfelelő Java-backend;
a Java használatából nem következik, hogy microservice-ekre kell bontani.

## Vizsgán jól használható megfogalmazás

> A Java webes technológiái elsősorban szerveroldali alkalmazások,
> backend szolgáltatások
> és vállalati webes rendszerek fejlesztésére szolgálnak.  
> A klasszikus alapok közé tartozik a Servlet és a JSP,
> míg a modern gyakorlatban a Spring Boot
> és a Jakarta EE a legfontosabb irányok közé tartoznak.  
> A Java különösen erős stabilitás, skálázhatóság és enterprise használat terén.

## Gyors önellenőrzés

1. Mire használják a Javát a weben?
2. Melyek a klasszikus Java webes alapok?
3. Melyek a modern irányok?
4. Miért erős a Java enterprise környezetben?
5. Mi a különbség Java és JavaScript között?

## Rövid válaszok az önellenőrzéshez

1. Főleg backend és webes szerveroldali fejlesztésre
2. Servlet és JSP
3. Spring Boot és Jakarta EE
4. Stabil ökoszisztéma és jó skálázhatóság miatt
5. Két külön nyelv, eltérő fő szereppel

## Források

Ellenőrizve: `2026-10-14`.

- [Spring: Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/): controller és JSON-válasz, teljes mintaprojekt előfeltételei.
- [Jakarta Servlet](https://jakarta.ee/specifications/servlet/): aktív Servlet-specifikáció.
- [Jakarta Pages](https://jakarta.ee/specifications/pages/): a JSP karbantartott utódneve és működése.
- [Jakarta EE FAQ](https://jakarta.ee/about/faq/): EE 9 névtérváltás.


1. Oracle Java  
   https://www.oracle.com/java/  
   Használat: a Java hivatalos platformforrása.

2. Spring - Web Applications  
   https://spring.io/web-applications/  
   Használat: modern Java webes fejlesztési ökoszisztéma.

3. Spring Guide - Serving Web Content  
   https://spring.io/guides/gs/serving-web-content/  
   Használat: gyakorlati példa Java-alapú webes alkalmazásra.

4. Jakarta EE Learn  
   https://jakarta.ee/learn/  
   Használat: hivatalos enterprise Java webes háttér.

Megnyitva: `2026-04-08`
