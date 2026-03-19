import argparse
import json
import axiom

def handle(args: argparse.Namespace):
    """
    Handles the `build` route. Explicitly leverages standard `axiom.compile` logic 
    without initiating runtimes.
    """
    workflow_name = args.workflow
    print(f"Building workflow: {workflow_name}...")
    
    # Standard Axiom hooks mapped transparently out logic 
    registry = axiom.load_registry("./registry")
    workflow = registry.get_workflow(workflow_name)
    
    plan = axiom.compile(workflow)
    
    with open("execution_plan.json", "w") as f:
        # Saving strictly bounded output. No executions context invoked.
        json.dump(plan, f, indent=2, default=str)
        
    print("Build complete: execution_plan.json")
