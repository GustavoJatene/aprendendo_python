n = int(input("Digite um numero: "))
op = int(input("[1]SOMA\n[2]SUBTRAÇÃO\n[3]MULTIPLICAÇÃO\n[4]DIVISÃO\nTecle sua opção: "))
resultado = 0
if op == 1:
    print("TABUADA DE SOMA")
    for c in range(0,11):
        resultado = n + c
        print("{} + {} = {}".format(n, c, resultado))
elif op == 2:
    print("TABUADA DE SUBTRAÇÃO")
    for c in range(0,11):
        resultado = n - c
        print("{} - {} = {}".format(n, c, resultado))
elif op == 3:
    print("TABUADA DE MULTIPLICAÇÃO")
    for c in range(0,11):
        resultado = n * c
        print("{} x {} = {}".format(n, c, resultado))
else:
    print("TABUADA DE DIVISÃO")
    for c in range(0,11):
        resultado = n / c
        print("{} / {} = {}".format(n, c, resultado))