#from consumer import GenericConsumer, NormalConsumer, PromotionalConsumer
from consumer import *
from storeItem import *
from store_inventory import StoreInventory
c1 = GenericConsumer("Generic Consumer")
c2 = NormalConsumer("Normal Consumer", "Mario", "Rossi", "anjdcejcnje@gmail.com")
c3 = PromotionalConsumer("Promotional Consumer", "Franco", "Verdfi", "skskskksks@gmail.com")

i1 = GenericItem(111, 9.99)
i2 = NormalItem(222, 19.99, "Laptop", "A high-performance laptop for work and gaming.")
i3 = ForeignItem(333, 29.99, "Smartphone", "A sleek smartphone with advanced features.", "China")
i4 = GenericItem(444, 4.99)

store = StoreInventory()
store.addItem(i1)
store.addItem(i2)
store.addItem(i3)
store.addItem(i4)


print("------ Store Inventory -----")
store.stampaStoreInventory()

print("\n\n")

