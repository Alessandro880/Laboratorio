from .player import Player
import random
import time

class CPUGod(Player):
    def __init__(self, name, sign):
        super().__init__(name, sign)

    def make_move(self, table):

        print(f"\n{self.name} sta pensando", end=" ",flush=True)
        time.sleep(0.5)
        print('.', end=" ",flush=True)
        time.sleep(0.5)
        print('.', end=" ",flush=True)
        time.sleep(0.5)
        print('.')

        if(table[1][1] == ' '):
            table[1][1] = self.sign
            return
        for x in table: #soluzioine vittoria righe
            if(x[0]==self.sign and x[1]==self.sign and x[2]==' '): 
                x[2] = self.sign
                return 
            if(x[2]==self.sign and x[1]==self.sign and x[0]==' '): 
                x[0] = self.sign
                return
            if(x[2]==self.sign and x[0]==self.sign and x[1]==' '): 
                x[1] = self.sign
                return
        
        #Soluzioione vittoria diagonale
        if(table[0][0]==self.sign and table[1][1]==self.sign and table[2][2]==' '): 
            table[2][2] = self.sign
            return
        if(table[2][2]==self.sign and table[1][1]==self.sign and table[0][0]==' '): 
            table[0][0] = self.sign
            return
        if(table[0][0]==self.sign and table[2][2]==self.sign and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        ##
        if(table[2][0]==self.sign and table[1][1]==self.sign and table[0][2]==' '): 
            table[0][2] = self.sign
            return
        if(table[2][0]==self.sign and table[0][2]==self.sign and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        if(table[0][2]==self.sign and table[1][1]==self.sign and table[2][0]==' '): 
            table[2][0] = self.sign
            return

        #soluzione vittoria verticale prima colonna
        if(table[0][0]==self.sign and table[1][0]==self.sign and table[2][0]==' '): 
            table[2][0] = self.sign
            return
        if(table[0][0]==self.sign and table[2][0]==self.sign and table[1][0]==' '): 
            table[1][0] = self.sign
            return
        if(table[1][0]==self.sign and table[2][0]==self.sign and table[0][0]==' '): 
            table[0][0] = self.sign
            return
        
         #soluzione vittoria verticale seconda colonna
        if(table[0][1]==self.sign and table[1][1]==self.sign and table[2][1]==' '): 
            table[2][1] = self.sign
            return
        if(table[0][1]==self.sign and table[2][1]==self.sign and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        if(table[1][1]==self.sign and table[2][1]==self.sign and table[0][1]==' '): 
            table[0][1] = self.sign
            return
        
         #soluzione vittoria verticale terza colonna
        if(table[0][2]==self.sign and table[1][2]==self.sign and table[2][2]==' '): 
            table[2][2] = self.sign
            return
        if(table[0][2]==self.sign and table[2][2]==self.sign and table[1][2]==' '): 
            table[1][2] = self.sign
            return
        if(table[1][2]==self.sign and table[2][2]==self.sign and table[0][2]==' '): 
            table[0][2] = self.sign
            return
        
        enemy = ''
        if(self.sign == 'X'): enemy = 'O'
        else: enemy='X'
        for x in table: #soluzioine  righe
            if(x[0]==enemy and x[1]==enemy and x[2]==' '): 
                x[2] = self.sign
                return 
            if(x[2]==enemy and x[1]==enemy and x[0]==' '): 
                x[0] = self.sign
                return
            if(x[2]==enemy and x[0]==enemy and x[1]==' '): 
                x[1] = self.sign
                return
           
           #Diagonali 
        if(table[0][0]==enemy and table[1][1]==enemy and table[2][2]==' '): 
            table[2][2] = self.sign
            return
        if(table[2][2]==enemy and table[1][1]==enemy and table[0][0]==' '): 
            table[0][0] = self.sign
            return
        if(table[0][0]==enemy and table[2][2]==enemy and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        
        if(table[2][0]==enemy and table[1][1]==enemy and table[0][2]==' '): 
            table[0][2] = self.sign
            return
        if(table[2][0]==enemy and table[0][2]==enemy and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        if(table[0][2]==enemy and table[1][1]==enemy and table[2][0]==' '): 
            table[2][0] = self.sign
            return
        

        #Prima colonna
        if(table[0][0]==enemy and table[1][0]==enemy and table[2][0]==' '): 
            table[2][0] = self.sign
            return
        if(table[0][0]==enemy and table[2][0]==enemy and table[1][0]==' '): 
            table[1][0] = self.sign
            return
        if(table[1][0]==enemy and table[2][0]==enemy and table[0][0]==' '): 
            table[0][0] = self.sign
            return

        #Seconda colonna
        if(table[0][1]==enemy and table[1][1]==enemy and table[2][1]==' '): 
            table[2][1] = self.sign
            return
        if(table[0][1]==enemy and table[2][1]==enemy and table[1][1]==' '): 
            table[1][1] = self.sign
            return
        if(table[1][1]==enemy and table[2][1]==enemy and table[0][1]==' '): 
            table[0][1] = self.sign
            return
        
         #terza colonna
        if(table[0][2]==enemy and table[1][2]==enemy and table[2][2]==' '): 
            table[2][2] = self.sign
            return
        if(table[0][2]==enemy and table[2][2]==enemy and table[1][2]==' '): 
            table[1][2] = self.sign
            return
        if(table[1][2]==enemy and table[2][2]==enemy and table[0][2]==' '): 
            table[0][2] = self.sign
            return

        if(table[1][1]==enemy and table[0][0]==' ' and table[0][2]==' ' and table[2][0]==' ' and table[2][2]==' '): 
            table[0][0] = self.sign
            return
        if(table[0][2] == ' '): 
            table[0][2] = self.sign
            return
        if(table[2][0] == ' '): 
            table[2][0] = self.sign
            return
        if(table[2][2] == ' '): 
            table[2][2] = self.sign
            return
        
        if(table[0][0]==enemy and table[0][1]==' '): 
            table[0][1] = self.sign
            return
        if(table[0][2]==enemy and table[0][1]==' '): 
            table[0][1] = self.sign
            return
        
        if(table[0][0]==enemy and table[1][0]==' '): 
            table[1][0] = self.sign
            return
        if(table[2][0]==enemy and table[1][0]==' '): 
            table[1][0] = self.sign
            return
        
        if(table[2][0]==enemy and table[2][1]==' '): 
            table[2][1] = self.sign
            return
        if(table[2][2]==enemy and table[2][1]==' '): 
            table[2][1] = self.sign
            return
        
        if(table[0][2]==enemy and table[1][2]==' '): 
            table[1][2] = self.sign
            return
        if(table[2][2]==enemy and table[1][2]==' '): 
            table[1][2] = self.sign
            return
        
        
        
        while(1):
            x = random.randint(0,2)
            y = random.randint(0,2)
            if(table[x][y] == ' '):
                table[x][y] = self.sign
                return
            
        

