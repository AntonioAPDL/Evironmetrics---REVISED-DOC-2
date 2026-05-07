#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

FIGURES = [
    {'label':'fig:sanlorenzo','filename':'usgs.png','category':'Setup / Inputs','role':'Study-setting figure','bundle':'generated/workflow_linked_support_sources/figures/usgs.png','note':'Workflow-linked support figure'},
    {'label':'fig:covariates','filename':'precip_soilmoisture_climatePC1_faceted_labeled.png','category':'Setup / Inputs','role':'Covariate setup figure','bundle':'generated/workflow_linked_support_sources/figures/precip_soilmoisture_climatePC1_faceted_labeled.png','note':'Workflow-linked support figure'},
    {'label':'fig:retrospectives','filename':'retrospective_log_discharge_plot_faceted.png','category':'Setup / Inputs','role':'Retrospective-product setup figure','bundle':'generated/workflow_linked_support_sources/figures/retrospective_log_discharge_plot_faceted.png','note':'Workflow-linked support figure'},
    {'label':'fig:ensembles','filename':'forecats.png','category':'Setup / Inputs','role':'Forecast-product setup figure','bundle':'generated/workflow_linked_support_sources/figures/forecats.png','note':'Workflow-linked support figure'},
    {'label':'fig:synth1','filename':'posterior_samples_valid.png','category':'Selected Model','role':'Representative selected-model synthesis','bundle':'generated/exal_m_t1_20221225/posterior_samples_valid.png','note':'Verified representative 2022-12-25 exAL-M-T1 output'},
    {'label':'fig:dry_quantile','filename':'All_exal_2012-2016_DISC.png','category':'Historical Summaries','role':'Dry-period historical summary','bundle':'generated/historical_summary_sources/figures/All_exal_2012-2016_DISC.png','note':'Historical-summary support figure'},
    {'label':'fig:rainy_quantile','filename':'All_exal_2017-2019_DISC.png','category':'Historical Summaries','role':'Rainy-period historical summary','bundle':'generated/historical_summary_sources/figures/All_exal_2017-2019_DISC.png','note':'Historical-summary support figure'},
    {'label':'fig:80_components','filename':'80_component_1991_2022.png','category':'Historical Summaries','role':'Long-cycle component summary','bundle':'generated/historical_summary_sources/figures/80_component_1991_2022.png','note':'Historical-summary support figure'},
    {'label':'fig:synth2','filename':'posterior_samples_counter_valid.png','category':'Appendix Support','role':'Historical-only reference synthesis','bundle':'generated/workflow_linked_support_sources/figures/posterior_samples_counter_valid.png','note':'Workflow-linked appendix support figure'},
]

TABLES = [
    {'label':'tab:benchmark_crps_models','role':'Five-cutoff benchmark table','source':'generated/he2_publication_manifest_snapshot/he2_bayesian_publication_manifest.csv','note':'Frozen HE2 publication manifest snapshot'},
    {'label':'tab:components_23_31','role':'Representative covariate-effects table','source':'generated/exal_m_t1_20221225/covariate_effects_summary.csv','note':'Representative 2022-12-25 exAL-M-T1 output'},
    {'label':'tab:gamma_sigma_intervals1','role':'Appendix gamma summary','source':'generated/exal_m_t1_20221225/gamma_summary.csv','note':'Supplementary appendix support'},
    {'label':'tab:gamma_sigma_intervals2','role':'Appendix sigma summary','source':'generated/exal_m_t1_20221225/sigma_summary.csv','note':'Supplementary appendix support'},
]


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


