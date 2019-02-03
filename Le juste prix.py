from random import randint

nb = randint(1, 1000)

running = True

while running:
    price = int(input("Entrez un prix: "))
    if price == nb:
        print("C'est gagné!")
        running = False
        print("Fin du jeu")
    elif price < nb:
        print("C'est plus!")
    elif price > nb:
        print("C'est moins!")



# Choisir un nombre entre 1 et 1000
# Tant que le jeu n'est pas finit
# Demander à l'utilisateur "Entrez un prix"
# Si il trouve le juste prix : "C'est gagné !
# Sinon afficher "c'est plus" ou "c'est moins"