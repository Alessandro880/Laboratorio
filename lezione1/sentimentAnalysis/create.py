import csv
import random

# Frasi costruite usando le parole delle tue liste!
pos_reviews = [
    "I loved this product, it is excellent.",
    "Very happy with this, good job.",
    "A fantastic and wonderful experience.",
    "Great quality, I love it.",
    "This is so good, excellent work.",
    "I loved the design, really great.",
    "A wonderful item, I am happy.",
    "Fantastic service, good people."
]

neg_reviews = [
    "This is really bad, I am sad.",
    "Terrible quality, poor materials.",
    "I hate this, it is terrible.",
    "A sad experience, really poor.",
    "I hated the service, bad job.",
    "Terrible and poor, I hate it."
]

# Prima metà (50 recensioni: 35 positive, 15 negative -> 70% positive)
mazzo_1 = [ [random.choice(pos_reviews), "positiva"] for _ in range(35) ] + \
          [ [random.choice(neg_reviews), "negativa"] for _ in range(15) ]
random.shuffle(mazzo_1) # Mischiamo l'ordine

# Seconda metà (50 recensioni: 35 positive, 15 negative -> 70% positive)
mazzo_2 = [ [random.choice(pos_reviews), "positiva"] for _ in range(35) ] + \
          [ [random.choice(neg_reviews), "negativa"] for _ in range(15) ]
random.shuffle(mazzo_2) # Mischiamo l'ordine

# Uniamo i mazzi per formare il file da 100 recensioni
dataset = mazzo_1 + mazzo_2

# Scriviamo il file TSV usando il tab ('\t')
with open("recensioni.tsv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter='\t') 
    
    # Riga di intestazione
    writer.writerow(["text", "label"])
    
    # Scriviamo i dati
    writer.writerows(dataset)

print("File 'test_70_30.tsv' creato con successo!")
print("Totale: 100 recensioni (70 positive, 30 negative)")