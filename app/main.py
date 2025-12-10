from fastapi import FastAPI
from .engine import WorkflowEngine
from .workflow import NODES, EDGES


app = FastAPI()
engine = WorkflowEngine()

@app.post("/graph/create")
def create_graph():
    graph_id = engine.create_graph(NODES, EDGES)
    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph():
    initial_state = {
        "code": "def a(): pass\ndef b(): pass",
        "quality_score": 5
    }

    run_id, final_state, logs = engine.run_graph("graph1", initial_state)
    return {
        "run_id": run_id,
        "final_state": final_state,
        "logs": logs
    }
