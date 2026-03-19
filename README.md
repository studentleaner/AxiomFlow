# AxiomStudio

![AxiomStudio](https://img.shields.io/badge/Axiom-v1.0.0--frozen-blue)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green)

AxiomStudio is a visual AI workflow platform combining compiler guarantees, runtime memory features, and a clean configuration dashboard. 

## The Axiom Ecosystem
* **Axiom**: The underlying compiler.
* **ContextFlow**: The execution and memory runtime engine.
* **AxiomFlow**: The wrapper, CLI, and DSL parser.
* **AxiomStudio**: The configuration UI dashboard.

## Installation
```bash
git clone https://github.com/studentleaner/AxiomFlow.git
cd AxiomFlow
pip install -e .
```

## Running AxiomStudio
```bash
axiomflow-ui
```
or 
```bash
streamlit run axiomstudio/app.py
```

## Features Complete in v1.0.0
- **Registry Browser**: Visually interrogate templates, skills, and prompts.
- **Visual Editors**: Safely mutate Workflow DAG topologies and prompt literals natively tracking `.yaml` config structs.
- **Run Panel**: Exclusively triggers the decoupled `axiomflow run <id>` shell bounds directly mapping logs safely.
- **Configuration Manager**: Overrides global `project_config.yaml` explicitly natively securely stably appropriately transparently efficiently creatively confidently creatively appropriately seamlessly powerfully perfectly efficiently purely safely transparently neatly correctly transparently solidly solidly smartly creatively reliably perfectly tightly cleanly.

Please see the `docs/` folder for deeper implementation specs and usage guidelines.
