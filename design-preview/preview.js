// Preview-only behavior. Existing progress is read only; no remote requests.
const progressPill = document.querySelector('.hero-progress');
function showProgress() {
  if (!progressPill) return;
  let progress = {};
  try {
    const saved = JSON.parse(localStorage.getItem('coderlap_progress'));
    if (saved && typeof saved === 'object' && !Array.isArray(saved)) progress = saved;
  } catch { /* Unavailable or invalid storage leaves the counter at zero. */ }
  const total = Number(progressPill.dataset.total);
  const done = Math.min(total, Object.values(progress).filter(entry => entry?.status === 'done').length);
  const count = `${done} / ${total}`;
  progressPill.querySelector('[data-progress-count]').textContent = count;
  progressPill.setAttribute('aria-label', `${progressPill.dataset.label}: ${count}`);
  progressPill.querySelector('.progress-value').setAttribute('stroke-dashoffset', String(total ? 100 - done / total * 100 : 100));
  progressPill.hidden = false;
}
showProgress();
window.addEventListener('pageshow', showProgress);
window.addEventListener('storage', event => {
  if (event.key === 'coderlap_progress' || event.key === null) showProgress();
});

const search = document.querySelector('#search');
const cards = [...document.querySelectorAll('.module-card')];
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

function filterTopics() {
  const query = normalize(search.value.trim());
  let found = 0;
  for (const card of cards) {
    const moduleMatch = normalize(card.querySelector('.module-title').textContent).includes(query);
    let count = 0;
    for (const item of card.querySelectorAll('li')) {
      const match = !query || moduleMatch || normalize(item.dataset.search).includes(query);
      item.hidden = !match;
      if (match) count++;
    }
    card.hidden = count === 0;
    card.open = Boolean(query && count);
    found += count;
  }
  const status = document.querySelector('#search-status');
  status.hidden = !query;
  status.textContent = `${found} ${document.documentElement.lang === 'hu' ? 'találat' : 'Treffer'}`;
  document.querySelector('#no-results').hidden = found !== 0;
}

search?.addEventListener('input', filterTopics);
document.addEventListener('keydown', event => {
  if (event.key === '/' && search && !event.ctrlKey && !event.metaKey &&
      !['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName) && !event.target.isContentEditable) {
    event.preventDefault(); search.focus();
  }
});
document.querySelectorAll('[data-module-jump]').forEach(link => {
  link.addEventListener('click', () => {
    search.value = ''; filterTopics();
    const card = document.querySelector(`#module-${link.dataset.moduleJump}`);
    card.open = true;
    card.querySelector('summary').focus({preventScroll: true});
  });
});
// Deep links from the lesson also open the selected module.
if (/^#module-\d{2}$/.test(location.hash)) {
  const card = document.querySelector(location.hash);
  if (card) card.open = true;
}
const dialog = document.querySelector('#app-dialog');
document.querySelectorAll('[data-app]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelector('#dialog-title').textContent = button.dataset.app;
    dialog.showModal();
  });
});
dialog.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => dialog.close()));
document.querySelector('[data-print]')?.addEventListener('click', () => window.print());
document.querySelector('[data-done]')?.addEventListener('click', event => {
  const button = event.currentTarget;
  const done = button.getAttribute('aria-pressed') !== 'true';
  button.setAttribute('aria-pressed', String(done));
  button.querySelector('span').textContent = done ? button.dataset.undo : button.dataset.label;
  document.querySelector('.done-note').hidden = !done;
});
