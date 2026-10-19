# Dependencies and installation profiles

The **single source of package requirements** is [`pyproject.toml`](../pyproject.toml).
The requirements files and Conda environments reference its optional extras,
rather than duplicating version specifications. Minimum versions are tested in
CI against a fresh Python environment; this is not a frozen full dependency lockfile.

| File | Purpose | Installs |
| --- | --- | --- |
| `pyproject.toml` | Installable Python distribution and authoritative dependencies | NumPy, pandas, SciPy |
| `requirements.txt` | Minimal pip installation | `-e .` |
| `requirements-dev.txt` | Tests, plotting and package building | `-e .[dev]` |
| `requirements-market.txt` | Optional market-provider clients plus dev tools | `-e .[dev,market]` |
| `environment.yml` | Conda scientific/development environment | Python 3.11, `.[dev]` |
| `environment-market.yml` | Conda environment with optional vendor clients | Python 3.11, `.[dev,market]` |

## Pip (all operating systems)

```bash
python -m venv .venv
# Activate in PowerShell: .venv\Scripts\Activate.ps1
# Activate in Bash/zsh: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest -q
python examples/posterior_integration_vs_plugin.py
```

For a library-only install, instead use
`python -m pip install -r requirements.txt`.
Optional vendor clients: `python -m pip install -r requirements-market.txt`.

## Conda (all operating systems)

```bash
conda env create -f environment.yml
conda activate wti-asian-option-pricing
python -m pytest -q
```

To add optional data-provider clients in a **separate** environment:
```bash
conda env create -f environment-market.yml
conda activate wti-asian-option-pricing-market
```

Conda resolves the Python/pip bootstrap while pip performs the editable install.
Run these commands from the root of this repository. For a fresh environment
after updating the definition, use `conda env update -f environment.yml --prune`;
the Conda environment step is documented but not executed by GitHub CI.

## Scope and reproducibility

The base package needs no vendor account. The `market` extra adds
`databento` and `yfinance`; it **does not download**, purchase, or
license market observations. The private research project retains original
Barchart/Databento files; these are not available from this public archive.

Install `.[dev]` to reproduce synthetic code tests. Full historical
experiments require independently licensed dated futures and options data,
input manifests, appropriate computation, and checks against the original
private research results. The repo does not advertise a fully independent
empirical replication from source-only files.

If you need exact environment reconstruction for a Zenodo release, capture
`python -m pip freeze` and Python/OS version from the verified release job
and store them as **release metadata**, not as an unreviewed, platform-specific
global requirements file.

## Software license

The repository's original software code and documentation are distributed
under the [MIT License](../LICENSE). This license **does not grant any
redistribution rights** for Barchart, Databento, CME/NYMEX or other
third-party data. Data license compliance is independent of software licensing.
