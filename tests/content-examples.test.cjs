const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const util = require('node:util');
const vm = require('node:vm');

const root = path.join(__dirname, '..');
const registry = JSON.parse(fs.readFileSync(path.join(root, 'LAP_CONTENT_REGISTRY.json'), 'utf8'));

// Only explicitly marked, self-contained console examples run here.
// Browser, SQL and illustrative fragments have their own documented prerequisites.
function runnableExamples(filename) {
  const markdown = fs.readFileSync(filename, 'utf8').replace(/\r\n/g, '\n');
  const examples = Array.from(markdown.matchAll(/^<!-- example:run -->\s*```javascript\n([\s\S]*?)^```[ \t]*$/gm), match => {
    const nextFence = /^```([^\n]*)\n([\s\S]*?)^```[ \t]*$/m.exec(markdown.slice(match.index + match[0].length));
    assert.equal(nextFence?.[1], 'text', `${filename}: runnable example needs a text output block`);
    return { code: match[1], expected: nextFence[2].trimEnd() };
  });
  assert.equal(examples.length, (markdown.match(/^<!-- example:run -->[ \t]*$/gm) || []).length,
    `${filename}: every run marker must precede a supported JavaScript block`);
  return examples;
}

for (const item of registry.items) {
  const huPath = path.join(root, item.path);
  const dePath = path.join(path.dirname(huPath), 'README.de.md');
  const hungarian = runnableExamples(huPath);
  const german = runnableExamples(dePath);
  if (!hungarian.length && !german.length) continue;

  test(`${item.id}: runnable examples are identical in HU and DE`, () => {
    assert.deepEqual(german, hungarian);
  });

  hungarian.forEach((example, index) => {
    test(`${item.id}: example ${index + 1} produces the published output`, () => {
      const output = [];
      const context = vm.createContext({
        console: { log: (...values) => output.push(util.format(...values)) },
        TextEncoder,
        TextDecoder,
        URL,
        URLSearchParams,
        structuredClone,
      });
      vm.runInContext(example.code, context, { timeout: 1000, filename: `${item.id}-${index + 1}` });
      assert.equal(output.join('\n'), example.expected);
    });
  });
}
