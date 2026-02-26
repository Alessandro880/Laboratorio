class Book:
    def __init__(self, titolo, autore, anno, tipo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.tipo = tipo
    def stampa(self):
        return f"{self.titolo} | {self.autore} | {self.anno} | {self.tipo}"  
      
class Library:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    def mostra_libri(self):
        for l in self.libri:
            print(l.stampa())


letto = "-"
biblioteca  = Library()
while(letto != "quit"):
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    anno = input("Inserisci l'anno di pubblicazione del libro: ")
    tipo = input("Inserisci il tipo del libro (es. romanzo, saggio, ecc.): ")

    libro = Book(titolo, autore, anno, tipo)
    biblioteca.aggiungi_libro(libro)

    letto = input("Vuoi inserire un altro libro? (digita 'quit' per uscire): ")

biblioteca.mostra_libri()