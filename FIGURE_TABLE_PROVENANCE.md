# Figure and Table Provenance Inventory

## Scope

This document records the current provenance status of manuscript figures and interpretation-dependent tables for the revised Environmetrics article.

Primary manuscript repo:
- `/data/muscat_data/jaguir26/project1_ucsc_phd/Evironmetrics---REVISED-DOC-2`

Primary workflow repo currently linked to figure/table generation:
- `/data/muscat_data/jaguir26/project1_ucsc_phd_v8_launch_471fcfd`

Main purpose:
- identify which manuscript outputs are already traceable to the current workflow,
- distinguish reproducible workflow-linked outputs from legacy or ambiguous outputs,
- and define the next regeneration tasks needed to align all interpretation material with the final selected `exAL-M-T1` analysis behind Table 1.

This inventory does **not** yet certify that every interpretation-dependent object comes from the final selected run used for the published five-cutoff CRPS table. It establishes provenance first, so regeneration and manuscript updates can be done safely.

## Overall conclusion

The manuscript repo is **not self-contained** for figure/table generation. It contains the article source and static assets, but not the full workflow required to regenerate them. However, the workflow repo above contains direct figure-generation code, reproducibility documentation, and posterior-table export infrastructure.

Most important result from this audit:
- every figure file currently used by the manuscript and checked below matches the workflow repo's recorded gold hash exactly.

That means the current manuscript figures are strongly linked to the current workflow repo, even though the manuscript repo itself does not yet carry the generation scripts.

Table provenance is weaker but still promising:
- the workflow repo contains a formal post-stage table-export contract,
- helper code for `gamma`, `sigma`, and covariate-effect summaries,
- and tests that encode the expected table schema and representative values.

The remaining work is to tie the interpretation tables and cutoff-specific interpretation figures to the exact final selected `exAL-M-T1` run used for the current Table 1 CRPS values.

## Current workflow evidence

### Figure-generation evidence

The workflow repo contains the following direct figure-generation references:
- `R/environmetrics/40_figures.R`
- `scripts/make_environmetrics_figures.R`
- `Environmetrics_Figures.ipynb`
- `repro/extracted/Environmetrics_Figures__RECOVERED_WORKING.r`
- `repro/REPO_MAP.md`
- `repro/REPRODUCE_PAPER.md`
- `repro/gold_DISC_figures.sha256`

### Posterior-table export evidence

The workflow repo contains the following table-export infrastructure:
- `R/environmetrics/02_helpers_core.R`
- `R/unified/stages/stage_post.R`
- `R/unified/post_artifact_contract.R`
- `repro/UNIFIED_WORKFLOW_README.md`
- `tests/testthat/test_post_posterior_table_exports.R`

The documented post-stage outputs are:
- `gamma_summary.csv`
- `sigma_summary.csv`
- `covariate_effects_summary.csv`
- optional `.tex` snippets for the same summaries
- `posterior_table_exports_README.md`
- `posterior_table_exports_manifest.csv`

## Figure provenance map

### High-confidence, workflow-linked figures already matching the recorded gold outputs

The following manuscript figure assets in `Evironmetrics---REVISED-DOC-2/DISC/` were hashed locally and match the workflow repo's `repro/gold_DISC_figures.sha256` exactly.

| Manuscript label | Current asset | Current manuscript role | Workflow evidence | Hash match | Repro status | Selected-run status | Recommended action |
|---|---|---|---|---|---|---|---|
| `fig:sanlorenzo` | `DISC/usgs.png` | study-setting figure | `REPO_MAP.md`, `REPRODUCE_PAPER.md`, `40_figures.R`, notebook | yes | reproducible from workflow repo | not selected-run dependent | keep |
| `fig:covariates` | `DISC/precip_soilmoisture_climatePC1_faceted_labeled.png` | covariate setup figure | same as above | yes | reproducible from workflow repo | not selected-run dependent | keep |
| `fig:retrospectives` | `DISC/retrospective_log_discharge_plot_faceted.png` | retrospective-product setup figure | notebook + `40_figures.R`; source path still slightly less explicit in docs | yes | reproducible from workflow repo with minor documentation gap | not selected-run dependent | keep, but preserve source note |
| `fig:ensembles` | `DISC/forecats.png` | forecast-product setup figure | notebook, `40_figures.R`, dedicated `FORECATS_INPUTS_AND_WEIGHTING_PLAN.md` | yes | reproducible from workflow repo, but with extra workflow complexity | not selected-run dependent | keep, but treat as a sensitive workflow artifact |
| `fig:dry_quantile` | `DISC/All_exal_2012-2016_DISC.png` | historical regime illustration | `REPO_MAP.md`, `REPRODUCE_PAPER.md`, `40_figures.R`, notebook | yes | reproducible from workflow repo | selected-run consistency still needs decision | provenance decision, then keep or regenerate |
| `fig:rainy_quantile` | `DISC/All_exal_2017-2019_DISC.png` | historical regime illustration | same as above | yes | reproducible from workflow repo | selected-run consistency still needs decision | provenance decision, then keep or regenerate |
| `fig:synth1` | `DISC/posterior_samples_valid.png` | predictive synthesis illustration | `REPO_MAP.md`, `REPRODUCE_PAPER.md`, `40_figures.R`, notebook | yes | reproducible from workflow repo | must match final selected run | regenerate from final selected run |
| `fig:80_components` | `DISC/80_component_1991_2022.png` | appendix long-cycle seasonal illustration | `REPO_MAP.md`, `REPRODUCE_PAPER.md`, `40_figures.R`, notebook | yes | reproducible from workflow repo | selected-run consistency still needs decision | provenance decision, then keep or regenerate |
| `fig:synth2` | `DISC/posterior_samples_counter_valid.png` | appendix historical-only predictive synthesis | `REPO_MAP.md`, `REPRODUCE_PAPER.md`, `40_figures.R`, notebook | yes | reproducible from workflow repo | must match final selected run if retained | regenerate from final selected run if retained |

