from expense import Expense
from expense_db import ExpenseDatabase

def main():
    db = ExpenseDatabase()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Remove Expense")
        print("5. Search Expense by Title")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter expense title: ")
            amount = float(input("Enter amount: "))
            expense = Expense(title, amount)
            db.add_expense(expense)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = db.to_dict()
            if not expenses:
                print("No expenses recorded.")
            else:
                for exp in expenses:
                    print(exp)

        elif choice == "3":
            expense_id = input("Enter expense ID to update: ")
            expense = db.get_expense_by_id(expense_id)
            if expense:
                new_title = input("Enter new title (leave blank to keep current): ")
                new_amount = input("Enter new amount (leave blank to keep current): ")
                
                new_amount = float(new_amount) if new_amount else None
                expense.update(title=new_title if new_title else None, amount=new_amount)
                print("Expense updated successfully!")
            else:
                print("Expense not found.")

        elif choice == "4":
            expense_id = input("Enter expense ID to remove: ")
            db.remove_expense(expense_id)
            print("Expense removed successfully!")

        elif choice == "5":
            title = input("Enter title to search: ")
            results = db.get_expense_by_title(title)
            if results:
                for exp in results:
                    print(exp.to_dict())
            else:
                print("No matching expenses found.")

        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()