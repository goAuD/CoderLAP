# Musterloesung Minimal

## Cél

Ez egy tudatosan egyszerű, vizsgabarát mintamegoldás a `18_Uebungsbeispiel` blokkhoz.

## Fájlok

- `index.html`
- `styles.css`
- `app.js`
- `vendor/qrcode.js` - third-party library, nem módosítandó
  Forráskód: https://github.com/kazuhikoarase/qrcode-generator

## Forráskód

<details>
<summary>index.html</summary>

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SV-Nummer Pruefung und QR-Code</title>
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    rel="stylesheet"
  >
  <link rel="stylesheet" href="./styles.css">
</head>
<body>
  <main class="container py-4 py-md-5">
    <div class="row justify-content-center">
      <div class="col-12 col-lg-8">
        <div class="card shadow-sm border-0">
          <div class="card-body p-4 p-md-5">
            <div class="mb-4">
              <p class="text-uppercase text-secondary small mb-2">LAP Uebungsbeispiel</p>
              <h1 class="h3 mb-2">Stammdaten-Formular mit SV-Pruefung</h1>
              <p class="text-secondary mb-0">
                Minimale Musterloesung mit <code>Bootstrap</code>, SV-Validierung und QR-Code.
              </p>
            </div>

            <form id="stammdaten-form" novalidate>
              <div class="row g-3">
                <div class="col-12 col-md-6">
                  <label for="vorname" class="form-label">Vorname</label>
                  <input id="vorname" name="vorname" type="text" class="form-control" autocomplete="given-name">
                  <div class="invalid-feedback">Bitte einen Vornamen eingeben.</div>
                </div>

                <div class="col-12 col-md-6">
                  <label for="nachname" class="form-label">Nachname</label>
                  <input id="nachname" name="nachname" type="text" class="form-control" autocomplete="family-name">
                  <div class="invalid-feedback">Bitte einen Nachnamen eingeben.</div>
                </div>

                <div class="col-12">
                  <label for="svnummer" class="form-label">SV-NR</label>
                  <input
                    id="svnummer"
                    name="svnummer"
                    type="text"
                    class="form-control"
                    inputmode="numeric"
                    autocomplete="off"
                    placeholder="z. B. 4422 180599"
                    aria-describedby="svnummer-help"
                  >
                  <div id="svnummer-help" class="form-text">
                    Format: <code>LLLL TTMMJJ</code> bzw. 10 Ziffern mit optionalem Leerzeichen nach der 4. Stelle.
                  </div>
                  <div class="invalid-feedback" id="svnummer-feedback">
                    Bitte eine SV-Nummer eingeben.
                  </div>
                </div>
              </div>

              <div class="d-grid d-sm-flex gap-2 mt-4">
                <button type="submit" class="btn btn-primary">Pruefen und QR-Code erzeugen</button>
                <button type="button" class="btn btn-outline-secondary" id="reset-button">Zuruecksetzen</button>
              </div>
            </form>

            <div id="result-wrapper" class="mt-4 d-none">
              <div id="result-alert" class="alert mb-3" role="status"></div>
              <div class="qr-panel">
                <div class="d-flex flex-column flex-md-row align-items-start gap-4">
                  <div>
                    <h2 class="h5 mb-2">QR-Code</h2>
                    <p class="text-secondary mb-2">Der Inhalt des QR-Codes ist genau ein Wort:</p>
                    <p class="mb-0"><code id="qr-payload"></code></p>
                  </div>
                  <div id="qr-code" class="qr-code-box" aria-live="polite"></div>
                </div>
              </div>
            </div>

            <div class="mt-4 pt-4 border-top">
              <h2 class="h6">PDF-Testdaten</h2>
              <div class="small text-secondary">
                <div><strong>Gueltig:</strong> 4422 180599, 3567 010705, 5884 050902</div>
                <div><strong>Ungueltig:</strong> 2511 010100, 5255 121299, 4999 070700</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <script src="./vendor/qrcode.js"></script>
  <script src="./app.js"></script>
