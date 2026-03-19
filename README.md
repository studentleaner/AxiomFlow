# AxiomFlow

AxiomFlow is the official usability layer built on top of **Axiom** and **ContextFlow**.

It provides a beginner-friendly, high-level runtime, DSL helpers, and execution utilities while keeping the Axiom core compiler fully frozen and deterministic.

AxiomFlow does NOT replace Axiom.
AxiomFlow does NOT modify Axiom.
AxiomFlow wraps Axiom.

Repository:
https://github.com/studentleaner/AxiomFlow


---

## Philosophy

The ecosystem is split into strict layers:

Axiom → Compiler  
ContextFlow → Runtime / Execution  
AxiomFlow → Usability / Runner / DSL / Integration  

This separation guarantees:

- deterministic execution
- version locking
- no hidden runtime logic
- no framework leaks
- enterprise reproducibility


---

## Architecture


User / CLI / UI
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


AxiomFlow never changes Axiom internals.
AxiomFlow never bypasses ExecutionPlan.
AxiomFlow never executes workflows directly.

All execution goes through ContextFlow.


---

## Goals

AxiomFlow exists to solve the usability gaps of Axiom:

| Gap | Solution |
|------|----------|
| No execution runner | AxiomFlow Runner |
| JSON too manual | DSL / templates |
| No memory / RAG | ContextFlow bridge |
| Not beginner friendly | High-level API |
| No tooling | CLI helpers |
| No ecosystem glue | Integration layer |


---

## Non-Goals

AxiomFlow will NOT:

- modify Axiom schema
- modify Axiom runtime
- modify ExecutionPlan format
- add execution inside Axiom
- add memory inside Axiom
- add RAG inside Axiom
- add UI inside Axiom

If a feature requires core change → rejected.


---

## Roadmap (STRICT — 4 iterations only)

The project must finish in 4 iterations.

No extra phases allowed.

No redesign allowed.

No scope expansion allowed.


### Iteration 1 — Runner Layer

Goal:
Provide simple execution API on top of Axiom + ContextFlow.

Features:

- run(workflow, inputs)
- load registry
- compile plan
- execute via ContextFlow
- adapter selection

Example:

```python
from axiomflow import run

run("workflow.support_router", inputs)
```

Scope:

runner

contextflow bridge

adapter selection

config support

No DSL yet.

Iteration 2 — DSL / Template Helpers

Goal:
Make workflows easier to write.

Features:

YAML DSL

template generators

prompt helpers

workflow builder

schema scaffolding

Example:

axiomflow init support_router

Scope:

DSL parser

JSON generator

template presets

starter kits

No UI yet.

Iteration 3 — CLI + Tooling

Goal:
Provide simple command interface.

Commands:

axiomflow run
axiomflow build
axiomflow validate
axiomflow search
axiomflow init

Scope:

CLI wrapper

runner integration

registry integration

DSL integration

No UI yet.

Iteration 4 — ContextFlow Integration + Memory / RAG helpers

Goal:
Bridge Axiom workflows to ContextFlow features.

Features:

memory helpers

rag helpers

tool helpers

provider config

execution presets

Example:

run(
    "workflow.support_router",
    inputs,
    memory=True,
    rag=True,
)

Scope:

contextflow bridge

helper APIs

execution configs

No UI.
No server.
No agent framework.

After Iteration 4 → PROJECT COMPLETE

Installation
pip install axiomflow

Requirements:

pip install axiom
pip install contextflow
Example
examples/
  support_router/

Run:

axiomflow run examples/support_router
Relationship to Axiom

AxiomFlow depends on Axiom.

Axiom does NOT depend on AxiomFlow.

AxiomFlow must only use public APIs.

Relationship to ContextFlow

ContextFlow is the execution runtime.

AxiomFlow uses ContextFlow to execute ExecutionPlans.

AxiomFlow never executes plans itself.

Project Rules

Core must stay frozen

No architecture changes

No new layers

No runtime inside Axiom

No execution inside Axiom

No more than 4 iterations

After iteration 4 → release

Status

Iteration 1 — pending
Iteration 2 — pending
Iteration 3 — pending
Iteration 4 — pending

License

MIT
