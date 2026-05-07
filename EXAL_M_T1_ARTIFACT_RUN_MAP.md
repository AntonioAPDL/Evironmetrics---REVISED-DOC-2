# exAL-M-T1 Artifact-to-Run Map

Date: 2026-05-06

## Purpose

This file locks the reproducible `exAL-M-T1` source set used by the revised article and maps each manuscript object to its exact verified run/output source.

It is the execution companion to:
- `EXAL_M_T1_RELAUNCH_CHECKLIST.md`
- `FIGURE_TABLE_PROVENANCE.md`

## 1. Locked reproducible source set

The revised article now carries a minimal local freeze of the five verified publication `exAL-M-T1` runs under:

- `generated/exal_m_t1_five_run_sources/`

For each cutoff, that local freeze includes:
- `crps_forecast_summary.csv`
- `compare_report.json`
- `summary.json`

These local copies are derived from the verified workflow replay roots and should be treated as the article-side provenance anchor for the five-cutoff `exAL-M-T1` CRPS lineage.

## 2. Verified five-run publication lineage

| Cutoff | Local frozen copy | Canonical run root | Canonical CRPS source | Status |
|---|---|---|---|---|
| `2021-01-23` | `generated/exal_m_t1_five_run_sources/20210123_exal_m_t1/` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_publication_replay_representatives_20260506/20210123_exal_m_t1/runs/multimodel_20210123_v8_eps360cf1_exdqlm_multivar_keep_featurecov_cf1` | `post/outputs/.../tables/crps_forecast_summary.csv` | `PASS` |
| `2021-11-12` | `generated/exal_m_t1_five_run_sources/20211112_exal_m_t1/` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_publication_replay_representatives_20260506/20211112_exal_m_t1/runs/multimodel_20211112_v8_eps180cf1_exdqlm_multivar_keep_featurecov_cf1` | `post/outputs/.../tables/crps_forecast_summary.csv` | `PASS` |
| `2021-12-21` | `generated/exal_m_t1_five_run_sources/20211221_exal_m_t1/` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_publication_replay_representatives_20260506/20211221_exal_m_t1/runs/multimodel_20211221_v8_eps1cf1_exdqlm_multivar_keep_featurecov_cf1` | `post/outputs/.../tables/crps_forecast_summary.csv` | `PASS` |
| `2022-05-11` | `generated/exal_m_t1_five_run_sources/20220511_exal_m_t1/` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_publication_replay_representatives_20260506/20220511_exal_m_t1/runs/multimodel_20220511_v8_eps180cf1_exdqlm_multivar_keep_featurecov_cf1` | `post/outputs/.../tables/crps_forecast_summary.csv` | `PASS` |
| `2022-12-25` | `generated/exal_m_t1_five_run_sources/20221225_exal_m_t1/` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_publication_replay_representatives_20260506/20221225_exal_m_t1/runs/multimodel_20221225_v8_exalm_t1_discount_grid_exact_v1_set09_exdqlm_multivar_keep` | `post/outputs/.../tables/crps_forecast_summary.csv` | `PASS` |

## 3. Representative selected-model bundle

The representative Section 5 cutoff is `2022-12-25`.

The revised article now carries a richer local copy of the verified representative output bundle under:

- `generated/exal_m_t1_20221225/`

That bundle now includes:
- selected synthesis figures:
  - `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.(png,pdf)`
  - `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.(png,pdf)`
- synthesis exports:
  - `exdqlm_multivar_synth_keep_cutoff_window_quantiles.csv`
  - `exdqlm_multivar_synth_keep_cutoff_window_sample_subset.csv`
- figure provenance:
  - `figure_manifest.csv`
  - `publication_figure_manifest.csv`
  - `publication_style_used.yaml`
- posterior tables:
  - `covariate_effects_summary.csv/.tex`
  - `gamma_summary.csv/.tex`
  - `sigma_summary.csv/.tex`
  - `posterior_table_exports_manifest.csv`
- CRPS summaries:
  - `crps_forecast_summary.csv`
  - `crps_forecast_per_time.csv`

## 4. Manuscript artifact map

### In-scope objects now locked to the verified five-run/representative source set

| Manuscript object | Current role | Locked cutoff/run | Exact verified source | Current manuscript target | Current status |
|---|---|---|---|---|---|
| `tab:benchmark_crps_models` | five-cutoff validation table | HE2 publication freeze across all five cutoffs | local snapshot in `generated/he2_publication_manifest_snapshot/`, with the `exAL-M-T1` row additionally locked to `generated/exal_m_t1_five_run_sources/<slug>/crps_forecast_summary.csv` | values in `wileyNJD-APA.tex` Table 1 | locked |
| `fig:synth1` | representative selected-model illustration | `2022-12-25 exAL-M-T1 keep` | `generated/exal_m_t1_20221225/exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.png` | `DISC/posterior_samples_valid.png` | refreshed |
| `tab:components_23_31` | representative transfer-function summary | `2022-12-25 exAL-M-T1 keep` | `generated/exal_m_t1_20221225/covariate_effects_summary.csv` | values in `wileyNJD-APA.tex` | refreshed |

### Supplementary appendix support tied to the representative selected-model run

| Manuscript object | Current role | Locked cutoff/run | Exact verified source | Current manuscript target | Current status |
|---|---|---|---|---|---|
| `tab:gamma_sigma_intervals1` | supplementary appendix `gamma` summary | `2022-12-25 exAL-M-T1 keep` | `generated/exal_m_t1_20221225/gamma_summary.csv` | values in `wileyNJD-APA.tex` | refreshed |
| `tab:gamma_sigma_intervals2` | supplementary appendix `sigma` summary | `2022-12-25 exAL-M-T1 keep` | `generated/exal_m_t1_20221225/sigma_summary.csv` | values in `wileyNJD-APA.tex` | refreshed |

### Workflow-linked but outside the locked five-run keep source set

These objects are still reproducible workflow assets, but they are not part of the narrow locked `exAL-M-T1` keep-run source set above.

| Manuscript object | Current role | Current source status | Action |
|---|---|---|---|
| `fig:synth2` | appendix historical-only reference | not sourced from the locked five-run keep lineage; current `DISC/posterior_samples_counter_valid.png` remains a workflow-linked counterfactual artifact outside this narrowed keep-run freeze | defer or regenerate from a separately locked counterfactual workflow if retained |
| `fig:dry_quantile` | historical regime illustration | workflow-linked historical figure, hash-matched to the current workflow gold record and frozen locally in `generated/historical_summary_sources/`; not a five-run cutoff artifact | keep as historical-summary object |
| `fig:rainy_quantile` | historical regime illustration | workflow-linked historical figure, hash-matched to the current workflow gold record and frozen locally in `generated/historical_summary_sources/`; not a five-run cutoff artifact | keep as historical-summary object |
| `fig:80_components` | appendix long-cycle historical summary | workflow-linked historical figure, hash-matched to the current workflow gold record and frozen locally in `generated/historical_summary_sources/`; not a five-run cutoff artifact | keep as historical-summary object |

### Setup figures outside the selected-model refresh scope

| Manuscript object | Role | Action |
|---|---|---|
| `fig:sanlorenzo` | study-setting figure | keep |
| `fig:covariates` | data/covariate setup figure | keep |
| `fig:retrospectives` | retrospective-product setup figure | keep |
| `fig:ensembles` | forecast-product setup figure | keep |

## 5. What this means operationally

1. The five verified `exAL-M-T1` keep runs are now the locked reproducible source set for the main selected-model manuscript evidence.
2. Any further refresh of the central selected-model objects `fig:synth1` and `tab:components_23_31` should use only the files recorded above.
3. The appendix support tables `tab:gamma_sigma_intervals1` and `tab:gamma_sigma_intervals2` should remain supplementary and should continue to use the representative `2022-12-25` source files recorded above.
4. `fig:synth2` and the historical-summary figures should not be silently treated as part of that five-run keep lineage. If they remain in the paper, they should either:
   - stay explicitly labeled as separate workflow-linked historical/counterfactual objects, or
   - be regenerated from a separately locked source path.

## 6. Locked choice for the current manuscript pass

For the current revised article pass, the chosen approach is:

1. keep `fig:dry_quantile`, `fig:rainy_quantile`, and `fig:80_components`
2. treat them explicitly as workflow-linked historical summaries
3. do not treat them as additional five-cutoff forecast-validation evidence
4. do not force them into the representative `2022-12-25` selected-run bundle
5. preserve their article-side provenance bundle in `generated/historical_summary_sources/`

This is the strongest minimal choice because it preserves reproducibility, avoids mixing incompatible provenance roles, and does not require unnecessary reruns.
