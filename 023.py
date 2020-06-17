num = int(input("Digite um numero de até 4 digitos: "))
un = num % 10
dez = num //10 % 10
cen = num //100 % 10
mil = num // 1000 % 10
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(un, dez, cen, mil))
