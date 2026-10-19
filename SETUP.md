# Creating the clean repository without transferring the old Git history

The publication kit does **not** create a GitHub repository or Zenodo DOI automatically. First confirm the original vendor-data repository is private.

## Step A — create an empty private destination

Use https://github.com/new?owner=heri-espino&name=WTI-Asian-Option-Pricing&visibility=private . Set the name to `WTI-Asian-Option-Pricing`. Leave **Initialize with README**, `.gitignore`, and **license** unchecked, because the export provides those files. Create it as **private first** until the release audit is complete.

If working with ChatGPT connected to GitHub, give it the new repository URL and grant the GitHub connector access to the repository. It can then help transfer reviewed source files and documentation without asking you to manage Git commands.

## Step B — optionally export the sources yourself

Extract this ZIP. It contains a source-export tool, `prepare_public_repository.py`. You must run it against a **local copy** of the original (now private) research repository; the ZIP intentionally does not contain the entire scientific source code.

```powershell
python prepare_public_repository.py `
  --source "C:\path\to\Bayesian-Uncertainty-in-WTI-APOs" `
  --dest "C:\path\to\WTI-Asian-Option-Pricing"
cd "C:\path\to\WTI-Asian-Option-Pricing"
python scripts/check_public_release.py
python -m pip install -e ".[dev]"
python -m pytest -q tests/test_bayesian_gbm.py tests/test_asian_pricing.py
```

The exporter copies 18 pricing/inference modules, 39 experiment entry points, nine mathematical/numerical tests, a synthetic-only figure, and the cleaned S1–S4 supplement when present. It excludes the original `data/`, `results/`, vendor bundles, archives and `.git` history. It generates `SOURCE_PROVENANCE.json` from source hashes and the private commit ID. **This is an export candidate, not a substitute for human content and rights review.**

If those test commands fail in the stripped-down public layout, fix or document that dependency before publishing. Do not silently add restricted market data to make tests pass.

## Step C — review and publish later

- Inspect all files and pass the checks in `RELEASE_CHECKLIST.md`.
- Decide a software license only after confirming the original code is yours to license; do not license third-party price histories.
- Push the curated directory using a **fresh** first commit. Never import, fork or mirror the original repository.
- Once the reviewer-anonymity and market-data rights constraints are resolved, switch the **new clean repository** to public.
- Connect that repository to Zenodo, enable it, create a GitHub tagged release, verify the generated **real** DOI, then cite the software in the **author-identifying** manuscript or where the editor approves.

For precise Zenodo instructions see `docs/zenodo_and_blind_review.md`.
