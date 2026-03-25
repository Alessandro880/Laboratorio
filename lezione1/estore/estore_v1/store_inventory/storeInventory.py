from storeItem import *
from ui import *
class StoreInventory :
    def __init__(self):
        self.item = {
            "genericItem" : [0,[]],
            "normalItem" : [0,[]],
            "foreignItem" : [0,[]]
        }
    def addItem(self, item):
        if isinstance(item, ForeignItem):
            self.item["foreignItem"][0] += 1
            self.item["foreignItem"][1].append(item)
        elif isinstance(item, NormalItem):
            self.item["normalItem"][0] += 1
            self.item["normalItem"][1].append(item)
        elif isinstance(item, GenericItem):
            self.item["genericItem"][0] += 1
            self.item["genericItem"][1].append(item)

    def removeItem(self, item):
        if isinstance(item, ForeignItem):
            if(findItemById(self, item.id) != None):
                self.item["foreignItem"][0] -= 1
                self.item["foreignItem"][1].remove(item)
                print("\n-> Item removed: ", item, "\n")
        elif isinstance(item, NormalItem):
            if(findItemById(self, item.id) != None):
                self.item["normalItem"][0] -= 1
                self.item["normalItem"][1].remove(item)
                print("\n-> Item removed: ", item, "\n")
        elif isinstance(item, GenericItem):
            if(findItemById(self, item.id) != None):
                self.item["genericItem"][0] -= 1
                self.item["genericItem"][1].remove(item)
                print("\n-> Item removed: ", item, "\n")


    def stampaStoreInventory(self):
        print("Generic Item: ", self.item["genericItem"][0])
        for item in self.item["genericItem"][1]:
            print(item)
        print("\nNormal Item: ", self.item["normalItem"][0])
        for item in self.item["normalItem"][1]:
            print(item)
        print("\nForeign Item: ", self.item["foreignItem"][0])
        for item in self.item["foreignItem"][1]:
            print(item)
