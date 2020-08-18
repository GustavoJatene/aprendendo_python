nome = str
sexo = ""
idade = int
media = 0
contador = 0
mvelho = 0
nvelho = ""
contf = 0
for c in range(1,5):
    print("{}° Pessoa".format(c))
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite o sexo, [M]/[F]: ")).upper()
    contador = contador+1
    media += idade
    if idade > mvelho:
        nvelho = nome
        mvelho = idade
    if sexo == "F" and idade<20:
        contf = contf+1
print("A média de idade das pessoas é: {} anos".format((media)/contador))
print("A pessoa mais velha se chama {} e tem {} anos".format(nvelho,mvelho))
print("Existem apenas {} mulheres menores de 20 anos".format(contf))