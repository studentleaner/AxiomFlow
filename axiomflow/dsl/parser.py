import yaml
from typing import Dict, Any

def parse_yaml(path: str) -> Dict[str, Any]:
    """
    Load a pure YAML file and convert it to a Python dictionary.
    No Axiom schema rules, defaults logic, or builder functions execute here.
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if data is None:
        return {}
    return data
