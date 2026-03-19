import argparse
from .commands import init, build, validate, run, search

def main():
    parser = argparse.ArgumentParser(description="AxiomFlow CLI - The Usability Layer for Axiom")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Init
    parser_init = subparsers.add_parser("init", help="Initialize a new AxiomFlow project structure")
    parser_init.add_argument("name", type=str, help="Name of the project")

    # Build
    parser_build = subparsers.add_parser("build", help="Compile a workflow DSL into an Axiom ExecutionPlan JSON")
    parser_build.add_argument("workflow", type=str, help="Name of the workflow to build")

    # Validate
    parser_validate = subparsers.add_parser("validate", help="Validate DSL / JSON workflows strictly via AxiomRegistry")
    parser_validate.add_argument("path", type=str, help="Path to validate")

    # Run
    parser_run = subparsers.add_parser("run", help="Run a compiled Axiom workflow via ContextFlow")
    parser_run.add_argument("workflow", type=str, help="Name of the workflow to run")

    # Search
    parser_search = subparsers.add_parser("search", help="Search the Axiom Registry")
    parser_search.add_argument("--tag", type=str, required=True, help="Tag to search for")

    args = parser.parse_args()

    if args.command == "init":
        init.handle(args)
    elif args.command == "build":
        build.handle(args)
    elif args.command == "validate":
        validate.handle(args)
    elif args.command == "run":
        run.handle(args)
    elif args.command == "search":
        search.handle(args)

if __name__ == "__main__":
    main()
