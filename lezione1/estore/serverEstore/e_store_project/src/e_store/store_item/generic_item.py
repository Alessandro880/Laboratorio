from pydantic import BaseModel

class GenericItem(BaseModel):
    """Represents an item with a price."""
    name:str
    price:float
    
    def get_price(self) -> float:
        """Return item price."""
        return self.price
