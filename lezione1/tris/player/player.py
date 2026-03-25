'''
Creazione dell'oggetto player, il quale prende il nome e
il simbolo per giocare
'''

class Player:
    def __init__(self, name:str, sign:str):
        self.name = name
        self.sign=sign
    
    def make_move(self, table):
        pass