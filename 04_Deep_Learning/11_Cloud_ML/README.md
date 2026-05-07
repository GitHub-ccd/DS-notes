# Section 11 — Cloud ML Platforms

Productionising ML models on AWS SageMaker, Microsoft Azure ML, and Google Cloud Vertex AI.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_data_science_and_machine_learning_engineering.ipynb` | Data science vs ML engineering — the productionisation gap |
| `02_introduction_to_aws_sagemaker.ipynb` | SageMaker Studio, training jobs, built-in algorithms |
| `03_productionizing_machine_learning_models_section_intro.ipynb` | Section introduction |
| `04_productionizing_machine_learning_models_section_recap.ipynb` | Section recap |
| `05_productionizing_models_with_sagemaker.ipynb` | SageMaker endpoints — deploying a trained model as a REST API |
| `06_the_aws_ecosystem.ipynb` | S3, EC2, IAM, SageMaker — core AWS services for ML |
| `07_azure_ml.ipynb` | Azure ML Studio, pipelines, managed endpoints, MLflow integration |
| `08_gcp_vertex_ai.ipynb` | Vertex AI — AutoML, Pipelines, Model Registry, Gemini integration |

## 2026 Context

AWS, Azure, and GCP each hold roughly 30% of the cloud ML market:

- **AWS SageMaker** — most mature ML platform; broadest set of managed algorithms; common in US enterprise
- **Azure ML** — dominant in Microsoft/Office365 environments; strong MLflow integration; good for hybrid (cloud + on-prem) deployments
- **GCP Vertex AI** — tightest integration with Google's foundation models (Gemini); strong for BigQuery-native ML workflows

All three offer AutoML, managed training, model registry, REST endpoints, and MLOps pipelines. The concepts transfer across platforms — the APIs differ but the patterns are identical.