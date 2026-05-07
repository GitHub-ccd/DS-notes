# Section 44 — Transformers & Attention Mechanism

The mathematical and architectural foundations of every modern LLM.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_attention_mechanism.ipynb` | Queries, keys, values — scaled dot-product attention from scratch. Why attention replaces recurrence. |
| `02_multi_head_attention.ipynb` | Why multiple attention heads? Attending to different representation subspaces in parallel. |
| `03_transformer_architecture.ipynb` | Full transformer block: encoder, decoder, encoder-decoder. Layer normalisation, residual connections, feed-forward layers. |
| `04_positional_encoding.ipynb` | Sinusoidal and learned positional encodings — giving attention a sense of order. |
| `05_bert_gpt_t5_architectures.ipynb` | The three families: encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5). When to use each. |

## 2026 Context

> The transformer (Vaswani et al., 2017) is the foundational architecture for all modern LLMs. Understanding it is not required to *use* HuggingFace models, but is essential for making informed choices about which model family fits a task and for understanding fine-tuning behaviour.