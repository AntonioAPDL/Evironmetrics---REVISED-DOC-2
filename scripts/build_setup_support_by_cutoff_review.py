#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

FIGURE_NAMES = [
    'usgs.png',
    'precip_soilmoisture_climatePC1_faceted_labeled.png',
    'retrospective_log_discharge_plot_faceted.png',
    'forecats.png',
]


def main() -> None:
    parser = argparse.ArgumentParser(description='Build an article-side review report for setup/support figures by cutoff.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    article_root = args.article_root.resolve()
    bundle_root = article_root / 'generated' / 'setup_support_by_cutoff'
    if not bundle_root.exists():
        raise FileNotFoundError(f'Missing article-side setup/support bundle: {bundle_root}')

    out_root = article_root / 'generated' / 'setup_support_by_cutoff_review'
    out_root.mkdir(parents=True, exist_ok=True)

    cutoffs = sorted([p for p in bundle_root.iterdir() if p.is_dir() and p.name[:8].isdigit()])
    records = []
    for cutoff_dir in cutoffs:
        meta_path = cutoff_dir / 'inputs' / 'cutoff_metadata.json'
        review_manifest = cutoff_dir / 'review' / 'figure_manifest.csv'
        meta = __import__('json').loads(meta_path.read_text())
        with review_manifest.open() as f:
            rows = list(csv.DictReader(f))
        records.append((cutoff_dir, meta, rows))

    with (out_root / 'figure_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['cutoff_dir', 'cutoff_date', 'run_id', 'figure_name', 'article_bundle_path', 'sha256', 'bytes'])
        for cutoff_dir, meta, rows in records:
            for row in rows:
                writer.writerow([
                    cutoff_dir.name,
                    meta['cutoff_date'],
                    meta['run_id'],
                    row['figure_name'],
                    str((cutoff_dir / 'figures' / row['figure_name']).relative_to(article_root)),
                    row['sha256'],
                    row['bytes'],
                ])

    md = [
        '# Setup/Support Figures by Cutoff Review\n\n',
        'This review bundle mirrors the cutoff-specific setup/input/support figures derived from the verified exAL-M-T1 run bundles.\n\n',
        '## Cutoff summary\n',
        '| Cutoff | Directory | Run ID | Plot window | Forecast starts |\n',
        '|---|---|---|---|---|\n',
    ]
    for cutoff_dir, meta, _rows in records:
        md.append(f"| {meta['cutoff_date']} | `{cutoff_dir.name}` | `{meta['run_id']}` | {meta['plot_start']} to {meta['plot_end']} | {meta['forecast_start_date']} |\n")
    md.append('\n')
    md.append('## Review paths\n')
    md.append('- `generated/setup_support_by_cutoff/`\n')
    md.append('- `generated/setup_support_by_cutoff_review/gallery.html`\n')
    md.append('- `generated/setup_support_by_cutoff_review/figure_manifest.csv`\n')
    (out_root / 'SETUP_SUPPORT_BY_CUTOFF_REVIEW.md').write_text(''.join(md))

    html = [
        '<!doctype html><html><head><meta charset="utf-8"><title>Setup/Support Figures by Cutoff</title>',
        '<style>body{font-family:Arial,sans-serif;margin:24px;} .cutoff{margin-top:36px;} .grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;} .card{border:1px solid #ddd;padding:12px;border-radius:8px;background:#fff;} img{max-width:100%;height:auto;border:1px solid #eee;} .meta{font-size:13px;color:#333;line-height:1.4;} code{background:#f4f4f4;padding:2px 4px;border-radius:4px;}</style></head><body>',
        '<h1>Setup/Support Figures by Cutoff</h1>',
        '<p>These figures are generated from the verified exAL-M-T1 run-scoped input bundles and mirrored into the revised-article repo for review.</p>'
    ]
    for cutoff_dir, meta, rows in records:
        html.append(f'<div class="cutoff"><h2>{meta["cutoff_date"]}</h2>')
        html.append(f'<p class="meta"><strong>Directory:</strong> <code>{cutoff_dir.name}</code><br><strong>Run ID:</strong> <code>{meta["run_id"]}</code><br><strong>Plot window:</strong> {meta["plot_start"]} to {meta["plot_end"]}<br><strong>Forecast starts:</strong> {meta["forecast_start_date"]}</p>')
        html.append('<div class="grid">')
        for row in rows:
            rel = Path(os.path.relpath(cutoff_dir / 'figures' / row['figure_name'], out_root))
            html.append('<div class="card">')
            html.append(f'<h3>{row["figure_name"]}</h3>')
            html.append(f'<p class="meta"><strong>SHA256:</strong> <code>{row["sha256"][:16]}...</code><br><strong>Bytes:</strong> {row["bytes"]}</p>')
            html.append(f'<img src="{rel.as_posix()}" alt="{row["figure_name"]}">')
            html.append('</div>')
        html.append('</div></div>')
    html.append('</body></html>')
    (out_root / 'gallery.html').write_text(''.join(html))
    print('Built setup/support-by-cutoff review successfully.')


if __name__ == '__main__':
    main()
