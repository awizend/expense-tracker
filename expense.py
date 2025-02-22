import uuid
from datetime import datetime

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())  # Generate a unique UUID string for the expense
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Store the creation time in UTC
        self.updated_at = self.created_at  # Initially, updated_at is the same as created_at
    
    def update(self, title=None, amount=None):
        """Update the title and/or amount of the expense and update the updated_at timestamp."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Set the updated_at timestamp to the current time
    
    def to_dict(self):
        """Returns a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }