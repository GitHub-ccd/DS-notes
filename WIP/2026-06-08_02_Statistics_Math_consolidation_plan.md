# Module 02 — Statistics & Math Consolidation Plan
*2026-06-08*

**Status: IN PROGRESS** — working section by section. Audit each section before writing notebooks.

---

## Background

Module 02 was editorially reviewed in a previous session (summaries rewritten, stale content flagged) but was **not** consolidated — it still uses the original paired lesson+lab model throughout. The same consolidation approach from Module 01 applies here.

`00_Descriptive_Statistics` was already consolidated in a prior session (8 source notebooks → 5, moved from 01/03). All remaining sections (01–11) are untouched and still in the old format.

### Same rules as Module 01

- Lesson + lab → one integrated notebook
- Section intro / recap → dropped
- Quiz / codealong → absorbed as a practice block or dropped if thin
- Target compression: ~3:1

---

## Module Structure

| Section | Approx. files | Status |
|---------|--------------|--------|
| `00_Descriptive_Statistics` | 5 | ✅ Done (prior session) |
| `01_Combinatorics_Probability` | 14 → 5 | ✅ Done |
| `02_Statistical_Distributions` | 17 → 5 | ✅ Done |
| `03_Central_Limit_Theorem` | 7 | ⬜ Pending |
| `04_Hypothesis_Testing` | 11 | ⬜ Pending |
| `05_Stat_ANOVA` | 13 | ⬜ Pending |
| `06_AB_testing` | 6 | ⬜ Pending |
| `07_Bayesian_Stat` | 8 | ⬜ Pending |
| `08_Linear_Regression` | 13 → 4 | ✅ Done |
| `09_multiple_regression` | 21 → 6 | ✅ Done |
| `10_Linear_Model_Extensions` | 8 → 3 | ✅ Done |
| `11_Appendix` | 20 → 4 | ✅ Done |
| **Total remaining** | **~138** | |

---

## Section Plans

Section plans are filled in after auditing each section's files. Audit first, plan, then execute.

---

### 01 — Combinatorics & Probability

✅ **Complete.**

**Source files (14):**

| File | Type | Topic |
|------|------|-------|
| `01_combinations_lab.ipynb` | Lab | Combinations |
| `02_combinations.ipynb` | Lesson | Combinations |
| `03_conditional_probability_lab.ipynb` | Lab | Conditional probability |
| `04_conditional_probability.ipynb` | Lesson | Conditional probability |
| `05_intro_to_probability_lab.ipynb` | Lab | Probability basics |
| `06_intro_to_probability.ipynb` | Lesson | Probability basics |
| `07_intro_to_sets_lab.ipynb` | Lab | Sets |
| `08_intro_to_sets.ipynb` | Lesson | Sets |
| `09_law_of_total_probability_lab.ipynb` | Lab | Law of total probability |
| `10_law_of_total_probability.ipynb` | Lesson | Law of total probability |
| `11_permutations_and_factorials_lab.ipynb` | Lab | Permutations & factorials |
| `12_permutations_and_factorials.ipynb` | Lesson | Permutations & factorials |
| `13_probability_introduction.ipynb` | Intro | **DROPPED** (thin section intro) |
| `16_probability_simulations_lab.ipynb` | Lab | Total probability simulations |

