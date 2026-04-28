# Step 2: Registration

## Overview
Implement the backend logic for user registration. The registration form template already exists with fields for name, email, and password. This step adds the POST handler to validate input, hash the password, check for duplicate emails, and create a new user in the database.

## New dependencies
None - uses `werkzeug.security.generate_password_hash` which is already in the project.

## Routes
Modify `/register` route in `app.py`:
- Current: Only handles GET, renders `register.html`
- New: Handle both GET and POST requests
  - GET: Render registration form (existing behavior)
  - POST: Process registration form submission
    - Validate form data (name, email, password present)
    - Check if email already exists
    - Hash password using `generate_password_hash`
    - Insert new user into database
    - Redirect to login page on success
    - Re-render form with error message on failure

## Database changes
No schema changes needed. The `users` table already exists with:
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `name` (TEXT NOT NULL)
- `email` (TEXT UNIQUE NOT NULL)
- `password_hash` (TEXT NOT NULL)
- `created_at` (TEXT DEFAULT datetime('now'))

Add a new function to `database/db.py`:
- `create_user(name, email, password_hash)` - inserts a new user and returns the user id
- `get_user_by_email(email)` - fetches a user by email to check for duplicates

## Templates
No changes needed. `register.html` already has:
- Form with POST method to `/register`
- Fields: name, email, password
- Error display block for showing validation errors
- Link to login page for existing users

## Files to create or change
- `expense-tracker/app.py` - Update `/register` route to handle POST
- `expense-tracker/database/db.py` - Add `create_user()` and `get_user_by_email()` functions

## Rules for implementation
- Use `request.method` to distinguish between GET and POST in the route handler
- Use `request.form.get()` to access POST data safely
- Always hash passwords using `werkzeug.security.generate_password_hash` before storing
- Check for duplicate emails before inserting to avoid UNIQUE constraint violations
- Provide user-friendly error messages for common failures (email taken, missing fields)
- Redirect to login page after successful registration (PRG pattern - Post/Redirect/Get)
- Use Flask's `redirect()` and `url_for()` for redirects
- Follow existing code style in app.py (function-based views, clear route comments)
- Sanitize/validate user input - ensure password meets minimum length requirement (8 chars)

## Definition of done
- [ ] GET `/register` renders the registration form
- [ ] POST `/register` with valid data creates a new user and redirects to login
- [ ] POST `/register` with duplicate email shows error message
- [ ] POST `/register` with missing fields shows error message
- [ ] Password is hashed before storing in database
- [ ] New database helper functions added to `db.py`
