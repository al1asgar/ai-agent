import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

st.title("AI Agent — Tools in Action")
st.caption("Ask a math or current-events question; the agent picks the right tool. Bring your own OpenAI key — nothing is stored.")

openai_api_key = st.sidebar.text_input("Your API Key", type="password")

@tool
def multiply(a : int, b : int) -> int:
    """Multiply two Integers together"""
    return a*b

search = DuckDuckGoSearchRun()

@tool 
def web_search(query : str) -> str:
    """Search the web for current events, facts, or recent information"""
    return search.run(query)

@st.cache_resource
def build_agent(api_key):
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
    return create_react_agent(model, [web_search, multiply])

question = st.text_input("Ask your question:")

if not openai_api_key:
    st.info("Enter your OpenAI API key in the sidebar to begin")
elif question:
    agent = build_agent(openai_api_key)
    result = agent.invoke({"messages": [("user", question)]})

    st.write(result["messages"][-1].content)

    with st.expander("See the agent's steps"):
        for m in result["messages"]:
            st.markdown(f"**{m.type}**")
            if m.content:
                st.write(m.content)
            if getattr(m, "tool_calls", None):
                st.write(m.tool_calls)
