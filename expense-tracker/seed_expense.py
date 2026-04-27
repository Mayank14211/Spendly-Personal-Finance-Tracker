import sqlite3
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path(__file__).parent / "spendly.db"

# Expense categories with realistic descriptions
CATEGORIES = {
    "Food": ["Lunch at cafe", "Dinner with friends", "Grocery shopping", "Coffee and snacks", "Fast food", "Restaurant bill", "Home delivery order", "Breakfast at diner", "Weekend buffet"],
    "Transport": ["Uber ride", "Metro card recharge", "Bus fare", "Taxi to airport", "Fuel refill", "Auto rickshaw", "Ola cab", "Monthly pass", "Parking fee"],
    "Bills": ["Electricity bill", "Water bill", "Internet subscription", "Mobile recharge", "Gas connection", "Maintenance charges", "DTH subscription", "House rent", "Property tax"],
    "Health": ["Pharmacy purchase", "Doctor consultation", "Gym membership", "Health checkup", "Medical test", "Yoga class", "Vitamins supplement", "Dental care", "Physiotherapy session"],
    "Entertainment": ["Movie tickets", "Concert entry", "Netflix subscription", "Gaming purchase", "Theme park entry", "Sports event", "Music streaming", "Book purchase", "Art exhibition"],
    "Shopping": ["New clothes", "Electronics gadget", "Home decor", "Shoes and footwear", "Watch accessory", "Bag purchase", "Cosmetics", "Jewelry", "Stationery items"],
    "Other": ["Random purchase", "Emergency expense", "Gift for friend", "Donation", "Pet supplies", "Car maintenance", "Home repair", "Laundry service", "Miscellaneous"]
}


def get_db():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def get_user(user_id):
    """Fetch user by ID."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def generate_expense(user_id, months_back):
    """Generate a single random expense."""
    category = random.choice(list(CATEGORIES.keys()))
    description = random.choice(CATEGORIES[category])
    amount = round(random.uniform(10, 500), 2)

    # Random date within the last 'months' months
    days_back = random.randint(0, months_back * 30)
    expense_date = datetime.now() - timedelta(days=days_back)
    date_str = expense_date.strftime("%Y-%m-%d")

    return (user_id, amount, category, date_str, description)


def seed_expenses(user_id, count=10, months=3):
    """Generate and insert dummy expenses for a user."""
    # Verify user exists
    user = get_user(user_id)
    if not user:
        print(f"Error: User with id {user_id} does not exist.")
        sys.exit(1)

    # Generate expenses
    expenses = [generate_expense(user_id, months) for _ in range(count)]

    # Insert into database
    conn = get_db()
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        expenses
    )

    conn.commit()
    conn.close()

    # Calculate date range
    dates = [exp[3] for exp in expenses]
    earliest = min(dates)
    latest = max(dates)

    # Print summary
    print(f"Expenses seeded successfully!")
    print(f"  User: {user['name']} ({user['email']})")
    print(f"  Number of expenses: {count}")
    print(f"  Date range: {earliest} to {latest}")


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python seed_expense.py <user_id> [count] [months]")
        print("  user_id: ID of the user to add expenses for")
        print("  count: number of expenses to generate (default: 10)")
        print("  months: how many months back to generate from (default: 3)")
        sys.exit(1)

    user_id = int(sys.argv[1])
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    months = int(sys.argv[3]) if len(sys.argv) > 3 else 3

    seed_expenses(user_id, count, months)
