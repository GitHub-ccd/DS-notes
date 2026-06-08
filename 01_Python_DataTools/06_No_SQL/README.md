# Section 08 — NoSQL & Vector Databases

Non-relational databases: document stores (MongoDB) and vector databases — the backbone of modern ML retrieval pipelines.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_mongodb_lab.ipynb` | MongoDB CRUD lab |
| `02_mongodb.ipynb` | MongoDB with pymongo — insert, find, update, delete |
| `05_nosql_document_stores.ipynb` | Document store concepts — JSON documents, flexible schema |
| `06_vector_databases.ipynb` | Vector databases — ChromaDB, FAISS, semantic search |

## 2026 Context

MongoDB is widely used in production web backends but is rarely the right tool for ML/AI workflows. The more relevant NoSQL category for data scientists in 2026 is the **vector database**: ChromaDB, FAISS, Pinecone, Weaviate, and pgvector are the backbone of RAG pipelines and semantic search. `06_vector_databases.ipynb` covers this pattern — it is the bridge to the RAG section in Module 05.