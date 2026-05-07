# HE2 Publication Manifest Snapshot

This bundle freezes a local copy of the HE2 publication manifest used to source the main five-cutoff benchmark CRPS table in the revised article.

Purpose:
- preserve an article-side copy of the frozen HE2 publication benchmark source
- keep the revised article repo self-contained for the final benchmark table values
- record the exact files used to synchronize `tab:benchmark_crps_models`

Contents:
- `he2_bayesian_publication_manifest.md`
- `he2_bayesian_publication_manifest.csv`
- `he2_bayesian_publication_alignment.csv`
- `he2_bayesian_publication_inputs.csv`

Source workflow location:
- `/data/muscat_data/jaguir26/project1_ucsc_phd/reports/he2_publication_manifest/`

Role in the manuscript:
- supports `tab:benchmark_crps_models`
- provides the frozen five-cutoff benchmark values for all Bayesian model families
- the `exAL-M-T1` row in the article is additionally backed by the narrower verified replay bundle under `generated/exal_m_t1_five_run_sources/`
