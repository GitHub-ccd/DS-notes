# 01_Python_DataTools — Change Log (2026 Update)

**Status:** ✅ Complete  
**Date:** 2026-05-04

---

## What Was Done

### 01 — Data Science Introduction
- **Removed** `14_learn_lessons_lab.ipynb` — Flatiron Learn platform-specific, no standalone value
- **Removed** `15_learn_lessons.ipynb` — Flatiron Learn platform-specific, no standalone value
- **Rewrote** `S1_Data_Science_Introduction.ipynb` — fixed broken `dsc-*` links, clean section index

### 04 — Pandas & Visualization
- **Annotated** `11_kaggle_and_boston_housing_dataset.ipynb` — Boston Housing dataset removed from sklearn v1.2; alternatives: `fetch_california_housing()`, Ames Housing via `fetch_openml`

### 08 — NoSQL
- **Rewrote** `S8_No_SQL.ipynb` — positions MongoDB as legacy context, adds vector DB section with comparison table
- **Annotated** `02_mongodb.ipynb` — context note + updated install instructions (`conda install mongodb` deprecated)
- **New** `06_vector_databases.ipynb` — covers ChromaDB, FAISS, semantic search concepts, comparison table (ChromaDB / FAISS / Pinecone / Weaviate / Qdrant), RAG pipeline intro

### 09 — JSON & APIs
- **Rewrote** `S9_JSON_and_APIs.ipynb` — removed stray SQL links left from old reorganisation; clean index with LLM API section
- **New** `08_llm_apis.ipynb` — Anthropic Claude API: messages format, system prompt, multi-turn conversations, structured JSON outputs, streaming, sentiment classification, summarisation, model selection guide (Opus/Sonnet/Haiku)

### 10 — Webscraping
- **Rewrote** `WebScraping.ipynb` — fixed broken links; added Selenium → Playwright comparison table, when-to-use guide, robots.txt ethics section

---

## What Was Left Alone (Evergreen)
- **02** Git & Environment — Git is Git
- **03** Control Flow, Functions, Stats — timeless Python basics
- **05** Data Cleaning — timeless
- **06** Seaborn & Visualization — Matplotlib/Seaborn still standard; Plotly bonus already present
- **07** SQL — gold standard, evergreen

---

## New Files Added
| File | Location | Purpose |
|------|----------|---------|
| `06_vector_databases.ipynb` | `08_No_SQL/` | ChromaDB + FAISS lab, RAG intro |
| `08_llm_apis.ipynb` | `09_JSON_and_APIs/` | Anthropic API patterns |

## Files Removed
| File | Reason |
|------|--------|
| `14_learn_lessons_lab.ipynb` | Flatiron Learn platform-specific |
| `15_learn_lessons.ipynb` | Flatiron Learn platform-specific |
