# AxiomFlow Local UI

AxiomFlow provides a lightweight local UI utilizing `streamlit`.

**To start the UI:**
```bash
axiomflow-ui
```

## Responsibilities
The UI acts strictly as a thin wrapper interfacing the underlying command-line sequence structure. No runtime capabilities are compiled locally. Internal components interact solely via `subprocess.run(["axiomflow", ...])` CLI requests directly.

- **Viewer**: Read-only display formatting mapping definitions.
- **Editor**: Textual overwrites saving states onto disk transparently.
- **Runner**: Executes internal configurations invoking deterministic contexts seamlessly masking output feedback cleanly onto dashboards safely.
