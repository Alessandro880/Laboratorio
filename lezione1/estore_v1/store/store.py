from store_inventory import StoreInventory

class Store:
    def __init__(self, inventory: StoreInventory, money: int):
        self.inventory = inventory
        self.money = money

    def displayInventory(self):
        print(f"------ Store Inventory -----")
        print(f" Cassa : {self.money}\n")
        self.inventory.stampaStoreInventory()
