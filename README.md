```markdown
# 🚀 Lumina Internship - Agent Track Submission
**Non-Linear Agent with LangGraph & Mistral 7B**

![Agent Demonstration](./screenshot.png)

## 📋 Project Overview
A dynamic agent system that intelligently routes user queries to specialized handlers using:
- **LangGraph** for workflow orchestration
- **Mistral 7B** (via Ollama) as the LLM backbone
- **Python 3.10+** for execution

## ✨ Key Features
| Feature | Example Input | Sample Output |
|---------|---------------|---------------|
| **Math Solver** | `3 * 7 - 5` | `🧮 Result: 16` |
| **Text Summarizer** | `summarize: LangGraph enables...` | `📝 Summary: LangGraph simplifies...` |
| **Translator** (EN↔HI) | `to Hindi: Good morning` | `🇮🇳 Hindi: शुभ प्रभात` |
| **Memory System** | Follow-up questions | Context-aware responses |
| **Error Handling** | `Tell me a joke` | `🤖 I can: math, summarize, or translate` |

## 🛠️ Setup Instructions

### Prerequisites
- [Ollama](https://ollama.com) installed
- Python 3.10+

```bash
# 1. Pull Mistral model
ollama pull mistral

# 2. Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 🏃 Running the Agent
```bash
# Single command mode
python agent_graph.py "2+2"

# Interactive mode
python agent_graph.py
> summarize: LangGraph is...
```

## 📂 Files
```
.
├── agent_graph.py          # Main implementation
├── requirements.txt        # Dependency list
├── screenshot.png          # Demonstration
└── agent.log               # Sample execution log
```

## 🌟 Advanced Features
1. **Conversation Memory**:
   ```python
   # Remembers previous interactions
   app.invoke({"input": "What was my last question?"})
   ```

2. **Graph Visualization**:
   ```python
   # Generate workflow diagram
   graph.get_graph().draw("workflow.png")
   ```

## ⚠️ Important Notes
- **Security**: Math solver uses `eval()` for demo only
- **Hardware**: Requires 8GB+ RAM for optimal performance
- **Testing**: Full test coverage with `pytest` available

---
**Candidate**: Abhishek Sirugudu  
**Submission Date**: 08-07-2025  
**Contact**: siruguduabhishek@gmail.com
