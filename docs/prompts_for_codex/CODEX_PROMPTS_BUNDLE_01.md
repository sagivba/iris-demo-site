# CODEX Prompt Bundle 01 - Foundation and Documentation

מטרה: להכין את הבסיס לפרויקט כך שהריפו יהיה עקבי, קריא, וניתן להמשך מימוש.
כל המשימות במקבץ זה אמורות להיות בטוחות לביצוע יחד. בסיום המקבץ יש לבצע review ו-pull.

---

## TASK 1 - הקמת שלד הפרויקט

```text
You are working in the iris-demo-site repository.

Goal:
Verify and normalize the project skeleton for a small Iris prediction demo app.

Scope:
- Inspect the current repository structure.
- Ensure the expected directories exist and are used consistently:
  .github/
  .vscode/
  docs/
  model/
  routes/
  services/
  static/
  templates/
  tests/
- Do not add unrelated directories.
- Do not implement application logic yet.
- If placeholder files are missing, create minimal empty or commented placeholders only where needed.

Constraints:
- Keep the structure simple.
- Do not introduce a database layer.
- Do not add authentication or user management.
- Do not rename the repository.
- Preserve existing files unless they are clearly redundant placeholders.

Deliverables:
- A clean, minimal, consistent project structure.
- Brief inline comments only where necessary.

At the end:
- Summarize exactly what files or directories were created, removed, or normalized.
```

---

## TASK 2 - תלויות וסביבת עבודה

```text
You are working in the iris-demo-site repository.

Goal:
Prepare a minimal and correct Python dependency setup for an Iris demo web application.

Scope:
- Review requirements.txt.
- Keep dependencies minimal and directly relevant to:
  - web app runtime
  - model loading / prediction
  - tests
- Remove unnecessary packages if present.
- Do not pin overly complex or experimental tooling unless clearly required.

Constraints:
- The application is a small demo, not a production platform.
- Do not add database dependencies.
- Do not add cloud SDKs.
- Do not add frontend build pipelines.
- Keep the stack lightweight.

Expected outcome:
- requirements.txt is clean and sufficient for local execution and tests.
- If useful, add short dependency grouping comments.

At the end:
- Output a concise explanation of why each dependency is needed.
```

---

## TASK 3 - תיעוד

```text
You are working in the iris-demo-site repository.

Goal:
Create or update README.md so it matches the real purpose of the system.

System purpose:
This project is a demo web app that receives 4 Iris features from the user, runs a trained prediction model, and returns the predicted class.

README must include:
- project purpose
- short architecture overview
- folder structure overview
- setup instructions
- local run instructions
- test run instructions
- example input
- example output
- current limitations
- future improvements

Constraints:
- Keep the README practical and aligned with the current repo.
- Do not document features that do not exist.
- Do not claim production readiness.
- Use clear Markdown.

At the end:
- Ensure the README is accurate to the repository state.
```

---

## TASK 4 - GitHub והעלאה לריפו

```text
You are working in the iris-demo-site repository.

Goal:
Prepare the repository for a clean first implementation cycle from a Git hygiene perspective.

Scope:
- Review .gitignore and make sure it fits a Python demo project.
- Ensure common local/dev artifacts are ignored.
- Do not ignore source files that belong in the repo.
- If useful, add or normalize basic repository hygiene files already expected in the repo.

Constraints:
- Keep .gitignore minimal and correct.
- Do not add CI workflows unless they already exist and only need normalization.
- Do not create noisy meta files.

At the end:
- Provide a short summary of repository hygiene changes.
```
