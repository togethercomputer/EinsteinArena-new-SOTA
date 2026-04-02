# New State-of-the-Art on Hexagon Packing in a Hexagon (n = 12)

We improve the `hexagon-packing` benchmark from [Einstein Arena](https://einsteinarena.com): pack 12 disjoint unit regular hexagons inside a larger regular hexagon while minimizing the outer side length.

---

## Problem Statement

Submit `hexagons` (12 triples `[cx, cy, angle_deg]`), `outer_side_length`, `outer_center`, and `outer_angle_deg`.

The verifier matches `einstein-arena/web/src/lib/problems/hexagon-packing.ts` and returns

$$\text{score} = \text{outer side length} + 100 \cdot \text{penalty},$$

where each overlap between inner hexagons and each inner hexagon that is not fully contained in the outer hexagon contributes to the penalty. Lower is better.

### Verification

The notebook [`analysis.ipynb`](analysis.ipynb) loads the Einstein Arena baseline plus our candidate and recomputes both scores locally with the same verifier logic.

---

## Results Comparison

| Method | Source | Date | Score (lower is better) |
|--------|--------|------|------------------------:|
| AlphaEvolve V2 | [Georgiev et al.](https://arxiv.org/abs/2511.02864); `einstein-arena/web/data/baselines/alphaevolve.json` | Nov 2025 | 3.9419123 |
| **Ours** | This repo (`solutions/ours_2026.json`) | Apr 2026 | **3.9416523** |

Improvement over the AlphaEvolve baseline: `-0.0002600`.

---

## References

- B. Georgiev, J. Gomez-Serrano, T. Tao, L. Wagner, "Mathematical exploration and discovery at scale," *arXiv:2511.02864*, 2025.
