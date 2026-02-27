from book import Book
from library import Library


biblioteca = Library()

for i in range(100000):
    libro = Book(f"{i}", f"{i}", 2000+i, f"{i%10}")
    biblioteca.aggiungi_libro(libro)

biblioteca.mostra_libri()

print("\n\nRicerca per autore\n")
cerca_a = input("Inserisci autore da cercare : ")

biblioteca.cerca_autore(cerca_a)
print("\n\nRicerca per titolo\n")
cerca_t = input("Inserisci titolo da cercare : ")
biblioteca.cerca_titolo(cerca_t)