import numpy as np
from scipy.special import comb

def p_variation(series, p=2):
    """
    Compute p‑variation of a 1D time series.
    p=2 gives quadratic variation (realised variance).
    """
    if len(series) < 2:
        return 0.0
    diff = np.diff(series)
    if p == 2:
        # quadratic variation
        return np.sum(diff**2)
    else:
        return np.sum(np.abs(diff)**p)

def bernoulli_functional(signature, functional='exp'):
    """
    Apply a Bernoulli functional to the signature (simplified: use the signature's first level).
    For this engine, we use the p‑variation as the score directly.
    """
    # For simplicity, we just return the p‑variation as the score
    return signature

def rough_path_score(returns, p=2):
    """
    Compute the p‑variation of the return series as a roughness measure.
    """
    ret_series = returns.dropna().values
    if len(ret_series) < 2:
        return 0.0
    var = p_variation(ret_series, p)
    # Normalise by length to avoid scale dependence
    var = var / len(ret_series)
    return var
