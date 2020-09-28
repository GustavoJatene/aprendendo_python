num = cont = res = 0
while True:
    print("-" * 50)
    num = int(input("Digite um valor para ver a tabuada: "))
    print("-" * 50)
    if num > 0:
        for cont in range(0,11):
            res = num * cont
            print(f"{cont} * {num} = {res}")
    else:
        print("SAINDO")
        break