from flask import Flask, render_template, request, redirect, url_for, session
from database.db import init_db, seed_db, get_user_by_email, get_user_by_id, create_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "spendly-dev-secret-key-change-in-production"


@app.context_processor
def inject_user():
    """Make user info available to all templates when logged in."""
    if session.get("user_id"):
        user = get_user_by_id(session["user_id"])
        if user:
            return {"user_name": user["name"], "user_email": user["email"]}
    return {}


with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Extract form data
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Validate input
        if not name or not email or not password:
            return render_template("register.html", error="All fields are required")

        if len(password) < 8:
            return render_template("register.html", error="Password must be at least 8 characters")

        # Check for duplicate email
        existing_user = get_user_by_email(email)
        if existing_user:
            return render_template("register.html", error="Email already registered")

        # Create new user
        password_hash = generate_password_hash(password)
        create_user(name, email, password_hash)

        # Redirect to login page
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Extract form data
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Validate input
        if not email or not password:
            return render_template("login.html", error="Email and password are required")

        # Look up user by email
        user = get_user_by_email(email)
        if not user:
            return render_template("login.html", error="Invalid email or password")

        # Verify password
        if not check_password_hash(user["password_hash"], password):
            return render_template("login.html", error="Invalid email or password")

        # Store user ID in session
        session["user_id"] = user["id"]

        # Redirect to landing page (dashboard)
        return redirect(url_for("landing"))

    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    """Clear session and redirect to landing page."""
    session.pop("user_id", None)
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    return "Profile page — coming in Step 4"


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
