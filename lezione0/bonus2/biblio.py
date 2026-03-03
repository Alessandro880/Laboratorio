from book import Book
from library import Library
from libraryFast import LibraryFast
import time

#biblioteca = Library()
biblioteca = LibraryFast()

for i in range(10000):
    libro = Book(f"{i}", f"{i}", 2000+i, f"{i%10}")
    biblioteca.aggiungi_libro(libro)

letto = "-"
while letto != "quit" :

    letto = input("\nInserire un libro : 'i'\nVisualizza biblioteca : 'v'\nRicerca autore : 'ra'\nRicerca titolo : 'rt'\n\n Uscire : 'quit'\n\n")

    if(letto == "i"):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = input("Inserisci l'anno di pubblicazione del libro: ")
        tipo = input("Inserisci il tipo del libro (es. romanzo, saggio, ecc.): ")

        libro = Book(titolo, autore, anno, tipo)
        biblioteca.aggiungi_libro(libro)

    elif(letto == "v"):
        print("\n")
        biblioteca.mostra_libri()
        print("\n")

    elif(letto =="ra"):
        ric_a = input("Inserisci nome autore : ")
        biblioteca.cerca_autore(ric_a)

    elif(letto =="rt"):
        ric_t = input("Inserisci titolo libro : ")
        biblioteca.cerca_titolo(ric_t)

    elif(letto == "quit"):
        break