from .player import Player

class HumanPlayer(Player):
    def __init__(self, name, sign):
        super().__init__(name, sign)

    def make_move(self, table):
        x=''
        y=''
        while(1):
            try:
                print(f"È il turno di {self.name}")
                x=input("inserisci la coordinata x : ")
                y=input("inserisci la coordinata y : ")
                x=int(x)
                y=int(y)
                if(x<0 or x>3) : 
                    print("inserisci x tra 1 e 3!\n")
                    continue
                if(y<1 or y>3) : 
                    print("inserisci y tra 1 e 3!\n")
                    continue
                if(table[x-1][y-1] == ' '):
                    table[x-1][y-1] = self.sign
                    break
                else :
                    print("Mossa non valida!\n")
            except ValueError:
                print('inserisci dei numeri!\n')
