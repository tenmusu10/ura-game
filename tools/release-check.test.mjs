// release-check.mjs のテスト：npm test
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { globToRegExp, releaseProblems } from './release-check.mjs';

test('glob：** はフォルダをまたぎ、* はまたがない', () => {
  assert.ok(globToRegExp('**/*.html').test('index.html'));
  assert.ok(globToRegExp('**/*.html').test('a/b/legal.html'));
  assert.equal(globToRegExp('*.html').test('a/legal.html'), false);
  assert.ok(globToRegExp('js/*.js').test('js/config.js'));
  assert.equal(globToRegExp('js/*.js').test('js/config.json'), false);
});

const rules = [
  { files: ['**/*.html'], pattern: 'class="ph"', message: '仮置き' },
  { files: ['**/*.js'], pattern: 'ca-app-pub-3940256099942544', message: 'テスト用広告' },
];
const files = { 'index.html': '<p>\n<span class="ph">000</span>\n</p>', 'js/ad.js': "const ID = 'ca-app-pub-3940256099942544/123';", 'templates/x.html': '<span class="ph">', 'README.md': 'class="ph" の説明' };
const read = f => files[f] ?? null;

test('ファイルと行番号つきで見つける', () => {
  assert.deepEqual(releaseProblems(rules, Object.keys(files), read), [
    'index.html:2  仮置き：class="ph"',
    'js/ad.js:1  テスト用広告：ca-app-pub-3940256099942544',
  ]);
});

test('templates/・対象外の拡張子・skip に入れたものは見ない', () => {
  assert.deepEqual(releaseProblems(rules, ['templates/x.html', 'README.md'], read), []);
  assert.deepEqual(releaseProblems(rules, ['index.html'], read, ['index.html']), []);
});

test('壊れた正規表現はそれ自体を問題として出す', () => {
  assert.match(releaseProblems([{ pattern: '(' }], ['index.html'], read)[0], /正規表現/);
});
