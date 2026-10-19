# Experiments by research question

Experiment filenames follow the original research package so runs and model implementations remain traceable. The public package preserves their source code; it does not contain all required licensed market inputs.

| Research question | Main scripts | Required input |
| --- | --- | --- |
| When does posterior integration matter? | `experiments/massive_mechanism_map.py`, `experiments/taylor_mechanism.py` | Simulated returns |
| Is posterior inference calibrated? | `experiments/simulation_based_calibration.py` | Simulated returns |
| Are Asian option calculations numerically stable? | `experiments/wti_high_precision_pricing.py`, `experiments/wti_randomized_qmc_benchmark.py` | Configuration and, for WTI targets, licensed market curves |
| How are first-nearby WTI APO fixings priced? | `experiments/wti_apo_empirical.py`, `experiments/build_wti_apo_panel.py` | Historical Barchart APO/CL histories |
| How are forward-time volatility inputs compared? | `experiments/wti_forward_q_validation.py`, `experiments/wti_apo_implied_volatility.py` | Licensed time-stamped option panels |
| Does vanilla WTI IV transfer across option types? | `experiments/wti_external_vanilla_q_validation.py`, `experiments/wti_databento_external_q_iv.py` | Databento LO and matching CL observations |
| How sensitive are conclusions to liquidity/time clustering? | `experiments/wti_liquidity_bootstrap.py`, `experiments/wti_external_q_cluster_bootstrap.py` | Previously constructed target-date panels |

**Before running large simulations:** inspect each script's `--help`, configuration and resource requirements. Synthetic studies can be computationally intensive. Some scripts are the historical orchestration entry points and have not been revalidated on the public stripped-down layout. Never interpret a failed missing-data run as scientific evidence.

The basic checks in `tests/` exercise selected pricing and Bayesian numerical routines without purchasing data. The full private experiment audit is separate from publication of this software package.
