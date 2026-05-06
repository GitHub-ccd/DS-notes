# 01_Python_DataTools — Change Log (2026 Update)

**Status:** ✅ Complete  
**Date:** 2026-05-04

---

## What Was Done

### S1 — Data Science Introduction
- **Removed** `S1_14_learn_lessons_lab.ipynb` — Flatiron Learn platform-specific, no standalone value
- **Removed** `S1_15_learn_lessons.ipynb` — Flatiron Learn platform-specific, no standalone value
- **Rewrote** `S1_Data_Science_Introduction.ipynb` — fixed broken `dsc-*` links, clean section index

### S4 — Pandas & Visualization
- **Annotated** `S4_11_kaggle_and_boston_housing_dataset.ipynb` — Boston Housing dataset removed from sklearn v1.2; alternatives: `fetch_california_housing()`, Ames Housing via `fetch_openml`

### S8 — NoSQL
- **Rewrote** `S8_No_SQL.ipynb` — positions MongoDB as legacy context, adds vector DB section with comparison table
- **Annotated** `S8_02_mongodb.ipynb` — context note + updated install instructions (`conda install mongodb` deprecated)
- **New** `S8_06_vector_databases.ipynb` — covers ChromaDB, FAISS, semantic search concepts, comparison table (ChromaDB / FAISS / Pinecone / Weaviate / Qdrant), RAG pipeline intro

### S9 — JSON & APIs
- **Rewrote** `S9_JSON_and_APIs.ipynb` — removed stray SQL links left from old reorganisation; clean index with LLM API section
- **New** `S9_08_llm_apis.ipynb` — Anthropic Claude API: messages format, system prompt, multi-turn conversations, structured JSON outputs, streaming, sentiment classification, summarisation, model selection guide (Opus/Sonnet/Haiku)

### S10 — Webscraping
- **Rewrote** `S10_WebScraping.ipynb` — fixed broken links; added Selenium → Playwright comparison table, when-to-use guide, robots.txt ethics section

---

## What Was Left Alone (Evergreen)
- **S2** Git & Environment — Git is Git
- **S3** Control Flow, Functions, Stats — timeless Python basics
- **S5** Data Cleaning — timeless
- **S6** Seaborn & Visualization — Matplotlib/Seaborn still standard; Plotly bonus already present
- **S7** SQL — gold standard, evergreen

---

## New Files Added
| File | Location | Purpose |
|------|----------|---------|
| `S8_06_vector_databases.ipynb` | `S8_No_SQL/` | ChromaDB + FAISS lab, RAG intro |
| `S9_08_llm_apis.ipynb` | `S9_JSON_and_APIs/` | Anthropic API patterns |

## Files Removed
| File | Reason |
|------|--------|
| `S1_14_learn_lessons_lab.ipynb` | Flatiron Learn platform-specific |
| `S1_15_learn_lessons.ipynb` | Flatiron Learn platform-specific |
