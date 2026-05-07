# Section 48 — AI Agents & Tool Use

Building LLM-powered agents that can reason, plan, and take actions using external tools.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_what_are_agents.ipynb` | Agent architecture: perception → memory → planning → action loop. Types of memory (in-context, external, episodic). Single-agent vs multi-agent. When agents beat vanilla LLM calls. |
| `02_function_calling.ipynb` | OpenAI and Anthropic tool use APIs. Defining tools as JSON schemas. Handling tool calls and results in the conversation loop. Parallel tool calls. |
| `03_react_langchain_agents.ipynb` | ReAct (Reason + Act) pattern. LangChain `create_react_agent` with custom tools. Tracing agent steps with LangSmith. |
| `04_langgraph.ipynb` | LangGraph for stateful, graph-based agent workflows. Nodes, edges, conditional branching, human-in-the-loop. When LangGraph beats a simple agent loop. |
| `05_multi_agent_frameworks.ipynb` | Multi-agent patterns: orchestrator-worker, debate, peer review. AutoGen, CrewAI overview. Claude Agent SDK for building production agents on Anthropic's platform. |

## 2026 Context

> **State of agents (2026):** Function calling is now stable across all major model APIs and is the foundation of every production agent. LangGraph and the Anthropic/OpenAI agent SDKs have matured into the primary build surfaces. AutoGen/CrewAI are popular for research and prototyping but less common in production. The biggest unsolved problem is *reliability* — agents still fail on long multi-step tasks at rates that require human-in-the-loop checkpoints.