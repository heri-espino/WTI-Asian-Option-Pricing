# Installation and validation

This is the public source-only research software. It has independent Git
history and excludes the private project's downloaded market observations.

For dependency profiles, optional packages and reproducibility constraints,
see [docs/dependencies.md](docs/dependencies.md).

## Option A: pip + virtual environment (Windows PowerShell)

```powershell
cd WTI-Asian-Option-Pricing
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python scripts/check_public_release.py
python -m pytest -q
python examples/posterior_integration_vs_plugin.py
```

On macOS/Linux, replace the environment creation/activation with
`python3 -m venv .venv` and `source .venv/bin/activate`, then run
the same `python -m pip ...` commands.

To install only the library, use `requirements.txt` instead.
To install optional Databento/yfinance clients, use `requirements-market.txt`.

## Option B: Conda

```bash
conda env create -f environment.yml
conda activate wti-asian-option-pricing
python scripts/check_public_release.py
python -m pytest -q
python examples/posterior_integration_vs_plugin.py
```

The separate `environment-market.yml` adds optional vendor clients,
but it does not obtain a market-data license.

## What is reproducible?

The numerical tests and illustrative synthetic example require no vendor
account. Full empirical experiments need **your own licensed input data**,
plus the time-stamped source definitions documented under `docs/`.
Do not silently substitute Yahoo CL=F for contract-specific CL curves.

## Before a Zenodo DOI

Finish the open tasks in [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md),
including the independent scientific and data-rights review, double-blind
submission policy, and verification of the specific release files.
The repository has **not** yet been assigned a Zenodo DOI.
