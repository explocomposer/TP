from random import randrange

argent = int(input("Entrez votre somme d'argent initiale : \n>>> "))
running = True

while running:
    nb_mise = int(input("Choisissez un nombre sur lequel miser entre 0 et 49 : \n>>> "))
    mise = int(input("Choisissez un montant à miser : \n>>> "))
    argent -= mise
    roulette = randrange(50)
    print("La roulete tourne... Et le numéro gagnant est le",roulette,"!")
    if nb_mise == roulette:
        mise *= 3
        argent += mise
        print("Vous avez gagné ! Vous possédez maintenant",argent,"$!")
    elif nb_mise % 2 == roulette % 2:
        mise %= 2
        argent += mise
        print("Vous avez misé sur la bonne couleur, vous possédez maintenant",argent,"$.")
    else:
        print("Vous avez perdu... Vous possédez maintenant",argent,"$.")
        if argent < 1:
            running = False
            print("Fin du jeu")
