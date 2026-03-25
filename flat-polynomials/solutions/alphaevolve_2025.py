"""
±1 coefficients for the degree-69 flat polynomial benchmark (AlphaEvolve V2 baseline).

Source: B. Georgiev, J. Gómez-Serrano, T. Tao, L. Wagner, "Mathematical exploration
        and discovery at scale," arXiv:2511.02864 — reproduced in
        einstein-arena/web/data/baselines/alphaevolve.json ("flat-polynomials").
Score: C+ = 1.3409252794557085 under the Einstein Arena verifier (1e6 samples on |z|=1).
"""

import numpy as np

coefficients = np.array([
    1, 1, -1, -1, -1, 1, 1, 1, 1, -1,
    -1, -1, 1, 1, -1, -1, -1, -1, 1, -1,
    1, 1, 1, 1, -1, 1, 1, 1, -1, 1,
    1, -1, -1, -1, -1, -1, -1, 1, -1, 1,
    1, -1, -1, -1, -1, -1, -1, -1, 1, -1,
    1, -1, -1, 1, -1, -1, 1, -1, -1, 1,
    1, -1, 1, 1, 1, -1, 1, -1, 1, -1,
], dtype=np.int8)
