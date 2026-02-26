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
    while True:
        letto = input("\nVuoi inserire un altro libro? digita 'add' \nVuoi visualizzare tutti i libri? digita 'vis' \nRicerca libro per autore ? digita 'ricA'\nRicerca per titolo? digita 'ricT'\n\n(digita 'quit' per uscire): ")
        if(letto == "add" or letto=="quit") :
            break
        elif(letto=="vis"):
            print("\n")
            biblioteca.mostra_libri()
            print("\n")
        elif(letto=="ricA"):
            autore_ricerca = input("Inserisci l'autore da cercare: ")
            print("\n")
            trovato=0
            for libro in biblioteca.libri:
                if libro.autore == autore_ricerca:
                    print(libro.stampa())
                    trovato=1
            if(trovato==0):
                print("Autore non trovato!!\n")
            print("\n")
        elif(letto=="ricT"):
            ricerca_titolo = input("Inserisci titolo libro : ")
            print("\n")
            trovato=0
            for l in biblioteca.libri : 
                if(l.titolo == ricerca_titolo):
                    print(l.stampa())
                    trovato=1
            if(trovato==0):
                print("Titolo non trovato!!\n")
            print("\n")

