"""
Main API layer bridging the UI constraints to the AxiomFlow wrapper strictly.
"""
from axiomstudio.services import runner, registry

def list_workflows():
    return registry.list_workflows()

def list_registry():
    return registry.list_registry()

def run_workflow(name: str, inputs: dict):
    return runner.run_workflow(name, inputs)

def build_workflow(name: str):
    return runner.build_workflow(name)
