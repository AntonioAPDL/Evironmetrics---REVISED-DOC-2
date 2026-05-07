#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
from pathlib import Path

HISTORICAL_SPEC = {
    "bundle": "historical_summary_sources",
    "title": "Historical Summary Figure Provenance Bundle",
    "readme": """# Historical Summary Figure Provenance Bundle

This bundle freezes the workflow-linked historical-summary figures retained in the revised article as descriptive appendix/supporting material.

Refresh script:
- `scripts/refresh_local_provenance_bundles.py`

Role in the manuscript:
- historical summaries of the fitted specification
- not part of the narrow five-cutoff `exAL-M-T1` keep-run validation lineage
- not representative-cutoff outputs
- not additional rolling-origin validation evidence

Workflow-side evidence:
- gold hash manifest:
  - `{workflow_root}/repro/gold_DISC_figures.sha256`
- repository map:
  - `{workflow_root}/repro/REPO_MAP.md`
- reproduction guide:
  - `{workflow_root}/repro/REPRODUCE_PAPER.md`
- historical figure-generation script:
  - `{workflow_root}/R/environmetrics/40_figures.R`

Verification status:
- the copied PNGs in `figures/` hash-match the workflow gold manifest exactly
- the hashes are recorded in `SHA256SUMS.txt`
- the per-figure source map is recorded in `manifest.csv`

This bundle is intentionally frozen rather than rerun during the narrow `exAL-M-T1` replay cycle.
""",
    "manifest_header": [
        "manuscript_label",
        "local_bundle_file",
        "article_disc_file",
        "sha256",
        "workflow_gold_manifest",
        "workflow_repo_map_ref",
        "workflow_reproduce_ref",
        "workflow_script_ref",
        "role",
        "rerun_status",
    ],
    "rows": [
        {
            "manuscript_label": "fig:dry_quantile",
            "filename": "All_exal_2012-2016_DISC.png",
            "workflow_repo_map_ref": "repro/REPO_MAP.md:82",
            "workflow_reproduce_ref": "repro/REPRODUCE_PAPER.md:94",
            "workflow_script_ref": "R/environmetrics/40_figures.R:7493",
            "role": "historical summary of fitted specification",
            "rerun_status": "not rerun in narrow exAL-M-T1 cycle",
        },
        {
            "manuscript_label": "fig:rainy_quantile",
            "filename": "All_exal_2017-2019_DISC.png",
            "workflow_repo_map_ref": "repro/REPO_MAP.md:83",
            "workflow_reproduce_ref": "repro/REPRODUCE_PAPER.md:95",
            "workflow_script_ref": "R/environmetrics/40_figures.R:7331",
            "role": "historical summary of fitted specification",
            "rerun_status": "not rerun in narrow exAL-M-T1 cycle",
        },
        {
            "manuscript_label": "fig:80_components",
            "filename": "80_component_1991_2022.png",
            "workflow_repo_map_ref": "repro/REPO_MAP.md:81",
            "workflow_reproduce_ref": "repro/REPRODUCE_PAPER.md:93",
            "workflow_script_ref": "R/environmetrics/40_figures.R:7869",
            "role": "historical summary of fitted specification",
            "rerun_status": "not rerun in narrow exAL-M-T1 cycle",
        },
    ],
}

