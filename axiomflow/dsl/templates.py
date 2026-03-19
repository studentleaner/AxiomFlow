from typing import Dict, Any

def create_support_router() -> Dict[str, Any]:
    """
    Outputs a preset JSON defining a support router workflow instance for Axiom.
    No logic is evaluated.
    """
    return {
        "type": "workflow",
        "id": "workflow.support_router",
        "version": "1.0.0",
        "nodes": ["prompt.detect_intent", "prompt.refund_handler"],
        "edges": [
            {
                "from": "prompt.detect_intent",
                "to": "prompt.refund_handler",
                "condition": {
                    "var": "intent",
                    "equals": "refund"
                }
            }
        ]
    }

def create_rag_workflow() -> Dict[str, Any]:
    """
    Outputs a preset JSON defining a classic RAG search node path.
    """
    return {
        "type": "workflow",
        "id": "workflow.rag_search",
        "version": "1.0.0",
        "nodes": ["tool.web_search", "prompt.synthesize"],
        "edges": [
            {
                "from": "tool.web_search",
                "to": "prompt.synthesize"
            }
        ]
    }

def create_classifier() -> Dict[str, Any]:
    """
    Outputs a preset JSON defining a generic classifier context graph.
    """
    return {
        "type": "workflow",
        "id": "workflow.classifier",
        "version": "1.0.0",
        "nodes": ["prompt.classify"],
        "edges": []
    }
