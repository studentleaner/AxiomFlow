"""
Main API layer bridging the UI constraints to the AxiomFlow wrapper strictly.
"""
from axiomstudio.services import run as run_service, registry, workflows, logs

def list_workflows():
    return workflows.list_workflows()

def list_registry():
    return registry.list_registry()

def get_registry_item(id: str):
    return registry.get_item(id)

def get_workflow(id: str):
    return workflows.get_workflow(id)

def run_workflow(name: str, inputs: dict):
    return run_service.run(name, inputs)

def get_logs():
    return logs.get_logs()

def get_last_plan():
    return logs.get_last_plan()
