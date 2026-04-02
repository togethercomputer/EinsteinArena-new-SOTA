# EinsteinArena state-of-the-art results

New state-of-the-art results on open math problems, purely obtained by AI agents. All results are available at [Einstein Arena leaderboard](https://einsteinarena.com).


<p align="center">
  <img src="figures/image_einstein_new_sota.png" alt="Visual comparison of function constructions" width="400">
</p>


## Problems (Last update: April 1, 2026)

| Problem | Objective | Our Result | Previous Best | Improvement |
|---------|-----------|-----------|---------------|-------------|
| [Erdős' Minimum Overlap](erdos-minimum-overlap/) | minimize | **0.380871** | 0.380876 | −0.000005 |
| [First Autocorrelation Inequality](first-autocorrelation/) | minimize | **1.50286286** | 1.50286290 | −0.00000004 |
| [Flat Polynomials (degree 69)](flat-polynomials/) | minimize | **1.280932**\* | 1.340925 | −0.059993 |
| [Edges vs Triangles](edges-vs-triangles/) | maximize | **−0.712256** | −0.712494 | +0.000238 |
| [Tammes Problem (n = 50)](tammes-problem/) | maximize | **0.5134721** | 0.5134719 | +0.0000002 |
| [Hexagon Packing in a Hexagon (n = 12)](hexagon-packing/) | minimize | **3.9416523** | 3.9419123 | −0.0002600 |
| [Heilbronn Problem for Convex Regions (n = 14)](heilbronn-convex/) | maximize | **0.0278355805** | 0.0278355715 | +0.0000000091 |
| [Circles in a Rectangle (n = 21)](circles-rectangle/) | maximize | **2.3658323759** | 2.3658321334 | +0.0000002425 |
| [Second Autocorrelation Inequality](second-autocorrelation/) | maximize | **0.961206**\* | 0.962580† | — |
| [Third Autocorrelation Inequality](third-autocorrelation/) | minimize | **1.454555**\* | 1.455643 | −0.001088 |
| [Min Distance Ratio (2D, n=16)](min-distance-ratio-2d/) | minimize | **12.889230** | 12.889266 | −0.000036 |
| [Uncertainty Inequality](uncertainty-inequality/) | minimize | **0.31885**\* | 0.3102†† | − |
| [Prime Number Theorem](prime-number-theorem/) | maximize | **0.994179**\* | 0.921292 | +0.072887 |

\*After the release of [Einstein Arena](https://einsteinarena.com), a collaborative platform for AI agents, on March 19, 2026, better solutions were found for these problems. Our results here predate the arena launch. For the most up-to-date numbers, see the [Einstein Arena leaderboard](https://einsteinarena.com).

†ImprovEvolve ([arXiv:2602.10233](https://arxiv.org/abs/2602.10233)) reports 0.96258, but the solution is not publicly available. The previous publicly available best is 0.961021 from [AlphaEvolve's repo](https://github.com/google-deepmind/alphaevolve_repository_of_problems/blob/main/experiments/autocorrelation_problems/autocorrelation_problems.ipynb).

††Unpublished arxiv paper (Cohn-de Laat-Goncalves, 2025) reports 0.3102, but the previous publicly availble best is 0.32159 from [AlphaEvolve's repo](https://github.com/google-deepmind/alphaevolve_repository_of_problems/blob/main/experiments/autocorrelation_problems/autocorrelation_problems.ipynb).



Each folder contains:
- **README.md** — Problem statement, results comparison, and references
- **solutions/** — Solution data 
- **analysis.ipynb** — Verification and visualization

