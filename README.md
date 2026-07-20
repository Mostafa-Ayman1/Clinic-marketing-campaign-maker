# 🚀 AI Marketing Campaign Generator

An AI-powered marketing campaign generator built using **Agentic AI** principles.

The system uses an **Orchestrator Agent** to coordinate multiple specialized AI agents, while leveraging **Parallelization** to execute independent tasks concurrently, reducing latency and improving efficiency.

---

# 🏗️ Architecture

```text
                    User Request
                          │
                          ▼
                  Orchestrator Agent
                          │
                          ▼
                  🔍 Research Agent
                          │
             Structured Research Output
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
   📅 Planner Agent              ✍️ Copywriter Agent
       (Parallel)                    (Parallel)
          │                               │
          └───────────────┬───────────────┘
                          ▼
                 ✅ Synthesizer Agent
                          │
                          ▼
                Final Marketing Campaign
```

---

# 🎯 Design Patterns Used

## 1. Orchestrator Pattern

The workflow is controlled by a dedicated **Orchestrator Agent**.

Responsibilities include:

- Managing the execution order
    
- Passing structured outputs between agents
    
- Coordinating dependencies
    
- Aggregating the final result
    

Instead of allowing agents to communicate directly, the Orchestrator acts as the single coordinator of the workflow.

---

## 2. Parallelization Pattern

Once the Research Agent finishes, two independent tasks are executed simultaneously:

- Planner Agent
    
- Copywriter Agent
    

Using:

```python
await asyncio.gather(
    planner_agent(...),
    copywriter_agent(...)
)
```

This significantly reduces total execution time compared to sequential execution.

---

# 🤖 AI Agents

### 🔍 Research Agent

Responsible for:

- Web research
    
- Market insights
    
- Marketing opportunities
    
- Constraints extraction
    

---

### 📅 Planner Agent

Responsible for:

- Campaign timeline
    
- Publishing schedule
    
- Platform planning
    
- Campaign organization
    

---

### ✍️ Copywriter Agent

Responsible for:

- Headlines
    
- Captions
    
- Hashtags
    
- Call-to-actions
    

---

### ✅ Synthesizer Agent

Responsible for:

- Combining outputs
    
- Validating consistency
    
- Producing the final structured campaign
    

---

# ⚡ Workflow

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
Synthesizer
      ▼
Gradio Dashboard
```

---

# 🛠️ Technologies

- Python
    
- Gradio
    
- OpenAI SDK
    
- Alibaba Qwen
    
- DuckDuckGo Search
    
- asyncio
    

---

# 🧩 AI Engineering Concepts

- Agentic AI
    
- Multi-Agent Systems
    
- Prompt Engineering
    
- Structured JSON Communication
    
- Orchestrator Pattern
    
- Parallelization Pattern
    
- Async Programming
    
- Workflow Automation