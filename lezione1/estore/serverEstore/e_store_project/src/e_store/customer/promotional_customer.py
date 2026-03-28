from e_store.customer.generic_customer import GenericCustomer

class PromotionalCustomer(GenericCustomer):
    """Customer with a 5% discount on purchases."""
    def purchase(self, price: float, password_input) -> bool:
        if(password_input != self.password):
            print("Invalid password!")
            return False        
        
        if self.can_afford(price):
            self.balance -= price*0.95
            return True
        return False
