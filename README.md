# AI Agent — Tools in Action

An autonomous AI agent that decides which tool to use for your question and chains them to reach an answer. Ask a math question and it uses a calculator tool; ask about current events and it searches the web — the model chooses, you don't.

**Live demo:** https://ai-agent-52.streamlit.app/
*(Bring your own OpenAI key — enter it in the sidebar. Nothing is stored.)*

**Demo video:** `paste your 60-second screen recording link here`

---

## What it does

- Takes a plain-English question and **decides which tool to call** — no manual routing
- `multiply` tool for exact arithmetic; `web_search` tool (DuckDuckGo) for current facts
- Shows the agent's reasoning: a **"See the agent's steps"** panel reveals each tool call and result
- Bring-your-own-key: runs on the visitor's OpenAI key, nothing stored

## How it works

Built on the **ReAct agent loop** (Reason → Act) using LangGraph:

1. The question goes to the model with a list of available tools
2. The model decides: answer directly, or call a tool
3. If it calls a tool, the tool runs and the result is fed back to the model
4. The loop repeats until the model produces a final answer

Under the hood it's a small graph with two nodes — the model and a tool-runner — with an edge that loops back to the model whenever the last message contains tool calls, and stops when it doesn't.

## Tech stack

- Python
- LangGraph — agent orchestration (the ReAct loop)
- LangChain + langchain-openai — model and tool interfaces
- OpenAI (`gpt-4o-mini`) — the reasoning model
- DuckDuckGo (`ddgs`) — web search tool
- Streamlit — UI and hosting

## Run it locally

```bash
git clone https://github.com/al1asgar/ai-agent.git
cd ai-agent
pip install -r requirements.txt
streamlit run agent.py
```

Then enter your OpenAI API key in the sidebar.

## Notes

- **Bring your own key:** uses the visitor's OpenAI API key (entered in the sidebar). No keys are collected or stored.
- The agent is only as current as its tools: web-search answers depend on the live search results returned.
- DuckDuckGo may occasionally rate-limit from shared cloud IPs; the math tool always works, and retrying usually clears a search hiccup.
---

_Built by Aliasgar Dohadwala — an applied-AI project exploring tool-calling and agent orchestration with LangGraph._
