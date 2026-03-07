from .normalCostumer import NormalCostumer

class PromotionalCostumer(NormalCostumer):
    discount = 5
    def __init__(self, id, saldo, nome, cognome, email):
        super().__init__(id, saldo, nome, cognome, email)

    def __str__(self):
        return super().__str__() + f" (discount : {PromotionalCostumer.discount} % )"
    
    def prezzo_scontato(self, prezzo):
        return prezzo -((prezzo*PromotionalCostumer.discount)/100)