def main() -> None:
    parser = argparse.ArgumentParser(description='Build a review report for current article assets.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    article_root = args.article_root.resolve()
    out_root = article_root / 'generated' / 'article_asset_review'
    out_root.mkdir(parents=True, exist_ok=True)
    disc_root = article_root / 'DISC'
    tex = (article_root / 'wileyNJD-APA.tex').read_text()

    fig_rows = []
    for fig in FIGURES:
        article_path = disc_root / fig['filename']
        bundle_path = article_root / fig['bundle']
        fig_rows.append({
            **fig,
            'article_path': str(article_path),
            'bundle_path': str(bundle_path),
            'sha256': sha256(article_path),
            'size_bytes': article_path.stat().st_size,
            'tex_line': find_line(tex, fig['filename']),
        })

    table_rows = []
    for tbl in TABLES:
        source = article_root / tbl['source']
        table_rows.append({
            **tbl,
            'source_path': str(source),
            'sha256': sha256(source),
            'size_bytes': source.stat().st_size,
            'tex_line': find_line(tex, tbl['label']),
        })

    with (out_root / 'figure_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['label','filename','category','role','article_path','bundle_path','sha256','size_bytes','tex_line','note'])
        for row in fig_rows:
            writer.writerow([row['label'],row['filename'],row['category'],row['role'],row['article_path'],row['bundle_path'],row['sha256'],row['size_bytes'],row['tex_line'],row['note']])

    with (out_root / 'table_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['label','role','source_path','sha256','size_bytes','tex_line','note'])
        for row in table_rows:
            writer.writerow([row['label'],row['role'],row['source_path'],row['sha256'],row['size_bytes'],row['tex_line'],row['note']])

    md = []
    md.append('# Article Asset Review Report\n')
    md.append('This report groups the current revised-article figures and tables by provenance role so they can be reviewed visually and operationally.\n')
    md.append('Primary visual gallery: `generated/article_asset_review/figure_gallery.html`\n')
    md.append('## Review priorities\n')
    md.append('1. Check that setup/input figures are legible and still appropriate.\n')
    md.append('2. Check that `fig:synth1` matches the intended representative selected-model story.\n')
    md.append('3. Check that historical-summary figures read as descriptive support rather than validation evidence.\n')
    md.append('4. Check that `fig:synth2` still deserves to remain as appendix support.\n')

    for category, items in grouped(fig_rows, 'category').items():
        md.append(f'## {category}\n')
        md.append('| Label | Role | Article file | Bundle file | TeX line | Note |\n')
        md.append('|---|---|---|---|---:|---|\n')
        for row in items:
            md.append(f"| `{row['label']}` | {row['role']} | `{Path(row['article_path']).name}` | `{Path(row['bundle_path']).as_posix().split('generated/',1)[-1]}` | {row['tex_line']} | {row['note']} |\n")
        md.append('\n')

    md.append('## Tables\n')
    md.append('| Label | Role | Source | TeX line | Note |\n')
    md.append('|---|---|---|---:|---|\n')
    for row in table_rows:
        md.append(f"| `{row['label']}` | {row['role']} | `{Path(row['source_path']).as_posix().split(str(article_root) + '/',1)[-1]}` | {row['tex_line']} | {row['note']} |\n")
    md.append('\n')
    md.append('## Generated manifests\n')
    md.append('- `generated/article_asset_review/figure_manifest.csv`\n')
    md.append('- `generated/article_asset_review/table_manifest.csv`\n')
    (out_root / 'ARTICLE_ASSET_REVIEW.md').write_text(''.join(md))

    html = []
    html.append('<!doctype html><html><head><meta charset="utf-8"><title>Article Figure Review</title>')
    html.append('<style>body{font-family:Arial,sans-serif;margin:24px;} .grid{display:grid;grid-template-columns:1fr;gap:28px;} .card{border:1px solid #ddd;padding:16px;border-radius:8px;background:#fff;} img{max-width:100%;height:auto;border:1px solid #eee;} h1,h2{margin-top:0} .meta{font-size:14px;color:#333;line-height:1.5;} code{background:#f4f4f4;padding:2px 4px;border-radius:4px;} .cat{margin-top:36px;}</style></head><body>')
    html.append('<h1>Revised Article Figure Review</h1>')
    html.append('<p>This gallery shows the current figure assets exactly as used by the revised article.</p>')
    for category, items in grouped(fig_rows, 'category').items():
        html.append(f'<div class="cat"><h2>{category}</h2><div class="grid">')
        for row in items:
            img_rel = '../../DISC/' + row['filename']
            html.append('<div class="card">')
            html.append(f'<h3>{row["label"]}</h3>')
            html.append(f'<p class="meta"><strong>Role:</strong> {row["role"]}<br><strong>TeX line:</strong> {row["tex_line"]}<br><strong>Bundle:</strong> <code>{row["bundle_path"].split(str(article_root)+"/",1)[-1]}</code><br><strong>Note:</strong> {row["note"]}</p>')
            html.append(f'<img src="{img_rel}" alt="{row["label"]}">')
            html.append('</div>')
        html.append('</div></div>')
    html.append('</body></html>')
    (out_root / 'figure_gallery.html').write_text(''.join(html))
    print('Built article asset review report successfully.')


if __name__ == '__main__':
    main()
