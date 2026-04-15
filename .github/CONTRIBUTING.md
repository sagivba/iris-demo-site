# Contributing

## Purpose

This repository is a small reference implementation for a future ML-powered web project.
Keep it simple, readable, reviewable, and easy for both humans and AI agents to understand.

This project uses:
- Flask
- WSL for local development
- a dedicated Conda environment
- unittest only
- small, focused changes
- no database
- minimal dependencies
- optional Docker support only

## Working Principles

- Make minimal diffs.
- Prefer small, isolated changes that are easy to review.
- Do not perform broad refactors unless explicitly requested.
- Keep architecture simple.
- Do not introduce new abstractions unless they clearly reduce complexity.
- Keep consistency between code, tests, and documentation.
- Update documentation when behavior, setup, commands, or structure changes.

## Architecture Expectations

Keep responsibilities separated:

- `app.py` is the entry point.
- `routes/` contains HTTP handlers only.
- `services/` contains application logic such as validation and prediction flow.
- `model/` contains training, model loading, and model-facing utilities.
- `templates/` contains HTML templates.
- `static/` contains CSS and static assets.
- `tests/` contains unittest-based test coverage.

Do not place ML logic directly inside route handlers.
Do not retrain the model during a request.
Do not add a database, background worker, or frontend framework unless explicitly requested.

## Environment Rules

Primary local workflow:
- WSL
- VS Code connected to WSL
- Conda environment
- unittest discovery from CLI and VS Code

Docker may be added only as optional support.
Docker must not replace the main local development flow.

## Testing Rules

- Use `unittest` only.
- Do not introduce `pytest`.
- Tests must run with:

```bash
python -m unittest discover -v
```

Add or update tests when changing behavior in:
- routes
- validation
- prediction service
- model loading or prediction flow

Prefer deterministic tests.
Avoid network calls and external service dependencies.

## Dependency Rules

- Keep dependencies minimal.
- Add a dependency only when it is clearly justified.
- Prefer the standard library when practical.
- Do not add tools, frameworks, or libraries that are not required for the current task.

## Secrets and Configuration

- Never commit secrets.
- Never commit credentials, tokens, or private keys.
- Keep environment-specific values out of source control.
- Use `.env` only for local development convenience where appropriate.

## CI Rules

Keep CI green.
Any code change should preserve the ability to run:
- application bootstrap
- unit tests
- GitHub Actions workflow

Do not merge changes that break the documented setup or test commands.

## Documentation Rules

When relevant, update:
- `README.md`
- `docs/dev-python.md`
- `.github/CONTRIBUTING.md`
- `AGENTS.md`

Documentation must stay aligned with:
- repository structure
- local setup steps
- training flow
- run commands
- test commands
- API usage

## Pull Request Guidance

Each PR should aim to do one focused thing.

Good examples:
- bootstrap the repo structure
- add Flask app skeleton
- add model training script
- add prediction service
- add API endpoint
- add validation
- add tests
- improve docs
- add CI
- add optional Docker support

Avoid mixing unrelated changes in one PR.

## Preferred Change Style

Prefer:
- explicit code
- clear names
- small functions
- direct flow
- narrow scope

Avoid:
- speculative abstractions
- hidden magic
- over-engineering
- repo-wide cleanup unrelated to the task
- renaming or moving files without strong reason

## For AI-assisted Contributions

If using Codex or another AI tool:
- keep each task narrow and self-contained
- make one logical change at a time
- preserve existing structure unless instructed otherwise
- update docs together with code
- do not invent missing requirements
- do not create extra layers beyond the intended architecture
