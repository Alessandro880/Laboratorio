from .genericCostumer import GenericCostumer
class NormalCostumer(GenericCostumer):
    def __init__(self,id, saldo, nome, cognome, email):
        super().__init__(id, saldo)
        self.nome = nome
        self.cognome = cognome
        self.email = email
    def __str__(self):
        return f"NormalCostumer (id : {self.id} , nome : {self.nome} , cognome : {self.cognome} , email : {self.email} )"
