import random

n1 = input("Nome do primeiro aluno: ")
n2 = input("Nome do segundo aluno: ")
n3 = input("Nome do terceiro aluno: ")
n4 = input("Nome do quarto aluno: ")
# lista = [n1,n2,n3,n4] pode criar uma lista
# escolha = random.choice(lista) e usar a função random pra embaralhar, no print, basta colocar a variável declarada aqui
print("O nome sorteado é {}.".format(random.choice([n1,n2,n3,n4])))