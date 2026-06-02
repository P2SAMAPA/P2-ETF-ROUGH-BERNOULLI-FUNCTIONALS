import numpy as np

def p_variation(returns, p=2.0):
    increments = np.diff(returns)
    if len(increments) == 0:
        return 0.0
    var = np.sum(np.abs(increments) ** p)
    return var / len(increments)

def bernoulli_functional(returns, threshold=0.5):
    increments = np.diff(returns)
    if len(increments) == 0:
        return 0.0
    return np.mean(np.abs(increments) > threshold)

def rough_path_score(returns, p=2.0, threshold=0.5, invert=False):
    """
    Compute roughness score (p-variation) or smoothness if invert=True.
    `threshold` is kept for API consistency with Bernoulli functional.
    """
    pvar = p_variation(returns, p)
    if invert:
        # smoothness (low roughness)
        score = 1.0 / (1.0 + pvar)
    else:
        # roughness
        score = pvar
    return score
