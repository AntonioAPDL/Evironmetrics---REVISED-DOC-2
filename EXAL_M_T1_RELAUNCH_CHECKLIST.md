# exAL-M-T1 Relaunch Checklist

## Purpose

This checklist fixes the exact source lineage for the selected manuscript model `exAL-M-T1` and records the relaunch contract needed to refresh interpretation-dependent outputs reproducibly.

Use this document when regenerating any Section 5 or appendix output that must remain consistent with the CRPS values reported in Table 1 of the manuscript.

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
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_keep_cutoff_window_sample_subset.csv`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.png`
- `posterior_table_exports_manifest.csv`

For all five authoritative source runs, the following posterior interpretation tables are currently missing:
- `covariate_effects_summary.csv`
- `gamma_summary.csv`
- `sigma_summary.csv`

So the figure refresh path already exists, but the interpretation-table export path still needs to be activated or repaired.

## Required artifacts after relaunch

Each relaunch of an authoritative source specification must preserve the following outputs.

### Required predictive-synthesis artifacts
- `publication_figure_manifest.csv`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.png`
- `exdqlm_multivar_synth_keep_cutoff_window_posterior_samples_with_raw_ensembles.pdf`
- `exdqlm_multivar_synth_keep_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_keep_cutoff_window_sample_subset.csv`

### Required optional/appendix synthesis artifacts
Keep these if `fig:synth2` or related appendix material remains in the paper:
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.png`
- `exdqlm_multivar_synth_drop_cutoff_window_posterior_samples.pdf`
- `exdqlm_multivar_synth_drop_cutoff_window_quantiles.csv`
- `exdqlm_multivar_synth_drop_cutoff_window_sample_subset.csv`

### Required posterior table exports
These are the key missing artifacts that the rerun must produce.

For the representative cutoff run at minimum:
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

### Heavy artifacts to retain
Do not trim these away if the relaunch can preserve them and storage is acceptable:
- posterior sample subsets already referenced by the publication figure manifest
- run manifests and resolved configs
- post-stage manifests and summaries
- any run-scoped objects needed to rebuild figures or tables without another relaunch

## Exact relaunch checklist

### Phase 1. Prelaunch locking
- [ ] Confirm that Table 1 remains authoritative and is not being regenerated in the same pass.
- [ ] Confirm that Section 5 remains anchored to the representative cutoff `2022-12-25`.
- [ ] Confirm that the relaunch target is the selected model `exAL-M-T1` / `exdqlm_multivar_synth_keep`.
- [ ] Confirm that the five authoritative source runs above are the reference lineage for this pass.
- [ ] Record the exact runtime directories, compare bundles, and resolved configs before rerunning.

### Phase 2. Relaunch scope
- [ ] Relaunch the five authoritative selected-model source specifications, or relaunch an equivalent workflow path that preserves the same selected specification for each cutoff.
- [ ] Ensure the relaunch preserves publication figure outputs.
- [ ] Ensure the relaunch writes posterior interpretation tables, not only CRPS tables.
- [ ] Ensure the relaunch keeps heavy artifacts rather than pruning them.

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

- [ ] `publication_figure_manifest.csv` exists
- [ ] keep posterior-synthesis PNG/PDF exists
- [ ] keep-with-raw-ensembles PNG/PDF exists
- [ ] keep quantile CSV exists
- [ ] keep sample-subset CSV exists
- [ ] `posterior_table_exports_manifest.csv` exists
- [ ] `posterior_table_exports_README.md` exists

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
