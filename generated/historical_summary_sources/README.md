# Historical Summary Figure Provenance Bundle

This bundle freezes the three workflow-linked historical-summary figures retained in the revised article as descriptive appendix/supporting material.

These figures are:
- `fig:dry_quantile` -> `figures/All_exal_2012-2016_DISC.png`
- `fig:rainy_quantile` -> `figures/All_exal_2017-2019_DISC.png`
- `fig:80_components` -> `figures/80_component_1991_2022.png`

Role in the manuscript:
- historical summaries of the fitted specification
- not part of the narrow five-cutoff `exAL-M-T1` keep-run validation lineage
- not representative-cutoff outputs
- not additional rolling-origin validation evidence

Why this bundle exists:
- to keep the revised article repo reproducible without reopening a new rerun cycle for these figures
- to preserve a local copy of the exact PNGs used by the manuscript
- to record the workflow-side evidence linking these files to the historical figure-generation path

Workflow-side evidence:
- gold hash manifest:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/gold_DISC_figures.sha256`
- repository map:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/REPO_MAP.md`
- reproduction guide:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/REPRODUCE_PAPER.md`
- historical figure-generation script:
  - `/data/muscat_data/jaguir26/project1_ucsc_phd/R/environmetrics/40_figures.R`

Relevant source references:
- `REPO_MAP.md:81-83`
- `REPRODUCE_PAPER.md:93-95`
- `REPRODUCE_PAPER.md:110-112`
- `40_figures.R:7331` for `All_exal_2017-2019_DISC.png`
- `40_figures.R:7493` for `All_exal_2012-2016_DISC.png`
- `40_figures.R:7869` for `80_component_1991_2022.png`

Verification status:
- the copied PNGs in `figures/` hash-match the workflow gold manifest exactly
- the hashes are recorded in `SHA256SUMS.txt`
- the per-figure source map is recorded in `manifest.csv`

This bundle was intentionally frozen rather than regenerated during the narrow `exAL-M-T1` replay cycle.
