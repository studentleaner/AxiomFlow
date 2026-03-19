from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class AxiomFlowConfig:
    """Configuration for AxiomFlow runner."""
    registry_path: str = "./registry"
    default_adapters: Dict[str, Any] = field(default_factory=dict)
    execution_timeout: Optional[int] = None
    # Iteration 1 only contains runner/execution settings. 
    # Memory and RAG settings will be added in Iteration 4.
