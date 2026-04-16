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
