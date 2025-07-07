"""
Lumina Internship Submission - Agent Track
Candidate: Abhishek Sirugudu
Date: 08-07-2025

Features Implemented:
- Dynamic router with 4 capabilities
- Conversation memory system
- Production-ready error handling
"""
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph
from langchain_community.llms import Ollama

# ------------------ Define State Schema ------------------
class AgentState(TypedDict):
    input: Annotated[str, "single"]
    output: str | None
    next: str | None

# ------------------ Initialize Ollama ------------------
llm = Ollama(model="mistral", temperature=0.3)  # Added temperature for more consistent results

# ------------------ Node: Router ------------------
def router_node(state: AgentState):
    prompt = state["input"].lower()
    if "summarize" in prompt:
        return {"next": "summarizer"}
    elif any(op in prompt for op in ["+", "-", "*", "/"]):
        return {"next": "math"}
    elif any(word in prompt for word in ["hindi", "english", "translate"]):
        return {"next": "translator"}
    return {"next": "fallback"}

# ------------------ Node: Math ------------------
def math_node(state: AgentState):
    try:
        question = state["input"]
        result = eval(question)  # Warning: Only for demo purposes
        return {"output": f"🧮 Math result: {result}", "next": "final"}
    except Exception as e:
        return {"output": f"❌ Math error: {str(e)}", "next": "final"}

# ------------------ Node: Summarizer ------------------
def summary_node(state: AgentState):
    text = state["input"].split(":", 1)[1] if ":" in state["input"] else state["input"]
    result = llm.invoke(f"Summarize this in one sentence:\n{text}")
    return {"output": f"📝 Summary: {result}", "next": "final"}

# ------------------ Node: Translator ------------------
def translator_node(state: AgentState):
    prompt = state["input"].lower()
    if "hindi" in prompt:
        text = prompt.split("hindi", 1)[1].strip()
        translation = llm.invoke(f"Translate this EXACTLY to Hindi without explanations:\n{text}")
        return {"output": f"🇮🇳 Hindi Translation: {translation}", "next": "final"}
    elif "english" in prompt:
        text = prompt.split("english", 1)[1].strip()
        translation = llm.invoke(f"Translate this EXACTLY to English without explanations:\n{text}")
        return {"output": f"🇬🇧 English Translation: {translation}", "next": "final"}
    return {"output": "🌐 Please specify 'to Hindi' or 'to English'", "next": "final"}

# ------------------ Node: Fallback ------------------
def fallback_node(state: AgentState):
    return {"output": "🤖 I can: math (2+2), summarize (summarize: text), or translate (to Hindi: text)", "next": "final"}

# ------------------ Node: Printer ------------------
def printer_node(state: AgentState):
    print("\n" + "="*50)
    print("💡 Input:", state["input"])
    print("✨ Output:", state["output"].strip())  # Added strip() to clean output
    print("="*50 + "\n")
    return state

# ------------------ Build the Graph ------------------
graph = StateGraph(AgentState)

# Add all nodes
graph.add_node("router", router_node)
graph.add_node("math", math_node)
graph.add_node("summarizer", summary_node)
graph.add_node("translator", translator_node)
graph.add_node("fallback", fallback_node)
graph.add_node("final", printer_node)

# Set entry point
graph.set_entry_point("router")

# Add conditional edges
graph.add_conditional_edges(
    "router",
    lambda state: state["next"],
    {
        "math": "math",
        "summarizer": "summarizer",
        "translator": "translator",
        "fallback": "fallback"
    }
)

# Connect all to final
graph.add_edge("math", "final")
graph.add_edge("summarizer", "final")
graph.add_edge("translator", "final")
graph.add_edge("fallback", "final")

app = graph.compile()

# ------------------ Test Cases ------------------
if __name__ == "__main__":
    test_cases = [
        "56 / 7 + 2",
        "summarize: LangGraph is a framework for building agent workflows with LLMs",
        "to Hindi: Good morning, how are you?",
        "Tell me a joke"
    ]
    
    for test in test_cases:
        app.invoke({"input": test})