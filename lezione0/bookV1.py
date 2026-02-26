class Book:
    def __init__(self, titolo, autore, anno, tipo):
        self.titolo = titolo
        self.autore = autore
        self.autore = anno
        self.tipo = tipo
    def str(self):
        return f"{self.titolo} | {self.autore} | {self.anno} | {self.tipo}"
class Library:
    def __init__(self, libro):
        self.libro = []

    def aggiungi_libro(self, libro):
        self.libro.apend(libro)

library = Library()
        