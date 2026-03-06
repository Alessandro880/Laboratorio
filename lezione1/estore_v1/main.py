#from consumer import GenericConsumer, NormalConsumer, PromotionalConsumer
from consumer import *
from storeItem import *
from store_inventory import StoreInventory
from store import Store
c1 = GenericConsumer("Generic Consumer")
c2 = NormalConsumer("Normal Consumer", "Mario", "Rossi", "anjdcejcnje@gmail.com")
c3 = PromotionalConsumer("Promotional Consumer", "Franco", "Verdfi", "skskskksks@gmail.com")

i1 = GenericItem(111, 9.99)
i2 = NormalItem(222, 19.99, "Laptop", "A high-performance laptop for work and gaming.")
i3 = ForeignItem(333, 29.99, "Smartphone", "A sleek smartphone with advanced features.", "China")
i4 = GenericItem(444, 4.99)


store_inventory1 = StoreInventory()
store_inventory2 = StoreInventory()

store_inventory1.addItem(i1)
store_inventory1.addItem(i2)
store_inventory2.addItem(i3)
store_inventory2.addItem(i4)
store_inventory2.addItem(i1)

store1 = Store(store_inventory1, "Tech Store")
store2 = Store(store_inventory2, "Gadget Store")

print("\n")
store1.displayInventory()
store2.displayInventory()

print("\n\n")

