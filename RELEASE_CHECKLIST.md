# Release checklist

## Implemented
- [x] The vendor-data source repository is private.
- [x] This destination has independent Git history; no fork/import.
- [x] Copied the actual reusable source, experiments, core numerical tests and
      one clearly identified synthetic mechanism figure.
- [x] No `data/`, `results/`, `archive/` or licensed raw CSVs in the publication tree.
- [x] Removed legacy source-archive material from supplement sections S1–S4.
- [x] Source origin commit and per-file Git blob IDs recorded in SOURCE_PROVENANCE.json.

## Archived software release

- [x] Published GitHub [v0.1.0](https://github.com/heri-espino/WTI-Asian-Option-Pricing/releases/tag/v0.1.0).
- [x] Obtained Zenodo DOI for v0.1.0: [10.5281/zenodo.23468649](https://doi.org/10.5281/zenodo.23468649) (record supplied by the author).

The archive already exists. The unfinished items below are follow-up scientific, legal, editorial, and release-quality checks; they must **not** be silently marked as passed simply because a DOI exists.

## Scientific and release-quality follow-up
- [x] Public CI installation, imports, 46 numerical tests and source-only scanner passed (commit `d5df8de250446f30fc06a7d6b48421ed28c1aedf`).
- [ ] Revalidate MIT packaging, pip/Conda manifests, source test suite and wheel/sdist build on this update.
- [ ] Independently verify full numerical reported results using *private* licensed inputs.
- [ ] Inspect every source script for local paths, network downloads or proprietary rows.
- [x] MIT license added to original source and packaging metadata. Vendor-data rights are explicitly excluded.
- [ ] Author confirms all copied source code is theirs to release under MIT and checks any third-party code notices.
- [ ] Confirm no third-party market data in PNG/supplement; figures derived from
      strictly synthetic histories are generally lower risk.
- [ ] Check REMEF's double-blind review policy before putting a public DOI
      into the reviewer manuscript.
- [x] Enabled GitHub–Zenodo integration and archived the v0.1.0 GitHub release.
- [x] Recorded the actual release DOI in the repository citation metadata.
- [ ] Ensure the author-identified REMEF manuscript cites the DOI while the blinded reviewer version does not identify the author.

## Editorial status
The DOI refers to an **archived research software release**, not a deposit of
Barchart, Databento or other licensed market data. It does not guarantee
independent full empirical replication from the public tree alone.
