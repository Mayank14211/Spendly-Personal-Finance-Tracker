# Step 3: Login and Logout

## Overview
Implement user authentication by adding login and logout functionality. Users will be able to sign in with their email and password, and sign out to end their session. This step introduces session management using Flask's built-in session support.

## New dependencies
None - uses Flask's built-in `session` object which is already available.

## Routes
Modify existing routes in `app.py`:

### `/login` (modified)
- Current: Only handles GET, renders `login.html`
- New: Handle both GET and POST requests
  - GET: Render login form (existing behavior)
  - POST: Process login form submission
    - Validate form data (email, password present)
    - Look up user by email
    - Verify password hash using `check_password_hash`
    - Store user ID in session on success
    - Redirect to profile page on success
    - Re-render form with error message on failure

### `/logout` (modified)
- Current: Returns placeholder string
- New: Clear session data and redirect to landing page
  - Remove user ID from session
  - Redirect to landing page (`/`)

## Database changes
No schema changes needed. Add a new function to `database/db.py`:

- `get_user_by_id(user_id)` - fetches a user by ID (useful for loading logged-in user data)

## Templates
Update `login.html`:
- Form already has POST method to `/login`
- Already has error display block
- No changes needed - template is ready for implementation

## Files to create or change
- `expense-tracker/app.py` - Update `/login` route to handle POST, update `/logout` to clear session
- `expense-tracker/database/db.py` - Add `get_user_by_id()` function

## Rules for implementation
- Use `flask.session` to store user ID after successful login
- Always verify password using `werkzeug.security.check_password_hash`
- Never store password in session - only store user ID
- Use `session.pop()` to clear session data on logout
- Redirect to profile page after successful login (PRG pattern)
- Redirect to landing page after logout
- Provide clear error messages for invalid credentials
- Consider adding a `login_required` decorator pattern for protected routes (future use)
- Follow existing code style in app.py (function-based views, clear route comments)
- Import `session` from Flask at the top of app.py

## Definition of done
- [ ] GET `/login` renders the login form
- [ ] POST `/login` with valid credentials logs user in and redirects to profile
- [ ] POST `/login` with invalid credentials shows error message
- [ ] `/logout` clears session and redirects to landing page
- [ ] Password verification uses `check_password_hash`
- [ ] User ID stored in session after login
- [ ] New database helper function `get_user_by_id()` added to `db.py`
- [ ] Profile route remains placeholder (will be implemented in Step 4)
