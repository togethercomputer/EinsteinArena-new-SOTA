"""
Improved ±1 coefficients (Mar 2026).

Construction: 71-bit PSL-optimal code 0x12493BE76A5EE2A3F1, mapped to ±1 and truncated to
70 coefficients for np.poly1d (z^69 … constant). See also
`chasing_sota/flat-polynomials/flat_polynomials_1290049.py`.

Score: C+ = 1.2809320527987995 under the Einstein Arena verifier (1e6 samples on |z|=1).
"""

import numpy as np

coefficients = np.array([
    -1, -1, 1, -1, -1, 1, -1, -1, 1, -1,
    -1, 1, -1, -1, 1, -1, -1, 1, 1, 1,
    -1, 1, 1, 1, 1, 1, -1, -1, 1, 1,
    1, -1, 1, 1, -1, 1, -1, 1, -1, -1,
    1, -1, 1, 1, 1, 1, -1, 1, 1, 1,
    -1, -1, -1, 1, -1, 1, -1, 1, -1, -1,
    -1, 1, 1, 1, 1, 1, 1, -1, -1, -1,
], dtype=np.int8)
