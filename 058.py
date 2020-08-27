import random

nrand = random.randint(1, 10)
cont = 1
print("Tente acertar o numero que a máquina irá escolher...")
print("-"*60)
urand = int(input("Escolha um numero: "))
if nrand == urand:
    print("Parabéns, você acertou de primeira")
else:
    while nrand != urand:
        urand = int(input("Tenete novamente: "))
        cont = cont+1
    print("Você usou {} chances para acertar".format(cont))