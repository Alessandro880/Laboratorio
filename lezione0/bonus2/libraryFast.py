from book import Book

class LibraryFast:
    def __init__(self):
        self.libri_autore = {}
        self.libri_titolo = {}
    
    def aggiungi_libro(self, libro):
        if libro.autore not in self.libri_autore:
            self.libri_autore[libro.autore] = []
        self.libri_autore[libro.autore].append(libro)

        self.libri_titolo[libro.titolo] = libro
    def mostra_libri(self):
        for l in self.libri_titolo.values():
            print(l.stampa())
    
    def cerca_autore(self, autore_ricerca):
        if autore_ricerca in self.libri_autore:
            for libro in self.libri_autore[autore_ricerca]:
                print(libro.stampa())
        else :
            print("Autore non trovato!!\n")
    def cerca_titolo(self, titolo_ricerca):
        if titolo_ricerca in self.libri_titolo:
            print(self.libri_titolo[titolo_ricerca].stampa())
        else:
            print("Titolo non trovato!!\n")

    def rimuovi_libro(self, titolo):
        for tit in self.libri_autore:
            if(tit == titolo):  self.libri_autore.remove(titolo)
        self.libri_titolo.pop(titolo)