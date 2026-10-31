// 公開前チェック：仮置きの文言・テスト用の ID・ダミーの連絡先などが残っていないかを調べる
// 調べる中身は kit.config.json の releaseCheck（files：対象の glob、pattern：正規表現、message：理由）
// 使い方：node tools/release-check.mjs（見つかれば一覧を出して終了コード1）。CI と公開用ビルドの前に回す
import { execFileSync } from 'node:child_process';
import { readFileSync, statSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { ROOT, loadConfig } from './kit-config.mjs';

// ひな形そのものや説明書きは調べない（例として禁止語を書いているため）
const ALWAYS_SKIP = ['kit.config.json', 'templates/**', 'docs/**', 'node_modules/**', 'dist/**', 'www/**', '**/*.test.mjs'];
const MAX_SCAN = 2 << 20;

// "**/*.html" → 正規表現。** はフォルダをまたぐ、* はまたがない
export function globToRegExp(glob) {
  let re = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*' && glob[i + 1] === '*') { re += glob[i + 2] === '/' ? '(?:.*/)?' : '.*'; i += glob[i + 2] === '/' ? 2 : 1; }
    else if (c === '*') re += '[^/]*';
    else if (c === '?') re += '[^/]';
    else re += c.replace(/[.+^${}()|[\]\\]/g, '\\$&');
  }
  return new RegExp(`^${re}$`);
}

// rules：kit.config.json の releaseCheck、files：調べるパス、read：中身を返す関数（読めなければ null）
export function releaseProblems(rules, files, read, skip = []) {
  const skipRe = [...ALWAYS_SKIP, ...skip].map(globToRegExp);
  const out = [];
  for (const rule of rules) {
    let re;
    try { re = new RegExp(rule.pattern); } catch (e) { out.push(`kit.config.json の releaseCheck の pattern が正規表現として読めません：${rule.pattern}`); continue; }
    const targets = (rule.files || ['**']).map(globToRegExp);
    for (const f of files) {
      if (skipRe.some(r => r.test(f)) || !targets.some(r => r.test(f))) continue;
      const text = read(f);
      if (text == null) continue;
      text.split('\n').forEach((line, i) => {
        const m = line.match(re);
        if (m) out.push(`${f}:${i + 1}  ${rule.message || '公開前に直す箇所'}：${m[0]}`);
      });
    }
  }
  return out;
}

function gitFiles() {
  const git = (...a) => execFileSync('git', a, { cwd: ROOT, encoding: 'utf8' });
  return [...new Set((git('ls-files') + git('ls-files', '--others', '--exclude-standard')).split('\n').filter(Boolean))];
}

function readSmall(f) {
  try { const p = path.join(ROOT, f); return statSync(p).size > MAX_SCAN ? null : readFileSync(p, 'utf8'); } catch { return null; }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  try {
    const cfg = loadConfig();
    const probs = releaseProblems(cfg.releaseCheck || [], gitFiles(), readSmall, cfg.releaseCheckSkip || []);
    if (probs.length) {
      console.error(`公開前に直す箇所が ${probs.length} 件あります：\n` + probs.map(p => '  - ' + p).join('\n'));
      process.exit(1);
    }
    console.log('公開前チェック：問題は見つかりませんでした');
  } catch (e) {
    console.error(e.message);
    process.exit(1);
  }
}
