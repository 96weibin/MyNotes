---
name: "summary-tool"
description: "Generates and updates summary for MyNotes project. Invoke when user wants to generate summary, update summary, or manage documentation structure."
---

# Summary Tool Skill

This skill helps manage the summary generation for the MyNotes project. It can generate, update, and monitor the project's SUMMARY.md file based on the Markdown files in the project.

## What This Skill Does

- **Generates Summary**: Creates a comprehensive SUMMARY.md file that lists all Markdown files in the project, organized by directory structure
- **Updates Summary**: Updates the existing SUMMARY.md file when new files are added or existing files are modified
- **Monitors Changes**: Monitors file system changes and automatically updates the summary
- **Git Integration**: Automatically updates the summary when committing changes with Git

## When to Invoke This Skill

Invoke this skill when:
- User asks to generate a summary for the MyNotes project
- User wants to update the existing summary
- User needs to monitor changes to Markdown files
- User wants to integrate summary generation with Git
- User asks about documentation structure management

## Usage Examples

### Generate Summary

```
Generate summary for MyNotes project
Create a summary of all Markdown files
Update the SUMMARY.md file
```

### Monitor Changes

```
Monitor Markdown files for changes
Start watching for file changes
Automatically update summary when files change
```

### Git Integration

```
Set up Git hook for summary update
Configure automatic summary update on commit
```

## How It Works

This skill uses the following scripts:

1. **summary_generator.py**: The main script that scans the project and generates the SUMMARY.md file
2. **watch_summary.py**: Monitors file system changes and automatically updates the summary
3. **Git pre-commit hook**: Automatically updates the summary when committing changes

## Available Commands

### Generate Summary
- **Command**: `python .github/summary-tool/summary_generator.py`
- **Description**: Scans the project and generates a new SUMMARY.md file

### Monitor Changes
- **Command**: `python .github/summary-tool/watch_summary.py`
- **Description**: Starts monitoring file system changes and updates the summary automatically

### Check Git Integration
- **Command**: `cat .git/hooks/pre-commit`
- **Description**: Shows the Git pre-commit hook configuration

## Technical Details

### Script Location
All scripts are located in the `.github/summary-tool/` directory:
- `.github/summary-tool/summary_generator.py`
- `.github/summary-tool/watch_summary.py`
- `.github/summary-tool/README_SUMMARY_TOOL.md` (documentation)

### Git Hook
The Git pre-commit hook is located at `.git/hooks/pre-commit` and is configured to automatically run the summary generator before each commit.

### Dependencies
- **Python 3**: Required for running the main scripts
- **watchdog**: Python library for file system monitoring (install with `pip install watchdog`)

## Troubleshooting

### Common Issues

1. **Script not running**: Ensure Python is installed and added to the system path
2. **Git hook not working**: Check that the hook file has execution permissions
3. **Summary not updating**: Verify that the script paths in the Git hook are correct

### Debugging

To debug issues:
1. Run the summary generator manually to check for errors
2. Check the Git hook output during commit
3. Verify file paths and permissions

## Examples

### Example 1: Generate Summary

**User Request:**
"Generate a summary for my MyNotes project"

**Action:**
Run `python .github/summary-tool/summary_generator.py` to generate the SUMMARY.md file

### Example 2: Monitor Changes

**User Request:**
"Start monitoring my Markdown files for changes"

**Action:**
Run `python .github/summary-tool/watch_summary.py` to start monitoring file system changes

### Example 3: Git Integration

**User Request:**
"Set up automatic summary update on Git commit"

**Action:**
Verify that the `.git/hooks/pre-commit` file is properly configured
