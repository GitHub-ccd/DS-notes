# MOD_4 Changes (2026 Update)

## Summary notebooks — all 14 rewritten

All section summaries (S33–S43 + CNN, Transfer Learning, Graph Theory) had broken `dsc-*` links or outdated content. Each was rewritten as a clean index with working relative links and 2026 context annotations.

| Section | Summary notebook | Notes |
|---------|-----------------|-------|
| S33 | PCA | Fixed links |
| S34 | Clustering | Fixed links; renamed `Section_33_clustering.ipynb` → `Section_34_clustering.ipynb` |
| S35 | PySpark | Fixed links; added Databricks context note |
| S36 | Recommendation Systems | Fixed links; added LLM/embedding-based recommendation note |
| S37 | Time Series | Fixed links |
| S38 | Time Series Models | Fixed links; added Prophet/NeuralProphet/Statsforecast context note |
| S39 | NLP | Fixed links; added NLTK legacy warning; added link to new Transformers notebook |
| S40 | Neural Networks | Fixed links; added PyTorch vs Keras comparison table |
| S41 | Deep Learning | Fixed links; added PyTorch and ViT forward reference |
| S42 | Tuning Neural Networks | Fixed links; added LR schedulers, Optuna, LayerNorm note |
| S43 | Cloud ML Platforms *(renamed from AWS-only)* | Fixed links; expanded to cover all 3 clouds |
| CNN | Convolutional Neural Networks | Links valid (content is local); added ViT/PyTorch context note |
| Transfer Learning | Transfer Learning | Links valid; added LoRA/foundation model context note |
| Graph Theory | Graph Theory | Links valid; added GNN/PyTorch Geometric context note |

## Content additions

### S35 — PySpark
Added `2026 context` note: Spark now runs almost exclusively on managed cloud platforms (Databricks, EMR, HDInsight, Dataproc). Databricks is the de-facto standard.

### S36 — Recommendation Systems
Added `2026 context` note: LLM-era recommendations use dense embeddings + vector databases. Pattern: encode items → store in vector DB → retrieve nearest neighbours at query time.

### S38 — Time Series Models
Added `2026 context` note: Prophet/NeuralProphet for business time series; Statsforecast for fast classical models; TimeGPT/Chronos for zero-shot forecasting.

### S39 — NLP
- Added `⚠️ LEGACY NOTE` at top: NLTK-based content is foundational but not the current production standard
- Added 2026 NLP section header in summary pointing to the new Transformers notebook

### S40–S42 — Neural Networks
- S40: Added Keras vs PyTorch comparison table with recommendation
- S41: Added forward reference to CNNs, Transformers, and PyTorch equivalents
- S42: Added LR schedulers, gradient clipping, Optuna, LayerNorm notes

### CNN, Transfer Learning, Graph Theory extras
- CNN: Added ViT/CLIP context and `torchvision`/HuggingFace paths
- Transfer Learning: Added LoRA/QLoRA note; broader foundation model context
- Graph Theory: Added GNN/PyTorch Geometric/DGL context note

## New notebooks

### `S39_14_transformers_huggingface.ipynb`
HuggingFace `transformers` + `datasets` for 2026 NLP:
- `pipeline` API for sentiment, NER, zero-shot classification
- Fine-tuning DistilBERT on text classification with `Trainer`
- Sentence embeddings with `sentence-transformers`
- spaCy for production NLP pipelines
- Quick-reference table of tasks → libraries → models

### `S43_07_azure_ml.ipynb`
Microsoft Azure Machine Learning:
- Core concepts + comparison table vs AWS SageMaker
- Workspace connection with `azure-ai-ml` SDK
- MLflow experiment tracking (native Azure ML integration)
- Custom training job submission
- Model registration + Managed Online Endpoint deployment
- Azure ML vs SageMaker differences table

### `S43_08_gcp_vertex_ai.ipynb`
Google Cloud Vertex AI:
- Core concepts + comparison table vs AWS SageMaker
- Custom training job with pre-built containers
- MLflow-compatible experiment tracking
- Model deployment to Vertex AI Endpoints (auto-scaling)
- Vertex AI Pipelines with Kubeflow Pipelines SDK
- Gemini foundation model access via `vertexai` SDK
- Three-way comparison table: Vertex AI vs SageMaker vs Azure ML

## Clutter removed

| Item | Reason |
|------|--------|
| `reorganize.py` (root) | One-off utility script, no longer needed |
| `S34_clustering/Section_33_clustering.ipynb` | Wrong section number in filename; replaced by `Section_34_clustering.ipynb` |
| `S35_pyspark/ds-spark-sparkcontext-onl01-dtsc-ft-030220/` | Legacy nested Flatiron repo; SparkContext content is in the numbered notebooks |
| `S36_Recommendation_Systems/als-recommender-system-pyspark-lab-onl01-dtsc-ft-030220/` | Legacy nested Flatiron repo |

Note: CNN, Graph_Theory, and Transfer_Learning nested `dsc-*` repos were **kept** — they are the sole source of lesson content for those sections (no numbered notebooks exist for them).
