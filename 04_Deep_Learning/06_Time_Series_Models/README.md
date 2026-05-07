# Section 06 — Time Series Models

Moving averages, exponential smoothing, ARMA, and ARIMA with Statsmodels.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_arma_models.ipynb` | ARMA — autoregressive and moving average components |
| `02_arma_models_statsmodels_lab.ipynb` | ARIMA with Statsmodels lab |
| `03_arma_models_statsmodels.ipynb` | Fitting ARIMA models with Statsmodels |
| `04_basic_time_series_models_lab.ipynb` | Basic time series models lab |
| `05_basic_time_series_models.ipynb` | Moving averages and exponential smoothing |
| `08_time_series_models_introduction.ipynb` | Section introduction |
| `09_time_series_models_section_recap.ipynb` | Section recap |

## 2026 Context

ARIMA remains a solid baseline. Modern alternatives worth knowing:

- **Prophet** — Meta's open-source library; fits trend and seasonality automatically, handles missing data and holidays, minimal tuning. Good for business time series with clear seasonal patterns. `pip install prophet`
- **NeuralProphet** — extends Prophet with AR-Net and lagged regressors via PyTorch
- **Statsforecast** — Nixtla's library; fast ARIMA, ETS, and Theta implementations, often outperforms Prophet on benchmark datasets

For large-scale or zero-shot forecasting: **TimeGPT** (Nixtla) and **Chronos** (Amazon) are foundation models for time series prediction.