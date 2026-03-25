from .player import Player
import time
import random

class CPU(Player):
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
        while(1):
            x = random.randint(0,2)
            y = random.randint(0,2)
            if(table[x][y] == ' '):
                table[x][y] = self.sign
                break