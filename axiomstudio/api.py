"""
Main API layer bridging the UI constraints to the AxiomFlow wrapper strictly.
"""
from axiomstudio.services import runner, registry, workflows

def list_workflows():
    return workflows.list_workflows()

def list_registry():
    return registry.list_registry()

def get_registry_item(id: str):
    return registry.get_item(id)

def get_workflow(id: str):
    return workflows.get_workflow(id)

def run_workflow(name: str, inputs: dict):
    return runner.run_workflow(name, inputs)

def build_workflow(name: str):
    return runner.build_workflow(name)
