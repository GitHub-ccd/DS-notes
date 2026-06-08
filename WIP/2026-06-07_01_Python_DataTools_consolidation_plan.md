# Module 01 — Consolidation Plan
*2026-06-07 — completed 2026-06-08*

**Status: COMPLETE ✅**

All sections executed and committed. 91 original notebooks across 8 sections → 45 consolidated notebooks. Net reduction: −46 files in the sections touched this session (−94 across the full plan including prior-session work on 01–03).

---

## Background — The Original Lesson + Lab Curriculum Style

The original curriculum (Modules 01–04) was built around a **paired notebook model**: every topic was split across two separate files — a lesson notebook and a `_lab` notebook.

### What the pattern looked like

```
04_pandas_visualization/
├── 01_pandas_viz_lab.ipynb        ← exercises with blanks / starter code
├── 02_pandas_viz_lesson.ipynb     ← narrative explanation of the concept
├── 03_...
├── 04_..._lab.ipynb
├── 05_..._lesson.ipynb
...
```

Every section also had:
- A **section intro** notebook (often a single markdown cell: "In this section you will learn…")
- A **section recap** notebook (just a summary of what was covered)
- Occasional **codealong** and **studygroup** notebooks with non-standard naming (e.g., `Groupby_StudyGroup_codealong.ipynb`)

### Why this caused problems

1. **File count explosion** — the lesson+lab pattern doubled the number of notebooks. Module 01 alone had 91 notebooks across 6 sections.
2. **Redundancy** — lab notebooks repeated the lesson's concept explanations with blanks inserted. Reading both felt like reading the same page twice.
3. **Section intros and recaps added noise** — short scaffolding notebooks interrupted flow without adding content.
4. **Non-standard names** — codealong, studygroup, and quiz notebooks broke the numbered-file convention and were hard to navigate.
5. **Shallow individual notebooks** — many notebooks were 5–15 cells, too short to build any mental model in isolation.

### The consolidation philosophy

Each lesson+lab pair was **merged into a single focused notebook** that teaches the concept and contains integrated exercises. This is the same approach used in Module 05 (the 2026 rebuild), which uses exactly 5 focused notebooks per section with no separate lab files.

**Rules applied during consolidation:**
- Lesson + lab → one notebook; exercises appear after the concept is taught, not in a separate file
- Section intro notebooks → absorbed into the opening cell of the first substantive notebook, or dropped
- Section recap notebooks → dropped entirely (the notebooks themselves are the reference)
- Codealong/studygroup notebooks → absorbed into the relevant topic notebook or dropped if content was thin
- Quiz notebooks → integrated as a practice block at the end of the relevant topic notebook

The target compression ratio was roughly **3:1** — three original notebooks became one consolidated notebook.

---

## Final Structure

```
01_Python_DataTools/
├── 01_Tools_Environment_Git/
├── 02_Python_Fundamentals/
├── 03_NumPy_Pandas_Viz/
├── 04_Data_Cleaning/
├── 05_SQL/
├── 06_No_SQL/
├── 07_JSON_and_APIs/
└── 08_Webscraping/

02_Statistics_Math/
└── 00_Descriptive_Statistics/    ← moved from 01/03 statistics notebooks
```

---

## Completion Summary

### Sections 01–03 + 02/00 (completed prior session)

| Section | Action | Result |
|---------|--------|--------|
| 02/00 Descriptive Statistics | Created from 8 notebooks moved out of 01/03 | 8 → 5 notebooks |
| 01/01 Tools & Git | Created new section from old 01 + 02 | 33 → 6 notebooks |
| 01/02 Python Fundamentals | Created new section from old 01 + 03 | 32 → 8 notebooks |
| 01/03 NumPy/Pandas/Viz | Created new section merging old 04 + 06 | 23 → 12 notebooks |
| Renumber 01 sections | 05→04, 07→05, 08→06, 09→07, 10→08 | — |

### Sections 04–08 (completed 2026-06-08)

