# DS Notes — Data Science Curriculum

Personal notes, labs, and projects from the Data Science program, organized across five modules covering the full ML pipeline from Python fundamentals to LLMs and AI agents.

---

## Structure

Each module is a self-contained folder with sections numbered 01–NN (restarting within each module). Every section contains flat numbered notebooks and a `README.md` index — no nested lesson subfolders.

**Two organizational styles coexist intentionally:**

- **Modules 01–04** (original curriculum) — sections contain variable numbers of notebooks, paired lesson + `_lab` exercises, `assets/` folders for images, and `data/` folders for datasets.
- **Module 05** (2026 rebuild) — exactly 5 focused notebooks per section, no lab pairs, no assets or data folders. References external resources rather than embedding screenshots. No helper scripts or generated files.

```
DS-notes/
├── 01_Python_DataTools/   # 01–10    Python, Pandas, EDA, SQL, APIs, Webscraping
├── 02_Statistics_Math/    # 01–11    Probability, Statistics, Linear Regression
├── 03_Classical_ML/       # 01–12    ML Algorithms (Logistic Reg, Trees, SVM, etc.)
├── 04_Deep_Learning/      # 01–14    Advanced ML, Deep Learning, NLP, Cloud ML
└── 05_LLMs_GenAI/         # 01–07    Transformers, RAG, Agents, Fine-tuning, LLMOps
```

---

## 01 — Python & Data Tools
**Sections 01–10**

| Section | Topic |
|---------|-------|
| 01 | Data Science Introduction — Python basics, variables, loops, conditionals |
| 02 | Git & Environment Setup — Bash, Git workflows, PEP8 |
| 03 | Control Flow, Functions & Statistics — Functions, loops, measures of central tendency & dispersion, correlation |
| 04 | NumPy, Pandas & Visualization — Arrays, DataFrames, importing data, statistical methods, Pandas plotting |
| 05 | Data Cleaning — Lambda functions, groupby, merging DataFrames, pivot tables, missing data |
| 06 | Seaborn & Visualization — Matplotlib customization, Seaborn, data viz best practices |
| 07 | SQL — Selecting, filtering, joins, subqueries, aggregation, SQL with Pandas |
| 08 | NoSQL — Document stores, MongoDB CRUD |
| 09 | JSON & APIs — JSON schemas, transforming data, working with web APIs |
| 10 | Webscraping — HTML, CSS, BeautifulSoup, scraping in practice |

---

## 02 — Statistics & Math
**Sections 01–11**

| Section | Topic |
|---------|-------|
| 01 | Combinatorics & Probability — Sets, permutations, combinations, conditional probability |
| 02 | Statistical Distributions — PMF, PDF, CDF, Binomial, Normal, z-scores, p-values |
| 03 | Central Limit Theorem — Sampling, CLT, confidence intervals, t-distribution |
| 04 | Hypothesis Testing — Null hypothesis, t-tests, effect sizes, Type I & II errors |
| 05 | ANOVA & Statistical Power — ANOVA, Welch's t-test, KS test, multiple comparisons |
| 06 | A/B Testing — A/B test design, analysis, and in-depth labs |
| 07 | Bayesian Statistics — Bayes' theorem, MLE, MAP, Bayesian vs. frequentist |
| 08 | Simple Linear Regression — OLS, Statsmodels, regression assumptions & diagnostics |
| 09 | Multiple Regression — Categorical variables, feature scaling, cross-validation, multicollinearity |
| 10 | Linear Model Extensions — Bias-variance tradeoff, interaction terms, polynomial regression |
| 11 | Appendix — Monte Carlo simulations, Poisson & exponential distributions, recursive functions |

---

## 03 — Classical ML
**Sections 01–12**

| Section | Topic |
|---------|-------|
| 11 | Object-Oriented Programming — Classes, instances, methods, variables |
| 02 | Linear Algebra — Vectors, matrices, linear equations, regression with NumPy |
| 03 | Calculus & Gradient Descent — Derivatives, gradient descent, cost functions |
| 04 | Regularization — Ridge, Lasso, feature selection, AIC/BIC |
| 05 | Logistic Regression & Evaluation — Confusion matrices, ROC/AUC, class imbalance |
| 06 | MLE & Logistic Regression (Deep Dive) — Coding from scratch, gradient descent review |
| 07 | K-Nearest Neighbors — Distance metrics, finding best K, Scikit-Learn implementation |
| 08 | Naive Bayes — Bayesian classifiers, document classification, Gaussian Naive Bayes |
| 09 | Decision Trees — ID3, entropy, CART, Scikit-Learn, tuning |
| 10 | Ensemble Methods — Random forests, gradient boosting, XGBoost, GridSearchCV |
| 11 | Support Vector Machines — SVM theory, kernel trick, Scikit-Learn |
| 12 | Pipelines — Scikit-Learn pipelines for end-to-end ML workflows |

---

## 04 — Deep Learning
**Sections 01–11**

| Section | Topic |
|---------|-------|
| 01 | PCA — Dimensionality reduction, eigendecomposition, PCA with Scikit-Learn |
| 02 | Clustering — K-means, hierarchical clustering, market segmentation |
| 03 | PySpark & Big Data — MapReduce, RDDs, Apache Spark, ML with Spark |
| 04 | Recommendation Systems — Collaborative filtering, SVD, ALS matrix factorization |
| 05 | Time Series — Trends, decomposition, visualization, stationarity |
| 06 | Time Series Models — ARMA, basic time series models with Statsmodels |
| 07 | NLP — Regular expressions, NLTK, word vectorization, text classification |
| 08 | Neural Networks — Keras, building and training basic neural networks |
| 09 | Deep Learning — Deeper networks, image classification with MLPs |
| 10 | Tuning Neural Networks — Normalization, regularization, end-to-end tuning |
| 11 | Cloud ML Platforms — AWS SageMaker, Azure ML, GCP Vertex AI |

---

## 05 — LLMs & GenAI
**Sections 01–07**

| Section | Topic |
|---------|-------|
| 01 | Transformers & Attention — Self-attention, multi-head attention, positional encoding, BERT/GPT/T5 |
| 02 | HuggingFace Ecosystem — Hub, tokenizers, datasets library, PEFT/LoRA, Accelerate |
| 03 | LLMs — Pre-training/SFT/RLHF, prompt engineering, chain-of-thought, APIs, evaluation |
| 04 | RAG — Chunking, embeddings, vector databases, hybrid retrieval, end-to-end pipeline |
| 05 | AI Agents — Tool use, function calling, LangGraph, multi-agent frameworks |
| 06 | LLM Fine-tuning — When to fine-tune, QLoRA, instruction tuning, DPO, Unsloth |
| 07 | LLMOps — Quantization, inference servers, monitoring, cost optimization |

---

## Tools & Libraries

`Python` `NumPy` `Pandas` `Matplotlib` `Seaborn` `Scikit-Learn` `Statsmodels` `NLTK` `BeautifulSoup` `SQLite` `MongoDB` `PySpark` `PyTorch` `Keras` `HuggingFace` `LangChain` `LangGraph` `FAISS` `ChromaDB` `Anthropic` `AWS SageMaker` `Azure ML` `GCP Vertex AI`
