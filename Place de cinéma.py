place_de_cinema = 0

print("""Séléctionnez le film de votre choix:
      Film 1 - 7 euros
      Film 2 - 12 euros
      Film 3 - 10 euros""")

film = int(input("-> "))

if film == 1:
    place_de_cinema += 7
    print("5 euros")
elif film == 2:
    place_de_cinema += 12
    print("7 euros")
elif film == 3:
    place_de_cinema += 10
    print("6 euros")

age = int(input("Entrez votre âge: "))
if age < 18:
    place_de_cinema -= 3
else:
    pass

bon = input("Possédez vous un bon de réduction? (oui,non) ")
if bon == "oui":
    place_de_cinema -= int(input("Entrez la valeur à déduire du prix de la place: "))
    print(place_de_cinema," euros")
elif bon == "non":
    pass

ppc = input("Souhaitez-vous du popcorn? (oui,non)")
if ppc == "oui":
    dose = input("Souhaitez vous une dose simple ou une double dose? (simple,double)")
    if dose == "simple":
        place_de_cinema += 1
        print(place_de_cinema," euros")
    elif dose == "double":
        place_de_cinema += 2
        print(place_de_cinema," euros")
    else:
        pass
elif ppc == "non":
    print(place_de_cinema," euros")

print("Le prix total est de ",place_de_cinema," euros.")