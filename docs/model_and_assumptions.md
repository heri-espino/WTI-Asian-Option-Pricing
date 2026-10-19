# Model and assumptions

The model is intentionally simple so posterior integration and the source of volatility information can be distinguished.

## Historical inference under the physical measure

For daily log returns, the baseline Gaussian likelihood uses

\[
R_i\sim\mathcal N\big((\mu-\tfrac12\sigma^2)\Delta t,\;\sigma^2\Delta t\big).
\]

The paper specifies prior distributions for drift and volatility and studies the posterior of volatility. It integrates drift analytically for the large synthetic experiment and uses random-walk Metropolis for empirical posterior inference.

## Risk-neutral futures and Asian-option pricing

The benchmark treats each maturity-specific WTI futures contract as driven by one shared Brownian shock under the risk-neutral measure:

\[
dF_t^u=\sigma F_t^u\,dW_t^Q.
\]

This is a **perfect instantaneous correlation** benchmark and not a claim that WTI futures curves behave this way in reality. Physical drift never enters risk-neutral pricing.

For the calendar-month Asian average, already-known first-nearby CL fixings are retained. Only unresolved dates are simulated/priced using contemporaneous maturity-specific futures curve inputs. Contract switches and last-trade dates must be mapped explicitly.

## Distinct uncertainty objects

1. Posterior-integrated point price: \(C_{\mathrm{PI}}=\mathbb E[C^Q(\sigma)\mid\mathcal D]\).
2. Plug-in point price: \(C_{\mathrm{PM}}=C^Q(\mathbb E[\sigma\mid\mathcal D])\).
3. Posterior distribution of **theoretical model prices**, which is not a market-price predictive interval.

Locally, the PI–PM difference is linked to option-price curvature and posterior volatility variance, whereas the dispersion of conditional model values has a first-order dependence on posterior standard deviation.

## Interpretation limits

The empirical price comparisons use Barchart settlement marks, some with zero volume; the largest APO panel covers only 15 valuation dates. Implied volatility is an *effective pricing input under the maintained model*, not by itself an identified variance risk premium or a unique risk-neutral diffusion parameter. No general dominance claim is made for all models and markets.
