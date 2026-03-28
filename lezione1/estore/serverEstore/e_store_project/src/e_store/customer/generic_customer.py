from pydantic import BaseModel

class GenericCustomer(BaseModel):
    """Represents a customer with balance and password."""
    name:str
    balance:float
        # Please keep in mind that storing a password in a production system requires care
        # this is just a toy example. 
    password:str
    list_p:dict
    
    def can_afford(self, price: float) -> bool:
        """Check if the customer can afford an item."""
        return self.balance >= price

    def purchase(self, price: float, password_input) -> bool:
        """Deduct price from balance if affordable."""

        if password_input != self.password:
            print("Invalid password!")
            return False
        if self.can_afford(price):
            self.balance -= price
            return True
        return False
