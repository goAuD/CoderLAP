# Domain Subdomain Top Level Domain

## Gyors vizuális kép

| Rész | Példa | Jelentés |
|---|---|---|
| TLD | `org` | legfelső szintű domain |
| domain | `mozilla.org` | regisztrált domain |
| subdomain | `developer.mozilla.org` | a domain alatti további név |

## Mi a domain?

A domainnév egy hierarchikus név az interneten.

Segít abban, hogy:

- ne IP-címeket kelljen megjegyezni
- emberi módon lehessen elérni egy szolgáltatást

Például:

- `example.com`
- `school.at`

## Mi a subdomain?

A subdomain egy magasabb szintű domain alatti további név.

Példák:

- `www.example.com`
- `mail.example.com`
- `api.example.com`

Gyakorlatban a subdomainnel gyakran külön szolgáltatásokat választunk szét:

- `mail` = levelezés
- `shop` = webshop
- `api` = backend API

## Mi a top-level domain?

A TLD a domainnév legfelső része.

Példák:

- `.com`
- `.org`
- `.at`
- `.hu`

Tipikus csoportok:

- `gTLD` = általános TLD, például `.com`, `.org`
- `ccTLD` = országkódos TLD, például `.at`, `.hu`

## Miért fontos ez?

Mert webes és hálózati környezetben gyakran kell tudni:

- mi az URL-ben a host vagy domainrész
- hol van a TLD
- mire való a subdomain

Ez vizsgán tipikus alapfogalom.

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| domain | internetes név |
| subdomain | a domain alatti további név |
| TLD | a legfelső, utolsó rész |
| URL | teljes webcím, nem csak a domain |

## Kidolgozott példa: URL és DNS-adat

A `https://api.example.org:8443/topics?id=7#answer` címben az `api.example.org` a host, a `8443` a port, a `/topics` az útvonal. A port és az útvonal nem része a domainnévnek. JavaScriptben a beépített URL-feldolgozóval megvizsgálhatjuk, hálózati kérés nélkül:

<!-- example:run -->
```javascript
const address = new URL('https://api.example.org:8443/topics?id=7#answer');
console.log(address.hostname);
console.log(address.port);
console.log(address.pathname);
console.log(address.searchParams.get('id'));
```

Várt kimenet:

```text
api.example.org
8443
/topics
7
```

DNS-ben az `A` rekord IPv4-, az `AAAA` IPv6-címet adhat, a `CNAME` másik névre mutató alias, az `MX` pedig a levelezési célkiszolgálót jelöli. Egy új DNS-rekord önmagában még nem állítja be a webszervert vagy a TLS-tanúsítványt. A TTL a gyorsítótárazás idejét szabályozza, ezért a változás nem minden kliensnél látszik azonnal.

A regisztrálható domain határát nem lehet mindig az utolsó két címkéből eldönteni: például a `co.uk` több címkéből álló nyilvános névtér.

## Vizsgán jól használható megfogalmazás

> A domainnév az interneten használt hierarchikus név,
> amely emberbarát módon azonosít egy szolgáltatást vagy erőforrást.  
> A domain több részből állhat: a legfelső szintű rész a TLD, a domain alatt pedig további subdomainek hozhatók létre.  
> Például a `developer.mozilla.org` névben az `org` a TLD, a `mozilla` a domain része, a `developer` az új címke, a teljes subdomainnév pedig `developer.mozilla.org`.

## Gyors önellenőrzés

1. Mi a TLD a `mail.school.at` névben?
2. Mi a subdomain a `developer.mozilla.org` névben?
3. Mire jó a domainnév?
4. Kötelező-e a `www`?
5. Ugyanaz-e az URL és a domainnév?

## Rövid válaszok az önellenőrzéshez

1. Az `at`
2. A `developer.mozilla.org` a `mozilla.org` subdomainje; a `developer` az új névcímke
3. Emberbarát internetes címzésre
4. Nem
5. Nem

## Források

1. MDN - Domain  
   https://developer.mozilla.org/en-US/docs/Glossary/Domain  
   Használat: jól használható technikai alapdefiníció domainre, subdomainre és FQDN-re.

2. MDN - Domain name  
   https://developer.mozilla.org/en-US/docs/Glossary/Domain_name  
   Használat: a domainnév felépítésének tömör, modern magyarázata.

3. MDN - TLD  
   https://developer.mozilla.org/docs/Glossary/TLD  
   Használat: a TLD fogalma és fő típusai.

4. ICANN - The Domain Name System  
   https://www.icann.org/resources/pages/dns-2022-09-13-en  
   Használat: hivatalos DNS- és domainháttér ICANN-forrásból.

5. IANA - Root Zone Management  
   https://www.iana.org/domains/root  
   Használat: hivatalos forrás a TLD-k és a gyökérzóna szerepéhez.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html): címkék, hierarchia, DNS-gyorsítótár.
- [MDN: URL](https://developer.mozilla.org/en-US/docs/Web/API/URL): URL-feldolgozás.

Ellenőrizve: `2026-10-14`.
