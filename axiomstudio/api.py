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

def save_workflow_file(id: str, data: dict):
    from axiomstudio.services import editor
    editor.save_workflow_file(id, data)

def load_workflow_file(id: str):
    from axiomstudio.services import editor
    return editor.load_workflow_file(id)

def load_registry_file(id: str):
    from axiomstudio.services import editor
    return editor.load_registry_file(id)

def save_registry_file(id: str, data: dict):
    from axiomstudio.services import editor
    editor.save_registry_file(id, data)

def get_config():
    from axiomstudio.services import config as conf
    return conf.load_config()

def save_config(data: dict):
    from axiomstudio.services import config as conf
    conf.save_config(data)
