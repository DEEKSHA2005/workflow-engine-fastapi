# Workflow Engine

A minimal workflow/graph execution engine built using Python + FastAPI, created for the AI Engineering Internship Assignment.

This project demonstrates:

- A lightweight workflow engine
- Node execution with shared state
- Branching + looping
- Graph creation and execution APIs

---

## Project Structure

    app/
        init.py
        main.py
        engine.py
        workflow.py
        tools.py

    requirements.txt
    README.md

---

## Engine Features

### Nodes

Each node is implemented as a simple Python function.

### Directed Edges

Edges define the execution order from one node to the next.

### Shared State

A single state dictionary flows through all nodes, updated at each step.

### Loop Support

The engine supports looping until a condition is met.

### Execution Logs

Each run stores detailed logs showing which nodes executed and in what order.

---

## Sample Workflow: Code Review Agent

Steps:
1)Extract functions
2)Check complexity
3)Detect issues
4)Suggest improvements
5)Loop until quality_score >= 8

---

## Installation

### 1. Clone the repository

    git clone <your_repo_url>
    cd workflow_engine

### 2️. Install dependencies

    pip install -r requirements.txt

### 3️. Start FastAPI server

    uvicorn app.main:app --reload

### 4️. Open the interactive API docs

    http://127.0.0.1:8000/docs

---

## Testing the API

### 1. Create Graph

    POST /graph/create

    Response:
    {"graph_id": "graph1"}

### 2. Run Graph

    POST /graph/run

    Example response:

    {
    "run_id": "run1",
    "final_state": {
    "code": "def a(): pass\ndef b(): pass",
    "quality_score": 8,
    "functions": 2,
    "complexity": 4,
    "issues": 6
    },
    "logs": [
    "Running: extract",
    "Running: check",
    "Running: detect",
    "Running: suggest",
    "Running: check",
    "Running: detect",
    "Running: suggest"
    ]
    }

---

### Future Improvements

- Async Node Execution
- Database Storage
- WebSocket Log Streaming
- Dynamic Graph Creation
- Advanced Branching
- Error Handling & Recovery
- Performance Optimization

---

## Conclusion

This project fulfills all required components of the assignment:

- Workflow engine
- Clean API design
- State management
- Loops + branching
- Demonstrative real example
- Clear and modular folder structure

