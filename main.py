# 14/9/2022   D/M/Y
# David A. Veilleux gr 405


def count_words(phrase):
    # on compte le nombre d'espaces et d'apostrophes
    espaces = (phrase.count(" "))
    apostrophe = (phrase.count("'"))

    # le nombre de mots est toujours 1 de plus que le nombre d'espaces et d'apostrophes
    # on trouve le nombre de mots
    return apostrophe + espaces + 1


# demande à l'utilisateur d'écrire une phrase. cette phrase sera enregistré comme un string sous la variable Count_Word
nombre_mots = count_words(input("Écris-moi une phrase. Je vais compter ses mots!\n--> "))

# le code dit a la personne le nombre de mots dans sa phrase
print(f"Le nombre de mots est {nombre_mots}!")
