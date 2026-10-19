# Maintainer guidance

This is a **public, source-only research software repository** for the paper
*Posterior Integration and Volatility Inputs in WTI Asian Options*.

- Maintain `main` as the only long-lived branch.
- Keep reusable code under `src/bayesian_asian_options/`; experiment entry
  points under `experiments/`, and numerical checks under `tests/`.
- Never import/fork/mirror the original research repository's Git history.
- **Never commit** raw Barchart or Databento histories, CME prices, market
  contract-date panels, proprietary reports, access tokens or personal system paths.
- Do not move experiment-generated outputs, raw downloads or trading data into
  the public repository. Local source data go in gitignored `data/`.
- Do not modify the scientific model to make tests pass: posterior inference is
  under physical P, risk-neutral pricing under Q, and target-date option
  settlements are excluded from prior-day volatility fits.
- Keep source provenance accurate and identify scientific results as reported,
  not independently reproduced, until the specific audit is completed.
- Public software builds and tests can run on push; large figure regeneration,
  paper compilation, simulations and archiving must be manually triggered.
- Update `AI_HANDOFF.md` after meaningful work. The publication release is
  **blocked** until code rights, cited numbers and journal blinding are checked.
