import numpy as np

def p_variation(returns, p=2.0):
    increments = np.diff(returns)
    if len(increments) == 0:
        return 0.0
    var = np.sum(np.abs(increments) ** p)
    return var / max(len(increments), 1)

def rough_path_score(returns, p=2.0, threshold=0.5, invert=False):
    pvar = p_variation(returns, p)
    if not np.isfinite(pvar):
        pvar = 0.0
    if invert:
        score = 1.0 / (1.0 + pvar) if pvar >= 0 else 0.0
    else:
        score = pvar
    return score
