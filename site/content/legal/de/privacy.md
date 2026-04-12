# Datenschutzerklärung

## Verantwortlicher Rahmen

- Projektname: CoderLAP
- Angebotsform: statische Bildungswebsite für die österreichische LAP in
  Applikationsentwicklung - Coding
- Aktueller Veröffentlichungsstatus: zugriffsbeschränkt mit `basic_auth`
- Verantwortliche Kontaktbasis: siehe Impressum und öffentliches Projektprofil

## Welche Datenverarbeitungen derzeit realistisch stattfinden

- Zugriffsanfragen können bei Cloudflare und auf dem Origin-Server technische
  Verbindungsdaten auslösen, etwa IP-Adresse, Zeitstempel, angeforderte URL,
  User-Agent und ähnliche Request-Metadaten
- Die aktuelle Zugriffsbeschränkung über `basic_auth` verarbeitet eingegebene
  Zugangsdaten nur zum Vergleich auf Webserver-Ebene; daraus werden keine
  Benutzerkonten innerhalb der Website aufgebaut
- Im Browser kann für die Lernfortschrittsfunktion ein lokaler Eintrag unter dem
  Schlüssel `coderlap_progress` gespeichert werden
- Dieser Browser-Speicher enthält nur den lokalen Fortschrittsstatus einzelner
  Themen und einen Zeitstempel

## Was derzeit nicht vorgesehen ist

- keine Anwendungsbenutzerkonten
- keine offenen Registrierungs- oder Kontaktformulare auf der veröffentlichten
  Website
- kein Analyse- oder Marketing-Tracking in der aktuellen Standardkonfiguration
- keine Kommentar- oder Community-Funktion auf der Website selbst

## Zwecke und Rechtsgrundlagen

- Auslieferung, Absicherung und Missbrauchsabwehr des Webangebots auf Grundlage
  berechtigter Interessen nach Art. 6 Abs. 1 lit. f DSGVO
- Zugriffsbeschränkung für den privaten Projektbetrieb ebenfalls auf Grundlage
  berechtigter Interessen nach Art. 6 Abs. 1 lit. f DSGVO
- Browserseitiger Fortschrittsspeicher nur für die angeforderte Lernfunktion des
  Angebots

## Speicherorte und Empfänger

- Cloudflare als vorgeschaltete Proxy- und Sicherheitsinfrastruktur
- selbst betriebene Origin-Infrastruktur mit Caddy auf Debian
- lokaler Browser-Speicher auf dem Gerät der nutzenden Person

## Speicherdauer

- Browserseitige Fortschrittsdaten bleiben auf dem Endgerät, bis sie durch die
  nutzende Person oder durch Browserbereinigung gelöscht werden
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
