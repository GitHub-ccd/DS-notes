# Section 03 — PySpark & Big Data

MapReduce, Resilient Distributed Datasets (RDDs), Apache Spark, and machine learning at scale.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_big_data_analytics_apache_spark.ipynb` | Apache Spark architecture |
| `02_big_data_introduction.ipynb` | Big data concepts — volume, velocity, variety |
| `03_machine_learning_with_spark_lab.ipynb` | ML with Spark lab |
| `04_machine_learning_with_spark.ipynb` | Spark MLlib — pipelines and classification |
| `05_parallel_and_distributed_computing_with_mapreduce.ipynb` | MapReduce — the parallel computing model |
| `06_resilient_distributed_datasets_rdd_lab.ipynb` | RDDs lab |
| `07_spark_docker_installation.ipynb` | Running Spark locally with Docker |
| `08_spark_introduction.ipynb` | Spark introduction — DataFrames, Spark SQL |
| `10_word_count_with_map_reduce_lab.ipynb` | Word count with MapReduce lab |

## 2026 Context

PySpark on a local Docker container is appropriate for learning, but in production Spark now runs almost exclusively on managed cloud platforms: **Databricks** (available on AWS, Azure, and GCP — the most popular Spark platform), **AWS EMR**, **Azure HDInsight/Synapse**, or **GCP Dataproc**. Databricks adds Delta Lake, Unity Catalog, and MLflow integration on top of Spark — making it the de-facto standard for large-scale ML pipelines. If you work with Spark professionally, expect to use Databricks rather than a self-managed cluster.