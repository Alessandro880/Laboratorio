class GenericCostumer :
    def __init__(self, id, saldo:int = 0):
        self.id = id
        self.__saldo=saldo
    def __str__(self):
        return f"(id : {self.id} )"
    def saldoAttuale(self)->int:
        return self.__saldo