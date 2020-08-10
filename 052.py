n = int(input("Digite um numero: "))
cont = 0
for c in range(1,n+1):
    if n%c==0:
        print("{}".format(c), end=" ")
        cont += 1
print("\nO numero é {} foi divisivel {} vezes".format(n, cont))
if cont == 2:
    print("Portanto, é primo")
else:
    print("Portanto, não é primo")
