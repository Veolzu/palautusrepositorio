# Repository notes

- This is a coursework collection, not one installable workspace: each exercise with a `pyproject.toml` has its own `uv.lock`. Run `uv sync` and project commands from that exercise's directory; do not assume a root-level test/build command.
- `viikko3/login` is a Flask app with Robot Framework browser tests. Its entrypoint is `src/index.py` (binds `0.0.0.0:5001`); templates are under `src/templates`, and the Robot suites are under `src/tests`.
- For `viikko3/login`, run `uv sync`, then start the app in one terminal with `uv run python src/index.py`; in another, run focused or full tests with `uv run robot src/tests/login.robot` or `uv run robot src/tests`. Tests require the app running on port 5001 and a working Browser/Playwright browser installation (`uv run rfbrowser init` in a fresh environment).
- Browser tests are headed by default (`HEADLESS` is `false` in `src/tests/resource.robot`); use `uv run robot -v HEADLESS:true src/tests` where no visible browser is available.
- The login app stores users in a process-local in-memory repository, not a database. Its Robot setup resets that state through `/tests/reset`; changes to test isolation or persistence should account for that shared singleton.
- Registration username/password validation happens in `src/services/user_service.py`, in `UserService.validate`; login credential checks are in `UserService.check_credentials` in the same file.
