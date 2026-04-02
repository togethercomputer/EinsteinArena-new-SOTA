# New State-of-the-Art on Circles in a Rectangle (n = 21)

We improve the `circles-rectangle` benchmark from [Einstein Arena](https://einsteinarena.com): pack 21 disjoint circles inside a rectangle of perimeter at most 4 while maximizing the sum of their radii.

---

## Problem Statement

Submit `circles` as an array of 21 triples `[x, y, r]`. The verifier matches `einstein-arena/web/src/lib/problems/circles-rectangle.ts` and returns

$$
\sum_{i=1}^{21} r_i
$$

provided that all radii are positive, every pair of circles is disjoint, and the bounding rectangle of all circles satisfies `width + height <= 2`. Higher is better.

### Verification

The notebook [`analysis.ipynb`](analysis.ipynb) loads the Einstein Arena baseline plus our candidate and recomputes both scores locally with the same verifier logic.

---

## Results Comparison

| Method | Source | Date | Score (higher is better) |
|--------|--------|------|-------------------------:|
| AlphaEvolve V2 | [Georgiev et al.](https://arxiv.org/abs/2511.02864); `einstein-arena/web/data/baselines/alphaevolve.json` | Nov 2025 | 2.3658321334 |
| **Ours** | This repo (`solutions/ours_2026.json`) | Apr 2026 | **2.3658323759** |

Improvement over the AlphaEvolve baseline: `+0.0000002425`.

---

## References

- B. Georgiev, J. Gomez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.
