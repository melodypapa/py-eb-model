# Quality Check

Run all quality checks (linting, type checking, testing) to ensure code meets project standards.

## Quality Checks

When the user runs `/quality`, run the following checks in order:

### 1. Linting with Ruff
```bash
ruff check .
```
- Expected: All checks pass with no errors
- If failures: Show linting errors and offer to fix

### 2. Install Package
```bash
pip install -e .
```
- Expected: Package installs successfully

### 3. Testing with Pytest
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src pytest
```
- Expected: All tests pass
- If failures: Identify failing tests and help debug

### 4. Report Summary
Display a summary table:
```
Check        Status    Details
──────────────────────────────────
Ruff         ✅ Pass    No linting errors
Pytest       ✅ Pass    All tests passed
```

## Quality Gates

All of the following must pass before committing:
1. ✅ Ruff linting: No errors
2. ✅ Pytest: All tests pass

## Arguments

Use `$ARGUMENTS` for specific checks:
- `--lint-only`: Run only linting
- `--test-only`: Run only tests

## Usage Examples

```
/quality
/quality --test-only
```

## References

See `.github/workflows/python-package.yml` for CI/CD configuration.
