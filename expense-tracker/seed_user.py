import sqlite3
import random
from datetime import datetime
from pathlib import Path
from werkzeug.security import generate_password_hash

DB_PATH = Path(__file__).parent.parent / "spendly.db"

# Indian first names (mix of regions/genders)
FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Reyansh", "Ayaan", "Krishna", "Ishaan",
    "Rahul", "Amit", "Rajesh", "Suresh", "Priya", "Anjali", "Sneha", "Deepika",
    "Arnav", "Vihaan", "Aryan", "Krishiv", "Shaurya", "Rohan", "Karan", "Vikram",
    "Meera", "Kavya", "Divya", "Pooja", "Neha", "Ritu", "Sunita", "Lakshmi",
    "Dhruv", "Pranav", "Siddharth", "Nikhil", "Akash", "Sanjay", "Pankaj", "Manoj",
    "Ananya", "Diya", "Aadhya", "Saanvi", "Aarohi", "Ira", "Myra", "Zara"
]

# Indian last names (diverse across regions)
LAST_NAMES = [
    "Sharma", "Verma", "Gupta", "Singh", "Kumar", "Patel", "Reddy", "Nair",
    "Iyer", "Menon", "Das", "Ghosh", "Bose", "Chatterjee", "Banerjee", "Mukherjee",
    "Joshi", "Pandey", "Tripathi", "Awasthi", "Saxena", "Malhotra", "Khanna", "Chopra",
    "Desai", "Shah", "Mehta", "Kapoor", "Sethi", "Bhatia", "Bhatt", "Rao",
    "Hegde", "Kulkarni", "Deshmukh", "Patil", "Jadhav", "Thakur", "Yadav", "Mishra"
]

EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "rediffmail.com"]


def get_db():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def email_exists(email):
    """Check if email already exists in the database."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0


def generate_unique_email(first_name, last_name):
    """Generate a unique email address."""
    first_name_clean = first_name.lower().replace(" ", "")
    last_name_clean = last_name.lower().replace(" ", "")

    # Try different formats
    formats = [
        f"{first_name_clean}.{last_name_clean}",
        f"{first_name_clean}{last_name_clean}",
        f"{first_name_clean[0]}{last_name_clean}",
        f"{first_name_clean}.{last_name_clean[0]}",
    ]

    max_attempts = 10
    for base in formats:
        for _ in range(max_attempts):
            suffix = random.randint(10, 999)
            domain = random.choice(EMAIL_DOMAINS)
            email = f"{base}{suffix}@{domain}"
            if not email_exists(email):
                return email

    # Fallback: keep generating until unique
    while True:
        suffix = random.randint(1000, 9999)
        domain = random.choice(EMAIL_DOMAINS)
        email = f"{first_name_clean}.{last_name_clean}{suffix}@{domain}"
        if not email_exists(email):
            return email


def init_users_table():
    """Ensure the users table exists."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()


def seed_user():
    """Create a single random Indian user."""
    # Ensure table exists
    init_users_table()

    # Generate random name
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)

    # Generate unique email
    email = generate_unique_email(first_name, last_name)

    # Hash password
    password_hash = generate_password_hash("password123")

    # Get current datetime
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert into database
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
        (f"{first_name} {last_name}", email, password_hash, created_at)
    )

    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    # Print confirmation
    print(f"User created successfully!")
    print(f"  id: {user_id}")
    print(f"  name: {first_name} {last_name}")
    print(f"  email: {email}")


if __name__ == "__main__":
    seed_user()
