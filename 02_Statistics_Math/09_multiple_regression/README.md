# Section 09 — Multiple Regression & Model Validation

Multiple regression, categorical variables, feature scaling, cross-validation, multicollinearity, and model persistence.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_cross_validation_lab.ipynb` | Cross-validation lab |
| `02_cross_validation.ipynb` | k-fold cross-validation — honest model evaluation |
| `03_data_science_processes.ipynb` | The DS workflow end-to-end |
| `04_dealing_with_categorical_variables_lab.ipynb` | Categorical variables lab |
| `05_dealing_with_categorical_variables.ipynb` | One-hot encoding and dummy variable trap |
| `06_feature_scaling_and_normalization_lab.ipynb` | Feature scaling lab |
| `07_feature_scaling_and_normalization.ipynb` | Min-max scaling, standardisation |
| `08_inference_vs_prediction.ipynb` | Inference (understanding) vs prediction (performance) |
| `09_log_transformations.ipynb` | Log transformations for skewed variables |
| `10_model_fit_linear_regression_lab.ipynb` | Model fit lab |
| `11_model_fit_linear_regression.ipynb` | Adjusted R², AIC, BIC, and F-statistic |
| `12_multicollinearity_of_features_lab.ipynb` | Multicollinearity lab |
| `13_multicollinearity_of_features.ipynb` | VIF and detecting multicollinearity |
| `14_multiple_linear_regression_in_statsmodels.ipynb` | Multiple regression in Statsmodels |
| `15_multiple_linear_regression.ipynb` | Multiple regression — extending OLS to many predictors |
| `16_multiple_linear_regression_statsmodels_lab.ipynb` | Multiple regression lab |
| `17_pickle.ipynb` | Saving and loading models with pickle and joblib |
| `18_regression_introduction.ipynb` | Section introduction |
| `19_regression_model_eval_recap.ipynb` | Section recap |
| `20_regression_model_validation_lab.ipynb` | Model validation lab |
| `21_regression_model_validation.ipynb` | Train-test split and model validation |

## 2026 Context

**Model persistence:** For sklearn models, prefer `joblib` over raw `pickle` — it is faster for large numpy arrays and is sklearn's own recommendation. `joblib.dump(model, 'model.joblib')` / `joblib.load('model.joblib')`. Note that `pickle` files can execute arbitrary code on load — never unpickle files from untrusted sources. For production deployments, consider **ONNX** (framework-agnostic, cross-language) or **MLflow model registry**. See `17_pickle.ipynb` for the security warning and alternatives.