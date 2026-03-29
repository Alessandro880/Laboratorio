import requests


#----- server logica -----

url = "http://127.0.0.1:8000/prodotti/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Errore: ", response.status_code)