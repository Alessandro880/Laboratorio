from .find import findItemById
from  storeItem import *
from costumer import *

def buyItemById(itemId:int , costumer, storeInventory, store):
    if(findItemById(storeInventory, itemId) == None):
        print("\n-> Item not in the store, Sorry!\n")
        return
    item = findItemById(storeInventory, itemId)
    if(item is isinstance(item, ForeignItem)):
        if(costumer is isinstance(costumer, PromotionalCostumer)):
            if(item.price > costumer.saldoAttuale()):
                print("\n-> Not enough budget to buy this item, Sorry!\n")
                return
            else :
                print("\n-> Item bought successfully! Congratulations!\n")
                storeInventory.removeItem(item)
                costumer.decrementaSaldo(item.price)
                print("\n-> Your new balance is: ", costumer.saldoAttuale(), "\n")
                store.money += item.price
                return
        elif(item.price*1.2>costumer.saldoAttuale()):
            print("\n-> Not enough budget to buy this item, Sorry!\n")
            return
        else :
            print("\n-> Item bought successfully! Congratulations!\n")
            storeInventory.removeItem(item)
            costumer.decrementaSaldo(item.price*1.2)
            store.money += item.price*1.2
            print("\n-> Your new balance is: ", costumer.saldoAttuale(), "\n")
            return
    else :
        if(costumer is isinstance(costumer, PromotionalCostumer)):
            if(item.price*0.8 > costumer.saldoAttuale()):
                print("\n-> Not enough budget to buy this item, Sorry!\n")
                return
            else :
                print("\n-> Item bought successfully! Congratulations!\n")
                storeInventory.removeItem(item)
                costumer.decrementaSaldo(item.price*0.8)
                store.money += item.price*.8
                print("\n-> Your new balance is: ", costumer.saldoAttuale(), "\n")
                return
        elif(item.price>costumer.saldoAttuale()):
            print("\n-> Not enough budget to buy this item, Sorry!\n")
            return
        else :
            print("\n-> Item bought successfully! Congratulations!\n")
            storeInventory.removeItem(item)
            costumer.decrementaSaldo(item.price)
            store.money += item.price
            print("\n-> Your new balance is: ", costumer.saldoAttuale(), "\n")
            return