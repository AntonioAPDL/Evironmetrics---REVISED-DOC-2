# exAL-M-T1 Relaunch Checklist

## Purpose

This checklist fixes the exact source lineage for the selected manuscript model `exAL-M-T1` and records the replay contract needed to refresh interpretation-dependent outputs reproducibly.

Use this document when regenerating any Section 5 or appendix output that must remain consistent with the CRPS values reported in Table 1 of the manuscript.

Preferred execution rule:
- unless a replay fails because the preserved source-run fit artifacts are unusable, prefer a post-only replay from the authoritative source runs over a full refit;
- preserve the exact selected-model source lineage tied to the published CRPS values;
- and keep the replay outputs complete enough that figures, tables, and their supporting diagnostics can be rebuilt without another launch.

Current status from the replay audit:
- the authoritative source runs do not retain the fit-side `DISC_variables_*.RData` bundles needed by the current post exporter;
- so post-only replay is not sufficient for the selected `exAL-M-T1` lineage as it stands;
- the replay contract therefore needs to preserve those fit-side artifacts in a representative full-fit rerun before we scale to all five cutoffs.

Primary manuscript repo:
- `/data/muscat_data/jaguir26/project1_ucsc_phd/Evironmetrics---REVISED-DOC-2`

Primary implementation/workflow repo:
- `/data/muscat_data/jaguir26/project1_ucsc_phd`

Primary runtime root:
- `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime`

## Locked model mapping

Paper label to workflow/runtime label:
- `exAL-M-T1` -> `exdqlm_multivar_synth_keep`

Interpretation:
- `exAL` = extended asymmetric Laplace likelihood
- `M` = multivariate synthesis
- `T1` = transfer block kept active in the forecast window

This is the selected model used in Table 1 and the model that should anchor the remaining interpretation outputs unless Table 1 itself is later regenerated.

## Important audit conclusion

The published Table 1 is not a single homogeneous compare family for every multivariate row. In several cutoffs, the `keep` and `drop` multivariate rows come from different compare bundles.

Therefore:
- do not assume that one later relaunch family is automatically the source of the entire published table,
- do not anchor Section 5 figures or interpretation tables to an arbitrary recent `exdqlm_multivar_keep` run,
- and do not regenerate manuscript interpretation outputs until the selected source run for each cutoff is fixed explicitly.

For the selected model `exAL-M-T1`, the authoritative source runs are the ones listed below.

## Authoritative Table 1 source runs for exAL-M-T1

These are the exact runtime runs whose `exdqlm_multivar_synth_keep` CRPS values match the published `exAL-M-T1` row in the manuscript.

| Cutoff | Published Table 1 CRPS | Source run | Source compare bundle |
|---|---:|---|---|
| `2021-01-23` | `0.1294989214689244` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/runs/multimodel_20210123_v8_eps180cf1_l2_mv` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/reports/multimodel_20210123_v8_eps180cf1_compare` |
| `2021-11-12` | `0.0201373509141342` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/runs/multimodel_20211112_v8_epsTTcf1_l2_mv` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/reports/multimodel_20211112_v8_epsTTcf1_compare` |
| `2021-12-21` | `0.2830434692948816` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_histfix_20260407/runs/multimodel_20211221_v8_eps90_l2_mv` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_histfix_20260407/reports/multimodel_20211221_v8_eps90_compare` |
| `2022-05-11` | `0.0164959678591005` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_histfix_20260407/runs/multimodel_20220511_v8_epsTT_l2` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_histfix_20260407/reports/multimodel_20220511_v8_epsTT_compare` |
| `2022-12-25` | `0.5991104389071235` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/runs/multimodel_20221225_v8_eps90cf1_l2_mv` | `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/reports/multimodel_20221225_v8_eps90cf1_compare` |

## Important compatibility note

Several of the authoritative source runs above predate the newer deterministic-climate relaunch path in which:
- forecast precipitation is enabled after the cutoff,
- forecast soil moisture is enabled after the cutoff,
- and the large-scale climate factor remains in passthrough mode.

In the authoritative published source runs, the deterministic-climate block is still reported as disabled in the run summaries.

That means there are two different standards we could optimize for:
- exact agreement with the currently published Table 1 values, or
- strict agreement with the newer updated-input workflow.

This checklist is written for the first goal:
- preserve exact agreement with the current published Table 1 while refreshing Section 5 and appendix outputs.

If we later decide to prioritize the updated-input workflow instead, then Table 1 itself must be regenerated and this checklist should be revised accordingly.

## Section 5 representative cutoff

Locked choice for Section 5 and the main predictive-synthesis illustration:
- representative cutoff: `2022-12-25`
- authoritative run: `/data/muscat_data/jaguir26/project1_ucsc_phd_runtime/multimodel_v8_20260402/runs/multimodel_20221225_v8_eps90cf1_l2_mv`

Use this run for:
- `fig:synth1`
- `fig:synth2` if retained
- `tab:components_23_31`

unless Table 1 is later regenerated and the manuscript standard changes.

## Current artifact status of the authoritative source runs

For all five authoritative source runs, the following artifacts already exist:
- `publication_figure_manifest.csv`
- `publication_style_used.yaml`
- `figure_manifest.csv`
- `post_artifacts_manifest.csv`
- `post_artifacts_summary.json`
- `timestamps.csv`
- `timestamps_keep.csv`
- `data_cbind_tY_X.csv`
- `data_cbind_tY_X.rds`
- `data_cbind_tY_X_keep.csv`
- `data_cbind_tY_X_keep.rds`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_keep_cutoff_window_sample_subset.csv`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `posterior_table_exports_manifest.csv`

