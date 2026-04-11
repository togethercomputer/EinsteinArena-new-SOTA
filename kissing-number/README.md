# New State-of-the-Art on the Kissing Number Problem (d = 11)

We improve the **kissing number** lower bound in dimension 11: place non-overlapping unit spheres touching a central unit sphere in $\mathbb{R}^{11}$, maximizing the count.

---

## Problem Statement

The kissing number problem asks: how many non-overlapping unit spheres can simultaneously touch a central unit sphere in $d$ dimensions?

Submit `vectors` — an array of exactly 594 non-zero vectors in $\mathbb{R}^{11}$. Each vector $x_i$ defines a direction; the verifier normalizes it and places a unit sphere at $2x_i / \|x_i\|$ (distance 2 from the origin, i.e. touching the central unit sphere).

For each pair of sphere centers at distance $d < 2$, the spheres overlap. The penalty is:

$$\text{loss} = \sum_{i < j} \max(0,\; 2 - \|c_i - c_j\|)$$

where $c_i = 2x_i / \|x_i\|$.

A score of exactly **0** means a valid kissing configuration — proof that the kissing number in dimension 11 is at least 594. The verifier uses high-precision decimal arithmetic (80-digit precision) to confirm $\min_{i < j} \|v_i - v_j\|^2 \geq \max_i \|v_i\|^2$, guaranteeing non-overlap without floating-point error.

---

## Results Comparison

| Method | Source | Date | Kissing number lower bound |
|--------|--------|------|---------------------------:|
| Ganzhinov | [arXiv:2207.08266](https://arxiv.org/abs/2207.08266) | Jul 2022 | 592 |
| AlphaEvolve | [Georgiev et al.](https://arxiv.org/abs/2511.02864) | Nov 2025 | 593 |
| **Ours** | This repo (`solutions/ours_2026.json`) | Apr 2026 | **594** |

Our construction provides **594** unit spheres in dimension 11 with zero overlap, establishing a new lower bound. The verifier confirms the configuration is valid using exact decimal arithmetic.

Full verification is in [`analysis.ipynb`](analysis.ipynb).

---

## References

- **AlphaEvolve** — [Georgiev et al.](https://arxiv.org/abs/2511.02864): B. Georgiev, J. Gómez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.
- **Ganzhinov** — [arXiv:2207.08266](https://arxiv.org/abs/2207.08266): M. Ganzhinov, "New kissing numbers in dimensions 25 to 31," 2022.
