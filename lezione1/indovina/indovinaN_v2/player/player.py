class Player :
    win:int = 0
    def __init__(self, name):
        self.name=name
        self.ntentativi = 0
        self.tentativi =[]

    def vittoria(self):
        Player.win += 1

    def nVittorie(self):
        return Player.win
    def __str__(self):
        return f"{self.name} ha vinto con {self.ntentativi} tentativi ! \n"