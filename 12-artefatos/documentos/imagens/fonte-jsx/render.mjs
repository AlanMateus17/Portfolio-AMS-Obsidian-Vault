import fs from 'fs'; import path from 'path'; import * as esbuild from 'esbuild';
import React from 'react'; import { renderToStaticMarkup } from 'react-dom/server';
const [,, inDir, outDir] = process.argv;
fs.mkdirSync(outDir, { recursive: true });
// cores fixas no lugar das variáveis do tema (funciona fora do claude.ai, claro e escuro legível)
const VARS = { '--cds-chart-axis':'#6b7280', '--cds-chart-categorical-1':'#2563eb', '--cds-chart-categorical-2':'#d97706', '--cds-chart-categorical-3':'#059669', '--cds-chart-categorical-4':'#7c3aed', '--cds-chart-categorical-5':'#db2777', '--cds-text-primary':'#111827', '--cds-text-secondary':'#4b5563', '--cds-chart-reference-tint':'#f3f4f6', '--cds-chart-grid':'#e5e7eb', '--cds-chart-muted':'#9ca3af', '--cds-surface':'#ffffff', '--cds-background':'#ffffff' };
const claude = { Visualize: ({ sources, children }) => { const d = {}; for (const k in sources) d[k] = sources[k].data; return children({ ...d, datum: () => ({}) }); } };
const fix = s => s.replace(/var\((--[a-z0-9-]+)\)/g, (m, v) => VARS[v] || (console.error('variável sem cor:', v), '#6b7280'));
let ok = 0, fail = 0;
for (const f of fs.readdirSync(inDir).filter(f => f.endsWith('.jsx')).sort()) {
  try {
    const src = fs.readFileSync(path.join(inDir, f), 'utf8');
    const { code } = await esbuild.transform(src, { loader: 'jsx', format: 'cjs', jsx: 'transform' });
    const m = { exports: {} }; new Function('module', 'exports', 'React', 'claude', code)(m, m.exports, React, claude);
    const Comp = m.exports.default;
    let svg = renderToStaticMarkup(React.createElement(Comp));
    svg = fix(svg).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif" ');
    fs.writeFileSync(path.join(outDir, f.replace(/\.jsx$/, '.svg')), svg); ok++;
  } catch (e) { console.error('ERRO', f, e.message); fail++; }
}
console.log('svg ok', ok, 'erro', fail);
