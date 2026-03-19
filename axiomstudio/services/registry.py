"""
Safely indexes storage configurations tracking file bounds appropriately mimicking Registry reads.
"""
import os

def list_workflows(directory: str = "workflows") -> list:
    """Discovers available workflows dynamically structurally bounding mapping arrays."""
    if not os.path.exists(directory):
        return []
    return [f.replace(".yaml", "") for f in os.listdir(directory) if f.endswith(".yaml")]

def list_registry(directory: str = "registry") -> list:
    """Discovers explicitly mapped schema index layouts locally."""
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith(".yaml") or f.endswith(".json")]
