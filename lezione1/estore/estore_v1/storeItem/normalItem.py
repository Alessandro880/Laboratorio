from .genericItem import GenericItem
from pydantic import BaseModel

class NormalItem(GenericItem, BaseModel):
    name:str
    description:str

    def __str__(self):
        return f"NormalItem(id={self.id}, price={self.price}, name={self.name}, description={self.description})"