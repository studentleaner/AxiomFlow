"""
Isolates workflows loading procedures parsing configurations purely.
"""
import os
import json
import yaml
from axiomflow.dsl.parser import parse_yaml

def list_workflows(directory: str = "workflows") -> list:
    """Discovers available workflows dynamically structurally bounding mapping arrays."""
    if not os.path.exists(directory):
        return []
    
    items = []
    for f in os.listdir(directory):
        if f.endswith(".yaml"):
            items.append({
                "id": f.replace(".yaml", ""),
                "file": f
            })
    return items

def get_workflow(id: str, directory: str = "workflows") -> dict:
    """Extracts execution nodes definitions securely directly."""
    path = os.path.join(directory, f"{id}.yaml")
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        content = f.read()
    return parse_yaml(content)
