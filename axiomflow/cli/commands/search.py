import argparse
import axiom

def handle(args: argparse.Namespace):
    """
    Searches internal AxiomRegistry definitions.
    """
    tag = args.tag
    print(f"Searching for tag: '{tag}'")
    
    registry = axiom.load_registry("./registry")
    results = registry.query(tag=tag)
    
    if not results:
        print("No matching configurations found.")
        return
        
    for r in results:
        print(f" - {r}")
