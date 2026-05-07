# Article Asset Review Report
This report groups the current revised-article figures and tables by provenance role so they can be reviewed visually and operationally.
Primary visual gallery: `generated/article_asset_review/figure_gallery.html`
## Review priorities
1. Check that setup/input figures are legible and still appropriate.
2. Check that `fig:synth1` matches the intended representative selected-model story.
3. Check that historical-summary figures read as descriptive support rather than validation evidence.
4. Check that `fig:synth2` still deserves to remain as appendix support.
## Setup / Inputs
| Label | Role | Article file | Bundle file | TeX line | Note |
|---|---|---|---|---:|---|
| `fig:sanlorenzo` | Study-setting figure | `usgs.png` | `workflow_linked_support_sources/figures/usgs.png` | 241 | Workflow-linked support figure |
| `fig:covariates` | Covariate setup figure | `precip_soilmoisture_climatePC1_faceted_labeled.png` | `workflow_linked_support_sources/figures/precip_soilmoisture_climatePC1_faceted_labeled.png` | 262 | Workflow-linked support figure |
| `fig:retrospectives` | Retrospective-product setup figure | `retrospective_log_discharge_plot_faceted.png` | `workflow_linked_support_sources/figures/retrospective_log_discharge_plot_faceted.png` | 277 | Workflow-linked support figure |
| `fig:ensembles` | Forecast-product setup figure | `forecats.png` | `workflow_linked_support_sources/figures/forecats.png` | 328 | Workflow-linked support figure |

## Selected Model
| Label | Role | Article file | Bundle file | TeX line | Note |
|---|---|---|---|---:|---|
| `fig:synth1` | Representative selected-model synthesis | `posterior_samples_valid.png` | `exal_m_t1_20221225/posterior_samples_valid.png` | 455 | Verified representative 2022-12-25 exAL-M-T1 output |

## Historical Summaries
| Label | Role | Article file | Bundle file | TeX line | Note |
|---|---|---|---|---:|---|
| `fig:dry_quantile` | Dry-period historical summary | `All_exal_2012-2016_DISC.png` | `historical_summary_sources/figures/All_exal_2012-2016_DISC.png` | 428 | Historical-summary support figure |
| `fig:rainy_quantile` | Rainy-period historical summary | `All_exal_2017-2019_DISC.png` | `historical_summary_sources/figures/All_exal_2017-2019_DISC.png` | 437 | Historical-summary support figure |
| `fig:80_components` | Long-cycle component summary | `80_component_1991_2022.png` | `historical_summary_sources/figures/80_component_1991_2022.png` | 582 | Historical-summary support figure |

## Appendix Support
| Label | Role | Article file | Bundle file | TeX line | Note |
|---|---|---|---|---:|---|
| `fig:synth2` | Historical-only reference synthesis | `posterior_samples_counter_valid.png` | `workflow_linked_support_sources/figures/posterior_samples_counter_valid.png` | 596 | Workflow-linked appendix support figure |

## Tables
| Label | Role | Source | TeX line | Note |
|---|---|---|---:|---|
| `tab:benchmark_crps_models` | Five-cutoff benchmark table | `generated/he2_publication_manifest_snapshot/he2_bayesian_publication_manifest.csv` | 343 | Frozen HE2 publication manifest snapshot |
| `tab:components_23_31` | Representative covariate-effects table | `generated/exal_m_t1_20221225/covariate_effects_summary.csv` | 391 | Representative 2022-12-25 exAL-M-T1 output |
| `tab:gamma_sigma_intervals1` | Appendix gamma summary | `generated/exal_m_t1_20221225/gamma_summary.csv` | 509 | Supplementary appendix support |
| `tab:gamma_sigma_intervals2` | Appendix sigma summary | `generated/exal_m_t1_20221225/sigma_summary.csv` | 543 | Supplementary appendix support |

## Generated manifests
- `generated/article_asset_review/figure_manifest.csv`
- `generated/article_asset_review/table_manifest.csv`
