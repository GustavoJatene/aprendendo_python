num = cont = soma = 0
while True:
    num = int(input("Digite um numero ou 999 para encerrar: "))
    cont += 1
    if num == 999:
        break
    soma += num
print(f"Foram digitados {cont} numeros e a soma total é de {soma}")