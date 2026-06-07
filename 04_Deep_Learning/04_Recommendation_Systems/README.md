# Section 04 — Recommendation Systems

Collaborative filtering, SVD matrix factorisation, and ALS-based recommendations with Spark MLlib.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_collaborative_filtering_singular_value_decomposition.ipynb` | SVD for matrix factorisation and latent factor models |
| `02_implementing_recommender_systems_lab.ipynb` | Recommender systems lab |
| `03_implementing_recommender_systems.ipynb` | Building a recommender from scratch |
| `04_matrix_factorization_als.ipynb` | ALS — Alternating Least Squares in Spark MLlib |
| `06_recommendation_system_introduction.ipynb` | Collaborative filtering, content-based, implicit vs explicit ratings |

## 2026 Context

SVD and ALS-based collaborative filtering remain widely used, but LLM-era recommendation systems increasingly use **dense embeddings** instead of sparse user-item matrices. The modern pattern: encode items (products, articles, songs) as embedding vectors using a transformer model; store embeddings in a vector database (Pinecone, Weaviate, ChromaDB, pgvector); at query time embed the user's context and retrieve nearest neighbours by cosine similarity. This approach handles cold-start better and naturally incorporates text metadata. Libraries: `sentence-transformers`, `faiss`, `hnswlib`. See Module 05 Section 04 (RAG) for the underlying retrieval mechanics.