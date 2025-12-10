TOOLS = {}

def register_tool(name, func):
    TOOLS[name] = func

def detect_smells(code):
    return {"issues": 2}

register_tool("detect_smells", detect_smells)