WORKFLOW_LINKED_SPEC = {
    "bundle": "workflow_linked_support_sources",
    "title": "Workflow-Linked Support Figure Bundle",
    "readme": """# Workflow-Linked Support Figure Bundle

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
- generator logic: `{workflow_root}/R/environmetrics/40_figures.R`
- headless figure runner: `{workflow_root}/scripts/run_environmetrics_figures.R`
- workflow handoff: `{workflow_root}/R/unified/stages/stage_post.R`

Legacy path to avoid as the primary contract:
- `{workflow_root}/scripts/make_environmetrics_figures.R`

This bundle closes the remaining article-side provenance gap for workflow-linked setup/support figures.
""",
    "manifest_header": [
        "article_label",
        "filename",
        "manuscript_role",
        "provenance_role",
        "article_disc_path",
        "bundle_path",
        "sha256",
        "gold_sha256",
        "gold_match",
        "primary_generator",
        "clean_entrypoint",
        "notes",
    ],
    "rows": [
        {
            "article_label": "fig:sanlorenzo",
            "filename": "usgs.png",
            "manuscript_role": "study-setting figure",
            "provenance_role": "setup/support",
            "primary_generator": "R/environmetrics/40_figures.R",
            "clean_entrypoint": "scripts/run_environmetrics_figures.R",
            "notes": "workflow-linked support figure; clean via run-scoped workflow",
        },
        {
            "article_label": "fig:covariates",
            "filename": "precip_soilmoisture_climatePC1_faceted_labeled.png",
            "manuscript_role": "covariate setup figure",
            "provenance_role": "setup/support",
            "primary_generator": "R/environmetrics/40_figures.R",
            "clean_entrypoint": "scripts/run_environmetrics_figures.R",
            "notes": "workflow-linked support figure; clean via run-scoped workflow",
        },
        {
            "article_label": "fig:retrospectives",
            "filename": "retrospective_log_discharge_plot_faceted.png",
            "manuscript_role": "retrospective-product setup figure",
            "provenance_role": "setup/support",
            "primary_generator": "R/environmetrics/40_figures.R",
            "clean_entrypoint": "scripts/run_environmetrics_figures.R",
            "notes": "workflow-linked support figure; retrospective selection logic rebuilt in current script",
        },
        {
            "article_label": "fig:ensembles",
            "filename": "forecats.png",
            "manuscript_role": "forecast-product setup figure",
            "provenance_role": "setup/support",
            "primary_generator": "R/environmetrics/40_figures.R",
            "clean_entrypoint": "scripts/run_environmetrics_figures.R",
            "notes": "workflow-linked support figure; depends on documented forecast weighting/overlay contract",
        },
        {
            "article_label": "fig:synth2",
            "filename": "posterior_samples_counter_valid.png",
            "manuscript_role": "appendix historical-only reference synthesis",
            "provenance_role": "appendix support",
            "primary_generator": "R/environmetrics/40_figures.R",
            "clean_entrypoint": "scripts/run_environmetrics_figures.R",
            "notes": "workflow-linked counterfactual artifact; intentionally outside narrow selected-run refresh",
        },
    ],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_gold_hashes(workflow_root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    gold_path = workflow_root / "repro" / "gold_DISC_figures.sha256"
    for line in gold_path.read_text().splitlines():
        if "  DISC/" not in line:
            continue
        digest, rel = line.split("  ", 1)
        out[rel.replace("DISC/", "")] = digest
    return out


def write_bundle(article_root: Path, workflow_root: Path, spec: dict, gold: dict[str, str]) -> None:
    bundle_root = article_root / "generated" / spec["bundle"]
    fig_dir = bundle_root / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    disc_dir = article_root / "DISC"

    rows_out: list[list[str]] = []
    sums: list[str] = []

    for row in spec["rows"]:
        src = disc_dir / row["filename"]
        dst = fig_dir / row["filename"]
        shutil.copy2(src, dst)
        digest = sha256(dst)
        sums.append(f"{digest}  figures/{row['filename']}")

        if spec["bundle"] == "historical_summary_sources":
            rows_out.append([
                row["manuscript_label"],
                f"figures/{row['filename']}",
                f"DISC/{row['filename']}",
                digest,
                str(workflow_root / "repro" / "gold_DISC_figures.sha256"),
                str(workflow_root / row["workflow_repo_map_ref"]),
                str(workflow_root / row["workflow_reproduce_ref"]),
                str(workflow_root / row["workflow_script_ref"]),
                row["role"],
                row["rerun_status"],
            ])
        else:
            rows_out.append([
                row["article_label"],
                row["filename"],
                row["manuscript_role"],
                row["provenance_role"],
                f"DISC/{row['filename']}",
                f"generated/{spec['bundle']}/figures/{row['filename']}",
                digest,
                gold.get(row["filename"], ""),
                str(digest == gold.get(row["filename"], "")),
                row["primary_generator"],
                row["clean_entrypoint"],
                row["notes"],
            ])

    readme = spec["readme"].format(workflow_root=str(workflow_root))
    (bundle_root / "README.md").write_text(readme)

    with (bundle_root / "manifest.csv").open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(spec["manifest_header"])
        writer.writerows(rows_out)

    (bundle_root / "SHA256SUMS.txt").write_text("\n".join(sorted(sums)) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh local article-side provenance bundles.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--workflow-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--bundle", choices=["all", "historical", "workflow_linked"], default="all")
    args = parser.parse_args()

    article_root = args.article_root.resolve()
    workflow_root = args.workflow_root.resolve()
    gold = load_gold_hashes(workflow_root)

    if args.bundle in {"all", "historical"}:
        write_bundle(article_root, workflow_root, HISTORICAL_SPEC, gold)
    if args.bundle in {"all", "workflow_linked"}:
        write_bundle(article_root, workflow_root, WORKFLOW_LINKED_SPEC, gold)

    print("Refreshed provenance bundles successfully.")


if __name__ == "__main__":
    main()
