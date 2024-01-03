class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("Expense Tracker:")
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
