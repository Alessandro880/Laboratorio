class Library:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    def mostra_libri(self):
        for l in self.libri:
            print(l.stampa())
    def cerca_autore(self, autore_ricerca):
        trovato=0
        for l in self.libri :
            if(l.autore == autore_ricerca):
                print(l.stampa())
                trovato=1
        if(trovato==0):
            print("Autore non trovato!!\n")
    def cerca_titolo(self, titolo_ricerca):
        trovato=0
        for l in self.libri :
            if(l.autore == titolo_ricerca):
                print(l.stampa())
                trovato=1
        if(trovato==0):
            print("Titolo non trovato!!\n")