</body>
</html>
```

</details>

<details>
<summary>styles.css</summary>

```css
body {
  background: #f5f7fb;
}

.card {
  border-radius: 1rem;
}

.qr-panel {
  padding: 1rem;
  background: #f8fafc;
  border: 1px solid #dbe3f0;
  border-radius: 0.75rem;
}

.qr-code-box {
  min-width: 188px;
  min-height: 188px;
  display: grid;
  place-items: center;
  padding: 0.75rem;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 0.75rem;
}

.qr-code-box svg {
  display: block;
  width: 168px;
  height: 168px;
}
```

</details>

<details>
<summary>app.js</summary>

```javascript
const form = document.getElementById("stammdaten-form");
const firstNameInput = document.getElementById("vorname");
const lastNameInput = document.getElementById("nachname");
const svInput = document.getElementById("svnummer");
const svFeedback = document.getElementById("svnummer-feedback");
const resultWrapper = document.getElementById("result-wrapper");
const resultAlert = document.getElementById("result-alert");
const qrCodeBox = document.getElementById("qr-code");
const qrPayload = document.getElementById("qr-payload");
const resetButton = document.getElementById("reset-button");

svInput.addEventListener("input", () => {
  svInput.value = formatSvInput(svInput.value);
  svInput.classList.remove("is-invalid", "is-valid");
});

firstNameInput.addEventListener("input", () => {
  firstNameInput.classList.remove("is-invalid");
});

lastNameInput.addEventListener("input", () => {
  lastNameInput.classList.remove("is-invalid");
});

form.addEventListener("submit", (event) => {
  event.preventDefault();

  clearValidationState();

  const firstName = firstNameInput.value.trim();
  const lastName = lastNameInput.value.trim();
  const svNumber = svInput.value.trim();

  let hasMissingRequiredField = false;

  if (!firstName) {
    firstNameInput.classList.add("is-invalid");
    hasMissingRequiredField = true;
  }

  if (!lastName) {
    lastNameInput.classList.add("is-invalid");
    hasMissingRequiredField = true;
  }

  if (!svNumber) {
    svFeedback.textContent = "Bitte eine SV-Nummer eingeben.";
    svInput.classList.add("is-invalid");
    hasMissingRequiredField = true;
  }

  if (hasMissingRequiredField) {
    hideResult();
    return;
  }

  const validation = validateAustrianSvNumber(svNumber);

  if (validation.isValid) {
    svInput.classList.add("is-valid");
    showResult({
      ok: true,
      title: "SV-Nummer ist gueltig.",
      detail: "Der QR-Code enthaelt den Text Richtig.",
      payload: "Richtig"
    });
    return;
  }

  svFeedback.textContent = validation.message;
  svInput.classList.add("is-invalid");
  showResult({
    ok: false,
    title: "SV-Nummer ist ungueltig.",
    detail: "Der QR-Code enthaelt den Text Falsch.",
    payload: "Falsch"
  });
});

resetButton.addEventListener("click", () => {
  form.reset();
  clearValidationState();
  hideResult();
});

function clearValidationState() {
  firstNameInput.classList.remove("is-invalid");
  lastNameInput.classList.remove("is-invalid");
  svInput.classList.remove("is-invalid", "is-valid");
  svFeedback.textContent = "Bitte eine SV-Nummer eingeben.";
}

function hideResult() {
  resultWrapper.classList.add("d-none");
  qrCodeBox.innerHTML = "";
  qrPayload.textContent = "";
  resultAlert.className = "alert mb-3";
  resultAlert.textContent = "";
}