For all five authoritative source runs, the following posterior interpretation tables are currently missing:
- `covariate_effects_summary.csv`
- `gamma_summary.csv`
- `sigma_summary.csv`

So the figure refresh path already exists, but the interpretation-table export path still needs to be activated or repaired.

## Required artifacts after replay

Each replay of an authoritative source specification must preserve the following outputs.

### Required predictive-synthesis artifacts
- `figure_manifest.csv`
- `publication_figure_manifest.csv`
- `publication_style_used.yaml`
- `timestamps.csv`
- `timestamps_keep.csv`
- `data_cbind_tY_X.csv`
- `data_cbind_tY_X.rds`
- `data_cbind_tY_X_keep.csv`
- `data_cbind_tY_X_keep.rds`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_keep_cutoff_window_sample_subset.csv`
- `post/inputs/nws_post_adapter.csv`
- `post/inputs/glofas_post_adapter.csv`
- `post/inputs/retros_post_adapter.csv`

### Required optional/appendix synthesis artifacts
Keep these if `fig:synth2` or related appendix material remains in the paper:
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples_with_raw_ensembles.pdf`
- `exdqlm_multivar_synth_drop_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_drop_cutoff_window_sample_subset.csv`

### Required scoring and health tables
These are needed both for replay verification and for later auditability.

- `crps_forecast_summary.csv`
- `crps_forecast_per_time.csv`
- `crps_input_health.csv`
- `crps_input_health_per_time.csv`
- `crps_forecast_summary_keep.csv`
- `crps_forecast_per_time_keep.csv`
- `crps_input_health_keep.csv`
- `crps_input_health_per_time_keep.csv`

### Required posterior table exports
These are the key missing artifacts that the rerun must produce.

For each authoritative replay if possible, and at minimum for the representative cutoff run:
- `covariate_effects_summary.csv`
- `covariate_effects_summary.rds`
- `covariate_effects_summary.tex`
- `gamma_summary.csv`
- `gamma_summary.rds`
- `gamma_summary.tex`
- `sigma_summary.csv`
- `sigma_summary.rds`
- `sigma_summary.tex`
- `posterior_table_exports_manifest.csv`
- `posterior_table_exports_README.md`

### Required fit-side artifacts for reproducible post regeneration
These are the artifacts the post stage still expects when rebuilding the selected multivariate outputs.

For each quantile `q \in \{05,20,35,50,65,80,95\}`:
- legacy primary-mode drop artifact:
  - `fit/q=<q>/outputs/DISC_variables_<q_num>_exAL_synth_DISC.RData`
  - `fit/q=<q>/outputs/multivar_forecast_health.txt`
  - `fit/q=<q>/logs/fit.log`
- keep-mode artifact:
  - `fit/exdqlm_multivar/keep/q=<q>/outputs/DISC_variables_<q_num>_exAL_synth_DISC.RData`
  - `fit/exdqlm_multivar/keep/q=<q>/outputs/multivar_forecast_health.txt`
  - `fit/exdqlm_multivar/keep/q=<q>/logs/fit.log`

