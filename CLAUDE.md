# AxiomFlow — Project Intelligence for Claude

The official usability layer built on top of Axiom and ContextFlow: an authoring studio (CLI + Streamlit UI) for prompts, skills and workflow playbooks. Not an engine - it drives Axiom/ContextFlow.

This is the entry point for all AI-assisted work in this repo. `AGENTS.md` carries the same rules for other agents - **edit both in the same commit**; the `## Rules` sections must stay byte-identical (`Test-ProjectBaseline.ps1` checks).

## Reading order (cold start)

1. `README.md` - what it is, how to build/test/run.
2. `docs/DELIVERY_BACKLOG.md` - what is done (with evidence), what is next, what is blocked.
3. `docs/DECISIONS.md` - settled decisions for this repo.
4. `docs/architecture.md` - before touching code.

## Rules

1. **All model calls go through AbstractAI** (`/v1/complete`, prompts from `/v1/prompts`) - never a provider SDK directly.
2. **Import the kit, never copy** - shared code comes from a versioned package/feed.
3. **Creds from Vaultwarden** - no secrets in the repo or in docs (env var *names* only).
4. **Idempotent + config-driven** - no manual steps; re-running is safe.
5. **Verify-then-commit** - build/test green -> commit on a branch -> push.
6. **Docker/data on D:, never C:.**
7. **Status lives in `docs/DELIVERY_BACKLOG.md` only** - update it in the same commit as the work; ✅ needs evidence (command, test name, commit, or dated live check).
8. **Decisions are recorded, not remembered** - a new or reversed decision gets a `D-nn` entry in `docs/DECISIONS.md` in the same commit.
9. **Never edit `docs/SPEC.md` in place** - it is the owner's source text; supersede it through `DECISIONS.md`.

### AxiomFlow-specific (on top of the 9 above)

10. **A usability layer, not an engine** - logic belongs in Axiom/ContextFlow; AxiomFlow orchestrates and presents.
11. **Tests need the sibling components** - `axiomflow.runner` imports `axiom` and `axiomflow.bridge` imports `contextflow`. Run tests with the `Axiom/src` and `ContextFlow` roots on `PYTHONPATH` (CI checks the sibling repos out alongside this one).

## Project specifics

- Slug: `axiomflow` · Stack: Python 3.10+ / Axiom / ContextFlow / Streamlit / networkx · Owner: Pradeep
- Factory role: authoring studio (not an engine).
- No Kanboard/Wiki.js SDLC provisioning yet - tracked in this repo's `docs/DELIVERY_BACKLOG.md`.

## Verify

```text
build:  (no build - pure Python; deps installed in CI)
test:   pytest -q        # with Axiom/src and ContextFlow on PYTHONPATH
run:    python -m axiomflow.cli.main --help   # or: streamlit run axiomstudio/app.py
```

## Where things live

- Packages `axiomflow/` (cli, dsl, ui, runner, bridge), `axiomstudio/` (Streamlit studio + services); tests `tests/`, docs `docs/`.
- CI `.github/workflows/ci.yml`.
- Documentation standard: `D:\Code\Projects\project-baseline\BASELINE.md`.
