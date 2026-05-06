# MOD_2 — Change Log (2026 Update)

**Status:** ✅ Complete  
**Date:** 2026-05-04

---

## What Was Done

### Housekeeping — All Sections (S11–S21)
- **Removed** `make_pdf.ipynb` from every section (11 files) — utility script, not educational content
- **Removed** `Sections_XX.ipynb` duplicates from every section (9 files) — redundant copies of summaries
- **Removed** `S11_Combinatorics_Probability-Copy1.ipynb` — duplicate
- **Removed** `Sec_11.ipynb` — duplicate
- **Removed** `S12/stat_funtions.ipynb` — scratch file (misspelled, unused)
- **Rewrote all 11 summary notebooks** (S11–S21) — fixed broken `dsc-*` links, clean section indexes with working relative links

### S14 — Hypothesis Testing
- **Updated** `S14_Hypothesis_Testing.ipynb` — added **Causal Inference** awareness section: Potential Outcomes framework, DAGs, Difference-in-Differences, Instrumental Variables; Python tools: `dowhy`, `causalml`, `econml`

### S16 — A/B Testing
- **Updated** `S16_AB_testing.ipynb` — added 2026 context note on modern A/B platforms (Statsig, LaunchDarkly, Amplitude Experiment, Optimizely) and why the underlying statistics here still matter

### S17 — Bayesian Statistics
- **Updated** `S17_Bayesian_Stat.ipynb` — added **PyMC v5** working code example for practical Bayesian computation (prior, likelihood, posterior sampling via MCMC)

### S18 — Linear Regression
- **Updated** `S18_Linear_Regression.ipynb` — Boston Housing project section flagged with deprecation note and alternatives
- **Annotated** `S18_10_regression_boston_lab.ipynb` — Boston Housing dataset deprecation notice (removed sklearn v1.2), California Housing and Ames Housing as replacements
- **Annotated** `S18_11_regression_boston_lab.ipynb` — same deprecation notice

### S19 — Multiple Regression & Model Validation
- **Updated** `S19_multiple_regression.ipynb` — model persistence section adds joblib (sklearn-preferred), ONNX (production/cross-language), MLflow (model registry) context
- **Annotated** `S19_17_pickle.ipynb` — security warning (arbitrary code execution on load), joblib as preferred alternative, ONNX for production

---

## What Was Left Alone (Evergreen)
The core mathematics in MOD_2 does not expire:
- **S11** Combinatorics & Probability — timeless
- **S12** Statistical Distributions — timeless
- **S13** Central Limit Theorem — timeless
- **S15** ANOVA & Statistical Power — timeless
- **S20** Linear Model Extensions (bias-variance, polynomial, interaction terms) — timeless
- **S21** Appendix — timeless

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
| S14 summary | Causal inference section (DoWhy, DAGs, econml) |
| S16 summary | Modern A/B testing platforms context note |
| S17 summary | PyMC v5 Bayesian computation example |
| S18 summary | Boston Housing deprecation inline note |
| S19 summary | joblib / ONNX / MLflow model persistence note |
| S18_10, S18_11 | Boston Housing deprecation blockquotes |
| S19_17 | Pickle security warning + joblib/ONNX alternatives |
