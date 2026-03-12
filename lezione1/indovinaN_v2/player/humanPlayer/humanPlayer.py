from player import Player
import os

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def prendiInput(self, n):
        #os.system("clear")
        while True:
            

            while True :
                try :
                    indovina = input(f"Indovina il numero (0-100): ")
                    numero = int(indovina)
                    break
                except ValueError:
                    print("Perfavore inserisci dei numeri !\n")
            self.ntentativi+=1
            self.tentativi.append(numero)
            if(numero == n) :
                print(f"{self.name} Hai vinto!\n")
                self.vittoria()
                break
            elif(n>numero):
                print("Il tuo nomero è più piccolo")
                wait = input("Premi per riprovare!\n")
            else:
                print("Il tuo nomero è più grande")
                wait = input("Premi per riprovare!\n")
        
