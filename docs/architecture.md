# Finalized Architecture Stack

AxiomFlow rests logically encapsulated over the underlying runtime mechanisms securely ensuring clean decoupling:

### The Layers
`UI -> CLI -> Runner -> Axiom -> ContextFlow`

1. **AxiomFlow UI**: Simple local graphical display over operations executing subprocess hooks strictly.
2. **AxiomFlow CLI**: The central router linking actions contextually mapping to python models independently avoiding state overlap.
3. **Runner**: Component orchestrating cleanly `axiom.compile` routines bound seamlessly interacting directly inside ContextFlow.
4. **Axiom**: The compiler and registry index schema model, functionally unobservable externally and frozen permanently.
5. **ContextFlow**: Terminal structured executor processing strictly `ExecutionPlan` boundaries without modification locally.
