from player import *
from ui import *
import os
import time

table:Table
p1:Player
p2:Player
win:str
nmosse:int = 0

os.system('clear')

tipoc:str = ' '
while(tipoc != '1' and tipoc != '2'):
    tipoc = input("\nScegliere il tipo di tabella :\n - 1 ascii\n - 2 unicode\n -> ")

if(tipoc == '1'):
    table = TAscii()
else:
    table = TUnicode()

tipo1 = ''
while(tipo1 != '1' and tipo1 != '2' and tipo1 != '3'):
    tipo1 = input("\nScegliere il tipo di giocatore per player1 :\n - 1 Human\n - 2 Cpu\n - 3 Cpu God\n -> ")

tipo2 = ''
while(tipo2 != '1' and tipo2 != '2' and tipo2 != '3'):
    tipo2 = input("\nScegliere il tipo di giocatore per player2 :\n - 1 Human\n - 2 Cpu\n - 3 Cpu God\n -> ")

if(tipo1 == '1'):
    name1 = input("Nome player1 : ")
    p1 = HumanPlayer(name1, 'X')
elif(tipo1 == '2') : p1 = CPU('CPU base','X')
else : p1 = CPUGod("CPU God 1",'X')

if(tipo2 == '1'):
    name2 = input("Nome player2 : ")
    p2 = HumanPlayer(name2, 'O')
elif(tipo2=='2') : p2 = CPU('cpu2', 'O')
else: p2 = CPUGod("CPU God 2",'O')


time.sleep(1)
os.system('clear')

k=0
while(k<=8):
    k+=1
    nmosse +=1
    os.system('clear')
    table.show()
    p1.make_move(table.table)
    os.system('clear')
    table.show()
    win = check(table.table)
    if(win != ' ' or k==9): 
        break
    p2.make_move(table.table)
    k+=1
    time.sleep(0.2)
    os.system('clear')
    table.show()
    win = check(table.table)
    if(win != ' '): 
        break

if(win == p1.sign):
    print(f"Il giocatore {p1.name} ha vinto!!\n")
elif(win == p2.sign):
    print(f"Il giocatore {p2.name} ha vinto!!\n")
else:
    print("Nessuno ha vinto !!\n")

print(f"Numero totale di mosse : {nmosse}")