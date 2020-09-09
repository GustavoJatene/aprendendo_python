n1 = int(input("Informe o primeiro termo: "))
n2 = int(input("Razão da PA: "))
res = 10
cont = 0
cont2 = int
sair = False
while not sair:
    while cont < res:
        print("{}".format(n1), end="-")
        n1 = n1 + n2
        cont = cont + 1
    print("STOP")
    cont = int(input("Quantos termo a mais você quer mostrar? "))
    if cont == 0:
        sair = True
    elif cont == 10:
        cont = 0
print("SAINDO")
'''
NÃO CONSEGUI FAZER DESAFIO COMPLETO, MAS SEGUE A RESPOSTA DO CURSO EM VÍDEO
primeiro = int(input("digite o primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}>".format(termo), end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
'''