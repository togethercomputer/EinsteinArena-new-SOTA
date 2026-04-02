# New State-of-the-Art on the Heilbronn Problem for Convex Regions (n = 14)

We improve the `heilbronn-convex` benchmark from [Einstein Arena](https://einsteinarena.com): place 14 points in the plane to maximize the minimum triangle area, normalized by the area of the convex hull.

---

## Problem Statement

Submit `points` as an array of 14 coordinate pairs `[x, y]`. The score is

$$
\frac{\min_{1 \le i < j < k \le 14} \operatorname{area}(p_i, p_j, p_k)}{\operatorname{area}(\operatorname{conv}(p_1, \dots, p_{14}))}.
$$

The verifier matches `einstein-arena/web/src/lib/problems/heilbronn-convex.ts`. Higher is better, and degenerate point sets receive `-inf`.

### Verification

The notebook [`analysis.ipynb`](analysis.ipynb) loads the AlphaEvolve baseline plus our candidate and recomputes both scores locally with the same objective.

---

## Results Comparison

| Method | Source | Date | Score (higher is better) |
|--------|--------|------|-------------------------:|
| AlphaEvolve V2 | [Georgiev et al.](https://arxiv.org/abs/2511.02864); `einstein-arena/web/data/baselines/alphaevolve.json` | Nov 2025 | 0.0278355715 |
| **Ours** | This repo (`solutions/ours_2026.json`) | Apr 2026 | **0.0278355805** |

Improvement over the AlphaEvolve baseline: `+0.0000000091`.

---

## References

- B. Georgiev, J. Gomez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.
