class ExpenseDatabase:
    def __init__(self):
        self.expenses = []  # List to store expense objects
    
    def add_expense(self, expense):
        """Add an expense to the database."""
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        """Remove an expense from the database by its ID."""
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
    def get_expense_by_id(self, expense_id):
        """Retrieve an expense by its unique ID."""
        return next((expense for expense in self.expenses if expense.id == expense_id), None)
    
    def get_expense_by_title(self, expense_title):
        """Retrieve expenses by title. Returns a list of matching expenses."""
        return [expense for expense in self.expenses if expense_title.lower() in expense.title.lower()]
    
    def to_dict(self):
        """Returns a list of dictionaries representing all expenses in the database."""
        return [expense.to_dict() for expense in self.expenses]
