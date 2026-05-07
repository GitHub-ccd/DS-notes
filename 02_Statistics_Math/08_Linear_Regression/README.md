# Section 08 — Simple Linear Regression

Ordinary least squares, Statsmodels, regression assumptions, diagnostics, and statistical inference.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_coefficient_of_determination_lab.ipynb` | R² lab |
| `02_coefficient_of_determination.ipynb` | R² — coefficient of determination |
| `03_complete_regression_lab.ipynb` | End-to-end regression lab |
| `04_linear_regression_section_intro.ipynb` | Section introduction |
| `05_linear_regression_section_recap.ipynb` | Section recap |
| `06_ols_regression_diagnostics.ipynb` | OLS diagnostics — residual plots, Q-Q plots, Cook's distance |
| `07_ols_statsmodels_lab.ipynb` | OLS with Statsmodels lab |
| `08_ols_statsmodels.ipynb` | Fitting and interpreting OLS models with Statsmodels |
| `09_regression_assumptions.ipynb` | LINE assumptions — linearity, independence, normality, equal variance |
| `10_regression_boston_lab.ipynb` | Regression project lab |
| `11_regression_boston_lab.ipynb` | Regression project lab (solutions) |
| `12_significance_p_value.ipynb` | Coefficient significance and p-values |
| `13_simple_linear_regression_lab.ipynb` | Simple linear regression lab |
| `14_simple_linear_regression.ipynb` | OLS derivation — minimising the sum of squared residuals |
| `15_stat_learning_theory.ipynb` | Statistical learning theory |

## 2026 Context

`10_regression_boston_lab.ipynb` and `11_regression_boston_lab.ipynb` use the **Boston Housing dataset**, which was removed from scikit-learn in v1.2 due to an ethical concern with one of its features. As a replacement, use the **California Housing** dataset (`from sklearn.datasets import fetch_california_housing`) or the **Ames Housing** dataset (`pip install ameshousing`). The regression techniques themselves are unchanged.