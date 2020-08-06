print("Calculo de uma Progressão aritmética")
n = int(input("Infome um numero: "))
cont = 0
razao = int(input("Informe a razão: "))
for c in range (n,10*razao):
    print("{}".format(n),end=",")
    n = n+razao
    cont+=1
    if cont == 10:
        break
print("FINISH")

'''
primeiro = int(input("Infome um numero: "))
razao = int(input("Informe a razão: "))
decimo = n +(10-1)*razão
for c in range (primeiro,decimo+razao, razao):
    print("{}".format(c),end=",")
print("FINISH")
SOLUÇÃO DO GUANABARA, A SOLUÇÃO ANTERIOR FOI A QUE ENCONTREI
'''