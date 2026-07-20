# 🚀 AI Marketing Campaign Generator

An AI-powered marketing campaign generator built using **Agentic AI**, where multiple specialized AI agents collaborate to create a complete marketing campaign from a single user request.

The project demonstrates how to build scalable AI workflows using the **Orchestrator** and **Parallelization** design patterns to coordinate multiple agents efficiently.

---

# ✨ Features

- 🔍 AI-powered market research
- 📅 Automatic campaign planning
- ✍️ AI-generated marketing copy
- ⚡ Parallel execution for faster responses
- 🎯 Structured JSON communication between agents
- 🖥️ Interactive Gradio dashboard
- 📝 Execution logging for debugging

---

# 🏗️ System Architecture

```text
                      User Request
                          │
                          ▼
                🧠 Orchestrator Agent
                          │
         ┌────────────────┼────────────────┐
         │                │                │
         ▼                ▼                ▼
 Research Task     Planner Task    Copywriter Task
         │
         ▼
   🔍 Research Agent
         │
 Structured Research
         │
         ├──────────────────────────┐
         │                          │
         ▼                          ▼
📅 Planner Agent            ✍️ Copywriter Agent
      (Parallel)                 (Parallel)
         │                          │
         └──────────────┬───────────┘
                        ▼
              HTML Formatter + UI
```

---

# 🎯 AI Design Patterns

## 🧠 Orchestrator Pattern

The Orchestrator Agent is responsible for:

- Understanding the user's request
- Breaking the request into specialized tasks
- Generating independent instructions for each agent
- Dispatching tasks to the appropriate AI agents
- Coordinating execution order
- Managing dependencies
- Collecting the outputs

The agents never communicate directly with each other. Every interaction is managed through the Orchestrator.

---

## ⚡ Parallelization Pattern

Only the Research Agent has an execution dependency.

Once research is complete, both the Planner Agent and Copywriter Agent become independent and are executed concurrently using Python's asyncio.

```python
planner_result, copywriter_result = await asyncio.gather(
    planner_agent(planner_input),
    copywriter_agent(copywriter_input),
)
```

Running these agents concurrently significantly reduces total execution time compared to sequential execution.

---

# 🤖 AI Agents

## 🔍 Research Agent

Responsible for:

- Market research
- Competitor analysis
- Audience insights
- Marketing opportunities
- Business constraints
- Structured research output

---

## 📅 Planner Agent

Transforms research into a marketing strategy.

Responsibilities:

- Campaign stages
- Channel strategy
- Content calendar
- Content briefs
- KPIs
- Campaign assumptions

---

## ✍️ Copywriter Agent

Creates campaign content based on the research and planning.

Responsibilities:

- Headlines
- Captions
- Social media posts
- Hashtags
- Call-to-actions

---

# ⚙️ Workflow

```text
User Request
      │
      ▼
Research Agent
      │
      ▼
asyncio.gather(...)
      │
 ┌────┴────┐
 ▼         ▼
Planner  Copywriter
 └────┬────┘
      ▼
Campaign Formatter
      ▼
Gradio Dashboard
```

---

# 🛠️ Tech Stack

- Python
- Gradio
- OpenAI SDK
- Alibaba Qwen
- DuckDuckGo Search
- asyncio

---

# 📂 Project Structure

```text
marketing-campaign-generator/
│
├── agents/
│   ├── orchestrator.py
│   ├── researcher.py
│   ├── planner.py
│   └── copywriter.py
│
├── prompts/
│   ├── copywriter_prompt.txt
│   ├── orchestrator_prompt.txt
│   ├── planner_prompt.txt
│   └── researcher_prompt.txt
│
├── services/
│   └── openai_client.py
│
├── ui/
│   └── gradio_ui.py
│ 
├── utils/
│   ├── formatter.py
│   ├── logger.py
│   └── helpers.py
│
├── app.py
├── config.py
├── log.txt
├── requirements.txt
└── .env.example
```

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/ai-marketing-campaign-generator.git

cd ai-marketing-campaign-generator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Add your API keys.

Run the application:

```bash
python app.py
```

---

# 🔑 Environment Variables

```env
OPENAI_API_KEY=your_key
ALIBABA_API_KEY=your_key
```

---

# 💡 AI Engineering Concepts Demonstrated

- Agentic AI
- Multi-Agent Systems
- Orchestrator Pattern
- Parallelization Pattern
- Prompt Engineering
- Structured JSON Communication
- Async Programming
- Workflow Automation

---
