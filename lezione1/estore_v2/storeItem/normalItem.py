from .genericItem import GenericItem

class NormalItem(GenericItem):
    def __init__(self, id, price, name, description):
        super().__init__(id, price)
        self.name = name
        self.description = description

    def __str__(self):
        return f"NormalItem(id={self.id}, price={self.price}, name={self.name}, description={self.description})"