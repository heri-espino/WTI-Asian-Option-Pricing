"""Small reproducible illustration of posterior integration versus plug-in pricing.

No market data or posterior-inference claim: the volatility scenarios below are
deliberately illustrative. The market-paper estimates are not recreated here.
"""
from __future__ import annotations

import numpy as np
from bayesian_asian_options.asian_pricing import (
    asian_arithmetic_call_mc,
    posterior_price_samples,
)


def main() -> None:
    # Illustrative values only: NOT a fitted WTI posterior or empirical result.
    rng = np.random.default_rng(20261018)
    volatility_scenarios = np.exp(rng.normal(np.log(0.30), 0.12, size=21))
    inputs = dict(S0=100.0, K=100.0, r=0.03, T=0.5, n_steps=24)

    values = posterior_price_samples(
        volatility_scenarios,
        **inputs,
        n_paths=4_000,
        seed=20261018,
    )
    posterior_integrated = float(np.mean(values))
    mean_volatility = float(np.mean(volatility_scenarios))
    posterior_mean_plugin = asian_arithmetic_call_mc(
        **inputs,
        sigma=mean_volatility,
        n_paths=4_000,
        seed=20261018,
    ).price

    assert np.isfinite(posterior_integrated)
    assert np.isfinite(posterior_mean_plugin)
    print(f"Mean scenario volatility: {mean_volatility:.4f}")
    print(f"Average conditional Q price (PI illustration): {posterior_integrated:.6f}")
    print(f"Q price at mean volatility (PM illustration): {posterior_mean_plugin:.6f}")
    print(f"Difference (PI minus PM): {posterior_integrated-posterior_mean_plugin:+.6f}")
    print("Illustrative scenarios only; not an empirical posterior or paper statistic.")


if __name__ == "__main__":
    main()
