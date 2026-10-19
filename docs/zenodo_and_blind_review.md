# Zenodo archiving and journal double-blind review

## Creating a DOI through the GitHub integration

1. Finish the code/data-rights review and select an appropriate software license. Inspect `SOURCE_PROVENANCE.json` and run `python scripts/check_public_release.py`.
2. Create a **new repository** under the researcher's GitHub account. Do not use *Import repository*, *Fork* or *Mirror*; doing so may disclose old vendor-data commits.
3. Publish the new, reviewed source contents as an initial commit on `main`. Do not include source history from the private research archive.
4. In Zenodo, connect GitHub, use **Sync now**, and enable the **new** repository **before creating the release**.
5. Create a GitHub release with an immutable version tag such as `v0.1.0` after verification. Wait for Zenodo to archive it and display the registered DOI.
6. Verify that the Zenodo record is for *software*, carries the correct author name and ORCID, points to the release, and contains no licensed data.
7. Only then record the **actual** DOI in citation metadata and the author-identified version of the manuscript.

Do **not** reserve a second Zenodo deposit DOI if you are already using automatic GitHub release archiving, unless you explicitly intend to manage a separate record; otherwise duplicate, conflicting citations can result.

## Double-blind manuscript

The new public GitHub repository and its Zenodo DOI name the author. A blinded review submission that cites or links them can defeat double-blind review. Keep the reviewer file anonymous and ask the journal whether an identifying code DOI belongs only in the title-page/metadata version until review is complete.

A truthful temporary blinded wording, if the editor approves, is:

> Code and reproducibility instructions are available as anonymized review material. The archived software DOI and identifying project repository will be supplied after the double-blind review stage.

Only use this if there actually is an anonymized review package; do not claim access has been provided when it has not.

## Paper software citation (after DOI exists)

Example formatting, **not a valid citation until completed**:

`Espino-Montelongo, H. (2026). Posterior Integration and Volatility Inputs in WTI Asian Options: Research Software (Version 0.1.0) [Computer software]. Zenodo. https://doi.org/ACTUAL-DOI`

Do not publish a placeholder DOI as if it were registered.