**New structure (5 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_sets.ipynb` | 08 + 07 | 52 |
| `02_probability_basics.ipynb` | 06 + 05 | 59 |
| `03_permutations_and_combinations.ipynb` | 12 + 11 + 02 + 01 | 76 |
| `04_conditional_probability.ipynb` | 04 + 03 | 16 |
| `05_law_of_total_probability.ipynb` | 10 + 09 + 16 | 44 |

**Result:** 14 → 5 (drop 1, consolidate 13 → 4 active = 3.25:1)

---

### 02 — Statistical Distributions

✅ **Complete.**

**Source files (17 + 1 subdirectory, dropped):**

| File | Type | Topic |
|------|------|-------|
| `01_bernoulli_and_binomial_distribution_lab.ipynb` | Lab | Bernoulli & Binomial |
| `02_bernoulli_and_binomial_distribution.ipynb` | Lesson | Bernoulli & Binomial |
| `03_cumulative_distribution_function_lab.ipynb` | Lab | CDF |
| `04_cumulative_distribution_function.ipynb` | Lesson | CDF |
| `07_normal_distribution_lab.ipynb` | Lab | Normal distribution |
| `08_normal_distribution.ipynb` | Lesson | Normal distribution |
| `09_one_sample_z_test_lab.ipynb` | Lab | One-sample z-test |
| `10_one_sample_z_test.ipynb` | Lesson | One-sample z-test |
| `11_probability_density_function.ipynb` | Lesson | PDF (no lab) |
| `12_probability_mass_function_lab.ipynb` | Lab | PMF (class size paradox) |
| `13_probability_mass_function.ipynb` | Lesson | PMF |
| `14_skewness_and_kurtosis_lab.ipynb` | Lab | Skewness & kurtosis |
| `15_skewness_and_kurtosis.ipynb` | Lesson | Skewness & kurtosis |
| `16_standard_normal_distribution_lab.ipynb` | Lab | Standard normal |
| `17_standard_normal_distribution.ipynb` | Lesson | Standard normal & z-score |
| `18_stat_distributions_use_cases.ipynb` | Conceptual | Distribution types overview |
| `19_z_score_p_value.ipynb` | Lesson | z-score, p-value, hypotheses |
| `probability-density-functions-lab-onl01-dtsc-ft-030220/` | **DROPPED** | Old Learn.co artifact |

**New structure (5 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_distribution_functions.ipynb` | 18 + 13 + 12 + 11 + 04 + 03 | 81 |
| `02_bernoulli_and_binomial.ipynb` | 02 + 01 | 36 |
| `03_normal_distribution.ipynb` | 08 + 07 + 17 + 16 | 41 |
| `04_skewness_and_kurtosis.ipynb` | 15 + 14 | 12 |
| `05_z_test_and_hypothesis_testing.ipynb` | 19 + 10 + 09 | 22 |

**Result:** 17 → 5 (drop 1 dir, consolidate 17 → 5 = 3.4:1)

---

### 03 — Central Limit Theorem

✅ **Complete.** Commit: `7aeee85`

**Source files (7):**

| File | Type | Topic |
|------|------|-------|
| `01_central_limit_theorem_lab.ipynb` | Lab | CLT practice |
| `02_central_limit_theorem.ipynb` | Lesson | CLT theory |
| `03_confidence_intervals_lab.ipynb` | Lab | Confidence intervals |
| `06_intervals_with_t_distribution_lab.ipynb` | Lab | t-distribution intervals |
| `07_intervals_with_t_distribution.ipynb` | Lesson | t-distribution intervals |
| `08_introduction_to_sampling.ipynb` | Lesson | Sampling intro |
| `09_sampling_statistics_lab.ipynb` | Lab | Sampling statistics |

**New structure (3 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_central_limit_theorem.ipynb` | 08 + 02 + 01 + 09 | 70 |
| `02_confidence_intervals.ipynb` | 03 | 22 |
| `03_t_distribution_intervals.ipynb` | 07 + 06 | 37 |

**Result:** 7 → 3 (2.3:1)

---

### 04 — Hypothesis Testing

✅ **Complete.** Commit: `11bac2d`

**Source files (11):**

| File | Type | Topic |
|------|------|-------|
| `01_effect_sizes.ipynb` | Lesson | Effect size |
| `02_experimental_design.ipynb` | Lesson | Experimental design |
| `03_hypothesis_testing_intro.ipynb` | Intro | **DROPPED** |
| `05_one_sample_t_tests_lab.ipynb` | Lab | One-sample t-test |
| `06_p_values_and_null_hypothesis.ipynb` | Lesson | P-values |
| `07_resampling_methods_lab.ipynb` | Lab | Resampling |
| `08_resampling_methods.ipynb` | Lesson | Resampling |
| `09_t_tests.ipynb` | Lesson | T-tests |
| `10_two_sample_t_tests_lab.ipynb` | Lab | Two-sample t-test |
| `11_type_1_and_2_error_lab.ipynb` | Lab | Type I/II errors |
| `12_type_1_and_2_error.ipynb` | Lesson | Type I/II errors |

**New structure (5 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_hypothesis_testing_foundations.ipynb` | 02 + 06 | 3 |
| `02_effect_size.ipynb` | 01 | 57 |
| `03_t_tests.ipynb` | 09 + 05 + 10 | 43 |
| `04_type_1_and_2_errors.ipynb` | 12 + 11 | 35 |
| `05_resampling_methods.ipynb` | 08 + 07 | 15 |

**Result:** 11 → 5 (drop 1, consolidate 10 → 5 = 2.2:1)

---

### 05 — ANOVA & Statistical Power

✅ **Complete.** Commit: `cd20183`

**Source files (13):**

| File | Type | Topic |
|------|------|-------|
| `01_anova_lab.ipynb` | Lab | ANOVA |
| `02_anova.ipynb` | Lesson | ANOVA |
| `03_effect_sizes_pvalues_and_power_lab.ipynb` | Lab | Effect size + power simulations |
| `04_goodharts_law_and_metric_tracking.ipynb` | Conceptual | Goodhart's law |
| `05_kolmogorov_smirnov_test.ipynb` | Lesson | KS test |
| `06_komogorov_smirnov_test_lab.ipynb` | Lab | KS test |
| `07_multiple_comparisons_problem.ipynb` | Lesson | Multiple comparisons |
| `08_statistical_power_anova_introduction.ipynb` | Intro | **DROPPED** |
| `09_statistical_power_anova_recap.ipynb` | Recap | **DROPPED** |
| `10_statistical_power_lab.ipynb` | Lab | Statistical power |
| `11_statistical_power.ipynb` | Lesson | Statistical power |
| `12_welchs_ttest_lab.ipynb` | Lab | Welch's t-test |
| `13_welchs_ttest.ipynb` | Lesson | Welch's t-test |

**New structure (5 notebooks):**

| New file | Sources | Notes |
|----------|---------|-------|
| `01_anova.ipynb` | 02 + 01 | ANOVA lesson + lab |
| `02_statistical_power.ipynb` | 11 + 10 + 03 | Power lesson + two practice labs |
| `03_welchs_ttest.ipynb` | 13 + 12 | Welch's t-test lesson + lab |
| `04_ks_test.ipynb` | 05 + 06 | KS test lesson + lab |
| `05_multiple_comparisons.ipynb` | 07 + 04 | Multiple comparisons + Goodhart's law |

**Result:** 13 → 5 (drop 2, consolidate 11 → 5 = 2.2:1)

---

### 06 — A/B Testing

✅ **Complete.** Commit: `c3ec1c9`

**Source files (6):**

| File | Type | Topic |
|------|------|-------|
| `01_ab_testing_introduction.ipynb` | Intro | **DROPPED** |
| `02_ab_testing_lab.ipynb` | Lab | A/B testing basic lab |
| `03_ab_testing.ipynb` | Lesson | A/B testing theory |
| `04_ab_testing_recap.ipynb` | Recap | **DROPPED** |
| `05_in_depth_ab_testing_lab.ipynb` | Lab | In-depth Kaggle survey lab |
| `06_website_ab_testing_lab.ipynb` | Lab | Website conversion lab |

**New structure (2 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_ab_testing.ipynb` | 03 + 02 | 15 |
| `02_ab_testing_advanced.ipynb` | 05 + 06 | 34 |

**Result:** 6 → 2 (drop 2, consolidate 4 → 2 = 2:1)

---

### 07 — Bayesian Statistics

✅ **Complete.** Commit: `b68e550`

**Source files (8):**

| File | Type | Topic |
|------|------|-------|
| `01_bayes_theorem_lab.ipynb` | Lab | Bayes theorem |
| `02_bayes_theorem.ipynb` | Lesson | Bayes theorem |
| `03_bayesian_stats_introduction.ipynb` | Intro | **DROPPED** |
| `04_bayesian_stats_recap.ipynb` | Recap | **DROPPED** |
| `05_bayesians_vs_frequentists.ipynb` | Conceptual | Frequentist vs Bayesian |
| `06_map_multinomial_bayes.ipynb` | Lesson | MAP + Multinomial Bayes |
| `07_mle.ipynb` | Lesson | MLE (28 cells) |
| `08_monty_hall_problem_lab.ipynb` | Lab | Monty Hall problem |

**New structure (3 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_bayes_theorem.ipynb` | 02 + 01 | 12 |
| `02_bayesian_inference.ipynb` | 05 + 06 | 3 |
| `03_mle.ipynb` | 07 + 08 | 30 |

**Result:** 8 → 3 (drop 2, consolidate 6 → 3 = 2:1)

---

### 08 — Linear Regression

✅ **Complete.** Commit: `39dc5af`

**Source files (13):**

| File | Type | Topic |
|------|------|-------|
| `01_coefficient_of_determination_lab.ipynb` | Lab | R-squared |
| `02_coefficient_of_determination.ipynb` | Lesson | R-squared |
| `03_complete_regression_lab.ipynb` | Lab | Complete regression from scratch |
| `06_ols_regression_diagnostics.ipynb` | Lesson | OLS diagnostics |
| `07_ols_statsmodels_lab.ipynb` | Lab | OLS with statsmodels |
| `08_ols_statsmodels.ipynb` | Lesson | OLS with statsmodels |
| `09_regression_assumptions.ipynb` | Lesson | Regression assumptions |
| `10_regression_boston_lab.ipynb` | Lab | **DROPPED** (blank duplicate of 11) |
| `11_regression_boston_lab.ipynb` | Lab | Boston housing diagnostics |
| `12_significance_p_value.ipynb` | Lesson | Significance & p-values in regression |
| `13_simple_linear_regression_lab.ipynb` | Lab | Simple linear regression |
| `14_simple_linear_regression.ipynb` | Lesson | Simple linear regression |
| `15_stat_learning_theory.ipynb` | Conceptual | Statistical learning theory |

**New structure (4 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_simple_linear_regression.ipynb` | 15 + 14 + 13 | 22 |
| `02_ols_statsmodels.ipynb` | 08 + 07 + 03 | 52 |
| `03_model_evaluation.ipynb` | 02 + 01 + 12 | 16 |
| `04_regression_diagnostics.ipynb` | 09 + 06 + 11 | 36 |

**Result:** 13 → 4 (drop 1, consolidate 12 → 4 = 3:1)

---

### 09 — Multiple Regression

✅ **Complete.** Commit: `30fb1bf`

**Source files (21):**

| File | Type | Topic |
|------|------|-------|
| `01_cross_validation_lab.ipynb` | Lab | Cross-validation |
| `02_cross_validation.ipynb` | Lesson | Cross-validation |
| `03_data_science_processes.ipynb` | Conceptual | **DROPPED** (thin DS workflow overview) |
| `04_dealing_with_categorical_variables_lab.ipynb` | Lab | Categorical encoding |
| `05_dealing_with_categorical_variables.ipynb` | Lesson | Categorical encoding |
| `06_feature_scaling_and_normalization_lab.ipynb` | Lab | Feature scaling |
| `07_feature_scaling_and_normalization.ipynb` | Lesson | Feature scaling |
| `08_inference_vs_prediction.ipynb` | Conceptual | Inference vs prediction |
| `09_log_transformations.ipynb` | Lesson | Log transformations |
| `10_model_fit_linear_regression_lab.ipynb` | Lab | Model fit |
| `11_model_fit_linear_regression.ipynb` | Lesson | Model fit & feature selection |
| `12_multicollinearity_of_features_lab.ipynb` | Lab | Multicollinearity |
| `13_multicollinearity_of_features.ipynb` | Lesson | Multicollinearity |
| `14_multiple_linear_regression_in_statsmodels.ipynb` | Lesson | MLR in statsmodels |
| `15_multiple_linear_regression.ipynb` | Lesson | MLR intro |
| `16_multiple_linear_regression_statsmodels_lab.ipynb` | Lab | MLR practice |
| `17_pickle.ipynb` | Lesson | Saving models with pickle |
| `18_regression_introduction.ipynb` | Intro | **DROPPED** |
| `19_regression_model_eval_recap.ipynb` | Recap | **DROPPED** |
| `20_regression_model_validation_lab.ipynb` | Lab | Model validation |
| `21_regression_model_validation.ipynb` | Lesson | Model validation |

**New structure (6 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_multiple_linear_regression.ipynb` | 15 + 14 + 16 | 38 |
| `02_categorical_variables.ipynb` | 05 + 04 | 89 |
| `03_feature_engineering.ipynb` | 07 + 06 + 09 | 51 |
| `04_model_diagnostics.ipynb` | 08 + 13 + 12 + 11 + 10 | 78 |
| `05_model_validation.ipynb` | 21 + 20 | 41 |
| `06_cross_validation.ipynb` | 02 + 01 + 17 | 53 |

**Result:** 21 → 6 (drop 3, consolidate 18 → 6 = 3:1)

---

### 10 — Linear Model Extensions

✅ **Complete.** Commit: `185aec0`

**Source files (8):**

| File | Type | Topic |
|------|------|-------|
| `01_bias_variance_trade_off_lab.ipynb` | Lab | Bias-variance tradeoff |
| `02_bias_variance_trade_off.ipynb` | Lesson | Bias-variance tradeoff |
| `03_extensions_to_linear_models_intro.ipynb` | Intro | **DROPPED** |
| `04_extensions_to_linear_models_recap.ipynb` | Recap | **DROPPED** |
| `05_interaction_terms_lab.ipynb` | Lab | Interaction terms |
| `06_interaction_terms.ipynb` | Lesson | Interaction terms |
| `07_polynomial_regression_lab.ipynb` | Lab | Polynomial regression |
| `08_polynomial_regression.ipynb` | Lesson | Polynomial regression |

**New structure (3 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_bias_variance.ipynb` | 02 + 01 | 80 |
| `02_interaction_terms.ipynb` | 06 + 05 | 60 |
| `03_polynomial_regression.ipynb` | 08 + 07 | 50 |

**Result:** 8 → 3 (drop 2, consolidate 6 → 3 = 2:1)

---

### 11 — Appendix

✅ **Complete.** Commit: `18a1a71`

**Source files (20):**

| File | Type | Topic |
|------|------|-------|
| `01_data_science_toolbox_review.ipynb` | Review | DS toolbox overview |
| `02_exploring_your_data_lab.ipynb` | Lab | Exploratory data analysis |
| `03_exploring_your_data.ipynb` | Lesson | Exploratory data analysis |
| `04_exponential_distribution_lab.ipynb` | Lab | Exponential distribution |
| `05_exponential_distribution.ipynb` | Lesson | Exponential distribution |
| `06_full_ds_regression_intro.ipynb` | Intro | **DROPPED** |
| `07_full_ds_regression_recap.ipynb` | Recap | **DROPPED** |
| `08_modeling_your_data_lab.ipynb` | Lab | Modeling a project |
| `09_modeling_your_data.ipynb` | Lesson | Modeling a project |
| `10_monte_carlo_simulations_lab.ipynb` | Lab | Monte Carlo simulations |
| `11_monte_carlo_simulations.ipynb` | Lesson | Monte Carlo simulations |
| `12_obtaining_your_data_lab.ipynb` | Lab | Obtaining data |
| `13_obtaining_your_data.ipynb` | Lesson | Obtaining data |
| `14_poisson_distribution_lab.ipynb` | Lab | Poisson distribution |
| `15_poisson_distribution.ipynb` | Lesson | Poisson distribution |
| `16_recursive_functions_lab.ipynb` | Lab | Recursive functions |
| `17_recursive_functions.ipynb` | Lesson | Recursive functions |
| `18_scrubbing_and_cleaning_data_lab.ipynb` | Lab | Scrubbing & cleaning data |
| `19_scrubbing_and_cleaning_data.ipynb` | Lesson | Scrubbing & cleaning data |
| `20_uniform_distribution.ipynb` | Lesson | Uniform distribution |

**New structure (4 notebooks):**

| New file | Sources | Cells |
|----------|---------|-------|
| `01_data_workflow.ipynb` | 01 + 13 + 12 + 03 + 02 + 19 + 18 | 67 |
| `02_modeling_project.ipynb` | 09 + 08 | 67 |
| `03_probability_distributions.ipynb` | 15 + 14 + 05 + 04 + 20 | 31 |
| `04_simulation_and_recursion.ipynb` | 11 + 10 + 17 + 16 | 44 |

**Result:** 20 → 4 (drop 2, consolidate 18 → 4 = 4.5:1)

---

## Running Totals

| Section | Before | After | Δ | Commit |
|---------|--------|-------|---|--------|
| 00 Descriptive Statistics | 8 | 5 | −3 | (prior session) |
| 01 Combinatorics & Probability | 14 | 5 | −9 | TBD |
| 02 Statistical Distributions | 17 | 5 | −12 | TBD |
| 03 Central Limit Theorem | 7 | 3 | −4 | `7aeee85` |
| 04 Hypothesis Testing | 11 | 5 | −6 | `11bac2d` |
| 05 ANOVA & Statistical Power | 13 | 5 | −8 | `cd20183` |
| 06 A/B Testing | 6 | 2 | −4 | `c3ec1c9` |
| 07 Bayesian Statistics | 8 | 3 | −5 | `b68e550` |
| 08 Linear Regression | 13 | 4 | −9 | `39dc5af` |
| 09 Multiple Regression | 21 | 6 | −15 | `30fb1bf` |
| 10 Linear Model Extensions | 8 | 3 | −5 | `185aec0` |
| 11 Appendix | 20 | 4 | −16 | TBD |
| **Total** | **146** | **55** | **−91** | |
