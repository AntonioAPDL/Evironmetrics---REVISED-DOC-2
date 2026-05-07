#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

from article_asset_manifest import load_manifest, manifest_path


CURRENT_MODEL_SOURCE_CLASSES = {
    'setup_support_v2_representative',
    'current_selected_model_representative',
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_line(text: str, needle: str) -> int:
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i
    return -1


def grouped(items, key):
    out = {}
    for item in items:
        out.setdefault(item[key], []).append(item)
    return out


def build_current_model_output_wiring_audit(out_root: Path, fig_rows: list[dict], table_rows: list[dict]) -> None:
    md: list[str] = []
    md.append('# Current Model-Output Wiring Audit\n\n')
    md.append('This audit is generated from `ARTICLE_GENERATED_ASSET_MANIFEST.json` and the current article-side generated bundles.\n\n')
    md.append('## Figure and Table Status\n\n')
    md.append('| Manuscript object | Current article number | Current source | Current-model-output wired? | Notes |\n')
    md.append('|---|---|---|---:|---|\n')
    figure_numbers = {
        'fig:sanlorenzo': 'Figure 1',
        'fig:covariates': 'Figure 2',
        'fig:retrospectives': 'Figure 3',
        'fig:ensembles': 'Figure 4',
        'fig:dry_quantile': 'Figure 5',
        'fig:rainy_quantile': 'Figure 6',
        'fig:synth1': 'Figure 7',
        'fig:80_components': 'Figure A1',
        'fig:synth2': 'Figure A2',
    }
    table_numbers = {
        'tab:components_23_31': 'Table 2',
        'tab:gamma_sigma_intervals1': 'Table A.1',
        'tab:gamma_sigma_intervals2': 'Table A.2',
        'tab:benchmark_crps_models': 'Table 1',
    }
    for row in fig_rows:
        md.append(f"| `{row['label']}` | {figure_numbers.get(row['label'], '')} | `{row['generated_source']}` -> `DISC/{row['filename']}` | {'Yes' if row['current_model_output_wired'] else 'No'} | {row['note']} |\n")
    for row in table_rows:
        wired = row['source_class'] in CURRENT_MODEL_SOURCE_CLASSES or row['label'] == 'tab:benchmark_crps_models'
        note = row['note'] + '; now auto-included into TeX' if row['generated_tex_exists'] else row['note']
        md.append(f"| `{row['label']}` | {table_numbers.get(row['label'], '')} | `{row['generated_tex']}` | {'Yes' if wired else 'No'} | {note} |\n")
    (out_root / 'CURRENT_MODEL_OUTPUT_WIRING_AUDIT.md').write_text(''.join(md))


def main() -> None:
    parser = argparse.ArgumentParser(description='Build a review report for current article assets.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    article_root = args.article_root.resolve()
    out_root = article_root / 'generated' / 'article_asset_review'
    out_root.mkdir(parents=True, exist_ok=True)
    disc_root = article_root / 'DISC'
    tex = (article_root / 'wileyNJD-APA.tex').read_text()
    manifest = load_manifest(article_root)

    fig_rows = []
    for fig in manifest['figures']:
        article_path = disc_root / fig['filename']
        bundle_path = article_root / fig['generated_source']
        fig_rows.append({
            **fig,
            'article_path': str(article_path),
            'bundle_path': str(bundle_path),
            'sha256': sha256(article_path),
            'size_bytes': article_path.stat().st_size,
            'tex_line': find_line(tex, fig['filename']),
        })

    table_rows = []
    for tbl in manifest['tables'].values():
        generated_tex = article_root / tbl['generated_tex']
        table_rows.append({
            **tbl,
            'source_path': ', '.join(tbl['sources'].values()),
            'generated_tex_path': str(generated_tex),
            'generated_tex': tbl['generated_tex'],
            'generated_tex_exists': generated_tex.exists(),
            'sha256': sha256(generated_tex),
            'size_bytes': generated_tex.stat().st_size,
            'tex_line': find_line(tex, tbl['label']),
        })

    with (out_root / 'figure_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['label','filename','category','role','article_path','bundle_path','sha256','size_bytes','tex_line','source_class','current_model_output_wired','note'])
        for row in fig_rows:
            writer.writerow([row['label'],row['filename'],row['category'],row['role'],row['article_path'],row['bundle_path'],row['sha256'],row['size_bytes'],row['tex_line'],row['source_class'],row['current_model_output_wired'],row['note']])

    with (out_root / 'table_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['label','role','generated_tex','source_path','sha256','size_bytes','tex_line','source_class','note'])
        for row in table_rows:
            writer.writerow([row['label'],row['role'],row['generated_tex'],row['source_path'],row['sha256'],row['size_bytes'],row['tex_line'],row['source_class'],row['note']])

    md = []
    md.append('# Article Asset Review Report\n\n')
    md.append('This report groups the current revised-article figures and tables by provenance role so they can be reviewed visually and operationally.\n\n')
    md.append(f'Manifest contract: `{manifest_path(article_root).name}`\n\n')
    md.append('Primary visual gallery: `generated/article_asset_review/figure_gallery.html`\n\n')
    md.append('Primary wiring audit: `generated/article_asset_review/CURRENT_MODEL_OUTPUT_WIRING_AUDIT.md`\n\n')
    md.append('## Review priorities\n\n')
    md.append('1. Check that setup/input figures are legible and still appropriate.\n')
    md.append('2. Check that `fig:synth1` matches the intended representative selected-model story.\n')
    md.append('3. Check that historical-summary figures read as descriptive support rather than validation evidence.\n')
    md.append('4. Check that appendix support figures/tables are still placed appropriately.\n\n')

    for category, items in grouped(fig_rows, 'category').items():
        md.append(f'## {category}\n\n')
        md.append('| Label | Role | Article file | Generated source | TeX line | Wired to current outputs? | Note |\n')
        md.append('|---|---|---|---|---:|---|---|\n')
        for row in items:
            rel_bundle = Path(row['bundle_path']).as_posix().split(str(article_root) + '/', 1)[-1]
            md.append(f"| `{row['label']}` | {row['role']} | `{Path(row['article_path']).name}` | `{rel_bundle}` | {row['tex_line']} | {'yes' if row['current_model_output_wired'] else 'no'} | {row['note']} |\n")
        md.append('\n')

    md.append('## Tables\n\n')
    md.append('| Label | Role | Generated include | TeX line | Note |\n')
    md.append('|---|---|---|---:|---|\n')
    for row in table_rows:
        md.append(f"| `{row['label']}` | {row['role']} | `{row['generated_tex']}` | {row['tex_line']} | {row['note']} |\n")
    md.append('\n')
    md.append('## Generated manifests\n\n')
    md.append('- `generated/article_asset_review/figure_manifest.csv`\n')
    md.append('- `generated/article_asset_review/table_manifest.csv`\n')
    md.append('- `generated/article_asset_review/CURRENT_MODEL_OUTPUT_WIRING_AUDIT.md`\n')
    (out_root / 'ARTICLE_ASSET_REVIEW.md').write_text(''.join(md))

    html = []
    html.append('<!doctype html><html><head><meta charset="utf-8"><title>Article Figure Review</title>')
    html.append('<style>body{font-family:Arial,sans-serif;margin:24px;} .grid{display:grid;grid-template-columns:1fr;gap:28px;} .card{border:1px solid #ddd;padding:16px;border-radius:8px;background:#fff;} img{max-width:100%;height:auto;border:1px solid #eee;} h1,h2{margin-top:0} .meta{font-size:14px;color:#333;line-height:1.5;} code{background:#f4f4f4;padding:2px 4px;border-radius:4px;} .cat{margin-top:36px;}</style></head><body>')
    html.append('<h1>Revised Article Figure Review</h1>')
    html.append(f'<p>This gallery shows the current figure assets exactly as used by the revised article. Selection contract: <code>{manifest_path(article_root).name}</code>.</p>')
    for category, items in grouped(fig_rows, 'category').items():
        html.append(f'<div class="cat"><h2>{category}</h2><div class="grid">')
        for row in items:
            img_rel = '../../DISC/' + row['filename']
            html.append('<div class="card">')
            html.append(f'<h3>{row["label"]}</h3>')
            html.append(f'<p class="meta"><strong>Role:</strong> {row["role"]}<br><strong>TeX line:</strong> {row["tex_line"]}<br><strong>Generated source:</strong> <code>{row["generated_source"]}</code><br><strong>Source class:</strong> {row["source_class"]}<br><strong>Current-model-output wired:</strong> {"yes" if row["current_model_output_wired"] else "no"}<br><strong>Note:</strong> {row["note"]}</p>')
            html.append(f'<img src="{img_rel}" alt="{row["label"]}">')
            html.append('</div>')
        html.append('</div></div>')
    html.append('</body></html>')
    (out_root / 'figure_gallery.html').write_text(''.join(html))

    build_current_model_output_wiring_audit(out_root, fig_rows, table_rows)
    print('Built article asset review report successfully.')


if __name__ == '__main__':
    main()
