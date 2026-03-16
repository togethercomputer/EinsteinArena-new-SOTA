"""
Step function construction found by AlphaEvolve (Google DeepMind, May 2025).

Source: Georgiev, Gomez-Serrano, Tao, Wagner (2025)
        https://arxiv.org/abs/2511.02864
Colab:  https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb
Upper bound: C_5 <= 0.380924
Number of steps: 95
"""

import numpy as np

ae_half = np.array([
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 3.60911302e-10, 3.62124044e-10, 4.02849974e-12,
    4.47352578e-12, 4.76914172e-12, 0.506074303,
    0.632046692, 0.679332798, 0.888193865,
    0.889214704, 0.678231235, 2.976636922840846e-07,
    0.0947643739, 0.0143926342, 0.423931858,
    0.598073612, 0.803909612, 0.683098916,
    0.314749384, 0.404059484, 0.858443734,
    0.796503042, 0.590433152, 0.41056218,
    0.270932695, 0.613384276, 0.709501647,
    0.580573615, 0.803538112, 0.715263878,
    0.822611331, 0.808433879, 0.683533985,
    0.645719012, 0.889417725, 0.943389845,
    0.841536959, 0.794505216, 0.941943428,
    0.962223227, 0.961270753, 0.992409079,
])

h_values = np.concatenate((ae_half[:-1], ae_half[::-1]))
