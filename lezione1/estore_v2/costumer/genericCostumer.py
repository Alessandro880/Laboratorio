class GenericCostumer :
    def __init__(self, username, password, saldo:int = 0):
        self.username = username
        self.__saldo=saldo
        self.__password = password
    def __str__(self):
        return f"(username : {self.username} )"
    def saldoAttuale(self)->int:
        return self.__saldo
    def decrementaSaldo(self, amount:float):
        self.__saldo -= amount
    def incrementaSaldo(self, amount:float):
        self.__saldo += amount
    def checkPassword(self, password):
        return self.__password == password