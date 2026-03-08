from .normalItem import NormalItem

class ForeignItem(NormalItem):
    def __init__(self, id, price:float, name, description, country):
        super().__init__(id, price, name, description)
        self.country = country

    def __str__(self):
        return f"ForeignItem(id={self.id}, price={self.price}, name={self.name}, description={self.description}, country_of_origin={self.country})"