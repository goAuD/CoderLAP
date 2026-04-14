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

## Vizsgán jól használható megfogalmazás

> A domainnév az interneten használt hierarchikus név,
> amely emberbarát módon azonosít egy szolgáltatást vagy erőforrást.  
> A domain több részből állhat: a legfelső szintű rész a TLD, a domain alatt pedig további subdomainek hozhatók létre.  
> Például a `developer.mozilla.org` névben az `org` a TLD, a `mozilla` a domain része, a `developer` pedig subdomain.

## Gyakori vizsgahibák

- Az URL-t és a domainnevet ugyanannak tekinteni.
- Azt hinni, hogy a `www` mindig kötelező.
- Nem felismerni, hogy a subdomain a domain része.
- A TLD-t összekeverni a teljes domainnel.

## Gyors önellenőrzés

1. Mi a TLD a `mail.school.at` névben?
2. Mi a subdomain a `developer.mozilla.org` névben?
3. Mire jó a domainnév?
4. Kötelező-e a `www`?
5. Ugyanaz-e az URL és a domainnév?

## Rövid válaszok az önellenőrzéshez

1. Az `at`
2. A `developer`
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
