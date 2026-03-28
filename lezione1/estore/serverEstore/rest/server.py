import sys
sys.path.append("../e_store_project/src")

from fastapi import FastAPI, HTTPException
from e_store.store.store import Store
#from e_store_project.src.e_store.inventory.inventory import Inventory
from e_store.store_inventory.store_inventory import StoreInventory
from e_store.customer import *
from e_store.store_item import *
app = FastAPI()

users ={}

c1 = GenericCustomer(name="Alessandro", balance=2000, password="ciao",list_p={})
c2 = NormalCustomer(name="Federico",balance=200.21, password="ciao",list_p={})
c3 = PromotionalCustomer(name="Milena",balance=500.33, password="ciao",list_p={})

users[c1.name] = c1
users[c2.name] = c2
users[c3.name] = c3

i1 = GenericItem(name='Iphone16', price=999.99) # type: ignore
i2 = GenericItem(name='Samsungs26', price=899.99)
i3 = GenericItem(name='Ipad pro', price=1500.99)
i4 = GenericItem(name="Lavatrice", price=400.99)

store_inventory1 = StoreInventory(items={})

store_inventory1.add_item(i1, 4)
store_inventory1.add_item(i2,3)
store_inventory1.add_item(i3,10)
store_inventory1.add_item(i4,7)

store = Store(inventory=store_inventory1, balance=1000)



@app.get("/list_inventory/")
def show_list_inventory(): 
    return store.inventory.items


@app.get("/user_items/")
def show_user_items():
    lista_el = {}
    for user in users:
        lista_el[user] = users[user].list_p
    return lista_el

@app.get("/item_information/{item_name}")
def show_item_id(item_name:str):
    return store.find_item(item_name)

@app.get("/user_balance/{user_name}")
def show_user_balance(user_name:str):
    if(user_name  not in users):
        return "User not found !!"
    return users[user_name].balance

@app.post("/purchase/")
def item_purchase(item:str, user_n, password):
    if(item not in store.inventory.items):
        return "Item non in the store"
    if(not store.sell_item(users[user_n], item,1, password)):
        return f"Balance not sufficient! current balance : {users[user_n].balance}"
    else :
        if item not in users[user_n].list_p:
            users[user_n].list_p[item] = 1
        else:
            users[user_n].list_p[item] += 1
        return f"Prodocut bought! , new balance : {users[user_n].balance}"