# Section 06 — A/B Testing

A/B test design, statistical analysis, and interpreting results.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_ab_testing_introduction.ipynb` | Section introduction |
| `02_ab_testing_lab.ipynb` | A/B testing lab |
| `03_ab_testing.ipynb` | A/B test setup, analysis, and interpretation |
| `04_ab_testing_recap.ipynb` | Section recap |
| `05_in_depth_ab_testing_lab.ipynb` | In-depth A/B testing lab |
| `06_website_ab_testing_lab.ipynb` | Website A/B testing lab |

## 2026 Context

In industry, A/B tests are rarely run with manual `scipy` code. Platforms like **Statsig**, **LaunchDarkly**, **Amplitude Experiment**, and **Optimizely** handle randomisation, exposure logging, and sequential testing automatically. Understanding the underlying statistics taught here is what lets you interpret and challenge their outputs — that knowledge does not expire.