class WorkflowEngine:
    def __init__(self):
        self.graphs = {}
        self.runs = {}

    def create_graph(self, nodes, edges):
        graph_id = "graph1"
        self.graphs[graph_id] = {
            "nodes": nodes,
            "edges": edges
        }
        return graph_id

    def run_graph(self, graph_id, state):
        graph = self.graphs[graph_id]
        nodes = graph["nodes"]
        edges = graph["edges"]

        logs = []
        run_id = "run1"

        current = "extract"

        while True:
            logs.append(f"Running: {current}")
            state = nodes[current](state)

            self.runs[run_id] = state

            # Loop condition
            if current == "suggest":
                if state["quality_score"] >= 8:
                    break
                current = "check"
                continue

            current = edges[current]

        return run_id, state, logs