These fit-side artifacts are not optional for the current replay path. Their absence is what caused the authoritative post-only replay to fail.

### Required post artifact bookkeeping
- `post_artifacts_manifest.csv`
- `post_artifacts_summary.json`

### Required run-level audit artifacts
- `run_manifest.yaml`
- `resolved_config.yaml`
- `fit/logs/fit_stage.log`
- `fit/logs/shared_input_source_map.log`
- `report/summary.json`
- `report/summary.md`
- `validate/compare_report.json`
- `validate/compare_report.txt`
- `validate/current.sha256`
- `validate/canonical.sha256`
- environment snapshots under `env/`

### Heavy artifacts to retain
Do not trim these away if the replay can preserve them and storage is acceptable:
- posterior sample subsets already referenced by the publication figure manifest
- quantile-sidecar caches used by the publication figure renderer
- multivariate synthesis cache RDS files for both `keep` and `drop` modes
- run manifests and resolved configs
- validate outputs and report summaries
- post-stage manifests and summaries
- any run-scoped objects needed to rebuild figures or tables without another relaunch

## 2026-05-05 replay audit update

Current status after the first representative authoritative replay pass:
- the replay artifact contract was rechecked against the current manuscript needs and is complete for the selected-model refresh path;
- the representative cutoff `2022-12-25` full-fit replay is now environment-compatible and reaches the quantile-specific fit stage under the authoritative source lineage;
- however, the authoritative full-fit replay is not yet numerically stable across all quantiles, so the rerun is not yet ready to refresh manuscript figures or tables.

Representative full-fit replay used in this audit:
- config: `/data/muscat_data/jaguir26/project1_ucsc_phd/config/unified_runs_exalm_t1_postreplay_20260505/paper_exalm_t1_fullfit_20221225_20260505.yaml`
- run root: `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/runs/paper_exalm_t1_fullfit_20221225_20260505`

Resolved environment and replay-compatibility blockers:
- the legacy Rcpp kernels now compile with `cpp14` rather than `cpp11`;
- the replay path now loads `readr` explicitly where the legacy covariate loaders still used `read_csv()`;
- the replay path now combines `exdqlm` model components with the correct `+` method rather than relying on a missing legacy `combineMods()` helper;
- the post stage already prefers run-scoped shared inputs when present, which remains necessary for strict-source replays.

Current representative numerical-stability status:
- `q = 0.05` is progressing normally through the VB iterations;
- `q = 0.95` is also progressing normally;
- `q = 0.20` fails decisively with `FFF_list iter=19[[1]] contains non-finite values`;
- `q = 0.35`, `0.50`, `0.65`, and `0.80` show repeated `non-finite dq_transf` and `optim failure` events, followed by refreeze cycles.

Operational consequence:
- the representative authoritative full-fit replay does not yet complete the post, validate, and report stages;
- therefore the post-rerun CRPS verification contract below remains blocked;
- and no manuscript figures or interpretation tables should be refreshed from this replay until the numerical-stability issue is resolved.

## Exact relaunch checklist

### Phase 1. Prelaunch locking
- [ ] Confirm that Table 1 remains authoritative and is not being regenerated in the same pass.
- [ ] Confirm that Section 5 remains anchored to the representative cutoff `2022-12-25`.
- [ ] Confirm that the relaunch target is the selected model `exAL-M-T1` / `exdqlm_multivar_synth_keep`.
- [ ] Confirm that the five authoritative source runs above are the reference lineage for this pass.
- [ ] Record the exact runtime directories, compare bundles, and resolved configs before rerunning.

### Phase 2. Relaunch scope
- [ ] Prefer post-only replay from the five authoritative selected-model source runs rather than a full refit.
- [ ] Use `inputs.post.use_fit_outputs_from_run: true` and the exact authoritative `source_run_id`.
- [ ] Keep `data_prep_shared: true` so the replay writes the run-scoped shared-input bundle expected by the post stage.
- [ ] Set `inputs.shared.exact_source_snapshot_root` to the authoritative source run’s `inputs/shared/` tree so the replay inherits the same shared-input snapshot.
- [ ] Run with `post.smoke_fast: false`, `post.figures: true`, and `post.export_tables: true`.
- [ ] Preserve figures, tables, caches, and bookkeeping artifacts by launching with `CLEANUP_RDATA_AFTER_POST=0`.
- [ ] Keep `validate` and `report` enabled so each replay closes with its own audit trail.
- [ ] If post-only replay fails because the authoritative source run lacks the required fit-side `DISC_variables_*.RData` bundles, escalate to a full-fit replay from the frozen authoritative snapshot rather than substituting a newer lineage.

