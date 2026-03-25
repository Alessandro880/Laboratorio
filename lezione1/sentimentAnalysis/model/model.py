import csv
class Model():
    def __init__(self, name):
        self.name = name
        self.righe = []
        self.positive:int = 0
        self.percentuale:int

    def inserisciRighe(self, file):
        with open(file, "r", encoding="utf-8") as f:
            lettore = csv.reader(f)
            for line in lettore: 
                self.righe.append(line)
                

    def studia():
        print("Studia la prima metà!\n")

    def printaPerc(self):
        print(f"\nIl {self.name} ha accuratezza pari a : {self.percentuale}%\n")

