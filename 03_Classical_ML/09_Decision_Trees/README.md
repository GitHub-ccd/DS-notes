# Section 09 — Decision Trees

Entropy, information gain, CART, ID3, scikit-learn decision trees, and hyperparameter tuning.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_decision_trees_lab.ipynb` | Decision trees lab |
| `02_decision_trees_section_intro.ipynb` | Section introduction |
| `03_decision_trees_section_recap.ipynb` | Section recap |
| `04_decision_trees_with_sklearn_codealong.ipynb` | Fitting and visualising `DecisionTreeClassifier` |
| `05_entropy_and_information_gain.ipynb` | Shannon entropy and information gain as split criteria |
| `06_ID3_trees_lab.ipynb` | ID3 algorithm lab |
| `07_introduction_to_decision_trees.ipynb` | CART vs ID3 — Gini index vs entropy |
| `08_regression_cart_trees_codealong.ipynb` | `DecisionTreeRegressor` — predicting continuous targets |
| `09_regression_cart_trees_lab.ipynb` | Regression tree lab |
| `10_tuning_decision_trees_lab.ipynb` | Decision tree tuning lab |
| `11_tuning_decision_trees.ipynb` | `max_depth`, `min_samples_split`, pruning |
| `12_tuning_regression_trees_lab.ipynb` | Regression tree tuning lab |

## 2026 Context

Tree-based feature importance (`.feature_importances_`) is the classic way to understand which features a tree used. For richer, model-agnostic explanations, use **SHAP** — it provides consistent, additive attribution values that work across decision trees, ensembles, and other models. See `05_shap_explainability.ipynb` in Section 12 (Pipelines).