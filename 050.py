soma = 0
n = 0
for c in range(1,7):
    n = int(input("Digite o {}º numero: ".format(c)))
    if n%2==0:
        soma += n
print("A soma somente  dos numeros pares é: {}".format(soma))