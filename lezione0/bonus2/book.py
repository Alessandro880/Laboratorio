class Book:
    def __init__(self, titolo, autore, anno, tipo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.tipo = tipo
    def stampa(self):
        return f"{self.titolo} | {self.autore} | {self.anno} | {self.tipo}"  
      