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
| **01_Python_DataTools** — Python, Pandas, SQL, APIs, Scraping | Mostly solid, 2 sections needed work | ✅ Done |
| **02_Statistics_Math** — Probability, Stats, Regression | Evergreen math, housekeeping only | ✅ Done |
| **03_Classical_ML** — Classical ML (Logistic Reg, Trees, SVM, etc.) | Solid, sklearn still dominant | ✅ Done |
| **04_Deep_Learning** — Deep Learning, NLP, Cloud ML | Needs significant work — field moved fastest here | ✅ Done |
| **05_LLMs_GenAI** — LLMs, GenAI & Agents | New module — no legacy content, built from scratch | ✅ Done |

---

## Module Status

### ✅ 01_Python_DataTools — Complete
See [01_Python_DataTools/CHANGES.md](./01_Python_DataTools/CHANGES.md)

Key actions taken:
- Removed Flatiron Learn-platform notebooks (S1_14, S1_15)
- Annotated Boston Housing dataset as deprecated (S4)
- Rebuilt S8 NoSQL: MongoDB marked as legacy context; added `S8_06_vector_databases.ipynb` (ChromaDB, FAISS)
- Fixed S9 summary (had stray SQL links); added `S9_08_llm_apis.ipynb` (Anthropic API patterns)
- Rebuilt S10 WebScraping summary: Selenium → Playwright comparison, ethics section

### ✅ 02_Statistics_Math — Complete
See [02_Statistics_Math/CHANGES.md](./02_Statistics_Math/CHANGES.md)

Key actions taken:
- Removed 22 clutter files (make_pdf.ipynb, Sections_XX.ipynb, duplicates)
- Rewrote all 11 broken summary notebooks (S11–S21)
- Annotated both Boston Housing lab notebooks in S18
- Added causal inference section to S14 summary (DoWhy, DAGs, econml)
- Added PyMC v5 example to S17 Bayesian summary
- Added modern A/B platform note to S16
- Added joblib/ONNX/MLflow note to S19 model persistence section
- Added pickle security warning to S19_17

### ✅ 03_Classical_ML — Complete
See [03_Classical_ML/CHANGES.md](./03_Classical_ML/CHANGES.md)

Key actions taken:
- Rewrote all 12 broken summary notebooks (S21–S32) — replaced dsc-* links with working relative links
- Removed 5 clutter items: 3 root-level orphan notebooks, `reorganize.py`, and `S30/ds-xgboost-lab-onl01-dtsc-ft-030220/` nested repo
- Added LightGBM/CatBoost context note to S30 Ensemble Methods summary
- Added ColumnTransformer pattern (with code example) to S32 Pipelines summary
- Added SHAP cross-reference notes to S29, S30, and S31 summaries
- Added `S32_05_shap_explainability.ipynb` — SHAP values for tree models and sklearn pipelines

### ✅ 04_Deep_Learning — Complete

See [04_Deep_Learning/CHANGES.md](./04_Deep_Learning/CHANGES.md)

Key actions taken:
- Rewrote all 14 summary notebooks (S33–S43 + CNN, Transfer Learning, Graph Theory)
- Fixed naming anomaly: S34 summary was `Section_33_clustering.ipynb` → `Section_34_clustering.ipynb`
- Removed 4 clutter items: `reorganize.py`, wrong-named S34 summary, and 2 nested legacy repos (S35/S36)
- Note: CNN, Graph Theory, Transfer Learning nested repos kept — they are the sole lesson content for those sections
- Added Databricks context note to S35; embedding-based recommendation note to S36
- Added Prophet/NeuralProphet/TimeGPT note to S38
- Added NLTK legacy warning + `S39_14_transformers_huggingface.ipynb` (HuggingFace `transformers`, `sentence-transformers`, spaCy)
- Added PyTorch vs Keras comparison to S40; Optuna/LayerNorm notes to S42
- Added ViT/CLIP note to CNN; LoRA/foundation model note to Transfer Learning; GNN/PyTorch Geometric note to Graph Theory
- Expanded S43 to cover all three major cloud ML platforms:
  - `S43_07_azure_ml.ipynb` — Azure ML SDK v2, MLflow tracking, managed endpoints
  - `S43_08_gcp_vertex_ai.ipynb` — Vertex AI, Kubeflow Pipelines, Gemini API

### ✅ 05_LLMs_GenAI — Complete

**Sections:**

| Section | Topic | Notebooks |
|---------|-------|-----------|
| S44 | Transformers & Attention Mechanism | 5 lessons: self-attention, multi-head attention, transformer arch, positional encoding, BERT/GPT/T5 families |
| S45 | HuggingFace Ecosystem | 5 lessons: Hub, tokenizers, datasets library, PEFT/LoRA, Accelerate |
| S46 | LLMs — Concepts, Prompting & Evaluation | 5 lessons: what are LLMs, prompt engineering, chain-of-thought, LLM APIs, evaluation |
| S47 | RAG (Retrieval-Augmented Generation) | 5 lessons: why RAG, document loading/chunking, embeddings/vector DBs, retrieval strategies, end-to-end pipeline |
| S48 | AI Agents & Tool Use | 5 lessons: agent architecture, function calling, ReAct/LangChain, LangGraph, multi-agent frameworks |
| S49 | LLM Fine-tuning | 5 lessons: when to fine-tune, LoRA/QLoRA, instruction tuning, RLHF/DPO, end-to-end with Unsloth/TRL |
| S50 | LLMOps & Deployment | 5 lessons: quantization, inference servers, LLM monitoring, cost optimization, LLMOps overview |

**Note:** S39_14 (04_Deep_Learning) is the entry point to HuggingFace `transformers` — S44/S45 go deeper into theory and advanced tooling.

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
