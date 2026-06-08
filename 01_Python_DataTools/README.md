# 01 — Python & Data Tools

**Sections 01–08** — reorganized from the original 10 sections into 8 clean, consolidated sections.

Each section folder contains:
- Numbered lesson notebooks: `NN_topic.ipynb` (lesson and practice integrated)
- `README.md` — section overview and notebook descriptions
- `assets/` — images and HTML files referenced by notebooks (where applicable)
- `data/` — CSV, JSON, SQLite and other data files (where applicable)

---

## 01 — Tools, Environment & Git
Python/data-science toolchain from scratch: what data science is, setting up Anaconda + Jupyter, the command line, Git fundamentals, branching, collaboration, and PEP 8 style.

| Notebook | Topic |
|----------|-------|
| `01_what_is_data_science.ipynb` | DS problem types, OSEMN framework, types of analytics |
| `02_environment_setup.ipynb` | Git, Anaconda, conda environments, Jupyter shortcuts |
| `03_bash_and_command_line.ipynb` | Navigation, file management, pipes, DS shell patterns |
| `04_git_fundamentals.ipynb` | Three states, core workflow, commit messages, cheat sheet |
| `05_git_branching_and_collaboration.ipynb` | Branches, merge conflicts, stash, GitHub PR workflow |
| `06_python_style.ipynb` | PEP 8, naming conventions, import order, auto-formatters |

---

## 02 — Python Fundamentals
Core Python for data science: types, strings, collections, control flow, functions, and a capstone text analysis project.

| Notebook | Topic |
|----------|-------|
| `01_variables_and_types.ipynb` | Variables, int/float/bool/None, truthiness, type coercion |
| `02_strings.ipynb` | String methods, f-strings, slicing, data cleaning patterns |
| `03_collections.ipynb` | Lists, dicts, tuples, sets — creation, indexing, comprehensions |
| `04_conditionals.ipynb` | if/elif/else, comparison operators, ternary expressions |
| `05_loops.ipynb` | for/while, enumerate/zip/range, break/continue |
| `06_functions.ipynb` | def, parameters, *args/**kwargs, scope, lambda, map/filter |
| `07_operators_and_methods.ipynb` | Built-in functions, operator precedence, file I/O |
| `08_macbeth_project.ipynb` | Capstone: word frequency analysis of Shakespeare's Macbeth |

---

## 03 — NumPy, Pandas & Visualization
The core data science computing stack: arrays, DataFrames, and the full visualization pipeline.

| Notebook | Topic |
|----------|-------|
| `01_python_libraries_intro.ipynb` | Stack overview, import conventions, API exploration |
| `02_numpy.ipynb` | Arrays, dtypes, vectorized math, broadcasting, indexing |
| `03_pandas_data_structures.ipynb` | Series, DataFrames, creation patterns, index alignment |
| `04_pandas_data_access.ipynb` | `.loc[]`, `.iloc[]`, boolean indexing, `.query()` |
| `05_importing_data.ipynb` | `read_csv`, JSON, Excel, SQL; key parameters, post-load checklist |
| `06_statistical_analysis_with_pandas.ipynb` | `.describe()`, `.groupby()`, correlation, `.apply()` |
| `07_data_ethics.ipynb` | Bias taxonomy, protected attributes, fairness metrics |
| `08_visualization_with_pandas.ipynb` | `.plot()` API: line, bar, hist, scatter, box |
| `09_visualization_best_practices.ipynb` | Encoding hierarchy, misleading charts, accessibility |
| `10_matplotlib.ipynb` | Figure/Axes architecture, multi-panel layouts, annotations |
| `11_seaborn.ipynb` | Relational, distributional, categorical plots; heatmaps, facets |
| `12_eda_project.ipynb` | Capstone: full EDA on King County house sales (OSEMN) |

---

## 04 — Data Cleaning
Lambda functions, groupby, combining DataFrames, pivot tables, and handling missing data.

| Notebook | Topic |
|----------|-------|
| 01–02 | Combining DataFrames (concat, merge, join) |
| 03 | Data Cleaning Project |
| 04–05 | Dealing with Missing Data |
| 07 | Introduction — Pandas ETL |
| 08–09 | Lambda Functions |
| 10–11 | More on Missing Data |
| 12 | Pandas GroupBy |
| 13–14 | Pivot Tables |
| 15 | Section Recap |

---

## 05 — SQL
SQL fundamentals: selecting, filtering, ordering, grouping, joins, subqueries, database administration, and using SQL with Pandas.

| Notebook | Topic |
|----------|-------|
| 01–02 | Database Admin 101 |
| 03–04 | Filtering & Ordering |
| 05–06 | Grouping Data |
| 07–08 | Join Statements |
| 09 | More Practice with SQL Queries |
| 10–11 | One-to-Many & Many-to-Many Joins |
| 12–13 | Selecting Data |
| 14 | SQL Data Types |
| 15–16 | SQL Interview Questions |
| 17 | SQL Introduction |
| 19–20 | Subqueries |
| 21–22 | Using SQL with Pandas |

---

## 06 — NoSQL
NoSQL database concepts, document stores, MongoDB, and vector databases.

| Notebook | Topic |
|----------|-------|
| 01 | MongoDB Lab |
| 02 | MongoDB |
| 05 | NoSQL Document Stores |
| 06 | Vector Databases |

---

## 07 — JSON & APIs
JSON format, known and unknown JSON schemas, transforming JSON data, web APIs, and LLM APIs.

| Notebook | Topic |
|----------|-------|
| 01–02 | Exploring & Transforming JSON Schemas |
| 03 | JSON & APIs Intro |
| 04–05 | JSON |
| 06–07 | Working with Known JSON Schemas |
| 08 | LLM APIs |

---

## 08 — Web Scraping
HTML and CSS fundamentals, BeautifulSoup, and scraping real websites with Python.

| Notebook | Topic |
|----------|-------|
| 01 | CSS Code Along |
| 02 | HTML & CSS Scraping Intro |
| 03 | HTML & CSS Scraping Recap |
| 05 | HTML Introduction |
| 06 | Intro to CSS |
| 08 | Researching HTML Elements |
| 09 | Scraping Concerts Lab |
| 10 | Scraping Images |
| 11 | Separating Content & Presentation |
| 12–13 | Web Scraping in Practice + Lab |
| 14 | Web Scraping with Beautiful Soup |
