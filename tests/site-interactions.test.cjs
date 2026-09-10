// Dependency-free behavior tests for the script's asynchronous UI states.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { runInNewContext } = require('node:vm');

const source = readFileSync(join(__dirname, '../site/assets/js/site.js'), 'utf8');

function page({ reducedMotion = false, observerSupported = true } = {}) {
  let document;
  class Element {
    constructor(tag) {
      this.tagName = tag.toUpperCase();
      this.children = [];
      this.attributes = {};
      this.events = {};
      this.dataset = {};
      this.className = '';
      this.classList = {
        contains: name => this.className.split(' ').includes(name),
        add: name => { if (!this.classList.contains(name)) this.className += ' ' + name; },
        remove: name => { this.className = this.className.split(' ').filter(x => x !== name).join(' '); },
      };
    }
    appendChild(child) { this.children.push(child); return child; }
    append(...children) { children.forEach(child => this.appendChild(child)); }
    prepend(child) { this.children.unshift(child); }
    replaceChildren(...children) { this.children = children; }
    setAttribute(name, value) { this.attributes[name] = value; }
    getAttribute(name) { return this.attributes[name] ?? null; }
    hasAttribute(name) { return name in this.attributes; }
    removeAttribute(name) { delete this.attributes[name]; }
    addEventListener(name, callback) { (this.events[name] ??= new Set()).add(callback); }
    removeEventListener(name, callback) { this.events[name]?.delete(callback); }
    emit(name, extra = {}) {
      const event = { target: this, preventDefault() {}, ...extra };
      this.events[name]?.forEach(callback => callback(event));
    }
    focus() { document.activeElement = this; }
    contains(target) { return target === this || this.children.some(child => child.contains(target)); }
    matches(selector) {
      if (selector.startsWith('.')) return this.classList.contains(selector.slice(1));
      if (selector.startsWith('[')) return this.hasAttribute(selector.slice(1, -1));
      return this.tagName === selector.split(/[:[]/)[0].toUpperCase();
    }
    querySelectorAll(selector) {
      return this.children.flatMap(child => [
        ...(selector.split(', ').some(part => child.matches(part)) ? [child] : []),
        ...child.querySelectorAll(selector),
      ]);
    }
    querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  }
  document = new Element('document');
  document.body = new Element('body');
  document.body.dataset = { siteRoot: '/hu/', closeLabel: 'Bezárás', loadingLabel: 'Témák betöltése…', loadErrorLabel: 'Nem sikerült.', homeLabel: 'Kezdőlap' };
  document.append(document.body);
  document.createElement = tag => new Element(tag);
  const shell = new Element('div');
  shell.className = 'site-shell';
  const trigger = new Element('a');
  trigger.setAttribute('data-quick-view-link', '');
  trigger.href = '/hu/#catalog-title';
  const section = new Element('article');
  section.className = 'topic-article';
  shell.append(trigger, section);
  document.body.append(shell);
  const pending = [];
  const observed = new Set();
  let intersect;
  const window = { matchMedia: () => ({ matches: reducedMotion }), addEventListener() {} };
  const context = {
    document, window, console, setTimeout, clearTimeout,
    localStorage: { getItem: () => null },
    AbortSignal: { timeout: milliseconds => ({ milliseconds }) },
    fetch: (url, options) => new Promise((resolve, reject) => pending.push({ url, options, resolve, reject })),
  };
  if (observerSupported) {
    context.IntersectionObserver = window.IntersectionObserver = class {
      constructor(callback) { intersect = callback; }
      observe(target) { observed.add(target); }
      unobserve(target) { observed.delete(target); }
    };
  }
  runInNewContext(source, context);
  return { document, trigger, section, pending, observed,
    open: () => document.body.classList.contains('sidebar-open'),
    panel: () => document.querySelector('[data-sidebar-panel]'),
    close: () => document.querySelector('.quick-view-close').emit('click'),
    intersect: () => intersect([{ isIntersecting: true, target: section }]),
  };
}

const settle = () => new Promise(resolve => setImmediate(resolve));
const success = { ok: true, json: async () => ({ main_topics: [{ number: '15', label: 'Loops', topics: [] }] }) };

test('loading is visible and closable; a late response never reopens the overlay', async () => {
  const ui = page();
  ui.trigger.emit('click');
  assert.equal(ui.open(), true);
  assert.equal(ui.panel().getAttribute('aria-busy'), 'true');
  assert.equal(ui.panel().querySelectorAll('.quick-view-skeleton__bar').length, 5);
  assert.equal(ui.pending[0].url, '/hu/data/navigation.json');
  assert.equal(ui.pending[0].options.signal.milliseconds, 5000);
  ui.close();
  ui.trigger.emit('click');
  assert.equal(ui.pending.length, 1, 'reopening while loading must reuse the request');
  ui.close();
  ui.pending[0].resolve(success);
  await settle();
  assert.equal(ui.open(), false);
  assert.equal(ui.document.activeElement, ui.trigger);
  assert.equal(ui.panel().getAttribute('aria-busy'), null);
  assert.equal(ui.panel().querySelectorAll('details').length, 1);
  ui.trigger.emit('click');
  assert.equal(ui.open(), true);
  assert.equal(ui.pending.length, 1, 'loaded navigation is reused');
});

for (const failure of ['http', 'invalid-json-shape', 'network', 'timeout']) {
  test(`${failure}: removes skeleton, offers a home link, and permits retry`, async () => {
    const ui = page();
    ui.trigger.emit('click');
    if (failure === 'http') ui.pending[0].resolve({ ok: false });
    else if (failure === 'invalid-json-shape') ui.pending[0].resolve({ ok: true, json: async () => ({}) });
    else ui.pending[0].reject(new Error(failure));
    await settle();
    assert.equal(ui.open(), true);
    assert.equal(ui.panel().getAttribute('aria-busy'), null);
    assert.equal(ui.panel().querySelector('.quick-view-skeleton'), null);
    assert.equal(ui.panel().querySelector('a').href, '/hu/#catalog-title');
    assert.equal(ui.panel().querySelector('[role]').textContent, 'Nem sikerült.');
    ui.close();
    ui.trigger.emit('click');
    assert.equal(ui.pending.length, 2);
    ui.pending[1].resolve(success);
    await settle();
    assert.equal(ui.panel().querySelectorAll('details').length, 1);
  });
}

test('sections are observed once, without an initial hidden state', () => {
  const ui = page();
  assert.equal(ui.section.hidden, undefined);
  assert.equal(ui.observed.has(ui.section), true);
  ui.intersect();
  assert.equal(ui.section.classList.contains('workshop-reveal'), true);
  assert.equal(ui.observed.has(ui.section), false);
});

for (const options of [{ reducedMotion: true }, { observerSupported: false }]) {
  test(`reveal stays inactive with ${JSON.stringify(options)}`, () => {
    const ui = page(options);
    assert.equal(ui.observed.size, 0);
    assert.equal(ui.section.classList.contains('workshop-reveal'), false);
    assert.equal(ui.section.hidden, undefined);
  });
}
