from book import Book
from library import Library
from libraryFast import LibraryFast
import time

#biblioteca = Library()
biblioteca = LibraryFast()

for i in range(10000):
    libro = Book(f"{i}", f"{i}", 2000+i, f"{i%10}")
    biblioteca.aggiungi_libro(libro)


print("\n\nRicerca per autore\n")
cerca_a = input("Inserisci autore da cercare : ")

inizio = time.perf_counter()
biblioteca.cerca_autore(cerca_a)
fine = time.perf_counter()
tempo = fine-inizio
print(f"Tempo impiegato per cercare autore : {tempo:.8f} secondi\n")

print("\n\nRicerca per titolo\n")
cerca_t = input("Inserisci titolo da cercare : ")

inizio = time.perf_counter()
biblioteca.cerca_titolo(cerca_t)
fine = time.perf_counter()
tempo = fine-inizio
print(f"Tempo impiegato per cercare titolo : {tempo:.8f} secondi\n")
