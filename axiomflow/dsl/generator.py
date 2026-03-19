from typing import Dict, Any

def generate_workflow(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts a parsed DSL dictionary model into an Axiom compatible workflow JSON representation.
    Produces valid dict conforming directly to Axiom Core JSON rules.
    """
    workflow_data = data.get("workflow", {})
    return {
        "type": "workflow",
        "id": workflow_data.get("id"),
        "version": workflow_data.get("version", "1.0.0"),
        "nodes": workflow_data.get("nodes", []),
        "edges": workflow_data.get("edges", [])
    }
