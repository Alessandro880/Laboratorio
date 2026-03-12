import random
import os
from datetime import datetime

from player import *


adesso = datetime.now()
data = f"{adesso.day}/{adesso.month}/{adesso.year}"
ora = adesso.strftime("%H:%M:%S")
tentativi:int = []

#p = HumanPlayer(name)
nome:str
p = CpuPlayer("CPU:")

for i in range(1000):
    p.ntentativi=0
    p.tentativi = []
    n = random.randrange(0, 1000000000000)
    res = p.prendiInput(n)
    with open("file.tsv", "a", encoding="utf-8") as f:
        f.write(f"{p.name}\t{n}\t{p.ntentativi}\t")
        for x in p.tentativi :
            f.write(f"{x}-")
        f.write(f"\t{data}\t{ora}\n")
    
    


