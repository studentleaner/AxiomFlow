"""
Safely indexes storage configurations tracking file bounds appropriately mimicking Registry reads.
"""
import os
import json
import yaml
# AxiomFlow DSL import is explicitly permitted for safe reading logic.
from axiomflow.dsl.parser import parse_yaml

def list_registry(directory: str = "registry") -> list:
    """Discovers explicitly mapped schema index layouts locally and parses safe metadata attributes."""
    if not os.path.exists(directory):
        return []
    
    items = []
    for f in os.listdir(directory):
        if f.endswith(".yaml") or f.endswith(".json"):
            path = os.path.join(directory, f)
            with open(path, "r") as file:
                content = file.read()
                try:
                    if f.endswith(".yaml"):
                        data = yaml.safe_load(content)
                    else:
                        data = json.loads(content)
                    
                    items.append({
                        "id": f,
                        "type": data.get("type", "unknown"),
                        "version": data.get("version", "1.0"),
                        "tags": data.get("tags", [])
                    })
                except Exception:
                    items.append({
                        "id": f,
                        "type": "error",
                        "version": "unknown",
                        "tags": []
                    })
    return items

def get_item(id: str, directory: str = "registry") -> dict:
    """Safely retrieves a specific item natively."""
    path = os.path.join(directory, id)
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        content = f.read()
    if id.endswith(".yaml"):
        return yaml.safe_load(content) or {}
    return json.loads(content)
