#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
from pathlib import Path

FILES = [
    'he2_bayesian_publication_manifest.md',
    'he2_bayesian_publication_manifest.csv',
    'he2_bayesian_publication_alignment.csv',
    'he2_bayesian_publication_inputs.csv',
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description='Refresh the local HE2 publication manifest snapshot.')
    parser.add_argument('--article-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--workflow-root', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()

    article_root = args.article_root.resolve()
    workflow_root = args.workflow_root.resolve()
    src_root = workflow_root / 'reports' / 'he2_publication_manifest'
    dst_root = article_root / 'generated' / 'he2_publication_manifest_snapshot'
    dst_root.mkdir(parents=True, exist_ok=True)

    rows = []
    sums = []
    for name in FILES:
        src = src_root / name
        dst = dst_root / name
        shutil.copy2(src, dst)
        digest = sha256(dst)
        sums.append(f'{digest}  {name}')
        rows.append([name, str(src), f'generated/he2_publication_manifest_snapshot/{name}', digest])

    (dst_root / 'README.md').write_text(
        '# HE2 Publication Manifest Snapshot\n\n'
        'This bundle freezes the current workflow-side HE2 publication manifest inside the revised article repo.\n\n'
        'Refresh script:\n'
        '- `scripts/refresh_he2_manifest_snapshot.py`\n\n'
        'Canonical workflow source:\n'
        f'- `{src_root}`\n'
    )
    with (dst_root / 'manifest.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['filename', 'source_absolute_path', 'local_snapshot_path', 'sha256'])
        writer.writerows(rows)
    (dst_root / 'SHA256SUMS.txt').write_text('\n'.join(sorted(sums)) + '\n')
    print('Refreshed HE2 publication manifest snapshot successfully.')


if __name__ == '__main__':
    main()
