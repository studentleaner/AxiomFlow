# AxiomFlow CLI Reference

The AxiomFlow CLI provides tools to scaffold, validate, build, and run Axiom workflows reliably without executing runtime logic manually.

## Commands

### `axiomflow init <name>`
Creates a standard project layout. Generates `registry/`, `workflows/`, and `templates/` folders. Handled by `axiomflow.dsl.scaffold`.

### `axiomflow build <workflow>`
Converts a workflow DSL into a deterministic `execution_plan.json` by invoking `axiom.compile`. Must NOT execute logic immediately.

### `axiomflow validate <path>`
Validates your DSL structure strictly against the Axiom Schema (`axiom.AxiomRegistry`) to ensure it correctly maps before any execution takes place. No runtime logic.

### `axiomflow run <workflow>`
Executes an Axiom workflow directly passing through the internal Runner layer which safely pushes the standard payload into ContextFlow.

### `axiomflow search --tag <tag>`
Queries the Axiom registry (`axiom.AxiomRegistry.query()`) for specific defined modules, components, or routines without bespoke modification.
