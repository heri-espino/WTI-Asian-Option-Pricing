# Release requirements (blockers until verified)

This is a proposed clean public research **software** repository, not a data deposit.

- [ ] Set the original vendor-data repository to **private**; investigate public forks and cached copies separately.
- [ ] Create a new empty GitHub repository with a **fresh Git history**, not a fork/import/mirror of the original.
- [ ] Review the export folder, all source files and `SOURCE_PROVENANCE.json` before pushing. The automated scanner is necessary but not a license opinion.
- [ ] Confirm that no experimental script embeds a private API key, person-specific workstation path, or unlicensed market price arrays.
- [ ] Confirm ownership and choose an explicit software license. Never claim that it licenses market data.
- [ ] Verify `python -m pip install -e ".[dev]"`, relevant synthetic tests, README commands, and the source API after export.
- [ ] Recheck the cleaned supplement tables against the private source result files.
- [ ] Verify the source-commit SHA and paper manuscript numbers (310 / 2381 / 253 samples) before publication.
- [ ] Resolve the journal's double-blind review rules before including the public DOI in a blinded manuscript.
- [ ] Enable the **new** repository in Zenodo's GitHub integration **before** creating a tagged GitHub release.
- [ ] Publish a verified GitHub software release; inspect the Zenodo record and only then add its real DOI to `CITATION.cff` and the author-identified paper.

A Zenodo record, DOI and live GitHub repository do not yet exist for this release candidate.
