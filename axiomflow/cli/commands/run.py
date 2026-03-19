import argparse
from axiomflow import runner

def handle(args: argparse.Namespace):
    """
    Run command strictly invokes run API created inside Iteration 1 runner.py.
    The CLI must NEVER intercept or manually communicate with ContextFlow 
    bypassing the core runner wrapper layer.
    """
    workflow_name = args.workflow
    print(f"Executing workflow sequence: {workflow_name}")
    
    inputs = {}
    
    # Runner cleanly orchestrates the execution chain
    result = runner.run(workflow_name, inputs)
    
    print("\nExecution Complete:")
    print(result)
