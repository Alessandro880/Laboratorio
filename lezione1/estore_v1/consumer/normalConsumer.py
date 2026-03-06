from .genericConsumer import GenericConsumer
class NormalConsumer(GenericConsumer):
    def __init__(self,id, nome, cognome, email):
        super().__init__(id)
        self.nome = nome
        self.cognome = cognome
        self.email = email
    def __str__(self):
        return f"NormalCostumer (id : {self.id} , nome : {self.nome} , cognome : {self.cognome} , email : {self.email} )"
