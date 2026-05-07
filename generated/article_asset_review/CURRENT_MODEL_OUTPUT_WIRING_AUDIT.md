# Current Model-Output Wiring Audit

Date: 2026-05-07

## Purpose

This note records which manuscript figures and appendix tables are currently tied to the refreshed `2022-12-25` representative model-output bundle and which ones are still workflow-linked historical/support artifacts outside that refreshed path.

Representative verified model-output bundle:

- `generated/exal_m_t1_20221225/`

Representative manuscript-facing copies:

- `DISC/posterior_samples_valid.png`
- `DISC/usgs.png`
- `DISC/precip_soilmoisture_climatePC1_faceted_labeled.png`
- `DISC/retrospective_log_discharge_plot_faceted.png`
- `DISC/forecats.png`

## Figure and Table Status

| Manuscript object | Current article number | Current source | Current-model-output wired? | Notes |
|---|---|---|---|---|
| `fig:sanlorenzo` | Figure 1 | `generated/setup_support_by_cutoff_v2/20221225_exal_m_t1/figures/usgs.png` -> `DISC/usgs.png` | Yes | Refreshed from the validated `v2` setup/support family for the representative `2022-12-25` cutoff. |
| `fig:covariates` | Figure 2 | `generated/setup_support_by_cutoff_v2/20221225_exal_m_t1/figures/precip_soilmoisture_climatePC1_faceted_labeled.png` -> `DISC/...` | Yes | Refreshed from the validated `v2` setup/support family. |
| `fig:retrospectives` | Figure 3 | `generated/setup_support_by_cutoff_v2/20221225_exal_m_t1/figures/retrospective_log_discharge_plot_faceted.png` -> `DISC/...` | Yes | Refreshed from the validated `v2` setup/support family. |
| `fig:ensembles` | Figure 4 | `generated/setup_support_by_cutoff_v2/20221225_exal_m_t1/figures/forecats.png` -> `DISC/...` | Yes | Refreshed from the validated `v2` setup/support family. |
| `fig:dry_quantile` | Figure 5 | `generated/historical_summary_sources/figures/All_exal_2012-2016_DISC.png` -> `DISC/...` | No | Historical-summary figure, hash-matched and frozen locally, but not refreshed from the current representative model-output bundle. |
| `fig:rainy_quantile` | Figure 6 | `generated/historical_summary_sources/figures/All_exal_2017-2019_DISC.png` -> `DISC/...` | No | Historical-summary figure, hash-matched and frozen locally, but not refreshed from the current representative model-output bundle. |
| `fig:synth1` | Figure 7 | `generated/exal_m_t1_20221225/posterior_samples_valid.png` -> `DISC/posterior_samples_valid.png` | Yes | Byte-for-byte match with the verified representative `2022-12-25` rerun bundle. |
| `tab:components_23_31` | Table 2 | `generated/exal_m_t1_20221225/covariate_effects_summary.csv` | Yes, but manually synced into TeX | Values are current, but the table is not `\\input{}`-driven yet. |
| `tab:gamma_sigma_intervals1` | Table A.1 | `generated/exal_m_t1_20221225/gamma_summary.csv` | Yes, but manually synced into TeX | Current values match the regenerated `gamma` export, but the table is still manually maintained in `wileyNJD-APA.tex`. |
| `tab:gamma_sigma_intervals2` | Table A.2 | `generated/exal_m_t1_20221225/sigma_summary.csv` | Yes, but manually synced into TeX | Current values match the regenerated `sigma` export, but the table is still manually maintained in `wileyNJD-APA.tex`. |
| `fig:80_components` | Figure A1 | `generated/historical_summary_sources/figures/80_component_1991_2022.png` -> `DISC/...` | No | Historical long-cycle summary, hash-matched and frozen locally, but not refreshed from the current representative model-output bundle. |
| `fig:synth2` | Figure A2 | `generated/workflow_linked_support_sources/figures/posterior_samples_counter_valid.png` -> `DISC/...` | No | Workflow-linked historical-only counterfactual figure, not part of the refreshed representative rerun bundle. |

## Important Clarifications

1. `Figure 7` is current.
   - `DISC/posterior_samples_valid.png` matches `generated/exal_m_t1_20221225/posterior_samples_valid.png` exactly.

2. `Figures 5 and 6` are not current-model-output figures.
   - They are reproducible and frozen locally, but they are still historical-summary assets outside the refreshed representative rerun path.

3. `Tables A.1 and A.2` do use the current regenerated `2022-12-25` representative model exports.
   - However, they are still copied into the manuscript manually rather than auto-included from the generated files.

4. `Figure A1` is not from the current representative rerun bundle.
   - It is a historical long-cycle summary, not a refreshed representative-cutoff output.

5. `Figure A2` is not from the current representative rerun bundle.
   - It is a historical-only counterfactual artifact.
   - It is **not** the same thing as a forecast-window synthesis from the univariate `exdqlm` model.

## Practical Meaning

If the standard is:

- "must come directly from the current refreshed representative model-output bundle,"

then the manuscript objects that currently fail that standard are:

- Figure 5
- Figure 6
- Figure A1
- Figure A2

If the standard is:

- "must be reproducible and locally frozen, even if they are outside the refreshed representative rerun path,"

then those four objects are reproducible, but they are still only workflow-linked support/historical objects rather than current representative model-output objects.
