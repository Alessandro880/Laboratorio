from player import Player
import random

tentativo1:int

class CpuPlayer(Player):
    def __init__(self):
        super().__init__("CPU")

    
    def prendiInput(self,n):
        tentativo1 = random.randrange(0, 100)
        self.ntentativi += 1
        self.tentativi.append(tentativo1)
        while(True):
            
            if(tentativo1 == n): 
                print("La CPU ha vinto !!\n")
                self.vittoria()
                break
            elif(tentativo1 < n) :
                tentativo1+=1 
                self.tentativi.append(tentativo1)
                self.ntentativi += 1
            else:
                tentativo1 -=1 
                self.tentativi.append(tentativo1)
                self.ntentativi += 1


        

