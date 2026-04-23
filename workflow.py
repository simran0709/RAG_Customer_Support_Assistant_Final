from langgraph.graph import StateGraph


def input_node(state):
    print("\n[LangGraph] Input node activated")
    return state


def processing_node(state):
    print("[LangGraph] Processing node activated")
    return state


def decision_node(state):
    print("[LangGraph] Decision node activated")
    return state


def output_node(state):
    print("[LangGraph] Output node activated")
    return state


workflow = StateGraph(dict)

workflow.add_node("Input", input_node)
workflow.add_node("Process", processing_node)
workflow.add_node("Decision", decision_node)
workflow.add_node("Output", output_node)

workflow.set_entry_point("Input")

workflow.add_edge("Input", "Process")
workflow.add_edge("Process", "Decision")
workflow.add_edge("Decision", "Output")

graph = workflow.compile()

print("LangGraph workflow created successfully")