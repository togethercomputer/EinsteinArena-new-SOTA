# New State-of-the-Art on the Kissing Number Problem (d = 11)

We improve the **kissing number** lower bound in dimension 11: place non-overlapping unit spheres touching a central unit sphere in $\mathbb{R}^{11}$, maximizing the count.

---

## Problem Statement

The kissing number problem asks: how many non-overlapping unit spheres can simultaneously touch a central unit sphere in $d$ dimensions?

---

## Results Comparison

| Method | Source | Date | Kissing number lower bound |
|--------|--------|------|---------------------------:|
| Ganzhinov | [arXiv:2207.08266](https://arxiv.org/abs/2207.08266) | Jul 2022 | 592 |
| AlphaEvolve | [Georgiev et al.](https://arxiv.org/abs/2511.02864) | Nov 2025 | 593 |
| **Ours (v1)** | `solutions/ours_2026.json` | Apr 2026 | **594** |
| **Ours (v2)** | `solutions/solution_n=604_d=11.json` | Apr 2026 | **604** |

---

## Solutions

### v1: 594 vectors in $\mathbb{R}^{11}$ (`solutions/ours_2026.json`)

594 non-zero vectors verified with 80-digit decimal arithmetic: $\min_{i < j} \|v_i - v_j\|^2 \geq \max_i \|v_i\|^2$, confirming zero overlap without floating-point error.

### v2: 604 vectors in $\mathbb{Z}[\sqrt{2}]^{11}$ (`solutions/solution_n=604_d=11.json`)

604 vectors over $\mathbb{Z}[\sqrt{2}]$, each encoded by 22 integers $[p_0, q_0, \ldots, p_{10}, q_{10}]$ where coordinate $k$ is $p_k + q_k\sqrt{2}$. All vectors are scaled so that $\|x\|^2 = 36$. Verified with **pure integer arithmetic** (zero floats, zero tolerance): for all $i < j$, $\|x_i - x_j\|^2 \geq 36$ (equivalently, $\langle x_i, x_j \rangle \leq 18$).

This certifies $k(11) \geq 604$.

Full verification of both solutions is in [`analysis.ipynb`](analysis.ipynb).

---

## References

- **AlphaEvolve** — [Georgiev et al.](https://arxiv.org/abs/2511.02864): B. Georgiev, J. Gómez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.
- **Ganzhinov** — [arXiv:2207.08266](https://arxiv.org/abs/2207.08266): M. Ganzhinov, "New kissing numbers in dimensions 25 to 31," 2022.
