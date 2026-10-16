# AxiomFlow — Decisions

> Architecture/product decision records for **this repo**. Newest last. Never delete an entry — supersede it (`Status: Superseded by D-nn`).

## D-01 — Start from project-baseline

- **Date:** 2026-10-16
- **Status:** Accepted
- **Context:** Every ecosystem repo starts from the same foundation so agents and people can work across repos without re-learning structure.
- **Decision:** Adopt the baseline's Tier 1 documents (`CLAUDE.md`/`AGENTS.md` with identical `## Rules`, `docs/DELIVERY_BACKLOG.md`, `docs/DECISIONS.md`) and the baseline CI/secret-scan workflows. `Test-ProjectBaseline.ps1` must pass at Tier 1.
- **Consequences:** AxiomFlow gains a `docs/` status/ADR layer.

## D-02 — Production-readiness (PRR) work lands on a branch; CI checks out sibling components

- **Date:** 2026-10-16
- **Status:** Accepted
- **Context:** The SoftwareFactory workpack (`axiomflow.md`) requires a CI pipeline, a coverage floor and a secret scan. AxiomFlow imports the sibling components `axiom` (Axiom) and `contextflow` (ContextFlow); `setup.py` declares them as install requirements but their PyPI names are unrelated packages, so `pip install -e .` is not reliable on a clean runner.
- **Decision:** Do the PRR work on branch `prr/axiomflow` (never straight to `main`). CI (`.github/workflows/ci.yml`) clones `studentleaner/Axiom` and `studentleaner/ContextFlow` alongside the repo, puts `Axiom/src` + `ContextFlow` + the repo root on `PYTHONPATH`, installs ContextFlow's runtime deps, then runs the `pytest` entry point and re-runs under `--cov=axiomflow --cov=axiomstudio --cov-fail-under=40`. The secret scan is range-scoped (`.github/workflows/secret-scan.yml`).
- **Consequences:** Measured coverage is ~43% (both `axiomflow` and `axiomstudio`); a 40% floor is deliberately low and should be raised as tests are added. CI depends on the sibling repos' default branches being importable.
