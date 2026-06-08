# Section 07 — JSON & APIs

JSON data structures, REST API patterns, and LLM APIs — the primary API pattern for data scientists in 2026.

## Notebooks

| # | Notebook | Topic |
|---|----------|-------|
| 01 | `01_json_fundamentals.ipynb` | `json` module, load/dump, nested navigation, DataFrame from JSON |
| 02 | `02_exploring_json_schemas.ipynb` | Unknown schema exploration, type-checking loop, nested column expansion |
| 03 | `03_rest_apis_and_json_responses.ipynb` | HTTP methods, `requests`, status codes, known schema patterns |
| 04 | `04_llm_apis.ipynb` | Anthropic/OpenAI messages API, system prompts, structured output, streaming |

## 2026 Context

REST APIs are a foundational skill but LLM APIs have become the most common new API integration for data scientists. Key patterns: `requests.get()`, JSON parsing, API key authentication via environment variables. LLM-specific additions: structured output (JSON mode), streaming responses, tool use (function calling). `04_llm_apis.ipynb` covers the Anthropic and OpenAI patterns in depth.
