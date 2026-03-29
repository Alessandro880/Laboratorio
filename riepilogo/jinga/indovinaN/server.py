from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
import requests
import random

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

API_BASE_URL = "http://127.0.0.1:8000"

def crea_numero()->int:
    return random.randint(1,100)

indovina=crea_numero()

@app.get("/")
def init(request:Request):
    return templates.TemplateResponse(
        request=request,                    
        name="home.html"
          )

@app.post("/play")
def play_game(request: Request, guess: int=Form(...)):
    global indovina
    if guess == indovina:
        indovina=crea_numero()
        return templates.TemplateResponse(
        request=request,                    
        name="win.html",
        context={"number":guess}
          )
    if guess < indovina:
        messaggio_errore = "Il numero è troppo basso! Riprova."
    else:
        messaggio_errore = "Il numero è troppo alto! Riprova."

    # Ricarichiamo la home page, passandole il messaggio di errore
    return templates.TemplateResponse(
        request=request,                    
        name="home.html",
        context={"messaggio": messaggio_errore}
    )