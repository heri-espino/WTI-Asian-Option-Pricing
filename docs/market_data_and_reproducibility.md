# Market data, reproducibility and redistribution

## Sources and use

- **Barchart**: downloaded WTI APO settlement and individual CL futures histories, including price fields, volumes and open interest. These are external licensed inputs, **not project-owned data**.
- **Databento**: earlier-date vanilla WTI (`LO`) options and related CL futures series used to evaluate transfer across option families. Access can be billed and is subject to instrument/exchange permissions.
- **Yahoo CL=F**: explicitly labeled continuous/front-month historical-return *proxy*, not an exact substitute for the CL contracts needed to price the averaging schedule.
- **Treasury**: discounting inputs, including the documented approximation of converting par yields to short-horizon zero rates.

The public repository intentionally omits original observations and derivative contract-level panels. Obtaining purchase credits or downloading CSVs does **not** imply permission to redistribute them. Independently obtain and license any data required to reproduce empirical results. Vendor access alone does not imply all exchange rights.

## Reproduction hierarchy

1. **Self-contained:** inspect the package, equations, source tests and synthetic experiment configuration; no market account required.
2. **With permitted derived summaries:** compare report-level metrics and figures in the accompanying paper and reviewed supplement.
3. **With independently licensed data:** run the named market-data experiment entry points after providing documented source directories and historical cutoffs.

The last tier is not executable from this public archive alone. It should not silently fall back to invented sample prices.

## Information-set integrity

- Use only **earlier** option observations to estimate implied volatility for a valuation-date pricing comparison.
- Use the target date's realized fixings, discount factor and futures curve **only for repricing**, never to estimate prior implied volatility.
- Reconstruct the first-nearby CL fixing contract using actual expiry calendars.
- Never treat a CL roll discontinuity as a single physical WTI daily return.
- Respect within-valuation-date correlation and the small number of target dates when interpreting bootstrap intervals.

## Licensing checklist

Before public release confirm no vendor rows remain in source scripts, tests, figures, documentation, manifests or Git history. Releasing a separate clean repository avoids carrying raw market histories from the original repository's commits. A software license applies only to original code, not vendor content.
