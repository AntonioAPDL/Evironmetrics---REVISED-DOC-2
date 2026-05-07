# Historical Summary Figure Provenance Bundle

This bundle freezes the workflow-linked historical-summary figures retained in the revised article as descriptive appendix/supporting material.

Refresh script:
- `scripts/refresh_local_provenance_bundles.py`

Role in the manuscript:
- historical summaries of the fitted specification
- not part of the narrow five-cutoff `exAL-M-T1` keep-run validation lineage
- not representative-cutoff outputs
- not additional rolling-origin validation evidence

Workflow-side evidence:
- gold hash manifest:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/gold_DISC_figures.sha256`
- repository map:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/REPO_MAP.md`
- reproduction guide:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/REPRODUCE_PAPER.md`
- historical figure-generation script:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/R/environmetrics/40_figures.R`

Verification status:
- the copied PNGs in `figures/` hash-match the workflow gold manifest exactly
- the hashes are recorded in `SHA256SUMS.txt`
- the per-figure source map is recorded in `manifest.csv`

This bundle is intentionally frozen rather than rerun during the narrow `exAL-M-T1` replay cycle.
