# Section 49 — LLM Fine-tuning

When and how to fine-tune open-weight LLMs using parameter-efficient methods.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_when_to_finetune.ipynb` | Decision framework: prompting → RAG → fine-tuning → train from scratch. Cases where fine-tuning wins (style, format, cost/latency, privacy). Cases where it's a trap. |
| `02_lora_qlora.ipynb` | Why full fine-tuning is impractical for most. LoRA: low-rank decomposition of weight updates. QLoRA: 4-bit base model + LoRA adapters — fine-tuning a 7B model on a single consumer GPU. |
| `03_instruction_tuning.ipynb` | Dataset formats: Alpaca, ShareGPT, ChatML. Building a supervised fine-tuning dataset. Data quality over quantity. `trl` `SFTTrainer`. |
| `04_rlhf_dpo.ipynb` | RLHF: reward model + PPO loop. Why it's complex. DPO (Direct Preference Optimisation) as a simpler, more stable alternative. `trl` `DPOTrainer`. |
| `05_finetuning_with_unsloth.ipynb` | End-to-end QLoRA fine-tuning with Unsloth (2–5× faster than vanilla HuggingFace). Load → prepare dataset → train → save/push → run inference. |

## 2026 Context

> **Toolchain (2026):** Unsloth + TRL is the fastest path to QLoRA fine-tuning on a single GPU. For multi-GPU, use Axolotl or DeepSpeed + HuggingFace `Trainer`. For managed cloud fine-tuning, all three cloud providers offer API-based fine-tuning (OpenAI fine-tune API, Azure ML, Vertex AI). `pip install unsloth trl peft accelerate bitsandbytes`