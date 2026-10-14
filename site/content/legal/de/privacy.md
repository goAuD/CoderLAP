# Datenschutzerklärung

## Verantwortlicher Rahmen

- Geltungsbereich: CoderLAP (`https://coderlap.com`) und CoderQuiz
  (`https://quiz.coderlap.com`)
- Verantwortlicher für beide Angebote: Viktor Halupka, siehe Impressum
- Angebotsform: statische Lerninhalte und ein im Browser laufendes Übungsquiz
  für die österreichische LAP in Applikationsentwicklung - Coding
- Aktueller Veröffentlichungsstatus: zugriffsbeschränkt mit vorübergehendem
  HTTP Basic Auth
- Verantwortliche Kontaktbasis: siehe Impressum und öffentliches Projektprofil

## Welche Datenverarbeitungen derzeit realistisch stattfinden

- Zugriffsanfragen können bei Cloudflare und auf dem Origin-Server technische
  Verbindungsdaten auslösen, etwa IP-Adresse, Zeitstempel, angeforderte URL,
  User-Agent und ähnliche Request-Metadaten
- Der Browser übermittelt die HTTP-Basic-Auth-Zugangsdaten in HTTPS-Anfragen
  zur Zugriffsprüfung auf Webserver-Ebene. Dadurch entstehen keine
  Anwendungsbenutzerkonten. Für die beiden Webadressen kann der Browser eine
  getrennte Anmeldung verlangen; eine gemeinsame Anmeldung gibt es noch nicht
- Für den CoderLAP-Lernfortschritt kann im Browser ein lokaler Eintrag unter dem
  Schlüssel `coderlap_progress` gespeichert werden
- Dieser CoderLAP-Eintrag enthält den lokalen Fortschrittsstatus einzelner
  Themen und einen Zeitstempel

## Lokale Speicherung in CoderQuiz

CoderQuiz nutzt den `localStorage` des Browsers, um die Sprachauswahl zu
speichern und eine Übung fortsetzen zu können:

- `cq-lang`: die gewählte Oberflächensprache
- `cq-<bankId>-topics`: die ausgewählten Themen des jeweiligen Fragenpakets
- `cq-<bankId>-progress`: Kennungen, Revisionen und Reihenfolge der Fragen,
  aktuelle Frage und Ansicht, gemischte Reihenfolge der Antwortmöglichkeiten,
  gegebene Antworten, deren Auswertung, Punktestand und ausgewählte Themen

`<bankId>` steht für die Kennung des Fragenpakets. Jedes Paket hat damit einen
eigenen lokalen Spielstand. Diese Sprach- und Übungsdaten übermittelt die
Anwendung weder an den Server noch an externe Dienste. Davon zu unterscheiden
sind die oben genannten technischen Anfragedaten beim Laden der Seite und der
Fragenpakete.

`coderlap.com` und `quiz.coderlap.com` sind getrennte Browser-Ursprünge
(Origins). Ihre lokalen Speicher sind getrennt; es gibt keine automatische
Fortschrittssynchronisierung zwischen ihnen oder mit anderen Geräten. In den
Browsereinstellungen lassen sich durch Löschen der Websitedaten für
`quiz.coderlap.com` die Sprache, Themenauswahl und gespeicherte Übung gemeinsam
entfernen. Der CoderLAP-Fortschritt gehört dagegen zu den Websitedaten für
`coderlap.com`.

## Welche Funktionen es derzeit nicht gibt

- keine Anwendungsbenutzerkonten
- keine serverseitige Datenbank für Lernergebnisse
- keine offenen Registrierungs- oder Kontaktformulare auf der veröffentlichten
  Website
- kein Analyse- oder Marketing-Tracking in der aktuellen Standardkonfiguration
- keine Kommentar- oder Community-Funktion auf der Website selbst

## Zwecke und Rechtsgrundlagen

- Auslieferung, Absicherung und Missbrauchsabwehr des Webangebots auf Grundlage
  berechtigter Interessen nach Art. 6 Abs. 1 lit. f DSGVO
- Zugriffsbeschränkung für den privaten Projektbetrieb ebenfalls auf Grundlage
  berechtigter Interessen nach Art. 6 Abs. 1 lit. f DSGVO
- Browserseitige Speicherung für die gewählte Sprache, Themenauswahl und das
  Fortsetzen der angeforderten Lern- oder Übungsfunktion

## Speicherorte und Empfänger

- Cloudflare als vorgeschaltete Proxy- und Sicherheitsinfrastruktur
- selbst betriebene Origin-Infrastruktur mit Caddy auf Debian
- lokaler Browser-Speicher auf dem Gerät der nutzenden Person

## Speicherdauer

- Browserseitige Einstellungen und Fortschrittsdaten haben keine festgelegte
  Ablaufzeit; sie können durch Löschen der Websitedaten entfernt werden
- Ein Neustart des Quiz ersetzt die bisherige Übung; einen mit aktualisierten
  Fragen nicht mehr kompatiblen Spielstand verwirft die Anwendung
- technische Proxy- und Serverprotokolle sollen nur so lange aufbewahrt werden,
  wie sie für Betrieb, Missbrauchserkennung oder Fehleranalyse erforderlich sind

## Ihre Rechte

- Recht auf Information
- Recht auf Auskunft
- Recht auf Berichtigung
- Recht auf Löschung, soweit anwendbar
- Recht auf Einschränkung der Verarbeitung, soweit anwendbar
- Recht auf Widerspruch bei Verarbeitungen auf Basis berechtigter Interessen
- Recht auf Beschwerde bei der österreichischen Datenschutzbehörde

## Beschwerdestelle

- Österreichische Datenschutzbehörde
- Barichgasse 40-42, 1030 Wien
- `https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person`
- `https://dsb.gv.at/eingabe-an-die-dsb/beschwerde`

## Hinweis zum aktuellen Projektstatus

- Diese Datenschutzerklärung ist auf den derzeitigen privaten Rollout mit
  Zugangsschutz zugeschnitten
- Vor einer öffentlichen Freischaltung ohne `basic_auth` sollten Kontaktweg,
  Speicherfristen und die endgültige rechtliche Einordnung nochmals überprüft
  werden

## Quellen

- MDN, „Window: localStorage property“
  https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
  Zur Funktionsweise der getrennten, dauerhaften Speicherung je Browser-Origin.
- Caddy, „basic_auth“
  https://caddyserver.com/docs/caddyfile/directives/basic_auth
  Zur Funktionsweise der HTTP-Basic-Auth-Prüfung auf Webserver-Ebene.
- Österreichische Datenschutzbehörde, „Ihre Rechte als betroffene Person“
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person Verwendet
  für die österreichische Einordnung der Informationspflichten und
  Betroffenenrechte.
- Österreichische Datenschutzbehörde, „Beschwerde“
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde Verwendet für die konkrete
  österreichische Beschwerdestelle und den Hinweis auf das Beschwerderecht.
- EUR-Lex, Verordnung (EU) 2016/679 (DSGVO)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj Verwendet für Rechtsgrundlagen,
  Informationspflichten und Betroffenenrechte.
- RIS, Telekommunikationsgesetz 2021, § 165
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Verwendet für die österreichische Rechtsgrundlage rund um das Speichern oder
  Auslesen von Informationen auf Endeinrichtungen.
