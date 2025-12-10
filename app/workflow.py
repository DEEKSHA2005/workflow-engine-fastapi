def extract(state):
    code = state.get("code", "")
    state["functions"] = code.count("def ")
    return state


def check(state):
    state["complexity"] = state["functions"] * 2
    return state


def detect(state):
    state["issues"] = max(0, 10 - state["complexity"])
    return state


def suggest(state):
    # Increase quality score each loop
    state["quality_score"] = state.get("quality_score", 5) + 1
    return state


NODES = {
    "extract": extract,
    "check": check,
    "detect": detect,
    "suggest": suggest
}

EDGES = {
    "extract": "check",
    "check": "detect",
    "detect": "suggest",
    "suggest": None
}
