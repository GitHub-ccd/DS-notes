# MOD_5 — Changes Log (2026)

## Summary

MOD_5 is an entirely new module, built from scratch in 2026. There was no prior MOD_5 content. The module covers Large Language Models, Generative AI, and AI Agents — the most significant development in machine learning since deep learning.

## New Content

### Section summaries (7)
- `S44_Transformers_Attention/S44_Transformers_Attention.ipynb`
- `S45_HuggingFace_Ecosystem/S45_HuggingFace_Ecosystem.ipynb`
- `S46_LLMs_Prompting_Evaluation/S46_LLMs_Prompting_Evaluation.ipynb`
- `S47_RAG/S47_RAG.ipynb`
- `S48_AI_Agents/S48_AI_Agents.ipynb`
- `S49_LLM_Finetuning/S49_LLM_Finetuning.ipynb`
- `S50_LLMOps/S50_LLMOps.ipynb`

### S44 — Transformers & Attention (5 notebooks)
- `S44_01_attention_mechanism.ipynb` — Scaled dot-product attention from scratch, causal masking, visualization
- `S44_02_multi_head_attention.ipynb` — MultiHeadAttention class, torch.nn.MultiheadAttention, parameter analysis
- `S44_03_transformer_architecture.ipynb` — TransformerBlock, TinyGPT, three architecture families
- `S44_04_positional_encoding.ipynb` — Sinusoidal, learned, RoPE implementations with comparison
- `S44_05_bert_gpt_t5_architectures.ipynb` — BERT/GPT/T5 families with working code, decision guide

### S45 — HuggingFace Ecosystem (5 notebooks)
- `S45_01_huggingface_hub.ipynb` — Hub API, model cards, push_to_hub, Gradio/Spaces, evaluate library
- `S45_02_tokenizers.ipynb` — BPE/WordPiece/SentencePiece, special tokens, batch encoding, tiktoken
- `S45_03_datasets_library.ipynb` — Loading, mapping, filtering, streaming, DataCollator, save/load
- `S45_04_peft_lora.ipynb` — LoRA config, PEFT model wrapping, Trainer API, adapter save/load
- `S45_05_accelerate.ipynb` — Distributed training, mixed precision FP16/BF16, gradient accumulation

### S46 — LLMs, Prompting & Evaluation (5 notebooks)
- `S46_01_what_are_llms.ipynb` — Pre-training/SFT/RLHF, scaling laws (Chinchilla), model landscape 2026
- `S46_02_prompt_engineering.ipynb` — Zero-shot, few-shot, system prompts, JSON mode, temperature
- `S46_03_chain_of_thought.ipynb` — Zero-shot CoT, few-shot CoT, self-consistency, XML structured CoT
- `S46_04_llm_apis.ipynb` — Anthropic/OpenAI/Gemini APIs, streaming, structured output, prompt caching
- `S46_05_llm_evaluation.ipynb` — ROUGE/BLEU, MMLU/benchmarks, LLM-as-judge, pairwise evaluation

### S47 — RAG (5 notebooks)
- `S47_01_why_rag.ipynb` — RAG motivation, hallucination demo, RAG vs fine-tuning vs long context
- `S47_02_document_loading_chunking.ipynb` — LangChain loaders, chunking strategies, overlap tradeoffs
- `S47_03_embeddings_vector_databases.ipynb` — Sentence transformers, FAISS, ChromaDB, model comparison
- `S47_04_retrieval_strategies.ipynb` — Dense vs sparse (BM25), hybrid RRF, cross-encoder reranking, query expansion
- `S47_05_end_to_end_rag.ipynb` — LangChain LCEL RAG chain, ChromaDB, RAG evaluation, failure modes

### S48 — AI Agents & Tool Use (5 notebooks)
- `S48_01_what_are_agents.ipynb` — Agent loop from scratch, tools, memory, planning, when to use agents
- `S48_02_function_calling.ipynb` — Anthropic tool use API, parallel tool calls, tool design best practices
- `S48_03_react_langchain_agents.ipynb` — LangChain tool calling agents, built-in tools, session memory
- `S48_04_langgraph.ipynb` — StateGraph, conditional edges, checkpointing, human-in-the-loop
- `S48_05_multi_agent_frameworks.ipynb` — Supervisor pattern, LangGraph multi-agent, framework landscape

### S49 — LLM Fine-tuning (5 notebooks)
- `S49_01_when_to_finetune.ipynb` — Decision hierarchy, what fine-tuning can/cannot do, data requirements
- `S49_02_lora_qlora.ipynb` — QLoRA memory math, bitsandbytes 4-bit config, training data format, TRL SFTTrainer
- `S49_03_instruction_tuning.ipynb` — Base vs instruction-tuned, Self-Instruct data generation, chat templates
- `S49_04_rlhf_dpo.ipynb` — RLHF vs DPO, preference data format, DPOTrainer, LLM-generated preference pairs
- `S49_05_finetuning_with_unsloth.ipynb` — Unsloth recipe, inference, GGUF export, fine-tuning checklist

### S50 — LLMOps & Deployment (5 notebooks)
- `S50_01_quantization.ipynb` — INT8 math, GGUF format guide, AWQ/GPTQ for GPU, decision guide
- `S50_02_inference_servers.ipynb` — Ollama, vLLM (PagedAttention), streaming TTFT, deployment guide
- `S50_03_llm_monitoring.ipynb` — LLMTrace logging, LangSmith setup, quality monitoring, observability stack
- `S50_04_cost_optimization.ipynb` — Model pricing comparison, prompt caching savings, output length control, app-level caching
- `S50_05_llmops_overview.ipynb` — End-to-end LLMOps wrapper, maturity model, MOD_5 summary table

## API and library choices
- All API notebooks use `claude-haiku-4-5-20251001` (fast, cost-effective for examples)
- Agent/RAG notebooks use `langchain-anthropic` + LangChain LCEL
- Vector search uses `sentence-transformers/all-MiniLM-L6-v2` (no API key required)
- In-process vector store uses `chromadb` (easy setup) and `faiss-cpu` (performance reference)
