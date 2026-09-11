const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const moduleRoot = path.join(__dirname, '..', '15_Grundkenntnisse_des_Programmierens');
const topics = [
  '05_Sortieralgorithmen_Bubblesort_Quicksort',
  '06_Suchalgorithmen_sequentiell_binaer',
  '17_Schleifen',
];

function examplesIn(topic, filename) {
  const markdown = fs.readFileSync(path.join(moduleRoot, topic, filename), 'utf8');
  const fences = Array.from(markdown.matchAll(/^```([^\r\n]*)\r?\n([\s\S]*?)^```\s*$/gm));
  const examples = [];
  for (let index = 0; index < fences.length; index++) {
    if (fences[index][1] !== 'javascript') continue;
    const output = fences[index + 1];
    assert.equal(output?.[1], 'text', `${topic}/${filename}: example needs an output block`);
    examples.push({ code: fences[index][2], expected: output[2].trim() });
  }
  assert.ok(examples.length > 0, `${topic}/${filename}: no runnable examples`);
  return examples;
}

function execute(code) {
  const output = [];
  const context = vm.createContext({ console: { log: (...values) => output.push(values.join(' ')) } });
  vm.runInContext(code, context, { timeout: 1000 });
  return { context, output: output.join('\n') };
}

for (const topic of topics) {
  const hungarian = examplesIn(topic, 'README.md');
  const german = examplesIn(topic, 'README.de.md');
  test(`${topic}: both languages publish identical code and outputs`, () => {
    assert.deepEqual(german, hungarian);
  });
  for (const [language, examples] of [['hu', hungarian], ['de', german]]) {
    examples.forEach((example, index) => {
      test(`${topic}/${language}: example ${index + 1} matches the published output`, () => {
        assert.equal(execute(example.code).output, example.expected);
      });
    });

    if (topic.startsWith('05_')) {
      for (const [index, functionName] of ['bubbleSort', 'quickSort'].entries()) {
        test(`${topic}/${language}: ${functionName} preserves input and sorts boundary cases`, () => {
          const { context } = execute(examples[index].code);
          const cases = [[], [7], [3, 1, 2], [2, 2, 1], [-3, 0, -7, 2.5], [1, 2, 3, 4], [4, 3, 2, 1]];
          context.cases = cases.map(values => [...values]);
          context.sortResults = [];
          vm.runInContext(`
            for (const values of cases) {
              const result = ${functionName}(values);
              sortResults.push({ result, values, distinct: result !== values });
            }
          `, context, { timeout: 1000 });
          context.sortResults.forEach(({ result, values, distinct }, caseIndex) => {
            const original = cases[caseIndex];
            assert.deepEqual(Array.from(result), [...original].sort((a, b) => a - b));
            assert.deepEqual(values, original);
            assert.equal(distinct, true);
          });
        });
      }
    }

    if (topic.startsWith('06_')) {
      for (const [index, functionName] of ['linearSearch', 'binarySearch'].entries()) {
        test(`${topic}/${language}: ${functionName} finds present values and terminates without a match`, () => {
          const { context } = execute(examples[index].code);
          context.cases = [[], [7], [-7, -3, 0, 2.5], [1, 2, 2, 4]];
          context.targets = [-8, -7, -3, 0, 1, 2, 2.5, 3, 4, 7, 8];
          context.searchResults = [];
          const before = JSON.stringify(context.cases);
          vm.runInContext(`
            for (const values of cases) {
              for (const target of targets) {
                searchResults.push({ values, target, result: ${functionName}(values, target) });
              }
            }
          `, context, { timeout: 1000 });
          for (const { values, target, result } of context.searchResults) {
            if (functionName === 'linearSearch' || !values.includes(target)) {
              assert.equal(result, values.indexOf(target));
            } else {
              assert.ok(Number.isInteger(result) && result >= 0 && result < values.length);
              assert.equal(values[result], target);
            }
          }
          assert.equal(JSON.stringify(context.cases), before);
        });
      }
    }
  }
}
