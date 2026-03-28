import sys
sys.path.append(".")

from fastapi import FastAPI, HTTPException
from store import Store
from store_inventory import *
from costumer import *
from storeItem import *
app = FastAPI()


# c1 = GenericCostumer("Generic Consumer")
# c2 = NormalCostumer("Normal Consumer",200.21, "Mario", "Rossi", "anjdcejcnje@gmail.com")
# c3 = PromotionalCostumer("Promotional Consumer",500.33, "Franco", "Verdfi", "skskskksks@gmail.com")

i1 = GenericItem(id=111, price=9.99)
i2 = NormalItem(id=222, price=19.99, name="Laptop", description="A high-performance laptop for work and gaming.")
i3 = ForeignItem(id=333, price=29.99, name="Smartphone", description="A sleek smartphone with advanced features.", country="China")
i4 = GenericItem(id=444, price=4.99)


store_inventory1 = StoreInventory()

store_inventory1.addItem(i1)
store_inventory1.addItem(i2)
store_inventory1.addItem(i3)
store_inventory1.addItem(i4)

store = Store(inventory=store_inventory1, money=1000)


@app.get("/list_inventory/")
def show_list_inventory(): 
    return store.inventory