# open-problem-bounds

New state-of-the-art results on open problems in combinatorics and harmonic analysis, obtained by AI agents.

## Problems

| Problem | Objective | Our Result | Previous Best | Improvement |
|---------|-----------|-----------|---------------|-------------|
| [Erdős' Minimum Overlap](erdos-minimum-overlap/) | minimize | **0.380871** | 0.380876 | −0.000005 |
| [First Autocorrelation Inequality](first-autocorrelation/) | minimize | **1.50286286** | 1.50286290 | −0.00000004 |
| [Second Autocorrelation Inequality](second-autocorrelation/) | maximize | **0.961206** | 0.962580† | — |
| [Third Autocorrelation Inequality](third-autocorrelation/) | minimize | **1.454555** | 1.455643 | −0.001088 |

†ImprovEvolve ([arXiv:2602.10233](https://arxiv.org/abs/2602.10233)) reports 0.96258, but the solution is not publicly available. The previous publicly available best is 0.961021 from [AlphaEvolve's repo](https://github.com/google-deepmind/alphaevolve_repository_of_problems/blob/main/experiments/autocorrelation_problems/autocorrelation_problems.ipynb).

Each folder contains:
- **README.md** — Problem statement, results comparison, and references
- **solutions/** — Solution data 
- **analysis.ipynb** — Verification and visualization

