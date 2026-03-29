from fastapi import FastAPI

app = FastAPI()

value = {}

@app.get("/posts/{index}")
def read_post(index):
    if index not in value:
        return {"errore": "Post non trovato"}
    return value[index]

@app.post("/posts")
def write_posts(insert:dict):
        
    if insert["userID"] not in value:
        value[insert["userID"]] = insert
        return insert
    else :
        return f"UserID {insert["userID"]} alredy exist!"
    
   
    