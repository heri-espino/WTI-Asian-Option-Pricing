# Contributing

Contributions should improve numerical correctness, documentation or
reproducibility without adding licensed market observations.

1. Start from `main`, use a short-lived feature branch, and open a pull request.
2. Install the development profile from `requirements-dev.txt` or
   `environment.yml`.
3. Run `python scripts/check_public_release.py`,
   `python -m pytest -q`, and
   `python examples/posterior_integration_vs_plugin.py`.
4. Add tests to numerical changes and document any scientific assumption.
5. Do not change historical inference under P, pricing under Q, target-date
   information cutoffs, or first-nearby fixing mechanics without an explicit
   methodological justification and corresponding tests.
6. Never upload raw market data, vendor account details, tokens, hard-coded
   workstation paths, transaction-level price panels or the old private repo's
   Git history. The release scanner is a guardrail, not a guarantee.
7. Heavy simulations and artifact builds must be manual, not triggered by pushes.

For the current software release status and pending scientific audit, see
[`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md).
