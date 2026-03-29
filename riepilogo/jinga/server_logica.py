
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Prodotto(BaseModel):
    id:int
    nome:str
    prezzo:float
    descrizione:str

prodotti: List[Prodotto] = [
    Prodotto(id=1, nome="Prodotto 1", prezzo= 10.11, descrizione="Descrizione p1"),
    Prodotto(id=2, nome="Prodotto 2", prezzo= 23.11, descrizione="Descrizione p2"),

]


@app.get("/prodotti", response_model=List[Prodotto])
def get_prodotti():
    return prodotti

@app.get("/prodotti/{id}", response_model=Prodotto)
def get_prodotto(id:int):
    for p in prodotti:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Prodotto non trovato")
