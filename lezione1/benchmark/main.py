import time
import random
import matplotlib.pyplot as plt


# lista = []
# insieme = []

# for x in range(100):
#     l=[]
#     i = set()
#     n = random.randrange(300, 1000)
#     for y in range(n):
#         l.append(y)
#         i.add(y)
#     lista.append(l)
#     insieme.append(i)

# with open ("liste.tsv", "a", encoding="UTF-8") as f:

#     for l in lista:
#         for x in range(10):
#             n = random.randrange(0, 999)
#             timeStart = time.perf_counter()
#             if(n in l): pass
#             timeEnd = time.perf_counter()
#             t = timeEnd - timeStart
#             if(n in l):
#                 f.write(f"{t} \t {len(l)}\n")

# with open ("set.tsv", "a", encoding="UTF-8") as f:

#     for l in insieme:
#         for x in range(10):
#             n = random.randrange(0, 999)
#             timeStart = time.perf_counter()
#             if(n in l): pass
#             timeEnd = time.perf_counter()
#             t = timeEnd - timeStart
#             if(n in l):
#                 f.write(f"{t} \t {len(l)}\n")



tempoL =[]
elementiL = []

with open("liste.tsv", "r", encoding="UTF-8") as f:
    for r in f:
        el = r.strip().split("\t")
        tempoL.append(float(el[0]))
        elementiL.append(int(el[1]))
tempoL.sort()
elementiL.sort()
plt.plot(tempoL, elementiL, color='red', label="Ricerca liste")
plt.xlabel("X-tempo ricerca")
plt.ylabel("Y-numero Elementi")
plt.title("Benchmark")

tempoI = []
elementiI = []
with open("set.tsv", "r", encoding="UTF-8") as f:
    for r in f:
        el = r.strip().split("\t")
        tempoI.append(float(el[0]))
        elementiI.append(int(el[1]))
tempoI.sort()
elementiI.sort()
plt.plot(tempoI, elementiI, color='green', label='Ricerca insiemi')

plt.legend()
plt.show()


