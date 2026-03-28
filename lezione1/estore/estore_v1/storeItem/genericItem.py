from pydantic import BaseModel

class GenericItem(BaseModel):
    id:int
    price:float

    def __str__(self):
        return f"GenericItem(id={self.id}, price={self.price})"