# exAL-M-T1 Setup/Support v2 Input Alignment Audit

Date: 2026-05-07

## Scope

This audit checks whether the cutoff-specific `v2` setup/support figures under `generated/setup_support_by_cutoff_v2/` are plotted from the same input bundles used by the verified `exAL-M-T1` model runs that reproduce the published HE2 CRPS table.

The audit focuses on four questions:

1. Do the plotted retrospective and forecast files exactly match the model-input bundles behind the selected `exAL-M-T1` runs?
2. Why do several `retrospective_log_discharge_plot_faceted.png` panels still look chopped?
3. Is `20220511_exal_m_t1/figures/forecats.png` using the correct retrospective and forecast lineage, especially for NWS?
4. Can we truthfully say that the cutoff-specific setup/support figures are aligned with the model-input bundles used for the CRPS table?

## Bottom line

- `nws_forecast.csv`, `glofas_forecast.csv`, and `retros.csv` used by the figures are aligned with the selected model-input bundles for all five cutoffs.
- `2022-05-11 forecats.png` is using the correct histfix lineage: `nws_retro_v21` early, `nws_retro_v30` tail fill near cutoff, `glofas_hist_v31_lisflood_cons`, `nws_forecast` with 8 daily targets, and `glofas_forecast` with 28 daily targets.
- `usgs.png` and the covariate figure now use full `1987-05-29 -> cutoff` history, and the current coverage audit shows no missing daily coverage in those windows.
- The chopped retrospective panels are **not** just a plotting bug. For `2021-01-23`, `2021-11-12`, and `2022-12-25`, the selected retrospective support used by the model itself is genuinely short-window. So a figure that is both:
  - perfectly faithful to the selected model-input retrospective support, and
  - visually full-history from 1987,
  is not possible for those three cutoffs without changing the meaning of the figure.

## Exact alignment checks

For each cutoff, the audit compared the selected-run shared inputs against the source paths recorded in `inputs/shared/source_map.txt`.

### Result summary

| Cutoff | `retros.csv` matches selected model input source | `nws_forecast.csv` matches selected model input source | `glofas_forecast.csv` matches selected model input source | Requested retrospective span | Actual selected retrospective span | Full retrospective history available? |
|---|---|---|---|---|---|---|
| `2021-01-23` | Yes | Yes | Yes | `1987-05-29 -> 2021-01-23` | `2018-02-08 -> 2021-01-23` | No |
| `2021-11-12` | Yes | Yes | Yes | `1987-05-29 -> 2021-11-12` | `2018-11-28 -> 2021-11-12` | No |
| `2021-12-21` | Yes | Yes | Yes | `1987-05-29 -> 2021-12-21` | `1987-05-29 -> 2021-12-21` | Yes |
| `2022-05-11` | Yes | Yes | Yes | `1987-05-29 -> 2022-05-11` | `1987-05-29 -> 2022-05-11` | Yes |
| `2022-12-25` | Yes | Yes | Yes | `1987-05-29 -> 2022-12-25` | `2020-01-10 -> 2022-12-25` | No |

The requested vs available spans above come directly from the per-cutoff `coverage_audit.yaml` files in `generated/setup_support_by_cutoff_v2/<cutoff>/metadata/`.

## Why the short-window retrospective panels look chopped

This is the key distinction.

For the short-window cutoffs (`2021-01-23`, `2021-11-12`, `2022-12-25`), the selected `exAL-M-T1` runs do **not** use a full 1987-to-cutoff retrospective support window. The preserved retrospective input actually begins later.

That is consistent with the documented short-window synthetic-retrospective policy in:

- `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/UNIFIED_MULTIMODEL_WORKFLOW_TRACKER.md`
- `/data/muscat_data/jaguir26/project1_ucsc_phd/repro/run/EXAL_M_T1_SETUP_SUPPORT_V2_SOURCE_MANIFEST.md`

Operationally, those cutoffs use a shared retrospective window determined by the selected NWS synthetic retrospective and the selected GloFAS retrospective support. The resulting model-input retrospective series starts at:

- `2018-02-08` for `2021-01-23`
- `2018-11-28` for `2021-11-12`
- `2020-01-10` for `2022-12-25`

So the current retrospective panels are revealing a real property of the selected model-input contract, not silently using the wrong forecast files.

## `2022-05-11 forecats.png` validation

This cutoff belongs to the long-history histfix class.

Confirmed bundle lineage:

- GloFAS retrospective source: `glofas_hist_v31_lisflood_cons`
- NWS retrospective source policy: `nws_retro_v21` early, `nws_retro_v30` tail fill near cutoff
- NWS forecast range: `2022-05-12 -> 2022-05-19`
- GloFAS forecast range: `2022-05-12 -> 2022-06-08`

From the authoritative histfix lineage table:

- `nws_retro_v21`: `12271` daily rows
- `nws_retro_v30`: `496` daily rows
- last rows before cutoff are all `nws_retro_v30`

This is the expected and documented behavior for the `2022-05-11` histfix cutoff.

## Coverage conclusions by figure type

### `usgs.png`

- Uses the selected-run shared USGS series.
- Full `1987-05-29 -> cutoff` coverage is available for all five cutoffs.
- No missing daily coverage was found in the requested window.

### `precip_soilmoisture_climatePC1_faceted_labeled.png`

- Uses the selected-run shared `PPT`, `SOIL`, and `PCA` covariate files.
- Full `1987-05-29 -> cutoff` coverage is available for all five cutoffs.
- No missing daily coverage was found in the requested window.

### `retrospective_log_discharge_plot_faceted.png`

- Uses retrospective support aligned to the selected model-input retrospective series.
- Full `1987-05-29 -> cutoff` support is available only for `2021-12-21` and `2022-05-11`.
- The short-window cutoffs are faithfully short because the model-input retrospective support itself is short.

### `forecats.png`

- Uses the selected cutoff-specific forecast products and the cutoff-centered `+/- 28 day` display window.
- Forecast bundles align with the selected model-input forecast files for all five cutoffs.

## Honest limitation

The current `v2` family can honestly claim:

- setup/support figures are cutoff-specific,
- forecast files match the selected model-input bundles,
- retrospective files match the selected model-input bundles,
- and the full-history coverage audit is explicit.

But it cannot honestly claim that **all retrospective figures should show 1987-to-cutoff model-input support** for all cutoffs, because that is false for three of the five selected `exAL-M-T1` runs.

## Recommended interpretation

The clean interpretation is:

- `usgs.png` and the covariate figure are full-history context figures through the cutoff;
- `forecats.png` is the cutoff-centered forecast-context figure;
- `retrospective_log_discharge_plot_faceted.png` is the selected-model-input retrospective support figure, which is full-history only for the histfix cutoffs.

If a full-history retrospective-source figure is still desired for all cutoffs, it should be introduced as a **different figure class** derived from raw retrospective source histories, not as the exact selected model-input retrospective figure.
