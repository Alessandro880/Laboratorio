from .genericCostumer import GenericCostumer
class NormalCostumer(GenericCostumer):
    def __init__(self,username, password, saldo, nome, cognome, email):
        super().__init__(username, password, saldo)
        self.nome = nome
        self.cognome = cognome
        self.email = email
    def __str__(self):
        return f"(username : {self.username} , nome : {self.nome} , cognome : {self.cognome} , email : {self.email} )"
