# AxiomFlow — Delivery Backlog

> **Single source of truth for scope, status and evidence.** Update this file in the same commit as the work it describes. A row is not ✅ until its Evidence column holds something another person can re-run and get the same result.
> Standard: `D:\Code\Projects\project-baseline\BASELINE.md`.

Status: ✅ Done · 🔄 In progress · ⬜ Not started · ⛔ Blocked · 🟡 Deferred · ❌ Dropped (say why)

## Summary

| Area | Outcome | Status |
|---|---|---|
| M0 Foundations | Repo builds, tests run, CI green | 🔄 |
| Production readiness (PRR) | Work the SoftwareFactory `axiomflow.md` plan | 🔄 |

## Production Readiness (PRR-axiomflow) — 🔄 In progress

Generated from `SoftwareFactory/docs/production-readiness/axiomflow.md`. Work lands on branch `prr/axiomflow` (never `main`).

| PRR Task | What | Status | Evidence |
|---|---|---|---|
| PRR-axiomflow-01 | C1 CI pipeline runs — `.github/workflows/ci.yml` (Python 3.12 + sibling Axiom/ContextFlow on PYTHONPATH) | ◐ | `.github/workflows/ci.yml`; created this commit |
| PRR-axiomflow-02 | C2 CI runs the tests — `pytest -q` | ◐ | `.github/workflows/ci.yml` step "Run tests (C2)"; locally `PYTHONPATH=. ;Axiom/src;ContextFlow pytest -q` -> `30 passed` |
| PRR-axiomflow-03 | D2 CLAUDE.md + AGENTS.md (identical `## Rules`) | ◐ | `CLAUDE.md`, `AGENTS.md`; created this commit |
| PRR-axiomflow-04 | D3 docs/DELIVERY_BACKLOG.md | ◐ | `docs/DELIVERY_BACKLOG.md`; created this commit |
| PRR-axiomflow-05 | D4 docs/DECISIONS.md | ◐ | `docs/DECISIONS.md`; created this commit |
| PRR-axiomflow-06 | C3 CI coverage floor — `--cov-fail-under=40` | ◐ | `.github/workflows/ci.yml` step "Coverage floor (C3)"; locally `--cov=axiomflow --cov=axiomstudio` -> `TOTAL 666 377 43%` |
| PRR-axiomflow-07 | C4 CI secret scan — gitleaks (range-scoped) | ◐ | `.github/workflows/secret-scan.yml`; created this commit |
| PRR-axiomflow-08 | O1 Deploy artefact (Dockerfile) | ⬜ | Next (tool - decide whether a container image is appropriate) |
| PRR-axiomflow-09 | V3 wiki-sync space | ⬜ | Owner/infra item |
| PRR-axiomflow-10 | P4 config from env + `.env.example` | ⬜ | Next - `axiomflow/config.py`, `axiomstudio/services/config.py` |
| PRR-axiomflow-11 | P5 deploy + rollback doc | ⬜ | Next |
| PRR-axiomflow-12 | P10 security doc / threat model | ⬜ | Next |
| PRR-axiomflow-13 | P11 QA / acceptance doc | ⬜ | Next |
| PRR-axiomflow-14 | known issue: D2/R3/R4 missing | ◐ partial | D2 closed by -03; R3 + R4 present (scan flags stale) |

### Waiting on owner (PRR-axiomflow)

- **V3 wiki-sync space** — Wiki.js space `projects/axiomflow` not provisioned; owner/infra work.
- **O1 deploy artefact** — AxiomFlow is a tool; whether it ships as a container or a pip package is an owner packaging decision.
- **Runner/Axiom API drift** (known issue `docs/01 §7`: "runner imports Axiom functions that do not exist") — a code fix, out of scope for scaffolding; tracked here for the owner.
