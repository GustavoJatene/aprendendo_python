n1 = int(input("Informe o primeiro termo: "))
n2 = int(input("Razão da PA: "))
cont = 0
while cont < 10:
    print("{}".format(n1), end="-")
    n1 = n1+n2
    cont = cont + 1
if cont == 10:
    print(end="FIM")