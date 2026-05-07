#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

FIGURE_NAMES = [
    'usgs.png',
    'precip_soilmoisture_climatePC1_faceted_labeled.png',
    'retrospective_log_discharge_plot_faceted.png',
    'forecats.png',
]


def main() -> None:
    parser = argparse.ArgumentParser(description='Promote one validated setup/support-by-cutoff v2 bundle into DISC/.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--slug', default='20221225_exal_m_t1')
    args = parser.parse_args()

    article_root = args.article_root.resolve()
    bundle_root = article_root / 'generated' / 'setup_support_by_cutoff_v2' / args.slug
    figures_root = bundle_root / 'figures'
    if not figures_root.exists():
        raise FileNotFoundError(f'Missing setup/support v2 figure bundle: {figures_root}')

    disc_root = article_root / 'DISC'
    disc_root.mkdir(parents=True, exist_ok=True)
    for name in FIGURE_NAMES:
        shutil.copy2(figures_root / name, disc_root / name)

    selection_root = article_root / 'generated' / 'setup_support_by_cutoff_v2_article_selection'
    selection_root.mkdir(parents=True, exist_ok=True)
    meta = json.loads((bundle_root / 'metadata' / 'cutoff_entry.json').read_text())
    selection = {
        'selected_slug': args.slug,
        'selected_cutoff_date': meta['cutoff_date'],
        'selected_run_root': meta['selected_run_root'],
        'selected_figure_bundle_root': meta['figure_bundle_root'],
        'bundle_class': meta['bundle_class'],
        'figures': FIGURE_NAMES,
    }
    (selection_root / 'selection_manifest.json').write_text(json.dumps(selection, indent=2) + '\n')
    print(f'Promoted {args.slug} setup/support v2 figures into {disc_root}')


if __name__ == '__main__':
    main()
