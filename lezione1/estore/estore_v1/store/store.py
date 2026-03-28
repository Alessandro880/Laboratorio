from store_inventory import StoreInventory
from pydantic import BaseModel

class Store(BaseModel):
    inventory:StoreInventory
    money:float

    def displayInventory(self):
        print(f"------ Store Inventory -----")
        print(f" Cassa : {self.money}\n")
        self.inventory.stampaStoreInventory()