function showResult({ ok, title, detail, payload }) {
  resultWrapper.classList.remove("d-none");
  resultAlert.className = ok ? "alert alert-success mb-3" : "alert alert-danger mb-3";
  resultAlert.innerHTML = `<strong>${escapeHtml(title)}</strong><br>${escapeHtml(detail)}`;
  qrPayload.textContent = payload;
  renderQrCode(payload);
}

function renderQrCode(payload) {
  qrCodeBox.innerHTML = "";

  const qr = qrcode(0, "M");
  qr.addData(payload);
  qr.make();

  qrCodeBox.innerHTML = qr.createSvgTag(6, 0);
}

function formatSvInput(value) {
  const digits = value.replace(/\D/g, "").slice(0, 10);

  if (digits.length <= 4) {
    return digits;
  }

  return `${digits.slice(0, 4)} ${digits.slice(4)}`;
}

function validateAustrianSvNumber(rawValue) {
  const digits = rawValue.replace(/\D/g, "");

  if (!/^\d{10}$/.test(digits)) {
    return {
      isValid: false,
      message: "Die SV-Nummer muss aus genau 10 Ziffern bestehen."
    };
  }

  const day = Number(digits.slice(4, 6));
  const month = Number(digits.slice(6, 8));
  const year = Number(digits.slice(8, 10));

  if (!isValidSvDatePart(day, month, year)) {
    return {
      isValid: false,
      message: "Der Datumsanteil der SV-Nummer ist ungueltig."
    };
  }

  const expectedCheckDigit = computeCheckDigit(digits);
  const actualCheckDigit = Number(digits[3]);

  if (expectedCheckDigit === 10 || actualCheckDigit !== expectedCheckDigit) {
    return {
      isValid: false,
      message: "Die Pruefziffer der SV-Nummer ist ungueltig."
    };
  }

  return {
    isValid: true,
    message: ""
  };
}

function computeCheckDigit(digits) {
  const relevantDigits = [
    Number(digits[0]),
    Number(digits[1]),
    Number(digits[2]),
    Number(digits[4]),
    Number(digits[5]),
    Number(digits[6]),
    Number(digits[7]),
    Number(digits[8]),
    Number(digits[9])
  ];

  const weights = [3, 7, 9, 5, 8, 4, 2, 1, 6];

  const sum = relevantDigits.reduce((accumulator, digit, index) => {
    return accumulator + digit * weights[index];
  }, 0);

  return sum % 11;
}

function isValidSvDatePart(day, month, year) {
  if (day < 1 || day > 31) {
    return false;
  }

  if (month >= 13 && month <= 99) {
    // Officially a fictitious month value can be used in special cases.
    return true;
  }

  if (month < 1 || month > 12) {
    return false;
  }

  const fullYears = [1900 + year, 2000 + year];

  return fullYears.some((fullYear) => isRealCalendarDate(fullYear, month, day));
}

function isRealCalendarDate(year, month, day) {
  const date = new Date(year, month - 1, day);

  return date.getFullYear() === year
    && date.getMonth() === month - 1
    && date.getDate() === day;
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}
```

</details>

## Mit tud?

- responsive űrlap `Bootstrap`-pel
- kötelező mezők ellenőrzése
- osztrák `SV-Nr` validálása
- `QR`-kód generálása `Richtig` / `Falsch` tartalommal

## Mit nem tud?

- adatmentés
- backend
- adatbázis
- extra UX vagy admin funkciók

## Futtatás

1. Nyisd meg az `index.html` fájlt böngészőben.
2. Töltsd ki a mezőket.
3. Kattints a gombra.
4. Ellenőrizd a megjelenő eredményt és a `QR`-kódot.

## Ajánlott tesztadatok

### Érvényes

- `4422 180599`
- `3567 010705`
- `5884 050902`

### Érvénytelen

- `2511 010100`
- `5255 121299`
- `4999 070700`

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135

3. Bootstrap Docs  
   https://getbootstrap.com/docs/5.3/getting-started/introduction/

4. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator

Megnyitva: `2026-04-09`
