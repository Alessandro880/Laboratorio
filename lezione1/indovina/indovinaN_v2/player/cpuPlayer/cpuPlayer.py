from player import Player

tent:int = 0
lTente:list = []

def fastFind(minval, maxval,n):
        tentativo = (minval + maxval) // 2
        global tent, lTente
        tent+=1
        lTente.append(tentativo)
        if(tentativo==n): 
            #print("La CPU ha vinto !!")
            return
        
        if(tentativo>n):
            fastFind(minval, tentativo-1, n)
        else:
            fastFind(tentativo+1, maxval, n)

class CpuPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def prendiInput(self,n):
        global tent, lTente
        tent=0
        lTente=[]
        fastFind(0,1000000000000,n)
        self.ntentativi=tent
        self.tentativi = lTente
        return 0
        


        

