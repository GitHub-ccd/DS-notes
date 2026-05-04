# DS-Notes — Editorial Plan (2026 Update)

## Objective

Keep this repo as a **personal library of ML and AI learnings** — not a course archive.
Before adding new content, identify and update stale/legacy material module by module.

---

## Guiding Principles

- **Annotate, don't delete** stale content unless it has zero standalone value (e.g. platform-specific onboarding notebooks)
- Add `> ⚠️ LEGACY NOTE (2026):` blockquotes to notebooks with outdated tools/datasets
- Add `> ℹ️ 2026 context:` blockquotes for sections where the field has moved on but the foundations still apply
- Fix all broken `dsc-*` summary notebook links (legacy from Flatiron reorganisation)
- Remove utility clutter: `make_pdf.ipynb`, `Sections_XX.ipynb` duplicates, `-Copy1` files
- New notebooks use the naming pattern `SXX_NN_topic_name.ipynb`
- New summary notebooks are clean index files with working relative links

---

## 30,000-Mile View

| Module | Verdict | Priority |
|--------|---------|----------|
| **MOD_1** — Python, Pandas, SQL, APIs, Scraping | Mostly solid, 2 sections needed work | ✅ Done |
| **MOD_2** — Probability, Stats, Regression | Evergreen math, housekeeping only | ✅ Done |
| **MOD_3** — Classical ML (Logistic Reg, Trees, SVM, etc.) | Solid, sklearn still dominant | ✅ Done |
| **MOD_4** — Deep Learning, NLP, AWS | Needs significant work — field moved fastest here | 🔲 Pending |

**MOD_5 (proposed):** LLMs, GenAI & Agents — substantial enough for its own module. Scope TBD.

---

## Module Status

### ✅ MOD_1 — Complete
See [MOD_1/CHANGES.md](./MOD_1/CHANGES.md)

Key actions taken:
- Removed Flatiron Learn-platform notebooks (S1_14, S1_15)
- Annotated Boston Housing dataset as deprecated (S4)
- Rebuilt S8 NoSQL: MongoDB marked as legacy context; added `S8_06_vector_databases.ipynb` (ChromaDB, FAISS)
- Fixed S9 summary (had stray SQL links); added `S9_08_llm_apis.ipynb` (Anthropic API patterns)
- Rebuilt S10 WebScraping summary: Selenium → Playwright comparison, ethics section

### ✅ MOD_2 — Complete
See [MOD_2/CHANGES.md](./MOD_2/CHANGES.md)

Key actions taken:
- Removed 22 clutter files (make_pdf.ipynb, Sections_XX.ipynb, duplicates)
- Rewrote all 11 broken summary notebooks (S11–S21)
- Annotated both Boston Housing lab notebooks in S18
- Added causal inference section to S14 summary (DoWhy, DAGs, econml)
- Added PyMC v5 example to S17 Bayesian summary
- Added modern A/B platform note to S16
- Added joblib/ONNX/MLflow note to S19 model persistence section
- Added pickle security warning to S19_17

### ✅ MOD_3 — Complete
See [MOD_3/CHANGES.md](./MOD_3/CHANGES.md)

Key actions taken:
- Rewrote all 12 broken summary notebooks (S21–S32) — replaced dsc-* links with working relative links
- Removed 5 clutter items: 3 root-level orphan notebooks, `reorganize.py`, and `S30/ds-xgboost-lab-onl01-dtsc-ft-030220/` nested repo
- Added LightGBM/CatBoost context note to S30 Ensemble Methods summary
- Added ColumnTransformer pattern (with code example) to S32 Pipelines summary
- Added SHAP cross-reference notes to S29, S30, and S31 summaries
- Added `S32_05_shap_explainability.ipynb` — SHAP values for tree models and sklearn pipelines

### 🔲 MOD_4 — Pending (most work required)

**Sections:** S33 (PCA), S34 (Clustering), S35 (PySpark), S36 (Recommendation Systems), S37–S38 (Time Series), S39 (NLP), S40–S42 (Neural Networks/Deep Learning), S43 (AWS)
Plus existing extras: CNN, Transfer Learning, Graph Theory

**Expected work:**
- S35 PySpark: still relevant but add Databricks context note
- S36 Recommendations: add LLM-based recommendation note
- S39 NLP: **major rewrite** — NLTK-based NLP is legacy; needs Transformers/HuggingFace section
- S40–S42 Neural Networks: add PyTorch as modern alternative to Keras/TensorFlow
- S43 AWS: update for current SageMaker and add MLOps context
- Missing entirely: LLMs, RAG, Transformers, HuggingFace, Agents → likely MOD_5

### 🔲 MOD_5 — Proposed

**Proposed sections:**
| Section | Topic |
|---------|-------|
| S44 | Transformers & Attention Mechanism |
| S45 | HuggingFace Ecosystem |
| S46 | LLMs — Concepts, Prompting, Evaluation |
| S47 | RAG (Retrieval-Augmented Generation) |
| S48 | AI Agents & Tool Use |
| S49 | LLM Fine-tuning |
| S50 | LLMOps & Deployment |

---

## Conventions for New Notebooks

```
SXX_NN_topic_name.ipynb      # numbered notebook
SXX_topic_name.ipynb         # section summary / index (no number prefix)
```

Legacy note blockquote:
```markdown
> ⚠️ **LEGACY NOTE (2026):** ...explanation... **Use instead:** ...alternative...
```

2026 context blockquote:
```markdown
> **2026 context:** ...what changed, what to use now...
```
