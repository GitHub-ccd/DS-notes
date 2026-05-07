# Section 47 — RAG: Retrieval-Augmented Generation

Grounding LLM responses in retrieved documents to reduce hallucination and overcome knowledge cutoffs.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_why_rag.ipynb` | Why LLMs hallucinate. Knowledge cutoff problem. Context window economics. RAG as the practical solution — grounding responses in retrieved documents. |
| `02_document_loading_chunking.ipynb` | LangChain / LlamaIndex document loaders (PDF, web, CSV, Notion). Chunking strategies: fixed-size, recursive character, semantic, sentence. Chunk size tradeoffs. |
| `03_embeddings_vector_databases.ipynb` | Embedding models (`text-embedding-3-small`, `all-MiniLM-L6-v2`). Vector databases: ChromaDB (local), Pinecone (managed), FAISS (in-memory), pgvector (Postgres). ANN search algorithms. |
| `04_retrieval_strategies.ipynb` | Semantic search baseline. Hybrid retrieval: BM25 (sparse) + dense (reciprocal rank fusion). Reranking with cross-encoders. Contextual compression. MMR for diversity. |
| `05_end_to_end_rag.ipynb` | Full RAG pipeline with LangChain: load → chunk → embed → store → retrieve → generate. Evaluation with RAGAS (faithfulness, answer relevancy, context recall). |

## 2026 Context

> **RAG vs fine-tuning:** RAG is the default choice when you need to ground answers in a specific, updateable knowledge base (documents, database records, recent news). Fine-tuning is better when you need to change the model's *style*, *format*, or *domain vocabulary* — not just add knowledge. See `06_LLM_Finetuning` for the decision framework.