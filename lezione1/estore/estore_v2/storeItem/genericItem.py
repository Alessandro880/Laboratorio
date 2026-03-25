class GenericItem:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def __str__(self):
        return f"GenericItem(id={self.id}, price={self.price})"