# ============================================================
# Program 20: Expense Tracker
# Concepts: Lists of dicts, datetime, functions, data analysis
# ============================================================

# A simple personal expense tracker that allows users to:
# - Log expenses with category, amount, and date
# - View all expenses
# - See a breakdown by category
# - Find total spending
# Uses datetime module to record when each expense was added.

from datetime import datetime  # Import datetime for timestamps


# Pre-defined spending categories
CATEGORIES = [
    "Food", "Transport", "Shopping", "Bills",
    "Entertainment", "Health", "Education", "Other"
]


def get_category():
    """Let user pick a category from the predefined list."""
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"    {i}. {cat}")
    while True:
        try:
            idx = int(input("  Pick category number: "))
            if 1 <= idx <= len(CATEGORIES):
                return CATEGORIES[idx - 1]
            else:
                print(f"⚠️  Choose between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("⚠️  Please enter a number.")


def add_expense(expenses):
    """Add a new expense entry to the expenses list."""
    print("\n--- Add New Expense ---")

    # Get description
    desc = input("  Description: ").strip()
    if not desc:
        print("⚠️  Description is required.")
        return

    # Get amount
    try:
        amount = float(input("  Amount (₹): "))
        if amount <= 0:
            print("⚠️  Amount must be positive.")
            return
    except ValueError:
        print("⚠️  Invalid amount.")
        return

    # Get category
    category = get_category()

    # Create expense dictionary
    expense = {
        "description": desc,
        "amount":      amount,
        "category":    category,
        "date":        datetime.now().strftime("%Y-%m-%d %H:%M"),  # Current time
    }

    expenses.append(expense)
    print(f"\n✅ Expense added: {desc} — ₹{amount:,.2f} [{category}]")


def view_expenses(expenses):
    """Display all recorded expenses in a formatted table."""
    if not expenses:
        print("\n📋 No expenses recorded yet.")
        return

    print(f"\n{'#':<4}{'Date':<18}{'Description':<20}{'Category':<14}{'Amount':>10}")
    print("-" * 68)

    for i, exp in enumerate(expenses, start=1):
        print(f"{i:<4}{exp['date']:<18}{exp['description']:<20}"
              f"{exp['category']:<14}₹{exp['amount']:>9,.2f}")

    print("-" * 68)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total Spending:':<52}₹{total:>9,.2f}")


def category_breakdown(expenses):
    """Show spending totals grouped by category."""
    if not expenses:
        print("\n📋 No expenses to analyze.")
        return

    # Aggregate spending per category using a dictionary
    breakdown = {}
    for exp in expenses:
        cat = exp["category"]
        breakdown[cat] = breakdown.get(cat, 0) + exp["amount"]

    # Sort by amount (highest first)
    sorted_breakdown = sorted(breakdown.items(), key=lambda x: x[1], reverse=True)

    total = sum(exp["amount"] for exp in expenses)

    print("\n📊 Spending by Category:")
    print("-" * 40)
    for cat, amount in sorted_breakdown:
        percentage = (amount / total) * 100
        bar = "█" * int(percentage / 5)  # Simple text bar chart
        print(f"  {cat:<15} ₹{amount:>8,.2f}  {percentage:>5.1f}%  {bar}")
    print("-" * 40)
    print(f"  {'TOTAL':<15} ₹{total:>8,.2f}")


def main():
    print("=" * 50)
    print("       💰  Expense Tracker  💰")
    print("=" * 50)
    print("Track your daily expenses with categories.\n")

    expenses = []  # List of expense dictionaries

    while True:
        print("\n--- Menu ---")
        print("  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. Category Breakdown")
        print("  4. Quit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_breakdown(expenses)
        elif choice == "4":
            total = sum(e["amount"] for e in expenses)
            print(f"\n💸 Total spent this session: ₹{total:,.2f}")
            print("👋 Goodbye! Spend wisely!")
            break
        else:
            print("⚠️  Invalid option. Choose 1–4.")


if __name__ == "__main__":
    main()
