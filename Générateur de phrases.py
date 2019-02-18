from random import shuffle #importation du module

word = input("Entrez une suite de mots sous la forme(mot1-mot2-mot3)").split("-") # entrer une chaîne de caractère
shuffle(word) # mélanger la chaîne
print(word)
word_len = len(word) # transformation de la chaîne en liste

if word_len < 10:
    print(word[0],word[1]) # afficher un élément de la chaîne en l'identifiant par sa place dans la liste
else:
    print(word[word_len -1],word[word_len -2],word[word_len -3]) # afficher les trois derniers éléments de la chaîne
