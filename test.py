
#File
"""
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f :
        print(line.strip())

"""

# Esempio uso stringhe e variabili

""""
nome = "Alessandro"
eta = 22

messaggio = f"Ciao, sono {nome} e ho {eta} anni."
print(messaggio)

messaggio = f"Ciao sono {nome} e tra 5 anni avrò {eta+5} anni."
print(messaggio)

prezzo = 9.99
print(f"il prezzo è : {prezzo:.2f} euro")

print(f"Il nome maiuscolo è {nome.upper()}")

"""

#Parametri di default per funzioni
# --Posso passare anche più argomenti in modo sparso, non ordinato ma con assegnazione diretta : argomento=valore
""""
def saluta(nome="Mondo"):
    print(f"Ciao {nome}")

saluta("Alessandro")
saluta()

"""

# Liste  :
# Sono ordinate, modificabili e permettono valori duplicati 
"""
nomi = ["Alessandro", "Giulio", "Luca", "Alessandro"]
nomi.append(("Francesco"))
print(nomi)
nomi.remove("Alessandro") # elimina la prima occorrenza
print(nomi)
"""

# Tuple : 
# simili alle liste ma sono immutabili, non possono essere modificate dopo la creazione

"""
nomi = ("Alessandro", "Giulio", "Luca", "Alessandro")
print(nomi)
#nomi.remove("Alessandro")  questo darà un errore perché le tuple sono immutabili
# nomi[1] = "Francesco"     questo darà un errore perché le tuple sono immutabili
nomi = ("Mario", "aa", "aa") # posso creare una nuova tupla assegnando un nuovo valore alla variabile
print(nomi)
"""

# Set :
# sono collezioni non ordinatye, non indicizzate e non consentono duplicati
"""
nomi = {"Alessandro", "Giulio", "Luca"}
nomi.add("Patrizio")
print(nomi)
nomi.discard("Patrizio")
print(nomi)
print("Alessandro" in nomi) # verifica se un elemento è presente nel set    
"""

# Dizionari :
# memorizzano coppie chiave-valore, sono ordinati e modificabili
"""

studenti = {
    "00" : "Alessandro",
    "01" : "Giulio",
    "10" : "Luca",
    "11" : "Francesco"
}

studenti["111"] = "Patrizio" # aggiungo un nuovo elemento al dizionario

print(studenti)
del studenti["111"]
print(studenti)
"""

# Classi in python :
"""

class Animale :
    contatore = 0 # variabile di classe per contare il numero di istanze create

    def __init__(self, nome): # Costruttore
        self.nome=nome
        Animale.contatore += 1
    def parla(self):
        print(f"{self.nome} fa un verso")

    def __str__(self): #Metodo ridefinito per una stampa personalizzata
        return f"Animale chiamato : {self.nome}"
    
    @classmethod
    def get_contatore(cls):
        return f"Numero di oggetti creati : {cls.contatore}"

class Calcolatrice :
    @staticmethod
    def somma(a, b):
        return a + b
    

cane = Animale("Cane")
papera = Animale("Papera")
cane.parla()
print(cane)
papera.parla()
print(papera)
print(Animale.get_contatore())

# -- Campi Protetti e privati

    _nome_attributo : un singolo underscore si ottiente un campo protetto, per convenzione(comunque accessibile dall'esterno)
    __nome_attributo : un doppio underscore si ottiene un campo privato, che non è accessibile dall'esterno della classe (viene "mangiato" dal nome della classe)
class Animale :
    def __init__(self, nome, specie):
        self._nome = nome # campo protetto
        self.specie = specie
        
    def _suono(self):
        print("suono")
animale = Animale("Cane", "Mammifero")
print(animale._nome) # Accesso al campo protetto(non consigliato ma possibile)
# -------------------------------------------
class Banca :
    def __init__(self, nome, saldo):
        self.nome = nome # campo privato
        self.__saldo = saldo

    def deposita(self, import):
        if(importo>0):
            self.__saldo += importo
    def ottieni_saldo(self):
        retunr self.__saldo

conto = Banca("Ale", 1000)
conto.deposita(500)
print(conto.ottieni_saldo()) # ok
# print(conto.__saldo) Erroree !!
        
    

"""

# Ereditarietà

#Ereditare da piu classi
'''
class Mammifero:
    def fa_cose(self):
        print("Il mammifero fa un verso")

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print("L'animale fa un verso")

class Cane(Animale, Mammifero):
    def scodinzola(self):
        print(f"Il cane {self.nome} scodinzola")

fido = Cane("Fido")
print(fido.nome)
fido.parla()
fido.scodinzola()
fido.fa_cose()
'''

# Metodo super() : 
# permette di accedere ai metodi e attributi della superclasse da una sottoclasse, non viene chiamato automaticamente
# se non viene specificato __init__ in una sottoclasse, in automatico sara preso quello della superclasse
'''
class Animale:
    def __init__(self, nome):
        self.nome = nome
    def parla(self):
        print(f"{self.nome} fa un verso")

class Cane(Animale):
    def __init__(self, nome, razza):
        super.__init__(nome)
        self.razza = razza
        super().parla() # può essere usato per chiamare un metodo della superclasse
'''

