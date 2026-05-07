# Workflow-Linked Support Figure Bundle

This bundle freezes the remaining figure assets in the revised article that are reproducible from the workflow repo, but were not previously frozen locally in article-side provenance bundles.

Included figures:
- `usgs.png`
- `precip_soilmoisture_climatePC1_faceted_labeled.png`
- `retrospective_log_discharge_plot_faceted.png`
- `forecats.png`
- `posterior_samples_counter_valid.png`

## Role in the article

These figures fall into two groups:
- setup/support figures used to orient the reader to the study setting and input products;
- one appendix historical-only reference synthesis figure (`posterior_samples_counter_valid.png`).

They are not all part of the narrow five-cutoff `exAL-M-T1` selected-model refresh. They remain workflow-linked support artifacts.

## Clean reproduction path

The clean current reproduction path is the run-scoped workflow path:
- generator logic: `R/environmetrics/40_figures.R`
- headless figure runner: `scripts/run_environmetrics_figures.R`
- workflow handoff: `R/unified/stages/stage_post.R`

In the current workflow, `stage_post.R` exports the needed environment variables for:
- retrospective inputs,
- forecast inputs,
- USGS daily truth,
- covariate CSVs,
- engineered `covariate_features.csv`.

That is the path that should be treated as the authoritative current reproduction contract.

## Legacy / weaker entrypoint

The older standalone script:
- `scripts/make_environmetrics_figures.R`

is **not** the preferred reproduction contract. It still relies on notebook-linearized state and legacy hard-coded external covariate paths such as:
- `/data/muscat_data/jaguir26/projects/Project/Input/exAL/covariates/cov_1_ELI.csv`
- `/data/muscat_data/jaguir26/projects/Project/Input/exAL/covariates/cov_2_ONI.csv`

It also assumes several root-level defaults that are no longer present in this repo. So it should be treated as historical scaffolding, not the clean reproduction path.

## Verification

The files in this bundle are article-side copies of the current `DISC/` assets and hash-match the workflow gold manifest recorded in:
- `repro/gold_DISC_figures.sha256`

Additional workflow references:
- `repro/REPRODUCE_PAPER.md`
- `repro/REPO_MAP.md`
- `repro/FORECATS_INPUTS_AND_WEIGHTING_PLAN.md`

## Why this bundle exists

This bundle closes the remaining article-side provenance gap by making the workflow-linked support figures locally frozen alongside:
- the five-cutoff `exAL-M-T1` CRPS source set,
- the representative `2022-12-25` selected-model bundle,
- the historical-summary support figure bundle,
- and the HE2 publication manifest snapshot.
