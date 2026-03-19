import os

def init_project(name: str, base_dir: str = ".") -> None:
    """
    Generates a generic standard folders layout for AxiomFlow on disk.
    Not bounded to any active command line execution environment.
    """
    project_path = os.path.join(base_dir, name)
    directories = [
        "registry",
        "workflows",
        "templates"
    ]
    for directory in directories:
        dir_path = os.path.join(project_path, directory)
        os.makedirs(dir_path, exist_ok=True)
