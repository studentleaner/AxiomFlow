"""
Translates UI actions seamlessly bypassing architecture flaws. Connects to `axiomflow.runner`.
"""
import subprocess
from axiomflow import runner

def run_workflow(name: str, inputs: dict):
    """
    Programmatic natively mapped trigger relying strictly on AxiomFlow.
    """
    return runner.run(name, inputs)

def build_workflow(name: str):
    """
    Safely executes the build constraint command-line-tool cleanly isolated.
    """
    result = subprocess.run(["axiomflow", "build", name], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Build failed logic gracefully captured: {result.stderr or result.stdout}")
    return result.stdout
