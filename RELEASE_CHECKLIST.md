# Release checklist

## Implemented
- [x] The vendor-data source repository is private.
- [x] This destination has independent Git history; no fork/import.
- [x] Copied the actual reusable source, experiments, core numerical tests and
      one clearly identified synthetic mechanism figure.
- [x] No `data/`, `results/`, `archive/` or licensed raw CSVs in the publication tree.
- [x] Removed legacy source-archive material from supplement sections S1–S4.
- [x] Source origin commit and per-file Git blob IDs recorded in SOURCE_PROVENANCE.json.

## Must pass before a software release / Zenodo DOI
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
- [ ] Enable this repository in Zenodo **before** creating a tagged release.
- [ ] Create a GitHub `v0.1.0` release, verify the Zenodo DOI, update citation
      metadata with the *actual* DOI, and cite in the author paper if permitted.

## Editorial status
This repository is a **research software candidate**, not a deposit of
Barchart, Databento or other licensed market data. It does not guarantee
independent full empirical replication from the public tree alone.
