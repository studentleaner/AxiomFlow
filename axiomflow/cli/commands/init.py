import argparse
from axiomflow.dsl import scaffold

def handle(args: argparse.Namespace):
    """
    Handles `init` logic explicitly passing to DSL's scaffold functions.
    Does not execute Axiom engine APIs.
    """
    name = args.name
    print(f"Creating project structure for: {name}")
    
    # Delegated operation mapping to strict underlying tool
    scaffold.init_project(name)
    
    # Optionally build axiomflow.yaml marking it
    with open(f"{name}/axiomflow.yaml", "w") as f:
        f.write(f"project: {name}\nversion: 1.0\n")
        
    print("Project initialized successfully.")
