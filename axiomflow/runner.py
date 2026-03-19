from typing import Any, Dict, Optional

# Assuming axiom API exists in the environment based on project philosophy
import axiom

from .config import AxiomFlowConfig
from .adapters import select_adapters
from .bridge import ContextFlowBridge

def run(workflow_name: str, inputs: Dict[str, Any], config: Optional[AxiomFlowConfig] = None) -> Dict[str, Any]:
    """
    Run an Axiom workflow using ContextFlow as the execution engine.
    
    Args:
        workflow_name (str): The name or path of the workflow in the registry.
        inputs (Dict[str, Any]): Dictionary of inputs matching the workflow schema.
        config (Optional[AxiomFlowConfig]): Optional configuration overrides.
        
    Returns:
        Dict[str, Any]: The final execution result returned by ContextFlow.
    """
    if config is None:
        config = AxiomFlowConfig()
        
    # 1. Load registry
    registry = axiom.load_registry(config.registry_path)
    
    # 2. Compile plan
    workflow = registry.get_workflow(workflow_name)
    execution_plan = axiom.compile(workflow)
    
    # 3. Adapter selection
    adapters = select_adapters(execution_plan, config)
    
    # 4. ContextFlow bridge execution
    bridge = ContextFlowBridge(adapters=adapters, config=config)
    result = bridge.execute(execution_plan, inputs)
    
    return result
