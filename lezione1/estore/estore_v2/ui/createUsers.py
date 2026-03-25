from costumer import *

users = {}

def createUsers():
    with open("users.txt", "r", encoding='utf-8') as f:
        for line in f:
            print(line)
            if(len(line.split(","))==3):
                riga = line.split(",")
                users[riga[0]] = GenericCostumer(riga[0], riga[1], float(riga[2]))

            elif(len(line.split(","))==6):
                riga = line.split(",")
                users[riga[0]] = NormalCostumer(riga[0], riga[1], float(riga[2]), riga[3], riga[4], riga[5])

            elif(len(line.split(","))==7):
                riga = line.split(",")
                users[riga[0]] = PromotionalCostumer(riga[0], riga[1], float(riga[2]), riga[3], riga[4], riga[5], riga[6])
    return users