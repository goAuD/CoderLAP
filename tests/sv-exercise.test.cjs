const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const sample = path.join(__dirname, '../18_Uebungsbeispiel/06_Musterloesung_Minimal');
const app = fs.readFileSync(path.join(sample, 'app.js'), 'utf8');
const html = fs.readFileSync(path.join(sample, 'index.html'), 'utf8');
const makeQr = require(path.join(sample, 'vendor/qrcode.js'));

function loadSample() {
  const elements = new Map();
  for (const [, id] of html.matchAll(/\bid="([^"]+)"/g)) {
    const classes = new Set();
    elements.set(id, {
      value: '', innerHTML: '', textContent: '', className: '', listeners: {},
      classList: {
        add: (...names) => names.forEach(name => classes.add(name)),
        remove: (...names) => names.forEach(name => classes.delete(name)),
        contains: name => classes.has(name),
      },
      addEventListener(type, callback) { this.listeners[type] = callback; },
    });
  }
  const get = id => {
    assert.ok(elements.has(id), `Unknown HTML element: ${id}`);
    return elements.get(id);
  };
  get('stammdaten-form').reset = () => {
    for (const id of ['vorname', 'nachname', 'svnummer']) get(id).value = '';
  };
  const payloads = [];
  const context = vm.createContext({
    document: { getElementById: get },
    qrcode: (...args) => {
      const qr = makeQr(...args);
      const addData = qr.addData;
      qr.addData = value => { payloads.push(value); addData(value); };
      return qr;
    },
  });
  vm.runInContext(app, context, { timeout: 1000 });
  const submit = () => {
    let prevented = false;
    get('stammdaten-form').listeners.submit({ preventDefault() { prevented = true; } });
    assert.equal(prevented, true, 'The exercise must not submit personal data');
  };
  return { context, get, payloads, submit };
}

for (const [number, expected] of [
  ['4422 180599', true], ['3567 010705', true], ['5884 050902', true],
  ['2511 010100', false], ['5255 121299', false], ['4999 070700', false],
]) {
  test(`SV exercise: official PDF example ${number}`, () => {
    const { context } = loadSample();
    assert.equal(context.validateAustrianSvNumber(number).isValid, expected);
  });
}

test('SV exercise rejects malformed input without silently repairing it', () => {
  const { context } = loadSample();
  for (const input of ['4422x180599', '44221805990', '442218059', '4422-180599', '']) {
    assert.equal(context.validateAustrianSvNumber(input).isValid, false, input);
  }
  assert.equal(context.formatSvInput('4422x180599'), '4422x180599');
  assert.equal(context.formatSvInput('44221805990'), '44221805990');
  assert.equal(context.formatSvInput('4422180599'), '4422 180599');
  assert.equal(context.validateAustrianSvNumber(' 4422 180599 ').isValid, true);
});

test('SV exercise checks the serial-number and date boundaries', () => {
  const { context } = loadSample();
  // Synthetic examples, not person records. Both have matching check digits.
  assert.equal(context.validateAustrianSvNumber('0122010100').isValid, false);
  assert.equal(context.validateAustrianSvNumber('1232310424').isValid, false);
  assert.equal(context.isValidSvDatePart(29, 2, 24), true);
  assert.equal(context.isValidSvDatePart(29, 2, 23), false);
  assert.equal(context.isValidSvDatePart(1, 13, 0), true);
  assert.equal(context.isValidSvDatePart(0, 13, 0), false);
  assert.equal(context.isValidSvDatePart(32, 13, 0), false);
  assert.equal(context.isValidSvDatePart(1, 0, 0), false);
});

test('SV exercise accepts a zero check digit and rejects remainder ten', () => {
  const { context } = loadSample();
  // Dachverband's published arithmetic example has sum 176, remainder zero.
  assert.equal(context.validateAustrianSvNumber('1680250250').isValid, true);
  // Synthetic serial 107 + date 010100 gives sum 76, remainder ten.
  for (let check = 0; check <= 9; check++) {
    assert.equal(context.validateAustrianSvNumber(`107${check}010100`).isValid, false);
  }
});

test('SV exercise generates only the required words and clears stale results', () => {
  const { get, submit, payloads } = loadSample();
  get('vorname').value = 'Test';
  get('nachname').value = 'Beispiel';
  get('svnummer').value = '4422 180599';
  submit();
  assert.equal(get('qr-payload').textContent, 'Richtig');
  assert.match(get('qr-code').innerHTML, /^<svg\b/);
  // 21 modules plus four quiet-zone modules on each side, at six units each.
  assert.match(get('qr-code').innerHTML, /viewBox="0 0 174 174"/);

  get('svnummer').value = '2511 010100';
  get('svnummer').listeners.input();
  assert.equal(get('qr-code').innerHTML, '');
  assert.equal(get('result-wrapper').classList.contains('d-none'), true);
  submit();
  assert.equal(get('qr-payload').textContent, 'Falsch');
  assert.deepEqual(payloads, ['Richtig', 'Falsch']);

  get('vorname').value = '   ';
  submit();
  assert.equal(get('vorname').classList.contains('is-invalid'), true);
  assert.equal(get('qr-code').innerHTML, '');
  assert.equal(payloads.length, 2, 'A missing required field must not generate a QR');
});

test('SV exercise clears the result when either name changes or the form resets', () => {
  for (const id of ['vorname', 'nachname']) {
    const { get, submit } = loadSample();
    get('vorname').value = 'Test';
    get('nachname').value = 'Beispiel';
    get('svnummer').value = '4422 180599';
    submit();
    get(id).listeners.input();
    assert.equal(get('qr-code').innerHTML, '');
    submit();
    get('reset-button').listeners.click();
    assert.equal(get('qr-code').innerHTML, '');
    assert.equal(get('svnummer').value, '');
  }
});

for (const readme of ['README.md', 'README.de.md']) {
  test(`SV exercise: ${readme} publishes the actual complete source`, () => {
    const markdown = fs.readFileSync(path.join(sample, readme), 'utf8').replace(/\r\n/g, '\n');
    for (const [filename, language] of [['index.html', 'html'], ['styles.css', 'css'], ['app.js', 'javascript']]) {
      const section = markdown.split(`<summary>${filename}</summary>`)[1];
      assert.ok(section, filename);
      const published = section.match(new RegExp('```' + language + '\n([\\s\\S]*?)\n```'))?.[1];
      const actual = fs.readFileSync(path.join(sample, filename), 'utf8').replace(/\r\n/g, '\n').trimEnd();
      assert.equal(published, actual, filename);
    }
  });
}
