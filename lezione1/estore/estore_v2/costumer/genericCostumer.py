class GenericCostumer :
    def __init__(self, username, password, saldo:int = 0):
        self.username = username
        self.__saldo=saldo
        self.__password = password
    def __str__(self):
        s = self.username + "," + self.__password + "," + str(self.__saldo)
        return s
    def saldoAttuale(self)->int:
        return self.__saldo
    def decrementaSaldo(self, amount:float):
        self.__saldo -= amount
    def incrementaSaldo(self, amount:float):
        self.__saldo += amount
    def checkPassword(self, password):
        return self.__password == password