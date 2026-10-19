# Online Supplement — Detailed Design and Robustness Evidence

This supplement contains the evidence intentionally omitted from the compact main manuscript.
Sections S1--S4 are the stable locations cited by the paper. This public
supplement omits the historical drafting archive and all vendor market records.

## S1. Complete historical-volatility benchmarks

Table S1 gives the complete pooled comparison on the same 2,381 out-of-sample APO
contract-date observations and 15 target dates. The rolling-window and EWMA choices were fixed
before inspecting their pricing errors. MAE and RMSE are in U.S. dollars per barrel.

**Table S1. Historical-volatility and prior option-implied volatility benchmarks.**

| Volatility input | N | Dates | MAE | RMSE |
| --- | ---: | ---: | ---: | ---: |
| Long-window historical PI | 2,381 | 15 | 2.6187 | 3.4090 |
| Rolling 252 returns | 2,381 | 15 | 5.2183 | 6.3933 |
| Rolling 126 returns | 2,381 | 15 | 8.3419 | 9.7846 |
| Rolling 63 returns | 2,381 | 15 | 4.5201 | 5.6465 |
| EWMA, half-life 63 days | 2,381 | 15 | 5.6616 | 6.8824 |
| Horizon-matched GARCH(1,1) | 2,381 | 15 | 2.6730 | 3.4441 |
| Earlier-date APO expanding smile | 2,381 | 15 | 0.1088 | 0.1725 |
| Previous-day APO smile | 2,381 | 15 | 0.1075 | 0.1594 |

The GARCH fit is estimated from earlier returns. The target-date return updates only the
end-of-day conditional variance state; parameters are not re-estimated with that return.
Forecast conditional variances are accumulated over each remaining fixing horizon and mapped
to the maintained common-factor constant-volatility APO representation.

## S2. Numerical accuracy and posterior calibration

The empirical PI--PM differences are small, so the numerical audit compares high-precision
pseudo-random Monte Carlo, independently scrambled Sobol pricing, and Curran conditioning.
Across the difficult targets, differences among the three PI--PM estimates are on the order of
micro-dollars, well below the empirical gaps near (10^{-3}) dollars per barrel.

As an additional scalar-volatility sensitivity, we compare pricing at posterior mean volatility with pricing at posterior root mean square (RMS) volatility,
$\sigma_{\mathrm{RMS}}=\sqrt{\mathbb E[\sigma^2\mid\mathcal D]}$, using the same Curran approximation for both. Their pooled pricing errors differ only slightly. This plug-in comparison does not substitute for averaging conditional prices over the posterior (PI).

**Table S2. Numerical identification and simulation-based calibration.**

**Panel A. Representative PI--PM differences (U.S. dollars per barrel).**

| Target | Pseudo-MC | Curran | Scrambled Sobol |
| --- | ---: | ---: | ---: |
| 2026-08-27, October call, K=98 | 0.0013683 | 0.0013690 | 0.0013717 |
| 2026-08-28, October call, K=98 | 0.0013394 | 0.0013402 | 0.0013393 |

**Panel B. Simulation-based calibration of the Gaussian volatility posterior.**

| Historical observations n | Mean posterior rank | KS p-value | Empirical 95% coverage |
| ---: | ---: | ---: | ---: |
| 21 | 0.5000 | 0.861 | 0.9500 |
| 63 | 0.4993 | 0.348 | 0.9505 |
| 252 | 0.4978 | 0.210 | 0.9483 |
| 1,260 | 0.5027 | 0.106 | 0.9505 |

The numerical comparison establishes practical resolution of the PI--PM difference; it does not
imply that Curran and Monte Carlo produce identical absolute option prices. The calibration
experiment uses 200,000 prior-predictive datasets in total, with 50,000 replications at each
sample size.

## S3. Liquidity and valuation-date dependence

Contracts observed on the same valuation date share the futures curve, historical posterior,
and market environment. Error differences are therefore resampled by valuation-date cluster.
The qualitative ranking also persists under transaction-activity and open-interest restrictions.

**Table S3. Positive-volume out-of-sample comparison.**

| Volatility input | N | Target-date clusters | MAE | RMSE |
| --- | ---: | ---: | ---: | ---: |
| Historical PI | 62 | 13 | 1.6340 | 2.3391 |
| Earlier-date APO expanding smile | 62 | 13 | 0.1003 | 0.1358 |
| Previous-day APO smile | 62 | 13 | 0.1084 | 0.1333 |

The same direction is preserved at open-interest thresholds of 10, 100, and 500 contracts.
At open interest of at least 100, the option-implied MAEs are approximately 0.106--0.107
versus 1.990 for the historical benchmark. Long-dated positive-volume observations remain
sparse within individual expiries, so maturity-specific transaction-price interpretation is
more limited than the pooled comparison.

## S4. Vanilla-WTI transfer and CRR refinement

The external LO validation uses a fixing-count weighted RMS mapping as its primary transfer from
maturity-specific vanilla-WTI implied volatilities to the scalar volatility required by the
maintained APO pricing model. A second mapping chooses the scalar volatility that matches the
variance of the unresolved arithmetic-average component under the same common-factor
representation.

**Table S4. LO scalar-transfer and tree-refinement diagnostics.**

**Panel A. Alternative LO scalar mapping on the 253-observation common-support sample.**

| Specification | MAE | RMSE |
| --- | ---: | ---: |
| Previous-day LO, primary weighted-RMS mapping | 0.1559 | 0.2599 |
| Previous-day LO, variance-matched mapping | 0.1562 | 0.2612 |
| Expanding LO, primary weighted-RMS mapping | 0.1604 | 0.2858 |
| Expanding LO, variance-matched mapping | 0.1611 | 0.2869 |

**Panel B. Absolute LO implied-volatility changes under CRR refinement.**

| Refinement | Mean | Median | 95th percentile | Maximum |
| --- | ---: | ---: | ---: | ---: |
| 80 to 160 steps | 0.000820 | — | — | — |
| 160 to 320 steps | 0.000402 | 0.000284 | 0.001089 | 0.001810 |

The refinement audit contains 156 stratified LO contract-dates. It establishes practical
stability of the production 160-step inversion at the precision relevant for the external
comparison; it is not a proof of an exact infinite-tree limit. A separate strictly-prior
surface-shape audit contains 144 diagnostics over 12 dates, with no nonpositive or nonfinite
fitted volatilities inside observed prior support and at most one direction change in the fitted
curves.

---
