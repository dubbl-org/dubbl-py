# Contributing to dubbl-py

Thank you for your interest in contributing to the Dubbl Python SDK! This guide will help you get started.

## Development Setup

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/your-username/dubbl-py.git
   cd dubbl-py
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=dubbl --cov-report=term-missing

# Run a specific test file
pytest tests/test_client.py
```

## Code Quality

We use [ruff](https://docs.astral.sh/ruff/) for linting and formatting, and [mypy](https://mypy.readthedocs.io/) for type checking.

```bash
# Lint
ruff check .

# Format
ruff format .

# Type check
mypy src/dubbl
```

## Making Changes

1. **Create a branch** for your changes:
   ```bash
   git checkout -b feat/your-feature
   ```

2. **Make your changes** and ensure:
   - All tests pass
   - Code is properly formatted and linted
   - Type annotations are included for public APIs
   - New features have corresponding tests

3. **Commit your changes** following [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add support for new endpoint
   fix: handle timeout errors correctly
   docs: update README with new examples
   ```

4. **Push your branch** and open a Pull Request.

## Pull Request Guidelines

- Keep PRs focused on a single change
- Include tests for new functionality
- Update documentation if needed
- Ensure CI checks pass

## Adding a New Resource

If the Dubbl API adds a new resource, follow these steps:

1. Create a new file in `src/dubbl/resources/` with both sync and async classes
2. Add the resource to `src/dubbl/resources/__init__.py`
3. Add the resource to both `Dubbl` and `AsyncDubbl` classes in `src/dubbl/_client.py`
4. Add tests in `tests/`
5. Update the README resource table

## Reporting Issues

- Use [GitHub Issues](https://github.com/dubbl-org/dubbl-py/issues) for bug reports and feature requests
- Include Python version, SDK version, and a minimal reproducible example

## Code of Conduct

Be kind and respectful. We're all here to build something useful together.
