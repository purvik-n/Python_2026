# ============================================================
# Program 16: Simple ATM Machine Simulator
# Concepts: Classes, OOP, methods, conditionals, input validation
# ============================================================

# This program simulates a basic ATM machine.
# It demonstrates Object-Oriented Programming (OOP) in Python.
# Key OOP concepts: class, __init__, instance variables, methods

class ATM:
    """
    Represents a simple ATM machine with a PIN-protected bank account.
    
    Attributes:
        balance (float): Current account balance
        pin (str)      : 4-digit PIN for authentication
        max_attempts   : Max wrong PIN attempts before lockout
    """

    MAX_PIN_ATTEMPTS = 3  # Class variable — shared across all ATM instances

    def __init__(self, initial_balance, pin):
        """
        Constructor: Initialize the ATM with a starting balance and PIN.
        Called automatically when you do: atm = ATM(1000, "1234")
        """
        self.__balance  = initial_balance  # __ makes it private (encapsulation)
        self.__pin      = str(pin)         # Store PIN as string
        self.__attempts = 0                # Track wrong PIN attempts
        self.__locked   = False            # Account lock status

    def __check_pin(self, entered_pin):
        """
        Private method to verify the PIN.
        Increments attempt counter on failure.
        """
        if self.__locked:
            print("🔒 Account is LOCKED due to too many failed attempts.")
            return False

        if str(entered_pin) == self.__pin:
            self.__attempts = 0  # Reset on correct PIN
            return True
        else:
            self.__attempts += 1
            remaining = self.MAX_PIN_ATTEMPTS - self.__attempts
            print(f"❌ Wrong PIN. {remaining} attempt(s) remaining.")
            if self.__attempts >= self.MAX_PIN_ATTEMPTS:
                self.__locked = True
                print("🔒 Account LOCKED! Too many failed attempts.")
            return False

    def check_balance(self, pin):
        """Display current balance after PIN verification."""
        if self.__check_pin(pin):
            print(f"\n💰 Your current balance: ₹{self.__balance:,.2f}")

    def deposit(self, pin, amount):
        """Deposit money into the account."""
        if self.__check_pin(pin):
            if amount <= 0:
                print("⚠️  Deposit amount must be positive.")
                return
            self.__balance += amount
            print(f"✅ ₹{amount:,.2f} deposited successfully.")
            print(f"   New balance: ₹{self.__balance:,.2f}")

    def withdraw(self, pin, amount):
        """Withdraw money if sufficient balance exists."""
        if self.__check_pin(pin):
            if amount <= 0:
                print("⚠️  Withdrawal amount must be positive.")
            elif amount > self.__balance:
                print(f"❌ Insufficient funds. Available: ₹{self.__balance:,.2f}")
            else:
                self.__balance -= amount
                print(f"✅ ₹{amount:,.2f} withdrawn successfully.")
                print(f"   Remaining balance: ₹{self.__balance:,.2f}")


def main():
    print("=" * 45)
    print("      🏧  ATM Machine Simulator  🏧")
    print("=" * 45)
    print("Default PIN: 1234  |  Starting balance: ₹10,000\n")

    # Create an ATM instance (OOP in action!)
    atm = ATM(initial_balance=10000, pin="1234")

    while True:
        print("\n--- Menu ---")
        print("  1. Check Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            pin = input("Enter PIN: ")
            atm.check_balance(pin)

        elif choice == "2":
            pin = input("Enter PIN: ")
            try:
                amount = float(input("Deposit amount: ₹"))
                atm.deposit(pin, amount)
            except ValueError:
                print("⚠️  Invalid amount.")

        elif choice == "3":
            pin = input("Enter PIN: ")
            try:
                amount = float(input("Withdrawal amount: ₹"))
                atm.withdraw(pin, amount)
            except ValueError:
                print("⚠️  Invalid amount.")

        elif choice == "4":
            print("\n🙏 Thank you for using our ATM. Goodbye!")
            break

        else:
            print("⚠️  Invalid option. Choose 1–4.")


if __name__ == "__main__":
    main()
