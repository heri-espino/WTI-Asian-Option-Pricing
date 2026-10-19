# Quick setup

This is the actual clean public research repository. It has a fresh Git
history and excludes all third-party raw market observations.

## Install and verify

```bash
python -m venv .venv
# PowerShell: .venv\\Scripts\\Activate.ps1
# Unix: source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/check_public_release.py
python -m pytest -q tests
```

## What can run without market data?

Core mathematical and simulation tests do not require a Barchart or Databento
account. The full empirical workflows under `experiments/` require
separately licensed dated futures/option observations; see
`docs/market_data_and_reproducibility.md`. They should not automatically
download/purchase market data.

## Releasing the research software

Do **not** tag or release until the checks in `RELEASE_CHECKLIST.md` pass.
Enable this repository in Zenodo's GitHub integration *before* the first
release. After Zenodo archives the GitHub release, use its real DOI in
`CITATION.cff` and the author-identified manuscript where allowed.
