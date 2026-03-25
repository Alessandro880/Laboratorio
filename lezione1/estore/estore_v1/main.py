from costumer import *
from storeItem import *
from store_inventory import StoreInventory
from store import Store
from ui import *
import os

c1 = GenericCostumer("Generic Consumer")
c2 = NormalCostumer("Normal Consumer",200.21, "Mario", "Rossi", "anjdcejcnje@gmail.com")
c3 = PromotionalCostumer("Promotional Consumer",500.33, "Franco", "Verdfi", "skskskksks@gmail.com")

i1 = GenericItem(111, 9.99)
i2 = NormalItem(222, 19.99, "Laptop", "A high-performance laptop for work and gaming.")
i3 = ForeignItem(333, 29.99, "Smartphone", "A sleek smartphone with advanced features.", "China")
i4 = GenericItem(444, 4.99)


store_inventory1 = StoreInventory()

store_inventory1.addItem(i1)
store_inventory1.addItem(i2)
store_inventory1.addItem(i3)
store_inventory1.addItem(i4)

store = Store(store_inventory1, 1000)

letto = " "

while(letto!= '6'):
    print("-------MENU-------\n 1. Display Store Inventory\n 2. Buy Item by ID\n 3. Find Item by ID\n 4. Visualizza Saldo\n 5. Ricarica saldo \n6. Exit\n")
    letto = input("---> ")

    if(letto== '1'):
        os.system('clear')
        store.displayInventory()
        print("\n\n")
    
    elif(letto == '2'):
        buy = input("Insert the ID : ")
        os.system('clear')
        buyItemById(int(buy), c2, store_inventory1, store)
    
    elif (letto == '3'):
        find = input("Insert the ID : ")
        os.system('clear')
        findItemById(store_inventory1, int(find))
    elif(letto == '4'):
        os.system('clear')
        print("\n-> Your current balance is: ", c2.saldoAttuale(), "\n")  
    elif(letto == '5'):
        os.system('clear')
        ricarica = input("Insert the amount to recharge: ")
        c2.incrementaSaldo(float(ricarica))
        print("\n-> Your new balance is: ", c2.saldoAttuale(), "\n") 

