# Section 12 — Pipelines & Explainability

Scikit-learn pipelines for end-to-end ML workflows and SHAP values for model explainability.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_pipelines_intro.ipynb` | Why pipelines — preventing data leakage, simplifying cross-validation |
| `02_pipelines_lab.ipynb` | Pipelines lab |
| `03_pipelines_recap.ipynb` | Section recap |
| `04_pipelines.ipynb` | Building `sklearn.pipeline.Pipeline` objects |
| `05_shap_explainability.ipynb` | SHAP values — model-agnostic feature attribution for trees and pipelines |

## 2026 Context

The modern scikit-learn pattern for heterogeneous feature sets is `ColumnTransformer` — apply different preprocessing to numeric vs categorical columns in a single pipeline step, then feed into any estimator. This replaces the older pattern of manually splitting, scaling, and encoding before passing to a model. `ColumnTransformer` + `Pipeline` is the standard structure for any production sklearn workflow.