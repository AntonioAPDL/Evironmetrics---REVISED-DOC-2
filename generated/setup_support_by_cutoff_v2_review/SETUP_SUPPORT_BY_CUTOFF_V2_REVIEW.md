# Setup/Support Figures by Cutoff v2 Review

See also: `INPUT_ALIGNMENT_AUDIT.md` in this same directory for the exact selected-run input alignment and the explanation of why three retrospective panels remain short-window.

This review bundle mirrors the corrected cutoff-specific setup/input/support figures derived from the validated exAL-M-T1 v2 runtime family.

## Cutoff summary
| Cutoff | Directory | Bundle class | Requested history | Retrospective available from | Forecast window | Published CRPS |
|---|---|---|---|---|---|---:|
| 2021-01-23 | `20210123_exal_m_t1` | `short_window_synth_bundle` | 1987-05-29 to 2021-01-23 | 2018-02-08 | 2020-12-26 to 2021-02-20 | 0.1569 |
| 2021-11-12 | `20211112_exal_m_t1` | `short_window_synth_bundle` | 1987-05-29 to 2021-11-12 | 2018-11-28 | 2021-10-15 to 2021-12-10 | 0.0284 |
| 2021-12-21 | `20211221_exal_m_t1` | `histfix_long_history_bundle` | 1987-05-29 to 2021-12-21 | 1987-05-29 | 2021-11-23 to 2022-01-18 | 0.2369 |
| 2022-05-11 | `20220511_exal_m_t1` | `histfix_long_history_bundle` | 1987-05-29 to 2022-05-11 | 1987-05-29 | 2022-04-13 to 2022-06-08 | 0.0210 |
| 2022-12-25 | `20221225_exal_m_t1` | `short_window_synth_bundle` | 1987-05-29 to 2022-12-25 | 2020-01-10 | 2022-11-27 to 2023-01-22 | 0.4375 |

## Policy summary
| Cutoff | NWS policy | GloFAS policy | Notes |
|---|---|---|---|
| 2021-01-23 | nws_synth_retro_ens_mean keep-source policy | glofas_hist_v21_htessel_cons |  |
| 2021-11-12 | nws_synth_retro_ens_mean keep-source policy | glofas_hist_v31_lisflood_cons |  |
| 2021-12-21 | nws_retro_v21 with nws_retro_v30 tail fill after natural v21 coverage end | glofas_hist_v31_lisflood_cons | histfix lineage should show nws_retro_v21 early support and nws_retro_v30 tail fill near cutoff |
| 2022-05-11 | nws_retro_v21 with nws_retro_v30 tail fill after natural v21 coverage end | glofas_hist_v31_lisflood_cons | histfix lineage should show nws_retro_v21 early support and nws_retro_v30 tail fill near cutoff |
| 2022-12-25 | nws_synth_retro_ens_mean keep-source policy with documented gapfix | glofas_hist_v31_lisflood_cons | gapfix applied to nws_synth_retro_ens_mean on 2022-07-15 |

## Coverage audit
| Cutoff | USGS full history | PPT full history | SOIL full history | PCA full history | Retros full history | Retros available start |
|---|---|---|---|---|---|---|
| 2021-01-23 | True | True | True | True | False | 2018-02-08 |
| 2021-11-12 | True | True | True | True | False | 2018-11-28 |
| 2021-12-21 | True | True | True | True | True | 1987-05-29 |
| 2022-05-11 | True | True | True | True | True | 1987-05-29 |
| 2022-12-25 | True | True | True | True | False | 2020-01-10 |
