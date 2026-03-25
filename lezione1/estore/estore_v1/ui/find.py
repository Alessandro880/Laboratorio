from storeItem import *

def findItemById(store_inventory, item_id):
    for type in store_inventory.item:
        for item in store_inventory.item[type][1]:
            if(item.id == item_id):
                print("\n-> Item found!: ", item, "\n")
                return item
    print("\n-> Item not found!\n")
    return None
