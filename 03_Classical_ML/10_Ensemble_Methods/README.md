# Section 10 — Ensemble Methods

Bagging, random forests, gradient boosting, XGBoost, and hyperparameter search with GridSearchCV.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_ensemble_methods.ipynb` | Bagging vs boosting — wisdom of crowds applied to models |
| `04_gradient_boosting_and_weak_learners.ipynb` | Sequential boosting — each tree corrects the residuals of the previous |
| `05_gradient_boosting_lab.ipynb` | Gradient boosting lab |
| `06_gridsearchcv_lab.ipynb` | GridSearchCV lab |
| `07_gridsearchcv.ipynb` | Exhaustive hyperparameter search with cross-validation |
| `08_random_forests.ipynb` | Random subspace method — decorrelating trees via feature subsampling |
| `09_tree_ensembles_random_forests_lab.ipynb` | Random forests lab |
| `10_xgboost.ipynb` | XGBoost — regularised gradient boosting |

## 2026 Context

XGBoost remains widely used, but **LightGBM** (`lightgbm.LGBMClassifier`) is now often preferred for tabular data — it trains faster (leaf-wise growth), handles large datasets with lower memory use, and frequently matches or beats XGBoost with less tuning. **CatBoost** is a strong alternative when the data has high-cardinality categoricals. For most new tabular ML projects, benchmark LightGBM first. For model explanations across any boosting library, `shap.TreeExplainer` is the standard tool.