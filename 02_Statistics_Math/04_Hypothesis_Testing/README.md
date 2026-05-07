# Section 04 — Hypothesis Testing

Null hypothesis significance testing, t-tests, effect sizes, Type I and II errors, and resampling methods.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_effect_sizes.ipynb` | Effect sizes — Cohen's d, practical vs statistical significance |
| `02_experimental_design.ipynb` | Experimental design — control groups, randomisation, confounders |
| `03_hypothesis_testing_intro.ipynb` | Section introduction |
| `04_hypothesis_testing_section_recap.ipynb` | Section recap |
| `05_one_sample_t_tests_lab.ipynb` | One-sample t-test lab |
| `06_p_values_and_null_hypothesis.ipynb` | p-values and the null hypothesis |
| `07_resampling_methods_lab.ipynb` | Resampling methods lab |
| `08_resampling_methods.ipynb` | Bootstrap and permutation tests |
| `09_t_tests.ipynb` | One-sample and two-sample t-tests |
| `10_two_sample_t_tests_lab.ipynb` | Two-sample t-test lab |
| `11_type_1_and_2_error_lab.ipynb` | Type I and II error lab |
| `12_type_1_and_2_error.ipynb` | Type I error (false positive) and Type II error (false negative) |

## 2026 Context

**p-values:** A p < 0.05 result is not automatically meaningful — always pair with effect size and power analysis. p-values are widely misused; they indicate the probability of observing data this extreme under the null, not the probability that the null is true.

**Causal inference:** Hypothesis testing tells you whether an effect exists. It does not tell you why, or what would happen if you intervened. Causal inference is the field that answers those questions — key tools are Potential Outcomes frameworks, DAGs (directed acyclic graphs), Difference-in-Differences, and Instrumental Variables. Python libraries: `dowhy`, `causalml`, `econml`.