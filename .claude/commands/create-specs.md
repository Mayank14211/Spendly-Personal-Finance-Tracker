---
description: Create a spec file and feature branch for the next Spendly step
argument-hint: <step_number> <feature_name>
allowed-tools: Read, Write, Glob, Bash(git:*)
---

**User input:** `$ARGUMENTS`

**Step 1 — Check working directory is clean**
- Run `git status --porcelain` to check for uncommitted changes
- If dirty, print error: "Working directory is not clean. Please commit or stash changes first." and exit

**Step 2 — Parse arguments**
- Extract `step_num` (integer) and `feature_title` (rest of the string)
- Generate `feature_slug` from feature_title (lowercase, spaces to hyphens, remove special chars)
- Generate `branch_name` as `feature/step-<step_num>-<feature_slug>`

**Step 3 — Check branch name is not taken**
- Run `git branch --list <branch_name>` 
- If branch exists, print error: "Branch '<branch_name>' already exists." and exit

**Step 4 — Switch to main and pull latest**
- Run `git checkout master`
- Run `git pull origin master`

**Step 5 — Create and switch to the feature branch**
- Run `git checkout -b <branch_name>`

**Step 6 — Research the codebase**
- Read `expense-tracker/app.py` to understand existing routes and structure
- Read `expense-tracker/database/db.py` to understand database schema and patterns
- Read `CLAUDE.md` for project overview and architecture
- Glob for existing spec files in `.claude/specs/` to understand spec format

**Step 7 — Write the spec**
Create a markdown spec file with the following sections:

```markdown
# Step <step_num>: <feature_title>

## Overview
<Brief description of what this feature does and why it's needed>

## New dependencies
<List any new packages/libraries needed, or "None">

## Routes
<List new routes or changes to existing routes in app.py>

## Database changes
<Describe new tables, columns, or changes to database schema>

## Templates
<List new templates or changes to existing templates>

## Files to create or change
<List of files that need to be created or modified>

## Rules for implementation
- <Coding standards and patterns to follow>
- <Security considerations>
- <Any constraints or guidelines>

## Definition of done
- [ ] <Completion criteria 1>
- [ ] <Completion criteria 2>
- [ ] <Completion criteria 3>
```

**Step 8 — Save the spec**
- Write the spec to `.claude/specs/<step_number>-<feature_slug>.md`

**Step 9 — Report to the user**
Print:
```
Branch:    <branch_name>
Spec file: .claude/specs/<step_number>-<feature_slug>.md
Title:     <feature_title>
```
