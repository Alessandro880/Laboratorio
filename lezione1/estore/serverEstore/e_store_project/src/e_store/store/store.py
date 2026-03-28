from e_store.store_inventory.store_inventory import StoreInventory
from e_store.customer.generic_customer import GenericCustomer
from pydantic import BaseModel

class Store(BaseModel):
    """Store containing inventory and balance."""
    inventory:StoreInventory
    balance:float
    
    def sell_item(self, customer: GenericCustomer, item_name: str, quantity: int, password) -> bool:
        """Sell an item to a customer if possible."""
        if item_name in self.inventory.get_items():
            item_data = self.inventory.get_items()[item_name]
            total_price = item_data['item'].get_price() * quantity
            if customer.purchase(total_price, password) and self.inventory.remove_item(item_name, quantity):
                self.balance += total_price
                return True
        return False
    

    def find_item(self, name:str):
        if(name not in self.inventory.items):
            return "Item not found in the store !!"
        else:
            return self.inventory.items[name]
