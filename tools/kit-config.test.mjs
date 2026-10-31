// kit-config.mjs のテスト：npm test
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { loadConfig, pick, missing, excludeSpecs } from './kit-config.mjs';

test('ひな形の kit.config.json が読める', () => {
  const cfg = loadConfig();
  assert.equal(typeof pick(cfg, 'android.tagPrefix'), 'string');
  assert.ok(Array.isArray(cfg.notApp));
  assert.ok(Array.isArray(cfg.releaseCheck));
});

test('点区切りで値を取る', () => {
  const cfg = { a: { b: { c: 1 } } };
  assert.equal(pick(cfg, 'a.b.c'), 1);
  assert.equal(pick(cfg, 'a.x.c'), undefined);
});

test('使う機能に必要な値が空なら名前を返す', () => {
  assert.deepEqual(missing({ android: { package: '', gradle: 'g', tagPrefix: 't', buildCommand: 'b' } }, 'android'), ['android.package']);
  assert.deepEqual(missing({ web: { pagesRepo: 'o/r', pagesDir: '.', buildCommand: 'b', copy: [] } }, 'web'), ['web.copy']);
  assert.throws(() => missing({}, 'ios'), /知らない機能/);
});

test('数えないパスを git の exclude に変える', () => {
  assert.deepEqual(excludeSpecs(['social/', '*.md']), [':(exclude)social', ':(exclude)*.md']);
});
