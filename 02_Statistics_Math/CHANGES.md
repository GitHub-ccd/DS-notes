# 02_Statistics_Math — Change Log (2026 Update)

**Status:** ✅ Complete  
**Date:** 2026-05-04

---

## What Was Done

### Housekeeping — All Sections (01–11)
- **Removed** `make_pdf.ipynb` from every section (11 files) — utility script, not educational content
- **Removed** `Sections_XX.ipynb` duplicates from every section (9 files) — redundant copies of summaries
- **Removed** `S11_Combinatorics_Probability-Copy1.ipynb` — duplicate
- **Removed** `Sec_11.ipynb` — duplicate
- **Removed** `02_Statistical_Distributions/stat_funtions.ipynb` — scratch file (misspelled, unused)
- **Rewrote all 11 summary notebooks** (01–11) — fixed broken `dsc-*` links, clean section indexes with working relative links

### 04 — Hypothesis Testing
- **Updated** `S14_Hypothesis_Testing.ipynb` — added **Causal Inference** awareness section: Potential Outcomes framework, DAGs, Difference-in-Differences, Instrumental Variables; Python tools: `dowhy`, `causalml`, `econml`

### 06 — A/B Testing
- **Updated** `S16_AB_testing.ipynb` — added 2026 context note on modern A/B platforms (Statsig, LaunchDarkly, Amplitude Experiment, Optimizely) and why the underlying statistics here still matter

### 07 — Bayesian Statistics
- **Updated** `S17_Bayesian_Stat.ipynb` — added **PyMC v5** working code example for practical Bayesian computation (prior, likelihood, posterior sampling via MCMC)

### 08 — Linear Regression
- **Updated** `S18_Linear_Regression.ipynb` — Boston Housing project section flagged with deprecation note and alternatives
- **Annotated** `S18_10_regression_boston_lab.ipynb` — Boston Housing dataset deprecation notice (removed sklearn v1.2), California Housing and Ames Housing as replacements
- **Annotated** `S18_11_regression_boston_lab.ipynb` — same deprecation notice

### 09 — Multiple Regression & Model Validation
- **Updated** `S19_multiple_regression.ipynb` — model persistence section adds joblib (sklearn-preferred), ONNX (production/cross-language), MLflow (model registry) context
- **Annotated** `S19_17_pickle.ipynb` — security warning (arbitrary code execution on load), joblib as preferred alternative, ONNX for production

---

## What Was Left Alone (Evergreen)
The core mathematics in 02_Statistics_Math does not expire:
- **01** Combinatorics & Probability — timeless
- **02** Statistical Distributions — timeless
- **03** Central Limit Theorem — timeless
- **05** ANOVA & Statistical Power — timeless
- **10** Linear Model Extensions (bias-variance, polynomial, interaction terms) — timeless
- **11** Appendix — timeless

---

## Files Removed (22 total)
| Pattern | Count | Reason |
|---------|-------|--------|
| `make_pdf.ipynb` | 11 | Utility script, not educational |
| `Sections_*.ipynb` | 9 | Duplicate summary copies |
| `-Copy1.ipynb` | 1 | Duplicate |
| `Sec_11.ipynb` | 1 | Duplicate |
| `stat_funtions.ipynb` | 1 | Scratch file |

## New Content Added (inline)
| Location | Content Added |
|----------|--------------|
| 04 summary | Causal inference section (DoWhy, DAGs, econml) |
| 06 summary | Modern A/B testing platforms context note |
| 07 summary | PyMC v5 Bayesian computation example |
| 08 summary | Boston Housing deprecation inline note |
| 09 summary | joblib / ONNX / MLflow model persistence note |
| S18_10, S18_11 | Boston Housing deprecation blockquotes |
| S19_17 | Pickle security warning + joblib/ONNX alternatives |
