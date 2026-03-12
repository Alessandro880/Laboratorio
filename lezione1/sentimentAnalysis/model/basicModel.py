from .model import Model

class BasicModel(Model):
    def __init__(self, name):
        super().__init__(name)

    def studia(self):
        lista = self.righe[:(len(self.righe)//2)]
        for x in lista:
            if(x[1] == "positiva\n"):
                self.positive+=1

        self.percentuale = (self.positive*100)/len(lista)
