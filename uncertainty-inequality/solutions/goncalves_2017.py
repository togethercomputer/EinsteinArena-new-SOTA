"""
Hermite polynomial coefficients from Gonçalves et al. (2017).

Source: Gonçalves, Oliveira e Silva, Steinerberger (2017)
        https://www.sciencedirect.com/science/article/pii/S0022247X17301804
Upper bound: C_4 <= 0.3523
"""

import numpy as np

coefficients = np.array([
    -113 / 100,
    1 / 25,
    1 / 3240,
])
