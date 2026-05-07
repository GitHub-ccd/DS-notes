# Section 46 — LLMs: Concepts, Prompting & Evaluation

How LLMs are built, how to prompt them effectively, and how to measure their performance.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_what_are_llms.ipynb` | Pre-training on next-token prediction, RLHF, instruction tuning. Scaling laws (Chinchilla). Emergent capabilities. GPT-4, Claude, Gemini, Llama — model landscape. |
| `02_prompt_engineering.ipynb` | Zero-shot, few-shot, system prompts, role prompting. Structured output (JSON mode). Temperature and sampling. Common failure modes. |
| `03_chain_of_thought.ipynb` | Chain-of-thought (CoT), zero-shot CoT ("think step by step"), tree-of-thought, self-consistency. When and why reasoning prompts help. |
| `04_llm_apis.ipynb` | OpenAI, Anthropic, and Gemini API clients. Structured output, streaming, vision inputs, token counting, rate limiting. Prompt caching with Anthropic. |
| `05_llm_evaluation.ipynb` | BLEU/ROUGE (why they're insufficient for LLMs), standard benchmarks (MMLU, HumanEval, MT-Bench), LLM-as-judge pattern, `evaluate` library. |

## 2026 Context

> **Model landscape (2026):** Closed — GPT-4o/o1 (OpenAI), Claude Sonnet/Opus (Anthropic), Gemini 1.5 Pro (Google). Open-weight — Llama 3.x (Meta), Mistral, Qwen2.5, Gemma2. For most tasks, start with a frontier API; fine-tune open-weight only when you need data privacy, cost control, or domain specialisation.