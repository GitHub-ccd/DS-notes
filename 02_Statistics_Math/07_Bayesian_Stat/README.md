# Section 07 — Bayesian Statistics

Bayes' theorem, MLE, MAP estimation, and the Bayesian vs frequentist distinction.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_bayes_theorem_lab.ipynb` | Bayes' theorem lab |
| `02_bayes_theorem.ipynb` | Bayes' theorem — prior, likelihood, posterior |
| `03_bayesian_stats_introduction.ipynb` | Section introduction |
| `04_bayesian_stats_recap.ipynb` | Section recap |
| `05_bayesians_vs_frequentists.ipynb` | Bayesian vs frequentist interpretation of probability |
| `06_map_multinomial_bayes.ipynb` | MAP estimation and multinomial Bayes |
| `07_mle.ipynb` | Maximum likelihood estimation |
| `08_monty_hall_problem_lab.ipynb` | Monty Hall problem lab |

## 2026 Context

Bayesian thinking is increasingly relevant in 2026 — both in classical statistics and as the theoretical backbone of LLM probabilistic reasoning. For practical Bayesian modelling (defining a prior, observing data, sampling the posterior), the modern tool is **PyMC v5** (formerly PyMC3). It lets you define probabilistic models in Python and sample posteriors via MCMC or variational inference. `pip install pymc`