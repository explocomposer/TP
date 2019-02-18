# Définir les variables capital, taux, année, capital_objectif
# Tant que capital < capital objectif : alors capital augmente de capital * 1 + taux / 100 puis année augmente de 1
# Retourner l'année où le capital objectif est atteint

capital = float(input("Entrez un capital: "))
taux = float(input("Entrez un taux: "))
capital_objectif = float(input("Entrez un objectif de capital: "))
année = int(input("Entrez l'année du placement: "))

def cap():
    global capital
    capital *= taux / 100 + 1

while capital < capital_objectif:
    cap()
    année += 1

print("L'année à laquelle le capital objectif est atteint est l'année",année)
