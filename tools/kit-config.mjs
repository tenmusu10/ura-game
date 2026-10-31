// kit.config.json（アプリごとの設定）を読む。道具はここから import し、ワークフローは CLI で値を取る
// 使い方：node tools/kit-config.mjs get android.package   → 値を1行で出す（配列・オブジェクトは JSON）
//         node tools/kit-config.mjs check                → 必須の値が埋まっているかを見る（埋まっていなければ終了コード1）
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

export function loadConfig(root = ROOT) {
  const file = path.join(root, 'kit.config.json');
  let text;
  try { text = fs.readFileSync(file, 'utf8'); } catch { throw new Error('kit.config.json がありません。リポジトリ直下に置いてください（ひな形は teck-matome にあります）'); }
  try { return JSON.parse(text.replace(/^﻿/, '')); } catch (e) { throw new Error(`kit.config.json が JSON として読めません：${e.message}`); }
}

// "android.package" のような点区切りで値を取る。無ければ undefined
export function pick(cfg, key) {
  return key.split('.').reduce((o, k) => (o == null ? undefined : o[k]), cfg);
}

// 使う機能ごとに必須の値。空のままワークフローを動かすと、どこが足りないかをここで言う
const REQUIRED = {
  android: ['android.package', 'android.gradle', 'android.tagPrefix', 'android.buildCommand'],
  store: ['android.package', 'store.ja'],
  web: ['web.pagesRepo', 'web.pagesDir', 'web.buildCommand', 'web.copy'],
};

export function missing(cfg, feature) {
  const keys = REQUIRED[feature];
  if (!keys) throw new Error(`知らない機能です：${feature}（${Object.keys(REQUIRED).join(' / ')}）`);
  return keys.filter(k => {
    const v = pick(cfg, k);
    return v == null || v === '' || (Array.isArray(v) && !v.length);
  });
}

// git の pathspec に変える（「数えない」パスの一覧 → :(exclude)…）
export function excludeSpecs(list) {
  return list.map(p => `:(exclude)${p.replace(/\/$/, '')}`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const [cmd, arg] = process.argv.slice(2);
  try {
    const cfg = loadConfig();
    if (cmd === 'get') {
      const v = pick(cfg, arg || '');
      if (v === undefined) throw new Error(`kit.config.json に ${arg} がありません`);
      console.log(typeof v === 'string' ? v : JSON.stringify(v));
    } else if (cmd === 'check') {
      const miss = missing(cfg, arg || '');
      if (miss.length) throw new Error(`kit.config.json の次の値が空です：${miss.join(', ')}（SETUP.md を見て埋めてください）`);
      console.log(`${arg} に必要な設定はそろっています`);
    } else {
      throw new Error('使い方：node tools/kit-config.mjs get <キー> | check <android|store|web>');
    }
  } catch (e) {
    console.log(`::error::${e.message}`);
    process.exit(1);
  }
}
