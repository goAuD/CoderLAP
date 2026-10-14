# Schutz von Client PCs

## Gyors vizuális kép

| Védelem | Miért kell? |
|---|---|
| frissítés | hibák és sebezhetőségek javítása |
| vírusvédelem | malware felismerése és blokkolása |
| tűzfal | hálózati kapcsolatok szűrése |
| MFA | fiókvédelem erősítése |
| felhasználói korlátozás | kisebb kár hiba vagy támadás esetén |
| backup | helyreállítás adatvesztés után |

## Mitől kell védeni a kliensgépet?

Tipikus kockázatok:

- malware
- phishing
- gyenge vagy újrahasznált jelszó
- elavult szoftver
- jogosulatlan hozzáférés
- adatvesztés

## Melyek a legfontosabb védelmi lépések?

### 1. Frissíts rendszeresen

Frissíteni kell:

- operációs rendszert
- böngészőt
- alkalmazásokat
- biztonsági szoftvert

Ez csökkenti a kihasználható hibák számát.

### 2. Használj malware-védelmet

Szükséges:

- valamilyen naprakész vírus- és fenyegetésvédelem

Ez segíthet:

- ismert kártevők felismerésében
- gyanús viselkedés blokkolásában

### 3. Tartsd bekapcsolva a tűzfalat

A kliensoldali tűzfal:

- szűri a hálózati kapcsolatokat
- csökkenti a támadási felületet

### 4. Erős jelszó + MFA

Alapszabály:

- hosszú, egyedi jelszó
- lehetőleg jelszókezelő
- ahol lehet, MFA

### 5. Ne dolgozz folyamatosan admin joggal

Napi használatra jobb:

- normál felhasználói fiók

### 6. Figyelj a phishingre és a letöltésekre

Ne:

- nyiss meg gyanús mellékletet
- kattints ellenőrizetlen linkre
- telepíts ismeretlen forrásból programot

### 7. Backup

Ha mégis baj van:

- a jó backup az egyik legfontosabb mentőöv

## Mit nem tud egyetlen eszköz sem egyedül?

Sem az antivírus, sem a tűzfal, sem az MFA nem elég önmagában.

A jó védelem:

- több rétegből áll

## Átadás előtti ellenőrzés egy tanulói laptopon

Egy gép akkor tekinthető előkészítettnek, ha az ellenőrzés eredménye is látszik. Nézd meg az operációs rendszer és a böngésző tényleges frissítési állapotát, a támogatott verziót és a szükséges újraindításokat. A firmware és a telepített alkalmazások is részei a leltárnak. Támogatás nélkül maradt rendszernél a leváltást vagy dokumentált átmeneti védelmet is meg kell tervezni.

Napi munkához normál fiókot, automatikus képernyőzárat és szükség szerint lemeztitkosítást használj. A lemeztitkosítás főleg az elveszett, lezárt eszköz adatait védi; a már bejelentkezett munkamenetben futó kártevőt nem állítja meg. A helyreállítási kulcs legyen hozzáférhető akkor is, ha maga a laptop nem működik.

A fióknál az egyedi jelszó, a jelszókezelő és az MFA együtt hasznos. A megfelelően használt FIDO/WebAuthn-alapú hitelesítés adathalászattal szemben is ellenálló lehet; a kézzel begépelt egyszer használatos kód általában nem az. A helyreállítási lehetőséget is próbáld ki.

Végül állíts vissza egy mintadokumentumot mentésből egy külön mappába, és nyisd meg. Ha gyanús fertőzés történik, a hálózati kapcsolat elkülönítése és az üzemeltető értesítése előzze meg az ellenőrizetlen takarítást. Így a továbbterjedés és a bizonyítékvesztés kockázata is csökken.

## Vizsgán jól használható megfogalmazás

> A kliens PC védelmét több rétegben kell megvalósítani.  
> Ide tartozik a rendszeres frissítés, a naprakész malware-védelem,
> a helyi tűzfal, az erős jelszó és MFA használata,
> a korlátozott jogosultságok, a phishing elleni tudatosság
> és a rendszeres biztonsági mentés.  
> Egyetlen eszköz önmagában nem elég, ezért rétegzett védelemre van szükség.

## Gyors önellenőrzés

1. Mondj öt alap védelmi lépést kliens PC-re.
2. Miért fontos a frissítés?
3. Miért hasznos az MFA?
4. Miért ne dolgozz állandóan admin joggal?
5. Miért fontos a backup akkor is, ha van antivírus?

## Rövid válaszok az önellenőrzéshez

1. Frissítés, antivírus, tűzfal, erős jelszó, MFA, korlátozott jog, backup
2. Mert javítja a sebezhetőségeket
3. Mert a jelszón túl plusz védelmet ad
4. Mert hiba vagy támadás esetén nagyobb a kár
5. Mert adatvesztés és ransomware ellen helyreállítási lehetőséget ad

## Források

1. CISA - Secure Yourself & Your Family  
   https://www.cisa.gov/secure-our-world/secure-yourself-your-family  
   Használat: hivatalos, általános cyber hygiene alapforrás kliensvédelemhez.

2. CISA - Update Software  
   https://www.cisa.gov/secure-our-world/update-software  
   Használat: a gyors és rendszeres frissítés jelentőségéhez.

3. CISA - Recognize and Report Phishing  
   https://www.cisa.gov/secure-our-world/recognize-and-report-phishing  
   Használat: phishing elleni felhasználói tudatossághoz.

4. CISA - More Than a Password  
   https://www.cisa.gov/mfa  
   Használat: MFA szerepe a fiókvédelemben.

5. Microsoft Support - Windows Security App Overview  
   https://support.microsoft.com/en-us/office/windows-security-app-overview-ae70cc96-a9cd-4443-a210-e41cb973d3a6  
   Használat: modern Windows kliensvédelmi komponensek áttekintése.

6. Microsoft Support - Virus and Threat Protection in the Windows Security App  
   https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e  
   Használat: naprakész végpontvédelem és fenyegetéskezelés gyakorlati oldala.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html): hitelesítési tényezők és adathalászattal szembeni ellenállás
- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide): elkülönített, titkosított mentések és ellenőrzött helyreállítás

Ellenőrizve: `2026-10-14`.
