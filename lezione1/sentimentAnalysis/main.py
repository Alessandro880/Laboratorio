from model import *
import os

os.system("clear")

m = BasicModel("BasicModel")

m.inserisciRighe("recensioni.tsv")
m.studia()
m.printaPerc()

w = WordModel("WordModel")

w.inserisciRighe("recensioni.tsv")
w.studia()
w.printaPerc()