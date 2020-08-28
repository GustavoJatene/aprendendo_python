sair = False
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opc = int
maior = n1
while not sair:
    print("-" * 30)
    print("[1] Para SOMAR\n[2] Para MULTIPLICAR\n[3] Para MAIOR\n[4] Para NOVOS NUMEROS\n[5] Para SAIR")
    print("-" * 30)
    opc = int(input("Digite a opção: "))
    if opc == 1:
        print("-" * 30)
        print("A soma entre {} + {} é {}".format(n1,n2,n1+n2))
        print("-"*30)
    elif opc == 2:
        print("-" * 30)
        print("A multiplicação entre {} + {} é {}".format(n1, n2, n1 * n2))
        print("-" * 30)
    elif opc == 3:
        print("-" * 30)
        if n2 > maior:
            maior = n2
        print("O numero maior entre {} e {} é {}".format(n1, n2, maior))
        print("-" * 30)
    elif opc == 4:
        print("-" * 30)
        n1 = int(input("Digite um novo primeiro valor: "))
        n2 = int(input("Digite um novo segundo valor: "))
        print("-" * 30)
    else:
        print("Fazendo Logout")
        sair = True