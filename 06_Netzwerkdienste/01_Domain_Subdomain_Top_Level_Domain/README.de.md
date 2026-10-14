# Domain Subdomain Top Level Domain

## Schneller visueller Überblick

| Teil | Beispiel | Bedeutung |
|---|---|---|
| TLD | `org` | Top-Level-Domain |
| Domain | `mozilla.org` | registrierte Domain |
| Subdomain | `developer.mozilla.org` | weiterer Name unterhalb der Domain |

## Was ist eine Domain?

Ein Domainname ist ein hierarchischer Name im Internet.

Er hilft dabei, dass:

- man sich keine IP-Adressen merken muss
- man Dienste auf menschenfreundliche Weise erreichen kann

Zum Beispiel:

- `example.com`
- `school.at`

## Was ist eine Subdomain?

Eine Subdomain ist ein weiterer Name unterhalb einer übergeordneten Domain.

Beispiele:

- `www.example.com`
- `mail.example.com`
- `api.example.com`

In der Praxis werden mit Subdomains häufig verschiedene Dienste getrennt:

- `mail` = E-Mail
- `shop` = Webshop
- `api` = Backend-API

## Was ist eine Top-Level-Domain?

Die TLD ist der oberste Teil des Domainnamens.

Beispiele:

- `.com`
- `.org`
- `.at`
- `.hu`

Typische Gruppen:

- `gTLD` = generische TLD, z. B. `.com`, `.org`
- `ccTLD` = länderspezifische TLD, z. B. `.at`, `.hu`

## Warum ist das wichtig?

Weil man in Web- und Netzwerkumgebungen häufig wissen muss:

- was im URL der Host- oder Domainteil ist
- wo die TLD steht
- wozu die Subdomain dient

Das ist bei Prüfungen ein typischer Grundbegriff.

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Domain | Internetname |
| Subdomain | weiterer Name unterhalb der Domain |
| TLD | der oberste, letzte Teil |
| URL | vollständige Webadresse, nicht nur die Domain |

## Durchgearbeitetes Beispiel: URL und DNS-Eintrag

In `https://api.example.org:8443/topics?id=7#answer` ist `api.example.org` der Host, `8443` der Port und `/topics` der Pfad. Port und Pfad gehören nicht zum Domainnamen. Mit dem eingebauten JavaScript-URL-Parser lässt sich die Adresse ohne Netzwerkanfrage untersuchen:

<!-- example:run -->
```javascript
const address = new URL('https://api.example.org:8443/topics?id=7#answer');
console.log(address.hostname);
console.log(address.port);
console.log(address.pathname);
console.log(address.searchParams.get('id'));
```

Erwartete Ausgabe:

```text
api.example.org
8443
/topics
7
```

Im DNS kann ein `A`-Eintrag eine IPv4-, ein `AAAA`-Eintrag eine IPv6-Adresse liefern. `CNAME` ist ein Alias auf einen anderen Namen, `MX` bezeichnet den Ziel-Mailserver. Ein neuer DNS-Eintrag konfiguriert noch keinen Webserver und kein TLS-Zertifikat. Die TTL regelt die Zwischenspeicherung, weshalb Änderungen nicht bei allen Clients sofort sichtbar werden.

Die Grenze der registrierbaren Domain lässt sich nicht immer aus den letzten zwei Labels ableiten: `co.uk` ist beispielsweise ein öffentlicher Namensraum aus mehreren Labels.

## Prüfungstaugliche Formulierung

> Ein Domainname ist ein hierarchischer Name im Internet,
> der einen Dienst oder eine Ressource auf menschenfreundliche Weise identifiziert.  
> Eine Domain kann aus mehreren Teilen bestehen:
> Der oberste Teil ist die TLD,
> und unterhalb der Domain können weitere Subdomains erstellt werden.  
> Zum Beispiel ist im Namen `developer.mozilla.org` das `org` die TLD, `mozilla` der Domainteil und `developer` das zusätzliche Label; der vollständige Subdomainname lautet `developer.mozilla.org`.

## Schnelle Selbstkontrolle

1. Was ist die TLD im Namen `mail.school.at`?
2. Was ist die Subdomain im Namen `developer.mozilla.org`?
3. Wozu dient ein Domainname?
4. Ist `www` Pflicht?
5. Sind URL und Domainname dasselbe?

## Kurzantworten zur Selbstkontrolle

1. `at`
2. `developer.mozilla.org` ist eine Subdomain von `mozilla.org`; `developer` ist das zusätzliche Label
3. Für menschenfreundliche Internetadressierung
4. Nein
5. Nein

## Quellen

1. MDN - Domain  
   https://developer.mozilla.org/en-US/docs/Glossary/Domain  
   Verwendung: gut verwendbare technische Grunddefinition für Domain, Subdomain und FQDN.

2. MDN - Domain name  
   https://developer.mozilla.org/en-US/docs/Glossary/Domain_name  
   Verwendung: knappe, moderne Erklärung des Aufbaus eines Domainnamens.

3. MDN - TLD  
   https://developer.mozilla.org/docs/Glossary/TLD  
   Verwendung: Begriff und Haupttypen der TLD.

4. ICANN - The Domain Name System  
   https://www.icann.org/resources/pages/dns-2022-09-13-en  
   Verwendung: offizieller DNS- und Domain-Hintergrund aus ICANN-Quelle.

5. IANA - Root Zone Management  
   https://www.iana.org/domains/root  
   Verwendung: offizielle Quelle zur Rolle der TLDs und der Root-Zone.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html): Labels, Hierarchie und DNS-Cache.
- [MDN: URL](https://developer.mozilla.org/en-US/docs/Web/API/URL): URL-Verarbeitung.

Geprüft: `2026-10-14`.
