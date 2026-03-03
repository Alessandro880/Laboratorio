from book import Book
from libraryFast import LibraryFast
import time
import os


biblioteca = LibraryFast()

for i in range(20):
    libro = Book(f"{i}", f"{i}", 2000+i, f"{i%10}")
    biblioteca.aggiungi_libro(libro)

letto = "-"
while letto != "quit" :
    letto = input("\n- Inserire un libro : 'i'\n- Visualizza biblioteca : 'v'\n- Ricerca autore : 'ra'\n- Ricerca titolo : 'rt'\n- Rimuovere un libro : 'remL'\n\n- Uscire : 'quit'\n\n")

    if(letto == "i"):
        os.system('clear')
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = input("Inserisci l'anno di pubblicazione del libro: ")
        tipo = input("Inserisci il tipo del libro (es. romanzo, saggio, ecc.): ")

        libro = Book(titolo, autore, anno, tipo)
        biblioteca.aggiungi_libro(libro)

    elif(letto == "v"):
        os.system('clear')
        print("\n")
        biblioteca.mostra_libri()
        print("\n")

    elif(letto =="ra"):
        os.system('clear')
        ric_a = input("Inserisci nome autore : ")
        biblioteca.cerca_autore(ric_a)

    elif(letto =="rt"):
        os.system('clear')
        ric_t = input("Inserisci titolo libro : ")
        biblioteca.cerca_titolo(ric_t)

    elif(letto=="remL"):
        os.system('clear')
        rem_t = input("Inserisci titolo libro da rimuovere : ")
        biblioteca.rimuovi_libro(rem_t)
    elif(letto == "quit"):
        break
    else : 
        print("Comando non riconosciuto !! \n")
        time.sleep(1)
        os.system('clear')
