# Custom Slash Commands

This directory contains custom slash commands (skills) for Claude Code to automate common workflows in the py-armodel2 project.

## Available Commands

### `/gh-workflow` - GitHub Workflow Automation
Automates the complete GitHub workflow:
1. Create GitHub issue based on changes
2. Create feature branch
3. Stage and commit changes
4. Push to GitHub only (not gitee)
5. Create pull request

**Usage:**
```
/gh-workflow
/gh-workflow Implement new parser for AUTOSAR models
/gh-workflow feature: Add support for base class extraction
```

### `/test` - Test Runner
Run the project test suite with comprehensive reporting.

**Usage:**
```
/test                    # Run all tests
/test --unit            # Run only unit tests
/test --integration     # Run only integration tests
/test tests/models/test_autosar_models.py  # Run specific test file
```

### `/quality` - Quality Check
Run all quality checks (linting, type checking, testing) to ensure code meets project standards.

**Usage:**
```
/quality        # Run all quality checks
/quality --fix  # Auto-fix linting issues
/quality --test-only  # Run only tests
```

**Quality Gates:**
- ✅ Ruff linting: No errors
- ✅ Mypy type checking: No issues
- ✅ Pytest: All tests pass
- ✅ Coverage: ≥95%

### `/req` - Requirement Management
Manage AUTOSAR project requirements with traceability.

**Usage:**
```
/req add SWR_WRITER_00007 "Add support for custom markdown templates"
/req update SWR_WRITER_00006 maturity accept
/req check traceability
/req list draft
/req search parser
```

### `/gen-class` - Class Generator for AUTOSAR Models
Generate Python classes from AUTOSAR ARXML files based on M2 model definitions with proper type handling and inheritance.

**Usage:**
```
/gen-class                    # Run full workflow with defaults
/gen-class --arxml-file demos/arxml/CustomTypes.arxml
/gen-class --dry-run          # Analysis only, no code changes
/gen-class --update-only      # Update code based on existing report
```

**Workflow Phases:**
1. **Analysis Phase**: Analyze ARXML files, collect class hierarchy information, create documentation
2. **Update Phase**: Update class inheritance chains, verify class members/attributes with proper AUTOSAR type aliases

**Output:**
- Documentation report: `docs/reports/class-todo-items.md`
- Updated class files with correct inheritance
- Summary report of changes

**Key Features:**
- Uses AUTOSAR type aliases (Identifier, CategoryString, String, etc.) instead of raw Python types for better semantics
- All initial values are `None` or `[]` (never `""`, `0`, or `False`)
- Proper list handling with `list[Type]` not `Optional[list[Type]]`

## Creating New Commands

To create a new slash command:

1. Create a new markdown file in `.claude/commands/`
2. The filename becomes the command name (e.g., `debug.md` → `/debug`)
3. Write the workflow instructions in markdown format
4. Use `$ARGUMENTS` to accept dynamic user input

### Example Command Structure

```markdown
# Command Title

Brief description of what the command does.

## Actions

Step-by-step instructions for Claude to follow.

## Usage Examples

```
/command
/command arg1 arg2
```

## Notes

Additional context or constraints.
```

## Best Practices

- **One command per file**: Each file defines one slash command
- **Descriptive names**: Use clear, descriptive command names
- **Project context**: Commands automatically have access to `CLAUDE.md` for project context
- **Use $ARGUMENTS**: Accept dynamic input from users
- **Track progress**: Use TodoWrite tool for multi-step workflows
- **Error handling**: Handle errors gracefully and ask for guidance
- **Show progress**: Report progress updates at each step

## Command Development

When creating or modifying commands:

1. Test the command thoroughly before committing
2. Ensure it follows project coding standards
3. Update this README with new commands
4. Document any special requirements or dependencies
5. Run quality checks: `/quality`

## References

- Project documentation: `CLAUDE.md`
- Requirements: `docs/requirement/requirements.md`
- Coding standards: `docs/development/coding_rules.md`
