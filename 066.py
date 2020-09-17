num = cont = soma = 0
while True:
    num = int(input("Digite um numero ou 999 para encerrar: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"Foram digitados {cont} numeros e a soma total é de {soma}")