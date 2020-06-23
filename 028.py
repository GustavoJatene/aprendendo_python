import random
rand = random.randint(1, 5)
print("Escolha um número de 1 à 5")
print("-"*27)
nusr = int(input("Informe o numero:" ))
if rand == nusr:
    print("Parabéns, você acertou!")
else:
    print("Você errou o numero que pensei foi {}".format(rand))