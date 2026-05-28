# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spendly — a Flask-based personal expense tracking web application. This is an educational project with placeholder routes for students to implement features step-by-step.

## Commands

```bash
# Run the application
python app.py

# Install dependencies
pip install -r requirements.txt

# Run tests (pytest configured via requirements.txt)
pytest
```

## Architecture

**Tech Stack:**
- Backend: Flask 3.1.3 with Jininja2 templating
- Database: SQLite (via `sqlite3` module) — connection helper in `database/db.py`
- Frontend: Vanilla JS, CSS (no frameworks)
- Testing: pytest + pytest-flask

**Structure:**
```
expense-tracker/
├── app.py              # Flask app with routes
├── database/
│   └── db.py          # SQLite connection utilities (students implement)
├── static/
│   ├── css/style.css  # All page styles
│   └── js/main.js     # Frontend JavaScript
└── templates/
    ├── base.html      # Base template (navbar, footer)
    ├── landing.html   # Landing page with hero + features
    ├── login.html     # Login form
    ├── register.html  # Registration form
    ├── terms.html     # Terms and Conditions
    └── privacy.html   # Privacy Policy
```

**Routes (app.py):**
- `/` — Landing page
- `/register`, `/login` — Auth pages (forms rendered, backend not implemented)
- `/terms`, `/privacy` — Static policy pages
- `/logout`, `/profile`, `/expenses/**` — Placeholder routes for students

**Database (database/db.py):**
Students implement three functions:
- `get_db()` — Returns SQLite connection with `row_factory` and foreign keys enabled
- `init_db()` — Creates tables via `CREATE TABLE IF NOT EXISTS`
- `seed_db()` — Inserts sample development data

**Key Implementation Notes:**
- The landing page includes a YouTube modal triggered by "See how it works" button
- All pages extend `base.html` which provides consistent navbar/footer
- The project uses custom design tokens (CSS variables) for theming
- Routes return placeholder strings for unimplemented features — students fill these in

**Critical Rules / Implementation Notes**

  - The landing page includes a YouTube modal
  triggered by "See how it works" button
  - All pages extend base.html which provides
  consistent navbar/footer
  - The project uses custom design tokens (CSS
  variables) for theming
  - Routes return placeholder strings for
  unimplemented features — students fill these in


**Code Style**

  - No specific style guide mentioned in CLAUDE.md
  - Standard Flask/Python conventions expected
  - Educational project — code should be clear and
  instructional

**Preferred Libraries**

  From the tech stack:
  - Flask 3.1.3 (web framework)
  - sqlite3 (built-in Python module for database)
  - pytest + pytest-flask (testing)