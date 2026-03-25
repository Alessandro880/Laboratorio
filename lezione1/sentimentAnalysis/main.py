from model import *
import os
import csv

os.system("clear")
    

m = BasicModel("BasicModel")

m.inserisciRighe("recensioni.csv")
m.studia()
m.printaPerc()


w = WordModel("WordModel")
w.inserisciRighe("recensioni.csv")
w.studia()

w.analizza()
w.printaPerc()
