from typing import Dict, Any

# Must only utilize public Registry layer, without any reference
# to runtime models executing constraints.
from axiom import AxiomRegistry

def validate_workflow_json(workflow_json: Dict[str, Any]) -> bool:
    """
    Validates a defined workflow dictionary mapping by executing ONLY Axiom's
    Registry registration procedure. Ensuring structure meets standard bounds.
    """
    registry = AxiomRegistry()
    try:
        # Pushing into a dummy registry strictly validates internal schemas.
        registry.register_workflow(workflow_json)
        return True
    except Exception:
        return False
