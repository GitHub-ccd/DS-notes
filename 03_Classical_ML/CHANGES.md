# 03_Classical_ML — Changes (2026 Update)

## Summary notebooks — all 12 rewritten

All section summaries (01–12) had broken `dsc-*` links pointing to legacy Flatiron GitHub repos. Each was rewritten as a clean index file with working relative links to the numbered lesson notebooks (`SXX_NN_topic.ipynb`). Annotations from the original summaries were preserved and expanded where relevant.

| Section | Summary notebook |
|---------|-----------------|
| 01 | OOP Concepts |
| 02 | Linear Algebra |
| 03 | Calculus & Gradient Descent |
| 04 | Regularization & Feature Selection |
| 05 | Logistic Regression & Classification Metrics |
| 06 | MLE & Logistic Regression Deep Dive |
| 07 | K-Nearest Neighbors |
| 08 | Naive Bayes |
| 09 | Decision Trees |
| 10 | Ensemble Methods |
| 11 | SVM |
| 12 | Pipelines |

## Content additions

### 09 — Decision Trees
Added `2026 context` note pointing to SHAP for feature attribution beyond `.feature_importances_`.

### 10 — Ensemble Methods
Added `2026 context` note: LightGBM now often preferred over XGBoost for tabular data (leaf-wise growth, lower memory, less tuning). CatBoost noted for high-cardinality categoricals. SHAP `TreeExplainer` referenced for explanations.

### 11 — SVM
Added `2026 context` note: SVMs less dominant post-2015; remain useful for small/high-dimensional datasets. SHAP `KernelExplainer` noted for SVM explanations.

### 12 — Pipelines
Added `2026 context` note with `ColumnTransformer` as the modern standard for heterogeneous preprocessing (replaces manual split/scale/encode pattern). Code example included.

## New notebook

**`S32_05_shap_explainability.ipynb`** — Introduction to SHAP values for tree models and sklearn pipelines:
- `TreeExplainer` for sklearn trees, RF, GBM, XGBoost, LightGBM
- Summary plot, force plot, bar plot
- Integrating SHAP with a sklearn `Pipeline`
- `KernelExplainer` for model-agnostic explanations (SVM, logistic regression)
- Quick-reference table of explainer types

## Clutter removed

| Item | Reason |
|------|--------|
| `3-EDA_old1.ipynb` (root) | Orphaned pre-reorganisation notebook |
| `4-Model_old1.ipynb` (root) | Orphaned pre-reorganisation notebook |
| `4-Model_old2.ipynb` (root) | Orphaned pre-reorganisation notebook |
| `reorganize.py` (root) | One-off utility script, no longer needed |
| `10_Ensemble_Methods/ds-xgboost-lab-onl01-dtsc-ft-030220/` | Legacy nested Flatiron repo; content covered by `S30_10_xgboost.ipynb` |
