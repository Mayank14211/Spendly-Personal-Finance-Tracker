---
description: Seed realistic dummy expenses for a specific user
argument-hint: <user_id> <count> <months>
allowed-tools: Read, Bash(python3:*)
---

Read `expense-tracker/database/db.py` to understand the expenses table schema, the db connection pattern, and the database file name.

**User input:** `$ARGUMENTS`

**Step 1 — Parse arguments**
- Extract `user_id`, `count` (number of expenses), and `months` (how many months back to generate expenses from today)
- Default `count` to 10 and `months` to 3 if not provided

**Step 2 — Verify user exists**
- Query the users table for the given `user_id`
- If user doesn't exist, print error and exit

**Step 3 — Generate and insert expenses**
- Generate realistic dummy expenses with:
  - `amount`: random between 10-500, rounded to 2 decimals
  - `category`: randomly pick from: Food, Transport, Bills, Health, Entertainment, Shopping, Other
  - `date`: random date within the last `months` months
  - `description`: realistic description matching the category (e.g., "Lunch at cafe" for Food, "Uber ride" for Transport)
  - `user_id`: the provided user_id
  - `created_at`: current datetime
- Use the same `get_db()` pattern from db.py
- Insert all expenses in a single executemany call

**Step 4 — Confirm**
- Print summary:
  - User name and email
  - Number of expenses inserted
  - Date range covered (earliest to latest expense date)
