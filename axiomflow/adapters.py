from typing import Dict, Any
from .config import AxiomFlowConfig

def select_adapters(execution_plan: Any, config: AxiomFlowConfig) -> Dict[str, Any]:
    """
    Selects and configures adapters required by the ExecutionPlan.
    """
    adapters = {}
    
    # In Iteration 1, we combine default adapters from the config.
    # Future iterations could inspect the execution_plan to lazily load
    # or select specific adapters (e.g., specific LLM providers).
    adapters.update(config.default_adapters)
    
    return adapters
