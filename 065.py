sair = "n"
num = int
maior = 0
menor = 0
cont = 0
soma = 0
media = int
while sair != "s":
    num = int(input("Digite um numero: "))
    sair = str(input("Quer continuar? [S/N]: ")).upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if sair == "N":
        sair = "s"
    media = soma/cont
print("Você digitou {} numeros e a média total é {}\nO maior numero é {} e o menor é {}".format(cont, media, maior, menor))