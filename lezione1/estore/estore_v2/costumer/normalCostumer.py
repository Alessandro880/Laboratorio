from .genericCostumer import GenericCostumer
class NormalCostumer(GenericCostumer):
    def __init__(self,username, password, saldo, nome, cognome, email):
        super().__init__(username, password, saldo)
        self.nome = nome
        self.cognome = cognome
        self.email = email
    def __str__(self):
        s = super().__str__()
        return s+f",{self.nome},{self.cognome},{self.email}"
