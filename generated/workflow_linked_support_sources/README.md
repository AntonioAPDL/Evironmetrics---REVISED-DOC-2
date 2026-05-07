# Workflow-Linked Support Figure Bundle

This bundle freezes the remaining figure assets in the revised article that are reproducible from the workflow repo, but are not part of the narrow selected-model rerun bundle.

Refresh script:
- `scripts/refresh_local_provenance_bundles.py`

Included figures:
- `usgs.png`
- `precip_soilmoisture_climatePC1_faceted_labeled.png`
- `retrospective_log_discharge_plot_faceted.png`
- `forecats.png`
- `posterior_samples_counter_valid.png`

Clean reproduction path:
- generator logic: `/data/muscat_data/jaguir26/project1_ucsc_phd/R/environmetrics/40_figures.R`
- headless figure runner: `/data/muscat_data/jaguir26/project1_ucsc_phd/scripts/run_environmetrics_figures.R`
- workflow handoff: `/data/muscat_data/jaguir26/project1_ucsc_phd/R/unified/stages/stage_post.R`

Legacy path to avoid as the primary contract:
- `/data/muscat_data/jaguir26/project1_ucsc_phd/scripts/make_environmetrics_figures.R`

This bundle closes the remaining article-side provenance gap for workflow-linked setup/support figures.
