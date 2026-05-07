# Section 50 — LLMOps & Deployment

Serving, monitoring, and optimising LLMs in production.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_quantization.ipynb` | Reducing model size for deployment: GGUF (llama.cpp), GPTQ, AWQ, bitsandbytes 4-bit/8-bit. Accuracy vs size tradeoffs. Which format to use when. |
| `02_inference_servers.ipynb` | vLLM (PagedAttention, continuous batching — production standard), Ollama (local dev, easy setup), TGI (HuggingFace Text Generation Inference), llama.cpp (CPU inference). OpenAI-compatible REST APIs. |
| `03_llm_monitoring.ipynb` | What to monitor: latency, cost, token usage, hallucination rate, user feedback. Tools: LangSmith (tracing), Weights & Biases (experiments + prompts), Arize/WhyLabs (drift). LLM-as-judge for automated quality scoring. |
| `04_cost_optimization.ipynb` | Model selection (GPT-4o-mini vs GPT-4o), prompt compression (LLMLingua), semantic caching (GPTCache), batching async requests, prompt caching (Anthropic), context window management. |
| `05_llmops_overview.ipynb` | End-to-end LLMOps architecture: development → evaluation → deployment → monitoring → feedback loop. CI/CD for prompts. The LLMOps stack in 2026. |

## 2026 Context

> **The LLMOps stack (2026):**
>
> | Layer | Tools |
> |-------|-------|
> | Development | VS Code + Claude Code, JupyterLab, Cursor |
> | Experiment tracking | MLflow, W&B, LangSmith |
> | Fine-tuning | Unsloth, Axolotl, TRL |
> | Serving (self-hosted) | vLLM, Ollama, TGI |
> | Serving (managed) | AWS Bedrock, Azure OpenAI, Vertex AI |
> | Observability | LangSmith, Arize, Helicone |
> | Evaluation | RAGAS, DeepEval, Promptfoo |