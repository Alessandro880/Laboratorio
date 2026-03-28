from .normalItem import NormalItem
from pydantic import BaseModel

class ForeignItem(NormalItem, BaseModel):
    country:str

    def __str__(self):
        return f"ForeignItem(id={self.id}, price={self.price}, name={self.name}, description={self.description}, country_of_origin={self.country})"