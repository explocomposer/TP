statue = True

def get_vowels(word):

    number = 0

    for letter in word:
        if letter in ["A","E","I","O","U","a","e","i","o","u"]:
            number += 1
    return number

while statue:
    word = input("Entrez un mot: ")
    nb_vowels = get_vowels(word)
    print("Il y a",nb_vowels," voyelles dans le mot.")