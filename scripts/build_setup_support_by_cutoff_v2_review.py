#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path

import yaml


def main() -> None:
    parser = argparse.ArgumentParser(description='Build an article-side review report for setup/support figures by cutoff (v2).')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    article_root = args.article_root.resolve()
    bundle_root = article_root / 'generated' / 'setup_support_by_cutoff_v2'
    if not bundle_root.exists():
        raise FileNotFoundError(f'Missing article-side setup/support v2 bundle: {bundle_root}')

    out_root = article_root / 'generated' / 'setup_support_by_cutoff_v2_review'
    out_root.mkdir(parents=True, exist_ok=True)

    cutoffs = sorted([p for p in bundle_root.iterdir() if p.is_dir() and p.name[:8].isdigit()])
    records = []
    for cutoff_dir in cutoffs:
        meta = json.loads((cutoff_dir / 'metadata' / 'cutoff_entry.json').read_text())
        support = yaml.safe_load((cutoff_dir / 'metadata' / 'support_window.yaml').read_text())
        policy = yaml.safe_load((cutoff_dir / 'metadata' / 'policy_summary.yaml').read_text())
        coverage = yaml.safe_load((cutoff_dir / 'metadata' / 'coverage_audit.yaml').read_text())
        rows = list(csv.DictReader((cutoff_dir / 'review' / 'figure_manifest.csv').open()))
        records.append((cutoff_dir, meta, support, policy, coverage, rows))

    with (out_root / 'figure_manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['cutoff_dir', 'cutoff_date', 'published_crps', 'bundle_class', 'support_start', 'support_end', 'retrospective_available_start', 'retrospective_full_history_available', 'plot_start', 'plot_end', 'forecast_start_date', 'figure_name', 'article_bundle_path', 'sha256', 'bytes'])
        for cutoff_dir, meta, support, _policy, coverage, rows in records:
            for row in rows:
                writer.writerow([
                    cutoff_dir.name,
                    meta['cutoff_date'],
                    meta['published_crps'],
                    meta['bundle_class'],
                    support['support_start'],
                    support['support_end'],
                    support['retrospective_available_start'],
                    coverage['retrospective']['full_history_available'],
                    support['plot_start'],
                    support['plot_end'],
                    support['forecast_start_date'],
                    row['figure_name'],
                    str((cutoff_dir / 'figures' / row['figure_name']).relative_to(article_root)),
                    row['sha256'],
                    row['bytes'],
                ])

    md = [
        '# Setup/Support Figures by Cutoff v2 Review\n\n',
        'This review bundle mirrors the corrected cutoff-specific setup/input/support figures derived from the validated exAL-M-T1 v2 runtime family.\n\n',
        '## Cutoff summary\n',
        '| Cutoff | Directory | Bundle class | Requested history | Retrospective available from | Forecast window | Published CRPS |\n',
        '|---|---|---|---|---|---|---:|\n',
    ]
    for cutoff_dir, meta, support, policy, coverage, _rows in records:
        md.append(f"| {meta['cutoff_date']} | `{cutoff_dir.name}` | `{meta['bundle_class']}` | {support['support_start']} to {support['support_end']} | {support['retrospective_available_start']} | {support['plot_start']} to {support['plot_end']} | {meta['published_crps']} |\n")
    md.append('\n## Policy summary\n')
    md.append('| Cutoff | NWS policy | GloFAS policy | Notes |\n')
    md.append('|---|---|---|---|\n')
    for cutoff_dir, meta, support, policy, coverage, _rows in records:
        md.append(f"| {meta['cutoff_date']} | {policy['nws_policy_summary']} | {policy['glofas_policy_summary']} | {policy.get('notes','')} |\n")
    md.append('\n## Coverage audit\n')
    md.append('| Cutoff | USGS full history | PPT full history | SOIL full history | PCA full history | Retros full history | Retros available start |\n')
    md.append('|---|---|---|---|---|---|---|\n')
    for cutoff_dir, meta, support, policy, coverage, _rows in records:
        md.append(
            f"| {meta['cutoff_date']} | {coverage['usgs']['full_history_available']} | {coverage['ppt']['full_history_available']} | "
            f"{coverage['soil']['full_history_available']} | {coverage['pca']['full_history_available']} | "
            f"{coverage['retrospective']['full_history_available']} | {coverage['retrospective']['available_start']} |\n"
        )
    (out_root / 'SETUP_SUPPORT_BY_CUTOFF_V2_REVIEW.md').write_text(''.join(md))

    html = [
        '<!doctype html><html><head><meta charset="utf-8"><title>Setup/Support Figures by Cutoff v2</title>',
        '<style>body{font-family:Arial,sans-serif;margin:24px;} .cutoff{margin-top:36px;} .grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;} .card{border:1px solid #ddd;padding:12px;border-radius:8px;background:#fff;} img{max-width:100%;height:auto;border:1px solid #eee;} .meta{font-size:13px;color:#333;line-height:1.4;} code{background:#f4f4f4;padding:2px 4px;border-radius:4px;}</style></head><body>',
        '<h1>Setup/Support Figures by Cutoff v2</h1>',
        '<p>These figures are generated from the validated exAL-M-T1 v2 cutoff-specific setup/support workflow and mirrored into the revised-article repo for review.</p>'
    ]
    for cutoff_dir, meta, support, policy, coverage, rows in records:
        html.append(f'<div class="cutoff"><h2>{meta["cutoff_date"]}</h2>')
        html.append(f'<p class="meta"><strong>Directory:</strong> <code>{cutoff_dir.name}</code><br><strong>Bundle class:</strong> <code>{meta["bundle_class"]}</code><br><strong>Requested history:</strong> {support["support_start"]} to {support["support_end"]}<br><strong>Retrospective available from:</strong> {support["retrospective_available_start"]}<br><strong>Forecast window:</strong> {support["plot_start"]} to {support["plot_end"]}<br><strong>NWS policy:</strong> {policy["nws_policy_summary"]}<br><strong>GloFAS policy:</strong> {policy["glofas_policy_summary"]}<br><strong>Coverage audit:</strong> USGS={coverage["usgs"]["full_history_available"]}, PPT={coverage["ppt"]["full_history_available"]}, SOIL={coverage["soil"]["full_history_available"]}, PCA={coverage["pca"]["full_history_available"]}, Retros={coverage["retrospective"]["full_history_available"]}</p>')
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
    print('Built setup/support-by-cutoff v2 review successfully.')


if __name__ == '__main__':
    main()