### Notes on figure confidence

1. `forecats.png` is reproducible, but its workflow is more delicate than the other setup figures.
   - The workflow repo includes a dedicated reproducibility plan at:
     - `repro/FORECATS_INPUTS_AND_WEIGHTING_PLAN.md`
   - That document records both the current generation path and known sensitivity around weighted/legacy inputs.

2. The dry/wet regime figures and the appendix long-cycle figure are reproducible as artifacts, but their **manuscript role** still needs to be fixed.
   - We still need to decide whether they are:
     - historical summaries of the selected specification, or
     - outputs tied to one representative final cutoff.

3. The synthesis figures are the most sensitive selected-run artifacts.
   - They are reproducible from the workflow repo,
   - but they must be regenerated or re-verified against the exact final selected run that produced the current Table 1 CRPS values.

## Table provenance map

### Interpretation-dependent tables in the manuscript

| Manuscript label | Current manuscript role | Current provenance evidence | Confidence | Repro status | Selected-run status | Recommended action |
|---|---|---|---|---|---|---|
| `tab:benchmark_crps_models` | main five-cutoff forecast-validation table | current manuscript table; not audited here against workflow exports | medium | needs separate validation against finalized benchmark pipeline | main reference table | leave for separate benchmark audit |
| `tab:components_23_31` | main-text covariate-effects summary | workflow export contract exists for `covariate_effects_summary.csv`; helper code and tests exist; current values also appear in workflow `article.txt` | medium | reproducible from workflow repo in principle | must match final selected run | regenerate from final selected run and relink manuscript table |
| `tab:gamma_sigma_intervals1` | appendix `gamma` summary | workflow export contract exists for `gamma_summary.csv`; helper code and tests exist; current values also appear in workflow `article.txt` | medium | reproducible from workflow repo in principle | provenance role still needs decision | verify against selected specification export, then keep or regenerate |
| `tab:gamma_sigma_intervals2` | appendix `sigma` summary | workflow export contract exists for `sigma_summary.csv`; helper code and tests exist; current values also appear in workflow `article.txt` | medium | reproducible from workflow repo in principle | provenance role still needs decision | verify against selected specification export, then keep or regenerate |

### Notes on table confidence

1. Table exports are better documented than they first appeared.
   - The workflow repo has a formal post-stage artifact contract.
   - Export helpers and tests are already in place.
   - The missing piece is the exact run-level linkage for the current manuscript tables.

2. `tab:components_23_31` is the highest-priority table to refresh.
   - The current note says the coefficients are reported at final time `T`.
   - That is no longer sufficient on its own now that the paper's main empirical evidence is the five-cutoff CRPS comparison.
   - We need to decide whether the covariate table is tied to one representative final cutoff or another explicitly defined selected run, and then regenerate it from that run.

3. The appendix `gamma` and `sigma` tables may be acceptable as historical summaries of the selected specification.
   - If we keep them that way, the captions and surrounding text should say so explicitly.
   - If not, they should be regenerated from the same selected-run context as the other interpretation summaries.

## Provenance classification for the next phase

### Group A: keep as workflow-linked setup figures
These already have strong provenance and do not depend on the selected-run decision.
- `fig:sanlorenzo`
- `fig:covariates`
- `fig:retrospectives`
- `fig:ensembles`

### Group B: selected-run dependent and must be refreshed or verified first
These are too tightly tied to one fitted output to leave ambiguous.
- `fig:synth1`
- `tab:components_23_31`
- `fig:synth2` if retained in the appendix

### Group C: reproducible, but manuscript role still needs an explicit provenance decision
These can be kept only if we clearly decide whether they are historical summaries of the selected specification or outputs from one representative final cutoff.
- `fig:dry_quantile`
- `fig:rainy_quantile`
- `fig:80_components`
- `tab:gamma_sigma_intervals1`
- `tab:gamma_sigma_intervals2`

## Recommended next steps

1. Decide the provenance policy for Section 5 and the appendix.
   - Recommended policy:
     - Section 4 remains the five-cutoff validation evidence.
     - Section 5 uses outputs from one representative final cutoff of the selected `exAL-M-T1` specification.
     - Appendix tables/figures may remain historical summaries of the selected specification if labeled clearly.

2. Regenerate the selected-run dependent outputs first.
   - `tab:components_23_31`
   - `fig:synth1`
   - `fig:synth2` if retained

3. Make an explicit keep-versus-regenerate decision for the historical summary objects.
   - `fig:dry_quantile`
   - `fig:rainy_quantile`
   - `fig:80_components`
   - `tab:gamma_sigma_intervals1`
   - `tab:gamma_sigma_intervals2`

4. Once the selected-run provenance is settled, update the manuscript captions and nearby text so the role of each object is explicit.

5. After the manuscript-side provenance is stable, synchronize the corrections letter to the same selected-run logic and figure/table references.

## Audit status summary

### Established in this pass
- the current manuscript figure assets are workflow-linked and hash-verified,
- the workflow repo contains a formal table-export path for the interpretation tables,
- and we now know which outputs are safe to keep, which need explicit provenance language, and which must be regenerated from the final selected run.

### Still unresolved after this pass
- exact run-level linkage between the current interpretation tables/figures and the finalized `exAL-M-T1` benchmark run behind Table 1,
- final manuscript policy for historical summaries versus representative-final-cutoff illustrations,
- and the corresponding corrections-letter synchronization.
