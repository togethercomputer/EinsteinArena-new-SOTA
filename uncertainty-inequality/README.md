# New State-of-the-Art on the Uncertainty Inequality

We let AI agents tackle an open problem in harmonic analysis — the **uncertainty inequality** — and obtained a new state-of-the-art upper bound using the Laguerre LP framework. Details on the method will come in a forthcoming write-up.

---

## Problem Statement

Given a function $f: \mathbb{R}\rightarrow \mathbb{R}$, define the Fourier transform $\widehat{f}(\xi) := \int_\mathbb{R} f(x) e^{-2\pi i x\xi} dx$ and

$$A(f) := \inf \lbrace r > 0: f(x) \geq 0 \text{ for all } |x| \geq r \rbrace.$$

Let $C_4$ be the largest constant satisfying

$$A(f) A(\widehat{f}) \geq C_4$$

for all even $f$ with $\max(f(0), \widehat{f}(0)) < 0$.

### Methods

Two polynomial construction approaches have been used to obtain upper bounds:

**Hermite method** ([Gonçalves et al., 2017](https://www.sciencedirect.com/science/article/pii/S0022247X17301804)). Construct $P(x) = \sum_{k=0}^{m} c_k H_{4k}(x)$ with the constraint $P(0) = 0$. The upper bound is the largest sign-change root of $P(x)/x^2$, squared, divided by $2\pi$.

**Laguerre LP method** ([Cohn & Gonçalves, 2019](https://arxiv.org/abs/1712.04438)). Prescribe $k$ double root positions $z_1, \ldots, z_k > 0$ and construct $g(x) = \sum_j \alpha_j L_j^{(-1/2)}(x)$ (generalized Laguerre polynomials of even degree) subject to $g(0) = 0$, $g'(0) = 1$, and $g(z_i) = g'(z_i) = 0$. The upper bound is the largest sign-change root of $g(x) / (x \prod_i (x - z_i)^2)$, divided by $2\pi$.

---

## Results Comparison

| Method | Source | Date | Approach | Upper Bound (lower is better) |
|--------|--------|------|----------|------:|
| Gonçalves et al. | [Gonçalves et al. (2017)](https://www.sciencedirect.com/science/article/pii/S0022247X17301804) | 2017 | Hermite (3 coefficients) | 0.3523 |
| AlphaEvolve | [Novikov et al. (2025)](https://arxiv.org/abs/2506.13131) | June 2025 | Hermite (3 coefficients) | 0.3521 |
| AlphaEvolve V2 | [Georgiev et al. (2025)](https://arxiv.org/abs/2511.02864) | Nov 2025 | Laguerre LP (6 coefficients) | 0.3283 |
| **Ours (Together AI)** | This repo | Mar 2026 | Laguerre LP (13 double roots) | **0.3189** |

For full verification, see [`analysis.ipynb`](analysis.ipynb).

---

## References

- D. Gonçalves, F. Oliveira e Silva, S. Steinerberger, "Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots," *J. Math. Anal. Appl.*, 2017.
- H. Cohn, F. Gonçalves, "An optimal uncertainty principle in twelve dimensions via modular forms," *Forum Math. Pi*, 2019. [arXiv:1712.04438](https://arxiv.org/abs/1712.04438).
- Novikov et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery," *arXiv:2506.13131*, 2025.
- B. Georgiev, J. Gómez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.

