# Section 06 — NoSQL & Vector Databases

Non-relational databases: document stores (MongoDB) and vector databases — the backbone of modern ML retrieval pipelines.

## Notebooks

| # | Notebook | Topic |
|---|----------|-------|
| 01 | `01_nosql_and_mongodb.ipynb` | Why NoSQL, document stores, pymongo CRUD + practice |
| 02 | `02_vector_databases.ipynb` | Embeddings, ChromaDB, FAISS, semantic search, RAG overview |

## 2026 Context

MongoDB is widely used in production web backends but is rarely the right tool for ML/AI workflows. The more relevant NoSQL category for data scientists in 2026 is the **vector database**: ChromaDB, FAISS, Pinecone, Weaviate, and pgvector are the backbone of RAG pipelines and semantic search. `02_vector_databases.ipynb` covers this pattern — it is the bridge to the RAG section in Module 05.
