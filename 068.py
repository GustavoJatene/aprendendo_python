import random
print("PAR OU IMPAR")
cont = 0
while True:
    print("-"*50)
    num = int(input("Insira um numero: "))
    esc = int(input("[1]PAR\n[2]IMPAR\nEfetue sua escolha: "))
    maquina = random.randint(0,10)
    total = num + maquina
    print(f"Seu numero foi {num} e o computador escolheu {maquina}, o total é {total}")
    if esc == 1:
        if total % 2 == 0:
            print("Você ganhou, deu PAR")
            cont += 1
        else:
            print("Você perdeu, deu IMPAR")
            cont += 1
            break
    elif esc == 2:
        if total % 2 == 0:
            print("Você perdeu, deu IMPAR")
            cont += 1
            break
        else:
            print("Você ganhou, deu PAR")
            cont += 1
print(f"Você jogou {cont} vezes e venceu {cont-1} vezes")