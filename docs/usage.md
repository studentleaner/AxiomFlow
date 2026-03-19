# Usage Architecture

AxiomFlow operates via a strict one-way chain of boundaries guaranteeing deterministic and reliable workflows.

## The Interaction Flow
All steps follow this progression:

**1. DSL (Domain Specific Language)**
Workflows are defined using simplified DSL syntax or declarative python helpers (avoiding internal runtime parameters).

**2. Runner Layer**
The internal `Runner` wraps execution and orchestrates the Axiom Compiler logic via strictly mapped API routes.

**3. Execution (ContextFlow)**
The `Runner` isolates actual functionality by relaying exactly encoded execution packets directly to ContextFlow runtime logic arrays.

AxiomFlow functions strictly as an unbinding wrapper.
It never alters execution plans nor performs independent operation states.
