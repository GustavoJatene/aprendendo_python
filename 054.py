from datetime import date
lista = [] #lista vazia para armazenar os anos
anoa = date.today().year
idade = 0
maior, menor = 0,0
for n in range(1,8):
    ano = int(input("Digite o {}º ano de nascimento: ".format(n)))
    idade = anoa-ano
    lista.append(ano) #estou armazenando os anos, caso seja preciso de consultas posteriores
    if idade > 18:
        maior += 1
    else:
        menor += 1
print("Total de menores de idade: {}".format(menor))
print("Total de meiores de idade: {}".format(maior))