from .normalCostumer import NormalCostumer

class PromotionalCostumer(NormalCostumer):
    
    def __init__(self,username, password, saldo, nome, cognome, email, discount=5):
        super().__init__(username, password, saldo, nome, cognome, email)
        self.discount = discount

    def __str__(self):
        return super().__str__() + f",{self.discount}"
    
    def prezzo_scontato(self, prezzo):
        return prezzo -((prezzo*self.discount)/100)
    
    def modifyDisc(self, discount):
        self.discount = discount