# AI handoff — clean WTI Asian-option pricing repository

## Purpose
A source-only public software companion to the REMEF research paper; the
private original repository retains Barchart/Databento observations,
intermediate data, JFM drafts, and full experiment history.

## Scientific boundary
Bayesian inference uses physical futures returns; option pricing uses a
risk-neutral single-factor futures model with explicit first-nearby WTI fixing
and posterior integration. No dataset or price row is included publicly.

## Last completed step
Copied 18 reusable library modules, 39 experiment entry-point scripts and
9 core tests from original commit `077c9e61ae4da91a5f42c4f040a3975a1360f57b`
with a clean public Git history. Exported the synthetic mechanism figure and
the clean S1–S4 supplement (historical drafting archive excluded).

## Public test confirmation
The first public CI run on source import (6595ce7b1e75173fd020503d906c0cec361d1777)
passed the public-data scanner, installation and **46 core numerical tests**.
A second lightweight example is now included and tested in CI.

## Next tasks
1. Verify the public CI installation/imports and all core tests.
2. Audit public files for hardcoded paths, secrets, arrays copied from market
   sources, and dependencies that assume private results.
3. Verify published research numbers from the private source; full numerical
   verification is a separate task.
4. Select software license with author's approval.
5. Ensure the journal's double-blind policy is addressed before citing this
   author-identifying repository/DOI in a reviewer manuscript.
6. In Zenodo, connect this GitHub repo, enable GitHub archiving, create a
   verified manual GitHub release, then record the **real DOI** and cite it.

## Never claim
A GitHub repository URL alone does not have a Zenodo DOI; the Zenodo record
does not exist until an actual deposit/release. Public code without licensed
input data does not reproduce the entire empirical dataset automatically.
