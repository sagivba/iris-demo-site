# AGENTS.md

## Purpose

This file defines strict operational rules for AI agents working in this repository.

This repository is a small Flask-based reference implementation for an ML web app using the Iris dataset.
The goal is not just to ship a demo, but to preserve a clean template for future ML web projects.

Act conservatively.
Prefer small, reviewable, low-risk changes.

## Primary Development Context

Assume all local development is performed with:

- WSL
- VS Code connected to WSL
- a dedicated Conda environment
- `unittest` as the only supported test framework

Docker is optional support only.
Do not treat Docker as the default workflow.
Do not replace the WSL + Conda + VS Code workflow.

## Non-Negotiable Rules

1. Use Flask.
2. Use `unittest` only. Never introduce `pytest`.
3. Keep changes small, focused, and easy to review.
4. Do not perform broad refactors unless explicitly requested.
5. Do not introduce a database.
6. Do not retrain the ML model during requests.
7. Do not place ML logic directly inside route handlers.
8. Do not add unnecessary frameworks or dependencies.
9. Preserve a repo structure that is easy for both humans and AI tools to understand.
10. Update documentation when commands, behavior, or structure change.

## Repository Intent

This repo should remain:

- simple
- clear
- modular
- easy to extend
- easy to review
- AI-friendly

Favor explicit structure over cleverness.

## Expected Repository Structure

Maintain this structure unless explicitly instructed otherwise:

- `app.py`
- `requirements.txt`
- `README.md`
- `.env`
- `Dockerfile`
- `docs/dev-python.md`
- `.github/CONTRIBUTING.md`
- `.github/workflows/ci.yml`
- `.vscode/settings.json`
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `routes/`
- `services/`
- `model/`
- `templates/`
- `static/`
- `tests/`

Do not invent additional top-level architecture layers unless requested.

## Layer Responsibilities

### `app.py`
- App entry point.
- App factory is acceptable if requested or already present.
- Keep startup logic simple.

### `routes/`
- Handle HTTP request and response flow only.
- Parse request data.
- Delegate validation and prediction work to services.
- Return rendered HTML or JSON responses.
- Keep route handlers thin.

### `services/`
- Hold application logic.
- This includes validation flow and prediction orchestration.
- Service code may call model-loading or model-prediction utilities.
- Services should remain simple and directly readable.

### `model/`
- Hold training, model loading, and prediction-facing model utilities.
- Store logic related to the persisted model artifact.
- Keep model handling separate from HTTP concerns.

### `templates/`
- HTML templates only.

### `static/`
- CSS and simple static assets only.

### `tests/`
- `unittest` test suite only.
- Must support:
  - `python -m unittest discover -v`

## Task Execution Rules

When implementing tasks:

- Do one logical task at a time.
- Keep diffs minimal.
- Do not combine unrelated changes.
- Do not "clean up" unrelated code.
- Do not rename files unless required.
- Do not move files unless required.
- Do not add placeholders for future systems unless requested.
- Do not create speculative abstractions.

If a requested task has dependencies, state them clearly.
If a task should be done before another, say so explicitly.

## Planning Rules for AI Agents

Before changing code:

1. Identify the exact scope of the task.
2. Change only the files needed for that task.
3. Preserve the intended layering.
4. Keep implementation direct.
5. Update the relevant docs if behavior or commands change.
6. Add or update `unittest` coverage when behavior changes.

## Dependency Policy

Keep dependencies minimal.

Allowed direction:
- Flask for web app
- scikit-learn and model serialization support for the ML flow
- other small supporting packages only when clearly needed

Do not add:
- frontend frameworks
- ORMs
- task queues
- database drivers
- large config frameworks
- dependency managers beyond the chosen local workflow unless explicitly requested

## Validation and Error Handling

Validation should be explicit and easy to follow.
Error responses should be clear and deterministic.
Avoid hidden validation behavior.

For API work:
- return structured JSON errors for invalid input

For HTML form flow:
- return a clear user-facing error path without adding unnecessary frontend complexity

## Testing Policy

Use `unittest` only.

Tests should cover, when implemented:
- home page load
- valid form submission
- invalid form submission
- valid API request
- invalid API request
- prediction service behavior

All tests must work with:

```bash
python -m unittest discover -v
```

Prefer deterministic tests.
Avoid flaky timing-based tests.
Avoid network or external service dependencies.

## Documentation Policy

Keep documentation aligned with implementation.

When relevant, update:
- `README.md`
- `docs/dev-python.md`
- `.github/CONTRIBUTING.md`
- `AGENTS.md`

Documentation should clearly describe:
- setup in WSL
- Conda environment usage
- install commands
- model training commands
- run commands
- test commands
- API usage
- optional Docker usage

## CI Policy

Keep GitHub Actions simple.
CI should run on:
- push
- pull_request

CI should install dependencies and run unit tests.
Do not add unnecessary CI complexity.

## Docker Policy

Docker is optional only.
It may be added as an additional run mode.
It must not become the primary development flow.
Do not redesign the repo around Docker.

## AI-Friendly Repo Rules

This repository should remain easy for AI tools to navigate.

That means:
- predictable file locations
- narrow file responsibilities
- limited indirection
- clear naming
- direct code paths
- docs that match reality

Avoid creating structure that only makes sense after reading many files.

## What to Avoid

Do not:
- over-engineer
- add unused abstraction layers
- introduce patterns with no current need
- hide simple logic behind excessive indirection
- mix web, service, and model concerns
- commit secrets
- add broad formatting-only changes across the repo
- change unrelated files in the same task

## Preferred Delivery Style for AI Agents

For each task:
- make the smallest useful change
- keep the change internally consistent
- ensure tests still pass when applicable
- update docs when needed
- leave the repo in a usable state

If implementation is partial by design, make that explicit in docs or comments only where useful.
Do not add noisy comments.

## When Requirements Are Ambiguous

If ambiguity is small, choose the simplest implementation consistent with the repository rules.
If ambiguity materially affects architecture or workflow, ask before proceeding.

## Summary

Optimize for:
- simplicity
- clarity
- maintainability
- small diffs
- strong boundaries
- easy review
- AI-friendly structure

Do not optimize for sophistication.
