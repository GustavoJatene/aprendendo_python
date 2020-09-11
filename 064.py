soma = 0
num = int
cond = False
cont = 0

while not cond:
    num = int(input("Digite um valor: "))
    cont += 1
    soma += num
    if num == 999:
        cond = True
        cont -= 1
        soma -= 999
print("Foram digitados {} numeros e a soma deles é {}".format(cont, soma))