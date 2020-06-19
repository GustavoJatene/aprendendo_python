fra = str(input("Escreva uma frase: ")).strip()
print("A letra 'A' aparece {} vezes.".format(fra.lower().count("a")))
print("A primeira letra aparece na {} posição.".format(fra.lower().find("a")))
print("A última letra 'A' aparece na {} posição.".format(fra.lower().rfind("a")))