| Section | Before | After | Δ | Commit |
|---------|--------|-------|---|--------|
| 04 Data Cleaning | 16 | 6 | −10 | `ec273ea` |
| 05 SQL | 22 | 6 | −16 | `45b0f31` |
| 06 NoSQL | 5 | 2 | −3 | `87ab069` |
| 07 JSON & APIs | 8 | 4 | −4 | `89faf3c` |
| 08 Webscraping | 13 | 3 | −10 | `4aa5a1c` |
| **Total (this session)** | **64** | **21** | **−43** | |

### Overall plan totals

| Module | Section | Before | After | Δ |
|--------|---------|--------|-------|---|
| 01 | 01 Tools & Git | 33 | 6 | −27 |
| 01 | 02 Python Fundamentals | 32 | 8 | −24 |
| 01 | 03 NumPy/Pandas/Viz | 23 | 12 | −11 |
| 01 | 04 Data Cleaning | 16 | 6 | −10 |
| 01 | 05 SQL | 22 | 6 | −16 |
| 01 | 06 NoSQL | 5 | 2 | −3 |
| 01 | 07 JSON & APIs | 8 | 4 | −4 |
| 01 | 08 Webscraping | 13 | 3 | −10 |
| 02 | 00 Descriptive Statistics | 8 | 5 | −3 |
| **Total** | | **160** | **52** | **−108** |

---

## Detailed Section Plans

### 04 — Data Cleaning (complete `ec273ea`)

| # | Notebook | Merges From |
|---|----------|-------------|
| 01 | `01_combining_dataframes.ipynb` | 02 + 01 |
| 02 | `02_lambda_functions.ipynb` | 09 + 08 |
| 03 | `03_missing_data.ipynb` | 05 + 04 + 11 + 10 |
| 04 | `04_groupby_and_aggregation.ipynb` | 12 |
| 05 | `05_pivot_tables.ipynb` | 14 + 13 |
| 06 | `06_data_cleaning_project.ipynb` | 03 (rename) |

Dropped: `07_introduction_pandas_etl` (intro), `15_summary_data_cleaning_pandas` (recap), `Groupby_StudyGroup_codealong` (thin, non-standard).

### 05 — SQL (complete `45b0f31`)

| # | Notebook | Merges From |
|---|----------|-------------|
| 01 | `01_selecting_and_filtering.ipynb` | 13 + 12 + ORDER BY parts of 04 + 03 |
| 02 | `02_database_admin.ipynb` | 02 + 01 + 14 |
| 03 | `03_aggregation_and_groupby.ipynb` | 06 + 05 |
| 04 | `04_joins.ipynb` | 08 + 07 + 11 + 10 + 09 |
| 05 | `05_subqueries.ipynb` | 20 + 19 |
| 06 | `06_sql_with_pandas.ipynb` | 22 + 21 |

Dropped: `17` (corrupted intro), `18` (recap), `15` (no runnable DB), `16` (pre-answered quiz). Kept: `Airport_database/`, `Chinook_database/` standalone references.

### 06 — NoSQL (complete `87ab069`)

| # | Notebook | Merges From |
|---|----------|-------------|
| 01 | `01_nosql_and_mongodb.ipynb` | 05 + 02 + 01 |
| 02 | `02_vector_databases.ipynb` | 06 (rename) |

Dropped: `Other_DB.ipynb` (dead links).

### 07 — JSON & APIs (complete `89faf3c`)

| # | Notebook | Merges From |
|---|----------|-------------|
| 01 | `01_json_fundamentals.ipynb` | 05 + 04 |
| 02 | `02_exploring_json_schemas.ipynb` | 02 + 01 |
| 03 | `03_rest_apis_and_json_responses.ipynb` | 07 + 06 (+ ISS API demo added) |
| 04 | `04_llm_apis.ipynb` | 08 (rename) |

Dropped: `03_json_apis_intro` (section intro).

### 08 — Webscraping (complete `4aa5a1c`)

| # | Notebook | Merges From |
|---|----------|-------------|
| 01 | `01_html_and_css.ipynb` | 05 + 06 |
| 02 | `02_beautifulsoup_basics.ipynb` | 14 |
| 03 | `03_scraping_in_practice.ipynb` | 12 + 13 + 10 |

Dropped: `01` (Codepen link only), `02` (section intro), `03` (recap), `08` (how-to-Google markdown), `09` (ResidentAdvisor — Cloudflare + JS rendering, not scrapable with BS4), `11` (separation of concerns summary).
