# ------ HTML Server --------
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
import requests
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

API_BASE_URL = "http://127.0.0.1:8000"

#-----
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
#-------

@app.get("/")
def index(request:Request):
    try:
        response = requests.get(f"{API_BASE_URL}/prodotti")
        response.raise_for_status()
        prodotti = response.json()
    except requests.RequestException as e:
        prodotti = []
        print("Errore nella chiamata API : ", e)
    return templates.TemplateResponse(
        request=request,                    
        name="index.html", 
        context={"prodotti": prodotti}    )

@app.get("/prodotto/{id}")
def prodotto_detail(request:Request, id:int):
    try:
        response = requests.get(f"{API_BASE_URL}/prodotti/{id}")
        response.raise_for_status()
        prodotto = response.json()
    except requests.RequestException as e:
        prodotto = None
        print("Errore nella chiamata API : ", e)
    return templates.TemplateResponse(
        request=request,                    
        name="product_detail.html", 
        context={"prodotto": prodotto}    )