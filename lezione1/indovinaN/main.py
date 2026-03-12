import random
import os
from datetime import datetime

from player import *

n = random.randrange(0, 100)
#print(n)
adesso = datetime.now()
data = f"{adesso.day}/{adesso.month}/{adesso.year}"
ora = adesso.strftime("%H:%M:%S")
tentativi:int = []

#p = HumanPlayer(name)
nome:str
nome = input("Inserisci un nome : ")

p = HumanPlayer(nome)
    

p.prendiInput(n)
    
    


with open("file.tsv", "a", encoding="utf-8") as f:
    f.write(f"{p.name}\t{n}\t{p.ntentativi}\t")
    for x in p.tentativi :
        f.write(f"{x}-")
    f.write(f"\t{data}\t{ora}\n")