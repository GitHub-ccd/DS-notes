# 05 — LLMs & GenAI

Sections 01–07. A new module built from scratch in 2026 covering the transformer era of ML — everything from the attention mechanism through to productionising LLM-powered systems.

Each section folder contains:
- Numbered lesson notebooks: `NN_topic.ipynb`
- `README.md` — section overview and notebook descriptions

**Prerequisite:** 04_Deep_Learning sections 07–10 (NLP, Neural Networks) and S39_14 (HuggingFace `transformers` intro).

---

## 01 — Transformers & Attention Mechanism
The mathematical and architectural foundations of transformer models.

| # | Notebook |
|---|----------|
| 01 | Attention Mechanism — scaled dot-product attention, self-attention |
| 02 | Multi-Head Attention |
| 03 | Transformer Architecture — encoder, decoder, encoder-decoder |
| 04 | Positional Encoding |
| 05 | BERT, GPT, and T5 Architecture Families |

---

## 02 — HuggingFace Ecosystem
The complete HuggingFace toolchain for working with transformer models.

| # | Notebook |
|---|----------|
| 01 | HuggingFace Hub — models, datasets, model cards, Spaces |
| 02 | Tokenizers — BPE, WordPiece, SentencePiece |
| 03 | Datasets Library — loading, mapping, streaming |
| 04 | PEFT & LoRA — parameter-efficient fine-tuning |
| 05 | Accelerate — distributed training, mixed precision |

---

## 03 — LLMs: Concepts, Prompting & Evaluation
Understanding, using, and evaluating large language models.

| # | Notebook |
|---|----------|
| 01 | What Are LLMs — pre-training, RLHF, instruction tuning, scaling laws |
| 02 | Prompt Engineering — zero-shot, few-shot, system prompts, structured output |
| 03 | Chain-of-Thought & Advanced Prompting |
| 04 | LLM APIs — OpenAI, Anthropic, Gemini |
| 05 | LLM Evaluation — benchmarks, BLEU/ROUGE, LLM-as-judge |

---

## 04 — RAG (Retrieval-Augmented Generation)
Building knowledge-grounded LLM systems.

| # | Notebook |
|---|----------|
| 01 | Why RAG — hallucination, knowledge cutoffs, context limits |
| 02 | Document Loading & Chunking |
| 03 | Embeddings & Vector Databases |
| 04 | Retrieval Strategies — semantic, hybrid BM25+dense, reranking |
| 05 | End-to-End RAG Pipeline |

---

## 05 — AI Agents & Tool Use
Building autonomous agents that reason and act.

| # | Notebook |
|---|----------|
| 01 | What Are Agents — perception, memory, action, planning |
| 02 | Function Calling & Tool Use |
| 03 | ReAct Pattern & LangChain Agents |
| 04 | LangGraph — stateful multi-step agents |
| 05 | Multi-Agent Frameworks — AutoGen, CrewAI, Claude Agent SDK |

---

## 06 — LLM Fine-tuning
Adapting pre-trained models to domain-specific tasks.

| # | Notebook |
|---|----------|
| 01 | When to Fine-tune — vs RAG vs prompting decision framework |
| 02 | LoRA & QLoRA |
| 03 | Instruction Tuning & Dataset Formats |
| 04 | RLHF & DPO |
| 05 | End-to-End Fine-tuning with Unsloth & TRL |

---

## 07 — LLMOps & Deployment
Serving, monitoring, and operating LLMs in production.

| # | Notebook |
|---|----------|
| 01 | Quantization — GGUF, GPTQ, AWQ |
| 02 | Inference Servers — vLLM, Ollama, TGI |
| 03 | LLM Monitoring & Observability |
| 04 | Cost Optimization |
| 05 | LLMOps End-to-End Overview |
