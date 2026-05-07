# Section 45 — HuggingFace Ecosystem

The complete HuggingFace toolchain for working with pre-trained models.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_huggingface_hub.ipynb` | Navigating the Hub: finding models, reading model cards, pushing to Hub, using Spaces and Gradio for demos. |
| `02_tokenizers.ipynb` | BPE, WordPiece, SentencePiece — how text becomes token IDs. Special tokens, padding, truncation, fast tokenizers. |
| `03_datasets_library.ipynb` | `datasets` library: loading from Hub, mapping transforms, filtering, batched processing, memory-mapped Arrow format, streaming for large datasets. |
| `04_peft_lora.ipynb` | PEFT library: LoRA configuration, adding adapters to a base model, training only adapter weights, merging adapters back for deployment. |
| `05_accelerate.ipynb` | `accelerate` for device-agnostic training: single GPU → multi-GPU → mixed precision (fp16/bf16) with zero code changes. |

## 2026 Context

> Key libraries: `transformers`, `datasets`, `peft`, `accelerate`, `evaluate`, `trl` — all from HuggingFace. Install with `pip install transformers datasets peft accelerate evaluate trl`. Entry point is `04_Deep_Learning/07_NLP/14_transformers_huggingface.ipynb` which covers the `pipeline` API and basic fine-tuning; this section goes deeper.