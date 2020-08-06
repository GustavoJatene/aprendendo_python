pa = []
n = int(input("Infome um numero: "))
razao = int(input("Informe a razão: "))
for c in range (0,10):
    n += razao
    pa.append(n)
print("{}".format(pa))