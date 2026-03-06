from .normalConsumer import NormalConsumer

class PromotionalConsumer(NormalConsumer):
    discount = 5
    def __init__(self, id, nome, cognome, email):
        super().__init__(id, nome, cognome, email)

    def __str__(self):
        return super().__str__() + f" (discount : {PromotionalConsumer.discount} % )"
    
    def prezzo_scontato(self, prezzo):
        return prezzo -((prezzo*PromotionalConsumer.discount)/100)