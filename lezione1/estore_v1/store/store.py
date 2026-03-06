from store_inventory import StoreInventory

class Store:
    def __init__(self, inventory: StoreInventory, name: str):
        self.inventory = inventory
        self.name = name

    def displayInventory(self):
        print(f"------ Store Inventory di {self.name}-----")
        self.inventory.stampaStoreInventory()