### Phase 3. Post-rerun CRPS verification
For each cutoff, verify that the rerun still reproduces the published selected-model CRPS exactly for `exdqlm_multivar_synth_keep`.

- [ ] `2021-01-23` -> `0.1294989214689244`
- [ ] `2021-11-12` -> `0.0201373509141342`
- [ ] `2021-12-21` -> `0.2830434692948816`
- [ ] `2022-05-11` -> `0.0164959678591005`
- [ ] `2022-12-25` -> `0.5991104389071235`

Verification rule:
- use the rerun compare output for `exdqlm_multivar_synth_keep`
- compare the stored `mean_crps` against the published value at full available precision
- do not accept a rerun as authoritative for manuscript refresh if this check fails

### Phase 4. Post-rerun artifact contract verification
For each authoritative rerun, verify:

- [ ] `figure_manifest.csv` exists
- [ ] `publication_figure_manifest.csv` exists
- [ ] `publication_style_used.yaml` exists
- [ ] `timestamps.csv` exists
- [ ] `timestamps_keep.csv` exists
- [ ] `data_cbind_tY_X.csv/.rds` exists
- [ ] `data_cbind_tY_X_keep.csv/.rds` exists
- [ ] keep posterior-synthesis PNG/PDF exists
- [ ] keep-with-raw-ensembles PNG/PDF exists
- [ ] keep quantile CSV exists
- [ ] keep sample-subset CSV exists
- [ ] keep/drop cache RDS files remain present under `post/cache`
- [ ] `post/inputs/nws_post_adapter.csv` exists
- [ ] `post/inputs/glofas_post_adapter.csv` exists
- [ ] `post/inputs/retros_post_adapter.csv` exists
- [ ] `crps_forecast_summary.csv` exists
- [ ] `crps_forecast_per_time.csv` exists
- [ ] `crps_input_health.csv` exists
- [ ] `crps_input_health_per_time.csv` exists
- [ ] `crps_forecast_summary_keep.csv` exists
- [ ] `crps_forecast_per_time_keep.csv` exists
- [ ] `crps_input_health_keep.csv` exists
- [ ] `crps_input_health_per_time_keep.csv` exists
- [ ] `posterior_table_exports_manifest.csv` exists
- [ ] `posterior_table_exports_README.md` exists
- [ ] `post_artifacts_manifest.csv` exists
- [ ] `post_artifacts_summary.json` exists
- [ ] fit-side `DISC_variables_*.RData` bundles exist for both the legacy drop layout and the keep layout
- [ ] fit-side `multivar_forecast_health.txt` files exist for both layouts
- [ ] `fit/logs/fit_stage.log` exists
- [ ] `report/summary.json` and `report/summary.md` exist
- [ ] `validate/compare_report.json` and `validate/compare_report.txt` exist

For the representative cutoff `2022-12-25`, verify additionally:
- [ ] `covariate_effects_summary.csv/.rds/.tex` exists
- [ ] `gamma_summary.csv/.rds/.tex` exists
- [ ] `sigma_summary.csv/.rds/.tex` exists
- [ ] the representative keep figure is the one intended for `fig:synth1`
- [ ] the representative drop figure is available if `fig:synth2` is retained

### Phase 5. Manuscript handoff checks
- [ ] Refresh `fig:synth1` from the rerun artifact tied to the representative cutoff source run.
- [ ] Refresh `fig:synth2` from the rerun artifact if the appendix figure is retained.
- [ ] Refresh `tab:components_23_31` from `covariate_effects_summary.csv` of the representative cutoff run.
- [ ] Decide whether `gamma` and `sigma` appendix tables remain historical summaries or move to representative-cutoff exports.
- [ ] Update captions and nearby text so the role of each refreshed object is explicit.

## Recommended operating rule

Until Table 1 itself is intentionally regenerated, the safest standard is:
- figures and interpretation tables should be regenerated from the exact selected-model source specifications associated with the published CRPS values,
- not from a later relaunch family that happens to be close,
- and not from workflow-canonical assets whose lineage is less specific than the published table.

That rule keeps the manuscript internally coherent and makes the provenance story defensible.