# Classi Astratte :
# si usa il metodo abc, servono per definire un'interfaccia comune che deve essere implementata dalle sottoclassi
'''
Una classe astratta non può essere istanziata direttamente
Può contenere metodi implementati, o astratti, da completare nella sottoclasse @abstractmethod
'''
'''
from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato
    def area(self):
        return self.lato*2
    def perimetro(self):
        return self.lato*4

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    def area(self):
        return math.pi*self.raggio**2
    def perimetro(self):
        return 2*math.pi*self.raggio
    
q = Quadrato(5)
c = Cerchio(3)
'''

# Polimorfismo :
'''
È un concetto che permette di usare un interfaccia unica per diversi tipi di dati
Ovvero lo stesso metodo ridefinito con l'overriding può avere diversi comportamenti
a seconda dell'oggetto su cui viene chiamato
'''

#Funzione polimorfica :
'''
import math
class Rettangolo :
    def __init__(self, l, a):
        self.l = l
        self.a = a
    def area(self):
        return self.a*self.l
class Cerchio:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi*self.r**2
    
# funzione polimorfica che accetta un oggetto di tipo Forma e chiama il metodo area() senza preoccuparsi del tipo specifico dell'oggetto
def stampa_area(figura):
    print(f" L'area della figura è : {figura.area()}")


r = Rettangolo(4,5)
c = Cerchio(3)

stampa_area(r)
stampa_area(c)
'''

# Modifico comportamento operatore somma facendo overloading di __add__

'''
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
p1 = Punto(1,2)
p2 = Punto(3,4)
p3 = p1+p2
print(p3)

'''

# Overloading con *args che raccoglie gli arghomenti passati in una tupla
'''
class Matematica :
    def somma(self, *numeri):
        return sum(numeri)
    
n = Matematica()
print(n.somma(1,2,3,4,5))
print(n.somma(10,20))
'''

# Overloafing con **kwargs che li raccoglie in un dizionario
'''
class Persona :
    def __init__(self, **kwargs):
        self.nome = kwargs.get("nome", "Sconosciuto")
        self.eta = kwargs.get("eta", 0)
        self.citta = kwargs.get("citta", "Sconosciuta")

    def __str__(self):
        return f"nome : {self.nome}, eta : {self.eta}, citta : {self.citta}"

p1 = Persona(nome="Alessandro", eta=22)
p2 = Persona(nome="Giulio", citta="Roma")
print(p1)
print(p2)
'''

# Eccezioni :
'''
try :
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error : {e}")
finally:
    print("Operazione completata")
'''

'''
eta = 10
if(eta<18):
    raise ValueError("Devi essere maggiorenne !") # Lancia un'eccezione personalizzata
'''

# Funzioni lambda (anonime) :
'''

quadrato = lambda x : x**2
print(quadrato(5))

persone = [("Alessandro", 22), ("Giulio", 25), ("Luca", 20)]
persone_ordinate = sorted(persone, key=lambda x : x[1]) # ordina per età
print(persone_ordinate)
'''

# funzione Map
# map(funzione, iterabile) applica la funzione ad ogni elemento dell'iterabile
'''
numeri = [1,2,3,4,5]
raddoppia = list(map(lambda x:x**2, numeri))
print(raddoppia)
'''

# Funzione filter
# filter(funzione, iterabile) applica la funzione agli elementi dell'iterabile restituiendo solo quelli per cui la funzione restituisce True
'''
numeri = [1,2,3,4,5]
pari = list(filter(lambda x:x%2==0, numeri))
print(pari)
'''

# Funzione sorted
# restituisce una lista ordinata degli elementi di un iterabile, supporta ordinamento personalizzato tramite key
'''
parole = ["banana", "apple", "cherry", "date"]
numeri = [5,2,9,1,5,6]
ordinati = sorted(numeri)
par_ordinate = sorted(parole, key=len)
print(ordinati)
print(par_ordinate)
'''


# Type hinting
# permette di specificare i tipi di variabili, parametri e valori di ritorno delle funzioni
'''
def greet(name:str) -> str:
    return f"Ciao {name}!"

nome:str = "Alessandro"
age : int = 22
is_student : bool = True
print(greet(nome))
'''

# Strumenti più complessi del Typing
'''
from typing import List, Dict, Tuple, Union, Optional
from typing import Callable

def process_data(data: List[int], processor: Callable[[int], str]) ->List[str]: # Funzione che accetta una funzione come parametro
    return [processor(x) for x in data]

numbers: List[int] = [1,2,3,4,5]
scores : Dict[str, float] = {"Math": 90.5, "Science": 85.3}
person: Tuple[int, str] = (22, "Alessandro")
age: Optional[int] = None
identifier: Union[int, str] = "abc123"
'''

# Misurazione precisa del tempo
'''
import time
start_time = time.perf_counter() # tempo di inizio
# codice da misurare
p=0
for x in range(10000000):
    if(x%2==0):
        p += 1
    else : p+=2
end_time = time.perf_counter() # tempo di fine
elapsed_time = end_time - start_time
print(f"Tempo ascorso : {elapsed_time:.6f} secondi")

'''

# Matplotlib
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,5,7,11]    
plt.plot(x,y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Example Plot")

plt.show()
'''

