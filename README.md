# AxiomFlow (v1.0.0)

AxiomFlow is the official usability layer built on top of **Axiom** and **ContextFlow**.

It provides a beginner-friendly, high-level runtime, DSL helpers, execution utilities, and a thin local UI, while keeping the Axiom core compiler fully frozen and deterministic.

**AxiomFlow does NOT replace Axiom.**  
**AxiomFlow does NOT modify Axiom.**  
**AxiomFlow wraps Axiom.**  

Repository:  
https://github.com/studentleaner/AxiomFlow

---

## Architecture

```text
User / Local UI / CLI
      ↓
  AxiomFlow
      ↓
Axiom (Compiler)
      ↓
ContextFlow (Execution Runtime)
      ↓
   Adapters
      ↓
LLM / Tools / Memory
```

---

## Quickstart

**Installation**
```bash
pip install axiomflow
```

**Scaffold a New Workspace**
```bash
axiomflow init my_project
```

**Validate Definition Files**
```bash
axiomflow validate workflows/router.yaml
```

**Build Execution Plan**
```bash
axiomflow build workflow.support_router
```

**Execute the Workflow**
```bash
axiomflow run workflow.support_router
```

**Launch Thin Client Local UI**
```bash
axiomflow-ui
```

---

## The Stack Components

### CLI
The router terminal mapping declarative inputs flawlessly to backend components devoid of executable logic states dynamically overriding pipelines manually.

### DSL / Templates
Parsers (`YAML -> Dictionary -> Axiom JSON schema configuration limits`) safely and robustly asserting schema properties using mock registry endpoints natively.

### Runner
The bridge sequence extracting declarative graphs mapping precisely across boundaries enforcing valid initialization directly inside ContextFlow.

### Simple UI
Allows rapid deployment, review, and editing of configuration nodes visually wrapping tightly around `CLI subprocess.run()` triggers deterministically.

---

## Relationship to Axiom & ContextFlow
AxiomFlow depends entirely on Axiom.  
Axiom does NOT depend on AxiomFlow.  
ContextFlow operates structurally agnostic as the terminal receiver engine binding executing processes strictly according to boundaries established inside `ExecutionPlan` JSON sequences reliably.

---

## Project Status

**Iteration Roadmaps: COMPLETE**
- Iteration 1 — Runner Layer [✔]
- Iteration 2 — DSL / Template Helpers [✔]
- Iteration 3 — CLI + Tooling [✔]
- Iteration 4 — UI + Finalization [✔]

**Project Complete. Version 1.0.0 Released.**
The project roadmap is officially concluded and structurally frozen. Zero further iterations or feature additions will occur. Only security or critical standard bug fixes will be handled natively.

## License
MIT
